from pydantic import BaseModel
import yaml
import argparse


class Config(BaseModel):
    server_host: str = "localhost"
    server_port: int = 8000
    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_db: int = 0
    redis_password: str = ""


def parser_config(path: str) -> Config:
    with open(path, "r") as f:
        data = f.read()
        yaml_data = yaml.safe_load(data)
    return Config(**yaml_data)


parser = argparse.ArgumentParser()
parser.add_argument("--config", type=str, default="config.yml")
args = parser.parse_args()
config = parser_config(args.config)
