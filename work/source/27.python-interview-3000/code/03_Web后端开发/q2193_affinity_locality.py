"""就近路由下的会话亲和: 粘住区域复用缓存与数据 locality(纯标准库)。"""

USER_REGION = {"u1": "cn-east", "u2": "cn-north"}
CACHE_BY_REGION = {"cn-east": {"u1:cart": ["book"]}, "cn-north": {}}
CROSS_RTT_MS = 30                                     # 跨区回源一次的往返成本
counter = {"n": 0}


def get_cart(user, sticky=True):
    home = USER_REGION[user]
    if sticky:
        region = home
    else:
        regions = sorted(CACHE_BY_REGION)
        region = regions[counter["n"] % len(regions)]   # 不感知用户的轮转
        counter["n"] += 1
    key = user + ":cart"
    if key in CACHE_BY_REGION[region]:
        return CACHE_BY_REGION[region][key], region, 0
    return CACHE_BY_REGION[home].get(key), region, CROSS_RTT_MS


print("粘住主区      :", get_cart("u1", sticky=True))
print("不感知用户 1  :", get_cart("u1", sticky=False))
print("不感知用户 2  :", get_cart("u1", sticky=False))
cart, region, cost = get_cart("u1", sticky=False)
assert cost in (0, CROSS_RTT_MS)
print("要点: 亲和的收益是缓存命中与数据近距离, 判据是跨区请求占比与额外延迟是否超预算")
