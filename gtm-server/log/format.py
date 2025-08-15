from datetime import datetime
import json


# 模拟 json 格式日志
def format_logger(data):
    # 转换为东八区时间
    print(json.dumps(data))
