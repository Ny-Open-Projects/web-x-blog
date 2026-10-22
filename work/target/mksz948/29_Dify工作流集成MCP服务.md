# 29. Dify 工作流集成 MCP 服务

## 纲要

- **装 Agent 插件**：插件市场搜 `agent` → 装「Agent 策略」+「Dify Agent 策略」（前两个）
- **建 chatflow 工作流**：工作室 → 创建空白应用选 **chatflow 工作流** → 命名（如 `springAI-MCP`）
- **加 Agent 节点（react 策略）**：右键添加节点 → Agent → 策略选 **react（支持 MCP tools，下面那个）**，不选 functioncall（上面那个）→ 选大模型（通义千问 max / DeepSeek 等）
- **配置 MCP 工具**：工具列表里删默认示例只留一个 → 自定义 `serverName=springAI-MCP`、`transport=SSE`、URL=云上 `http://公网IP:488/sse`（从 Cursor 复制）→ 系统提示词「你是非常厉害的 MCP 工具调用助手…」→ 用户输入映射 `sys.query` → 记忆可开（`ChatMemory`）
- **连线与输出**：删原 LLM 节点，把开始 → Agent → 直接回复（显示 `agent 的 text 输出变量`）；**最大迭代次数必填**（否则发布报错）
- **实测**：「查询所有商品列表」→「以 HTML 展示并发送邮箱」→ 邮箱收到商品列表；日志可见调用链路

> 本章代码基于课程标准工程（`com.itzixi` 包）按课程口径重构，外部代码卷暂未挂载，重挂后可切换为逐文件提取的真实代码。

## 一、安装 Agent 插件

插件市场 → 搜 `agent` → 安装：
1. **Agent 策略**
2. **Dify Agent 策略**

> 老师推荐装这两个即可，其余按需。

## 二、创建 chatflow 工作流

```
工作室 → 创建空白应用 → 类型选「chatflow 工作流」→ 命名 springAI-MCP
```

默认三个原始节点：开始 → 大模型(LLM) → 直接回复。先跑默认（配大模型后「你是谁」可交互，走 DeepSeek）。

## 三、添加 Agent 节点（react 策略）

### 3.1 选策略

右键画布 → 添加节点 → **Agent** → 策略选**下面那个 `react`（支持 MCP tools）**，不是上面 `functioncall`。

> 两个策略区别：上面 `functioncall` 不支持 SSE MCP；下面 `react` 支持 MCP tools —— 本课用 react。

### 3.2 选大模型 + 删原 LLM

Agent 节点选大模型（通义千问 max / DeepSeek 等）→ 选中原 LLM 节点**删除** → 把「开始」连到 Agent、「Agent」连到「直接回复」。

## 四、配置 MCP 工具列表

Agent 节点 → 工具列表 → 点添加：

```
serverName  = springAI-MCP          # 自定义
transport   = SSE                    # 类型
URL         = http://公网IP:488/sse   # 从 Cursor 配置复制；本地用 localhost:488/sse
```

- 删掉默认示例，只保留这一个自研 MCP server 配置。
- 系统提示词（指令）：
 > 你是一个非常厉害的 MCP 工具调用助手，请根据用户的输入使用合适的 MCP 工具来反馈内容或者反馈用户的提问。

- 用户输入映射：`sys.query`（预览时输入框的自然语言即 `sys.query`）。
- 记忆功能：可开启/关闭（对应代码里的 `ChatMemory`）。
- **最大迭代次数**：必填（老师踩坑：不填发布报「不能为空」，手动补上再发布）。

## 五、连线与输出变量（踩坑）

老师踩坑：Agent 输出没显示 → 原因「直接回复」仍接原 LLM 输出 → 删除 LLM 关联，把「直接回复」的内容改为显示 **Agent 的 `text` 输出变量**。否则工作流跑成功但画面无内容。

```
开始 → Agent(react, MCP工具) → 直接回复(显示 agent.text)
```

## 六、发布与实测

1. 点「发布」（= 更新）→ 点「预览」测试。
2. 「查询所有商品列表」→ Agent 调 MCP 查库 → 日志可见；因加了「列表」二字返回纯 JSON（Dify 不便展示），可让模型以 markdown/HTML 回复。
3. 「查询所有商品信息，并用好看的 HTML 展示，发送到我的邮箱」→ 查商品 → 生成 HTML → 发邮件 → 邮箱收到列表。

