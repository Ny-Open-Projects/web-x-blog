# 177 Go Set 内存与版本差异 深挖

> 覆盖源 17-7 全文：空结构体零尺寸验证 + RWMutex 并发 set + 删除内存不回收坑 + Go 版本差异。主卡已给实现总览，本附录做"部分删除不回收根因"与"版本差异规避"。

## 思路与架构

```text
map 删除内存行为
├─ 部分删除: 只清 entry, hmap buckets 不缩容 → 内存不回收
├─ 全删/nil: bucket 可整体回收 → 内存回落
└─ 版本差异: 低版(如1.11)全删也不回收, 与编译器/OS/CPU 相关
```

## 方案取舍
- **为什么部分删除不回收**：map 底层 hmap 的 bucket 数组在删除时不会缩容，仅把对应槽位标记空；已分配 bucket 内存保留给后续插入复用，故删除一半键值内存不变 [经验]。
- **版本差异根因**：低版本 runtime 对"全删后的 bucket"回收策略更保守（甚至不回收），高版本在 key 全清后会释放；行为受 Go 版本/OS/CPU 架构影响，不能假定 [经验]。
- **规避内存泄漏**：定期 `make` 新 map 替换旧 map（旧 map 无引用后 GC 回收）；或写多删多场景用 `sync.Map`（但其自身有额外开销，非银弹）。

## 答题技巧
- 被问"删元素内存降吗"按层答：部分不回收 → 全删/nil 才回 → 低版全删也不回 [经验]。
- 主动边界到 `910`(空结构体尺寸)、`914`(map 原理)，构成 set 全栈 [边界]。

## 细节与核心 API

```go
// 经典 set：map[K]struct{}（value 为零尺寸，仅占 key 内存，无 value 开销）
set := map[string]struct{}{}
set["a"] = struct{}{}
if _, ok := set["a"]; ok { /* 存在 */ }
delete(set, "a")
// 内存：value 是 struct{}（0 字节），比 map[K]bool 省一个字节/项；runtime 用 zerobase 共享
// 版本差异：
//  - Go <1.24：手写 map[K]struct{} 或第三方泛型 set（如 deckarep/golang-set）
//  - Go 1.24+：标准库新增 maps 包（maps.Keys/Values/Clone 等），官方泛型容器生态完善
// 注意：map 遍历无序；并发要用 sync.Map 或加锁，不能多 goroutine 并发写
```
