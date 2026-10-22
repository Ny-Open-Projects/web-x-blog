# 82. 六大数据库存储实战: 动手部署 Neo4j 与节点、关系基础 CRUD

## 纲要

- 用 Docker 拉起 Neo4j，映射 7474（Web GUI）与 7687（Bolt 协议控制端口）
- 节点（Node）由"实例名 + 标签(Label) + 属性(Property)"构成，标签才是类型、实例名仅在本句内有效
- 三个核心 CQL 关键字：`CREATE` 建节点、`MATCH` 选择（类比 SELECT）、`WHERE` 过滤、`RETURN` 取字段
- 关系的方向性：单向、双向、无向，区别在于边上是否要分别表达两个方向的属性
- 删除错误关系：先 `MATCH` 再 `DELETE` 关系变量

## 📎 代码说明

本讲代码以**内联片段**形式呈现在正文中。课程课件仅发布第 2/3/4 章（MySQL 核心能力）的完整工程源码，本讲所属章节未随课件发布独立源码文件，故不做外部文件关联，请以正文片段为准。

## Docker 部署 Neo4j

和以往章节不同，Neo4j 是大家第一次接触的图数据库。仅用图示讲"点-边-属性"很难真正理解，因此直接用 Docker 起一个带 GUI 的实例，边练边学。

```bash
docker run -d --name neo4j-p \
  -p 7474:7474 \
  -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/123456 \
  neo4j:latest
```

- `7474`：浏览器访问的 Web GUI 端口
- `7687`：GUI 背后应用程序真正连接的 Bolt 控制端口（后续 Java 接入用）
- 默认库 `neo4j`，用户名 `neo4j`，密码 `123456`

启动后访问 `http://localhost:7474`，用上面账号 connect 即可进入 Cypher 命令行。

## 节点结构：实例名、标签、属性

用"雇员-部门"这个经典图关系做练习。先创建一个雇员节点：

```cypher
CREATE (emp:Employee {id: 1, name: 'david', salary: 1500})
```

这里极易混淆的两个概念：

- `emp` 是**实例名（node name）**，只在当前这一条语句内作为选择器生效
- `Employee`（冒号后面的）是**标签（Label）**，才是真正的类型，可以类比 Java 里的类名；而 `emp` 是它的一条 instance

创建后执行：

```cypher
MATCH (n:Employee) RETURN n LIMIT 25
```

这条语句里 `n` 同样是临时选择器，等价于"选出所有标签为 Employee 的节点并返回"。GUI 里能看到一个 `david` 节点，属性 `id=1,name=david,salary=1500`。返回结构是 JSON 对象，不是扁平的表。

再创建一个部门节点：

```cypher
CREATE (dept:Department {id: 1, name: 'accounting', location: 'shanghai'})
```

此时数据库里有两个**互无关联**的节点。

## MATCH / WHERE / RETURN 组合查询

`MATCH` 类似 SELECT 的选择器，可拼 `WHERE` 条件；`RETURN` 类比 `SELECT` 后面的字段，但返回的是对象甚至对象属性。

```cypher
-- 仅取财务部门节点
MATCH (n:Department) WHERE n.name = 'accounting' RETURN n

-- 只返回某个字段
MATCH (n:Department) WHERE n.name = 'accounting' RETURN n.id
MATCH (n:Department) WHERE n.name = 'accounting' RETURN n.location

-- 返回多个字段
MATCH (n:Department) RETURN n.id, n.name
```

多建几个部门便于练习：

```cypher
CREATE (dept2:Department {id: 2, name: 'research', location: 'beijing'})
```

`MATCH (n:Department) RETURN n` 此时能看到 research 与 accounting 两个节点。

## 关系的方向性

节点会建了，接下来要搞定"关系"。关系分三种形态，关键区别在于**边上的属性是否要分别表达两个方向**：

```mermaid
flowchart LR
    subgraph 单向
        A1[(Employee)] -->|belong| B1[(Department)]
    end
    subgraph 双向
        A2[(Employee)] <->|belong| B2[(Department)]
    end
    subgraph 无向
        A3[(Employee)] ---|belong| B3[(Department)]
    end
```

- **单向**：Employee 指向 Department（属于某部门），反向语义不同
- **双向**：双向边，两边各自可挂独立的属性（两者互相隔离，无关联）
- **无向**：只有一条边，不分谁指向谁，二者共用；要不要区分方向取决于边上属性是否要分别表达

这一节先把节点的 `CREATE / MATCH / WHERE / RETURN` 练熟，下面再正式建立关系并做增删改查。

## 技术点总结

- 7474 是 GUI、7687 是 Bolt 控制端口，二者都要映射出来
- 节点 = 实例名(临时) + Label(类型) + Property；Label 才是真正的类型
- `CREATE` 建、`MATCH` 选、`WHERE` 过滤、`RETURN` 取字段，是四个最基础的 CQL 关键字
- 关系的单向/双向/无向，核心看边属性是否要分方向表达


