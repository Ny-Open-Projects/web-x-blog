# 9-4 集成Tika文档读取器实现文档读取

## 【学习目标】

- 独立实现文档上传入口与 `DocumentService.handleDocument` 的骨架，说清「读取 → 切分 → 向量化 → 入库」四步各自的位置。
- 能说清向量模型与对话模型的区别，以及 Spring AI 已集成的文档读取器清单和选 Tika 的理由。
- 说清 `Document` 对象的结构（id / text / media / metadata），为后续切分与入库打好基础。

## 【正文】

### 一、先有数据，才有 RAG

在正式开发 Agent 之前，必须先有前置数据，也就是先把私有知识库建起来。只有以它为基础，大模型才能拿着私有知识库里的内容作为上下文来回答问题。所以开发的第一步是实现向量存储：上传文档 → 文档读取器读取 → 切分成不同的块 → 借助向量模型把文本块转成向量 → 存入向量数据库。这一步做完之后，后续的 Agent 开发才有数据源头，向量数据库才能作为上下文的数据来源。

```mermaid
flowchart LR
    A["上传文件 MultipartFile"] --> B["TikaDocumentReader 读取"]
    B --> C["TextSplitter 切分"]
    C --> D["EmbeddingModel 向量化"]
    D --> E["VectorStore 入库"]
```

### 二、上传入口：谁有权上传

回到 IDEA，先在 `helper` 包下建 `controller` 包，在其中创建 `DocumentController`，也就是文档处理接口，加上 `@RestController` 注解与 `@RequestMapping("/document")`。

```java
@RestController
@RequestMapping("/document")
public class DocumentController {
    @Resource
    @GetMapping("/upload")
    public R upload(MultipartFile file) {
        // 代码逻辑
    }
}
```

接下来要写的是文档上传接口。具体到这套系统，文档的上传方是开发人员而不是业务部门，因为上传的文档里主要存放的是表结构定义以及表与表之间的关系，只有程序员才清楚系统设计时表是怎么设计的、表之间是什么关系，所以这类文档理应由程序员提供。

该定位有两个工程后果：上传接口属于内部运维接口，不需要做复杂的权限体系；文档内容有固定撰写规范（表名、字段、关系齐全），元数据里应标明来源，方便出问题时溯源。

片段说明：`@Resource` 后面省略了字段声明，`upload` 方法体是占位逻辑，这是课程先搭骨架再填肉的写法；另外片段用 `@GetMapping` 接收文件，生产上的上传接口通常声明为 POST，语义更准确。

### 三、分层：重活下沉到 Service

拿到文件之后的处理流程是：先读取，再拆分，然后转成向量，最后入库。这几步涉及的代码量不小，不适合直接堆在 Controller 层，因此单独抽一层 Service。先建 `service` 包，再在其中建 `impl` 包，定义 `DocumentService` 接口并创建实现类 `DocumentServiceImpl`，实现类上标注 `@Service`。Controller 中通过 `@Resource` 注入 `DocumentService`。

Service 接口里定义 `handleDocument` 方法（处理文档），接收 `MultipartFile` 参数，不设返回值，Controller 侧直接返回 `R.success`。用 `Alt + Enter` 在接口上创建方法，再在实现类中生成实现，然后填充业务逻辑：第一步读取文档，即通过文档读取器把上传的文件读成文档对象，本质上相当于一次格式转换；第二步文档拆分，切成不同的块；第三步借助向量大模型把文本块转成向量；第四步入库。

分层理由值得说透：四步链路未来会被多个入口复用（手动上传、批量导入、定时同步），且每一步都有独立的异常与重试策略，堆在 Controller 里会迅速膨胀。Controller 只负责收参数、调 Service、包响应；Service 负责编排链路。

顺带说明统一响应体 `R`：它来自 `ai-common` 模块，使用前需要把该模块依赖加到 `ai-bi-helper` 的 POM 里并刷新，再回到 Controller 导入 `R`，编译就不再报错，这正是 9-3 里多模块设计的兑现点。

### 四、向量模型与对话模型

这里顺带说明向量大模型。它同样属于大模型的一种：常说的 DeepSeek、千问、ChatGPT 这类是做语言交互的大模型，而向量大模型不做语言交互，只负责把文本转成向量。两者的输入输出契约完全不同：

| 对比项 | 对话模型 | 向量模型 |
|---|---|---|
| 输入 | 提示词（系统消息 + 用户消息） | 一段文本 |
| 输出 | 自然语言回复 | 固定维度的浮点数组 |
| 用途 | 生成、改写、决策 | 相似度计算、语义检索 |
| 调用方式 | 多轮对话 | 单段进出、无状态 |

