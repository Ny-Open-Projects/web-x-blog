# 44. 文档加载与解析：DocumentLoader 与 Parser

## 纲要

- **第一步永远是加载数据源**：把文档读进内存才能分割/向量化
- **LangChain4j 内置加载器**：`FileSystemDocumentLoader`（文件）、`ClassPathDocumentLoader`（类路径）、`UrlDocumentLoader`（网页），以及 AWS/GitHub/Google/腾讯云等厂商加载器
- **文档解析器接口**：`DocumentParser`，实现类覆盖 TXT/HTML/Markdown（默认 `TextDocumentParser`）、PDF（`PDFBoxDocumentParser`）、微软 Office（`POI`）、Apache Tika 万能解析
- **加载 API 三场景**：单个文档 / 目录全部 / 目录含子目录递归
- **默认解析器**：不指定 parser 时用 `TextDocumentParser`，适合 TXT/MD/HTML

> 代码按课程口径重构示意（外部课件代码卷未挂载）。本卡覆盖 8-4/8-5/8-6，聚焦「怎么把各种格式塞进内存」。

## 一、加载器家族

```java
// 文件加载
List<Document> docs = FileSystemDocumentLoader.loadDocuments("/data/kb", new TextDocumentParser());
// 目录+后缀过滤
List<Document> docs = FileSystemDocumentLoader.loadDocuments("/data/kb",
        new FileExtensionMatcher(".txt"), new TextDocumentParser());
// 递归子目录
List<Document> docs = FileSystemDocumentLoader.loadDocumentsRecursively("/data",
        new FileExtensionMatcher(".txt"), new TextDocumentParser());
```

`UrlDocumentLoader` 直接传网页地址加载；厂商加载器（AWS/GitHub 等）需引入对应坐标。

## 二、解析器选择

| 格式 | 解析器 | 备注 |
|---|---|---|
| TXT / MD / HTML | `TextDocumentParser` | 默认，无需额外依赖 |
| PDF | `PDFBoxDocumentParser` | 需引 `pdfbox` 坐标 |
| Word/PPT/Excel | Apache POI 解析器 | 需引 POI 坐标 |
| 几乎全格式 | Apache Tika 解析器 | 自动检测类型，万能但重 |

## 三、加载即解析

```java
// 加载时指定解析器
Document doc = FileSystemDocumentLoader.loadDocument(
        "/data/sample.pdf", new PDFBoxDocumentParser());
System.out.println(doc.text());   // 打印解析出的文本
```

源码里 `loadDocument` 默认走 `DefaultDocumentParserFactory`，文本类用 `TextDocumentParser`；PDF 必须显式换 parser，否则解析失败。

## 四、FAQ

**Q1：不指定 parser 会怎样？**
用默认 `TextDocumentParser`，仅适合 TXT/MD/HTML；PDF/Word 必须换对应 parser。

**Q2：递归加载有什么坑？**
会遍历所有嵌套子目录，注意过滤后缀，避免把无关文件塞进知识库。

**Q3：Tika 万能解析值得用吗？**
格式杂、来源不可控时好用；但依赖重、对纯文本场景是杀鸡用牛刀。

## 五、面试高频问答

**1. LangChain4j 常见文档加载器？**
FileSystem / ClassPath / Url，以及 AWS/GitHub 等厂商加载器。

**2. 不同格式怎么解析？**
按格式选 `DocumentParser`：文本用默认，PDF 用 PDFBox，Office 用 POI，杂格式用 Tika。

**3. 加载 API 有哪几种粒度？**
单文档 / 目录全部 / 递归子目录三种。

## 六、ops 提示（加载红线）

> **解析器按需引入**：PDF 不引 `pdfbox`、Office 不引 POI 会运行时报错，按需加坐标。
>
> **后缀过滤必须配**：目录/递归加载务必用 `FileExtensionMatcher` 限定类型，防止污染知识库。
>
> **默认解析器只认文本**：别拿 `TextDocumentParser` 去解析 PDF，先识别格式再选 parser。

