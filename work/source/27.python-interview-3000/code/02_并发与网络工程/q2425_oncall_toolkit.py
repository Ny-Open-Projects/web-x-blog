# -*- coding: utf-8 -*-
"""综合设计题: 夜间值班自愈工具箱, 五个组件一条链。

- 探测带确定性故障注入与重试预算: 剧本可复现, 排障不靠抽签;
- 探测不通过就走降级缓存, 陈旧但可用的配置先顶上;
- 处置计划默认 dry-run, 审计留痕, 显式 apply 才真正执行;
- 一条链把探测、降级、处置、审计串成值班脚本的骨架。
"""
import random
import threading
import time


class ChaosInjector:
    """确定性注入: 种子定剧本, enabled 是总闸。"""

    def __init__(self, seed, fail_attempts, enabled=True):
        self.enabled = enabled
        rng = random.Random(seed)
        pool = [1, 2, 3, 4]
        rng.shuffle(pool)
        self.plan = set(pool[:fail_attempts])

    def check(self, attempt):
        if self.enabled and attempt in self.plan:
            return TimeoutError("注入故障 attempt=%d" % attempt)
        return None


class HealthProbe:
    """带预算的探测: 指数退避, 全程记尝试账。"""

    def __init__(self, injector, attempts=4, backoff=0.05):
        self.injector = injector
        self.attempts = attempts
        self.backoff = backoff

    def probe(self):
        for n in range(1, self.attempts + 1):
            exc = self.injector.check(n)
            if exc is None:
                return True, n
            print("  探测尝试 %d 失败: %s" % (n, exc))
            time.sleep(self.backoff * (2 ** (n - 1)))
        return False, self.attempts


class ConfigCache:
    """SWR 降级缓存: 上游活着时保鲜, 死了供旧值。"""

    def __init__(self):
        self.lock = threading.Lock()
        self.value = None

    def load(self, value):
        with self.lock:
            self.value = value

    def fallback(self):
        with self.lock:
            return self.value, self.value is not None


ACTIONS = {
    "restart-worker": lambda arg: "worker-%s 重启完成" % arg,
    "flush-cache": lambda arg: "缓存池 %s 已清空" % arg,
}


class Remediator:
    """处置器: dry-run 是默认, apply 是显式授权。"""

    def __init__(self, audit, effects):
        self.audit = audit
        self.effects = effects

    def remediate(self, plan, apply_mode):
        for action, arg in plan:
            if apply_mode:
                self.effects.append(ACTIONS[action](arg))
                self.audit.append("APPLY %s %s" % (action, arg))
            else:
                self.audit.append("DRY   %s %s" % (action, arg))


def nightly_round(probe, cache, remediator, healthy_config):
    """一次夜巡: 探测 -> 降级判断 -> 处置计划。"""
    ok, attempts = probe.probe()
    if ok:
        cache.load(healthy_config)
        config, stale = healthy_config, False
        plan = []
    else:
        config, stale = cache.fallback()
        plan = [("restart-worker", "a"), ("flush-cache", "main")]
        print("  探测失败, 走降级配置: %r stale=%s" % (config, stale))
    return {"healthy": ok, "attempts": attempts, "config": config,
            "stale": stale, "plan": plan}


def main():
    audit, effects = [], []
    cache = ConfigCache()
    cache.load("config-snapshot-v42")
    remediator = Remediator(audit, effects)

    # 第一夜: 服务抖动, 注入剧本 1 失败 2 失败 3 成功, 探测顶住
    print("第一夜: 服务抖动但自愈成功")
    probe1 = HealthProbe(ChaosInjector(seed=5, fail_attempts=2))
    round1 = nightly_round(probe1, cache, remediator, "config-v43")
    print("  结果:", round1)
    assert round1["healthy"] and round1["attempts"] == 3, "第 3 次探测应成功"
    assert round1["config"] == "config-v43" and not round1["stale"]
    remediator.remediate(round1["plan"], apply_mode=False)

    # 第二夜: 服务长死, 探测耗尽, 降级顶上, 处置计划 dry-run
    print("第二夜: 服务长死, 降级与 dry-run 处置")
    probe2 = HealthProbe(ChaosInjector(seed=7, fail_attempts=9))
    round2 = nightly_round(probe2, cache, remediator, "config-v43")
    print("  结果: healthy=%s config=%r stale=%s" %
          (round2["healthy"], round2["config"], round2["stale"]))
    assert not round2["healthy"], "剧本全失败, 探测必须耗尽"
    assert round2["config"] == "config-v43" and round2["stale"], \
        "降级缓存供出第一夜保鲜成功的好值"
    remediator.remediate(round2["plan"], apply_mode=False)
    assert effects == [], "dry-run 夜巡不产生任何真实变更"

    # 复盘: 值班日志两条夜巡的审计连成一条线
    print("夜巡审计:")
    for line in audit:
        print("  ", line)
    assert sum(1 for l in audit if l.startswith("DRY")) == 2, "两夜各一份计划留痕"
    assert all(l.startswith("DRY") for l in audit), "审计里不应混入未授权的 APPLY"


if __name__ == "__main__":
    main()
