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

    def test_byte_stream(self, file_type):
        byte_stream = file_type
        d = Decoder(byte_stream)
        result = d.decode()
        expected = {
            "type": "form-data",
            "name": "logo",
            "filename": "bobtail.png",
            "content_type": "image/png",
            "byte_stream": [
                b'\x89PNG\r',
                b'\x1a',
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
            ],
        }
        assert result == expected

    def test_file(self, file_type):
        png = file_type.split(b"image/png")[1]
        stream = io.BytesIO(png)
        with open("logo.png", "wb") as f:
            while True:
                buf = stream.read(16384)
                if not buf:
                    break
                f.write(buf)