选型红线：写入与查询必须使用同一个向量模型。不同模型产出的向量不在同一语义空间，混用的后果是「存得进、查不出」。

### 五、文档读取器选型：Tika

先做第一步，读取文档，这需要文档读取器。Spring AI 官方文档的 ETL 章节下有 `Document Readers` 一节，列了它已经集成的文档读取器：

| 读取器 | 覆盖格式 | 适用场景 |
|---|---|---|
| JSON 读取器 | JSON | 结构化配置、接口数据入库 |
| `Text Reader` | TXT | 纯文本 |
| HTML 文档读取器（基于 JSoup） | HTML | 爬虫抓取的页面 |
| Markdown 读取器 | MD | 技术文档 |
| `PDF Page` 读取器 / PDF 读取器 | PDF | 需要按页、按段精细控制时 |
| `Tika` 读取器 | PDF、DOC、DOCX、PPT、PPTX、HTML 等 | 格式混杂的通用场景 |

`Tika` 读取器的覆盖面最广，本项目就选用它来做文档读取。文档页面上已经贴出了对应的 Maven 依赖，直接复制到项目 POM 中引入，刷新后没有报错。

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-pdf-document-reader</artifactId>
    <version>1.0.3</version>
</dependency>
```

如实说明：课程此处贴出的依赖 artifactId 是 `spring-ai-pdf-document-reader`，而正文选用的读取器是 Tika，两者并不是同一个模块。复制坐标后，验收标准是「能否 import 到 `TikaDocumentReader`」，刷新 Maven 并编译验证。这类「文档说用 A、POM 里是 B」的坐标错位，是复制依赖时最常见的坑。

### 六、TikaDocumentReader 用法

回到 Service 实现，直接 `new TikaDocumentReader(...)` 创建读取器。构造参数需要一个 `Resource`，而 `MultipartFile` 本身就提供了 `getResource()` 方法，直接传入即可。拿到 reader 之后调用它的 `get()` 方法，会返回一个文档集合 `List<Document>`。

```java
@Service
public class DocumentServiceImpl implements DocumentService {
    // 业务逻辑
    @Override
    public void handleDocument(MultipartFile file) {
        // 读取文档内容
        new TikaDocumentReader(Resource resource);
        // 代码逻辑
    }
}
```

片段说明：`new TikaDocumentReader(Resource resource);` 这行是「声明用法」性质的占位代码，把构造参数的类型直接写在了调用位置。落到工程里应为：用 `file.getResource()` 构造读取器，调用 `get()` 取得 `List<Document>`，再交给后续切分步骤。代码块按课程原样保留，此处只在正文说明真实写法。

每个 `Document` 中包含 `id`、`text`、`media` 以及一个 Map 格式的 `metadata`：`id` 是文档标识，`text` 是读取出的文本内容，`media` 记录 MIME 类型等媒体信息，`metadata` 放来源文件名、标题等自定义键值对。换言之，文档读取器已经把上传的文档文件转换成文档集合，并自动往这些字段里填好了对应的数据。

生产上还有三条注意：加密或损坏的文件会让 Tika 解析抛错，需要捕获后返回明确错误码，而不是把异常堆到前端；超大文件要考虑内存占用，优先流式解析；`MultipartFile` 在容器里落在临时目录，处理完注意清理。

## 【易错点 / 面试题】

1. **面试官问：为什么选 Tika 而不是各格式专用读取器？** 一份依赖覆盖 PDF、DOC、DOCX、PPT、HTML 等主流格式，上传方是开发人员、格式不可控时最省心；代价是放弃细粒度控制，例如需要按页切分 PDF 时要换回 PDF 读取器。
2. **面试官问：`Document` 的 metadata 用来干什么？** 承载溯源信息（来源文件、章节标题等），召回成功后能告诉用户「结论出自哪份文档的哪一段」。这是 RAG 可解释性的基础，也是评测召回质量的抓手。
3. **易错点：向量模型混用。** 写入用一个模型、查询用另一个模型，向量不在同一语义空间，检索结果近似随机。写入与查询的模型名要作为配置固定下来。

## 【小结】

本节打通了 RAG 的数据源头：上传入口 `DocumentController`、服务骨架 `DocumentService.handleDocument`、读取器选型（Tika，覆盖面优先）与 `Document` 对象结构。四步链路只完成了第一步「读取」，切分与向量化在下一篇展开。

「Controller 只编排、Service 干重活」的分层思路，在本课程配套工程 `980-demo/src/main/java/com/carl/ai/transfer/controller/TransferController.java` 与 `980-demo/src/main/java/com/carl/ai/transfer/service/TransferOrderServiceImpl.java` 中同样成立，可对照阅读。
