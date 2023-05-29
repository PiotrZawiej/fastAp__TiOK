import unittest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

class TestApp(unittest.TestCase):
    def test_get_root(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"Aplication": "simple Fastapi aplication"}

    def test_get_posts(self):
        response = client.get("/posts")
        assert response.status_code == 200
        assert len(response.json()) == 10
        for post in response.json():
            assert "userId" in post
            assert "id" in post
            assert "title" in post
            assert "body" in post

    def test_get_post_comments(self):
        response = client.get("/posts/1/comments")
        assert response.status_code == 200
        assert len(response.json()) == 5
        for comment in response.json():
            assert "postId" in comment
            assert "id" in comment
            assert "name" in comment
            assert "email" in comment
            assert "body" in comment
            assert comment["postId"] == 1

if __name__ == "__main__":
    unittest.main()