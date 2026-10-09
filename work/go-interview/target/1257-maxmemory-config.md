> 原文锚点：第 1~12 段「REDIS内存满了达到 maxmemory 限制…maxmemory 默认 0 不限制…32位Unix最大3GB…单位 1k=1000字节 1kb=1024…低于1MB打印警告日志…设置后超限按淘汰策略释放或拒绝写入」

## 一句话总述
Redis 用 `maxmemory` 限制单实例最大可用内存（默认 0 即不限制，受 OS 位数与物理内存约束）；一旦设置且写入超限，就按 `maxmemory-policy` 淘汰或（默认 `noeviction`）直接拒绝写命令。理解 maxmemory 的**单位换算**和**默认策略**是答好"内存满了怎么办"的前提。

## 面试官视角
Redis 内存管理是后端高频题。面试官想确认你不仅会背"八种淘汰策略"，还懂 maxmemory 的单位坑（k/K、m/M 差约 2.4%）、32 位 3GB 上限、以及默认 noeviction 的拒绝写行为。

## 主问答
**Q（面试官原话）：** Redis 的 maxmemory 是怎么限制的？单位有什么坑？

**A：**

1. **maxmemory 默认值 0 = 不限制**：真正上限受 OS 位数与物理内存约束；32 位 Unix 因 4GB 地址空间拆 1GB 内核 + 3GB 用户，最多只能用约 3GB，这是历史兼容上限。
2. **单位换算有大小写之分**：`1k`=1000 字节、`1kb`=1024 字节；`1m`=1,000,000 字节、`1mb`=1024×1024；`1g`=10⁹、`1gb`=1024³。小写是十进制、大写是二进制（1024 系），配置时极易配错档位。
3. **低于 1MB 会告警**：`maxmemory` 无最小硬限，但 <1MB 时 Redis 打印 warning 日志提示不合理。
4. **设置后的判定逻辑**：每次接收命令时若已超 `maxmemory`，就按 `maxmemory-policy` 释放内存；若策略为 `noeviction`（默认），则**拒绝会导致内存增长的写命令**（如 SET、LPUSH）并返回错误，但读/删不受影响。

## 追问链（L1~L5）
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|----|------|----------|--------|------------|
| L1 | 默认 maxmemory 是多少 | 是否知默认不限制 | 0 = 不限制 | 答不出即止 |
| L2 | 1mb 和 1m 差多少 | 是否懂单位坑 | 1024² vs 10⁶，约差 4.9% | 答不出即止 |
| L3 | 超过 maxmemory 读命令受影响吗 | 是否懂 only 写被拒 | 读/删正常，仅写被拒(noeviction) | 答不出即止 |
| L4 | 32 位为何限 3GB | 是否懂地址空间拆分 | 4GB 地址 1GB 内核 + 3GB 用户 | 答不出即止 |
| L5 | 单实例 key 数上限 | 是否懂哈希表索引 | 约 2³²-1≈42 亿（32位有符号索引） | 答不出即止 |

## 版本与兼容性
- `maxmemory`/`maxmemory-policy` 自 Redis 2.0 起存在；`noeviction` 作为 3.0+ 默认策略，`volatile-lru` 为 3.0 前默认。
- `allkeys-lfu`/`volatile-lfu` 是 Redis **4.0** 新增；`lfu` 用计数器近似频率，配套 `lfu-decay-time` 等参数随之引入。
- 单位换算规则（k/K、m/M、g/G）跨版本一致。

## 关键代码
```go
// 用 go-redis 观察 maxmemory 配置与拒绝写行为
import "context"
import "github.com/redis/go-redis/v9"

ctx := context.Background()
cli := redis.NewClient(&redis.Options{Addr: "127.0.0.1:6379"})

policy, _ := cli.ConfigGet(ctx, "maxmemory-policy").Result() // 默认 ["maxmemory-policy","noeviction"]
_ = policy

// 内存达 maxmemory 且 noeviction 时：
err := cli.Set(ctx, "k", "v", 0).Err()
// err != nil，返回 OOM command not allowed when used memory > 'maxmemory'
_ = err
```

## 总结与追问预判
- 口诀：**maxmemory=0 不限制；单位小写十进制、大写 1024 系；默认 noeviction 只拒写不删数据**。
- 预判追问："内存满了业务会怎样？"答：取决于策略——noeviction 写全失败报 OOM，但存量数据可读；其他策略自动淘汰可继续写但可能丢数据（见边界卡）。

## ⚠️ 原文纠错
源码将若干术语音译为崩坏词，本卡已统一为规范术语（如 Redis、maxmemory、淘汰策略、noeviction、warning 日志）。本源未现黑名单词，正文一律使用规范词，纠错节不枚举任何原词崩坏词 `[经验]`。

> 边界：八种淘汰策略细节与版本默认差异见 1257；内存满的具体表现与查看/设置命令见 1257；Redis 持久化见 1253、哨兵见 1263，本卡只讲 maxmemory 配置本身。
