# 178. Cookie 与 Session 的区别

> 分类：网络/HTTP | 难度：L2 | 题型：对比题 | 频率：高 | 关键词：**Cookie** / **Session** / **无状态** / **sessionID**
> 原文锚点：第 121~148 段「HTTP 无状态；session 是服务端识别用户的方式（存 sessionID）；cookie 是 session 的一种实现（存客户端）；URL 重写也能实现」

## 一句话总述
HTTP 是**无状态**的，需服务端给每个用户生成标识来识别。**Session** 指"识别用户会话"的机制（通常服务端存 sessionID→用户ID）；**Cookie** 是实现 session 的**一种方式**（把 sessionID 存在客户端、每次请求带回）。另一种方式是 **URL 重写**（sessionID 拼进 URL 参数）。

## 面试官视角
- **考察意图**：是否分清"概念（session=识别机制）"与"实现（cookie=存储载体）"，且知道无状态是根因。
- **P5** 能说出 HTTP 无状态、cookie 存客户端 / **P6** 能讲清 session 在服务端、cookie 是载体、sessionID 对应关系 / **P7** 能对比 cookie 与 URL 重写、指出 cookie 值应加密、以及 session 存储（Redis）与过期。
- **红旗**：把 cookie 与 session 当成"两个并列的东西"而非"机制与实现"；或认为 cookie 存了全部用户数据。
- **惊艳点**：cookie 只存 **sessionID**（小、加密），真正用户数据在**服务端**（常存 Redis 按 ID 取）——所以服务端压力小、易横向扩展；cookie 被盗还有 CSRF/XSS 风险需 `HttpOnly/SameSite` 防护 —— 验证：`document.cookie` 与 `Set-Cookie` 头即可观察 `[经验]`。

## 主问答
**Q（面试官原话）：** Cookie 和 Session 有什么区别？

**A · 标准答案骨架：**
1. **先给结论**：**Session** 是"识别用户会话"的**机制**（服务端保存 sessionID→用户ID）；**Cookie** 是实现它的**一种载体**（把 sessionID 存在客户端、每次自动带回）。
2. **再给机制**：HTTP 无状态→服务端生成 sessionID；**Cookie** 方式由服务端 `Set-Cookie`、浏览器存客户端、后续请求自动带；**URL 重写**方式把 sessionID 拼进查询参数。
3. **最后给边界**：Cookie 里通常**只放 sessionID（加密）**，真实数据在服务端（常存 Redis）；除 cookie 外还可用 URL 重写实现 session，二者是"机制 vs 实现"而非并列。

**加分层**："session 是目的、cookie 是手段"一句话厘清关系；再补 `HttpOnly/Secure/SameSite` 才是生产级答案 `[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 为什么需要 session | 基本认知 | HTTP 无状态 | 换题 → 不及格 |
| L2 | cookie 存哪、session 存哪 | 是否背的 | cookie 客户端/session 服务端 | 判 P5 |
| L3 | URL 重写是什么 | 有没有真理解 | sessionID 拼 URL | 判 P6 |
| L4 | cookie 安全问题 | 架构判断 | HttpOnly/CSRF/XSS | 判 P6+ |
| L5 | 你用 Redis 存 session 吗 | 实战经验 | 分布式会话/过期 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| 通用 Web 模型 | 无 | 机制/实现区分稳定；可提 JWT 把状态移到客户端（无服务端 session） |

## 关键代码
```python
# 服务端：sessionID → user_id 映射（常存 Redis）[经验]
sessions = {"sess_abc123": 1001}
# 客户端：Cookie 携带 sessionID，每次请求带回，服务端据此取用户
def get_user(cookie_sid):
    return sessions.get(cookie_sid)
```

## ⚠️ 原文纠错
原文第 121~148 段音译需还原：「**筛选ID**」→ **sessionID（会话标识）**（ASR 误识）；「**cooooe/cooking/扣汇/扣绘**」→ **cookie**；「**sidecookie**」→ **set_cookie（设置 Cookie）**；「**REliase**」→ **Redis**；「**URR**」→ **URL**。概念（HTTP 无状态、session 是识别机制、cookie 是实现方式、URL 重写可替代）正确。核对范围：第 121~148 段 Cookie 与 Session。

## 总结与追问预判
- 无状态→需识别；session 是机制（服务端存 sessionID→userID），cookie 是实现（客户端载体），URL 重写可替代。
- 顺势会问：**HTTP 报文结构（见 173 卡）**、**WSGI 与部署（见 159/460 卡）**。
