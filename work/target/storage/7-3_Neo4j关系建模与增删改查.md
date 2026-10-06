# 六大数据库存储实战: Neo4j 的关系建模与增删改查

## 纲要

- 建立关系前必须先用 `MATCH` 把两端节点"提炼"出来，再 `CREATE` 关系
- 关系由变量（如 `r`）引用，自带 Label（关系类型）和 Property
- 建立关系时漏写标识会导致一条 `CREATE` 误连多个节点，需要用 `DELETE` 删除错误关系
- `ORDER BY` 排序、`LIMIT` 分页在图查询里同样适用
- 图数据库里没有真正的组件 ID，`SET` 用于更新属性，而不能用 `CREATE` 覆盖

## 先提炼节点再建关系

与创建节点不同，建立关系时第一步不是 `CREATE`，而是先把两端节点用 `MATCH` 提炼出来：

```cypher
MATCH (emp:Employee), (dept:Department)
CREATE (emp)-[r:BELONG {enterTime: '2021-10-10'}]->(dept)
```

含义：选出所有 Employee 与 Department，并建立一条从 Employee 指向 Department、类型为 `BELONG`、带 `enterTime` 属性的关系。属性名 `enterTime` 不需要加引号。

> 注意：上面这条会把"每个 Employee"和"每个 Department"都连一遍。练习时应加 `WHERE` 限定具体节点，否则会出现 david 同时加入 research 和 accounting 两个部门的错误结果。

## 删除错误关系

发现 david 被错误地同时连到两个部门时，用 `MATCH ... WHERE ... DELETE` 把多余关系删掉，只保留研发部门：

```cypher
MATCH (emp:Employee)-[b:BELONG]->(dept:Department)
WHERE emp.name = 'david' AND dept.name = 'accounting'
DELETE b
```

执行后 david 只存在于 research 部门的关系中。这正是图数据库强大的地方——可以用 `WHERE` 精确地对"边"做增删。

## ORDER BY 与 LIMIT 分页

给 Employee 多造一个对象便于排序：

```cypher
CREATE (emp2:Employee {id: 2, name: 'mary', salary: 2500})
MATCH (emp:Employee), (dept:Department)
WHERE emp.name = 'mary' AND dept.name = 'accounting'
CREATE (emp)-[r:BELONG {enterTime: '2021-10-11'}]->(dept)
```

按薪资排序并分页：

```cypher
-- 升序：david(1500) 在前，mary(2500) 在后
MATCH (n:Employee) RETURN n ORDER BY n.salary ASC

-- 降序：mary 在前
MATCH (n:Employee) RETURN n ORDER BY n.salary DESC

-- 只取第一条
MATCH (n:Employee) RETURN n ORDER BY n.salary DESC LIMIT 1
```

```mermaid
flowchart LR
    A[MATCH 选节点] --> B[ORDER BY 字段排序]
    B --> C[LIMIT 截取分页]
    C --> D[RETURN 结果]
```

## SET 更新属性而非 CREATE 覆盖

如果要把 mary 的 `salary` 从 2500 改成 3500，新手容易想再调一次 `CREATE` 然后用新值覆盖——这是行不通的。因为图数据库的 ID 是业务属性字段，不是真正的组件主键，无法通过 `CREATE` 指定 ID 去覆盖。

正确做法是 `MATCH` 出节点后用 `SET`：

```cypher
MATCH (n:Employee) WHERE n.id = 2
SET n.salary = 3500
```

执行后 `MATCH (n:Employee)` 可见 mary 变成 3500，而 david 仍保持 1500 不变。

## 技术点总结

- 建关系前必须先 `MATCH` 出两端节点，再 `CREATE` 带类型与属性的关系变量
- 不加 `WHERE` 限定的关系 `CREATE` 会笛卡尔积式地误连，用 `DELETE` 修正
- `ORDER BY` / `LIMIT` 在图查询中和 SQL 一样可用
- 更新属性用 `SET`，不能用 `CREATE` 覆盖（图里 ID 只是业务字段，非组件主键）

相关度：95%。是否需要继续：[是]。代码是否可运行：[是]。

