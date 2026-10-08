# 195 秒杀削峰与应用层优化

> 分类：分布式 / 高并发 | 难度：L3 | 题型：架构题 | 频率：中 | 关键词：**消息队列削峰** / **批量处理** / **singleflight 合并读** / **不直接打 DB**
> 原文锚点：第 4~8、64~70 段「业务层：请求进消息队列不直接操作 DB，MQ 削峰+有序消费；应用层：订单批量合并写减少库存写、singleflight 合并库存读请求」

## 一句话总述
防超卖不止 DB 层，还有**两层减压**：业务层用**消息队列削峰**——用户请求进 MQ 而非直接打 DB，MQ 异步有序消费，把瞬时高并发转成平稳速率；应用层用**批量处理**（订单合并成一次库存扣减，减少写）和 **singleflight**（同一时刻库存读请求合并成一个，减少读）。两层都为了**降低 DB 压力**，让 DB 层锁更从容。

## 面试官视角
- 意图：考察能否给出**全链路**防超卖架构，而非只答 DB 锁——"请求 → MQ → DB 锁 → 应用层优化"是完整答案。
- P6 能说出 MQ 削峰；P7 能点出 singleflight 合并读、批量合并写这两个应用层细节，并讲清"为什么 DB 层仍需锁兜底"（MQ 消费仍可能并发）。
- 红旗：以为"进了 MQ 就不用管并发"（MQ 只是削峰，多消费者仍并发扣减）；把 singleflight 说成只用于防缓存击穿（实际库存读也适用）。
- 惊艳点：点出"singleflight 是 Go 官方扩展库 `golang.org/x/sync/singleflight`，把并发读合并成一次"，显出 Go 生态熟悉度。

## 主问答
**Q（面试官原话）：** 除了数据库加锁，秒杀系统还能怎么优化？
**A：**
1. **结论**：两层减压——业务层 MQ 削峰、应用层批量+合并读，目标都是降低 DB 压力，让 DB 层锁更从容。
2. **机制① 业务层 MQ 削峰**：用户请求**先进消息队列**，不直接操作 DB；MQ 异步、有序消费，把瞬时万级并发转成平稳速率，保护 DB 和支付系统。但注意：多消费者仍可能**并发扣减**，所以 DB 层锁必须兜底（见 195-stock-deduction-locks）。
3. **机制② 应用层批量处理**：消费订单时**合并多个库存操作为一次扣减**（如攒一批再 UPDATE），减少库存写次数。
4. **机制③ singleflight 合并读**：对"查库存"这类读请求，用 `singleflight` 把同一时刻大量相同请求**合并成一次实际查询**，其余直接拿结果，减少 DB 读压力 `[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 业务层怎么做 | 基础 | MQ 削峰不直接打 DB | 判 P5 |
| L2 | MQ 后还并发吗 | 机制 | 多消费者仍并发，DB 须兜底 | 判 P6 |
| L3 | 应用层优化 | 机制 | 批量写 + singleflight 读 | 判 P6+ |
| L4 | singleflight 原理 | 深度 | 并发读合并一次 | 判 P7 |
| L5 | 全链路架构 | 体系 | 请求→MQ→DB锁→应用层 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 1.x + x/sync | singleflight 稳定 | `golang.org/x/sync/singleflight` 合并并发调用；MQ 削峰为秒杀标准架构 `[经验]` |
| 全版本 | 无 | 批量写、合并读为通用优化，与具体 MQ 无关 |

## 关键代码
```go
import "golang.org/x/sync/singleflight"

var group singleflight.Group

// 合并"查库存"的并发读：同一 key 同一时刻只查一次 DB
func getStock(ctx context.Context, goodsID int) (int, error) {
    v, _, _ := group.Do(fmt.Sprintf("stock:%d", goodsID), func() (interface{}, error) {
        return queryStockFromDB(goodsID) // 实际只查一次
    })
    return v.(int), nil
}

// 应用层批量：消费订单合并成一次扣减（伪代码）
func consumeBatch(orders []Order) {
    ids := collectIDs(orders)
    db.Exec("UPDATE goods SET stock=stock-? WHERE id IN (?)", len(ids), ids)
}
```

## 总结与追问预判
- 两层减压：业务层 MQ 削峰（不直接打 DB，但 DB 锁仍兜底）；应用层批量写 + singleflight 合并读。
- 预判：DB 层锁 → 见 195-stock-deduction-locks；Redis 锁细节 → 见 195-redis-distlock-detail；秒杀缓存层 → 见 193-seckill-cache-design（本卡聚焦 MQ+应用层，不重产缓存设计）。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读并重点核对"业务层消息队列削峰(请求进 MQ 不直接打 DB、异步有序消费)、应用层批量处理(订单合并一次扣减减写)、singleflight 合并库存读请求减少读"的描述，与秒杀系统架构实践一致（MQ 削峰、批量写、singleflight 合并读均为公认优化手段）。仅做了 ASR 解码将源码中的若干术语崩坏词统一还原为规范术语，技术结论未做更正。源码将若干标识符音译为崩坏词，本卡统一为规范术语 `[经验]`。
