# 4-8 Jmanus导入SpringAi自定义的MCP服务

【学习目标】

- 回顾基于 Spring AI Alibaba 的 MCP 服务端两种 Web 栈依赖选型（WebFlux 与 WebMVC starter）。
- 独立完成天气 MCP 服务端的 `application.yml` 配置与启动类编写，跑通服务端。
- 在 JManus 工作台把自定义 MCP 服务端导入为 SSE 类型配置，并定位 「URL path must contain 'sse'」 报错的原因。
- 记住 MCP 客户端配置的三要素：名称、通信类型、服务端地址。

【正文】

### 1. 回顾：MCP 服务端的两种 Web 栈依赖

上一节按 Spring AI Alibaba 文档实现了 MCP 服务端的 SSE 协议，导入的核心依赖如下：

```xml
<!-- 基于SpringBoot 的 Webflux 框架 实现MCP 服务端的 SSE 协议 -->
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>

<!-- 同样能够实现MCP 服务端的 SSE 协议 -->
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webmvc</artifactId>
</dependency>
```

两个 starter 都能实现 MCP 服务端的 SSE 协议，差别在底层 Web 栈：

| starter | 底层 Web 栈 | 适用场景 |
|---|---|---|
| `spring-ai-starter-mcp-server-webflux` | Reactor Netty + WebFlux，响应式非阻塞 | 高并发长连接场景，SSE 与响应式流天然同构 |
| `spring-ai-starter-mcp-server-webmvc` | Spring MVC，Servlet 阻塞栈 | 团队存量栈以 MVC 为主，接入成本低 |

选型理由：MCP 的 SSE 通道是「一条长连接持续推送消息」的形态，与 WebFlux 的 `Flux` 响应式流同构，因此文档首选 WebFlux；若团队熟悉 MVC、并发量不大，WebMVC starter 也能把同一套工具暴露成 MCP 服务端。生产上还有一条经验：MCP 服务端通常独立部署（如本课的 `imooc-weather-mcp-server`），与业务主应用进程隔离，避免工具端异常拖垮业务端。

### 2. 配置 MCP 服务端：application.yml

MCP 服务端的配置放在 Resources 目录下的 `application.yml`：

```yaml
server:
  port: 8081
spring:
  application:
    name: imooc-weather-mcp-server
ai:
  mcp:
    server:
      # MCP服务器的地址
      sse-message-endpoint: /mcp/weather
```

逐项说明：

- `server.port: 8081`：MCP 服务端使用独立端口，与主应用（JManus 的默认端口）错开，避免端口冲突；
- `spring.application.name: imooc-weather-mcp-server`：服务名，注册中心（如 Nacos）里以此标识该服务端；
- `ai.mcp.server.sse-message-endpoint: /mcp/weather`：SSE 消息端点路径，客户端经由此路径建立 SSE 连接并收发工具调用消息。

此处有一个文档未写明的坑：`sse-message-endpoint` 必须显式配置。Spring AI Alibaba 文档的快速开始没有列出这一项，但不配置它，客户端连接时会因端点缺失而失败。跟着课程实录配置可以直接绕开此坑，这也是「跟着文档抄会漏、跟着踩过坑的课程学能省时间」的典型例子。

### 3. 启动类：WeatherMCPApplication

在 server 包下创建 Spring Boot 启动类。由于该 MCP 专为天气服务，启动类命名为 `WeatherMCPApplication`：

```java
@SpringBootApplication
@EnableScheduling
public class WeatherMCPApplication {
    public static void main(String[] args) throws IOException, InterruptedException {
        if (args != null && args.length >= 1 && args[0].equals("Playwright")) {
            Playwright.create();
            System.out.println("Playwright init finished");
            System.exit(0);
        } else {
            SpringApplication.run(WeatherMCPApplication.class, args);
        }
    }
}
```

两个注解的分工：

- `@SpringBootApplication`：标准 Spring Boot 启动注解，组合了配置类声明、自动配置与组件扫描；
- `@EnableScheduling`：开启定时任务支持。MCP 服务端若需要周期性刷新数据（如定时抓取天气），定时任务是直接载体。

`main` 方法里多出一条 Playwright 分支：启动参数为 `Playwright` 时，仅完成 Playwright 初始化后退出；否则正常启动 Spring Boot 应用。这样设计把「浏览器环境初始化」与「服务启动」解耦，部署时可以先跑一次初始化命令准备好运行环境，再以无参方式启动服务。`IOException` 与 `InterruptedException` 的抛出签名与 Playwright 初始化过程中的阻塞等待相对应。

