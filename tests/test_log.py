from unittest import mock

from fraud_checker.logs import initialize_logs


class TestLog:
    @mock.patch('fraud_checker.logs.setup_logging')
    def test_logger_initialize(self, setup_mock):
        initialize_logs()
        setup_mock.assert_called_once()
