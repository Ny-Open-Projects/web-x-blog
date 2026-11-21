---
title: [Q2298] Agent 配置热更新:版本快照与原子替换
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2298 · Agent 配置热更新:版本快照与原子替换

> 难度:★★★★ | 标签:Agent, 配置, 工程化

**问**:线上 Agent 的 top_k、超时、模型名要改,又不能重启服务,怎么保证改的瞬间不出"半个新半个旧"的请求?

**答**:配置中心维护不可变快照,更新时构造新快照后一次引用替换——Python 赋值是原子的,读者要么看到完整旧版要么看到完整新版,不存在中间态。关键语义是在途隔离:请求开始时抓一个快照引用,后续配置怎么变都与本请求无关,一次请求从头到尾看到的配置自洽。更新前先校验:必填键缺失、字符串空值直接拒绝,非法配置根本进不了线上。回滚也是一次前滚更新:把旧值再 update 一遍,版本号继续单调递增,永远可审计,不做"把版本号拨回去"这种破坏单调性的事。

```python
# file: code/06_Agent与LLM及系统设计/q2298_config_hot_reload.py
"""Agent 配置热更新:版本号单调递增 原子替换快照 在途请求绑定旧快照跑完。"""


class ConfigCenter:
    def __init__(self, initial):
        self._snap = {"ver": 1, "cfg": dict(initial)}

    def snapshot(self):
        return self._snap

    def update(self, patch, required=()):
        missing = [k for k in required if k not in patch and k not in self._snap["cfg"]]
        blank = [k for k, v in patch.items() if isinstance(v, str) and not v.strip()]
        if missing or blank:
            raise ValueError("非法配置 缺失=%s 空值=%s" % (missing, blank))
        new_cfg = dict(self._snap["cfg"])
        new_cfg.update(patch)
        self._snap = {"ver": self._snap["ver"] + 1, "cfg": new_cfg}
        return self._snap["ver"]


if __name__ == "__main__":
    cc = ConfigCenter({"model": "m1", "top_k": 5, "timeout_s": 30})
    snap1 = cc.snapshot()
    assert snap1["ver"] == 1
    v2 = cc.update({"top_k": 9})
    assert v2 == 2
    assert snap1["cfg"]["top_k"] == 5, "在途请求持有旧快照 不受热更影响"
    assert cc.snapshot()["cfg"]["top_k"] == 9, "新请求即刻看到新配置"
    try:
        cc.update({"model": "   "}, required=("model",))
        raise SystemExit("空值配置应被拒")
    except ValueError:
        pass
    v3 = cc.update({"top_k": 5})
    assert v3 == 3 and cc.snapshot()["cfg"]["top_k"] == 5, "回滚也是一次前滚更新 版本只增不减"
    try:
        cc.update({"missing_key": 1}, required=("model", "temperature"))
        raise SystemExit("缺失必填应被拒")
    except ValueError as e:
        assert "temperature" in str(e)
    print("配置热更新通过:版本快照 原子替换 在途隔离 校验拒非法")
```

**追问**:
- 多进程部署怎么同步? 答:进程订阅版本号广播或轮询拉取,各自本地换绑快照,版本号对齐即视为一致
- 配置改坏了怎么快速止损? 答:保留最近 N 版快照内存驻留,一键 update 回上一版内容,秒级生效
