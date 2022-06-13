from dataclasses import dataclass, field
from types import MappingProxyType
from typing import List

from marshmallow_dataclass import class_schema

from droid.spec.response import ErrorResponseSchema


@dataclass
class CheckReport:
    check: str = field(metadata=dict(description='Название проверки'))
    colour: str = field(metadata=dict(description='Решение по проверке'))
    model: str = field(metadata=dict(description='Название модели'))
    version: str = field(metadata=dict(description='Версия модели'))
    score: str = field(metadata=dict(description='Оценка модели'))


@dataclass
class CheckerResponse:
    data: List[CheckReport] = field(
        metadata=dict(description='Результаты проверок'),
    )


CheckerResponseSchema = class_schema(CheckerResponse)

RESPONSES_SPEC = MappingProxyType(
    {
        200: {
            'description': 'OK',
            'schema': CheckerResponseSchema(),
        },
        400: {
            'description': 'Ошибки сериализации, подключения',
            'schema': ErrorResponseSchema(),
        },
        422: {
            'description': 'Ошибки валидации',
            'schema': ErrorResponseSchema(),
        },
        500: {
            'description': 'Internal Server Error',
            'schema': ErrorResponseSchema(),
        },
    },
)
