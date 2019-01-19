import pytest
import tempfile
from pgbackup import storage

@pytest.fixture
def input_file():
        f = tempfile.TemporaryFile("r+b")
        f.write(b"Testing")
        f.seek(0)
        return f

def test_storing_file_locally(input_file):
        """
        Writes content from one file-like to another
        """
        output_file = tempfile.NamedTemporaryFile(delete=False)
        storage.local(input_file, output_file)
        with open(output_file.name, "rb") as f:
                assert f.read() == b"Testing"


def test_storing_file_on_s3(mocker,input_file):
        """
        writes content from readable to s3
        """
        client = mocker.Mock()

        storage.s3(client,
                   input_file,
                   "bucket",
                   "file-name")
        
        client.upload_fileobj.assert_called_with(input_file, "bucket", "file-name")