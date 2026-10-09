# 704 Go HTTP Server 如何防止表单重复提交

> 分类：Web / Go net/http | 难度：L2 | 题型：方案设计 | 频率：高 | 关键词：**重复提交、幂等 token、PRG、GETDEL、URL 编码**

> 原文锚点：第 1~29 段「隐藏 token 或验证码、Post/Redirect/Get 模式、异步提交并禁用按钮、生成 token 时的 URL 编码问题」

## 一句话总述
防重复提交要**前后端一起做**：后端生成一次性 token 存 Redis、随表单下发隐藏字段、提交时用 `GETDEL`（原子取走即删）校验并消费；处理成功后用 **PRG（Post/Redirect/Get）** 重定向到结果页，让刷新/回退只重复 GET；前端禁用按钮只是体验层，可绕过，不能作为唯一防线。

## 面试官视角
P5 答「前端禁用按钮」就停了；P6 要说出 **PRG** 和 **服务端一次性 token** 两层；P7 必须补上「校验必须原子」（查了再删会有并发窗口）、「token 必须服务端生成并绑定用户/表单」、「重定向用 303 而不是 302」以及「接口幂等的终极兜底是唯一索引/业务主键」。

## 主问答
**Q（面试官原话）：** 用户狂点提交按钮，或者提交完刷新页面，表单被重复提交了，你怎么防？

1. **先定位三种来源**：① 处理完停留在 POST 结果页，**刷新/回退**重放 POST；② 网络差时用户**双击**提交按钮；③ 绕过界面用脚本**直接重放**请求。三种来源决定了必须多层防御 `[经验]`。
2. **PRG 解决第一种（必答）**：POST 处理成功后不返回页面，而是 `http.Redirect(w, r, "/result", http.StatusSeeOther)` 重定向到另一个 GET 路由；浏览器地址栏变成 GET，刷新只会重发 GET `[源码]`。**必须用 303**（`StatusSeeOther`）——302 在部分历史实现里会把重定向请求仍按 POST 发出，303 才强制转 GET。
3. **一次性 token 解决第二、三种（核心）**：GET 渲染表单时 `crypto/rand` 生成随机串存进 Redis（带 TTL，如 5 分钟），作为隐藏字段 `<input type="hidden" name="token" value="...">` 下发；POST 时校验并**原子取走** `[实测]`。本机用 `sync.Map` 的 `LoadAndDelete` 模拟原子消费：第 1 次提交 `loaded=true` 放行，第 2、3 次 `loaded=false` 直接拒绝——**关键点在"取"和"删"是一个原子动作**，生产用 Redis 的 `GETDEL`（Redis 6.2+）或 `SETNX` + 过期，绝不能先 `GET` 判存在再 `DEL`（并发下两个请求都能 GET 成功）。
4. **前端禁用按钮只是体验层**：异步提交（`fetch`/AJAX）后立即 `disabled = true`，并在收到响应前阻止二次点击；但这**只能在前端校验**，用户绕过界面直接发请求照样重复提交，所以服务端 token 校验不可省 `[经验]`。
5. **token 生成要过 URL 编码这一关**：HTTP 传参时特殊字符（空格、`+`、`&`、`=`、`%`）必须编码，否则服务端拿到的和客户端提交的不一致 `[实测]`——本机 Go 1.26.5 实测：原始 token `ab c+d&e=f%g`，经 `url.Values.Encode()` 变成 `token=ab+c%2Bd%26e%3Df%25g`，`url.ParseQuery` 能**原样取回** `ab c+d&e=f%g`；而**不编码直接拼接** `token=ab c+d&e=f%g` 时，解析报 `invalid URL escape "%g"`，取回的只有 `ab c d`——**已失真**。
6. **token 生成的两种建议（原文两条 + 一条修正）**：① 只生成字母数字组合，天然无需编码；② 需要任意字符时用编码输出——**本机实测长度**：`crypto/rand` 16 字节 → hex 32 字符 / base64url 22 字符，32 字节 → hex 64 字符 / base64url 43 字符；HMAC-SHA256 签名 32 字节 → base64url 43 字符 `[实测]`。原文建议用 MD5，这里**修正为**：MD5 作为不可逆摘要生成 token 虽可行，但已被证明可碰撞，安全场景应换 `crypto/rand` + `HMAC-SHA256`（顺带防篡改）。

