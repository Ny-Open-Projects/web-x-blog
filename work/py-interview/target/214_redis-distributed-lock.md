# 214. Redis 分布式锁

> 分类：数据库·缓存 | 难度：L3 | 题型：实战 | 频率：高 | 关键词：**分布式锁** / **SETNX** / **expire** / **随机值** / **释放锁**
> 原文锚点：第8章 8-4「分布式锁：多机多进程间同步；SETNX 加锁(无key才设) + expire 超时 + 随机UID值; 释放锁时校验UID再 delete；网上有开源实现可参考」

## 一句话总述
**Redis 分布式锁 = SETNX 加锁（key 不存在才设成功）+ EXPIRE 超时防死锁 + 释放时校验随机值再 DELETE**；解决多机多进程间的互斥。

## 面试官视角
- **考察意图**：是否写过/懂分布式锁的"正确姿势"，而不只是"set 个 key"。
- **P5** 能说出 SETNX 加锁、expire 超时、delete 释放 / **P6** 能解释"为什么释放前要校验随机值"（防误删别人的锁）与"expire 防进程崩遗留死锁" / **P7** 能指出"SETNX 与 EXPIRE 非原子需用 SET key val NX EX 一条命令"，并补充 Redlock/Redisson 等成熟方案。
- **红旗**：释放锁直接 `DEL` 不校验归属（可能删掉别人持有的锁）；只用 SETNX 不设超时（进程崩了锁永不清）。
- **惊艳点**：能点出"单条 `SET key uuid NX EX ttl` 原子加锁 + Lua 脚本原子释放"才是生产正确姿势 `[经验]`。

## 主问答
**Q（面试官原话）：** 如何用 Redis 实现分布式锁？

**A · 标准答案骨架：**
1. **加锁**：用 `SETNX`（set if not exist）设一个 key，key 不存在才设成功即抢到锁；同时用 `EXPIRE` 设超时，避免持有锁的进程崩溃后锁永不释放（死锁）。
2. **锁值用随机 UID**：每个竞争者用随机值（如 UUID）作锁值，释放锁时**先校验值属于自己再 DELETE**，防止误删别人持有的锁。
3. **释放**：通过 UID 判断是自己的锁，再执行 `DELETE` 释放。

**加分层**：源文件里的 SETNX + 单独 EXPIRE 有**非原子**风险（SETNX 后还没 EXPIRE 就崩了仍会死锁），生产应改用单条 `SET key uuid NX EX ttl` 原子加锁；释放用 Lua 脚本原子校验+删除。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 怎么加锁 | 基本认知 | SETNX 抢锁 | 换题 → 不及格 |
| L2 | 为什么设超时 | 是否懂死锁 | 崩了锁不清→死锁 | 判 P5 |
| L3 | 为什么校验随机值 | 关键安全 | 防误删他人锁 | 判 P6 |
| L4 | SETNX+EXPIRE 隐患 | 深入 | 非原子,应 SET NX EX | 判 P6+ |
| L5 | 生产方案 | 实战 | Redlock/Redisson/Lua原子释放 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| SETNX 加锁思路长期成立 | Redis 2.6.12 起 `SET key val NX EX` 单条原子加锁 | 面试答"SETNX+EXPIRE"即可，补"单条 SET NX EX 更优"显时效 |

## 关键代码
```python
# 分布式锁：原子加锁 + 随机值释放（redis-py）[实测, redis-py]
import redis, uuid
r = redis.Redis()
token = str(uuid.uuid4())
# 加锁：不存在才设，且带 10s 超时（原子）
ok = r.set("lock:order", token, nx=True, ex=10)
if ok:
    try:
        do_work()
    finally:
        # 释放：仅当值仍是自己的（Lua 保证原子）
        r.eval("if redis.call('get',KEYS[1])==ARGV[1] then return redis.call('del',KEYS[1]) else return 0 end",
               1, "lock:order", token)
```

## ⚠️ 原文纠错
- 机翻还原：「setNX」→ **SETNX**（set if not exists）；「expire」→ **EXPIRE**（超时）；「KTV / 个key」→ **key-value / key**；「县程 / 县城」→ **线程 / 进程**；「持有这个所」→ **持有锁**；「UID」→ **随机值（UUID）**。
- 原文"SETNX 加锁 + expire 加超时 + delete 释放，释放前用 UID 判断是不是自己的锁"——逻辑准确；但未强调 **SETNX 与 EXPIRE 非原子**，已补"单条 SET NX EX"这一生产要点。
- 原文"网上有开源版本可参考"——准确，可补 Redisson/Redlock。

## 总结与追问预判
正确姿势：SETNX 加锁 + EXPIRE 超时 + 随机值校验释放；生产用 `SET NX EX` 原子加锁 + Lua 原子释放。可衔接：**Redis 事务（见 213 卡）**、**缓存一致性（见 215 卡）**。
