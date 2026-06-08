import pytest
import sys
import os

if __name__ == "__main__":
    args = [
        "-v",
        "-s",
        "tests",
        "--alluredir=results"
    ]
    exit_code = pytest.main(args)
    os.system("allure serve results")
    sys.exit(exit_code)