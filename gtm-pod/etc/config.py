import argparse
import yaml


class GtmConfig:
    def __init__(self, config: str):
        self.config = config

    def parse_config(self):
        with open(self.config, "r") as f:
            data = yaml.safe_load(f)
            return data


# 解析命令行参数
args = argparse.ArgumentParser()
args.add_argument("--config", type=str, default="config.yml")
args = args.parse_args()

# 解析配置文件
gtm_config = GtmConfig(args.config)
config = gtm_config.parse_config()
