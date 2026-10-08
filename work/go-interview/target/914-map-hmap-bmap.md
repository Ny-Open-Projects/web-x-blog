# 914 Go map 底层结构：hmap 与 bmap

> 分类：Go/运行时 | 难度：L3 | 题型：原理题 | 频率：高 | 关键词：**hmap** / **bmap** / **bucket** / **top hash** / **溢出桶**
> 原文锚点：第 13~41 段「hmap(count/B/oldbuckets/overflow/nevacuate/extra)；bmap(top hash 高8位+keys[8]+values[8]，bucketCnt=8)；溢出 overflow 链表；B 决定桶数=2^B」

## 一句话总述
Go map 底层是**哈希查找表**，核心结构 **hmap**：`count`(元素数)、`B`(桶数=2^B)、`buckets`(指向 bmap 数组)、`oldbuckets`(扩容前旧桶)、`overflow`(溢出桶)、`nevacuate`(迁移进度)、`extra`(溢出相关附加字段)。每个 **bmap**（桶）存 **top hash 数组（key 哈希高 8 位）+ keys 数组(8) + values 数组(8)**，`bucketCnt=8`；桶满则用 **overflow 指针**串成链表——这就是 Go 用**链表法**解决哈希冲突。

## 面试官视角
- 意图：考察对 map 底层数据结构的**精确掌握**，是 map 题的"地基"。
- P6 能说出 hmap 含 buckets 数组、bmap 存 8 个键值对 + top hash；P7 能讲清 top hash（高 8 位）的作用、bucketCnt=8、溢出桶链表。
- 红旗：以为 map 是红黑树（Go 用哈希表+链表法，不是树）；忽略 top hash 是"高 8 位"用于快速比对。
- 惊艳点：点出"哈希冲突解决用链表法（非开放地址法）、bmap 用 top hash 避免每次都比较完整 key"，显出源码级理解（对比 1218 哈希 vs 搜索树选型）。

## 主问答
**Q（面试官原话）：** Go 的 map 底层是怎么实现的？结构体长啥样？
**A：**
1. **结论**：Go map 是**哈希查找表**，用**链表法**解决冲突。顶层 `hmap` 管元信息，`buckets` 指向 `bmap` 数组（长度 2^B），每个 `bmap` 是一个桶。
2. **机制（hmap 字段）**：`count` 元素数；`B` 桶数指数（桶数=2^B）；`buckets` 指向 bmap 数组；`oldbuckets` 指向扩容前的旧桶；`nevacuate` 记录迁移进度；`overflow`/`extra` 管理溢出桶。
3. **机制（bmap 结构）**：每个桶含 **top hash 数组（8 个，存 key 哈希高 8 位）** + **keys 数组（8 个）** + **values 数组（8 个）**，`bucketCnt=8`（一个桶最多 8 对）。桶满时通过 **overflow 指针**挂溢出桶，形成链表。`top hash` 用于快速比对——先比高 8 位再比完整 key，省去每次比较长 key `[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 哈希还是树 | 基础 | 哈希表+链表法 | 判 P5 |
| L2 | hmap 有哪些字段 | 机制 | count/B/buckets/oldbuckets | 判 P6 |
| L3 | bmap 存什么 | 机制 | top hash+keys[8]+vals[8] | 判 P6+ |
| L4 | top hash 作用 | 深度 | 高8位快速比对 | 判 P7 |
| L5 | 冲突怎么解 | 体系 | 链表法+溢出桶 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 1.0 ~ 1.22+ | 无 | hmap/bmap 结构、bucketCnt=8、链表法冲突解决恒定（runtime/map.go） `[经验]` |

## 关键代码
```go
// runtime/map.go 核心结构（精简）
type hmap struct {
    count    int    // 元素个数
    B        uint8  // 桶数 = 2^B
    buckets  unsafe.Pointer // 指向 bmap 数组(长度 2^B)
    oldbuckets unsafe.Pointer // 扩容前的旧桶
    nevacuate uintptr        // 已迁移的桶数(迁移进度)
    // extra 存溢出桶等附加字段
}
type bmap struct {
    tophash [8]uint8 // 每个 key 哈希的高 8 位
    // 紧跟：keys[8] + values[8] + overflow 指针(溢出桶链表)
}
const bucketCnt = 8 // 每桶最多 8 对键值
```

## 总结与追问预判
- hmap(buckets 数组, 桶数 2^B) + bmap(top hash+keys[8]+vals[8], 桶满挂 overflow 链表)；链表法解冲突。
- 预判：k 定位算法 → 见 914-map-key-locate；并发/注意事项 → 见 914-map-concurrency-float；哈希 vs 搜索树 → 见 1218-hash-bst-limits（本卡讲 Go 具体结构）。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读并重点核对"Go map 用哈希查找表+链表法、hmap 含 count/B/buckets/oldbuckets/overflow/nevacuate/extra、bmap 含 top hash(高8位)+keys[8]+values[8]、bucketCnt=8、桶满用 overflow 链表"的描述，与 Go runtime/map.go 的 hmap/bmap 实现一致（bmap 确有 tophash 数组、bucketCnt=8、溢出桶链表）。仅做了 ASR 解码将源码中的若干术语崩坏词统一还原为规范术语，技术结论未做更正。源码将若干标识符音译为崩坏词，本卡统一为规范术语 `[经验]`。
