---
disableNunjucks: true
title: "702 net/http 启动全景：三步→Serve 并发→ServeMux 路由（深卡）"
date: 2026-10-10 09:07:53
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：Go 网络 / net/http | 难度：L4 | 题型：体系题 | 频率：高 | 关键词：**net/http 体系**/**启动三步**/**每连接 goroutine**/**ServeMux 匹配**/**与 Gin 边界**

> 原文锚点：第 1~69 段「net/http 启动 server 全节」

## 思路与架构
net/http 启动这条线按「**启动三步 → Serve 并发 → ServeMux 路由**」三层串：
- 启动层：NewServeMux 建表 → HandleFunc 注册 → ListenAndServe 绑定（对应 `702-http-server-startup.md`）。
- 并发层：Serve 每连接 go c.serve()，handler==nil 兜底 DefaultServeMux（对应 `702-serve-goroutine-per-conn.md`）。
- 路由层：精确优先、前缀取最长、DefaultServeMux 全局单例（对应 `702-servemux-routing.md`）。

## 方案取舍
- **启动给 http-server-startup 卡**：三步 + addr 绑定（全网卡 vs 回环）。
- **内核给 serve-goroutine-per-conn 卡**：每连接 goroutine + nil 兜底，讲清并发模型。
- **路由给 servemux-routing 卡**：精确/子树/最长匹配 + 全局单例易冲突。
- **不重产 Gin**：Gin 中间件/启动见 706.md` / `707-gin-custom-validator.md`，本卡只在边界点一句「Gin 的 engine 自带 router，启动类似但中间件体系不同」。

## 答题技巧
1. 开场三步：建 mux → 注册 → ListenAndServe。
2. 底层一句：Serve 每连接 go c.serve()，handler nil 兜底 DefaultServeMux。
3. 路由规则：精确优先、前缀最长；包级 HandleFunc 进全局表，别多处混用。
4. 收尾：addr 冒号开头绑全网卡、指定 IP 限回环；原生不按 method 分流，需要靠 Handler 或框架。
5. 边界话术：**「这是 net/http 原生；Gin 是上层封装，engine 自带 router」**——避免被追问时把原生与框架 API 混为一谈。

## 细节与核心 API

```go
mux := http.NewServeMux()
mux.HandleFunc("/api", func(w http.ResponseWriter, r *http.Request) {
    w.Write([]byte("ok"))
})
srv := &http.Server{
    Addr:         ":8080",
    Handler:      mux,
    ReadTimeout:  5 * time.Second,   // 读整个请求超时（防慢速攻击）
    WriteTimeout: 10 * time.Second,  // 写响应超时
    IdleTimeout:  120 * time.Second, // keep-alive 空闲超时
}
// 关键：务必设超时，否则默认无超时可能被慢连接拖死
log.Fatal(srv.ListenAndServe())
// 优雅关闭见“优雅关闭全景”卡；ServeMux 默认不清理路径尾斜杠（可用 http.StripPrefix）
```
