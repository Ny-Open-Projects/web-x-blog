try:
    import pandas as pd
    PANDAS = True
except ImportError:
    PANDAS = False

# 指标字典:定义与实现绑定,消费方只调函数不写 SQL
METRIC_REGISTRY = {
    "gmv_paid": {
        "desc": "支付成功订单金额之和, 不含退款",
        "impl": lambda df: df.loc[df["status"] == "paid", "amount"].sum(),
    },
    "gmv_created": {
        "desc": "全部下单金额, 含未支付与退款",
        "impl": lambda df: df["amount"].sum(),
    },
    "refund_rate": {
        "desc": "退款金额 占 gmv_paid 比例",
        "impl": lambda df: (df.loc[df["status"] == "refunded", "amount"].sum()
                            / METRIC_REGISTRY["gmv_paid"]["impl"](df)),
    },
}

def compute(df, metric):
    return METRIC_REGISTRY[metric]["impl"](df)

if __name__ == "__main__":
    if PANDAS:
        df = pd.DataFrame({"status": ["paid", "created", "refunded"],
                           "amount": [100.0, 20.0, 10.0]})
        for m in METRIC_REGISTRY:
            print(m, "=", round(compute(df, m), 4))
    else:
        print("标准库思路:字典存定义与 lambda,同样可实现统一口径")
