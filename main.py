from flow import AutoLoginFlow

if __name__ == "__main__":
    # Libecityログインページ
    url = "https://libecity.com/signin"

    # AutoLoginFlowの起動と実行
    flow = AutoLoginFlow(url)
    flow.website_login_flow()
