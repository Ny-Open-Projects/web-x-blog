# 4-1 Spring Boot 4 快速入门，打造企业级项目基座

## 【学习目标】

学完这一篇，你应该能够：

1. 说清为什么本课程选 Spring Boot 作为基座，以及它「约定优于配置」解决了什么痛点。
2. 理解 Spring Boot 4 与 3.5.x 两条版本线的定位、生命周期与支持周期，做出合理选型。
3. 讲清 Spring Boot 4 的系统要求（Java 版本、构建工具、内嵌容器、Spring Framework 基线），并对照课程已配好的 JDK 21 + Maven。
4. 看懂配套工程 `982-demo` 的真实 `pom.xml`：它如何用 `spring-boot-starter-parent` 4.1.1 锁定版本、如何引入 Spring AI 2.0.1 的 `ChatClient` 抽象。
5. 在面试中回答「Spring Boot 自动配置是怎么工作的」「 starters 解决了什么问题」。

从这一章开始，我们就正式动手写代码了。先来认识核心框架 **Spring Boot**，它是后面所有行情接入、规则引擎、Agent 查询的代码容器。

## 【正文】

### 一、为什么选 Spring Boot

我们整个团队是专门做 Java 开发的，所有人都在用 Spring Boot 这类核心框架，技术体系以 Spring 为中心。Spring 的能力很广，从官网上可以看到它集成了非常多的内容，尤其是从 Spring 3 开始就整合了 **Spring AI**，在 AI 集成方面有了不小的突破。此外像 **WebFlux**、**Spring Cloud** 等模块也一直被广泛使用。

**Spring Boot 解决的核心痛点**：原生 Spring 时代，搭一个能跑的 Web 工程要手写大量 XML（数据源、事务、MVC、视图解析器……），版本一不对就 `ClassNotFoundException`。Spring Boot 用三条机制把它压平：

- **起步依赖（Starter）**：一个 `spring-boot-starter-web` 就把 Tomcat + Spring MVC + Jackson 等一整套兼容版本拉齐，你不再手动拼依赖树。
- **自动配置（Auto-configuration）**：根据 classpath 上存在的 jar，自动装配合适的 Bean（检测到 `spring-webmvc` 就配 `DispatcherServlet`，检测到 `spring-ai` 就配 `ChatClient` 默认实现），零 XML。
- **内嵌容器 + 可执行 jar**：应用自带 Tomcat，一条 `java -jar` 就能起，天然契合容器化部署。

对「要快速交付一个可部署风控 Bot」的课程目标来说，这三点直接把工程成本砍掉一大半，所以基座选它毫无悬念。

### 二、版本怎么选：4.x 还是 3.5.x

目前 Spring Boot 已经迭代到 **4.0.0** 该全新的大版本。我之前做演示文稿时还是 3.5，现在课程就直接用最新的稳定版 **4.0.0** 来学习和开发。

但版本选择上有几点要提醒：

- **3.5.8（GA）**：是一个比较老牌、稳定的版本，GA（General Availability）意味着正式发布、稳定可用；
- **4.0.0**：当前最新的稳定版，我们课程用它；
- **SNAPSHOT（快照版）** 和 **PRE / M1 之类的预览版**：可以用于本地预览测试，但**不适合生产环境**。我个人觉得 4.0.0 刚出，某些部分兼容性还不够理想，可能还要再迭代两三个版本才会更稳。

关于生命周期：4.0.x 的支持大概到 2027 年 11 月；而 3.5.x 的支持周期相当长，能持续到 2032 年。如果你不想追新，用 3.5.x 也完全没问题，毕竟 4.0 比较新，兼容性还在磨合。

**课程录制版本与配套工程版本的关系（重要）**：课程视频录制时基于 **Spring Boot 4.0.0** 讲解，但本课程的**配套生产级示例工程 `982-demo` 统一钉到了当前稳定版 `4.1.1`**（Spring AI 2.0.1 的推荐基线）。两者同属 4.x 大版本，API 与配置完全兼容，你读 `982-demo/pom.xml` 看到的 `spring-boot-starter-parent` 版本号是 `4.1.1`，这正是「栈锁定」的体现，不追 SNAPSHOT、不混用 3.x 与 4.x。

