# 11-9 BI报表问答Agent总结梳理

## 【学习目标】

学完本节，应当能够：

- 对着进阶版流程图，把「RAG 生成 → 评估 → 执行 → 邮件」全链路从头到尾串一遍，说清每个节点的职责与状态流转；
- 讲清两处 RAG 优化的动机与做法：按数字编号标题的文本切割、基于 `QueryTransformer` 的查询重写；
- 在 Redis 与 Milvus 之间给出向量库选型理由；
- 向面试官描述一个「带评估闭环的 RAG + Agent」项目全貌，并指出仍待改进的点。

## 【正文】

这节课把「智能 BI 报表问答系统」整体收个尾。项目开发到这就告一段落了，我们对照进阶版流程图，把整条链路从头到尾串一遍，并补几个优化点和课后作业。

### 一、全链路回顾

Agent 被触发时，起点是用户的一句自然语言查询。进入第一个节点 **RAG 检索生成 SQL**：这里会调用大模型，并走 RAG 召回，从向量数据库里把私有知识库中的文档内容检索出来，作为提示词的一部分告诉大模型，让它基于我们私有知识库的表结构设计和表间对应关系，生成对应的查询 SQL。

在该节点里，我们也通过提示词优化保证了「只生成查询 SQL，不会生成 `DELETE`、`UPDATE`、`INSERT`、`DROP` 这些写操作」；而评估节点又进一步把安全性加固了一层：对 SQL 的准确性和安全性做评估。

如果评估通过，就进入下一个节点 **执行 SQL 并动态生成 Excel 模板**：通过 `JdbcTemplate` 限制只执行查询类 SQL，并动态生成 Excel 模板；再往下到 **发送邮件** 节点，给具体用户发送带附件或不带附件的邮件。

全链路用 mermaid 画出来：

```mermaid
flowchart TD
    S([START]) --> G["RAG 检索生成 SQL<br/>GenSQLNode"]
    G --> E{"SQL 评估节点<br/>EvaluateNode"}
    E -- "pass" --> X["执行 SQL 并生成 Excel<br/>JdbcTemplate 限查询"]
    E -- "fail 且未超限" -->|回环| G
    E -- "loop 超限" --> Z([END])
    X --> M["发送邮件<br/>带附件 / 无内容提示"] --> Z
```

各节点职责与关键状态归纳如下：

| 节点 | 输入状态 | 输出状态 | 核心职责 |
|---|---|---|---|
| GenSQLNode | `userInput` | `genSQL` | RAG 召回表结构，生成查询 SQL，拒杀写操作 |
| EvaluateNode | `genSQL`、`loop` | `evaluateResult`、`loop+1` | 评估准确性与安全性，累加循环次数 |
| 条件边 EvaluateEdge | `evaluateResult`、`loop` | 路由决策 | 超限 → END，fail → 回环，pass → 放行 |
| ExecSQLAndCreateExcelNode | `genSQL` | `keyExcelFile` | JdbcTemplate 限查询，动态生成 Excel |
| SendEmailNode | `keyExcelFile` | - | 有附件发附件，无附件发提示邮件 |

一个值得改进的点：发送邮件的 `to`（收件人）现在写死了，实际应该取 `userId`，比如你们公司内部用企业微信，员工的公众号（账号）是可以拿到的，完全可以通过员工账号做消息推送。具体按你们公司的实际情况来接。该改进点和 11-8 节的对话隔离是同一脉络的，既然 `threadId` 已经按 `userId` 隔离，下游副作用（邮件、消息）也应该按 `userId` 寻址，链路才是完整的。

### 二、评估失败与循环限制

如果评估节点判 SQL 不通过，条件边会把整个工作流拉回上一个节点（RAG 检索生成 SQL），重新生成 SQL，再进入评估节点。但这里有个隐患：可能生成的 SQL 一直不对，陷入「评估-生成-评估」的无限循环。所以必须加循环限制：当达到设定的循环上限，就不再循环，而是直接由条件边把工作流连到结束节点。

这里留了个作业：把循环次数放到 **Nacos** 里，支持动态更新。因为一开始你未必知道循环几次合适，太大浪费性能，太小又可能生成不出准确的 SQL。我个人觉得执行 3 到 5 次比较合适，没有固定规范，需要在实际测试里微调。

值得补充的是该作业的工程含义：上限放配置中心之后，「调循环次数」从一次发版变成一次配置推送，出了问题可以分钟级回滚；这也是 11-6 节「重试预算」思想的落地方式，预算值本身也应该是可运营的参数。

### 三、提示词与 Temperature

整个项目的提示词，沿用了之前**智能库存调拨优化系统**的编写风格，一步步把不同节点的提示词代码写出来。建议大家自己手动敲一遍，才能真正体会什么样的提示词算好提示词。

另外就是大模型的 **Temperature（温度）** 参数：根据业务是否需要模型有一定创造性来决定怎么调（BI 系统表结构确定、求稳定，温度调低；库存预测求创造性，可保持较高温度）。11-8 节已把温度压到 `0.2` 并验证过：多次刷新生成的 SQL 几乎无差异。

