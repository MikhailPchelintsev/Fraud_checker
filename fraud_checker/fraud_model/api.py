import logging
from typing import List

import smart_fraud_checker
from smart_fraud_checker import load

from fraud_checker.config.config import SmartConf, conf
from fraud_checker.serializers.request import CheckerRequest
from fraud_checker.serializers.response import (
    CheckerResponse,
    CheckReport,
)

logger = logging.getLogger(__name__)


class CallFraudApi:

    def __init__(self, config: SmartConf) -> None:
        self._checker = load(threshold=conf.model.threshold, path=conf.model.model_path)
        self.check_name = 'call_fraud_check'

    def check(self, request: CheckerRequest) -> CheckerResponse:
        text = self._merge_text(request)
        result = self._checker.check(text)
        reports: List[CheckReport] = []
        reports.append(
            CheckReport(
                check=self.check_name,
                colour='red' if result.check_result else 'green',
                model=smart_fraud_checker.__name__,
                version=smart_fraud_checker.__version__,
                score=result.score,
            ),
        )
        return CheckerResponse(reports)

    def _merge_text(self, request_data: CheckerRequest) -> str:
        interval_lists = request_data.channels.values()
        intervals = [item for sublist in interval_lists for item in sublist]
        sorted_intervals = sorted(
            intervals,
            key=lambda item: (item.channel_number, item.interval_number),
        )
        rec_texts = [interval.recognized_text for interval in sorted_intervals]
        return ' '.join(rec_texts)


call_fraud_api = CallFraudApi(conf)
