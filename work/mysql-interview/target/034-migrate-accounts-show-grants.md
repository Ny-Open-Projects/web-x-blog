# 034 账号迁移方案二：导出授权语句重放

> 分类：用户管理 | 难度：L3 | 题型：设计题 | 频率：高 | 关键词：**pt-show-grants** / **SHOW CREATE USER** / **语句重放**
> 原文锚点：第 181~190 段「最方便的方式还是直接使用 Percona 公司所提供的 MySQL 管理工具集中的 pt-show-grants 工具」

## 一句话总述
**跨版本迁移账号的通用做法**：把源实例的 `CREATE USER` + `ALTER USER` + `GRANT` 语句导出成 SQL，在目标实例**重放执行**。

## 面试官视角
- **考察意图**：这是比"拷系统库"更专业的答案，看你是否知道有工具能把账号导出成可迁移语句。
- **P5** 知道可以写脚本读 mysql.user 拼语句。
- **P6** 能说出 **pt-show-grants**（Percona Toolkit）能导出建用户与授权语句。
- **P7** 能说明导出物的三段结构，并讲清它为什么比拷系统库更通用。
- **红旗**：① 手工拼 `CREATE USER` 却漏掉密码与账户属性；② 导出后不审阅直接全量执行。
- **惊艳点**：pt-show-grants 输出**可执行 SQL 文本**，因此**与版本、平台无关**，还能在重放前人工改 host 与密码策略 `[经验]` —— 验证：执行后观察输出，再 `mysql < out.sql` 重放。

## 主问答
**Q（面试官原话）：** 源库 5.6、新库 8.0，账号怎么迁过去？

**A：**
1. **结论**：不宜拷系统库（两版 `mysql.user` 结构差异大），应**导出建用户与授权语句**后在目标实例重放。
2. **机制**：最方便的是 Percona Toolkit 的 **`pt-show-grants`**（常用参数 `-u` 用户、`-p` 密码、`-h` 主机），输出标准 SQL：`CREATE USER` → `ALTER USER` 设密码与属性 → `GRANT` 授权。
3. **边界**：自写脚本读 `mysql.user` 也可行，但需自行处理**认证插件差异**（5.7 的 `mysql_native_password` 与 8.0 默认的 `caching_sha2_password`）。

**加分层**：重放前**先审阅输出**——host 可能绑旧 IP 段、密码插件可能不兼容新实例，这两处是迁移失败高频点。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 用什么工具导出 | 工具 | pt-show-grants | 换题 → 不及格 |
| L2 | 导出的是什么 | 产物理解 | 可执行 SQL 语句 | 判 P5 |
| L3 | 语句分几段 | 细节 | CREATE USER / ALTER USER / GRANT | 判 P6 |
| L4 | 为何比拷库通用 | 方案权衡 | 与版本平台无关、可审阅 | 判 P6+ |
| L5 | 迁移后怎么验收 | 工程闭环 | 逐账号 SHOW GRANTS 比对 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| 5.7 → 8.0 | 默认认证插件由 `mysql_native_password` 变为 `caching_sha2_password` | 迁移时可能需显式指定插件（详见 011 卡） |
| 8.0 | 原生支持 `SHOW CREATE USER` 直接拿建账号语句 | 补一句"8.0 原生也有 SHOW CREATE USER" |

## 关键代码
```sql
-- 导出（命令行工具，示意，未实跑）：pt-show-grants -h源 -u管理员 -p密码 > grants.sql
-- 重放：mysql -h目标 -u管理员 -p < grants.sql
SHOW CREATE USER 'app'@'192.168.1.%';
SHOW GRANTS FOR 'app'@'192.168.1.%';
```

## ⚠️ 原文纠错
原文把工具名读作"PDshobrrent / PP 设 grance"，按上下文（Percona 提供的 MySQL 管理工具集、导出授权语句）应为 **pt-show-grants**（Percona Toolkit 组件）`[存疑]`；原文"以 key=value 形式、逗号分割"指的是命令行参数写法，卡面已按标准 `-u`/`-p`/`-h` 给出。核心方案结论无误。

## 总结与追问预判
- 通用迁移 = **导出 CREATE USER + ALTER USER + GRANT 语句 → 目标重放**。
- 工具首选 **pt-show-grants**；重放前必审 host 与认证插件。
- 下一题：见 033（拷系统库方案对比）、011（8.0 认证插件变更）。