### 四、RAG 优化：文本切割

RAG 部分我们重点优化了「文本切割」。程序员提供的是数据库表结构和表间关系的文档，所以我们可以限定文档模板，用**数字编号作为标题**来拆分，保证一个数字标题下一定是一段完整的表结构定义，不会把不同表的结构切散，每个块里都是完整的一张表结构。

为什么表结构文档必须整表一块？因为 SQL 的正确性依赖「表间关系」这一跨段信息：`fact_sales` 的字段定义在一个编号下，`dim_date` 的定义在另一个编号下，而 `JOIN ... ON s.date_id = d.date_id` 的关系描述可能横跨两段。一旦按固定长度机械切分，JOIN 关系被切到两个块里，召回时任一块都信息不全，模型只能「猜」 join 条件，错误 SQL 就这样产生。**切割策略必须尊重文档的语义边界，而不是只尊重字节数。**

课程里还扩展了一个比较通用的**中文文本切割器**。它的原理是按句子切分，但中文要靠中文标点（句号、冒号、问号、分号、括号等）来断句；而且你可以自己指定块大小（`chunkSize`）和块之间的重叠大小（`chunkOverlap`）。两个切割器通用的核心，其实都是通过**正则表达式**来匹配切分：

```java
public class ChineseTextSplitter extends TextSplitter {
    private static final Pattern SENTENCE_SPLIT_PATTERN = Pattern.compile("[。！？]");
    private final int chunkSize;
    private final int chunkOverlap;
    // ... 其他代码 ...
    protected List<String> splitText(String text) {
        List<String> segments = new ArrayList<>();
        if (text == null || text.isBlank()) {
            return segments;
        }
        String[] sentences = SENTENCE_SPLIT_PATTERN.split(text);
        StringBuilder currentChunk = new StringBuilder();
        // ... 其他代码 ...
    }
}
```

如实说明这段代码与正文的出入：正文说断句标点包含「句号、冒号、问号、分号、括号等」，片段里的正则只写了 `[。！？]` 三类，按正文意图应把标点集合补全；`chunkSize` 与 `chunkOverlap` 只做了声明，片段内未展示用法（被 `// ... 其他代码 ...` 折叠），按通用切分器的形态，应当是把 `sentences` 依次拼入 `currentChunk`，达到 `chunkSize` 就收块、并按 `chunkOverlap` 与上一块重叠一段，防止语义正好在边界被截断。类结构上与 Spring AI 的 `TextSplitter` 抽象类一致：`split` 模板方法负责前后处理，`splitText` 是子类实现切分逻辑的钩子。

### 五、RAG 召回优化：查询重写

召回过程也做了优化，通过自动提示过程（查询转换器 `QueryTransformer`）对提示词做优化，帮用户重写查询。不同用户表达能力不同，表达不同会导致查询不同，召回效率也不同；所以接入大模型，让它把用户输入的查询优化、重写一遍，从而提高召回效率。生成 SQL 的节点就是基于 `RetrievalAugmentationAdvisor` 来做的：

```java
public class GenSQLNode implements Node {
    public Map<String, Object> apply(OverallState state) throws Exception {
        // 构建一个检索增强顾问
        RetrievalAugmentationAdvisor retrievalAugmentationAdvisor = RetrievalAugmentationAdvisor.builder()
            .queryTransformer(queryTransformer)
            .documentRetriever(vectorStoreDocumentRetriever)
            .builder()
            .queryAugmenter(ContextualQueryAugmenter.builder())
            .build();
        Flux<String> content = chatClientBuild.build().prompt(
            // 角色
            "你是一名熟练的 SQL 专家，负责根据企业数据库结构生成 SQL 查询。用户将以自然语言提出数据需求。"
            // 要求
            "1. 仅生成可执行的 SQL，不输出与 SQL 无关的文字或解释。\n"
            "2. 在生成 SQL 前，先根据用户需求检索到的表结构进行分析。"
        );
        // ... 其他代码 ...
    }
}
```

这段正是 Spring AI 2.0.1 里 RAG 的标准组装形态，三个部件各司其职：

| 部件 | 职责 | 不做的后果 |
|---|---|---|
| `QueryTransformer` | 把用户口语化提问改写为适合检索的查询 | 用户表达模糊，向量检索召回率低 |
| `DocumentRetriever` | 用改写后的查询从 `VectorStore` 取回表结构文档 | 模型看不到私有表结构，只能编造 |
| `ContextualQueryAugmenter` | 把召回内容拼装进发给大模型的提示词 | 召回了却没喂给模型，RAG 形同虚设 |

