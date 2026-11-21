---
title: [Q2863] token 计量的校准:本地估算与供应商回执偏差追踪
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2863 · token 计量的校准:本地估算与供应商回执偏差追踪

> 难度:★★★☆ | 标签:LLM 运维, 计量, 校准

**问**:预算控制靠本地 token 估算,但估算器为什么会漂?怎么发现并纠正?

**答**:本地估算省了计量依赖,但它对语言分布敏感:模型或流量从英文转中文,每 token 对应的字符数就变,预算按旧系数算,超支是无声的。治理办法是持续对账:每次请求都拿到供应商回执的真实用量,和本地估算比对,均值比率系统性偏离 1 超过阈值就告警并重校准系数——比如发现系统性低估 25%,估算系数相应下调,预算重新对准现实。校准是自愈的:新系数来自最近窗口的真实分布,流量再漂再校。要注意比率波动和漂移的区别:方差大说明流量混合,均值稳偏才是系数问题;校准记录要留档,「为什么上月预算失准」可以回放系数变化史。回执延迟到账的链路里,校准用最近已完成窗口,别用正在累计的半截数据。

```python
# file: code/06_Agent与LLM及系统设计/q2863_token_calibration.py
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
```

**追问**:
- 追问一:不同语言分桶校准吗? 答:大流量语种值得分桶,小语种共享全局系数,分桶阈值看量级,过度分桶会让每桶样本不足。
- 追问二:回执和本地估算差在哪些结构上? 答:工具调用消息和长代码块差异最大,校准样本按结构分层能定位到具体偏差源。
