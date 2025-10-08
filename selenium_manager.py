from selenium.webdriver.common.by import By                  # 要素を検索する方法を指定するための定義（ID, NAME, CSS_SELECTOR, など）
from selenium.webdriver.remote.webdriver import WebDriver     # ブラウザ操作オブジェクトの型ヒント用
from selenium.webdriver.remote.webelement import WebElement   # HTML要素（ボタンやテキストボックスなど）の型ヒント用
from selenium.common.exceptions import NoSuchElementException # 要素が見つからなかったときに発生する例外
from selenium import webdriver                                 # Chromeなどのブラウザを操作するための基本モジュール
from selenium.webdriver.chrome.options import Options          # Chrome起動時のオプション設定用
import logging                                                # ログ出力用モジュール
import time                                                   # 時間操作（待機など）用モジュール


class GetElement:
    """
    Seleniumで要素を取得する専用クラス。
    """

    def __init__(self, chrome: WebDriver, logger: logging.Logger):
        # 既存のChromeブラウザとloggerを保持
        self.chrome: WebDriver = chrome
        self.logger: logging.Logger = logger

    def get_by_id(self, value: str) -> WebElement:
        """ID属性で要素を取得"""
        self.logger.debug(f"要素取得開始 :\n {value}")
        try:
            element = self.chrome.find_element(By.ID, value)
            self.logger.debug(f"要素取得完了 :\n {value}")
            return element
        except NoSuchElementException as e:
            self.logger.error(f"要素取得失敗 :\n {e}")
            raise

    def get_by_name(self, value: str) -> WebElement:
        """name属性で要素を取得"""
        self.logger.debug(f"要素取得開始 :\n {value}")
        try:
            element = self.chrome.find_element(By.NAME, value)
            self.logger.debug(f"要素取得完了 :\n {value}")
            return element
        except NoSuchElementException as e:
            self.logger.error(f"要素取得失敗 :\n {e}")
            raise

    def get_by_css(self, value: str) -> WebElement:
        """CSSセレクタで要素を取得"""
        self.logger.debug(f"要素取得開始 :\n {value}")
        try:
            element = self.chrome.find_element(By.CSS_SELECTOR, value)
            self.logger.debug(f"要素取得完了 :\n {value}")
            return element
        except NoSuchElementException as e:
            self.logger.error(f"要素取得失敗 :\n {e}")
            raise

    def get_by_xpath(self, value: str) -> WebElement:
        """XPathで要素を取得"""
        self.logger.debug(f"要素取得開始 :\n {value}")
        try:
            element = self.chrome.find_element(By.XPATH, value)
            self.logger.debug(f"要素取得完了 :\n {value}")
            return element
        except NoSuchElementException as e:
            self.logger.error(f"要素取得失敗 :\n {e}")
            raise

    def get_by_class_name(self, value: str) -> WebElement:
        """class名で要素を取得"""
        self.logger.debug(f"要素取得開始 :\n {value}")
        try:
            element = self.chrome.find_element(By.CLASS_NAME, value)
            self.logger.debug(f"要素取得完了 :\n {value}")
            return element
        except NoSuchElementException as e:
            self.logger.error(f"要素取得失敗 :\n {e}")
            raise

    def get_by_tag_name(self, value: str) -> WebElement:
        """タグ名で要素を取得"""
        self.logger.debug(f"要素取得開始 :\n {value}")
        try:
            element = self.chrome.find_element(By.TAG_NAME, value)
            self.logger.debug(f"要素取得完了 :\n {value}")
            return element
        except NoSuchElementException as e:
            self.logger.error(f"要素取得失敗 :\n {e}")
            raise

    def get_by_link_text(self, value: str) -> WebElement:
        """リンクテキストで要素を取得"""
        self.logger.debug(f"要素取得開始 :\n {value}")
        try:
            element = self.chrome.find_element(By.LINK_TEXT, value)
            self.logger.debug(f"要素取得完了 :\n {value}")
            return element
        except NoSuchElementException as e:
            self.logger.error(f"要素取得失敗 :\n {e}")
            raise

    def get_by_partial_link_text(self, value: str) -> WebElement:
        """部分リンクテキストで要素を取得"""
        self.logger.debug(f"要素取得開始 :\n {value}")
        try:
            element = self.chrome.find_element(By.PARTIAL_LINK_TEXT, value)
            self.logger.debug(f"要素取得完了 :\n {value}")
            return element
        except NoSuchElementException as e:
            self.logger.error(f"要素取得失敗 :\n {e}")
            raise