如实说明这段代码的形态问题：`RetrievalAugmentationAdvisor.builder()` 链上 `.builder()` 出现了两次，完整实现应是一次性链式配置 `queryTransformer` / `documentRetriever` / `queryAugmenter(ContextualQueryAugmenter.builder().build())` 后 `build()`；`prompt(...)` 里多段字符串字面量之间没有逗号或 `+`，Java 中相邻字面量不会自动拼接，实际应传入完整提示词文本（或按 `ChatClient` 的 `system(...)` / `user(...)` 分句传入）；`chatClientBuild` 与别处的 `chatClientBuilder` 命名不一致；`// ... 其他代码 ...` 表明 advisor 装配之后还要挂到 ChatClient 上、并把 `Flux<String>` 收集成 `genSQL` 写回状态机。视频转写在长链式调用上容易丢行错位，跑工程时以文字描述与真实 API 为准。

此外还对查询做了增强：允许传入空内容，也就是召回内容为空时也不会让整个检索过程报错。这一点常被忽视但很关键，RAG 链路的可用性不能赌「一定召回到东西」，知识库未覆盖的问题照样会来，空召回时应当降级为「仅凭系统提示词作答」，而不是把 500 抛给用户。

向量数据库的选型上，我们讲了用 **Redis** 作向量库和用 **Milvus** 作向量库两种方式。如果公司私有知识库比较大，优先推荐 **Milvus**，第一它存的数据量大，第二检索效率更高。两个方向的取舍：

| 维度 | Redis（向量检索能力） | Milvus |
|---|---|---|
| 课程结论 | 可选方案 | 知识库大时优先 |
| 数据规模 | 适合中小规模 | 存的数据量大 |
| 检索效率 | 一般 | 更高 |
| 工程背景 | 复用已有 Redis 基础设施 | 专门的向量数据库，独立部署 |

### 六、下一章预告

以上就是智能 BI 报表问答系统的全部总结。从下一章开始，我们进入**企业私有化部署大模型**的部分。因为不管是库存调拨系统还是 BI 报表系统，目前参数配置里用的大模型都是第三方平台，阿里云百炼平台提供的 `qwen3-max`。而企业内更多是使用自己私有化部署的大模型，下一章就来讲这块内容。

## 【易错点 / 面试题】

1. **面试官问：「表结构文档为什么要按数字编号标题切，而不是按固定长度切？」**
   答：因为 SQL 生成的正确性依赖跨段信息，字段定义、表间 JOIN 关系必须完整地进入同一个块，模型才能生成正确的关联查询。固定长度切分会把 JOIN 关系切到两个块里，召回任一块都信息不全。切割策略要尊重语义边界：限定文档模板 + 数字编号标题，保证一个编号下是一张完整表结构。

2. **面试官问：「`QueryTransformer` 解决的是什么问题？」**
   答：解决「同一意图、不同表达」导致的召回率波动。用户说「看看去年每个月卖了多少」和「统计 2025 年各月销售总额」，向量空间中的落点并不一致；先用大模型把查询改写规范，再进向量检索，召回稳定性显著提升。它是 `RetrievalAugmentationAdvisor` 的第一环，后面还有 `DocumentRetriever`（取文档）与 `ContextualQueryAugmenter`（拼提示词）。

3. **易错点：召回为空时让链路报错。** 必须允许空召回降级，知识库不可能覆盖所有问题，空内容时凭系统提示词继续作答，把异常吞在链路内部，对外仍是一次完整响应。

4. **面试官问：「该项目里哪些设计可以迁移到你做过的其他系统？」**
   答：至少四个：其一，提示词层拒杀危险操作（只允许 SELECT）+ 执行层 `JdbcTemplate` 限查询的双防线；其二，评估节点 + 条件边 + 循环上限的闭环，以及「上限放配置中心」的运营化；其三，切割尊重语义边界、空召回容错这些 RAG 细节；其四，`threadId` 按用户隔离的状态管理。它们都不依赖 BI 这一具体业务。

## 【小结】

本节把智能 BI 报表问答系统收口：全链路为「RAG 检索生成 SQL → 评估节点（条件边 + 循环上限）→ 执行 SQL 生成 Excel → 发送邮件」，评估失败回环重生成、超限终止；RAG 侧做了两处关键优化，按数字编号标题切分保住表结构语义完整、用 `QueryTransformer` 重写查询提升召回，向量库在知识库规模变大时优先 Milvus；Temperature 压到 0.2 保证输出稳定。遗留改进点是邮件收件人应按 `userId` 寻址，循环上限应下沉 Nacos。同款「ChatClient 抽象 + 结构化落地」的组合在配套工程 `980-demo` 中构成最小闭环：`980-demo/src/main/java/com/carl/ai/transfer/extract/TransferOrderExtractor.java` 用 `chatClient.prompt().user(...).call().entity(TransferOrderParam.class)` 把 LLM 输出直接绑定为 POJO（底层即 `BeanOutputConverter`），与 `GenSQLNode` 用同一个 `ChatClient` 抽象，只是一个面向 RAG 生成、一个面向结构化抽取；`980-demo/src/main/java/com/carl/ai/transfer/convert/TransferOrderConvert.java` 承担 MapStruct 的 `param→model` 转换，`980-demo/src/main/java/com/carl/ai/transfer/service/TransferOrderServiceImpl.java` 与 `BbTransferOrderRepository` 完成受控入库，正好对应本课「生成 → 评估 → 执行 → 落库」链路的工程化缩影。
