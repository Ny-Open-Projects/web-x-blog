# 918 nil map 与空 map：只差一次初始化，却差出一整套行为矩阵

> 分类：Go 基础 / map | 难度：L2 | 题型：对比题 | 频率：极高 | 关键词：**nil map**/**空 map**/**隐式初始化**/**assignment to entry in nil map**/**引用语义**/**描述符拷贝**
> 原文锚点：第 1~15 段「当一个 map 变量被声明，但是没有被初始化的时候，它的值就是 nil，这就是所谓的 nil map，也就是没有分配内存的 map…空 map 是指已经初始化的 map，但是其中没有任何键值对…nil map 和空 map 的本质区别就体现在是否分配了内存」
> [边界] 本文只讲 **nil map / 空 map 自身的行为矩阵与 map-vs-slice 复制语义对比**：nil 切片可 `append` 而 nil map 不可写的对照见 `414-slice-nil-vs-map`，`make` 与零值体系见 `414-go-zero-value`，map 底层 `hmap`/`bmap` 结构见 `914-map-hmap-bmap`，均不重述。

## 一句话总述
**nil map 是"声明了但没分配内存"**，空 map 是"**已初始化、只是没放东西**"。差别只有一次初始化，但行为天差地别：**nil map 读、删、`len`、`range` 全都安全，唯独写会 panic**（`assignment to entry in nil map`）；空 map 则读写皆宜。更隐蔽的坑是**字面量 `map[K]V{}` 自带隐式初始化**——它已经是空 map，**不是** nil map。

## 面试官视角
- 考察意图：这是 **Go 入门第一道坎**，也是面试官最爱用来筛人的题。它同时考三件事——**零值语义**、**引用类型的初始化时机**、**能否背出 panic 原文**。
- 分档：P5 知道"nil map 不能写"；P6 知道"可以读"；P7 能**完整报出四类安全操作**（读/删/`len`/`range`）、**背出 panic 文本**，并能顺手讲清 **map 与 slice 复制语义的本质差别**。
- 红旗答案：「nil map 一用就崩」——**错**。只有写会崩，读是安全的，这是设计上刻意的便利（否则每次读都要判 nil）。
- 惊艳点：主动补「`delete` 一个 nil map **既不 panic 也无效果**，Go 把它当 no-op——这是"删除幂等"的设计一致性」[实测]。

## 主问答
**Q（面试官原话）：** nil map 和空 map 有什么区别？nil map 能读吗？

**A：**
1. **定义分野**：map 变量**声明但未初始化**时值为 **nil**，内部**没有分配内存**；**空 map 是已经初始化过、但一个键值对都没有**的 map [经验]。
2. **唯一判据**：二者的本质区别**只看是否分配了内存**，也就是**是否对 map 类型做了初始化**；与"里面有没有元素"无关——空 map 也是 0 个元素 [经验]。
3. **nil map 的四类安全操作**：**读**（返回零值 + `ok=false`，实测 `v=0 ok=false`）、**删除**（no-op，不 panic）、**`len`**（实测 0）、**`range`**（实测迭代 **0 次**直接结束）[实测]。
4. **nil map 唯一的雷**：**写入**。实测 panic 原文就是 **`assignment to entry in nil map`**——直译"往 nil map 里写入了一个 entry（键值对的实体）" [实测]。
5. **最容易混淆的声明方式**：`var m map[string]int` 是 **nil map**；而 `m := map[string]int{}` 这种**字面量形式**包含**一次隐式初始化**，它已经是**空 map**，实测 `emptyMap == nil` 输出 **`false`** [实测]。
6. **和切片不一样**：**nil 切片可以直接 `append`**，nil map 却不能写——这是两类引用类型在零值可用性上的关键差异 [经验]。
7. **map 的复制语义**：map 赋值**共享同一个底层结构**。实测 `m2 := m1; m2["b"] = 2` 之后，**`m1` 里也能看到 `b`**（`m1=map[a:1 b:2]`）[实测]。
8. **切片的复制语义相反**：切片赋值是**描述符拷贝**，二者**共享同一块底层数组**（实测首元素地址相同 `0x246383bce000`），但 **`len`/`cap`/起始地址各自独立**；所以 `append` 之后**原切片看不见新元素**——实测 `s1=[0 0](len=2)`、`s2=[0 0 99](len=3)` [实测]。
9. **工程结论**：**使用 map 前一定要初始化**；作为参数传出、或结构体字段在外部被填充时，尤其容易漏掉这一步 [经验]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | nil map 和空 map 区别？ | 定义 | 是否分配内存 | P5 停 |
| L2 | nil map 能读吗？ | 反直觉 | 能，返回零值 + ok=false | P6 停 |
| L3 | 写入 panic 原文是什么？ | 细节 | `assignment to entry in nil map` | P6 停 |
| L4 | `map[K]V{}` 是 nil 吗？ | 陷阱 | 不是，字面量已隐式初始化 | P7 停 |
| L5 | map 与 slice 复制后表现为何相反？ | 深度 | map 共享底层；slice 描述符独立 | P7+ 停 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 1.0 起（全版本） | nil map 读安全、写 panic | 行为从未改变 |
| Go 全版本 | panic 文本 `assignment to entry in nil map` | 记原文而非意译 [实测] |
| Go 全版本 | `delete` 对 nil map 是 no-op | 不 panic 也无效 [实测] |
| Go 全版本 | 字面量 `map[K]V{}` = 已初始化 | 与 `var` 声明不等价 [实测] |
| Go 1.21+ | 新增 `maps` 标准库包 | 但**赋值语义未变** |
| 并发场景 | 任何 map 并发写都会 fatal | nil map 也不例外 [经验] |

## 关键代码
```go
package main

import "fmt"

func main() {
	// ① nil map：读 / 删 / len / range 四类操作全部安全
	var nilMap map[string]int
	fmt.Printf("nilMap == nil -> %v, len=%d\n", nilMap == nil, len(nilMap))
	v, ok := nilMap["k"]
	fmt.Printf("nilMap 读: v=%d ok=%v\n", v, ok)
	delete(nilMap, "k") // no-op，不 panic
	for range nilMap {  // 迭代 0 次，不 panic
	}
	fmt.Println("nilMap 的读/删/len/range 均执行完毕")

	// ② 字面量声明自带隐式初始化：这是空 map，不是 nil map
	emptyMap := map[string]int{}
	fmt.Printf("emptyMap == nil -> %v, len=%d\n", emptyMap == nil, len(emptyMap))
	emptyMap["a"] = 1 // 写入成功

	// ③ nil map 写入的 panic 原文
	func() {
		defer func() { fmt.Printf("nil map 写入 panic: %v\n", recover()) }()
		nilMap["x"] = 1
	}()

	// ④ map 赋值：共享底层结构，新变量加键原变量可见
	m1 := map[string]int{"a": 1}
	m2 := m1
	m2["b"] = 2
	fmt.Printf("m1=%v m2=%v (m1 可见新键=%v)\n", m1, m2, m1["b"] == 2)

	// ⑤ slice 赋值：共享底层数组，但 len 独立 —— append 后原切片不可见
	s1 := make([]int, 2, 10) // cap 足够，保证 append 不扩容、地址才可比
	s2 := s1
	fmt.Printf("底层数组首元素地址相同=%v\n", &s1[0] == &s2[0])
	s2 = append(s2, 99)
	fmt.Printf("append 后 s1=%v(len=%d) s2=%v(len=%d)\n", s1, len(s1), s2, len(s2))
}
```

> 验证（`[实测]` 输出，go1.26.5 / macOS）：`nilMap == nil -> true, len=0`；`nilMap 读: v=0 ok=false`；`delete` 后 `len=0` 且程序继续；`range` **迭代 0 次**；`emptyMap == nil -> false, len=0`，随后写入成功输出 `map[a:1]`；写入 nil map 的 panic 原文为 **`assignment to entry in nil map`**；map 赋值后 `m1=map[a:1 b:2] m2=map[a:1 b:2] (m1 可见新键=true)`；slice 侧 `底层数组首元素地址相同=true`，`append 后 s1=[0 0](len=2) s2=[0 0 99](len=3)`。

## 总结与追问预判
- 一句话收尾：**"nil map 只写崩，其余全安全；字面量已初始化；map 共享、slice 独立"**。
- 大概率被追的三问：① 为什么读 nil map 不崩（返回零值是零值体系的一致性设计，让调用方不必先判 nil）；② 结构体里的 map 字段为什么常忘初始化（零值自动生效，编译期不报错，只有运行时写才暴露）；③ 函数返回 map 时要不要判 nil（通常返回空 map 更友好，调用方可直接写）。
- 反向加分：主动说出 **`delete` 对 nil map 是 no-op**，并把它与"删除操作幂等"这个设计原则联系起来。

## ⚠️ 原文纠错
1. 源码称 nil map「不能用于存储键值对」——准确说是**不能写**，读/删/`len`/`range` 均安全 [经验]。
2. 源码称对 nil map 删除「没有意义」——对，但应强调**它不 panic**，与写入形成鲜明对照 [经验]。
3. 源码未提 panic 原文 **`assignment to entry in nil map`**，面试里报出这句很加分 [实测]。
4. 源码未区分**字面量声明已隐式初始化**——`map[K]V{}` 是空 map，**不是** nil map [实测]。
5. 源码说切片赋值后「完全独立」——不准，**底层数组是共享的**，独立的只是 `len`/`cap` [实测]。
6. 源码未提示 `append` **扩容后**两者会彻底分家，实测结论仅在 `cap` 充足时成立 [经验]。
