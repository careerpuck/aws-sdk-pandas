# noqa: D100
from typing import TYPE_CHECKING, Any, Dict, Iterator, List, Literal, Optional, Tuple, Type, Union, overload

import boto3
import pyarrow as pa

import awswrangler.pandas as pd

if TYPE_CHECKING:
    try:
        import pymysql
    except ImportError:
        pass

def connect(  # noqa: D103
    connection: Optional[str] = ...,
    secret_id: Optional[str] = ...,
    catalog_id: Optional[str] = ...,
    dbname: Optional[str] = ...,
    boto3_session: Optional[boto3.Session] = ...,
    read_timeout: Optional[int] = ...,
    write_timeout: Optional[int] = ...,
    connect_timeout: int = ...,
    cursorclass: Optional[Type["pymysql.cursors.Cursor"]] = ...,
) -> "pymysql.connections.Connection[Any]": ...
@overload
def read_sql_query(
    sql: str,
    con: "pymysql.connections.Connection[Any]",
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
    con: "pymysql.connections.Connection[Any]",
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
    con: "pymysql.connections.Connection[Any]",
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
    con: "pymysql.connections.Connection[Any]",
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
    con: "pymysql.connections.Connection[Any]",
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
    con: "pymysql.connections.Connection[Any]",
    *,
    schema: Optional[str] = ...,
    index_col: Optional[Union[str, List[str]]] = ...,
    params: Optional[Union[List[Any], Tuple[Any, ...], Dict[Any, Any]]] = ...,
    chunksize: Optional[int],
    dtype: Optional[Dict[str, pa.DataType]] = ...,
    safe: bool = ...,
    timestamp_as_object: bool = ...,
) -> Union[pd.DataFrame, Iterator[pd.DataFrame]]: ...

_ToSqlModeLiteral = Literal[
    "append", "overwrite", "upsert_replace_into", "upsert_duplicate_key", "upsert_distinct", "ignore"
]

def to_sql(  # noqa: D103
    df: pd.DataFrame,
    con: "pymysql.connections.Connection[Any]",
    table: str,
    schema: str,
    mode: _ToSqlModeLiteral = ...,
    index: bool = ...,
    dtype: Optional[Dict[str, str]] = ...,
    varchar_lengths: Optional[Dict[str, int]] = ...,
    use_column_names: bool = ...,
    chunksize: int = ...,
    cursorclass: Optional[Type["pymysql.cursors.Cursor"]] = ...,
) -> None: ...
