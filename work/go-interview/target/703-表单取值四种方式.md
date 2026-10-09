# 703 表单取值四种方式：Form/PostForm 与 FormValue/PostFormValue

> 分类：Web / Go net/http | 难度：L3 | 题型：操作题 | 频率：高 | 关键词：**Request.Form、Request.PostForm、FormValue、PostFormValue、map、方法**

> 原文锚点：第 29~50 段「取值四种方式：Request.Form / Request.PostForm / FormValue() / PostFormValue()…Form 与 PostForm 是两个 map，后两者是方法…Form 含 URL 参数与表单值，PostForm 仅表单体」

## 一句话总述
表单值有四种取法：`r.Form` 与 `r.PostForm` 是 `map[string][]string` 字段；`r.FormValue(k)` 与 `r.PostFormValue(k)` 是方法。关键区别：`Form`/`FormValue` 含 URL 查询参数，而 `PostForm`/`PostFormValue` 仅含 POST 表单体。

## 面试官视角
P6 能说出四种方式；P7 要讲清「map 与方法的本质区别」以及 `Form` 包含 URL 参数而 `PostForm` 不含，这决定了取值范围差异。

## 主问答
**Q（面试官原话）：** 表单值有哪几种取法？有什么区别？

1. **两个 map**：`r.Form`、`r.PostForm` 是 `map[string][]string`，需先解析才能读 `[源码]`。
2. **两个方法**：`r.FormValue(k)`、`r.PostFormValue(k)` 直接按 key 返回首个值，内部触发解析 `[源码]`。
3. **Form 含 URL 参数**：`r.Form` 与 `FormValue` 数据源相同，既含 POST 表单值也含 URL 查询参数 `[源码]`。
4. **PostForm 仅表单体**：`r.PostForm` 与 `PostFormValue` 只含 POST 表单提交的值，不含 URL 参数 `[源码]`。
5. **选用建议**：只取表单体用 `PostFormValue`；需连同 URL 参数用 `FormValue` `[经验]`。

## 追问链
| 层级 | 追问 | 答不出停在哪档 |
|---|---|---|
| L1 | 几种取法？ | 答不出 2 map+2 方法 |
| L2 | map vs 方法？ | 说不出是否触发解析 |
| L3 | Form 含啥？ | 答不出含 URL 参数 |
| L4 | PostForm 含啥？ | 答不出仅表单体 |
| L5 | 怎么选？ | 答不出按是否要 URL |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 1.x 全版本 | 四 API 稳定 | map+方法并存 |
| 任意版本 | Form 含 query | URL 参数并入 |
| 任意版本 | 取首值 | Value 返回 []string[0] |

## 关键代码
```go
user := r.FormValue("username")     // 含 URL 参数 + 表单体
pwd  := r.PostFormValue("password") // 仅 POST 表单体
// map 形式（需先触发解析）：
_ = r.ParseForm()
fmt.Println(r.Form["username"])     // []string
```

## 总结与追问预判
**map 与方法是两套接口，范围不同**。下一步常问：为何 Form 有时是 nil——见同批 703-form-parse-lazy。

## ⚠️ 原文纠错
1. 事实核校：四种取法、Form/PostForm 是 map、FormValue/PostFormValue 是方法、Form 含 URL 参数而 PostForm 不含——均准确 `[经验]`。
2. 补充：原文未提 `r.Form` 在没调 Value 方法前为 nil，精确需先 ParseForm/调 Value 才填充 `[经验]`。
3. 崩坏词归一：源码将 Go、net/http、Handler、模板、表单取值方法等术语音译为多组崩坏词，本卡统一为规范术语 `[经验]`。
