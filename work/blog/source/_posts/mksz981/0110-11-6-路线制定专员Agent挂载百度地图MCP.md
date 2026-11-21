---
disableNunjucks: true
title: 11-6 路线制定专员Agent挂载百度地图MCP
date: 2026-10-24 10:49:00
categories: [多Agent与SpringAI]
tags: [AI Agent, SpringAI, AgentScope, 多Agent与SpringAI]
---

## 【学习目标】

- 理解 `Toolkit` 工具包在多 Agent 工程中的角色：智能体与工具之间的注册中心，本地 `@Tool` 与 MCP 工具在此汇合。
- 完成百度地图 MCP 客户端到路线制定 Agent 的挂载，读懂 `register` 方法重载的设计动机。
- 能用 `getToolNames()` 验证挂载结果，并定位「工具列表为空」的两类典型原因。

## 【正文】

### 1. 挂载思路：Agent → Toolkit → MCP 工具

11-5 完成了客户端的创建与初始化，`initBaiduMapMCP()` 返回的 `McpClientWrapper` 即「已握手、已拿到工具列表」的客户端实例。智能体不能直接持有 MCP 客户端，而是通过工具包（`Toolkit`）间接持有：先把 MCP 客户端注册进 `Toolkit`，再把 `Toolkit` 挂到 Agent 上。

对 ReAct 循环而言，它看到的不是「客户端」对象，而是工具清单里一个个具名的工具（名称 + 描述 + 入参 schema）。模型在推理时读到的正是这些工具描述，据此决定调用哪一个。MCP 的价值正在于此：工具的定义、入参、语义全部由服务端声明，客户端无需为每家地图服务商手写适配层。

```mermaid
flowchart LR
    A["百度地图MCP服务端"] -->|"tools/list 工具清单"| B["McpClientWrapper"]
    B -->|"registerMcpClient"| C["Toolkit 工具包"]
    C -->|"toolkit(toolkit)"| D["ReActAgent 路线制定专员"]
    D -->|"注册到 Nacos"| E["Nacos 注册中心"]
```

### 2. 把临时测试代码搬进 Bean 创建方法

上一节在 `main` 方法中做了临时验证，临时性地创建百度地图 MCP 客户端、完成初始化，并展示从服务端拿到的工具列表：

```java
public static void main(String[] args) {
    BaiduMapMCP mcp = new BaiduMapMCP();
    mcp.getBaiduMapMCP();
    mcp.initBaiduMapMCP();
}
```

现在把同一套逻辑搬进路线制定 Agent 的 Bean 创建方法：

```java
@Bean
public ReActAgent getRouteMakingAgent() {
    BaiduMapMCP mcp = new BaiduMapMCP();
    mcp.getBaiduMapMCP();
    McpClientWrapper mcpClient = mcp.initBaiduMapMCP();
    Toolkit toolUtils = new ToolUtils();
    Toolkit toolkit = toolUtils.getToolkit(mcpClient);
    // 注入到Nacos
    return AgentUtils.getReActAgentBuilder(
        name: "RouteMakingAgent",
        description: "路线制定Agent"
    ).toolkit(toolkit).build();
}
```

逐行拆解：

- 前两行创建并初始化百度地图 MCP 客户端，`initBaiduMapMCP()` 的返回值即已初始化的 `McpClientWrapper`；
- `ToolUtils` 是公共模块中封装的工具类，`getToolkit(mcpClient)` 负责把 MCP 客户端装进工具包并返回 `Toolkit`；
- `AgentUtils.getReActAgentBuilder(...)` 是统一的 Agent 构建入口，传入名称与描述；
- `.toolkit(toolkit)` 完成挂载：路线制定 Agent 从此拥有百度地图 MCP 服务端暴露的全部工具；
- 注释「注入到Nacos」提示该 Bean 会按 11-2 的方式注册到 Nacos，供主管 Agent 远程发现。

### 3. Toolkit 如何注册 MCP 客户端

`ToolUtils.getToolkit` 的实现很短，却是整个挂载机制的核心：

```java
public Toolkit getToolkit(McpClientWrapper mcp) {
    //把MCP服务端的所有工具添加到工具包
    toolkit.registerMcpClient(mcp);
    return toolkit;
}
```

为什么需要重载？在前面的课程中，工具注册走的是 `register` 方法，传入的参数是普通工具对象（`Object`）。MCP 客户端是 `McpClientWrapper` 类型，内部结构并不是「带工具注解的方法集合」，直接按 `Object` 传入原注册方法会报错。因此重写一个同名、同返回类型、入参不同的方法，内部调用专门的 `registerMcpClient` 通道。

