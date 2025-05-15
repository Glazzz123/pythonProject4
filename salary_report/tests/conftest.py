import pytest
import tempfile
from pathlib import Path


@pytest.fixture
def csv_file(tmp_path):
    def _create(content: str) -> Path:
        file_path = tmp_path / "test.csv"
        file_path.write_text(content.strip())
        return file_path
    return _create
