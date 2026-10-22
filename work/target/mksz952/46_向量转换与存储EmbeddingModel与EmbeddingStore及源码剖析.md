# 46. 向量转换与存储：EmbeddingModel 与 EmbeddingStore 及源码剖析

## 纲要

- **Embedding**：把文本/图像转成保留关键特征的向量，存入向量库；`EmbeddingStore` = 嵌入存储
- **LangChain4j 支持**：默认 `InMemoryEmbeddingStore`（内存，重启丢）；另支持 ClickHouse/Oracle/Pinecone 等
- **ingest 三动作**：`EmbeddingStore.ingest(documents)` 内部 = 文档分割 → 文本向量化 → 原始片段+向量入库
- **内置向量模型**：LangChain4j 内置轻量 Embedding 模型，入门方便；生产建议接百炼等大厂模型
- **源码剖析**：`ingest` 用递归 `DocumentSplitter`（默认 ≤300 token）→ 调 `EmbeddingModel` 向量化（返回向量+tokenCount）→ `addAll` 写 `InMemoryEmbeddingStore`（底层 CopyOnWriteArrayList）

> 代码按课程口径重构示意（外部课件代码卷未挂载）。本卡覆盖 8-8/8-9，是 RAG 索引落库的核心。

## 一、依赖与最小 Demo

```java
// 引两个坐标: langchain4j-easy-rag(提供 ingest 等) + DJL 相关(解决版本兼容报错)
// 加载 TXT → 内存向量库 → ingest
Document doc = FileSystemDocumentLoader.loadDocument("/data/kb.txt");
EmbeddingStore store = new InMemoryEmbeddingStore();
EmbeddingStore.ingest(doc, store);   // 一步完成 分割+向量化+入库
System.out.println(store);            // 查看向量化结果
```

## 二、ingest 内部三动作

```mermaid
flowchart TD
    A[ingest(documents, store)] --> B[DocumentSplitter 分割]
    B --> C[EmbeddingModel 向量化]
    C --> D[addAll: 原始片段+向量 入库]
```

源码（`EmbeddingStore.ingest`）实际调用：

1. **分割**：`documentSplitter` 默认 `DocumentSplitters.recursive(300)`（≤300 token）。
2. **向量化**：调内置 `EmbeddingModel.embed(segments)`，返回每段向量与 `tokenCount`。
3. **存储**：`store.addAll(embeddings,segments)` → `InMemoryEmbeddingStore` 底层用 `CopyOnWriteArrayList` 存。

## 三、EmbeddingStore 支持矩阵

| 存储 | 说明 |
|---|---|
| InMemoryEmbeddingStore | 默认，内存级，**生产不建议**（重启丢） |
| ClickHouse / Oracle | 关系型/分析型向量支持 |
| Pinecone | 云原生向量库，前述实战选用 |

## 四、内置模型的局限

LangChain4j 内置 Embedding 模型功能/稳定性弱于大厂服务。生产推荐接阿里百炼等（维度更高、语言支持更全、有容错）。

## 五、FAQ

**Q1：ingest 一步到位还是手动三步？**
Demo 用 `ingest` 一步；要自定义分割器/模型时用 `EmbeddingStore.builder()` + `addAll` 手动控制。

**Q2：为什么内存向量库不能上生产？**
重启/宕机数据全丢；必须换持久化向量库。

**Q3：内置向量模型够用吗？**
入门够；生产在精度、维度、稳定性上不如百炼等厂商模型。

## 六、面试高频问答

**1. EmbeddingStore.ingest 做了什么？**
三动作：递归分割（默认 ≤300 token）→ 调 EmbeddingModel 向量化 → addAll 把片段与向量存入向量库。

**2. 内存向量库底层结构？**
`InMemoryEmbeddingStore` 用 `CopyOnWriteArrayList` 存向量与文本。

**3. 为什么生产不用内置向量模型？**
精度/维度/稳定性不及大厂服务，且不可控。

## 七、ops 提示（存储红线）

> **内存向量库仅开发用**：`InMemoryEmbeddingStore` 重启即失，生产换 Pinecone/PG 向量等。
>
> **DJL 坐标别忘了**：用 `easy-rag` 时需补 DJL 相关坐标，否则报版本兼容错。
>
> **ingest 前定分割器**：要控粒度/重叠/正则，先 `DocumentSplitters.xxx` 再手动 `addAll`，别只依赖默认。