这样做的好处是调用方无感：`ToolUtils` 对外只暴露「拿到工具包」一个动作，本地工具与 MCP 工具两种来源被同一方法名屏蔽，后续再加新的工具来源也不必改动调用处。这是「用重载统一入口」的典型手法，入参类型决定分派到哪套注册逻辑，对外签名保持稳定。

### 4. 第一次运行：工具列表为空

验证方式很直接：挂载后调用工具包的 `getToolNames()`，把成功注册的工具列出来。首次运行的结果是空的。原因有两个：

1. **遍历方式不对**：工具包所列出的工具是一个 `Set` 集合，循环打印时需要加上 `stream()` 再调用 `forEach()`，直接迭代拿不到预期输出。这是 Java 集合 API 的使用细节。
2. **注册是异步的**：`registerMcpClient` 注册的并不是客户端对象本身，而是客户端所持有的 MCP 服务端工具列表；工具数量较多时，把每个工具逐个写入工具包需要时间。因此注册调用之后要 `block()` 等待注册完成，再打印工具名，否则读到的是「还没写完」的中间态。

修正后再次运行，日志先逐条输出每个工具的注册进度（`Registered tool ... in group 'ungrouped'`），随后打印出工具包内已完成注册的全部工具：

```
百度地图MCP工具列表: map_poi_extract
Registered tool 'map_geocode' in group 'ungrouped'
Registered tool 'map_reverse_geocode' in group 'ungrouped'
Registered tool 'map_search_places' in group 'ungrouped'
Registered tool 'map_place_details' in group 'ungrouped'
Registered tool 'map_directions_matrix' in group 'ungrouped'
Registered tool 'map_weather' in group 'ungrouped'
Registered tool 'map_ip_location' in group 'ungrouped'
```

按名称直读，日志中完成注册的工具覆盖七类地图能力：

| 工具名 | 按名称直读的用途 |
|---|---|
| `map_geocode` | 地理编码：地址转经纬度 |
| `map_reverse_geocode` | 逆地理编码：经纬度转地址 |
| `map_search_places` | 地点检索 |
| `map_place_details` | 地点详情查询 |
| `map_directions_matrix` | 路线/通勤矩阵计算 |
| `map_weather` | 目的地天气查询 |
| `map_ip_location` | IP 定位 |

至此，路线制定 Agent 的工具包中拥有了上述全部工具，可以支撑路线的制定。

从上下文角度看这次挂载的代价：七个工具的名称、描述、入参会一并进入模型的工具清单，每轮推理都要携带。工具数量上升到几十个时，就需要 10-4 讲过的渐进式加载思路来控制上下文规模，先索引，按需取用，而不是一次性全量注入。

## 【易错点 / 面试题】

1. **为什么 MCP 客户端不能直接按 `Object` 注册？** 类型不匹配：`register(Object)` 内部按「带工具注解的普通方法集合」处理，`McpClientWrapper` 并不符合这一结构，必须走 `registerMcpClient` 专用通道。重载而非改方法名，是为了让调用方继续用同一入口。
2. **注册后立刻 `getToolNames()` 为空？** 异步注册尚未完成，需要 `block()` 等待；日志中逐条出现的 `Registered tool ...` 就是注册进度的直接证据，排错时先看有没有这行。
3. **面试题：MCP 工具与本地 `@Tool` 工具在 Toolkit 里如何统一？** 两者最终都归一为「工具名 + 描述 + 入参 schema」汇入同一工具包，ReActAgent 只面对统一的工具清单，不关心工具来自本地代码还是远程 MCP 服务端。对应到 Spring AI 技术栈，即本地 `@Tool` 与 `McpToolCallback` 都可注册进 `ChatClient` 的工具集，由 `ToolCallingAdvisor` 统一驱动工具循环；工具数量庞大时还可引入 `ToolSearchToolCallingAdvisor` 做渐进式工具披露，控制进入上下文的工具规模。

## 【小结】

本节把百度地图 MCP 客户端通过 `Toolkit` 挂载到路线制定 Agent，并以 `getToolNames()` 验证了七类地图工具全部就位。下一节（11-7）让主管 Agent 不再依赖人工指定的成员名单，而是自主从 Nacos 发现远程成员并分发任务。在 `981-demo` 工程中，`com/travel/agent/agent/TeamMembers.java` 的 `routeMakingAgent` Bean 与 `com/travel/agent/tool/RouteMakingTools.java` 共同复刻了本节链路：源码注释中明确写着「真实环境里这些工具由百度地图 MCP Server 提供（map_geocode / map_directions 等），通过 `Toolkit.registerMcpClient(...)` 挂载到智能体」，离线演示则用本地桩返回同构数据，保证挂载形态与生产一致。
