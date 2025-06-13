from alpaca.data.live import StockDataStream
import config.appconfig

tradingConfig = config.appconfig.load_trading_config()

stream = StockDataStream(tradingConfig.key, tradingConfig.secret)

async def handle_trade(data):
    print(data)

stream.subscribe_trades(handle_trade, "AAPL")
#handle quota azt mutatja secenként mennyiért lehet megvenni
stream.run()


