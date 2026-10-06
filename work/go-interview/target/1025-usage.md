# 1025 Singleflight 用法：Group.Do 与同一 key 合并

> 分类：Go 并发 | 难度：中 | 题型：用法 | 频率：高 | 关键词：**Group.Do、key、并发合并、共享结果、回源**

> 原文锚点：第 12~35 段「demo 并发20请求、getArticleData、Group.Do、同 key 只一次打到 DB」

## 一句话总述
用法三步走：声明 `singleflight.Group`；在缓存未命中处调用 `g.Do(key, fn)`，fn 是真正的回源逻辑；同一 key 的并发调用会合并——只有一个 goroutine 执行 fn，其余直接拿返回值。示例里 20 个并发请求用同一个 key，最终只有 1 个打到数据库，20 个都拿到数据。

## 面试官视角
考官常要求手写或描述用法。关键点：① Do 返回 (val, err, shared)；② key 必须一致才会合并（key 是合并的判据）；③ fn 的返回值被所有等待者共享。能点出「key 设计决定合并粒度」很关键。

## 主问答
**Q（面试官原话）：** 怎么使用 singleflight？Do 方法返回什么？

1. **声明 Group**：`var g singleflight.Group`，无需初始化，零值可用。
2. **调用 Do**：`v, err, shared := g.Do(key, fn)`；fn 是回源函数（如查 DB），只在合并组中第一个请求时执行。
3. **key 即合并判据**：所有调用传相同 key 才会合并；key 不同则互不影响、各自执行。
4. **返回值**：v 是 fn 结果（被所有等待者共享），shared 表示该结果是否来自他人（true 表示本 goroutine 没执行 fn，是「搭车」拿到的结果）。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | 怎么用？ | 说不清 Group.Do |
| L2 | 返回几值？ | 漏 shared |
| L3 | key 作用？ | 说不清合并判据 |
| L4 | shared 含义？ | 说不清是否搭车 |
| L5 | 20 并发结果？ | 说不清都拿到同一份 |

## 版本与兼容性
| 项 | 说明 |
|------|------|
| Do 签名 | Do(key, fn) (v, err, shared) |
| 零值 | Group 零值即可用 |

## 关键代码
```go
func getArticleData() (interface{}, error) {
    if v := cache.Get(); v != nil { return v, nil }
    return g.Do("article", func() (interface{}, error) {
        return getArticleFromDB()
    })
}
```

## 总结与追问预判
核心：**g.Do(key, fn) 合并同 key 并发，返回 (val, err, shared)，shared 标记是否搭车**。追问常接「底层如何保证只执行一次」（见 1025-source）。

## ⚠️ 原文纠错
1. 事实核校： [经验] Group 零值可用、Do(key,fn) 返回 (val,err,shared)、同 key 合并、shared 含义——均正确，本卡为准。
2. 崩坏词归一：源码将 Go/goroutine/singleflight 等音译为崩坏词；本卡统一为规范术语。
