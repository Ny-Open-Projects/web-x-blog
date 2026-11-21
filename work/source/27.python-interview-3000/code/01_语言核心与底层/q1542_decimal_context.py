import threading
from decimal import (Decimal, DivisionByZero, ROUND_HALF_UP, getcontext,
                     localcontext)


def multiply_wide():
    a = Decimal("1." + "2" * 30)       # 31 位有效数字,精确构造
    b = Decimal("3")
    return a * b                        # 结果按当前上下文 prec 舍入


if __name__ == "__main__":
    ctx = getcontext()
    print("default prec:", ctx.prec, "| rounding:", ctx.rounding)
    print("prec=31 mult:", multiply_wide())

    with localcontext() as local:
        local.prec = 6
        print("prec=6  mult:", multiply_wide())
        print("1/3 at prec 6:", Decimal(1) / Decimal(3))
    print("restored prec:", getcontext().prec == ctx.prec)

    # 线程本地:子线程改 prec,主线程不受影响
    results = {}

    def worker():
        getcontext().prec = 4
        results["worker"] = str(Decimal(1) / Decimal(3))
        results["worker_prec"] = getcontext().prec

    t = threading.Thread(target=worker)
    t.start()
    t.join()
    print("worker:", results["worker"], "prec:", results["worker_prec"])
    print("main prec still:", getcontext().prec)

    # 量化到分:显式舍入模式,展示层专用
    price = Decimal("19.985")
    print("half_up  :", price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
    print("default  :", price.quantize(Decimal("0.01")), " 上下文 half-even")

    # traps:除零默认升级为异常,而不是返回 Infinity
    try:
        Decimal(1) / Decimal(0)
    except DivisionByZero:
        print("division by zero -> DivisionByZero")
