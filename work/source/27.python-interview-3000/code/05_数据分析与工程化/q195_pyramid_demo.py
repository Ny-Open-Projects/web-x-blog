# 演示同一功能在金字塔不同层的测试粒度

def calc_discount(price, vip):
    # 被测逻辑:单元测试层
    if vip:
        return price * 0.8
    return price

def order_api(price, vip):
    # 集成层:逻辑 + 序列化/依赖协作
    return {"price": calc_discount(price, vip)}

def test_unit_layer():
    # 单元:只测纯逻辑,无 IO,毫秒级
    assert calc_discount(100, True) == 80

def test_integration_layer():
    # 集成:测函数协作与返回结构
    assert order_api(100, False) == {"price": 100}

def test_e2e_smoke():
    # E2E 只保留一条 happy path 冒烟,断言从输入到出口的行为
    resp = order_api(100, True)
    assert resp["price"] == 80
