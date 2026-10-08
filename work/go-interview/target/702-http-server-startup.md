# 702 net/http 启动 HTTP Server 三步

> 分类：Go 网络 / net/http | 难度：L3 | 题型：原理题 | 频率：高 | 关键词：**NewServeMux**/**HandleFunc**/**ListenAndServe**/**DefaultServeMux**/**:port 全网卡**

> 原文锚点：第 3~32 段「创建 server 对象 / 注册路由 / 启动 server」

## 一句话总述
用 net/http 起服务分三步：① `http.NewServeMux()` 建**多路复用器**（mux，路由表）；② `mux.HandleFunc(path, func(w, r){...})` 注册路由回调（w=ResponseWriter 写响应、r=*Request 读请求）；③ `http.ListenAndServe(addr, mux)` 启动并监听。简写 `http.HandleFunc(...)` + `ListenAndServe(addr, nil)` 走**全局 DefaultServeMux**。addr 写 `:8888` 监听**所有网卡**、写 `127.0.0.1:8888` 仅本机。

## 面试官视角
net/http 启动是 Web 后端基本功。能讲清「mux 是路由表、HandleFunc 注册、ListenAndServe 把 addr 和 handler 绑一起」，再补一句「传 nil 为何也能跑（DefaultServeMux 兜底）」，就是合格；只 `http.ListenAndServe` 一行而不知其分层的不够。

## 主问答
**Q（面试官原话）：** 用 net/http 怎么启动一个 HTTP server？

1. **建 mux**：`mux := http.NewServeMux()` 得到多路复用器（路由表），负责按 URL 分发到回调。
2. **注册路由**：`mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request){ fmt.Fprint(w, "root") })`——前者是路由、后者回调（首参 ResponseWriter、次参 *Request）。
3. **启动**：`http.ListenAndServe(":8888", mux)` 把监听地址与 mux 绑一起并阻塞服务；返回的 error 需处理。
4. **简写法**：直接 `http.HandleFunc("/", h)` + `http.ListenAndServe(":8888", nil)`——前者用包级 **DefaultServeMux** 注册，后者 handler 传 nil 时由 Serve 设为 DefaultServeMux（见 `702-serve-goroutine-per-conn.md`）。
5. **addr 绑定**：`:8888`（冒号开头）监听本机**所有网卡**（含外网 IP 可访问）；`127.0.0.1:8888` 只绑回环，仅本机可达——生产按暴露需求选。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | 怎么起 server？ | 说不清 ListenAndServe |
| L2 | 路由怎么注册？ | 说不清 HandleFunc |
| L3 | mux 是什么？ | 说不清多路复用器 |
| L4 | 传 nil 为何能跑？ | 说不清 DefaultServeMux |
| L5 | :port 与 ip:port？ | 说不清全网卡 vs 回环 |

## 版本与兼容性
| 写法 | mux | 适用 |
|------|-----|------|
| NewServeMux + ListenAndServe(mux) | 自建 | 多路由/清晰 |
| http.HandleFunc + ListenAndServe(nil) | DefaultServeMux | 快速/单文件 |

## 关键代码
```go
mux := http.NewServeMux()
mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
    fmt.Fprint(w, "root") // w 实现 io.Writer，可直接写响应
})
mux.HandleFunc("/test", func(w http.ResponseWriter, r *http.Request) {
    fmt.Fprint(w, "test")
})
log.Fatal(http.ListenAndServe(":8888", mux)) // :8888 监听所有网卡
```

## 总结与追问预判
核心：**NewServeMux 建路由表 → HandleFunc 注册 → ListenAndServe 绑定启动；传 nil 走 DefaultServeMux**。追问拐向「ListenAndServe 底层」——备好「Serve 每连接起 goroutine、handler==nil 兜底 DefaultServeMux」（见 `702-serve-goroutine-per-conn.md`）。

## ⚠️ 原文纠错
1. 事实核校： [经验] 原文「三步：建 server 对象(mux)/注册路由 HandleFunc/启动 ListenAndServe；简法用 DefaultServeMux」——准确；本卡补入「ResponseWriter 实现 io.Writer 故可作 fmt.Fprint 目标」与「addr 冒号开头绑全网卡、指定 IP 限回环」的绑定细节（原文只提冒号）。
2. 崩坏词归一：源码将 HTTP / server / 多路复用器 / 路由 / 携程 / 回调 等音译为多组崩坏词，本卡统一为规范术语。
