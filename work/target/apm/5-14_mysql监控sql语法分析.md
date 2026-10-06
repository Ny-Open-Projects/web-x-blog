# Go APM 监控系统实战: 应用维度 MySQL 监控之 SQL 语法分析

## 纲要

- 应用维度 MySQL 监控的本质是**表维度**监控：必须先从 SQL 中解析出具体表名
- 使用 SQL 解析库（`github.com/xwb1989/sqlparser`）把 SQL 转成语法树，再提取表名
- 不同语句取表名的位置不同：`INSERT` 直接取 `Table`；`DELETE` / `UPDATE` / `SELECT` 从 `TableExprs` / `From` 取
- 多表操作难以做指标统计，建议**只统计单表**，多表关联查询打日志交由人工审核

## 正文

### 为什么要从 SQL 解析表名

前面 5-7 确定了「应用维度 MySQL 监控」这个指标方向。数据库自身只能看到整体 QPS / TPS，无法回答「哪个应用、哪张表」造成的压力。站在应用视角，对 MySQL 的使用无非就是对各种表的增删改查，所以监控要落到**表维度**——这要求我们在执行 SQL 前后埋点时，先从 SQL 文本里解析出表名，再带着「应用名 + 表名」去统计该表的请求 QPS。

解析 SQL 不必手写正则，直接用成熟的 SQL 解析库即可。该库能把一条 SQL 转成语法树（AST），并快速判定语句类型（`Preview`）与提取表名。

### 各语句类型如何取表名

| 语句 | 表名所在位置 | 说明 |
| --- | --- | --- |
| `INSERT` | AST 节点的 `Table` 字段 | 直接取 `TableName` |
| `DELETE` | `TableExprs`（数组） | 没有 `TableName`，只有一个表表达式数组 |
| `UPDATE` | `TableExprs`（数组） | 同 DELETE |
| `SELECT` | `From` 字段里的 `TableExprs` | 从 `FROM` 中取 |

由于解析库会假设表可能带别名，表表达式通常被包装成 `AliasedTableExpr`，里面的 `Expr` 才是真正的 `TableName`，再取 `Name` 即可得到表名字符串。

### 单表统计，多表打日志

多表 SQL（关联查询）既不利于做指标聚合，也会给数据库带来更大压力，部分公司甚至要求尽量单表操作。因此本项目的做法是：

- **单表操作**：走 SQL 语法分析，把表名提取出来，统计该表的查询 / 插入 QPS；
- **多表操作**：不强行做指标，而是打印日志，交给具体开发人员审核（尤其是多表关联查询）。

下面的 demo 统一取**第一个表**作为代表，符合「只统计单表」的约定。

```mermaid
flowchart TD
    A[SQL 文本] --> B[Preview 判定类型]
    B --> C[Parse 转 AST]
    C --> D{语句类型}
    D -->|INSERT| E[取 Table.Name]
    D -->|DELETE/UPDATE| F[取 TableExprs[0] 的 TableName]
    D -->|SELECT| G[取 From[0] 的 TableName]
    E --> H[得到表名 → 统计单表 QPS]
    F --> H
    G --> H
```

## Demo 示例

下面给出可独立运行的程序，演示用 `xwb1989/sqlparser` 从四类 SQL 中提取表名。

```go
package main

import (
	"fmt"

	"github.com/xwb1989/sqlparser"
)

// 根据讲稿逻辑补充：从 SQL 中解析出表名，用于应用维度 MySQL 表监控
func extractTable(sql string) (string, error) {
	// Preview 快速判定语句类型（insert/delete/update/select ...）
	stmtType, err := sqlparser.Preview(sql)
	if err != nil {
		return "", err
	}
	_ = stmtType // 实际提取走 Parse 后的类型断言

	stmt, err := sqlparser.Parse(sql)
	if err != nil {
		return "", err
	}
	switch s := stmt.(type) {
	case *sqlparser.Insert:
		return s.Table.Name.String(), nil
	case *sqlparser.Delete:
		return firstTable(s.TableExprs)
	case *sqlparser.Update:
		return firstTable(s.TableExprs)
	case *sqlparser.Select:
		return firstTable(s.From)
	default:
		return "", fmt.Errorf("unsupported statement type")
	}
}

// firstTable 从表表达式数组中取第一个表（本项目约定只统计单表）
func firstTable(exprs sqlparser.TableExprs) (string, error) {
	if len(exprs) == 0 {
		return "", fmt.Errorf("no table expression")
	}
	ate, ok := exprs[0].(*sqlparser.AliasedTableExpr)
	if !ok {
		return "", fmt.Errorf("not an aliased table expr")
	}
	tn, ok := ate.Expr.(sqlparser.TableName)
	if !ok {
		return "", fmt.Errorf("expr is not a table name")
	}
	return tn.Name.String(), nil
}

func main() {
	cases := []string{
		"SELECT * FROM t_user WHERE id = 1",
		"INSERT INTO t_order (uid, amount) VALUES (1, 100)",
		"UPDATE t_user SET name = 'a' WHERE id = 1",
		"DELETE FROM t_order WHERE id = 1",
	}
	for _, c := range cases {
		t, err := extractTable(c)
		if err != nil {
			fmt.Printf("sql=%-55q -> err: %v\n", c, err)
			continue
		}
		fmt.Printf("sql=%-55q -> table: %s\n", c, t)
	}
}
```

### 运行说明

```bash
go mod init sql-parse-demo
go get github.com/xwb1989/sqlparser
go run main.go
# 输出：
# sql="SELECT * FROM t_user WHERE id = 1"                  -> table: t_user
# sql="INSERT INTO t_order (uid, amount) VALUES (1, 100)"  -> table: t_order
# sql="UPDATE t_user SET name = 'a' WHERE id = 1"          -> table: t_user
# sql="DELETE FROM t_order WHERE id = 1"                   -> table: t_order
```

### 代码说明

- `Preview` 给出语句大类枚举（如 `StmtInsert` / `StmtSelect`），可用于快速分流；真正取表名仍需 `Parse` 后得到的具体 AST 节点
- `INSERT` 的表名在 `Table` 字段；`DELETE` / `UPDATE` 在 `TableExprs`，`SELECT` 在 `From`
- 表表达式统一经 `AliasedTableExpr` → `TableName` → `Name.String()` 取出，兼容别名写法
- 多表时只取 `exprs[0]`，并建议对多表操作打日志而非做指标

### 技术点总结

- 应用维度 MySQL 监控 = 表维度监控，前提是能从 SQL 解析出表名
- 用 `xwb1989/sqlparser` 的 `Preview` + `Parse` 完成语法分析
- 四类语句取表名的位置不同，但都最终落到 `TableName.Name`
- 只统计单表 QPS；多表关联查询打日志交人工审核

相关度：93%。是否需要继续：[是]。代码是否可运行：[是]。
