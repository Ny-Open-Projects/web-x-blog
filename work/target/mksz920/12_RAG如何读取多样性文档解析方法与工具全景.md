# 12. RAG 如何读取多样性文档：解析方法与工具全景

## 纲要

- **解析由框架整合**：LangChain 的 `document_loaders` 把常用文档解析做了封装，返回统一的 `Document`（含 `page_content` 文本 + `metadata`）。
- **HTML**：`WebBaseLoader`（urllib 下载 + BeautifulSoup 解析）、`BSHTMLLoader`（本地文件）；默认把标记内容顺序拼接（用换行分隔），不区分代码块等特殊内容；定制可用 BeautifulSoup 按标签 + CSS 类提取（如高亮代码块）。
- **PDF**：`PyMuPDFLoader` 提取文本与图片，但**不提表格**；直接用底层 `PyMuPDF`（fitz）`get_text()` + `extract_tables()` 可转 pandas；视觉方案有百度飞桨 PP-Structure、上海AI实验室 MinerU、RAGFlow、收费的 PDFLux / LlamaParse。
- **通用 / Office**：`unstructured` 库自动识别格式调用对应解析器（含位置坐标 + 类别）；Excel `ExcelLoader`、PPT `PowerPointLoader`、Word `Docx2txtLoader` 背后均为 unstructured（仅提文本）；定制用 `openpyxl`（识别合并单元格）、`python-pptx`（遍历 slide 提取文本 / 表格 / 图片）、`python-docx`（段落 + 表格）。
- **RAGFlow 的 deepDOC（机器视觉派）**：PDF 转图片 → OCR 识别文字 → 布局识别模型识别结构（标题 / 段落 / 表格 / 图像）→ TSR 表格识别（行列 + 合并单元格）→ 整合过滤页眉页脚；支持 PDF / Word / Excel / PPT / HTML / TXT / Markdown 多格式。
- **实践建议**：没有万能解析器，按文档特点选方法，复杂版式要做定制开发。
- 本章按课程口径重构；产品 / 框架名已规范化（LangChain / PyMuPDF / unstructured / openpyxl / python-pptx / python-docx / RAGFlow / MinerU）；剥离营销与课程群引流。

## 一、LangChain 的 Document 与 loader 体系

- 几乎所有 LangChain 解析方法都返回 `Document` 对象（`page_content` + `metadata`），下游统一消费。
- `document_loaders` 包聚合了各类解析器，是 RAG 数据读取的入口。

## 二、HTML 解析

- `WebBaseLoader`：自动下载 URL 并用 BeautifulSoup 解析；`BSHTMLLoader`：解析本地 HTML 文件。
- **局限**：把页面所有文本顺序拼接，不区分代码块等；如需只取代码块，用 BeautifulSoup 按 `div` + `highlight` CSS 类 `find_all` 定制提取。

## 三、PDF 解析

- `PyMuPDFLoader`：提取文本与图片，但表格被压成纯文本拼接。
- **定制**：底层 `PyMuPDF`（`fitz`）遍历页 → `get_text()` 取文本、`extract_tables()` 取表格并转 pandas / Markdown。
- **视觉方案**：PP-Structure、MinerU、RAGFlow、PDFLux / LlamaParse（收费）——更智能地识别布局与表格。

## 四、通用与 Office 文档

- `unstructured`：自动识别格式调解析器，返回含坐标与类别；但类别识别未必准。
- Office 专用 loader：`ExcelLoader` / `PowerPointLoader` / `Docx2txtLoader`（均底层 unstructured，仅提文本）。
- **定制提取表格 / 图片**：
 - Excel：`openpyxl` 遍历单元格、识别 `merged_cells.ranges` 合并单元格取值。
 - PPT：`python-pptx` 遍历 `slides` 的 shape，区分文本 / 表格 / `picture` 图片并保存。
 - Word：`python-docx` 遍历段落与表格行列。

## 五、RAGFlow deepDOC：机器视觉解析

- **流程**：PDF 每页转图片 → OCR 文字识别 → 布局识别（标题 / 段落 / 表格 / 图像）→ 对表格区域用 TSR 识别行列与合并单元格 → 整合、过滤页眉页脚 → 输出文本 + 表格。
- **支持格式**：PDF / Word / Excel / PPT / HTML / TXT / Markdown。
- 是 PDF 解析较优的开源方案，适合复杂版式。

## 六、FAQ

**Q1：PyMuPDFLoader 为什么提不出表格？**
它只把文本与图片提出，表格被压成连续文本；需直接用 fitz 的 `extract_tables()` 定制。

**Q2：unstructured 够用吗？**
通用文本提取够用，但版式 / 表格 / 图片识别不准，复杂场景要换专用库或定制。

**Q3：deepDOC 与 PyMuPDF 区别？**
deepDOC 走 OCR + 布局识别 + TSR 的视觉路线，对复杂版式（合并单元格等）更鲁棒；PyMuPDF 偏规则提取。

**Q4：合并单元格怎么正确取值？**
用 `openpyxl` 读 `merged_cells.ranges`，合并区值存于左上角单元格，据此回填。

## 七、面试高频问答

**1. RAG 读取文档的主流框架入口是什么？**
LangChain `document_loaders`，统一返回 `Document(page_content,metadata)`。

**2. 列举 PDF 的两种解析路线。**
规则路线（PyMuPDF / fitz 提文本与表格）；视觉路线（deepDOC / PP-Structure / MinerU，OCR+布局+TSR）。

**3. Office 文档表格/图片怎么定制提取？**
Excel→openpyxl、PPT→python-pptx、Word→python-docx，分别遍历 shape / 段落 / 合并单元格。

**4. deepDOC 的解析流水线？**
PDF转图→OCR→布局识别→TSR表格识别→整合过滤页眉页脚→输出文本+表格。

## 八、ops 提示（增效）

> **先判版式再选器**：纯文本用通用 loader；含表格 / 合并单元格用专用库定制。
>
> **deepDOC 兜底复杂 PDF**：版式乱、合并多，优先 deepDOC 视觉路线。
>
> **统一 Document 契约**：所有解析最终归一为 `Document`，下游分块 / 向量化才稳。

