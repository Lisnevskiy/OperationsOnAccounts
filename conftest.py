import json

import pytest


@pytest.fixture
def json_file(tmp_path):
    data = {'key': 'value'}
    file_path = tmp_path / 'test.json'
    with open(file_path, 'w') as f:
        json.dump(data, f)
    return file_path
