"""
Birman
"""
import io
from typing import Dict, List


class Decoder:
    """
    Decoder
    """
    data: bytes

    def __init__(self, data: bytes):
        self.data = data
    def _get_filename(self, field: List[bytes]) -> str:
        filename = field[0].split(b"name=")[1]
        filename = filename.split(b";")[0]
        filename = filename.decode("utf-8").strip()
        return filename.replace('"', "")

    def _get_name(self, field: List[bytes]) -> str:
        name = field[0].split(b"name=")[1]
        name = name.decode("utf-8").strip()  # incase there is any formatting remaining
        return name.replace('"', "")

    def _get_value(self, field: List[bytes]) -> str:
        # Check if the value is a byte stream
        for f in field:
            if f == b'\x89PNG\r':
                pass
        return field[2].decode("utf-8").strip()

    def decode(self) -> Dict:
        """
        :return: A Dict of multipart formdata fields e.g [name]: [name]: value
        :rtype Optional[Dict]:
        """
        fields = {}
        try:
            assert isinstance(self.data, bytes)
        except AssertionError:
            return {}
        _data_bytes = self.data.split(b"\r\nContent-Disposition")
        if len(_data_bytes) == 0:
            return {}
        data = _data_bytes[1:]
        for d in data:
            field = d.split(b"\n")
            # check if the field is a file
            f = field[0].split(b"filename=")
            if len(f) > 1:
                filename = self._get_filename(field)
                value = self._get_filename_value(d)
                fields[filename] = {"filename": filename, "value": value}
            else:
                name = self._get_name(field)
                value = self._get_value(field)
                fields[name] = {"name": name, "value": value}
        return fields

    def _get_filename_value(self, data: bytes) -> bytes:
        byte_str = data.split(b"Content-Type: image/png")
        return byte_str[1]

