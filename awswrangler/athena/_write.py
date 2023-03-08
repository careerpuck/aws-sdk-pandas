"""Amazon Athena Module gathering all write functions."""

import logging
from typing import Any, Dict, List, Optional

import boto3

from awswrangler import catalog, exceptions
from awswrangler._config import apply_configs
from awswrangler.athena._utils import (
    _QUERY_WAIT_POLLING_DELAY,
    _get_query_metadata,
    _get_s3_output,
    _get_workgroup_config,
    _QueryMetadata,
    _start_query_execution,
    _substitute_sql_params,
    _WorkGroupConfig,
)

_logger: logging.Logger = logging.getLogger(__name__)


def _create_insert_into_query(sql: str, table: str, database: str) -> str:
    fully_qualified_name = f'"{database}"."{table}"'

    insert_sql = f"INSERT INTO {fully_qualified_name}\n" f"{sql}"
    _logger.debug("insert into sql: %s", insert_sql)
    return insert_sql


@apply_configs
def insert_into(
    sql: str,
    table: str,
    database: str,
    mode: Optional[str] = None,
    partitions_values: Optional[List[List[str]]] = None,
    data_source: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
    s3_output: Optional[str] = None,
    workgroup: Optional[str] = None,
    encryption: Optional[str] = None,
    kms_key: Optional[str] = None,
    boto3_session: Optional[boto3.Session] = None,
    athena_query_wait_polling_delay: float = _QUERY_WAIT_POLLING_DELAY,
) -> None:
    if mode not in ("append", "overwrite", "overwrite_partitions"):
        raise exceptions.InvalidArgumentValue(
            "Mode must be one of (\"append\", \"overwrite\", \"overwrite_partitions\")"
        )

    wg_config: _WorkGroupConfig = _get_workgroup_config(session=boto3_session, workgroup=workgroup)
    s3_output = _get_s3_output(s3_output=s3_output, wg_config=wg_config, boto3_session=boto3_session)
    s3_output = s3_output[:-1] if s3_output[-1] == "/" else s3_output

    insert_sql = _create_insert_into_query(sql=_substitute_sql_params(sql, params), table=table, database=database)
    _logger.debug("insert_sql: %s", insert_sql)

    if mode == "overwrite":
        partitions_values = catalog.delete_all_partitions(
            table=table,
            database=database,
            boto3_session=boto3_session,
        )
        _logger.debug("deleted partitions: %s", partitions_values)
    if mode == "overwrite_partitions":
        if not partitions_values:
            raise exceptions.InvalidArgumentCombination(
                'Must provide `partitions_values` in mode="overwrite_partitions"'
            )
        catalog.delete_partitions(
            table=table,
            database=database,
            partitions_values=partitions_values,
            boto3_session=boto3_session,
        )

    query_id: str = _start_query_execution(
        sql=insert_sql,
        wg_config=wg_config,
        database=database,
        data_source=data_source,
        s3_output=s3_output,
        workgroup=workgroup,
        encryption=encryption,
        kms_key=kms_key,
        boto3_session=boto3_session,
    )
    _logger.debug("query_id: %s", query_id)
    query_metadata: _QueryMetadata = _get_query_metadata(
        query_execution_id=query_id,
        boto3_session=boto3_session,
        athena_query_wait_polling_delay=athena_query_wait_polling_delay,
    )
    _logger.debug("query metadata: %s", query_metadata)
