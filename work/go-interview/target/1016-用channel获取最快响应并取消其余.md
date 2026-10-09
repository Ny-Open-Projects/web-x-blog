# 1016 用 channel 获取最快响应（并取消其余）

> 分类：Go/并发 | 难度：L3 | 题型：方案题 | 频率：中 | 关键词：**最快响应**/**容量1channel**/**close取消**/**context取消**/**select**
> 原文锚点：第 33~60 段「异步发 3 请求→结果写容量 1 channel 取最先返回→无缓冲 bool channel close 通知其余取消→实际 HTTP 取消用 context」

## 一句话总述
「取最快响应」是 channel 的另一妙用：异步发起 N 个请求，把结果写进**容量为 1** 的 channel，只有最先返回的 goroutine 能写入、主协程读到即视为最快响应；同时用一个**无缓冲 bool channel**，拿到最快响应后 `close` 它，其余请求在 `select` 中检测到 close 即退出函数释放资源——真实 HTTP 取消须靠 `context` 取消底层请求。

## 面试官视角
- 考察意图：能否用「容量 1 channel + close 广播」实现最快响应与取消，并知道演示与生产的区别。
- 分档：P5 知容量 1 channel 只留最先结果；P6 能写 close 广播取消；P7 知演示用 channel、真实 HTTP 须 context 取消。
- 红旗答案：拿到最快响应后不取消其余请求（浪费资源）；把 channel close 当成真正取消了 HTTP 请求。
- 惊艳点：点出「close 一个 channel 可被多个接收方同时感知、天然广播语义」，以及「channel 只取消函数、真实网络取消靠 context」 [经验]。

## 主问答
**Q（面试官原话）：** 多个请求只要最快那个返回的结果，其余怎么处理？
**A：**
1. **容量 1 channel 取最快**：异步发 N 请求，完成写容量 1 的 channel，只有最先返回的 goroutine 写成功，主协程读到即最快响应 [经验]。
2. **close 广播取消其余**：另起无缓冲 bool channel，拿到最快响应后 `close` 它；其余请求 `select` 检测到关闭即退出函数、不再占用资源 [经验]。
3. **真实 HTTP 用 context**：演示用 channel 模拟取消；实际 HTTP 请求取消须用 `context` 取消底层连接，而非仅退出业务函数 [经验]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 怎么取最快？ | 机制 | 容量1 channel | P5 |
| L2 | 其余咋办？ | 取消 | close 广播 | P6 |
| L3 | close 语义？ | 特性 | 多接收方感知 | P6 |
| L4 | 真取消？ | 生产 | context 取消 | P7 |
| L5 | 超时？ | 工程 | ctx WithTimeout | P7+ |

## 版本与兼容性
- 本卡只覆盖「最快响应 + 取消」；channel 令牌桶限流见 1016、令牌桶 vs 信号量见 1016 [边界]。
- 信号量限并发见 1015、context 取消模式见 1025 等——本卡只引不重述 [边界]。

## 关键代码

```go
// 取最快响应：容量 1 channel 只留最先返回；close 广播取消其余
func fastest(urls []string) (string, error) {
    respCh := make(chan string, 1) // 容量 1：只有最先返回的能写入
    done := make(chan struct{})    // 无缓冲：close 即广播
    ctx, cancel := context.WithTimeout(context.Background(), 3*time.Second)
    defer cancel()
    for _, u := range urls {
        go func(u string) {
            r, err := doHTTP(ctx, u) // 真实请求用 ctx，可被取消
            if err != nil {
                return
            }
            select {
            case respCh <- r: // 最先完成者写入
                close(done) // 通知其余退出
            default:
            }
        }(u)
    }
    select {
    case r := <-respCh:
        return r, nil
    case <-ctx.Done():
        return "", ctx.Err() // 超时取消全部
    }
}
```

## 总结与追问预判
「最快响应」本质是「多生产者、单槽 channel、谁先谁赢」的竞态收敛。配合 context 超时即构成完整的「竞速 + 取消 + 超时」三件套。

## ⚠️ 原文纠错
1. 事实核校： [经验] 容量 1 channel 取最先返回、无缓冲 channel close 广播取消、真实 HTTP 用 context 取消——均正确。
2. 崩坏词归一：源码将若干术语音译为崩坏词，本卡统一为规范术语（goroutine、channel、context、取消、竞速等）。
