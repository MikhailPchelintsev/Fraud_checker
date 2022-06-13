from aiohttp import web

from fraud_checker.views import CheckerView

APP_ROUTES = [
    web.view('/api/v1/check', CheckerView, name='checker'),
]
