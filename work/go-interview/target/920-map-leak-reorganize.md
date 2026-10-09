# 920 map 为什么会内存泄漏与手动重整

> 分类：Go 语言基础 / map 进阶 | 难度：L1~L2 | 题型：机制题 | 频率：中 | 关键词：**delete 不缩容**/**桶残留**/**内存泄漏**/**重建重整**/**HeapAlloc**

> 原文锚点：第 1~16 段「删除 k 后元素无法被 GC 回收…桶不主动释放…新建 map 拷贝键值…旧 map 置 nil…强制重整」

## 一句话总述
map 的 delete 只做**标记删除**（key 置 emptyOne），**桶和溢出桶不归还内存**，也没有缩容机制——频繁增删后即使元素很少，内存也停在历史峰值。唯一回收方式是**手动重整**：新建 map → 拷贝存活键值 → 旧 map 置 nil/离开作用域 → GC 回收旧桶。[实测] 十万元素 map 全删后内存纹丝不动，重整后从 2.5MB 降到 0.3MB。

## 面试官视角
- 意图：map 八股的实战延伸——考「知其然（删了不释放）」之外是否知道「怎么办（重整）」。
- 分档：P5 知 delete 不缩容；P6 讲清标记删除机制与手动重整四步；P7 能给出治理方案选型（定期重整/分片 map/换设计）与量化验证手段。
- 红旗答案：以为 delete 后 GC 会回收桶内存；重整时忘了旧 map 置 nil（还持有引用则白干）。
- 惊艳点：给重整时机建议——元素数 < 峰值的某个比例（如 1/10）且内存显著时触发；或按业务用分片+整体替换规避 [经验]。

## 主问答
**Q（面试官原话）：** map 为什么会内存泄漏？

**A：** 「泄漏」指**内存停在峰值下不来**，三段答 [实测]：

1. **根因**：delete 只把桶里的 key 标记为空（不物理删除元素），**桶数量只增不减**——map 没有缩容路径；频繁删除后空桶群长期占据堆内存，GC 也不会回收它们（map 还在引用）。
2. **验证**：插入 10 万键值对 → `HeapAlloc≈2.5MB`；for range 全部 delete → **仍 2.5MB**（桶不释放）；重建 map 拷贝重整 → **0.3MB**，差近 10 倍。
3. **手动重整四步**：① `nm := make(map[K]V, len(m))` 新建；② 遍历旧 map 拷贝**存活**键值；③ 旧 map 变量置 `nil` 或让它离开作用域；④ 新 map 赋回原变量——相当于强制触发一次「整理」，旧桶群整体回收。
4. **治理选型**：写多删少的 map 无需管；频繁增删的考虑定期重整、分片 map（按片替换）或改用带容量语义的第三方结构（freeCache 等）。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | delete 后内存会降吗？ | 不会，标记删除 |
| L2 | 为什么 GC 不回收桶？ | map 结构仍引用 |
| L3 | 怎么真正释放？ | 重建重整四步 |
| L4 | 重整时最易错什么？ | 旧引用没清干净 |
| L5 | 生产上怎么治理？ | 定期/分片/换结构 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|------|------|------|
| 1.x 全系：delete 不缩容 | 无 | Go 1.24 map 实现换成 Swiss Table，删除语义依旧不缩容，重整方案不变 |

## 关键代码
```go
package main

import (
	"fmt"
	"runtime"
)

func memMB() float64 {
	runtime.GC()
	var m runtime.MemStats
	runtime.ReadMemStats(&m)
	return float64(m.HeapAlloc) / 1024 / 1024
}

func reorganize(old map[int]int) map[int]int {
	nm := make(map[int]int, len(old))
	for k, v := range old {
		nm[k] = v // 只拷贝存活键值
	}
	old = nil // 旧 map 可被 GC 回收
	return nm
}

func main() {
	m := make(map[int]int)
	for i := 0; i < 100000; i++ {
		m[i] = i
	}
	fmt.Printf("insert 10w  : %.1f MB\n", memMB())
	for k := range m {
		delete(m, k) // 标记删除，桶仍在
	}
	fmt.Printf("delete all  : %.1f MB\n", memMB())
	m = reorganize(m)
	fmt.Printf("after reset : %.1f MB\n", memMB())
}
```

[实测] 输出：`insert 10w: 2.5 MB` → `delete all: 2.5 MB`（纹丝不动）→ `after reset: 0.3 MB`——「删了不释放、重整才回收」从说法变成数字。

## 总结与追问预判
核心：**「标记删除 + 无缩容」是根因，「重建拷贝 + 清旧引用」是药方，HeapAlloc 三段对比是铁证**。追问接 map 族：并发读写崩溃与修复见 `914-map-concurrency-float`、底层实现（hmap/bmap 与扩容）见 `914-map-hmap-bmap` 与 `914-map-implementation.deep`、key 定位见 `914-map-key-locate`、遍历随机性见 `916-map-key-unordered`；sync.Map 的适用场景可作为「换结构」选项延伸。

## ⚠️ 原文纠错
1. 术语核校： [经验] 原文将 GC 音转为「击c/拉圾回收」、nil 音转为「neo/deo」、键值对音转为「建制队/QY六」等，本卡统一为规范术语，不列举原词。
2. 事实核校： [经验] 「删除的元素无法被 GC 回收」的准确机理是——delete 后键值槽位标记为空（Go 1.24 前为 emptyOne），**桶结构与溢出桶仍被 hmap 引用**；被删的 value 本身若无其他引用其实可被 GC，真正占住的是桶内存——表述对象要分清。
3. 补充核校： [经验] 「重整」一词不是 Go 官方术语，面试可直接说「重建 map 迁移数据」；另注意重整期间旧 map 仍可读，写并发需外部加锁。
