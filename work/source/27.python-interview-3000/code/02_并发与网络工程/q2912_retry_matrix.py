# -*- coding: utf-8 -*-
"""异常分类的重试矩阵: 可重试、致命与退避分档。

- 矩阵按"从具体到一般"排列, classify 用 isinstance 沿 MRO 匹配;
- TimeoutError / ConnectionError 都是 OSError 子类, 必须排在前面;
- 未登记的异常默认致命: 重试是给瞬态故障的, 不是给 bug 的。
"""
import time

# (异常类, 策略, 最大尝试次数, 基础退避秒)
# 顺序即优先级: 子类在前, 父类在后
RETRY_MATRIX = [
    (ValueError, "fatal", 1, 0.0),         # 参数错: 重试无意义
    (TimeoutError, "fixed", 3, 0.02),      # 超时: 快速固定间隔
    (ConnectionError, "expo", 3, 0.05),    # 连接错: 指数退避
    (OSError, "expo", 2, 0.08),            # 其他 IO 错: 慢速兜底
]


def classify(exc):
    """沿 MRO 找最近的登记项。"""
    for cls, policy, tries, delay in RETRY_MATRIX:
        if isinstance(exc, cls):
            return policy, tries, delay
    return "fatal", 1, 0.0                 # 未登记: 默认不重试


def run_with_matrix(fn, log):
    """按矩阵重试执行 fn, 返回 (成功?, 尝试次数, 结果或异常)。"""
    attempt = 0
    while True:
        attempt += 1
        try:
            return True, attempt, fn()
        except Exception as exc:           # 演示: 一律接住走矩阵分诊
            policy, tries, delay = classify(exc)
            log.append((attempt, type(exc).__name__, policy,
                        round(delay * 1000)))
            if policy == "fatal" or attempt >= tries:
                return False, attempt, exc
            if policy == "fixed":
                time.sleep(delay)
            else:                          # expo
                time.sleep(delay * (2 ** (attempt - 1)))


if __name__ == "__main__":
    # 用例一: 超时两次后成功 -> 命中 TimeoutError 而非其父类 OSError
    counter = {"n": 0}

    def flaky_timeout():
        counter["n"] += 1
        if counter["n"] < 3:
            raise TimeoutError("read timeout")
        return "ok-after-2-retries"

    log1 = []
    ok, tries, result = run_with_matrix(flaky_timeout, log1)
    print("用例一: ok=%s 尝试 %d 次, 决策路径 %s"
          % (ok, tries, [(e, p) for _, e, p, _ in log1] + [("ok",)]))
    assert ok and tries == 3
    assert log1[0][2] == "fixed", "应命中 TimeoutError 而非 OSError"

    # 用例二: 连接错误一直失败 -> 指数退避 3 次后放弃
    def always_down():
        raise ConnectionError("refused")

    log2 = []
    ok, tries, exc = run_with_matrix(always_down, log2)
    print("用例二: ok=%s 尝试 %d 次, 退避 ms=%s"
          % (ok, tries, [d for _, _, _, d in log2]))
    assert not ok and tries == 3 and log2[0][2] == "expo"

    # 用例三: ValueError -> 立即放弃, 一次都不重试
    def bad_input():
        raise ValueError("invalid argument")

    log3 = []
    ok, tries, exc = run_with_matrix(bad_input, log3)
    print("用例三: ok=%s 尝试 %d 次 (fatal 不重试)" % (ok, tries))
    assert not ok and tries == 1

    # 用例四: 未登记异常 -> 默认致命
    log4 = []
    ok, tries, exc = run_with_matrix(lambda: (_ for _ in ()).throw(KeyError("x")),
                                     log4)
    print("用例四: ok=%s 尝试 %d 次 (未登记默认致命)" % (ok, tries))
    assert not ok and tries == 1

    print("矩阵一览:")
    for cls, policy, tries, delay in RETRY_MATRIX:
        print("  %-16s -> %-6s tries=%d base=%dms"
              % (cls.__name__, policy, tries, delay * 1000))
    print("要点: 矩阵排序即优先级, 子类先判; 未登记的异常宁可失败也不重试")
