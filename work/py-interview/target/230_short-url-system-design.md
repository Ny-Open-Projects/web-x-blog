# 230. 短网址系统设计（需求·场景·存储）

> 分类：系统设计 | 难度：L4 | 题型：设计+实战 | 频率：高 | 关键词：**短网址** / **TinyURL** / **接口设计** / **MySQL 存储** / **QPS 估算** / **base62**
> 原文锚点：第10章 10-2「短网址系统=长网址转短网址服务(tinyurl/bitly)；需求：①长转短并存储 ②短还原长(跳转)；约束：短码后缀≤7位(大小写字母+数字62字符集)、为公司各业务提供共享服务(DRY)；QPS估算：以 bitly 实测每秒新增数百条、查询上千条，插入峰值数百/秒；存储：仅用 MySQL(运维成熟)，字段=自增ID/token(短码,不存完整短网址以便换主机名)/原URL/created_at，索引=token 加索引(唯一查询:根据短码还原长网址)」

## 一句话总述
**短网址系统 = 把长 URL 映射成 ≤7 位短码（62 字符集）并提供"长转短 / 短还原长"的服务**。设计上先量化场景（bitly 实测每秒新增数百、查询上千），存储只用 MySQL 即可：四字段（自增 ID / token / 原 URL / 创建时间）+ 给 token 加索引。

## 面试官视角
- **考察意图**：能否把"三要素框架"真正落地到一道真题——先厘清需求与约束、再算 QPS、最后定存储与索引。
- **P5** 能说出需求（长转短+短还原）与两个接口 / **P6** 能给出存储设计（MySQL 四字段、token 索引）并做 QPS 估算、解释"为何不存完整短网址" / **P7** 能讨论"单机 MySQL 不够时如何扩展（分库/缓存热点）、token 冲突与全局唯一性"。
- **红旗**：一上来就写 base62 代码却说不清需求与 QPS；把短码当主键或忽略索引。
- **惊艳点**：点出"只存 token 不存完整短网址，方便替换主机名/域名"，以及"公司级共享服务契合 DRY" `[经验]`。

## 主问答
**Q（面试官原话）：** 如何设计一个短网址系统？

**A · 标准答案骨架：**
1. **需求与接口**：核心两个 API——`long_to_short_url`（长→短并落库）、`short_to_long_url`（短→长，用于跳转）。本质是"长 URL ↔ 短码"的映射存储。
2. **场景与约束 + QPS 估算**：典型如 bitly/TinyURL；约束是**短码后缀 ≤7 位、由大小写字母+数字共 62 字符组成**。以 bitly 实测为参考——**每秒新增数百条、查询上千条**，插入峰值约数百/秒，量级不大，无需一上来就分布式 `[经验]`。
3. **数据存储设计**：直接选 **MySQL**（公司运维成熟、MySQL+Redis 常可支撑）。表字段四样：① 自增 `id`；② `token`（短码，**只存短码不存完整短网址**，方便换主机名）；③ 原 `url`；④ `created_at`。**索引只给 token 加**（唯一查询就是"凭短码还原长网址"）。
4. **短码算法与编码实现**：见 231（base62 编码）、532（Flask+Redis 计数器落地）。

**加分层**：能补"7 位 62 进制 = 62^7 ≈ 3.5 万亿，规模足够"；以及"若未来量极大，可对 token 分库、对热点短码加缓存"。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 短网址做什么 | 基本认知 | 长→短映射+跳转 | 换题 → 不及格 |
| L2 | 有哪些接口 | 需求拆解 | long_to_short/short_to_long | 判 P5 |
| L3 | 怎么存储 | 选型 | MySQL 四字段+token索引 | 判 P6 |
| L4 | QPS 多少 | 量化 | bitly实测数百增/上千查 | 判 P6+ |
| L5 | 量大怎么扩 | 高阶 | 分库/缓存热点/全局唯一 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| "MySQL 存映射 + token 索引"方案长期成立 | 无版本翻转 | 仍按四字段+token 索引答；可补分库分表/缓存作为扩展手段 |

## 关键代码
```sql
-- 短网址映射表（要素二：数据存储落地）[源码, sql]
CREATE TABLE shot_url (
    id          BIGINT        PRIMARY KEY AUTO_INCREMENT,  -- 自增主键，作 base62 源
    token       VARCHAR(10)   NOT NULL UNIQUE,            -- 短码（只存短码，主机名可替换）
    url         VARCHAR(2048) NOT NULL,                   -- 原始长网址
    created_at  DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_token (token)                                -- 凭短码还原长网址的唯一查询
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

## ⚠️ 原文纠错
- 机翻还原：「转网者 / 屌网址 / 展网者 / 装置token」→ **短网址 / 短码 token**；「tinyairservice」→ **TinyURL service**；「beitty/BC点com」→ **bitly.com**；「c位」→ **7 位**；「ftwitter」→ **Twitter**；「b子里」→ **bitly**；「外b框架」→ **Web 框架**；「nocircle」→ **NoSQL**；「circle / insersertinto / shot_url」→ **SQL / INSERT INTO / short_url 表**；「百分之s / 位位符」→ **`%s` 占位符**；「valvaleses」→ **VALUES**；「长幺l」→ **长 url**；「connection点cuser」→ **connection.cursor()**；「flash」→ **Flask**；「myyirlLDB」→ **MySQLdb**；「EDIS/REIS/relei」→ **Redis**；「ICR」→ **INCR**；「RRM」→ 误读（应为 MySQLdb 与 Redis）。
- 原文"需求两接口、≤7位62字符集、bitly QPS 实测、MySQL 四字段、token 索引"均准确。
- 原文"只存 token 不存完整短网址以便换主机名"准确，已作为加分点。

## 总结与追问预判
短网址系统=需求(两接口)+场景(QPS 估算)+存储(MySQL 四字段/token 索引)。短码算法（MD5 截断 vs 自增 base62）见 231 卡，编码实现见 232 卡。
