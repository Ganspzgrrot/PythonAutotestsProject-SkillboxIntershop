import pytest
import sys

if __name__ == "__main__":
    print("Запуск автоматических тестов Selenium....")
    args = [
        "-v",
        "-s",
        "tests"
    ]
    exit_code = pytest.main(args)
    print(f"Тестирование завершено с кодом: {exit_code}")

    sys.exit(exit_code)
    s = input('Нажмите ENTER, чтобы выйти')