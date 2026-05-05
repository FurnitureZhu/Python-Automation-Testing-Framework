from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_ui():
    # 1. 启动浏览器（自动匹配driver）
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # 2. 打开测试网站
        driver.get("https://the-internet.herokuapp.com/login")

        wait = WebDriverWait(driver, 10)

        # 3. 等待用户名输入框
        username = wait.until(
            EC.presence_of_element_located((By.ID, "username"))
        )

        # 4. 输入账号
        username.clear()
        username.send_keys("tomsmith")

        # 5. 输入密码
        password = driver.find_element(By.ID, "password")
        password.clear()
        password.send_keys("SuperSecretPassword!")

        # 6. 点击登录
        driver.find_element(By.CSS_SELECTOR, "button.radius").click()

        # 7. 验证登录成功提示
        message = wait.until(
            EC.presence_of_element_located((By.ID, "flash"))
        )

        assert "You logged into a secure area!" in message.text

    finally:
        driver.quit()