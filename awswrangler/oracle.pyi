# noqa: D100
from typing import TYPE_CHECKING, Any, Dict, Iterator, List, Literal, Optional, Tuple, Union, overload

import boto3
import pandas as pd
import pyarrow as pa

if TYPE_CHECKING:
    try:
        import oracledb
    except ImportError:
        pass

def connect(  # noqa: D103
    connection: Optional[str] = ...,
    secret_id: Optional[str] = ...,
    catalog_id: Optional[str] = ...,
    dbname: Optional[str] = ...,
    boto3_session: Optional[boto3.Session] = ...,
    call_timeout: Optional[int] = ...,
) -> "oracledb.Connection": ...
@overload
def read_sql_query(
    sql: str,
    con: "oracledb.Connection",
    index_col: Optional[Union[str, List[str]]] = ...,
    params: Optional[Union[List[Any], Tuple[Any, ...], Dict[Any, Any]]] = ...,
    chunksize: None = ...,
    dtype: Optional[Dict[str, pa.DataType]] = ...,
    safe: bool = ...,
    timestamp_as_object: bool = ...,
) -> pd.DataFrame: ...
@overload
def read_sql_query(
    sql: str,
    con: "oracledb.Connection",
    *,
    index_col: Optional[Union[str, List[str]]] = ...,
    params: Optional[Union[List[Any], Tuple[Any, ...], Dict[Any, Any]]] = ...,
    chunksize: int,
    dtype: Optional[Dict[str, pa.DataType]] = ...,
    safe: bool = ...,
    timestamp_as_object: bool = ...,
) -> Iterator[pd.DataFrame]: ...
@overload
def read_sql_query(
    sql: str,
    con: "oracledb.Connection",
    *,
    index_col: Optional[Union[str, List[str]]] = ...,
    params: Optional[Union[List[Any], Tuple[Any, ...], Dict[Any, Any]]] = ...,
    chunksize: Optional[int],
    dtype: Optional[Dict[str, pa.DataType]] = ...,
    safe: bool = ...,
    timestamp_as_object: bool = ...,
) -> Union[pd.DataFrame, Iterator[pd.DataFrame]]: ...
@overload
def read_sql_table(
    table: str,
    con: "oracledb.Connection",
    schema: Optional[str] = ...,
    index_col: Optional[Union[str, List[str]]] = ...,
    params: Optional[Union[List[Any], Tuple[Any, ...], Dict[Any, Any]]] = ...,
    chunksize: None = ...,
    dtype: Optional[Dict[str, pa.DataType]] = ...,
    safe: bool = ...,
    timestamp_as_object: bool = ...,
) -> pd.DataFrame: ...
@overload
def read_sql_table(
    table: str,
    con: "oracledb.Connection",
    *,
    schema: Optional[str] = ...,
    index_col: Optional[Union[str, List[str]]] = ...,
    params: Optional[Union[List[Any], Tuple[Any, ...], Dict[Any, Any]]] = ...,
    chunksize: int,
    dtype: Optional[Dict[str, pa.DataType]] = ...,
    safe: bool = ...,
    timestamp_as_object: bool = ...,
) -> Iterator[pd.DataFrame]: ...
@overload
def read_sql_table(
    table: str,
    con: "oracledb.Connection",
    *,
    schema: Optional[str] = ...,
    index_col: Optional[Union[str, List[str]]] = ...,
    params: Optional[Union[List[Any], Tuple[Any, ...], Dict[Any, Any]]] = ...,
    chunksize: Optional[int],
    dtype: Optional[Dict[str, pa.DataType]] = ...,
    safe: bool = ...,
    timestamp_as_object: bool = ...,
) -> Union[pd.DataFrame, Iterator[pd.DataFrame]]: ...
def to_sql(  # noqa: D103
    df: pd.DataFrame,
    con: "oracledb.Connection",
    table: str,
    schema: str,
    mode: Literal["append", "overwrite", "upsert"] = ...,
    index: bool = ...,
    dtype: Optional[Dict[str, str]] = ...,
    varchar_lengths: Optional[Dict[str, int]] = ...,
    use_column_names: bool = ...,
    primary_keys: Optional[List[str]] = ...,
    chunksize: int = ...,
) -> None: ...
def detect_oracle_decimal_datatype(cursor: Any) -> Dict[str, pa.DataType]: ...  # noqa: D103
def handle_oracle_objects(  # noqa: D103
    col_values: List[Any], col_name: str, dtype: Optional[Dict[str, pa.DataType]] = None
) -> List[Any]: ...
