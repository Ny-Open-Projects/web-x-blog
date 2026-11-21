---
title: [Q1383] 配置热更新:mtime 检测与原子替换
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1383 · 配置热更新:mtime 检测与原子替换

> 难度:★★★ | 标签:配置, 热更新

**问**:配置改了不想重启进程,自己实现热更新要注意什么?

**答**:三个关键点:**检测**(定时或事件驱动比较文件 mtime/版本号,文件内容没变也别重载,可用内容哈希去抖)、**原子替换**(新配置完整加载校验通过后,才在锁内整体替换快照;加载失败沿用旧值并告警,绝不能让进程进入半新半旧状态)、**生效语义**(读方每次拿不可变快照,而不是共享可变 dict 被中途改掉)。还要注意:多个进程实例各自 reload 时间不同,存在短暂的版本不一致窗口,依赖配置做路由/限流的逻辑要容忍。k8s 环境下 ConfigMap 挂载也是符号链接替换,mtime 检测同样适用。

```python
# file: code/03_Web后端开发/q1383_hot_reload.py
"""配置热更新:mtime 检测 + 校验后原子替换快照(纯标准库)。"""
import json
import os
import tempfile
import threading
import time


class HotConfig:
    def __init__(self, path):
        self.path = path
        self._snapshot = self._load(path)
        self._mtime = os.stat(path).st_mtime_ns
        self._lock = threading.Lock()

    @staticmethod
    def _load(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)

    def maybe_reload(self):
        try:
            mtime = os.stat(self.path).st_mtime_ns
        except OSError:
            return False
        if mtime == self._mtime:
            return False
        try:
            snap = self._load(self.path)
        except (ValueError, OSError) as exc:
            print("配置损坏,沿用旧值:", exc)
            self._mtime = mtime          # 避免反复报错,等待人工修复
            return False
        with self._lock:
            self._snapshot = snap
            self._mtime = mtime
        return True

    @property
    def snapshot(self):
        with self._lock:
            return self._snapshot


tmp = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8")
json.dump({"timeout": 3, "retries": 2}, tmp)
tmp.close()
cfg = HotConfig(tmp.name)
print("初始:", cfg.snapshot)

time.sleep(0.02)
with open(tmp.name, "w", encoding="utf-8") as f:
    json.dump({"timeout": 5, "retries": 5}, f)
print("合法更新生效:", cfg.maybe_reload(), cfg.snapshot)

with open(tmp.name, "w", encoding="utf-8") as f:
    f.write("{bad json")
print("损坏配置沿用旧值:", cfg.maybe_reload() is False, cfg.snapshot)
os.unlink(tmp.name)
```

**追问**:
- 为什么先校验后替换而不是边读边改?——共享 dict 被读到一半换值会出现"timeout 新值 + retries 旧值"的杂交状态,快照替换天然避免。
- 怎么通知各模块生效?——订阅回调在锁外派发,模块自己决定是否重初始化连接池等重资源。