运行启动类，日志显示服务启动成功。从日志结构还能看出一条关键事实：MCP 服务端本质上就是一个 Controller，Spring AI Alibaba 把 MCP 的 SSE 端点注册成了 Web 端点，工具调用消息经由 HTTP 通道进出。理解这一点有助于排查连接类问题：先确认端点路径与端口，再怀疑协议层。

### 4. 在 JManus 中导入自定义 MCP 服务端

JManus 项目在第 1 章已导入，启动类为 `OpenManusSpringBootApplication`，点击即可启动。进入工作台后，按两条横杠图标打开设置，可见 Tools 与 MCP 配置入口；进入后 MCP 服务器列表为空，点击「新建 MCP 配置」。

新建配置只有三个字段：

| 字段 | 本例取值 | 说明 |
|---|---|---|
| MCP 的名称 | `imooc-weather-mcp-server` | 与 `application.yml` 的 `spring.application.name` 保持一致 |
| 通信的类型 | SSE | 基于 SSE 协议的连接方式 |
| MCP 的地址 | `http://127.0.0.1:8081/mcp/weather` | 服务端地址，含 SSE 端点路径 |

首次保存时地址填的是 `http://127.0.0.1:8081`，点击保存后报错：

> Failed to add MCP server: 400 - MCP server configuration validation failed: SSE type URL path must contain 'sse'

报错含义：SSE 类型的 MCP 配置，其 URL 路径中必须包含 `sse` 标识，JManus 客户端据此判定连接方式与端点约定，缺少该标识即校验失败。按课程实录，把地址修正为 `http://127.0.0.1:8081/mcp/weather` 后保存成功，MCP 服务器列表中出现刚添加的、基于 Spring AI Alibaba 实现的天气服务端。

完整导入流程如下：

```mermaid
flowchart TD
    A["启动 WeatherMCPApplication<br/>端口 8081"] --> B["JManus 工作台 → 设置 → Tools/MCP"]
    B --> C["新建 MCP 配置<br/>名称 + 类型 + 地址"]
    C --> D{"点击保存"}
    D --|地址为根路径| E["400 校验失败<br/>URL path must contain 'sse'"]
    D --|地址含端点路径| F["保存成功<br/>出现在 MCP 服务器列表"]
    E --> C
```

### 5. 与后续章节的衔接

本课把「自定义 MCP 服务端」跑起来并导入 JManus，验证的是 MCP 客户端配置的最小闭环。到第 11 章，路线制定专员 Agent 会挂载百度地图 MCP（11-6），主管 Agent 通过 A2A 协议调度远程成员（11-7），届时 MCP 服务端从「本机演示的天气服务」换成「真实地图服务」，客户端侧的导入方式与本课完全一致。

【易错点 / 面试题】

1. **`sse-message-endpoint` 漏配**：文档未列此项，但不配客户端无法建立连接。排查顺序：先确认 `ai.mcp.server.sse-message-endpoint` 存在且与客户端填写的地址路径一致，再查端口占用与防火墙。
2. **SSE 地址校验失败**：JManus 对 SSE 类型配置强制校验 URL 路径含 `sse` 标识，直接填根地址会报 400。面试变体：「MCP 客户端连接服务端需要哪些信息？」，名称（服务标识）、传输类型（SSE 等）、服务端地址，三者缺一不可。
3. **两个 starter 混用**：WebFlux 与 WebMVC starter 二选一，同时引入会导致端点注册冲突。选型依据是团队技术栈与并发量，而非功能差异。

【小结】

本节以天气 MCP 服务端为样本，走完「依赖选型 → yml 配置 → 启动类 → 客户端导入」的完整链路，两条关键经验：`sse-message-endpoint` 必须显式配置；SSE 类型地址受客户端校验约束。可部署工程中，路线制定专员的工具箱 `981-demo/src/main/java/com/travel/agent/tool/RouteMakingTools.java` 即按「百度地图 MCP 服务端暴露工具列表」的形态组织：真实环境下 `map_geocode`、`map_directions` 等工具由百度地图 MCP Server 提供并挂载到智能体，离线演示用本地桩返回同构数据，保证「工具挂载 → 工具调用 → 结果回传」的链路形态与生产一致。技术前瞻：Spring AI 主线的 2.x 已把 MCP 工具暴露从手动注册 SSE 端点演进为注解式（`@McpTool`/`@McpResource`），并将 Skills、子 Agent 与渐进披露纳入 Spring AI Agents 方向，未来工具挂载会更标准化，但「显式配置端点 + 客户端按传输类型校验」这一连接契约不会变。下一篇看 Spring AI Alibaba 1.1 如何以 BOM 方式统一管理依赖。
