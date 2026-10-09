# 703 表单页渲染：template.ParseFiles 与 Execute

> 分类：Web / Go net/http | 难度：L2 | 题型：操作题 | 频率：中 | 关键词：**template.ParseFiles、Execute、相对路径、nil data、HTML 表单**

> 原文锚点：第 9~22 段「template 包下 ParseFiles 传 HTML 路径（相对执行目录）…两返回值模板指针与 error…Execute 传 ResponseWriter 与 data，无变量传 nil…HTML 表单 action 指向路由、含 username/password 字段」

## 一句话总述
渲染表单页用 `template.ParseFiles("login.html")` 解析模板（路径相对执行命令的目录），它返回模板指针与 error；`t.Execute(w, nil)` 输出，无变量传 `nil`。前端表单 `action` 指向后端路由，`method=post` 含 username/password 字段。

## 面试官视角
P5 能写出 ParseFiles+Execute；P6 要讲清「两返回值必须判 error」与「路径相对执行目录」；P7 能指出 `Execute` 的 data 是模板变量上下文，无变量传 nil。

## 主问答
**Q（面试官原话）：** 怎么用模板渲染登录表单页？

1. **解析模板**：`t, err := template.ParseFiles("login.html")` 两返回值，必须判 err `[源码]`。
2. **相对路径**：路径相对「执行 main 的当前目录」，不是文件所在目录，易踩坑 `[源码]`。
3. **执行输出**：`t.Execute(w, nil)` 把渲染结果写入 ResponseWriter；无模板变量传 `nil` `[源码]`。
4. **前端表单**：HTML 中 `<form action="/login" method="post">` 含 username/password 字段，提交到后端路由 `[源码]`。
5. **分支渲染**：GET 渲染页面，POST 由同路由 Handler 另一分支接收，形成闭环 `[经验]`。

## 追问链
| 层级 | 追问 | 答不出停在哪档 |
|---|---|---|
| L1 | 怎么渲染？ | 答不出 ParseFiles |
| L2 | 返回值？ | 说不出指针+error |
| L3 | 路径相对？ | 答不出执行目录 |
| L4 | data 传啥？ | 答不出 nil/变量 |
| L5 | 表单 action？ | 答不出指向路由 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 1.x 全版本 | text/template+html | html/template 防 XSS |
| 任意版本 | 两返回值 | 必判 error |
| 任意版本 | 路径相对 exec | 非文件目录 |

## 关键代码
```go
t, err := template.ParseFiles("login.html")
if err != nil { http.Error(w, err.Error(), 500); return }
t.Execute(w, nil) // 无变量传 nil；有变量传 struct/map
```

## 总结与追问预判
**渲染是表单闭环的第一半**。配合取值（703-form-value-methods）才是完整流程。

## ⚠️ 原文纠错
1. 事实核校：ParseFiles 两返回值、路径相对执行目录、Execute(w, data)、表单 action 指向路由——均准确 `[经验]`。
2. 补充：原文用 `html/template` 渲染，精确该包会自动转义防 XSS，优于 text/template `[经验]`。
3. 崩坏词归一：源码将 Go、net/http、Handler、模板等术语音译为多组崩坏词，本卡统一为规范术语 `[经验]`。
