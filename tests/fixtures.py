import pytest


@pytest.fixture(scope="function")
def multipart_data():
    return b'----------------------------782797925953098016952108\r\nContent-Disposition: form-data; name=\"email\"\r\n\r\ntest@test.com\r\n----------------------------782797925953098016952108\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\nwizard\r\n----------------------------782797925953098016952108--\r\n'


@pytest.fixture(scope="function")
def multipart_data_2():
    return b'----------------------------782797925953098016952108\r\nContent-Disposition: form-data; name=\"email\"\r\n\r\ntest@test.com\r\n----------------------------782797925953098016952108--\r\n'


@pytest.fixture(scope="function")
def file_type():
    return b'----------------------------138321988060416233833146\r\nContent-Disposition: form-data; name="name"\r\n\r\nJoe\r\n----------------------------138321988060416233833146\r\nContent-Disposition: form-data; name="age"\r\n\r\n47\r\n----------------------------138321988060416233833146\r\nContent-Disposition: form-data; name="logo"; filename="bobtail.png"\r\nContent-Type: image/png\r\n\r\n\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x08e\x00\x00\x02\x04\x08\x06\x00\x00\x01\xcd\x8f1\xca\x00\x00\x00\\x12\xbf\xb4}\xae\xc6n\xee\xc8\xe7\xee(aFB\xfb%Fn\xbe\x90[3cj\xc9\x02R\xea\x94\x80\x12P\x02J@\t(\x01%\xa0\x04\x94\x80\x12h\x08\x81\xff\x01\t\xb6!\x1f\x86\xa9?\xfb\x00\x00\x00\x00IEND\xaeB`\x82\r\n----------------------------138321988060416233833146--\r\n'
