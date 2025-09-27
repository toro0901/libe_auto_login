from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from logger import log  # logger.py の log 関数をインポート
import logging

class ChromeManager:
    # Chromeのオプション設定
    def get_chrome_options(self):
        options = Options()
        options.add_argument("--window-size=1200,800")
        return options

    # Chromeを起動
    def start_chrome(self):
        try:
            options = self.get_chrome_options()
            self.chrome_driver = webdriver.Chrome(options=options)
            log("Chromeを起動しました", logging.INFO)  # INFOレベル
            return self.chrome_driver
        except Exception as e:
            log(f"Chromeの起動中にエラーが発生しました: {e}", logging.ERROR)  # ERRORレベル
            raise

    # 指定URLを開く
    def open_site(self, url):
        try:
            if self.chrome_driver is None:
                raise RuntimeError("Chromeが起動していません。")
            self.chrome_driver.get(url)
            log(f"{url} を開きました", logging.INFO)
        except Exception as e:
            log(f"サイトを開く際にエラーが発生しました: {e}", logging.ERROR)
            raise

if __name__ == "__main__":
    chrome_manager = ChromeManager()

    # Chrome起動
    chrome_driver = chrome_manager.start_chrome()

    # Googleを開く
    chrome_manager.open_site("https://www.google.com")

    # Chrome終了
    time.sleep(2)
    chrome_driver.quit()
    log("Chromeを閉じました", logging.INFO)
