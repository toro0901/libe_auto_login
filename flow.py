import os
import time
from dotenv import load_dotenv
from selenium.webdriver.remote.webdriver import WebDriver

from chrome import ChromeManager
from selenium_manager import GetElement, ActionElement
from logger import Logger


class AutoLoginFlow:
    """
    指定されたサイトに自動でログインするフローを管理するクラス
    """

    def __init__(self, url: str):
        self.logger = Logger(__name__).get_logger()
        self.url = url
        self.chrome_manager = ChromeManager()
        self.driver: WebDriver = self.chrome_manager.start_chrome()
        self.get_element = GetElement(self.driver, self.logger)
        self.action_element = ActionElement(self.logger)

        # .envから環境変数読み込み
        load_dotenv()
        

    def website_login_flow(self) -> None:
        """ログイン操作フロー"""
        try:
            #1.サイトを開く
            self.logger.info(f"ログインページを開きます:{self.url}")
            self.chrome_manager.open_site(self.driver, self.url)

            #2.ログインID入力
            id_text = os.getenv("LOGIN_ID")
            self.logger.info(f"ログインIDを入力します:{id_text}")
            id_element = self.get_element.get_by_css('input[placeholder="メールアドレス"]')
            self.action_element.clear_and_send_keys(id_element, self.id_text)

            #3.パスワード入力
            password_text = os.getenv("LOGIN_PASSWORD")
            self.logger.info(f"パスワードを入力します:{password_text}")
            password_element = self.get_element.get_by_css('input[placeholder="パスワード"]')
            self.action_element.clear_and_send_keys(password_element, self.password_text)

            #4.ログインボタンクリック
            self.logger.info("ログインします")
            login_button = self.get_element.get_by_css('button.btn.bg_yellow')
            self.action_element.safe_click(login_button, self.driver)
            time.sleep(3)
            self.logger.info("ログイン完了")
        except Exception as e:
            self.logger.error(f"実行中にエラーが発生: {e}")
            raise
