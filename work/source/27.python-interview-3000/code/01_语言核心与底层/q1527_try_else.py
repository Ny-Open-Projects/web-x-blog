
PRICES = {"apple": 5, "banana": 2}


def parse_and_bill_narrow(line):
    """窄 try:只包真正会抛 ValueError 的类型转换。"""
    name, _, qty = line.partition(":")
    unit = PRICES[name]                # 查表错误如实抛 KeyError
    try:
        total = int(qty) * unit
    except ValueError:
        return None
    else:
        if total > 1000:
            raise ValueError("total 超限")   # 成功路径的问题不再被吞
        return total


def parse_and_bill_wide(line):
    """反例:try 拖得太宽,业务校验的异常被当成解析失败吞掉。"""
    try:
        name, _, qty = line.partition(":")
        unit = PRICES[name]
        total = int(qty) * unit
        if total > 1000:
            raise ValueError("total 超限")   # 业务校验,与解析无关
        return total
    except ValueError:
        return None                          # 业务错误被误归为解析失败


if __name__ == "__main__":
    print("narrow ok  :", parse_and_bill_narrow("apple:3"))
    print("narrow bad :", parse_and_bill_narrow("apple:x"))
    try:
        parse_and_bill_narrow("cherry:2")
    except KeyError as err:
        print("narrow miss:", "KeyError 如实抛出:", err)
    try:
        parse_and_bill_narrow("apple:400")
    except ValueError as err:
        print("narrow big :", "业务校验如实抛出:", err)

    print("wide ok    :", parse_and_bill_wide("apple:3"))
    print("wide bad   :", parse_and_bill_wide("apple:x"))
    print("wide big   :", parse_and_bill_wide("apple:400"), " # 业务错误被吞成 None")

    order = []
    try:
        order.append("try")
    except ValueError:
        order.append("except")
    else:
        order.append("else")
    finally:
        order.append("finally")
    print("execution  :", order)
