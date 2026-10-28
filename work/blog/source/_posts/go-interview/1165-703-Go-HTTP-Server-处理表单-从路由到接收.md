---
disableNunjucks: true
title: "703 Go HTTP Server 处理表单：从路由到接收"
date: 2026-10-07 10:46:09
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：Web / Go net/http | 难度：L2 | 题型：操作题 | 频率：高 | 关键词：**net/http、HandleFunc、模板渲染、GET、POST、表单接收**

> 原文锚点：第 1~28 段「用 net/http 包启动 server，监听 8888 端口，默认多路复用器定义路由…GET 渲染 HTML 模板，POST 提交表单到后端路由接收」

## 一句话总述
Go 用 `net/http` 起服务：默认多路复用器 `HandleFunc` 注册路由，Handler 内按 `r.Method` 分支——GET 用 `template.ParseFiles` 渲染表单页，POST 接收表单提交并读取字段。

## 面试官视角
P5 能写出 HandleFunc + 路由；P6 要讲清 `http.MethodGet` 常量而非字符串比较，以及模板路径相对「执行命令的目录」；P7 能指出表单字段如何读取。

## 主问答
**Q（面试官原话）：** Go 的 HTTP server 怎么处理表单输入？

1. **起服务**：`http.ListenAndServe(":8888", nil)` 用默认多路复用器，`nil` 表示用 `DefaultServeMux` `[源码]`。
2. **注册路由**：`http.HandleFunc("/login", loginHandler)` 把路径绑定到处理函数 `[源码]`。
3. **方法分支**：Handler 内 `if r.Method == http.MethodGet` 走渲染，否则（POST）走接收逻辑 `[源码]`。
4. **渲染表单**：GET 时 `template.ParseFiles("login.html")` 解析模板，`Execute(w, nil)` 输出页面 `[源码]`。
5. **接收提交**：POST 时从 `r.Form`/`r.PostForm` 或 `FormValue` 取 username/password 等字段 `[源码]`。

## 追问链
| 层级 | 追问 | 答不出停在哪档 |
|---|---|---|
| L1 | 怎么起服务？ | 答不出 ListenAndServe |
| L2 | 路由怎么绑？ | 答不出 HandleFunc |
| L3 | 方法分支？ | 答不出 r.Method |
| L4 | 模板路径？ | 说不出相对执行目录 |
| L5 | 怎么取字段？ | 答不出 FormValue |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 1.x 全版本 | net/http 标准库 | 无需第三方 |
| Go 1.22+ | 路由增强 | 支持 Method/路径通配 |
| 任意版本 | 默认复用器 | nil=DefaultServeMux |

## 关键代码
```go
http.HandleFunc("/login", func(w http.ResponseWriter, r *http.Request) {
    if r.Method == http.MethodGet {
        t, _ := template.ParseFiles("login.html")
        t.Execute(w, nil)
        return
    }
    // POST：见同批取值方法
})
http.ListenAndServe(":8888", nil)
```

## 总结与追问预判
**起服务→路由→方法分支→取值**是固定套路。下一步常问：表单值有几种取法——见同批 703-form-value-methods。

## ⚠️ 原文纠错
1. 事实核校：net/http 起服务、HandleFunc 路由、按 r.Method 分支、模板渲染、POST 取值——均准确 `[经验]`。
2. 补充：原文用默认多路复用器（`nil`），生产中更推荐显式 `http.NewServeMux()` 避免全局状态污染 `[经验]`。
3. 崩坏词归一：源码将 Go、net/http、Handler、模板、表单取值方法等术语音译为多组崩坏词，本卡统一为规范术语 `[经验]`。
