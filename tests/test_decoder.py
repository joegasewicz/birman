import io

from birman.decoder import Decoder
from tests.fixtures import (
    multipart_data,
    multipart_data_2,
    file_type,
)

class TestDecoder:

    def test_decode_1(self, multipart_data):
        decoder = Decoder(multipart_data)
        result = decoder.decode()
        expected = {
            "email": {
                "name": "email",
                "value": "test@test.com",
                "type": "text",
            },
            "password": {
                "name": "password",
                "value": "wizard",
                "type": "text",
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
                "type": "text",
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

    def test_byte_stream(self, file_type):
        byte_stream = file_type
        d = Decoder(byte_stream)
        result = d.decode()

        assert result["name"]["name"] == "name"
        assert result["name"]["value"] == "Joe"
        assert result["name"]["type"] == "text"
        assert result["age"]["name"] == "age"
        assert result["age"]["value"] == "47"
        assert result["age"]["type"] == "text"
        assert result["logo"]["name"] == "logo"
        assert result["logo"]["type"] == "file"
        assert result["logo"]["value"]["filename"] == "bobtail.png"
        assert result["logo"]["value"]["mimetype"] == "image/png"
        assert result["logo"]["value"]["file_data"] is not None
        assert isinstance(result["logo"]["value"]["file_data"], bytes)
