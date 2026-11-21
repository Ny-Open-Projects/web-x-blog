"""Q2863 token 计量的校准:本地估算与供应商回执的偏差追踪。

预算控制靠本地估算,但估算器会漂:换模型 换语言分布都会让「每字符
token 数」变化。持续对比本地估算与供应商回执,偏差超过阈值就告警
并重校准系数,预算才不会悄悄失真。
"""


def estimate(chars, factor=4.0):
    return max(1, int(round(chars / factor)))


def calibrate(samples, factor, alert=0.2):
    """samples: [(chars, receipt_tokens)],返回告警与新系数。"""
    ratios = [receipt / float(max(1, estimate(chars, factor)))
              for chars, receipt in samples]
    mean = sum(ratios) / len(ratios)
    drifted = abs(mean - 1.0) > alert
    new_factor = factor / mean if drifted else factor
    return {"mean_ratio": mean, "drifted": drifted,
            "new_factor": new_factor}


def main():
    # 现网换成中文为主的流量后,每 token 约 3.2 字符,而估算按 4 算
    samples = [(3200, 1000), (6400, 2000), (1600, 500),
               (4800, 1500), (8000, 2500)]
    r = calibrate(samples, factor=4.0)
    assert abs(r["mean_ratio"] - 1.25) < 0.01, r   # 系统性低估 25%
    assert r["drifted"] is True, r
    err_before = sum(abs(estimate(c, 4.0) - t) for c, t in samples)
    err_after = sum(abs(estimate(c, r["new_factor"]) - t) for c, t in samples)
    assert r["new_factor"] - 3.2 < 0.01, r
    assert err_after < err_before, (err_before, err_after)
    # 没漂移时不乱动系数
    ok = calibrate([(4000, 1000), (8000, 2000)], factor=4.0)
    assert ok["drifted"] is False and ok["new_factor"] == 4.0, ok
    print("偏差均值:", round(r["mean_ratio"], 3), "-> 触发重校准")
    print("系数 4.0 ->", round(r["new_factor"], 3))
    print("估算误差:", err_before, "->", err_after)


if __name__ == "__main__":
    main()
