import json
import pytest
from pytest_schema import schema

from Client.sample_client import SampleClient


class TestAvatar(SampleClient):

    @pytest.mark.avatar
    def test_avatar_info(self):
        url = "/info"
        avatar_info_schema = {
            "id": int,
            "synopsis": str,
            "yearsAired": str,
            "genres": list,
            "creators": list
        }
        response = self.get_avatar(url)
        body = json.loads(response.text)

        assert response.status_code == 200
        assert schema(avatar_info_schema) == body[0]
        assert len(body) == 1
