# 107 复制账号该给什么权限？8.0 认证插件坑在哪

> 分类：架构/复制 | 难度：L2 | 题型：工程题 | 频率：高 | 关键词：**REPLICATION SLAVE** / **caching_sha2_password** / **mysql_native_password** / **SSL**
> 原文锚点：第 174~184 段「把默认认证方式改成了 mysql_native_password，因为一些工具还不支持 8.0 默认的认证插件」

## 一句话总述
复制账号只要 **`REPLICATION SLAVE`** 一个权限；真正的坑不在权限，而在 **MySQL 8.0 默认认证插件换成 `caching_sha2_password`**，老客户端和老 HA 工具连不上。

## 面试官视角
- **考察意图**：区分「会建账号」和「踩过 8.0 升级的连接故障」。
- **P5** 能写出 `GRANT REPLICATION SLAVE` / **P6** 说清 8.0 换默认插件这件事及 `caching_sha2_password` 的两种交换方式 / **P7** 会补「要么开 SSL，要么换回 `mysql_native_password`，并说明这个妥协的安全代价」。
- **红旗**：「复制账号给 `ALL PRIVILEGES` 省事」；「8.0 和 5.7 账号通用」；「改 `default_authentication_plugin` 重启就好，不用管已有账号」。
- **惊艳点**：已有账号的插件是**建号时固化**的，只改全局 `default_authentication_plugin` **不影响存量账号**，必须 `ALTER USER ... IDENTIFIED WITH mysql_native_password` 重建密码 —— 验证：`SELECT user,host,plugin FROM mysql.user;`（8.0.36 `[经验]`）。

## 主问答
**Q：复制账号怎么建？升级到 8.0 后从库连不上主库了，你先查什么？**
**A：**
1. **先给结论**：只授 `REPLICATION SLAVE`（8.0.26+ 也可写 `REPLICATION SLAVE` 的同义新名），不要图省事给 `ALL`；连不上时**第一查认证插件**，第二查 SSL 与网络。
2. **再给机制**：8.0 默认 `caching_sha2_password`，它要求**加密通道或 RSA 公钥交换**才能传密码；老的 `mysql_native_password` 客户端库不认识它，直接报 `Authentication plugin 'caching_sha2_password' cannot be loaded`。
3. **最后给边界**：改插件是**降级妥协**——`mysql_native_password` 用 SHA1，安全强度弱于 `caching_sha2_password`；能上 SSL 就别降插件。
**加分层**：MMM / MHA / 旧版 ProxySQL 这类工具不支持新插件，是实战中被迫降回 `mysql_native_password` 的主因。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 复制需要什么权限 | 概念 | REPLICATION SLAVE | 换题 |
| L2 | 8.0 默认插件叫什么 | 版本感 | caching_sha2_password | 判 P5 |
| L3 | 为什么老客户端连不上 | 机制 | 需要 SSL 或 RSA 交换 | 判 P6 |
| L4 | 换回旧插件的代价 | 权衡 | SHA1，安全强度下降 | 判 P6+ |
| L5 | 改全局参数后老账号变了吗 | 实战 | 不变，要 ALTER USER | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| 5.7 默认 `mysql_native_password`；8.0 默认 `caching_sha2_password`（验证 8.0.36） | 8.0.4 起切换默认值；8.0.34 起 `mysql_native_password` 默认不再内置启用 | 新集群走 SSL + 新插件；要兼容老工具才显式降回旧插件 |

## 关键代码
```sql
-- 查看每个账号实际使用的认证插件
SELECT user, host, plugin FROM mysql.user;
-- 兼容老 HA 工具：把复制账号降回旧插件（必须重建密码才会切换）
ALTER USER 'repl'@'192.168.1.%'
  IDENTIFIED WITH mysql_native_password BY '***';
```

## ⚠️ 原文纠错
原文只说「8.0 默认认证方式 MMM/MHA 不支持，所以改成 mysql_native_password」，未点出**新插件需要 SSL 或 RSA 公钥交换**这一根因，也未说明**改全局参数不会改变存量账号**；已在主问答补全。机翻「mysqlnegativepassword」还原为 **`mysql_native_password`**。原文未提权限名，按官方要求补全为 `REPLICATION SLAVE`。

## 总结与追问预判
- 权限一个就够，坑在认证插件与加密通道。
- 下一题：见 106（异步复制搭建）、109（CHANGE MASTER TO 与 START SLAVE）。
