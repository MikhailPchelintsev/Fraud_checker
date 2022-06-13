from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Mapping

from marshmallow_dataclass import class_schema


@dataclass
class Interval:
    channel_number: int
    interval_number: int
    start_time: Decimal
    end_time: Decimal
    recognized_text: str


@dataclass
class CheckerRequest:
    channels: Mapping[int, List[Interval]] = field(
        metadata=dict(description='Каналы с интервалами'),
    )


CheckerRequestSchema = class_schema(CheckerRequest)
