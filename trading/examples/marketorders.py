from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest, LimitOrderRequest, GetOrdersRequest
from alpaca.trading.enums import OrderSide, TimeInForce,QueryOrderStatus
import config.appconfig

tradingConfig = config.appconfig.load_trading_config()

trading_client = TradingClient(tradingConfig.key, tradingConfig.secret)

# simple order
market_order_data = MarketOrderRequest(
    symbol="SPY",
    qty=1,
    side=OrderSide.BUY,
    time_in_force=TimeInForce.DAY #itt van több opció is pl fear or kill qtc stb...
)

#market_order = trading_client.submit_order(market_order_data)
#print(market_order)

#order with a set price
limit_order_data = LimitOrderRequest(
    symbol="SPY",
    qty=1,
    side=OrderSide.BUY,
    time_in_force=TimeInForce.DAY,
    limit_price=599
)

#limit_order = trading_client.submit_order(limit_order_data)
#print(limit_order)

#manage orders
request_params = GetOrdersRequest(
    status=QueryOrderStatus.OPEN
)

orders = trading_client.get_orders(request_params)

#cancel orders
#for order in orders:
#    trading_client.cancel_order_by_id(order.id)

#stockok lekérése
positions = trading_client.get_all_positions()

for position in positions:
    print(position.symbol, position.current_price)