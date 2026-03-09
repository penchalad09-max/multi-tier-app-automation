import requests
from unittest.mock import patch
from python.validate_app import validate_app

def test_validate_app(capsys):
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = "Hello World"  # or whatever your app returns
        validate_app("http://localhost:8081")
        captured = capsys.readouterr()
        assert "✅ App is serving content correctly." in captured.out





# Run the Below Code While we pytest.ini file or else it will not work as expected. pytest.ini file is used to specify the test paths and other configurations for pytest.

# import sys, os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "python")))

# from python.validate_app import validate_app

# def test_validate_app():
#     # Just ensure function runs without exception
#     try:
#         validate_app()
#         assert True
#     except Exception:
#         assert False
