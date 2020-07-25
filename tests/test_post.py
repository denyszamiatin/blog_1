import json
import datetime
from unittest import mock
from app import app


class MockPost:
    def __init__(self):
        self.title = "Title1"
        self.body = ""
        self.date = datetime.datetime.strptime("2020-04-01T00:00", "%Y-%m-%dT%H:%M")



def test_create_post():
    with mock.patch("app.db.session.add") as add, \
         mock.patch("app.db.session.commit") as commit:
        r = app.test_client().post('/posts', data=json.dumps(
            {
                "title": "Title1",
                "body": "qwdeevg",
                "date": "2010-04-01T00:00"
            }), content_type="application/json"
        )
        add.assert_called_once()
        commit.assert_called_once()
    assert r.status_code == 201
    assert r.json['title'] == "Title1"


def test_read_all_post():
    with mock.patch('app.db.session.query') as query:
        query.return_value.all.return_value = []
        r = app.test_client().get("/posts")
    assert r.status_code == 200
    assert len(r.json) == 0


def test_read_post():
    with mock.patch("app.db.session.query") as query:
        query.return_value.filter_by.return_value.first.return_value = MockPost()
        r = app.test_client().get("/posts/123")
    assert r.status_code == 200
    assert r.json['title'] == "Title1"


def test_update_post():
    with mock.patch("app.db.session.query") as query, \
         mock.patch("app.db.session.add") as add, \
         mock.patch("app.db.session.commit") as commit:
        query.return_value.filter_by.return_value.first.return_value = MockPost()
        r = app.test_client().put(
            "/posts/123",
            data=json.dumps({"title": "Title2"}),
            content_type="application/json"
        )
    assert r.status_code == 200
    assert r.json['title'] == "Title2"


def test_delete_post():
    with mock.patch("app.db.session.query") as query, \
            mock.patch("app.db.session.delete") as delete, \
            mock.patch("app.db.session.commit") as commit:
        query.return_value.filter_by.return_value.first.return_value = MockPost()
        r = app.test_client().delete('/posts/123')
    assert r.status_code == 204
