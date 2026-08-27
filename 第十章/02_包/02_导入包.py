# 1. import 包名.模块名
"""
import trade.order
import trade.pay

trade.order.create_order()
trade.pay.wechat_pay()
"""
from trade.order import create_order

# 2. import 包名.模块名 as 别名
"""
import trade.order as od
import trade.pay as pa

od.create_order()
pa.wechat_pay()
"""

# 3. from 包名.模块名 import 具体内容
"""
from trade.order import MAX_ORDER_AMOUNT, create_order
from trade.pay import TIMEOUT, wechat_pay

print(MAX_ORDER_AMOUNT)
create_order()
print(TIMEOUT)
wechat_pay()
"""

# 4. from 包名.模块名 import 具体内容 as 别名
"""
from trade.order import MAX_ORDER_AMOUNT as MAX_ORDER
from trade.pay import wechat_pay as wp

print(MAX_ORDER)
wp()
"""

# 5. from 包名.模块名 import *
"""
from trade.order import *
from trade.pay import *

create_order()
cancel_order()
show_info()
wechat_pay()
"""

# 6. from 包名 import 模块名
"""
from trade import order, pay

order.create_order()
pay.wechat_pay()
"""

# 7. from 包名 import 模块名 as 别名
"""
from trade import order as dd, pay as p

dd.create_order()
p.wechat_pay()
"""

# 8. from 包名 import *
"""
from trade import *

print(a)s
print(b)
print(pay.TIMEOUT)
create_order()
"""

# 9. import 包名
# import trade
#
# print(trade.a)
# print(trade.b)
# trade.pay.wechat_pay()
