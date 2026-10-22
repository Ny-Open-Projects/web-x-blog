# 32. 实战：Gradio 整合三大模块 UI 与事件处理部署

## 纲要

- **项目模块化框架（erag）**：把前序功能整合封装，目录含 `model`（大模型+embedding+提示词配置）、`util`（两个 RAG pipeline：制度问答 / 金融智库 Graph RAG）、`rooter`（ReAct RAG Router）、`ui`（界面设计与事件处理）、`assets`（图片）、`data`（模型文件如 embedding）、入口 `erag.py`（调 UI 启服务）。
- **UI 模块三部分**：① 初始设置（方言值、状态值「准备就绪/正在回答/回答完成」）；② 调用 RAG Router 执行 pipeline 并渲染；③ 界面设计（用 `Blocks` + HTML 标题 + Tabs + 行/列布局 + 组件）。
- **界面构建细节**：`Blocks` 设主题 + 标题；HTML 组件显示「企业员工助手 erag」居中标题；`Tabs` 收纳所有组件；左右列 1:3；左列两行（运行状态 Textbox + 参考信息 Textbox + 表格 HTML），右列 Chatbot + 输入框（多模态 Textbox，可上传文件、自动聚焦）+ 按钮行（隐藏左列 / undo / clear / reset）。
- **事件处理（核心）**：
 - `clear`/`reset`：把所有组件设回初始值（message 清空、Chatbot 设空列表、状态「准备就绪」、参考信息/表格清空）；
 - `undo`：从 history 列表去掉最近一个 QA（无数据返回空）；
 - 隐藏左列：切换按钮名称（show/hide）+ 更新该列可见性；
 - **submit（最重要）**：输入=下拉框+文本框+Chatbot；判空→提示；有值→调 Router 文本补全方法得响应（含 LLM 答案 + 上下文；若未走 pipeline 则返回「不能回答」文本）→ 流式收集 trunk 更新组件 → 拆分表格/其他上下文 → 表格进 HTML、其余进参考信息 Textbox。
- **部署**：`erag.py` 实例化 UI → build App；封装 FastAPI（`mount` Gradio 到子路径）→ uvicorn 启，设 4 workers 支持 4 路并发。
- **实测**：问制度问题→调制度 RAG（左列给 3 条上下文+表格）；问企业转型+投资机构→调 Graph RAG（流式答+上下文含投资关系/事件/时间）；问无关问题→返回「不能回答」并拼入 Chatbot；undo/clear/reset 均按预期。
- 本章按课程口径重构；代码为知识重构（外部代码卷未挂载）；产品名已规范（Gradio / FastAPI / uvicorn / erag）。

## 一、项目模块化框架

企业员工助手 erag 把前序功能整合封装：

| 模块 | 内容 |
| --- | --- |
| `model` | 大模型 + embedding 模型 + 所有提示词模板（制度问答/金融智库/关键词提取/ReAct 两类） |
| `util` | 制度问答 RAG pipeline、金融智库 Graph RAG pipeline |
| `rooter` | ReAct RAG Router（按问题选 pipeline，非两类则返回「不能回答」） |
| `ui` | 界面设计 + 事件处理（用 `Blocks`/`Chatbot` 渲染） |
| `assets` | 界面用图片 |
| `data` | 模型文件（如 embedding 模型） |
| `erag.py` | 入口，调 UI 并启动服务 |

> model/util/rooter 代码与前序演示一致，仅整合封装；UI 是新写重点。

## 二、UI 模块结构

UI 代码分三部分：
1. **初始设置**：固定值（方言欢迎词）、状态值（准备就绪/正在回答/回答完成）。
2. **调用 Router 执行 pipeline**：`get_response` 调 `llm_response`（RAG Router 文本补全方法）返回结果。
3. **界面设计**：放 `Blocks` 内，含组件与事件处理。

UI 类含多个事件处理函数（`do_chat`/`undo`/`clear`/`hide_reference` 等）+ `build` 真正构建界面。

## 三、界面构建（Blocks + 布局）

