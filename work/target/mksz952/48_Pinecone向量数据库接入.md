# 48. Pinecone 向量数据库接入

## 纲要

- **为何上 Pinecone**：内存向量库重启丢数据，生产需持久化；Pinecone 云原生向量库，注册送 2GB 免费空间
- **核心概念**：`database` 下建 `index`（类比数据库），index 下可建 `namespace`（命名空间，缩小检索范围）
- **score**：相似度得分，越高越相似（如 0.9998 近完全匹配）；底层用余弦相似度等算法
- **接入两步**：① 引 `langchain4j-pinecone` + 序列化坐标（漏序列化会 `NoSuchMethodError`）② 构造 `PineconeEmbeddingStore`（APIKey/index/namespace/服务器区域）
- **维度对齐铁律**：index 的向量维度必须 == EmbeddingModel 输出维度，否则异常

> 代码按课程口径重构示意（外部课件代码卷未挂载）。本卡覆盖 8-13/8-14。

## 一、控制台建索引

```mermaid
flowchart LR
    A[注册 Pinecone] --> B[建 index 如 myindex]
    B --> C[选向量模型/维度]
    C --> D[建 namespace: default]
    D --> E[Upsert 记录(ID+文本)]
    E --> F[按 ID/向量检索看 score]
```

- `score`：检索得分，越高越相似（余弦相似度得出）。
- 索引默认数量有限（如 5 个），测试时注意清理。

## 二、依赖与配置

```xml
<!-- pom: langchain4j-pinecone + 序列化坐标(防 NoSuchMethodError) -->
```

```java
// 构造向量库对象
EmbeddingStore store = PineconeEmbeddingStore.builder()
    .apiKey(System.getenv("PINECONE_API_KEY"))
    .index("myindex")
    .namespace("default")
    .serverSide("亚马逊服务器")
    .serverRegion("区域")
    .build();
// 维度必须等于 EmbeddingModel.dimension()，从百炼模型取后填入
```

## 三、写入向量数据

```java
Embedding embedding = embeddingModel.embed("我喜欢打乒乓球").content(); // 百炼向量化
store.add(embedding, "我喜欢打乒乓球");   // 向量 + 原始文本一并写入
// 回 Pinecone 控制台刷新，可见新 index 与向量记录
```

## 四、维度对齐

```
Pinecone index 维度 = embeddingModel.dimension()
```

建索引时把百炼模型维度（如 1024）填进索引；不一致会写入异常。

## 五、FAQ

**Q1：为什么不用内存向量库上生产？**
重启/宕机数据全丢；Pinecone 持久化且免运维。

**Q2：namespace 干嘛用？**
隔离不同业务数据，缩小检索范围、提升效率。

**Q3：漏序列化坐标报什么错？**
`NoSuchMethodError`；补上序列化依赖即可。

## 六、面试高频问答

**1. Pinecone 的 index/namespace 类比？**
index ≈ 数据库，namespace ≈ 库内分区/表，用于隔离与缩窄检索。

**2. 维度为何必须对齐？**
向量空间不一致，相似度计算无意义，写入即报错。

**3. score 含义？**
相似度得分（常由余弦相似度得出），越高代表查询与存储向量越相近。

## 七、ops 提示（接入红线）

> **序列化坐标必带**：`langchain4j-pinecone` 不配序列化依赖会 `NoSuchMethodError`，一次配齐。
>
> **维度先取后填**：用 `embeddingModel.dimension()` 取真实维度再建索引，别手填猜值。
>
> **索引数量管控**：免费层索引数有限，测试后清理，避免建满报错。

