import responses
from django.test import TestCase, Client


class EndpointTestCase(TestCase):
    fixtures = ["tests/unit/example_db.json"]

    def setUp(self):
        self.client = Client()

    def test_qotd(self):
        response = self.client.get("/qotd", {}, True)
        assert response.status_code == 200

        json = response.json()

        assert "quote" in json
        assert len(json["quote"]) > 0
        assert "author" in json
        assert "first_name" in json["author"]
        assert len(json["author"]["first_name"]) > 0
        assert "last_name" in json["author"]

    def test_authors(self):
        response = self.client.get("/authors", {}, True)
        assert response.status_code == 200

        json = response.json()

        assert "authors" in json
        assert len(json["authors"]) == 6
        assert "first_name" in json["authors"][0]
        assert len(json["authors"][0]["first_name"]) > 0
        assert "last_name" in json["authors"][0]

    def test_quotd_author(self):
        response = self.client.get("/quotd/Samuel Butler", {}, True)
        assert response.status_code == 200

        json = response.json()

        expected_json = {
            "quote": "Words are clothes that thoughts wear",
            "author": {
                "first_name": "Samuel",
                "last_name": "Butler"
            }
        }

        assert json == expected_json

    def test_quotd_author_first_name_only(self):
        response = self.client.get("/quotd/Yanni", {}, True)
        assert response.status_code == 200

        json = response.json()

        expected_json = {
            "quote": "If my music can change someone's mood for the better even a little bit, that's amazing.",
            "author": {
                "first_name": "Yanni",
                "last_name": ""
            }
        }

        assert json == expected_json

    def test_quotd_author_multiple_names(self):
        response = self.client.get("/quotd/Sarah Jessica Parker", {}, True)
        assert response.status_code == 200

        json = response.json()

        expected_json = {
            "quote": "Hello.",
            "author": {
                "first_name": "Sarah",
                "last_name": "Jessica Parker"
            }
        }

        assert json == expected_json

    def test_quotd_author_doesnt_exist(self):
        response = self.client.get("/quotd/Samuel Buttler", {}, True)
        assert response.status_code == 404

    @responses.activate
    def test_quotd_zen(self):
        rsp = responses.Response(
            method="GET",
            url="https://zenquotes.io/api/random",
            json=[
                {
                    "q": "While some of us act without thinking, too many of us think without acting.",
                    "a": "Dan Millman",
                    "h": "<blockquote>&ldquo;While some of us act without thinking, too many of us think without "
                         "acting.&rdquo; &mdash; <footer>Dan Millman</footer></blockquote>"
                }
            ]
        )

        responses.add(rsp)

        response = self.client.get("/quotd/zen", {}, True)
        assert response.status_code == 200

        expected_json = {
            "quote": "While some of us act without thinking, too many of us think without acting.",
            "author": {
                "first_name": "Dan",
                "last_name": "Millman"
            }
        }

        assert response.json() == expected_json


class EmptyEndpointTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_qotd(self):
        response = self.client.get("/qotd", {}, True)
        assert response.status_code == 404

    def test_authors(self):
        response = self.client.get("/authors", {}, True)
        assert response.status_code == 200

        json = response.json()

        assert "authors" in json
        assert len(json["authors"]) == 0

