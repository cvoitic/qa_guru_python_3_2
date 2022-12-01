import pytest
import random


@pytest.fixture(scope="session")
def open_browser():
    b = "browser"
    print("Браузер открыт!")
    print(f"Случайное число: {random.randint(0, 100)}")
    yield "b" #передача управления из этой функции
    b = ""
    print("Браузер закрыт!")
