from birman.decoder import Decoder
from tests.fixtures import multipart_data, multipart_data_2


class TestDecoder:

    def test_decode_1(self, multipart_data):
        decoder = Decoder(multipart_data)
        result = decoder.decode()
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

    def test_decode_2(self, multipart_data_2):
        decoder = Decoder(multipart_data_2)
        result = decoder.decode()
        expected = {
            "email": {
                "name": "email",
                "value": "test@test.com",
            },
        }
        assert result == expected

    def test_decode_3(self):
        decoder = Decoder(b"")
        result = decoder.decode()
        expected = {}
        assert result == expected

    def test_decode_4(self):
        decoder = Decoder(None)
        result = decoder.decode()
        expected = {}
        assert result == expected

    def test_decode_5(self):
        decoder = Decoder("")
        result = decoder.decode()
        expected = {}
        assert result == expected
