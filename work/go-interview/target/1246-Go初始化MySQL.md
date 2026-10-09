# 1246 Go 初始化 MySQL：驱动必须显式引入，连接池三项要设

> 分类：数据库 / Go 工程 | 难度：L3 | 题型：排错题 | 频率：高 | 关键词：**go-sql-driver、init 注册、连接池、MaxOpenConns、预编译、DSN**

> 原文锚点：第 44~62 段「对 mysql 的一些默认设置，包括最大的连接数、最大的空闲连接数、连接最大的存活时间，最后一个参数是我们开启了 SQL 的预编译…拼接我们 URL 的连接串…把这些设置完成之后我们可以设置一些回调函数，这些函数会在执行 create、query、update 操作的时候执行回调，打印出具体的 SQL 语句…我们需要格外注意一点，就是我们需要手动引入 go-sql-driver/mysql，虽然这里我们不需要使用这个库，但是我们需要引入这个包，因为这个包里面的 init 函数会做一些初始化的动作」

## 一句话总述
Go 初始化 MySQL 的三个必做项：**显式 import 驱动包**（靠其 `init` 完成驱动注册）、**设置连接池三参数**（最大连接数、最大空闲连接数、连接最大存活时间）、**开启预编译**；可再加执行回调打印 SQL 便于排查。

## 面试官视角
P6 能写出 `sql.Open("mysql", dsn)`；P7 必须讲清**「为什么不用这个包还要 import」**——驱动的 `init` 函数会把自己注册到 `database/sql`，用 `_` 空导入是 Go 的标准做法；以及连接池不配置的后果（连接耗尽或大量 TIME_WAIT）。

## 主问答
**Q（面试官原话）：** Go 连 MySQL，为什么 import 了一个从没调用的 mysql 包？

1. **必须手动引入驱动**：使用 MySQL 时**必须引入 go-sql-driver/mysql** `[源码]`。
2. **原因**：虽然代码中不直接使用该库，但其 **`init` 函数会执行初始化动作**（把驱动注册进 `database/sql`） `[源码]`。
3. **写法**：用空白导入 `_ "github.com/go-sql-driver/mysql"` 即可 `[经验]`。
4. **参数校验**：初始化时 **clientName 与用户名长度不能为零**，否则直接返回错误 `[源码]`。
5. **连接池三项**：设置**最大连接数**、**最大空闲连接数**、**连接最大存活时间** `[源码]`。
6. **预编译**：默认**开启 SQL 预编译**，提升重复执行效率并降低注入风险 `[源码]`。
7. **DSN 拼接**：拼接数据库连接串后传给连接函数，得到数据库对象 `[源码]`。
8. **执行回调**：注册回调函数，在 **create / query / update** 时触发，用于**打印具体 SQL 语句** `[源码]`。
9. **多客户端管理**：实例化后的客户端以 **clientName 为 key 存入 map**，便于按名获取 `[源码]`。

## 追问链
| 层级 | 追问 | 答不出停在哪档 |
|---|---|---|
| L1 | 驱动包为什么要 import？ | 答不出 init 注册驱动 |
| L2 | 空白导入怎么写？ | 答不出下划线导入 |
| L3 | 连接池要设哪三项？ | 答不出最大/空闲/存活时间 |
| L4 | 回调有什么用？ | 答不出打印 SQL 排查 |
| L5 | 多客户端怎么管理？ | 答不出按名字存 map |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 1.x 全版本 | database/sql 需驱动注册 | 必须空白导入驱动 |
| go-sql-driver v1 | DSN 支持多参数 | 注意 parseTime/loc 等常用参数 |
| 所有版本 | 连接池默认偏保守 | 高并发必须显式调优 |
| 所有版本 | 预编译 | 开启可提升重复执行性能 |

## 关键代码
```go
package main

import (
	"database/sql"
	"log"
	"time"

	// 必须显式引入：该包的 init 函数会把 mysql 驱动注册进 database/sql
	// 代码中并不直接调用它，故使用空白导入
	_ "github.com/go-sql-driver/mysql"
)

func newDB(dsn string, maxOpen, maxIdle int, maxLife time.Duration) (*sql.DB, error) {
	db, err := sql.Open("mysql", dsn) // 注意：Open 只校验参数，不建立真实连接
	if err != nil {
		return nil, err
	}

	// 连接池三项：最大连接数 / 最大空闲连接数 / 连接最大存活时间
	db.SetMaxOpenConns(maxOpen)
	db.SetMaxIdleConns(maxIdle)
	db.SetConnMaxLifetime(maxLife)

	// 真正验证连通性
	if err := db.Ping(); err != nil {
		return nil, err
	}
	return db, nil
}

func main() {
	log.SetFlags(log.Ldate | log.Lshortfile) // 打印日期与文件名，便于定位

	db, err := newDB("user:pass@tcp(127.0.0.1:3306)/test?parseTime=true",
		100, 20, 30*time.Minute)
	if err != nil {
		log.Println("init db failed:", err)
		return
	}
	defer db.Close()
}
```

## 总结与追问预判
**「不用还要 import」的答案是 init 注册**，这是 Go `database/sql` 插件式设计的标准套路。追问常是「`sql.Open` 之后为什么还要 `Ping`」——因为 `Open` 只做参数校验、**不建立真实连接**，连接是惰性建立的。遍历全表的查询写法见同批 1246-go-count-total。

## ⚠️ 原文纠错
1. 事实核校：必须引入驱动且依赖其 init、初始化参数校验、连接池三项设置、开启预编译、DSN 拼接、执行回调打印 SQL、按 clientName 存 map——均与 Go 数据库编程实践一致 `[经验]`。
2. 补充：原文提到「开启 SQL 预编译」，在 Go 标准库中对应 **预处理语句（Prepare）** 的使用；真正生效需要用 `db.Prepare` 或带参数的 `Query/Exec`，而非仅配置项 `[经验]`。
3. 崩坏词归一：源码将驱动、预编译、连接池、回调函数等术语音译为多组崩坏词，本卡统一为规范术语 `[经验]`。
