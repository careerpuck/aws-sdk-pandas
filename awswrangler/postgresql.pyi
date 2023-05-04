# noqa: D100
from ssl import SSLContext
from typing import TYPE_CHECKING, Any, Dict, Iterator, List, Literal, Optional, Tuple, Union, overload

import boto3
import pandas as pd
import pyarrow as pa

if TYPE_CHECKING:
    try:
        import pg8000
    except ImportError:
        pass

_ToSqlModeLiteral = Literal["append", "overwrite", "upsert"]

def connect(  # noqa: D103
    connection: Optional[str] = ...,
    secret_id: Optional[str] = ...,
    catalog_id: Optional[str] = ...,
    dbname: Optional[str] = ...,
    boto3_session: Optional[boto3.Session] = ...,
    ssl_context: Optional[Union[bool, SSLContext]] = ...,
    timeout: Optional[int] = ...,
    tcp_keepalive: bool = ...,
) -> "pg8000.Connection": ...
@overload
def read_sql_query(
    sql: str,
    con: "pg8000.Connection",
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
    con: "pg8000.Connection",
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
    con: "pg8000.Connection",
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
    con: "pg8000.Connection",
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
    con: "pg8000.Connection",
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
    con: "pg8000.Connection",
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
    con: "pg8000.Connection",
    table: str,
    schema: str,
    mode: _ToSqlModeLiteral = ...,
    index: bool = ...,
    dtype: Optional[Dict[str, str]] = ...,
    varchar_lengths: Optional[Dict[str, int]] = ...,
    use_column_names: bool = ...,
    chunksize: int = ...,
    upsert_conflict_columns: Optional[List[str]] = ...,
    insert_conflict_columns: Optional[List[str]] = ...,
) -> None: ...
