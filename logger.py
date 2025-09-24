import logging

LEVEL_COLORS = {
    logging.DEBUG: "\033[34m",    # 青
    logging.INFO: "\033[32m",     # 緑
    logging.WARNING: "\033[33m",  # 黄
    logging.ERROR: "\033[31m",    # 赤
    logging.CRITICAL: "\033[35m"  # マゼンタ
}
RESET_COLOR = "\033[0m"

#loggerの定義
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

#コンソール用ハンドラ
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

#レベルごとに色をつけて表示する関数
def log(message, level=logging.INFO):
    color = LEVEL_COLORS.get(level, "\033[37m")
    level_name = logging.getLevelName(level)
    #文字列を作って色付け
    full_message = f"{level_name} : {message}"
    colored_message = f"{color}{full_message}{RESET_COLOR}"
    logger.log(level, colored_message)

#テスト出力
log("デバッグメッセージ", logging.DEBUG)
log("情報メッセージ")
log("警告メッセージ", logging.WARNING)
log("エラーメッセージ", logging.ERROR)
log("重大なエラーメッセージ", logging.CRITICAL)