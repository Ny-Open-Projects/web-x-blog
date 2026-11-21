"""异常流量识别:频次、UA 多样性、referer 缺失率、路径集中度四信号打分"""

import math
from collections import Counter, defaultdict

LOGS = [
    # ip, ua, path, referer
    ("10.0.0.1", "ua-A", "/item/1", "https://search.example.com"),
    ("10.0.0.1", "ua-A", "/item/2", "https://search.example.com"),
    ("10.0.0.1", "ua-A", "/item/1", None),
    ("10.0.0.1", "ua-A", "/item/3", None),
    ("10.0.0.1", "ua-A", "/item/1", None),
    ("10.0.0.1", "ua-A", "/item/2", None),
    ("10.0.0.2", "ua-B", "/home", "https://ad.example.com"),
    ("10.0.0.2", "ua-C", "/home", None),
    ("10.0.0.3", "ua-D", "/item/1", "https://search.example.com"),
]


def shannon_entropy(counter):
    total = sum(counter.values())
    if total == 0:
        return 0.0
    return -sum((n / total) * math.log2(n / total) for n in counter.values())


def score_ip(rows):
    """四个信号各占 25 分,总分 >= 60 判定为疑似机器流量"""
    ips = defaultdict(list)
    for ip, ua, path, ref in rows:
        ips[ip].append((ua, path, ref))
    result = {}
    for ip, hits in ips.items():
        n = len(hits)
        ua_entropy = shannon_entropy(Counter(ua for ua, _, _ in hits))
        no_ref = sum(1 for _, _, ref in hits if ref is None) / n
        path_counter = Counter(p for _, p, _ in hits)
        top_concentration = max(path_counter.values()) / n
        s_freq = min(n / 8, 1) * 25          # 频次:8 次封顶
        s_ua = (1 - min(ua_entropy, 1)) * 25  # UA 熵越低越像脚本
        s_ref = no_ref * 25
        s_path = top_concentration * 25
        result[ip] = {"score": s_freq + s_ua + s_ref + s_path, "n": n}
    return result


if __name__ == "__main__":
    for ip, info in sorted(score_ip(LOGS).items(), key=lambda x: -x[1]["score"]):
        verdict = "疑似机器流量" if info["score"] >= 60 else "正常"
        print(f"{ip} 请求 {info['n']} 次 打分 {info['score']:.0f} -> {verdict}")
    print("线上应再叠加时段分布、点击间隔方差等信号并人工复核后再封禁")
