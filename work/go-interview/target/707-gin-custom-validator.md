# 707 自定义验证器注册与 FieldLevel 反射

> 分类：Web框架 | 难度：L2 | 题型：工程题 | 频率：中 | 关键词：**RegisterValidation** / **FieldLevel** / **Engine指针断言**
> 原文锚点：第 39~56 段「自定义验证器…validata的NG强转成指针…注册自定义验证器」

## 一句话总述
超出内置规则时，用 `validator.RegisterValidation(name, fn)` 注册自定义规则；fn 入参是 `validator.FieldLevel`，经反射拿到字段值做判断；注册必须在启动路由之前完成。

## 面试官视角
- **考察意图**：是否会扩展校验器、理解注册时机与反射取值。
- **P5**：会写 RegisterValidation 并绑定标签。**P6**：说清 FieldLevel 反射取值 + 注册要早于路由。**P7**：知道需从 `binding.Validator.Engine().(*validator.Validate)` 拿到实例再注册、知道类型断言失败的处理。
- **红旗答案**：在 handler 里才注册验证器；注册前已 Bind 导致不生效。
- **惊艳点**：注册入口是 `v := binding.Validator.Engine().(*validator.Validate); v.RegisterValidation("name", fn)` —— 拿不到 Engine 就注册不进 Gin 默认校验器 [源码]

## 主问答
**Q（面试官原话）：** 内置规则不够用，怎么加自己的校验逻辑？
**A：**
1. **结论**：实现 `func(validator.FieldLevel) bool` 并通过 `RegisterValidation` 注册成新标签。
2. **机制**：函数内用 `fl.Field().Interface()`（或 `Int()`）经反射取字段值；返回 false 即校验失败。
3. **边界**：注册必须在 `r.Run()`/路由注册**之前**；标签名不能与内置冲突。
**加分层：** 自定义规则与框架无关，可直接复用同一 validator 实例。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 怎么加自定义规则 | 知不知道 | RegisterValidation | 换题→不及格 |
| L2 | 函数里怎么取值 | 背还是推 | FieldLevel 反射 | 判 P5 |
| L3 | 注册时机有要求吗 | 踩坑经验 | 早于路由启动 | 判 P6 |
| L4 | 怎么拿到 Gin 的 validator | 架构判断 | Engine().(*validator.Validate) | 判 P6+ |
| L5 | 跨字段自定义校验 | 实战 | fl.Parent()+Field() | 答得上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| Gin v1.7+（validator/v10） | v8 接口签名不同 | 按 v10 的 FieldLevel 答 [经验] |

## 关键代码
```go
func validMtime(fl validator.FieldLevel) bool {
    t := fl.Field().Int() // 反射取 int 值
    if t == 0 {
        return false
    }
    return time.Now().Unix()-t >= 0 // 必须小于当前时间
}
// 启动前：v := binding.Validator.Engine().(*validator.Validate); v.RegisterValidation("mtime", validMtime)
```
示意，未验证。

## 总结与追问预判
- 自定义 = FieldLevel 反射 + RegisterValidation，注册早于路由。
- 预判：面试官会问校验失败如何精确定位字段（见 707-gin-bind-error-handling）。

## ⚠️ 原文纠错
未发现技术错误。核对范围：通读全文并重点核对代码 API 与版本相关行为；仅做了机翻解码（如 勾浪→Go 等拼写还原），技术结论未做更正.
