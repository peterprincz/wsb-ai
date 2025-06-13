from alpaca.data import StockHistoricalDataClient, StockTradesRequest
from datetime import datetime
import config.appconfig

tradingConfig = config.appconfig.load_trading_config()

data_client = StockHistoricalDataClient(tradingConfig.key, tradingConfig.secret)

request_params = StockTradesRequest(
    symbol_or_symbols="AAPL",
    start=datetime(2025, 6, 9, 8, 20),
    end=datetime(2025, 6, 9, 8, 30)
)

trades = data_client.get_stock_trades(request_params=request_params)

print(trades)
