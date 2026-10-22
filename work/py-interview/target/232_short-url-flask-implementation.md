# 232. 短网址服务编码实现（Flask + Redis + MySQL）

> 分类：系统设计 | 难度：L4 | 题型：实战编码+面试表达 | 频率：高 | 关键词：**Flask** / **Redis INCR** / **MySQLdb** / **视图函数** / **图文并茂** / **白纸分区**
> 原文锚点：第10章 10-2「单文件 Flask 应用：MySQL存数据+Redis计数器；建表 shot_url(id自增,token,url,created_at,token索引)；视图：取 request.json['url']→redis incr 得 index→encode(index) 得 token→INSERT INTO shot_url(token,url) VALUES(%s,%s)→commit→返回 short.com+token(redis INCR首次返回1略过0)；演示正确返回短网址；回答重点：图文并茂，白纸分区=左上数据表/中间算法+接口/底部请求流程图，紧扣三要素；常见题：短网址/秒杀/评论系统」

## 一句话总述
**落地短网址服务用单文件 Flask**：`request.json` 取长 URL → **Redis `INCR` 拿全局自增 index** → `encode(index)` 得 62 进制 token → **MySQL 参数化 INSERT** → 提交并返回 `short.com/{token}`。面试时**图文并茂**：白纸分区（左上数据表 / 中间算法+接口 / 底部请求流程图），紧扣三要素。

## 面试官视角
- **考察意图**：能否把设计"真正写出来跑通"，而不是只会讲；以及能否在白板上结构化表达。
- **P5** 能说出实现主线（取 URL→计数→编码→落库→返回） / **P6** 能写出关键代码（Redis INCR + 参数化 INSERT，注意防注入）并指出"INCR 首次返回 1" / **P7** 能讲清"为何 Redis 做计数器而非 MySQL 自增（分布式/原子/高性能）"，并演示白纸分区画图法。
- **红旗**：INSERT 用字符串拼接（注入风险）；把 Redis 计数器当成可有可无；面试只口述不画图。
- **惊艳点**：强调"参数化查询防注入（呼应 524 卡）"与"INCR 原子性避免并发重复 ID"，以及"白纸分区=数据表/算法/流程图三块" `[经验]`。

## 主问答
**Q（面试官原话）：** 你刚才的设计，能写个 demo 实现吗？面试怎么讲清楚？

**A · 标准答案骨架：**
1. **实现主线（4 步）**：① 从 `request.json['url']` 取长 URL；② `index = redis.incr('counter')` 拿全局自增 ID（**原子、并发安全**，首次返回 1）；③ `token = encode(index)` 转 62 进制短码（见 231）；④ **参数化** `INSERT INTO shot_url(token, url) VALUES(%s, %s)` → `commit` → 返回 `https://short.com/{token}`。
2. **为什么 Redis 做计数器**：自增 ID 需要**全局唯一且高并发**——Redis `INCR` 单命令原子、性能高，比 MySQL 自增更适合分布式/高并发计数（MySQL 自增也可，但跨实例扩展弱）。
3. **面试表达法（图文并茂）**：白纸合理分区——**左上角**写数据表定义（字段+索引）、**中间**写算法原理 + 接口契约、最**底部**画请求流程图（请求→计数→编码→落库→返回）。围绕"场景/存储/算法"三要素展开，让面试官一眼看懂 `[经验]`。
4. **常见题库**：短网址、秒杀、评论系统最常被考，针对性总结这几类即可举一反三。

**加分层**：能补"短还原长接口（凭 token 查表返回原 URL 做 302 跳转）"与"防注入用参数化（呼应 524 卡 SQL 注入防范）"。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 怎么实现 | 基本认知 | 取URL→计数→编码→落库 | 换题 → 不及格 |
| L2 | 为何Redis计数 | 选型 | INCR原子/高并发/全局唯一 | 判 P5 |
| L3 | 防注入 | 安全意识 | 参数化INSERT(%s) | 判 P6 |
| L4 | 面试怎么讲 | 表达 | 白纸分区图+三要素 | 判 P6+ |
| L5 | 还原跳转/扩展 | 高阶 | 302跳转+分库/缓存 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| Flask + Redis INCR + MySQL 参数化方案长期成立 | 无版本翻转 | 仍按此栈答；可补"异步落库/消息队列解耦"作为进阶，但不偏离主流程 |

## 关键代码
```python
# 短网址服务视图函数（Flask + Redis 计数器 + MySQL 存储）[源码, python]
import redis, pymysql
from flask import Flask, request

app = Flask(__name__)
r = redis.Redis()                                  # 全局自增 ID 计数器
conn = pymysql.connect(host="localhost", user="root",
                       password="", database="test")

@app.route("/shorten", methods=["POST"])
def shorten():
    long_url = request.json["url"]                 # ① 取长 URL
    index = r.incr("short_url_counter")            # ② 原子自增 ID（首次返回 1）
    token = encode(index)                          # ③ 十进制 → 62 进制短码
    with conn.cursor() as cur:
        cur.execute(                               # ④ 参数化 INSERT，防注入
            "INSERT INTO shot_url(token, url) VALUES (%s, %s)",
            (token, long_url))
    conn.commit()
    return {"short_url": f"https://short.com/{token}"}
```

## ⚠️ 原文纠错
- 机翻还原：「flash / flassql / 少鸭lapp」→ **Flask**；「RRM / myyirlLDB」→ **MySQLdb**；「EDIS/REIS/rerei/relei」→ **Redis**；「ICR」→ **INCR**；「rereisase点store」→ **redis_client（调用 INCR）**；「circle / insersertinto / shot_url / shodRL」→ **SQL / INSERT INTO / short_url 表**；「百分之s / 位位符」→ **`%s` 占位符**；「valvaleses」→ **VALUES**；「长幺l」→ **长 url**；「connection点cuser」→ **connection.cursor()**；「short点com」→ **short.com（演示主机名）**；「外b框架」→ **Web 框架**。
- 原文"单文件 Flask、Redis INCR 计数、MySQL 参数化落库、返回 short.com+token、白纸分区图文并茂"均准确。
- 原文未显式强调"参数化防注入"，已结合 524 卡补强（见加分层与代码注释）。

## 总结与追问预判
短网址实战把 528/529/530/531 串成闭环：场景估算→MySQL 存储→base62 算法→Flask+Redis+MySQL 落地，面试用白纸分区图文并茂表达。第十章系统设计完结（10-3 为章末总结 R4，见进度表）。
