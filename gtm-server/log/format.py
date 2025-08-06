from datetime import datetime
import json


# 模拟 json 格式日志
def format_logger(data):
    data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(json.dumps(data))
