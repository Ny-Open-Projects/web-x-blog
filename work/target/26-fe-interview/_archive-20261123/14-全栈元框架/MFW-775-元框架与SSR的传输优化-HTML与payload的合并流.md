---
title: [MFW-775] HTML 与 payload 的合并流
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-775：HTML 与 payload 的合并流

**答**:
- Next 的双流合并（RBL-507 深化）：1) **单响应双内容**（HTML shell + Flight payload 在同一个响应（payload 附加在 HTML 后——单 TCP 连接/单压缩流/单缓存条目）；2) **payload 的嵌入方式**：HTML 内嵌 `<script>(self.__next_f=self.__next_f||[]).push(chunk)</script>`——Flight chunk 以 inline script 推入（client 解析器消费）；3) **合并的流序**：HTML 先（shell）→ payload chunk 穿插（每个 Suspense resolve 时对应的 Flight chunk 紧跟 HTML patch——双流的时序交织 RBL-507）。
- 合并流的压缩优化：HTML 与 Flight 同流压缩（共享字典 RBL-702）——HTML 的重复结构被 Flight 的重复结构共用字典——压缩率高于分流。
- 分流 vs 合并流的选材：合并流（Next 默认——单请求简单）；分流（payload 独立请求——payload 可独立缓存/复用——RSC prefetch 的形态）；「合并 = 初始加载、分流 = 导航 prefetch」。
- 追问钩子：为什么「payload 嵌入 HTML 的 inline script」而非「独立 script src」？——inline = payload 与 HTML 同流到达（无额外请求——数据与渲染同步）；script src = payload 需要单独请求（额外 RTT——数据延迟）；「同流的原子性」：payload 与 HTML 一起到达（chunked 流——HTML 渲染完 payload 立即可解析——无等待）；inline script 的体积代价（payload 内嵌 HTML——HTML 体积增大）被压缩弥补（RBL-702 双流压缩）。

```javascript
// Next 的合并流形态
// HTTP 响应：
// <!-- HTML shell -->
// <div>...content...</div>
// <!-- Flight chunk 内嵌 -->
// <script>(self.__next_f=self.__next_f||[]).push(["0",["$","div",...]])</script>
// <!--$?--><template id="B:0"></template>...
// <script>(self.__next_f.push(["1","..."]))</script>
// <!-- 更多 HTML -->
// <script>(self.__next_f.push(["2","..."]))</script>
// client 解析器消费：
// window.__next_f.push = (chunk) => flightParser.process(chunk);   // inline script 推入
// 流序交织：HTML 段 → Flight chunk → HTML 段 → Flight chunk（交替）
```
