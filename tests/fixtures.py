from http import HTTPStatus

GOOD_REQUESTS = (
    '''
    {
        "channels": {
            "1": [
                {
                    "end_time": "16.420000",
                    "interval_number": 1,
                    "channel_number": 1,
                    "recognized_text": "Алло Так давай ты поможешь мне 1 трубку положить?",
                    "start_time": "0.000000"
                }
            ],
            "2": [
                {
                    "end_time": "3.653000",
                    "interval_number": 1,
                    "channel_number": 2,
                    "recognized_text": "Точно",
                    "start_time": "2.856000"
                },
                {
                    "end_time": "12.535000",
                    "interval_number": 4,
                    "channel_number": 2,
                    "recognized_text": "Давай расскажи",
                    "start_time": "11.515500"
                }
            ]
        }
    }''',
)

BAD_REQUESTS = (
    (
        b'nuds',
        HTTPStatus.BAD_REQUEST,
    ),
    (
        '''
        {
            "channels": {
                "1": [
                    {
                        "end_time": "16.420000",
                        "interval_number": 1,
                        "channel_number": 1,
                        "recognized_text": 0,
                        "start_time": "0.000000"
                    }
                ],
                "2": [
                    {
                        "end_time": "3.653000",
                        "interval_number": 1,
                        "channel_number": 2,
                        "recognized_text": 1,
                        "start_time": "2.856000"
                    }
                ]
            }
        }''',
        HTTPStatus.UNPROCESSABLE_ENTITY,
    ),
)