**大版本选型的工程判断**：4.x 要求 Java 17 起步、Spring Framework 7、Jakarta EE 升级，是一次「现代化大版本」；3.5.x 则是长寿稳定线，支持到 2032。追新（4.x）能早享虚拟线程、Spring AI 2.0 等新能力，但要承担初期兼容性打磨；守旧（3.5.x）最稳，只是部分新特性要等。课程为了演示 Spring AI 2.0 的 `ChatClient` / `@Tool` / Advisor 体系，必须走 4.x。

### 三、系统要求（System Requirements）

翻到官方文档的 System Requirements，Spring Boot 4.0.0 的要求如下：

- **Java 版本**：至少 **Java 17**，兼容到 Java 25。我们课程用的是 **JDK 21**（也是一个稳定版本），最新的 JDK 25 虽然能用，但太新了，没太大必要；
- **构建工具**：
  - **Maven**：3.6.3 或更高（我本地装的是 3.9.0 和 3.9.2，完全够用，只要大于 3.6.3 即可）；
  - **Gradle**：8.x（8.14+）或 9.x，也支持。
- **嵌入式 Servlet 容器**：内置了 **Tomcat、Jetty**（以及 Undertow），这些我们基本不用自己操心；
- **Spring Framework**：至少需要 7.0.1。

虽然有些同事习惯用 Gradle，但我们该项目仍然以 **Maven** 为主（前面几节的环境也是按 Maven 配的）。至于内置的 Tomcat / Jetty，直接拿来用就好，不需要额外处理。

环境这块，上一章我们已经配好了 JDK 21 + Maven，所以到这里我们的 Spring Boot 基础环境就齐活了。下一节课，我们就一步一步把代码框架搭起来。

**为什么 JDK 21 是甜点版本**：17 是 4.x 的底线，但 21 才是「虚拟线程 + Record 模式 + 分代 ZGC」的成熟点。Spring AI 2.0 的工具循环、流式输出大量依赖虚拟线程承载高并发 Agent 调用，所以课程选 21 而非刚好达标的 17。JDK 25 虽新，但生态（部分库尚未适配）和课程可复现性都不如 21 稳，故不追。

**内嵌容器不用操心的含义**：Spring Boot 把 Tomcat 作为默认内嵌容器打进可执行 jar，你不需要单独装 Tomcat、不需要打 `war` 丢进外部容器。这直接服务于「容器化一键部署」，`docker-compose` 里 `java -jar` 起的就是该自带容器的进程（参考 `982-demo/docker-compose.yml` 的 `build: .` + `8080` 暴露）。

### 四、对照真实工程：982-demo 的 pom.xml 长什么样

光看文档不如看真代码。课程配套工程 `982-demo` 的 `pom.xml` 是这样锁定栈的（节选要点）：

- 父工程用 `spring-boot-starter-parent` 的 **4.1.1** 版本，自动带入兼容的 Spring Framework 7 与依赖管理；
- 在 `properties` 里显式写 `java.version=21` 与 `spring-ai.version=2.0.1`；
- 用 `spring-ai-bom` 该 import 类型的依赖管理，把整个 Spring AI 2.0.1 的版本树一次性锁死，避免你手动引错子模块版本；
- 业务依赖只声明「起步依赖」：`spring-boot-starter-web`（Web + Tomcat）、`spring-boot-starter-actuator`（健康检查 / 指标）、`spring-boot-starter-validation`（参数校验）、`micrometer-registry-prometheus`（指标暴露），以及 `spring-ai-starter-model-openai`（Spring AI 2.0.1 的大模型接入起步包）。

这里有一个关键认知：**Spring AI 2.0.1 的开发者 API 与 1.x 完全一致**，你用到的 `ChatClient`、`@Tool`、`MessageChatMemoryAdvisor`、`ToolCallingAdvisor` 这些类名在 2.0 里一字未变，变化的只是底层「工具调用循环」从各 ChatModel 私有实现提升为 Advisor 链一等公民。所以课程里讲到的名词，在 `982-demo` 的工程代码里能一一对应，不会脱节。

### 五、Spring AI 在风控 Bot 里的落点

`982-demo` 用 Spring Boot 4.1.1 的自动配置把 `ChatClient` 装配好，再由业务代码拿来驱动风控查询 Agent。一个最小链路如下：

