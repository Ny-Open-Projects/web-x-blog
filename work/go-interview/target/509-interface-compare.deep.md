# 509 interface 比较全景（深挖）

> 分类：Go/类型系统 | 难度：L4 | 题型：体系化深挖 | 频率：中 | 关键词：**iface/eface** / **比较规则** / **nil 陷阱** / **答题技巧**

## 思路与架构
interface 比较题的答题架构是"**清单 → 底层 → 陷阱 → 规避**"四层：
- **清单层**：先答 Go 可比较类型清单（map/slice/func 不可互比但可 nil 比），建立地基。
- **底层层**：interface 有 eface/iface 两表示，比较看 type 同 + data 值同（非指针地址）。
- **陷阱层**：error != nil 却打印 nil —— type 非空的指针赋给接口，接口整体非 nil。
- **规避层**：返回 error 永远 `return nil`，不返回 nil 指针类型。

## 方案取舍
| 比较对象 | 相等条件 | 易错点 |
|---|---|---|
| 两 interface | type 同 且 data 指向值同 | 比的是值不是 data 指针地址 |
| 空接口 vs nil | type 和 data 都空 | 任一非空即不等 nil |
| nil 指针赋接口 | 永不等 nil | type=*T 非空是根因 |
| 不同动态类型 | 直接不等 | 即便值相同(int vs int32) |

**调试取舍**：`fmt` 只打印 data 值（会掩盖 type），排查必须用 `reflect.TypeOf` 看动态类型，或用反射/printerr 看 tab/data。

## 答题技巧
1. **先清单后底层**：开口先背"哪些类型可比较"，再进 interface 底层，层次分明。
2. **抓两个字段**：iface/eface 的 type + data，比较规则一句话收"type 同且 data 值同"。
3. **陷阱必讲**：error != nil 却打印 nil 是高频实战题，主动抛出显专业。
4. **区分 nil 两义**：nil interface（全空）vs nil pointer（type 非空）——这是区分 P6/P7 的分水岭。
5. **给工程规避**：return nil 归一化，把原理落到代码实践。