- `Blocks` 设主题（Gradio 内置样式）+ 页面 tab 标题；
- HTML 组件显示「企业员工助手 erag」h1 居中；
- `Tabs` 收纳所有组件；
- **左右列 1:3**：左列两行（状态 Textbox 初始「准备就绪」不可交互 + 参考信息 Textbox + 表格 HTML）；右列 Chatbot（气泡样式/复制按钮/双方图标）+ 问题输入框（多模态 Textbox 可传文件、自动聚焦）+ 按钮行（隐藏左列/undo/clear/reset）。

## 四、事件处理（核心逻辑）

### clear / reset
把组件设回初始值：message 文本框清空、Chatbot 设空列表 `[]`、状态「准备就绪」、参考信息/表格清空。Chatbot 值为 QA 列表，清空即空列表。

### undo
history 存所有 QA 列表；undo 去掉最近一个 QA（无数据返回空初始）。

### 隐藏左列
返回按钮自身（改名称 show/hide）+ 该列可见性（visible 显 / False 隐）。

### submit（最重要）
输入三组件：下拉框 + 问题 Textbox + Chatbot。逻辑：
1. message 为空 → 提示欢迎词；
2. 有值 → 调 Router 文本补全，得响应（LLM 答案 + 上下文；若未走 pipeline 仅返回「不能回答」文本）；
3. 若是纯文本（不能回答）→ 更新 message 清空、拼 QA 入 Chatbot、状态「回答完成」、参考信息给默认值；
4. 若走 pipeline（流式）→ 不断取 trunk 收集、更新 Chatbot/状态「正在回答」/参考信息「生成中」；最后拆分上下文：表格信息 → HTML 组件，其余 → 参考信息 Textbox。

## 五、部署与实测

### 部署
`erag.py` 实例化 UI → build App。两种启法：① 直接 `launch()`（单进程）；② 封装 FastAPI（`mount` Gradio 到子路径）→ uvicorn 启，设 4 workers 支持 4 路并发（按机器性能调进程数）。

### 实测三类问题
| 问题 | 命中 | 结果 |
| --- | --- | --- |
| 关于商假（制度） | 制度问答 RAG | LLM 答，左列 3 条上下文+表格（含亲属规定） |
| 哪些公司转型、投资机构是谁 | 金融智库 Graph RAG | 流式答，上下文含投资关系/事件/时间 |
| 某节目怎么样（无关） | 兜底 | 返回「对不起，不能回答」并拼入 Chatbot |

按钮：undo 撤掉最近 QA；clear/reset 恢复初始；均符合预期。三大模块（制度 RAG / Graph RAG / Router）通过界面完整串联。

## 六、FAQ

**Q1：erag 项目怎么模块化？**
model(模型+提示词)/util(两个RAG pipeline)/rooter(Router)/ui(界面+事件)/assets/data/erag.py 入口。

**Q2：submit 事件核心逻辑？**
判空→提示；有值→调 Router 得响应；纯文本走兜底，pipeline 走流式收集+拆分表格/上下文展示。

**Q3：参考信息里的表格怎么展示？**
用 HTML 组件单独渲染，与文本上下文分开，避免混排。

**Q4：为什么用 FastAPI 封装部署？**
支持多进程并发（uvicorn workers），比 launch 单进程更适合生产。

## 七、面试高频问答

**1. erag 项目模块划分？**
model / util / rooter / ui / assets / data / erag.py 入口。

**2. submit 事件怎么串联三大模块？**
调 Router 文本补全 → 据响应决定走哪条 RAG pipeline（或兜底）→ 流式渲染到 Chatbot + 左列上下文。

**3. 部署支持并发怎么做？**
Gradio mount 到 FastAPI 子路径，uvicorn 启并设 workers 数。

**4. Chatbot 清空/撤销怎么实现？**
清空设空列表 `[]`；撤销从 history 去最近一个 QA。

## 八、ops 提示（增效）

> **模块边界要清晰**：model/util/rooter/ui 分离，UI 只管渲染与事件，RAG 逻辑全在 util/rooter，后期换模型/换库不动 UI。
>
> **流式更新要节流**：submit 流式收集 trunk 时按节奏更新组件，别等全部完成才渲染，否则用户以为卡死。
>
> **生产务必多进程**：uvicorn workers ≥ 机器核数，单进程 launch 只能串行，并发一上来就堵。

