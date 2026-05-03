from birman.encoder import Encoder
from tests.fixtures import multipart_data


class TestEncoder:

    def test_parse_params(self):
        arg = "?email=test@test.com&password=wizard"
        result = Encoder.parse_params(arg)
        expected = {
            "email": {
                "name": "email",
                "value": "test@test.com",
            },
            "password": {
                "name": "password",
                "value": "wizard",
            },
        }
        assert result == expected

    def test_parse_params_2(self):
        arg = ""
        result = Encoder.parse_params(arg)
        expected = {}
        assert result == expected

    def test_parse_params_3(self):
        arg = "?"
        result = Encoder.parse_params(arg)
        expected = {}
        assert result == expected

    def test_parse_params_4(self):
        arg = "?email="
        result = Encoder.parse_params(arg)
        expected = {'email': {'name': 'email', 'value': ''}}
        assert result == expected