## 追问链
| 层级 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 重复提交有哪几种来源？ | 场景拆解 | 刷新重放 POST、双击、脚本直接重放三类 | 只说得出"用户点两下"，停在 L1 |
| L2 | 处理完直接返回页面有什么问题？ | PRG 意识 | 地址栏停在 POST，刷新会重放；改用 303 重定向到 GET 结果页 | 不知道 PRG，停在 L2 |
| L3 | token 存在哪、怎么校验？ | 服务端状态 | 服务端生成存 Redis 带 TTL，隐藏字段下发，提交时原子取走 | 说"存 session 里判断一下"，停在 L3 |
| L4 | 先 GET 判断再 DEL 有什么问题？ | 并发原子性 | 两个并发请求都 GET 成功 → 都放行；要用 GETDEL/SETNX 原子操作 | 看不出并发窗口，停在 L4 |
| L5 | 重定向为什么用 303 不用 302？ | 协议细节 | 302 在部分实现中重定向仍发 POST，303 强制转 GET | 答不出状态码差异，停在 L5 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| HTTP/1.1 全版本 | 303 See Other 语义 | PRG 一律用 `http.StatusSeeOther` |
| Go 全版本 | `net/http` 表单与重定向 | 无需第三方依赖 |
| **Go 1.22+** | `ServeMux` 支持 `POST /path` 方法路由 | 提交与结果页路由可显式分开声明，天然配合 PRG |
| Redis 6.2+ | `GETDEL` 原子取走 | 优先 `GETDEL`；更低版本用 `SETNX` + TTL 或 Lua 脚本 |
| 任意版本 | 接口幂等兜底 | 数据库唯一索引/业务主键兜底（见 1223） |

## 关键代码
```go
// ① GET：渲染表单时下发一次性 token（生产存 Redis，这里用内存 map 示意）
var tokens sync.Map // token -> 过期时间戳

func showForm(w http.ResponseWriter, r *http.Request) {
    b := make([]byte, 32)
    _, _ = rand.Read(b)
    tok := base64.RawURLEncoding.EncodeToString(b) // 43 字符，URL 安全无需再编码
    tokens.Store(tok, time.Now().Add(5*time.Minute).Unix())
    fmt.Fprintf(w, `<form method="post" action="/submit">
    <input type="hidden" name="token" value="%s">
    <input name="content"><button type="submit">提交</button></form>`, tok)
}

// ② POST：原子取走即消费，处理成功后 303 重定向（PRG）
func submit(w http.ResponseWriter, r *http.Request) {
    tok := r.PostFormValue("token")
    if _, ok := tokens.LoadAndDelete(tok); !ok { // 原子：取 + 删一步完成
        http.Error(w, "重复提交或 token 失效", http.StatusForbidden)
        return
    }
    // ... 落库等业务逻辑
    http.Redirect(w, r, "/result?ok=1", http.StatusSeeOther) // 303，强制转 GET
}
```

## 总结与追问预判
答题骨架背这三句：**「PRG 治刷新、一次性 token 治重放、唯一索引兜底」**。追问大概率走向两个方向：一是把 token 换成通用幂等方案（幂等键 + 唯一索引，见 1223；消息队列侧的幂等消费见 1418），二是追问分布式下 Redis 不可用怎么办（答：降级到数据库唯一索引做幂等表，或客户端生成幂等键 + 服务端去重表）。

`[边界]` 本卡只讲**防重复提交的三层机制与 token 的 URL 编码陷阱**，**不重述**表单的接收与字段读取（见 703）、`FormValue` 与 `PostFormValue` 的差异（见 703）、路由注册与多路复用器（见 702）。

## ⚠️ 原文纠错
1. 补充：原文只说「检查 token 是否被提交过」，未强调**原子性**；先查后删在并发下会双放行 `[经验]`。
2. 修正：原文称重定向到"另一个页面"，未指明状态码；PRG 应用 **303** 而非 302 `[经验]`。
3. 修正：原文建议对随机串做 MD5 编码，MD5 已可碰撞，应换随机串 + HMAC 签名 `[经验]`。
4. 补充：原文未提 token 需绑定用户与 TTL，裸 token 会被跨用户冒用 `[经验]`。
5. 崩坏词归一：源码将若干术语音译为崩坏词，本卡统一为规范术语 `[经验]`。
