# -*- coding:utf-8 -*-

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str,tz_str):
    # 时间化标
    dt_time=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    # 时区转化为数字
    tz = int(tz_str[3:].split(':')[0])

    # 创建时区utc
    tz_utc= timezone(timedelta(hours=tz))
    # 强制设置时区 utc
    f_time = dt_time.replace(tzinfo=tz_utc)
    return f_time.timestamp()


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')