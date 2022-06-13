from aiohttp import web
from aiohttp_apispec import docs

from droid import DroidView
from fraud_checker.call_fraud_model.api import call_fraud_api
from fraud_checker.serializers.request import (
    CheckerRequest,
    CheckerRequestSchema,
)
from fraud_checker.serializers.response import (
    RESPONSES_SPEC,
    CheckerResponseSchema,
)


class CheckerView(DroidView):

    validator = CheckerRequestSchema()  # type: ignore

    @docs(
        tags=['check.post'],
        responses=RESPONSES_SPEC,
    )
    async def post(self):
        checker_request: CheckerRequest = await self.validate()
        result = call_fraud_api.check(checker_request)
        response_body = CheckerResponseSchema().dumps(result)
        return web.json_response(body=response_body)
