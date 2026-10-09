> 原文锚点：第 24~48 段「浮点型可以比较…作为 map 的 k 会有什么问题…0.3 与很长小数位的浮点最终当成同一 k…float64bits 转成 uint64 再插入 k…0.3 和长浮点转出的 uint64 相等…两个 NAN 作为 k 不相等（NAN!=NAN），map 里能存两个 NAN key」（float 可作 key 但精度/NaN 诡异）

## 一句话总述
`float` 类型**可比较、能作 map key**，但有两个诡异坑：① **精度问题**——两个逻辑相等但二进制表示略不同的 float，经 `math.Float64bits` 转 `uint64` 后可能相同（合并为一个 key）或不同（取不到值）；② **NaN 不等于自身**——`NaN != NaN`，于是 map 里能存下**两个 NaN key**，看似重复却不相等。这正是 `914-map-concurrency-float.md` 提到的 float key 风险的**深层机理**。

## 面试官视角
这题考「可比较 ≠ 行为符合直觉」。float 在语法上可作 key（不像 slice 编译拒），但语义上坑多。考点：① 为什么 float key 会「取不到值/合并」；② NaN 的双 key 诡异；③ 正确做法（用整数/字符串等精确类型）。能讲清 `Float64bits` 机制，直接封神。

## 主问答
**Q（面试官原话）：** float 作 map key 有什么问题？

**A：**
1. **精度导致哈希不一致（取不到值/合并）**：map 对 key 算哈希时，float 的二进制表示（`math.Float64bits(f)` 转 `uint64`）参与运算。两个「逻辑相等」的 float 若二进制表示不同（如 `0.3` 与 `0.3+1e-17`），可能算出**不同哈希**→落到不同桶→`m[f]` 取不到预期 value；也可能（如某些长小数与 `0.3`）Float64bits 后恰好相等→被当成**同一 key 覆盖**。行为不可预测。
2. **NaN 不等于自身（双 key 诡异）**：`math.NaN() == math.NaN()` 返回 `false`。map 用相等性判 key，于是两个 `NaN` 被视为**不同 key**，`m[NaN]=3; m[NaN]=4` 后 map 里竟能存在**两个 key 都显示为 NaN** 的条目——打印出来像「重复 key」却互不相等，极难排查。
3. **正确做法**：**不要用 float 作 key**。需要浮点语义时，用「定点整数」（如金额用分 `int64`）、或把 float 格式化为固定精度字符串 `strconv.FormatFloat(f, 'f', 6, 64)` 作 key，规避精度与 NaN 问题。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | float 能作 key? | 语法合法 | 可比较故能作 key | 说「不能」算 L1 未过 |
| L2 | 为什么取不到值 | 精度机制 | Float64bits 哈希不一致 | 答不清算 L2 未过 |
| L3 | NaN 啥诡异 | 自不等 | NaN!=NaN→两 key | 不知算 L3 未过 |
| L4 | 怎么正确用 | 替代方案 | 定点 int/格式化 string | 只会「别用」算 L4 未过 |
| L5 | 与 914 关系 | 分层 | 914 讲风险，本卡讲机理 | 孤立算 L5 未过 |

## 版本与兼容性
- `math.Float64bits` / `math.NaN` 自 Go 1.0 恒定；IEEE-754 浮点语义跨语言一致。
- NaN 双 key 行为是 Go map 基于「== 比较」的必然结果，非 bug；`914-map-concurrency-float.md` 从「风险」角度点过，本卡补「Float64bits + NaN 自不等」机理。
- 与「可比较类型」（`509-comparable-types.md`）衔接：float **可比较**（能作 key），但比较结果反直觉，这是「可比较 ≠ 安全」的典型。

## 总结与追问预判
收口：**float 能作 key 但坑深——精度让哈希漂移取不到值，NaN 自不等能存双 key；改用定点 int 或格式化 string**。预判追问：① key 类型合法性（见 506.md`）；② 指针 key 按地址（见 506.md`）；③ 并发/无序风险（见 914.md`）。回答时把「`NaN != NaN` 能塞进两个 NaN key」抛出，是最惊艳的细节。

## ⚠️ 原文纠错
源视频转写将 Go / float / NaN / map key / 浮点精度 等音译为若干崩坏词，本卡已统一还原为规范术语（Go / float64 / NaN（Not-a-Number）/ map 键 / 浮点精度）。交付卡禁止保留任何原词崩坏写法。

> **[经验]** 面试官问「float 能作 key 吗」，**先答「语法能、工程不该」**——slice 是直接编译拒（硬约束），float 是「能编过但行为诡异」（软约束），两者性质不同。补一句「`NaN != NaN` 能在 map 里塞两个 NaN key」即可把 float key 讲透，比空说「有精度问题」高一个维度。

```go
package main

import (
	"fmt"
	"math"
	"strconv"
)

func main() {
	// ① 精度：两个「逻辑相等」的 float 可能哈希不同 → 取不到值
	m := map[float64]int{
		0.3:            5,
		0.3 + 1e-17:    6, // 与 0.3 逻辑相等，但 Float64bits 后可能不同桶
	}
	fmt.Println(m[0.3]) // 可能 5 也可能 0（取不到 6）→ 不可预测

	// ② NaN 自不等 → 能存两个 NaN key
	n := map[float64]int{}
	n[math.NaN()] = 3
	n[math.NaN()] = 4
	fmt.Println(math.NaN() == math.NaN()) // false
	fmt.Println(len(n))                     // 2！两个都显示 NaN 却不相等

	// ✅ 正确做法：定点整数 或 格式化字符串
	price := int64(0.3 * 100)              // 分
	key := strconv.FormatFloat(0.3, 'f', 6, 64) // "0.300000"
	_ = price
	_ = key
}
```
