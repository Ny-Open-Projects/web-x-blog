# 707 嵌套结构体校验：structonly、横杠、eqfield

> 分类：Web框架 | 难度：L2 | 题型：八股题 | 频率：中 | 关键词：**structonly** / **横杠跳过** / **eqfield跨字段**
> 原文锚点：第 19~37 段「ecofield等于password…structonly和中横线…忽略子字段校验」

## 一句话总述
嵌套结构体默认递归校验；用 `structonly` 或字段标签写 `-` 可跳过整层子结构校验；`eqfield=Password` 则声明本字段必须等于另一字段的值，可用于两次密码一致。

## 面试官视角
- **考察意图**：是否理解嵌套校验的递归默认行为及如何按需关闭。
- **P5**：会用 `eqfield` 做两次密码一致。**P6**：说清 `structonly`/`-` 跳过子结构。**P7**：知道 `eqfield` 等号后是**字段名（大写开头）**而非标签名，知道嵌套元素级校验要靠 `dive`。
- **红旗答案**：以为 `eqfield=password` 写的是标签名；不知道嵌套数组需 `dive` 才能进元素。
- **惊艳点**：`eqfield` 等号后必须是**结构体字段名（大写）**，不是 json/binding 标签名 —— 这是原文重点强调的易错点 [源码]

## 主问答
**Q（面试官原话）：** 嵌套结构体怎么跳过校验？两次密码一致怎么写？
**A：**
1. **结论**：`eqfield=Field` 做跨字段相等；`structonly` 或子字段写 `-` 跳过嵌套校验。
2. **机制**：默认 validator 递归进子结构；`structonly` 只校验本层不进子结构；`-` 让某个字段整体不参与校验。
3. **边界**：`eqfield` 引用的是字段名而非标签；真正要校验切片/map 元素需 `dive` 子句。
**加分层：** 这些都是 validator 通用能力，和 Gin 无关，换框架也通用。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | eqfield 干嘛 | 知不知道 | 跨字段相等 | 换题→不及格 |
| L2 | 怎么跳过子结构 | 背还是推 | structonly 或 - | 判 P5 |
| L3 | eqfield 写字段名还是标签 | 踩坑经验 | 字段名大写开头 | 判 P6 |
| L4 | 切片元素怎么校验 | 边界 | 用 dive 进入元素 | 判 P6+ |
| L5 | 自定义跨字段规则 | 实战 | RegisterValidation + fl.Field() | 答得上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| validator/v10 全版本 | structonly/-/eqfield 在 v8 已存在 | 按 v10 答 [经验] |

## 关键代码
```go
type User struct {
    Password  string `binding:"required,contains=123abc"`
    RePassword string `binding:"required,eqfield=Password"` // 等号后是字段名
    Extra2    Sub    `binding:"structonly"`                 // 只校验本层
    Extra3    Sub    `binding:"-"`                          // 整字段跳过
}
type Sub struct {
    F1 string `binding:"min=6"` // 被 structonly/- 跳过
}
```
示意，未验证。

## 总结与追问预判
- 递归默认；structonly/`-` 关闭；eqfield 引用字段名；元素级用 dive。
- 预判：面试官会问更灵活的校验怎么做（见 707-gin-custom-validator）。

## ⚠️ 原文纠错
原文对切片/map 的「元素值长度」校验只描述了效果，未给出 `dive` 子句这一真实语法（如 `binding:"gt=1,dive,min=2,max=100"` 才能进入元素逐项校验）。已在上文补正；嵌套元素级校验需 `dive`，非原文所述仅靠逗号分隔即可。
