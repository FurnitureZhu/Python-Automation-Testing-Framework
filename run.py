import pytest
import os

if __name__ == '__main__':
    pytest.main()
    os.system("allure generate ./reports -o ./reports/html --clean")
    os.system("allure open ./reports/html")