```mermaid
flowchart LR
    A[REST 请求<br/>GET /api/risk/query] --> B[RiskQueryAgent]
    B -->|ChatClient.prompt| C[大模型<br/>OpenAI / 通义 / DeepSeek]
    B -->|@Tool 工具循环| D[ToolCallingAdvisor]
    D --> E[查行情/判规则<br/>QuoteProvider + RuleEngine]
    C --> B
    B --> F[RiskAlert 结果]
```

`RiskQueryAgent`（`982-demo/src/main/java/com/riskbot/agent/RiskQueryAgent.java`）就是「Spring Boot 自动配置 + Spring AI ChatClient + @Tool 工具挂载」三者结合的具体产物：Spring Boot 负责把它作为 Bean 自动纳入容器，Spring AI 负责把自然语言查询路由到工具循环，最终由 `RuleEngine`（`PriceVolatilityRule` / `VolumeSpikeRule`）给出异动判定。这就是「企业级项目基座」承载 AI 能力的真实形态。

### 六、起步依赖一览（课程相关）

| Starter / 依赖 | 作用 | 课程 / 工程落点 |
|---|---|---|
| `spring-boot-starter-web` | Web MVC + 内嵌 Tomcat | REST 接口（`RiskController`） |
| `spring-boot-starter-actuator` | 健康检查 / 指标端点 | `/actuator/health`、`/actuator/metrics` |
| `spring-boot-starter-validation` | 入参校验 | 风控请求参数校验 |
| `micrometer-registry-prometheus` | Prometheus 指标 | 可观测性 |
| `spring-ai-starter-model-openai` | Spring AI 2.0.1 大模型接入 | `ChatClient` 驱动 `RiskQueryAgent` |
| `resilience4j-*` | 熔断 / 重试 / 限流 | 包裹对外 LLM / 行情调用 |

## 【易错点 / 面试题】

1. **面试题：Spring Boot 的自动配置（Auto-configuration）是怎么工作的？**
   答：Spring Boot 在启动时扫描 classpath 上的 jar，结合 `@ConditionalOnClass` / `@ConditionalOnMissingBean` 等条件注解，按需把合适的 Bean 装配进容器（如检测到 `spring-webmvc` 就配 `DispatcherServlet`）。你只需引入对应的 starter，大部分配置由框架按「约定」完成，无需手写。

2. **面试题：starter 解决了什么问题？**
   答：starter 把「一组兼容版本的相关依赖 + 默认自动配置」打包成一个坐标，你引入一个 `spring-boot-starter-web` 就自动获得 Tomcat + MVC + Jackson 的兼容组合，免去了手动拼依赖、对版本的痛苦，也避免了版本错配导致的运行期异常。

3. **易错点：把课程录制版 4.0.0 和工程版 4.1.1 当成两回事。** 两者同属 4.x，API 兼容；`982-demo` 钉 4.1.1 是栈锁定策略，不是另一套框架。阅读工程时以 `pom.xml` 里的 `4.1.1` 为准。

4. **易错点：用 Java 17 跑需要 21 特性的代码。** 4.x 底线是 17，但课程 / `982-demo` 明确用 21（虚拟线程等），`maven.compiler` 与运行时 JDK 都要 ≥21，否则虚拟线程等 API 编译失败。

5. **易错点：以为 Spring AI 2.0 改了开发者 API。** 2.0 仅把工具循环下沉为 Advisor 链，开发者用的 `ChatClient` / `@Tool` / `MessageChatMemoryAdvisor` 不变。升级时无需改业务代码调用方式。

## 【小结】

这一篇确立了工程基座：Spring Boot 用 starter + 自动配置 + 内嵌容器把「搭工程」的成本压到极低，课程基于 4.x 大版本（录制 4.0.0，配套 `982-demo` 钉 4.1.1），系统要求 Java 17 起、课程用 JDK 21，构建用 Maven 3.6.3+，内嵌 Tomcat 直接服务于容器化。Spring AI 2.0.1 通过 `spring-ai-starter-model-openai` 接入，其 `ChatClient`、`@Tool`、`ToolCallingAdvisor` 等开发者 API 与 1.x 一致，已在 `982-demo` 的 `RiskQueryAgent` 里真实落地。下一节课我们就一步步把代码框架真正搭起来，骨架（3-2 的 `pom` 聚合）之上，Spring Boot 的父子工程与 starter 体系会让我们每一步都「零配置起步」。
