# 25. 图数据库 Neo4j 与 Cypher 实战

## 纲要

- **两种主流图数据库**：① **Neo4j**（高性能原生图数据库，支持 Cypher，适合复杂关系数据、中小规模）；② **NebulaGraph**（分布式，原生支持水平扩展，可处理千亿节点/万亿边、毫秒延迟，适合超大规模高并发）。
- **类比记忆**：Neo4j ≈ Chroma（轻量易用）、NebulaGraph ≈ Milvus（大规模分布式）——与向量库选型思路一致。
- **Neo4j 部署**：Java 系，需 JDK17+；下社区版解压即用；`neo4j start/stop` 启停；可视化界面默认端口 **7474**；数据服务默认端口 **7687**。
- **查询语言 Cypher（声明式，易上手）**：核心动词 `CREATE`（建节点/关系）、`MATCH ... RETURN`（查并返）、`MERGE`（有则合并无则创建）。
- **节点语法**：`(:标签 {属性})`，如 `CREATE (p:Person {name:'Alice'})`。
- **关系语法**：`-[r:关系类型 {属性}]->`，箭头表方向，如 `(:Person)-[:LIKE]->(:Movie)`。
- **约束与索引**：约束保数据质量（如 `title` 唯一）；索引建在节点属性上提速查询（如按 `release` 查）。
- **多跳查询**：用 `*n` 表示跳数（1=直接连接，2=隔一跳），配合去重，可查「某人的直接/间接关联全数据」。
- 本章按课程口径重构；代码为知识重构（外部代码卷未挂载），演示基于 Python `py2neo`；产品名已规范（Neo4j / NebulaGraph / Cypher / JDK / Chroma / Milvus）。

## 一、Neo4j vs NebulaGraph 对比

| 维度 | Neo4j | NebulaGraph |
| --- | --- | --- |
| 定位 | 高性能原生图数据库，Cypher 易上手 | 分布式图数据库，原生水平扩展 |
| 分布式 | 后期靠集群模式扩展 | 一开始就分布式，水平扩展应对高并发 |
| 事务 | 支持 | 支持 |
| 查询语言 | Cypher（声明式，易学） | GQL（过程式，类 SQL） |
| 适用规模 | 千万级以下较好 | 千亿节点/万亿边、毫秒延迟，超大规模首选 |
| 工具 | 丰富图形界面 + 可视化 | 特定类型图查询/导入出色 |

**结论**：数据量不大（千万以下）→ Neo4j 性价比高、易上手；超大规模+高并发 → NebulaGraph 首选。本章用 Neo4j 讲解。

## 二、Neo4j 安装与部署

- **依赖**：Java 系，需安装 **JDK 17+**（OpenJDK 或 Oracle JDK 均可）。
- **获取**：下载**社区版** Neo4j（如 5.23），解压即用。
- **启停**：`neo4j start` 启动、`neo4j stop` 停止。
- **可视化**：浏览器访问默认 **7474** 端口，提供图/文本/表格/代码多种展示；可执行 Cypher 并查看节点与关系。
- **数据端口**：程序连接默认 **7687**。

## 三、Cypher 核心语法

### 1. 创建节点
```
CREATE (p:Person {name:'Alice'})      // 变量p，标签Person，属性name
CREATE (:Movie {title:'黑客帝国'})     // 电影节点带title属性
```

### 2. 创建关系（箭头表方向，关系可带属性）
```
CREATE (:Person {name:'Alice'})-[:LIKE {since:2020, rating:5}]->(:Movie {title:'黑客帝国'})
```

### 3. 约束与索引
```
CREATE CONSTRAINT FOR (m:Movie) REQUIRE m.title IS UNIQUE;   // title唯一，防重复
CREATE INDEX FOR (m:Movie) ON (m.release);                   // 按release建索引提速
```

### 4. 查询 MATCH ... RETURN
```
MATCH (p:Person {name:'汤姆汉克斯'}) RETURN p;                       // 简单查
MATCH (m:Movie) WHERE m.release>=1990 AND m.release<=2000 RETURN m.title;
```

### 5. 带关系的复杂查询
```
// 汤姆汉克斯参演的所有电影
MATCH (p:Person {name:'汤姆汉克斯'})-[:ACTED_IN]->(m:Movie) RETURN p, m;

// 与汤姆汉克斯共同参演过电影的演员
MATCH (p:Person {name:'汤姆汉克斯'})-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(co) RETURN co.name;

// 与某电影有关的所有人及其关系角色
MATCH (p:Person)-[r]-(m:Movie {title:'Cloud'}) RETURN p.name, type(r);
```

### 6. 多跳查询 `*n`
```
// 查 kevin 的直接(1跳)与间接(2跳)所有关联数据，去重
MATCH (p:Person {name:'kevin'})-[*1..2]-(x) RETURN p, x;
```
`*n` 表示关系跳数：1=直接连接，2=隔一跳，以此类推。

## 四、实战：用 py2neo 连接与操作

课程用 Python `py2neo` 操作 Neo4j：
- 安装：`pip install py2neo`
- 导入：`from py2neo import Graph,Node,Relationship`
- 连接：`Graph("bolt://host:7687",auth=("user","password"),name="db名")`
- 建节点：`Node(label,属性)`；入库用 `graph.merge(node,"label","key")`——按 key 判重，有则合并、无则创建。
- 建关系：`Relationship(节点A,"关系名",节点B,属性)`。

> `MERGE` 是图谱入库关键：避免重复节点，保证图谱干净。

## 五、FAQ

**Q1：Neo4j 和 NebulaGraph 怎么选？**
千万级以下、要易上手与可视化 → Neo4j；超大规模、高并发、要分布式 → NebulaGraph。

**Q2：Cypher 里 MATCH 和 RETURN 必须一起吗？**
MATCH 负责匹配/查询，RETURN 负责把结果返回；通常配对使用。

**Q3：MERGE 和 CREATE 区别？**
CREATE 无条件新建（可能重复）；MERGE 按 key 判重，有则合并无则创建，入库首选。

**Q4：多跳查询 `*2` 是什么？**
表示沿关系走 2 跳（隔一个节点），配合去重可捞取实体的直接+间接关联全数据。

## 六、面试高频问答

**1. Neo4j 与 NebulaGraph 核心差异？**
Neo4j 轻量易用、Cypher 声明式、适合中小规模；NebulaGraph 分布式原生、适合超大规模高并发。

**2. Cypher 创建关系怎么写？**
`(a:标签)-[:关系类型 {属性}]->(b:标签)`，箭头表示方向。

**3. 为什么图谱入库要用 MERGE？**
按 key 判重，有则合并无则创建，避免重复节点、保证图谱质量。

**4. 图数据库类比向量库怎么记？**
Neo4j≈Chroma（轻量）、NebulaGraph≈Milvus（大规模分布式）。

## 七、ops 提示（增效）

> **中小规模果断 Neo4j**：社区版免费、Cypher 半天可上手、可视化界面排查关系极方便，是原型与中小图谱首选。
>
> **大关系务必建索引**：按查询频繁的属性（公司名、事件类型）建索引，否则 MATCH 全图扫描会爆慢。
>
> **约束保质量**：对唯一性字段（如 title）加约束，从根源防脏数据重复节点。

