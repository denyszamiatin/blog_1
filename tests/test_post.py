import json
from app import app


def test_create_post():
    r = app.test_client().post('/posts', data=json.dumps(
        {
            "title": "Title1",
            "body": "qwdeevg",
            "date": "2010-04-01T00:00"
        }, content_type="application/json"
    ))
