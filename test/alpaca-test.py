from alpaca.trading.client import TradingClient

import config.appconfig

tradingConfig = config.appconfig.load_trading_config()

trading_client = TradingClient(tradingConfig.key, tradingConfig.secret)

print(trading_client.get_account().account_number)
print(trading_client.get_account().buying_power)