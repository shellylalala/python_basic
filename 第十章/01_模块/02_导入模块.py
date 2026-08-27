# 1. import 模块名
## 会导入模块的所有内容，又叫全部导入
## 注意：
# 1. Python 中导入模块的时，会执行对应模块中的代码。
# 2. 模块只加载一次，后续再次导入，直接复用缓存。
"""
import order
import pay

print(order.MAX_ORDER_AMOUNT)
order.create_order()
order.cancel_order()
order.show_info()

print("*" * 10)

print(pay.TIMEOUT)
pay.wechat_pay()
pay.ali_pay()
pay.show_info()
"""

# 2. import 模块名 as 别名
"""
import order as o
import pay as p

print(o.MAX_ORDER_AMOUNT)
o.create_order()
o.cancel_order()
o.show_info()

print("*" * 10)

print(p.TIMEOUT)
p.wechat_pay()
p.ali_pay()
p.show_info()
"""

# 3. from 模块名 import 具体内容1, 具体内容2, ......
"""
from order import MAX_ORDER_AMOUNT, show_info
from pay import wechat_pay, ali_pay

print(MAX_ORDER_AMOUNT)
show_info()
wechat_pay()
ali_pay()
"""

# 4. from 模块名 import 具体内容 as 别名
"""
from order import MAX_ORDER_AMOUNT as MAX_ORDER, show_info as show
from pay import wechat_pay as we_pay, ali_pay as a_pay

print(MAX_ORDER)
show()
a_pay()
we_pay()
"""

# 5. from 模块名 import *
from order import *
from pay import *

print(MAX_ORDER_AMOUNT)
# 存在覆盖，以后引入的为准
show_info()
wechat_pay()
ali_pay()
