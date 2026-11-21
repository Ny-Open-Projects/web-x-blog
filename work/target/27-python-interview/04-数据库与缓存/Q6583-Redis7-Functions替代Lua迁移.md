---
title: [Q6583] Redis 7 Functions 替代 Lua 迁移
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6583 · Redis 7 Functions 替代 Lua 脚本的迁移与取舍

难度：P6 ｜ 标签：Redis 7 / Lua / Functions / 版本演进

**问**：团队存量代码里有几十段 `EVAL` 内联 Lua（redis-py 里 `register_script`），升级 Redis 7 后想迁到 Functions（`FUNCTION LOAD`），迁移的收益、破坏点和回滚路径是什么？

**答**：
- **结论**：Functions 的价值是把脚本变成"库"：以库为单位命名（`fcall mylib.func`）、随副本复制（不再要求每个客户端内置相同脚本）、可持久化并在 failover 后自动加载，解决了 EVAL "脚本漂移"（各环境脚本版本不一致）的老问题。迁移破坏点：① `EVAL` 的 KEYS/ARGV 约定不变，但调用入口从 `eval` 变成 `fcall name nkeys keys...`，redis-py 的 `register_script` 不适用于 Functions，要换 `function_load` + `fcall`；② Functions 默认无写权限边界，加载用 `REPLACE` 时要注意幂等；③ 只支持 Lua 引擎（Redis 7），别指望 JS；④ 8.0 起有 Vector Sets 等新模块但脚本引擎仍是 Lua 5.1。
- **取舍**：不急着全量迁：短小、单点使用的脚本留 EVAL 成本最低；被多服务共享、有版本管理诉求的脚本（限流器、分布式锁逻辑）迁 Functions 收益最大。风险对冲：迁移期同时保留 EVAL 旧路径，用开关切换，Functions 库用 `FCALL` 失败时回退 EVAL——但注意两条路径必须操作相同的 key 布局，否则会出现"一半逻辑在缓存一半在脚本"的不一致。
- **实战**：迁移步骤：① 盘点所有 `register_script`/`eval` 调用点，按"共享程度"分级；② 编写 `.lua` 库文件（`#!lua name=mylib`），CI 里用 redis-testcontainers 做 `FUNCTION LOAD REPLACE` 的回归；③ 灰度按服务切换 `fcall`，观察 `info commandstats` 里 fcall 与 eval 的调用占比；④ 复盘项：Functions 库纳入版本管理（与代码同仓库），加载动作做成部署流水线的一步而非手工操作。

```python
# EVAL -> Functions 迁移的双路径封装与降级（标准库 + 可选 redis-py 5.x）
# 基线：Python 3.9+ / redis-py 5.x（Redis 7+）；缺库自动降级为内存模拟

import json


class ScriptRouter:
    """fcall 优先，失败回退 eval；保证 key 布局一致"""

    def __init__(self, redis_client=None) -> None:
        self.r = redis_client  # None 时用内存模拟
        self.loaded: dict[str, str] = {}

    def load(self, name: str, code: str) -> None:
        self.loaded[name] = code  # 真实环境: FUNCTION LOAD REPLACE code

    def run(self, func: str, keys: list[str], args: list) -> object:
        try:
            return self._fcall(func, keys, args)
        except KeyError:
            return self._eval(self.loaded["__legacy__"], keys, args)

    def _fcall(self, func, keys, args):
        if self.r is None:
            if func not in self.loaded:
                raise KeyError(func)
            return {"via": "functions", "func": func,
                    "keys": keys, "args": args}
        return self.r.fcall(func, len(keys), *keys, *args)

    def _eval(self, code, keys, args):
        if self.r is None:
            return {"via": "eval", "keys": keys, "args": args}
        return self.r.eval(code, len(keys), *keys, *args)


def main() -> None:
    router = ScriptRouter()  # 演示用内存模拟；生产传 redis.Redis(...)
    router.load("rate_limit", "-- 限流脚本正文，此处省略")
    out = router.run("rate_limit", ["rl:u42"], [10, 1])
    print(json.dumps(out, ensure_ascii=False))
    assert out["via"] == "functions"
    # 未加载的 func 触发回退
    router.loaded["__legacy__"] = "return 1"
    out2 = router.run("missing_func", ["k1"], [])
    assert out2["via"] == "eval"
    print("OK: functions 优先、eval 回退")


if __name__ == "__main__":
    main()
```

**追问 1**：Functions 为什么解决了 EVAL 的"脚本漂移"问题？
→ 一句话提示：EVAL 要求每个客户端持有相同脚本正文，脚本按内容哈希存在脚本缓存里，各环境可能版本不一；Functions 把脚本作为服务端命名对象持久化，客户端只引用名字，版本收敛到服务端。

**追问 2**：脚本执行和 MULTI/EXEC 事务、Pipeline 的并发语义有什么区别？
→ 一句话提示：脚本和事务一样是原子串行执行（期间不插入其他命令）；Pipeline 只省网络往返、不保证原子；把"多条命令打包"当原子性用是经典事故。

## 背诵要点
- Functions = 命名化、随副本复制、failover 自动加载的脚本库；客户端入口从 eval 换 fcall，redis-py register_script 不适用。
- 迁移分级：共享/有版本诉求的迁，单点短脚本留 EVAL；双路径切换必须同 key 布局。
- 收敛验证看 `info commandstats` 的 fcall/eval 占比；FUNCTION LOAD REPLACE 要进 CI 与部署流水线。

## 复盘追问
- 脚本里做了阻塞操作（大循环、Lua 端大排序）会怎样？提示：脚本原子执行期间整个实例单线程被占住，等价于一次 O(N) 慢命令，Q6561 的 Lua 长脚本阻塞就是这类事故。
- FUNCTION LOAD 在 Cluster 里怎么传播？提示：脚本以库为单位复制到所有节点，但仍要注意 reshard 后跨节点 key 访问与脚本内 key 参数（必须用 KEYS 传 key，不能硬编码 key 名，否则 Cluster 下行为未定义）。
