from typing import Any

from django.db import models
from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.models import Func, Transform
from django.db.models.expressions import Combinable, Expression, Value
from django.db.models.sql.compiler import SQLCompiler, _AsSqlType

class MySQLSHA2Mixin:
    def as_mysql(self, compiler: SQLCompiler, connection: BaseDatabaseWrapper, **extra_context: Any) -> _AsSqlType: ...

class OracleHashMixin:
    def as_oracle(self, compiler: SQLCompiler, connection: BaseDatabaseWrapper, **extra_context: Any) -> _AsSqlType: ...

class PostgreSQLSHAMixin:
    def as_postgresql(
        self, compiler: SQLCompiler, connection: BaseDatabaseWrapper, **extra_context: Any
    ) -> _AsSqlType: ...

class Chr(Transform):
    def as_mysql(self, compiler: SQLCompiler, connection: BaseDatabaseWrapper, **extra_context: Any) -> _AsSqlType: ...
    def as_oracle(self, compiler: SQLCompiler, connection: BaseDatabaseWrapper, **extra_context: Any) -> _AsSqlType: ...
    def as_sqlite(self, compiler: SQLCompiler, connection: BaseDatabaseWrapper, **extra_context: Any) -> _AsSqlType: ...

class ConcatPair(Func):
    def coalesce(self) -> ConcatPair: ...
    def as_sqlite(self, compiler: SQLCompiler, connection: BaseDatabaseWrapper, **extra_context: Any) -> _AsSqlType: ...
    def as_mysql(self, compiler: SQLCompiler, connection: BaseDatabaseWrapper, **extra_context: Any) -> _AsSqlType: ...

class Concat(Func):
    def __init__(self, *expressions: Any, **extra: Any) -> None: ...

class Left(Func):
    output_field: models.CharField
    def __init__(self, expression: Expression | str, length: Expression | int, **extra: Any) -> None: ...
    def get_substr(self) -> Substr: ...
    def as_oracle(self, compiler: SQLCompiler, connection: BaseDatabaseWrapper, **extra_context: Any) -> _AsSqlType: ...
    def as_sqlite(self, compiler: SQLCompiler, connection: BaseDatabaseWrapper, **extra_context: Any) -> _AsSqlType: ...

class Length(Transform):
    output_field: models.IntegerField
    def as_mysql(self, compiler: SQLCompiler, connection: BaseDatabaseWrapper, **extra_context: Any) -> _AsSqlType: ...

class Lower(Transform): ...

class LPad(Func):
    output_field: models.CharField
    def __init__(
        self, expression: Expression | str, length: Expression | int | None, fill_text: Expression = ..., **extra: Any
    ) -> None: ...

class LTrim(Transform): ...
class MD5(OracleHashMixin, Transform): ...

class Ord(Transform):
    output_field: models.IntegerField
    def as_sqlite(self, compiler: SQLCompiler, connection: BaseDatabaseWrapper, **extra_context: Any) -> _AsSqlType: ...
    def as_mysql(self, compiler: SQLCompiler, connection: BaseDatabaseWrapper, **extra_context: Any) -> _AsSqlType: ...

class Repeat(Func):
    output_field: models.CharField
    def __init__(self, expression: Expression | str, number: Expression | int | None, **extra: Any) -> None: ...
    def as_oracle(self, compiler: SQLCompiler, connection: BaseDatabaseWrapper, **extra_context: Any) -> _AsSqlType: ...

class Replace(Func):
    def __init__(self, expression: Combinable | str, text: Value, replacement: Value = ..., **extra: Any) -> None: ...

class Reverse(Transform):
    def as_oracle(self, compiler: SQLCompiler, connection: BaseDatabaseWrapper, **extra_context: Any) -> _AsSqlType: ...

class Right(Left):
    def get_substr(self) -> Substr: ...

class RPad(LPad): ...
class RTrim(Transform): ...
class SHA1(OracleHashMixin, PostgreSQLSHAMixin, Transform): ...

class SHA224(MySQLSHA2Mixin, PostgreSQLSHAMixin, Transform):
    def as_oracle(self, compiler: SQLCompiler, connection: BaseDatabaseWrapper, **extra_context: Any) -> _AsSqlType: ...

class SHA256(MySQLSHA2Mixin, OracleHashMixin, PostgreSQLSHAMixin, Transform): ...
class SHA384(MySQLSHA2Mixin, OracleHashMixin, PostgreSQLSHAMixin, Transform): ...
class SHA512(MySQLSHA2Mixin, OracleHashMixin, PostgreSQLSHAMixin, Transform): ...

class StrIndex(Func):
    output_field: models.IntegerField
    def as_postgresql(
        self, compiler: SQLCompiler, connection: BaseDatabaseWrapper, **extra_context: Any
    ) -> _AsSqlType: ...

class Substr(Func):
    output_field: models.CharField
    def __init__(
        self, expression: Expression | str, pos: Expression | int, length: Expression | int | None = ..., **extra: Any
    ) -> None: ...
    def as_sqlite(self, compiler: SQLCompiler, connection: BaseDatabaseWrapper, **extra_context: Any) -> _AsSqlType: ...
    def as_oracle(self, compiler: SQLCompiler, connection: BaseDatabaseWrapper, **extra_context: Any) -> _AsSqlType: ...

class Trim(Transform): ...
class Upper(Transform): ...
