# 703 FormValue 与 PostFormValue 的源码差异

> 分类：Web / Go net/http | 难度：L3 | 题型：源码题 | 频率：中 | 关键词：**FormValue、PostFormValue、ParseMultipartForm、POST/PUT/PATCH、URL 参数**

> 原文锚点：第 52~86 段「FormValue 与 PostFormValue 都只支持 POST/PUT/PATCH…FormValue 还能取 URL 后面参数，PostFormValue 只能取表单提交的值…底层都调 ParseMultipartForm」

## 一句话总述
`FormValue` 与 `PostFormValue` 底层都调 `ParseMultipartForm`，且都只接受 POST/PUT/PATCH 方法的参数。唯一区别：`FormValue` 额外能拿到 URL 查询参数，`PostFormValue` 只拿 POST 表单体的值。

## 面试官视角
P6 能说出「都只支持 POST/PUT/PATCH」；P7 要讲清源码链路：`FormValue`→`ParseMultipartForm` 后合并 URL 参数进 `Form`，`PostFormValue` 只读 `PostForm`，以及为何 GET 带 body 取不到。

## 主问答
**Q（面试官原话）：** FormValue 和 PostFormValue 有什么区别？

1. **同源解析**：两者都先判断 `r.Form`/`r.PostForm` 是否为空，空则调 `ParseMultipartForm` 解析 `[源码]`。
2. **方法限制**：都只支持 POST/PUT/PATCH 提交来的参数，GET 无表单体，取不到 `[源码]`。
3. **FormValue 范围大**：`FormValue` 的 `Form` 含 POST 表单值 + URL 查询参数，故能取 URL 后参数 `[源码]`。
4. **PostFormValue 范围小**：只读 `PostForm`，仅 POST 表单体，拿不到 URL 参数 `[源码]`。
5. **底层合并**：解析时先把表单体 append 进 `Form` 与 `PostForm`，再把 URL 参数并入 `Form` `[经验]`。

## 追问链
| 层级 | 追问 | 答不出停在哪档 |
|---|---|---|
| L1 | 都支持？ | 答不出 POST/PUT/PATCH |
| L2 | 底层？ | 说不出 ParseMultipartForm |
| L3 | 范围差异？ | 答不出 URL 参数 |
| L4 | 为何 GET 取不到？ | 答不出无表单体 |
| L5 | 合并顺序？ | 答不出体先 URL 后 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 1.x 全版本 | 两 API 行为一致 | 差异仅在范围 |
| 任意版本 | 惰性解析 | 调 Value 才 Parse |
| 任意版本 | GET 无 body | 仅 query 参数 |

## 关键代码
```go
// 源码等价逻辑
func (r *Request) FormValue(key string) string {
    r.ParseMultipartForm(defaultMaxMemory)
    if vs := r.Form[key]; len(vs) > 0 { return vs[0] } // Form 含 URL 参数
    return ""
}
// PostFormValue 只读 r.PostForm（不含 URL 参数）
```

## 总结与追问预判
**两方法范围差异是面试高频点**。回到惰性解析机制——见同批 703-form-parse-lazy。

## ⚠️ 原文纠错
1. 事实核校：两方法都调 ParseMultipartForm、仅支持 POST/PUT/PATCH、FormValue 含 URL 参数而 PostFormValue 不含——均准确 `[经验]`。
2. 补充：原文称都「只支持 POST/PUT/PATCH」，精确是方法限制针对表单体解析入口，URL 参数经 Form 仍可取 `[经验]`。
3. 崩坏词归一：源码将 Go、net/http、Handler、表单取值方法等术语音译为多组崩坏词，本卡统一为规范术语 `[经验]`。
