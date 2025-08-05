from datetime import datetime


# 模拟 json 格式日志
def format_logger(data):
    data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(data)
