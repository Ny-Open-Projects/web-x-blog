import random
import time


class ChaosInjector:
    """给依赖注入故障,验证调用方的降级预案是否生效。"""
    def __init__(self, fail_rate: float = 0.0, delay_ms: int = 0):
        self.fail_rate = fail_rate
        self.delay_ms = delay_ms
        self.enabled = False  # 回滚开关:随时一键停止注入

    def wrap(self, fn):
        def call(*args, **kwargs):
            if self.enabled:
                time.sleep(self.delay_ms / 1000)
                if random.random() < self.fail_rate:
                    raise ConnectionError("[chaos] injected failure")
            return fn(*args, **kwargs)
        return call


@ChaosInjector(fail_rate=0.5).wrap
def downstream_inventory(sku: str) -> int:
    return 99


def get_stock(sku: str) -> str:
    try:
        return f"stock={downstream_inventory(sku)}"
    except ConnectionError:
        return "stock=unknown"  # 降级:不因库存服务故障阻塞下单页


if __name__ == "__main__":
    random.seed(7)
    results = [get_stock("sku1") for _ in range(6)]
    print(results)
    print("fallback works:", any(r == "stock=unknown" for r in results))
