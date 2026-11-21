"""HTTP 缓存新鲜度: Date/Age 与新鲜度生命周期的计算(纯标准库)。"""
from email.utils import parsedate_to_datetime


def parse_http_date(s):
    return parsedate_to_datetime(s).timestamp()


def freshness_lifetime(resp, now=None):
    """按 RFC 7234 计算新鲜度生命周期(秒)。

    优先级: s-max-age > max-age > Expires-Date 差值 > 启发式 10% 的 Date-Last-Modified。
    """
    cc = resp.get("cache-control", "")
    directives = dict(d.split("=", 1) if "=" in d else (d, None)
                      for d in cc.split(",") if d.strip())
    if "s-maxage" in directives:
        return int(directives["s-maxage"])
    if "max-age" in directives:
        return int(directives["max-age"])
    if "expires" in resp and "date" in resp:
        return max(0, int(parse_http_date(resp["expires"]) - parse_http_date(resp["date"])))
    if "date" in resp and "last-modified" in resp:
        age_hint = parse_http_date(resp["date"]) - parse_http_date(resp["last-modified"])
        return max(0, int(age_hint * 0.10))    # 启发式: 存活时长的 10%
    return 0


def current_age(resp, request_time, response_time, now):
    """计算响应在缓存中已经"老"了多少秒, Age 头与本地时钟差都要算进去。"""
    date_v = parse_http_date(resp["date"]) if "date" in resp else response_time
    apparent_age = max(0, int(response_time - date_v))
    age_hdr = int(resp.get("age", "0"))
    corrected_received = max(apparent_age, age_hdr)
    response_delay = response_time - request_time
    corrected_initial = corrected_received + int(response_delay)
    resident = int(now - response_time)
    return corrected_initial + resident


def verdict(resp, request_time, response_time, now):
    age = current_age(resp, request_time, response_time, now)
    life = freshness_lifetime(resp)
    return age, life, age < life


base = {"date": "Mon, 02 Nov 2026 08:00:00 GMT"}
t = parse_http_date(base["date"])
# 情形一: max-age 60, 链路上 Age 10, 本地驻留 20 -> 仍新鲜
resp1 = dict(base, **{"cache-control": "max-age=60", "age": "10"})
age, life, fresh = verdict(resp1, t, t + 2, t + 22)
print("max-age=60 Age=10 驻留20 -> 已老 {}s 生命周期 {}s 新鲜 {}".format(age, life, fresh))
assert fresh
# 情形二: 无 max-age, 用 Expires-Date 差值
resp2 = dict(base, **{"expires": "Mon, 02 Nov 2026 08:00:30 GMT"})
print("Expires 差值 ->", freshness_lifetime(resp2), "s")
# 情形三: 无显式指令, 启发式 10% 的存活时长
resp3 = dict(base, **{"last-modified": "Mon, 02 Nov 2026 06:00:00 GMT"})
print("启发式(2小时存活的10%) ->", freshness_lifetime(resp3), "s")
# 情形四: 老化到超期 -> 不新鲜, 必须回源或带条件重验证
age, life, fresh = verdict(resp1, t, t + 2, t + 95)
print("老化到 95s 时 -> 新鲜 {}".format(fresh))
assert not fresh
print("要点: 新鲜度判定是 current_age 与 freshness_lifetime 的比较, Age 头会把中间链路的老化叠加进来")
