import subprocess
import json
import tempfile
import os
import pytest

@pytest.fixture
def json_structure():
    data = {
        "name": "interpreter",
        "type": "dir",
        "contents": [
            {"name": "LICENSE", "type": "file", "size": 1071, "time_modified": 1699882320, "permissions": "-rw-r--r--"},
            {"name": "README.md", "type": "file", "size": 83, "time_modified": 1699882320, "permissions": "-rw-r--r--"},
            {"name": "ast", "type": "dir", "contents": [
                {"name": "ast.go", "type": "file", "size": 100, "time_modified": 1699882320, "permissions": "-rw-r--r--"},
                {"name": "go.mod", "type": "file", "size": 20, "time_modified": 1699882320, "permissions": "-rw-r--r--"}
            ]},
            {"name": "go.mod", "type": "file", "size": 30, "time_modified": 1699882320, "permissions": "-rw-r--r--"},
            {"name": "lexer", "type": "dir", "contents": [
                {"name": "lexer.go", "type": "file", "size": 200, "time_modified": 1699882320, "permissions": "-rw-r--r--"},
                {"name": "lexer_test.go", "type": "file", "size": 150, "time_modified": 1699882320, "permissions": "-rw-r--r--"},
                {"name": "go.mod", "type": "file", "size": 40, "time_modified": 1699882320, "permissions": "-rw-r--r--"}
            ]},
            {"name": "main.go", "type": "file", "size": 500, "time_modified": 1699882320, "permissions": "-rw-r--r--"},
            {"name": "parser", "type": "dir", "contents": [
                {"name": "parser.go", "type": "file", "size": 300, "time_modified": 1699882320, "permissions": "-rw-r--r--"},
                {"name": "parser_test.go", "type": "file", "size": 350, "time_modified": 1699882320, "permissions": "-rw-r--r--"},
                {"name": "go.mod", "type": "file", "size": 60, "time_modified": 1699882320, "permissions": "-rw-r--r--"}
            ]},
            {"name": "token", "type": "dir", "contents": [
                {"name": "token.go", "type": "file", "size": 600, "time_modified": 1699882320, "permissions": "-rw-r--r--"},
                {"name": "go.mod", "type": "file", "size": 25, "time_modified": 1699882320, "permissions": "-rw-r--r--"}
            ]}
        ]
    }
    with tempfile.NamedTemporaryFile(delete=False, suffix='.json') as f:
        json.dump(data, f)
        f.flush()
        yield f.name
    os.remove(f.name)

def test_pyls_list(json_structure):
    result = subprocess.run(['pyls', '-l'], capture_output=True, text=True)
    assert result.returncode == 0
    assert "LICENSE" in result.stdout
    assert "README.md" in result.stdout
    assert "ast" in result.stdout
    assert "lexer" in result.stdout
    assert "main.go" in result.stdout
    assert "parser" in result.stdout
    assert "token" in result.stdout