> 老师提到在写 Dify 相关书籍，鼓励持续关注/交流。

## 七、工作流集成时序图

```mermaid
flowchart LR
    A[开始 sys.query] --> B[Agent节点 react策略]
    B --> C{工具列表: springAI-MCP(SSE)}
    C --> D[云上 mcp-server:488/sse]
    D --> E[查商品/邮件等MCP工具]
    E --> F[Agent.text 输出]
    F --> G[直接回复展示]
```

## 八、排错 SOP

1. **发布报「最大迭代次数不能为空」**：手动填入数值再发布（Dify bug，需显式填）。
2. **工作流成功但无输出**：「直接回复」仍接旧 LLM 输出；改成显示 Agent 的 `text` 变量。
3. **MCP 连接失败**：URL 协议/端口错（SSE 用 `http://公网IP:488/sse`）；安全组未放通 488。
4. **策略选错（functioncall）**：不支持 SSE MCP，换下面 react 策略。
5. **查商品只返回 JSON**：提示词要求 markdown/HTML 展示，纯「列表」易返 JSON。
6. **邮件发不出**：server 端邮件 MCP 配置正确且 server 运行；Dify 容器能访问公网发信。

## 九、FAQ

**Q1：react 和 functioncall 策略怎么选？**
要接 SSE MCP 工具选**下面 react**（支持 MCP tools）；functioncall 不支持 SSE MCP。

**Q2：serverName/transport/URL 怎么填？**
serverName 自定义；transport 选 SSE；URL 填云上 `http://公网IP:488/sse`（本地 `localhost:488/sse`）。

**Q3：sys.query 是什么？**
预览时用户在输入框的自然语言内容，映射到 Agent 的用户提问。

**Q4：为什么直接回复没内容？**
「直接回复」要接 Agent 的 `text` 输出变量，不是原 LLM；删 LLM 关联后重连。

**Q5：记忆功能对应什么？**
对应代码里的 `ChatMemory`，Agent 节点可开关多轮记忆。

**Q6：最大迭代次数干嘛的？**
限制 Agent 调用工具/推理的轮数，防死循环；Dify 要求必填。

## 十、面试高频问答

**1. Dify 工作流如何接外部 MCP？**
Agent 节点选 react 策略 → 工具列表加 SSE 类型 server（URL=server 的 /sse）→ 系统提示词引导调用。

**2. chatflow 与 agent 节点关系？**
chatflow 是可视化编排画布；Agent 节点在其内提供自主工具调用能力，串接开始/回复节点。

**3. 为什么用 react 而非 functioncall？**
react 支持 MCP tools（SSE），functioncall 不支持 SSE MCP，本课远程 server 必选 react。

**4. 工作流输出如何绑定？**
「直接回复」节点内容选 Agent 的 `text` 输出变量，否则空显；需删原 LLM 连线。

**5. Dify 集成自研 MCP 的价值？**
低代码把自研工具接入企业级 Agent/工作流，免写客户端，快速编排查库/发邮件等能力。

**6. 多工具自动编排在 Dify 体现？**
「查商品+HTML+发邮件」触发查库→生成HTML→发邮件，Agent 按提示词自主串联，日志可追溯。

## 十一、ops 提示（安全与网络）

> **MCP 暴露**：Dify 接的 `http://公网IP:488/sse` 暴露公网，需 server 端鉴权/白名单，别裸奔。
>
> **插件来源**：Agent 插件从 Dify 市场装，审可信度；避免装来路不明插件引入后门。
>
> **最大迭代次数**：设合理上限防 Agent 失控刷工具/烧 token；生产设较小值并监控。
>
> **提示词注入**：用户自然语言进系统提示词驱动的 Agent，防恶意指令越权调工具（如删库），server 端工具应做权限边界。
>
> **数据合规**：邮件/查库涉及用户数据，工作流经公网发信注意脱敏与授权。

> **课程收官**：Dify 工作流接 MCP 完成。mksz948（13 章）全部博客卡产出完毕 —— 从导学、SpringAI、环境、RAG、SearXNG、MCP、数据库交互、云部署到多平台集成，全栈打通。
