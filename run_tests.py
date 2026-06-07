import pytest
import os

if __name__ == "__main__":
    print("Запуск автоматических тестов Selenium....")
    args = [
        "-v",
        "-s"
    ]
    exit_code = pytest.main(args)
    print(self:=f"Тестирование завершено с кодом: {exit_code}")