from pydantic import BaseModel
import json
import os


class AppConfig(BaseModel):
    ollama_url: str
    model: str
    prompt_path: str
    client_id: str
    client_secret: str
    password: str
    user_agent: str
    username: str
    database_uri: str


class TradingConfig(BaseModel):
    key: str
    secret: str


def load_config(path: str = "config/config.json") -> AppConfig:
    newpath = (str)(os.path.dirname(__file__)) + "\config.json"
    with open(newpath, "r") as f:
        data = json.load(f)
    appconfig = AppConfig(**data)
    appconfig.password = os.getenv("reddit_password", "secret")
    return appconfig


def load_trading_config() -> TradingConfig:
    path = (str)(os.path.dirname(__file__)) + "\\tradingconfig.json"
    with open(path, "r") as f:
        data = json.load(f)
    trading_config = TradingConfig(**data)
    return trading_config


config: AppConfig = load_config()
tradingConfig: TradingConfig = load_trading_config()
