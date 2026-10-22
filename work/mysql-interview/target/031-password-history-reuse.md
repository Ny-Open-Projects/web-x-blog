# 031 历史密码重用策略（8.0）

> 分类：用户管理 | 难度：L3 | 题型：工程题 | 频率：中 | 关键词：**PASSWORD HISTORY** / **PASSWORD REUSE INTERVAL** / **password_reuse_history**
> 原文锚点：第 131~166 段「在 MySQL 8.0 中我们可以设置用户不能重用 n 次以内的密码…也可以控制禁止重用 n 天前的密码」

## 一句话总述
**8.0 新增历史密码限制**：`PASSWORD HISTORY n`（禁止重用最近 n 次用过的密码）与 `PASSWORD REUSE INTERVAL n DAY`（禁止重用 n 天内用过的密码），通常与密码过期**配套使用**。

## 面试官视角
- **考察意图**：这是 8.0 的新能力，用来区分"用过 8.0"和"只停留在 5.7"。
- **P5** 知道 8.0 能限制历史密码重用。
- **P6** 能说出两种维度（次数 / 时间）与对应语法，并知道要配合过期策略才有意义。
- **P7** 能指出落地前提：应用必须支持自动换密码，否则每次过期改密码都要人工介入，运维成本陡增。
- **红旗**：① 说 5.7 就有这个功能；② 只知次数不知时间维度；③ 认为设了历史策略就"足够安全"。
- **惊艳点**：限制的是**次数或时间**，两者可同时设置；设 `PASSWORD HISTORY 1` 后**重设成原密码会被明确拒绝** `[实测]` —— 验证：`ALTER USER 't'@'localhost' PASSWORD HISTORY 1;` 后再 `SET PASSWORD = '原密码'`，返回 ERROR 3638。

## 主问答
**Q（面试官原话）：** 密码过期了，用户把密码改回原来那个，能防住吗？

**A：**
1. **结论**：**8.0 可以**——用 `PASSWORD HISTORY n` 禁止重用最近 n 次密码，或 `PASSWORD REUSE INTERVAL n DAY` 禁止重用 n 天内的密码。
2. **机制**：8.0 在用户上记录历史密码信息（`mysql.password_history`），改密码时按次数/时间双重校验，不满足就报错拒绝。
3. **边界**：这两个策略**只在密码被改时才生效**，通常与"密码过期"配套——过期强制改，历史策略保证改出来的不是旧的。

**加分层**：也可用全局默认值 `password_history` / `password_reuse_interval` 统一约束，再用单账号设置覆盖，避免逐账号配置的漏网。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 8.0 有没有历史密码功能 | 版本能力 | 有，PASSWORD HISTORY | 换题 → 不及格 |
| L2 | 能按次数还是时间 | 两个维度 | 两者皆可 | 判 P5 |
| L3 | 历史密码存哪 | 机制 | 8.0 的 password_history 表 | 判 P6 |
| L4 | 为什么必须配套过期策略 | 设计理解 | 不触发改密就不校验 | 判 P6+ |
| L5 | 落地要什么前置条件 | 工程判断 | 程序能自动取新密码 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| 5.7 | **只有**密码过期，**无**历史密码限制 | 老版本答"只能靠外部流程约束" |
| 8.0 | 新增 `PASSWORD HISTORY` / `PASSWORD REUSE INTERVAL` | 现在按"过期 + 历史"配套答 |

## 关键代码
```sql
-- 建账号时一次性配好：90 天过期 + 禁止重用最近 5 次密码
CREATE USER 'app'@'192.168.1.%' IDENTIFIED BY 'Pwd#2026a'
  PASSWORD EXPIRE INTERVAL 90 DAY
  PASSWORD HISTORY 5;
-- 改密时违反历史策略会报错（ERROR 3638）
SET PASSWORD = 'Pwd#2026a';   -- 与历史重复，被拒绝
SELECT user, host, password_reuse_history FROM mysql.user WHERE user='app';
```

## ⚠️ 原文纠错
原文把 `password_history` 介绍为"禁止使用前 n 次密码"，方向正确；但原文口述"password history 的 count / default"时把 **default（跟随全局默认）与 default 值=0** 混为一谈——准确语义是 `PASSWORD HISTORY DEFAULT` 表示**跟随全局 `password_history` 变量**，此处已按官方语义修正。机翻音译（passwordhistorydeount、同用、重设）已还原为 PASSWORD HISTORY DEFAULT、重用、重设。

## 总结与追问预判
- 8.0 新增：**按次数**（PASSWORD HISTORY）与**按时间**（REUSE INTERVAL）双重历史限制。
- 必须与**密码过期**配套，否则不触发改密就等于没设。
- 下一题：见 030（密码过期策略）、032（过期对连接的影响）。
