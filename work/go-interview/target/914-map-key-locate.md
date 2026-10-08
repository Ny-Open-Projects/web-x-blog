# 914 map 的 key 定位与读写流程

> 分类：Go/运行时 | 难度：L3 | 题型：原理题 | 频率：高 | 关键词：**低 B 位定桶** / **高 8 位 top hash** / **溢出链遍历** / **最差 O(N)**
> 原文锚点：第 42~58 段「k 哈希64位：低 B 位定桶号、高 8 位 top hash 定桶内位置；写:定位桶→比 top hash→满则 overflow；读:哈希→低B位定桶→高8位找 top hash→比 key→溢出链遍历；冲突多最差 O(N)」

## 一句话总述
map 用 key 的 **64 位哈希值**定位：**低 B 位**决定落在哪个桶（桶数 2^B），**高 8 位（top hash）**决定在桶内的位置。写入先算哈希定桶，再比 top hash 找空位，桶满走 overflow 链；读取同理，比完 top hash 再比完整 key，命中取 value，未命中沿 overflow 链表继续。哈希冲突严重时退化为遍历，**最差复杂度 O(N)**。

## 面试官视角
- 意图：考察能否讲清"key 怎么落到具体存储位置"——是 map 原理题的核心机制。
- P6 能说出"低 B 位定桶、高 8 位定桶内"；P7 能完整描述读写流程 + "top hash 先筛、再比完整 key"的优化 + 最差 O(N)。
- 红旗：以为定位只看一次哈希就直接命中（忽略 top hash 二次筛选和 overflow 链）；以为 map 查找恒为 O(1)（冲突多退化为 O(N)）。
- 惊艳点：点出"top hash 高 8 位先粗筛，减少完整 key 比较次数"，显出对性能细节的理解。

## 主问答
**Q（面试官原话）：** 往 map 里放/取一个 key，底层是怎么定位的？
**A：**
1. **结论**：key 经哈希得 64 位值，**低 B 位**选桶（桶数 2^B），**高 8 位**作 top hash 在桶内定位。
2. **机制（写入）**：算哈希 → 低 B 位找到目标桶 → 比 top hash 找空槽放 key/value；若桶满，沿 **overflow 链**找/新建溢出桶再放。
3. **机制（读取）**：算哈希 → 低 B 位定桶 → 比 top hash 粗筛候选 → 再比**完整 key** 确认；命中取 value，未命中沿 overflow 链表继续，直到找到或遍历完。
4. **边界（复杂度）**：正常均摊 **O(1)**；但多个 key 哈希冲突挤同一桶/链时，读取需遍历该链，**最差 O(N)**（N 为元素数）`[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 低B位干啥 | 基础 | 定桶号 | 判 P5 |
| L2 | 高8位干啥 | 机制 | top hash 定桶内 | 判 P6 |
| L3 | 读写流程 | 机制 | 哈希→桶→top hash→key | 判 P6+ |
| L4 | 冲突怎么办 | 深度 | overflow 链遍历 | 判 P7 |
| L5 | 复杂度 | 体系 | 均摊O(1)最差O(N) | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 1.0 ~ 1.22+ | 无 | 低 B 位定桶、高 8 位 top hash、overflow 链、最差 O(N) 恒定 `[经验]` |

## 关键代码
```go
// map 定位示意（伪代码，对应 runtime 查找逻辑）
func lookup(m *hmap, key Key) (Value, bool) {
    h := hash(key)         // 64 位哈希
    b := h & (m.Bmask)     // 低 B 位 → 桶下标（桶数 2^B）
    bucket := addr(m.buckets, b)
    top := uint8(h >> 56)  // 高 8 位 → top hash
    for bucket != nil {
        for i := 0; i < bucketCnt; i++ {
            if bucket.tophash[i] == top && equal(bucket.keys[i], key) {
                return bucket.values[i], true // 先比 top 再比完整 key
            }
        }
        bucket = bucket.overflow // 沿溢出链继续
    }
    return zero, false
}
```

## 总结与追责预判
- 定位：低 B 位定桶、高 8 位 top hash 定桶内；写满走 overflow；读比 top hash 再比 key；均摊 O(1) 最差 O(N)。
- 预判：底层结构 → 见 914-map-hmap-bmap；注意事项 → 见 914-map-concurrency-float；哈希 vs 树 → 见 1218-hash-bst-limits。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读并重点核对"key 哈希64位、低 B 位定桶号、高 8 位 top hash 定桶内位置、写入定位桶比 top hash 满则 overflow、读取比 top hash 再比完整 key 沿溢出链遍历、冲突多最差 O(N)"的描述，与 Go map 查找/插入逻辑一致（runtime 用低位选桶、tophash 粗筛、overflow 链解决溢出）。仅做了 ASR 解码将源码中的若干术语崩坏词统一还原为规范术语，技术结论未做更正。源码将若干标识符音译为崩坏词，本卡统一为规范术语 `[经验]`。
