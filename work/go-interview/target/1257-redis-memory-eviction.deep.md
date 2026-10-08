## 思路与架构
```text
Redis 内存满的处理链路：
1. 写入路径：命令执行前检查 used_memory > maxmemory？
   - 否：正常执行。
   - 是：进入 eviction 流程，按 maxmemory-policy 选 victim。
2. noeviction：直接拒绝写（返回 OOM），不走淘汰。
3. allkeys-*/volatile-*：从对应 key 池按 LRU/LFU/random/ttl 近似采样挑 victim 删除，循环直到 used_memory < maxmemory 或无法释放。
4. 决策边界：volatile-* 仅含过期 key 池，若池空则退化为拒写。

记忆模型：maxmemory 是闸门、policy 是闸门后的分流规则、noeviction 是"只拦不删"、其余是"删了放行"。
```

## 方案取舍
```text
- 缓存 vs 数据源：纯缓存用 allkeys-lru/lfu（满了就逐，业务可回源）；含持久语义用 volatile-*（只逐过期项，保护未过期数据）。
- LRU vs LFU：LRU 重"最近"，抗短期热点但易误留历史长尾；LFU 重"频率"，抗突发、长期低频也逐，4.0+ 推荐。
- 是否开 maxmemory：生产必须设（防 OOM 被 OS kill），值按内存 70~80% 留碎片与峰值余量。
- noeviction 风险：写失败但数据全，适合"不能丢、可接受写阻塞"的场景。
```

## 答题技巧
```text
- 先抛结论"内存满不崩溃，看策略"，再分 noeviction（拒写保数据）vs 其他（淘汰保写但丢数据）。
- 必点版本默认：3.0 前 volatile-lru、3.0+ noeviction、4.0 加 LFU。
- 画"范围(allkeys/volatile) × 算法(lru/lfu/random/ttl) + noeviction = 8"矩阵防漏。
- 收尾落到运维：CONFIG GET/SET + redis.conf 持久化 + INFO memory 监控。
```
