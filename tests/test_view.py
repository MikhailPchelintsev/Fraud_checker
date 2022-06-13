from http import HTTPStatus

import pytest

from tests import fixtures as fx


class TestCheckerView:
    @pytest.mark.parametrize('request_bytes', fx.GOOD_REQUESTS)
    async def test_post_ok(
        self,
        droid_client,
        droid_settings,
        request_bytes,
    ):
        client = await droid_client(droid_settings)
        resp = await client.post(
            '/api/v1/check',
            data=request_bytes,
            headers={'Content-Type': 'application/json'},
        )
        assert resp.status == HTTPStatus.OK
        checks = (await resp.json())['data']
        for check in checks:
            assert 'colour' in check
            assert 'check' in check

    @pytest.mark.parametrize('request_bytes, expected_code', fx.BAD_REQUESTS)
    async def test_bad_request(
        self,
        droid_client,
        droid_settings,
        request_bytes,
        expected_code,
    ):
        client = await droid_client(droid_settings)
        resp = await client.post(
            '/api/v1/check',
            data=request_bytes,
            headers={'Content-Type': 'application/json'},
        )
        assert resp.status == expected_code
