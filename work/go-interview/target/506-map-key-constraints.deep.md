# 506 map key 可比较性约束深挖

## 思路与架构
「float/切片能否作 map key」的本质是 **map key 的可比较性约束（comparable）** 在三类场景下的落地：编译期硬拒（slice/map/func）、语法合法但语义诡异（float/NaN、指针）。它把「类型可比较清单」（`509-comparable-types.md`）迁移到了 map 这一具体数据结构的实战约束。

```text
map key 类型约束决策树
  ├─ 不可比较类型 (func/map/slice) ──→ 编译报错 invalid map key type（硬拒）
  ├─ 数组/结构体 ──→ 元素/字段全可比较才可作 key（否则编译报错）
  └─ 可比较但反直觉：
       ├─ float ──→ 精度→Float64bits 哈希漂移(取不到值/合并)；NaN!=NaN→可存双 key（软坑）
       └─ 指针 ──→ 比地址不比值→同值不同址产生双 key（软坑）
  结论：key 选型「值类型优先，指针慎选，float 禁用」
```

## 方案取舍
| key 类型 | 能否作 key | 行为 | 建议 |
| --- | --- | --- | --- |
| int/string/bool/chan/数组(元素可比) | ✅ | 精确相等比较 | **首选** |
| 结构体(字段全可比) | ✅ | 字段逐一比较 | 可用 |
| 指针 | ✅ | 比地址 | 慎选（同值双 key） |
| float | ⚠️ | 精度+NaN 诡异 | **禁用** |
| slice/map/func | ❌ | 编译报错 | 不可 |

**取舍结论**：能用值类型（int/string）就用值类型；float 一律改定点 int 或格式化 string；指针仅当确需「按对象身份区分」才用。这是「可比性合法 ≠ 行为安全」的典型——slice 是硬拒，float/指针是软坑。

**分层边界**：本批只讲 key 类型约束。map 的「并发写 panic / 无序遍历 / float key 取值风险」在 `914-map-concurrency-float.md`；「可比较类型清单」在 `509-comparable-types.md`；「指针比较」在 `503-pointer-compare.md`——均只引不重述。

## 答题技巧
1. **先给硬约束再给软坑**：开口「key 必须 comparable → slice/map/func 编译拒；float/指针能编过但诡异」，层次立现。
2. **编译报错最有说服力**：`var m map[[]int]int` 编译不过，比背名词更显实战。
3. **NaN 是点睛细节**：`NaN != NaN` 能在 map 塞两个 NaN key，是 float key 最惊艳的反直觉点。
4. **口诀收尾**：「值类型优先，指针慎选，float 禁用」——九字覆盖选型。
5. **避坑**：不说「float 不能作 key」（它能，只是不该）；不把「可比较」等同于「可作 key」（还需满足 comparable 约束且行为可预期）；不漏 slice/map/func 的编译期硬拒。

## 细节与核心 API

map 的 key 必须满足 **comparable**（可用 == / !=）：

```go
m1 := map[[2]int]string{}        // OK：数组 comparable
m2 := map[string]int{}           // OK
// m3 := map[[]int]int{}         // 编译错误：slice 不可比较
// m4 := map[map[string]int]int{}// 编译错误：map 不可比较
// m5 := map[func()]int{}         // 编译错误：func 不可比较
// 含不可比较字段的结构体也不能做 key
type Bad struct{ Slice []int }
// m6 := map[Bad]int{}           // 编译错误
// 浮点做 key 要避免 NaN（NaN != NaN 会导致查不到）
```
