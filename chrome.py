from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from logger import Logger

class ChromeManager:
    def __init__(self):
        #logger初期化
        self.logger = Logger(__name__).get_logger()
    
    def get_chrome_options(self):
        """
        Chromeの起動オプションの設定（今回はウィンドウサイズのみ）
        """
        options = Options()
        options.add_argument("--window-size=1200,800")
        return options
    
    def start_chrome(self):
        """
        Chromeを起動してdriverを返す
        """
        try:
            options = self.get_chrome_options()
            self.driver = webdriver.Chrome(options=options)
            self.logger.info("Chromeが起動しました")
            return self.driver
        except WebDriverException as e:
            self.logger.error(f"Chrome起動中にエラーが発生:{e}")
            raise

    def open_site(self, url:str):
        """
        指定したURLをChromeで開く
        """
        try:
            self.driver.get(url)
            self.logger.info(f"{url}を開きました")
        except WebDriverException as e:
            self.logger.error(f"サイトを開く際にエラー発生:{e}")
            raise


#===== 動作確認 =====
if __name__ ==  "__main__":
    manager = ChromeManager()
    url = "https://www.google.com"

    try:
        driver = manager.start_chrome()
        manager.open_site(url)
    except Exception as e:
        manager.logger.error(f"テスト中にエラー発生:{e}")