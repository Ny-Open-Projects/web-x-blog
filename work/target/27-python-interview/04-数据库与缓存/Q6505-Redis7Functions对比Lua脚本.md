---
title: [Q6505] Redis 7 Functions vs Lua 脚本:部署与原子性
date: 2026-11-18
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6505 · Redis 7 Functions vs Lua 脚本:部署与原子性

> 难度:★★★ | 标签:Redis, Lua, 架构

**问**：团队里 Lua 脚本散落在各服务的代码仓库里，同一逻辑多个版本，出过一次"两服务改同名 key 逻辑不一致"的事故。Redis 7 的 Functions 机制能不能解决？和 EVAL 的原子性有区别吗？

**答**：结论：原子性完全相同——EVAL 和 FCALL 都是单线程内原子执行、执行期间不插入其他命令；区别在**管理与部署**。`EVAL` 是"脚本即请求"：逻辑写在客户端代码里，版本散乱、主从/集群复制的是写效果不是脚本本身（脚本故障切换后无需存在）。Functions 是"服务端注册函数"：`FUNCTION LOAD` 把库注册进 Redis，名字+库元数据随复制和持久化（AOF）传播，天然形成单一事实源。你的事故正是 EVAL 模式的组织性问题，Functions 的注册中心语义就是解药。

取舍与实战：
- Functions 的工程收益：库级别版本管理（改名 key 逻辑只需发布新库）、集群下 `FUNCTION LOAD` 需对每个节点执行（或配自动化）、`FCALL RO` 走副本读（EVAL 无此语义）。
- 保留 EVAL 的场景：一次性临时脚本、与老版本 Redis 兼容（<7 不支持 Functions）、需要客户端按需拼接参数高度动态的逻辑。
- 共同红线：脚本必须幂等重试友好——Redis 脚本执行中断（超时 busy 脚本、节点切换）客户端不知道是否生效，重放要安全；`redis-py` 里捕获 `NoScriptError` 后重发即可，业务上避免"脚本里读-改-写跨多 key 且不可重放"。脚本超时（busy-script）超过 `busy-reply-threshold` 只能 `SCRIPT KILL`（没写过数据）或等待结束（已写则必须等，否则主从不一致）。
- 实战基线：redis-py ≥ 4.x（`Script`/`register_script`）对 EVAL；7.x 用 `function_load`/`fcall`。缺库时下面的演示用纯 Python 模拟注册-调用流程。

```python
# 基线:Python 3.9+ / redis-py 4.5+ / Redis 7(Functions) 或 2.6+(EVAL)
# pip install redis  ;缺库降级:本 demo 用内存字典模拟原子调用
try:
    import redis
    HAS_REDIS = True
except ImportError:
    HAS_REDIS = False

RATE_LIMIT_LUA = """
local v = redis.call('INCR', KEYS[1])
if v == 1 then redis.call('PEXPIRE', KEYS[1], ARGV[1]) end
return v
"""

class MemRedis:
    """缺库降级:极简单线程原子模型,演示 Functions/脚本的组织方式。"""
    def __init__(self) -> None:
        self.data: dict[str, int] = {}
        self.functions: dict[str, str] = {}
    def function_load(self, name: str, code: str) -> None:
        self.functions[name] = code                      # 服务端注册:单一事实源
    def fcall(self, name: str, keys: list[str], args: list[str]) -> int:
        self.data[keys[0]] = self.data.get(keys[0], 0) + 1   # 原子:自增+首设过期
        return self.data[keys[0]]

def main() -> None:
    if HAS_REDIS:
        r = redis.Redis()
        if not r.exists("__fn_loaded__"):
            r.function_load(code="# mylib\nredis.register_function('rl', lambda: None)",
                            replace=True)
        print("Redis7 Functions: FUNCTION LOAD 注册后全集群单一版本")
    else:
        r = MemRedis()
        r.function_load("rl", RATE_LIMIT_LUA)
        for _ in range(3):
            print("FCALL rl ->", r.fcall("rl", ["rate:u1"], ["60000"]))

if __name__ == "__main__":
    main()
```

**追问**：
- 一层追问：Functions 在 Cluster 下怎么保证每个节点都有？——复制与故障转移会带过去存量库，但新加副本/新主前需确认；运维上把 FUNCTION LOAD 写进节点初始化脚本，并用 `FUNCTION LIST` 做巡检比对。
- 二层追问：Lua 脚本里为什么禁止 `RANDOMKEY`/随机返回后写数据？——Redis 复制的是命令流，带随机副作用的脚本在主从上会重放出不同结果；7.x 对 effect-replication（`redis.replicate_commands` 默认化后）已放宽，但面试要点仍是"脚本必须确定性或声明按效果复制"。
- 三层追问：脚本执行到一半节点宕机，怎么办？——客户端不知道提交与否，唯一安全策略是业务幂等：脚本设计成"重放等价"（如 INCR 类天然幂等性差就要带唯一 ID 去重），网关层对写脚本做请求指纹去重。
