import pytest


@pytest.fixture(scope="function")
def multipart_data():
    return b'----------------------------782797925953098016952108\r\nContent-Disposition: form-data; name=\"email\"\r\n\r\ntest@test.com\r\n----------------------------782797925953098016952108\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\nwizard\r\n----------------------------782797925953098016952108--\r\n'


@pytest.fixture(scope="function")
def multipart_data_2():
    return b'----------------------------782797925953098016952108\r\nContent-Disposition: form-data; name=\"email\"\r\n\r\ntest@test.com\r\n----------------------------782797925953098016952108--\r\n'

