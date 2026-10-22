# 9. SpringAI 集成 DeepSeek：同步调用、流式输出与调用耗时统计

## 纲要

- **本章目标**：把大模型真正接入 Spring Boot 工程——先 DeepSeek 同步调用，再升级流式输出，最后用 AOP + StopWatch 做调用耗时统计
- **依赖引入**：父 `pom` 用 `dependencyManagement` 锁 `spring-ai-bom:1.0.0`，子模块加 `spring-ai-starter-model-openai`（注意 1.0 坐标改名，老 `spring-ai-openai` 已废弃）
- **配置三件套**：`spring.ai.openai.api-key` / `base-url` / `chat.options.model`（DeepSeek 兼容 OpenAI 协议，base-url 用 `https://api.deepseek.com`）
- **两种调用**：`call().content()` 同步返回字符串；`stream().content()` 返回 `Flux<String>` 流式逐字输出
- **提示词三类**：`system`（角色设定）/ `user`（用户输入）/ `assistant`（模型返回），本章重点用 system 设定「拉狗狗」助手
- **耗时统计**：AOP 环绕切面切 `service` 包通用统计；StopWatch 多任务分段计时更优雅
- **中文乱码**：Controller 里 `response.setCharacterEncoding("UTF-8")`，否则流式中文变乱码

> 本章代码基于课程标准工程（`com.itzixi` 包）按 SpringAI 1.0 API 重构，外部代码卷暂未挂载，重挂后可切换为逐文件提取的真实代码。

## 一、为什么先做「集成」这一课

前述把 mcp-client 工程跑起来了，但还只是空壳 Web。从本章起，工程才真正拥有「大脑」——能调大模型回答用户问题。课程老师原话：「前述把 web 跑通，这一章正式进入集成大模型环节。」先做 DeepSeek（国内可达、便宜），再换通义千问，后面章节再叠加 RAG / MCP / 联网搜索。

## 二、依赖引入（SpringAI 1.0 关键坑）

### 2.1 父 pom 用 dependencyManagement 锁版本

课程在前面 pom 里加了一段 `spring-ai-bom`（老师说是 `dependencyManagement`，和父 pom 的父子关系一致，统一管理版本）：

```xml
<!-- 父 pom 或根 pom -->
<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>org.springframework.ai</groupId>
      <artifactId>spring-ai-bom</artifactId>
      <version>1.0.0</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
  </dependencies>
</dependencyManagement>
```

### 2.2 子模块加 starter（注意 1.0 坐标改名）

```xml
<dependencies>
  <dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-model-openai</artifactId>
    <!-- 版本由 bom 统一管理，这里不写 version -->
  </dependency>
</dependencies>
```

> ⚠️ **坐标改名坑**：老师强调「Spring 这次改了包名，原来是 `spring-ai-openai`，现在叫 `spring-ai-starter-model-openai`」。以往坐标名一般不改，这次特例。用错坐标直接拉不到包。当前 SpringAI 官方稳定版是 `1.0.0`，早期有过 `snapshot` 预览版，包结构差异大，**锁定 1.0.0 不要用快照**。

## 三、application.yml 配置（DeepSeek 三件套）

```yaml
spring:
  ai:
    openai:
      api-key: sk-你的deepseek密钥
      base-url: https://api.deepseek.com
      chat:
        options:
          model: deepseek-chat
```

| 配置项 | 含义 | 课程取值 |
|---|---|---|
| `api-key` | 大模型密钥 | DeepSeek 开放平台创建的 key（课程充了 10 块，够用很久） |
| `base-url` | 网关地址（请求发往哪） | `https://api.deepseek.com`（接口文档里复制） |
| `chat.options.model` | 模型名 | `deepseek-chat`（对话模型）；`deepseek-reasoner` 是推理模型、`deepseek-coder` 是编码模型 |

> 老师原话：「DeepSeek 有几种类型——`deepseek-chat` 普通对话、`deepseek-reasoner` 推理大模型、`deepseek-coder` 编码输出。我们用 `deepseek-chat`。」申请路径：DeepSeek 开放平台 → 左侧 API keys → 创建（课程命名为 `spring-AI实战`）→ 复制密钥。

## 四、ChatClient 构建与系统提示词

### 4.1 定义 Service 接口

```java
// com.itzixi.service.ChatService
package com.itzixi.service;

public interface ChatService {
    /** 测试大模型交互聊天（同步） */
    String chatTest(String prompt);
}
```

### 4.2 实现类：构造器注入 ChatClient + 设 system 提示词

```java
// com.itzixi.service.impl.ChatServiceImpl
package com.itzixi.service.impl;

import com.itzixi.service.ChatService;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.stereotype.Service;

@Service
public class ChatServiceImpl implements ChatService {

    private final ChatClient chatClient;

    // 构造器注入：SpringBoot 自动配置 ChatClient.Builder
    public ChatServiceImpl(ChatClient.Builder builder) {
        this.chatClient = builder
                .defaultSystem("你是一个非常聪明的人工智能助手，可以帮我解决很多问题。我为你取个名字，你叫'拉狗狗'。")
                .build();
    }

    @Override
    public String chatTest(String prompt) {
        return chatClient.prompt(prompt).call().content();
    }
}
```

> 老师讲两种写法：直接把 system 串写进 `defaultSystem(...)`，或抽成 `private static final String SYSTEM_PROMPT = "...";` 再引用，后者更直观。构造器注入是老师推荐方式——SpringBoot 自动注入 `ChatClient.Builder`，默认走 OpenAI 规范模型。

### 4.3 Controller 测试

```java
// com.itzixi.controller.HelloController（追加方法）
@Resource
private ChatService chatService;

@GetMapping("/hello/chat")
public String helloChat(@RequestParam String message) {
    return chatService.chatTest(message);
}
```

启动后访问 `http://localhost:8080/hello/chat?message=你是谁` → 返回「我是拉狗狗，你的智能助手…」。把 system 提示词改成「家庭医生 / 架构师」等任意角色，模型就扮演对应角色——这就是**提示词工程**的雏形。

## 五、流式输出（Flux）与提示词三类

### 5.1 同步 vs 流式

同步 `call()` 要等模型整段生成完才返回（复杂问题等 1–2 分钟，体验差）；流式 `stream()` 像 DeepSeek / 通义千问网页那样「几个字几个字蹦出来」，体验好得多。

```java
// Service 新增流式方法
public Flux<String> chatStreamStr(String prompt) {
    return chatClient.prompt(prompt).stream().content();   // 逐字 Flux<String>
}

// 想要完整响应对象则用（信息量大，一般不直接丢前端）
public Flux<ChatResponse> chatStreamResponse(String prompt) {
    return chatClient.prompt(prompt).stream().chatResponse();
}
```

```java
// Controller
@GetMapping(value = "/hello/chatStreamStr", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
public Flux<String> chatStreamStr(@RequestParam String message, HttpServletResponse response) {
    response.setCharacterEncoding("UTF-8");   // ⚠️ 关键：否则中文乱码
    return chatService.chatStreamStr(message);
}
```

> 老师实测：`chatStreamResponse` 返回的是 `ChatResponse` 对象，里面数据量巨大（JSON 很长），一般不直传前端；`chatStreamStr` 只返回文字流，更干净。但流式默认中文乱码——必须在 Controller 里 `response.setCharacterEncoding("UTF-8")`，上面那个方法也要加，否则英文正常、中文乱码。

### 5.2 提示词三大类型（重点）

老师在本节拓展讲解，提示词分三种角色：

| 类型 | 含义 | 谁来写 |
|---|---|---|
| **system** | 系统提示词，定义模型角色/规则（如「你叫拉狗狗」） | 开发者写，每次调用都带 |
| **user** | 用户输入（如「你是谁」「帮我写菜谱」） | 用户写 |
| **assistant** | 模型最终返回的内容 | 模型写，我们无法定义 |

> `ChatResponse` 里的 `messageType=assistant` 就是模型返回角色。system + user 可自定义，assistant 不可控。理解三类是后续做 RAG / 多轮对话的基础。

## 六、AOP 环绕切面统计 LLM 调用耗时

每次手写在方法里算时间差太粗暴。Spring 天生面向切面，用 `@Around` 切 `service` 包统一统计。

### 6.1 引入 AOP 依赖

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-aop</artifactId>   <!-- 在 spring-boot 下，非 AI 包 -->
</dependency>
```

### 6.2 切面类

```java
// com.itzixi.aspect.TimeLogAspect
package com.itzixi.aspect;

import lombok.extern.slf4j.Slf4j;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.stereotype.Component;

@Aspect
@Component
@Slf4j
public class TimeLogAspect {

    // 切点：com.itzixi 包及其子包下 service 中任意类的任意方法、任意参数
    @Around("execution(* com.itzixi..service..*(..))")
    public Object recordTimeLog(ProceedingJoinPoint joinPoint) throws Throwable {
        long beginTime = System.currentTimeMillis();
        // 执行被切的方法
        Object result = joinPoint.proceed();
        long takeTime = System.currentTimeMillis() - beginTime;

        String className = joinPoint.getTarget().getClass().getName();
        String methodName = joinPoint.getSignature().getName();

        if (takeTime > 3000) {
            log.error("切点【{}.{}】耗时偏长：{} ms", className, methodName, takeTime);
        } else if (takeTime > 2000) {
            log.warn("切点【{}.{}】耗时中等：{} ms", className, methodName, takeTime);
        } else {
            log.info("切点【{}.{}】耗时：{} ms", className, methodName, takeTime);
        }
        return result;   // 必须抛出原结果
    }
}
```

**execution 表达式拆解**（老师逐段讲解）：

```
execution(* com.itzixi..service..*(..))
         │   │          │      │  │
         │   │          │      │  └ 任意参数
         │   │          │      └ 任意方法名
         │   │          └ 当前包及子包下任意类
         │   └ 包名 com.itzixi
         └ 任意返回类型
```

> 老师提醒：`..` 表示包及子包（后续加 `sub.xxx` 子包也能切到）；`*` 分别代表返回类型、类、方法名；`(..)` 任意参数。表达式写错时 IDEA 里那个切点标记（m 开头）点不动，正确时会列出被切的方法并能跳转，说明切面生效。

> 注意：流式调用本身异步很快（实测 14ms），为了让切面能测出耗时，老师临时加了 `Thread.sleep(6000)` 演示——真实场景不必加，只是为了让日志进「耗时偏长」分支。大模型返回默认 **markdown 格式**，后续转 HTML。

## 七、StopWatch 优雅分段计时（升级版）

`System.currentTimeMillis()` 相减不够优雅。Spring 自带 `StopWatch` 秒表，支持**多任务列表 + 时间占比**，适合一个方法内多业务块分别计时。

```java
// com.itzixi.test.TimeTest
@SpringBootTest
public class TimeTest {

    @Test
    public void test() throws InterruptedException {
        StopWatch sw = new StopWatch();

        sw.start("任务一");
        Thread.sleep(1000);
        sw.stop();

        sw.start("任务二");
        Thread.sleep(300);
        sw.stop();

        sw.start("任务三");
        Thread.sleep(100);
        sw.stop();

        System.out.println(sw.prettyPrint());      // 列表形式 + 占比
        System.out.println(sw.shortSummary());     // 简短统计
        System.out.println("所有任务总耗时：" + sw.getTotalTimeMillis());
        System.out.println("任务总数：" + sw.getTaskCount());
    }
}
```

输出示例：

```
StopWatch '': running time = 1402353200 ns
---------------------------------------------
ns         %     Task name
1402353200  100%  任务一
...
所有任务总耗时：1402
任务总数：3
```

> 老师比喻：「就像运动场跑步，三个哥们儿轮流跑，摁一下秒表暂停、再启动、再暂停。」`prettyPrint()` 出列表+百分比，`shortSummary()` 简短，`getTotalTimeMillis()` 总耗时，`getTaskCount()` 任务数。把 StopWatch 搬进切面：`takeTime = sw.getTotalTimeMillis()` 替换原来手算的时间差，更优雅。

> `@SpringBootTest` 包名要和启动类一致（`com.itzixi`），否则报「未指定」错；不一致就在注解加 `classes = 启动类.class` 显式指定。

## 八、关联代码文件（本章重构）

| 文件 | 作用 |
|---|---|
| `mcp-client/pom.xml` | 加 `spring-ai-starter-model-openai` + `spring-boot-starter-aop` |
| `mcp-client/src/main/resources/application.yml` | `spring.ai.openai` 三件套配置 |
| `mcp-client/src/main/java/com/itzixi/service/ChatService.java` | 聊天接口 |
| `mcp-client/src/main/java/com/itzixi/service/impl/ChatServiceImpl.java` | ChatClient 构建 + 同步/流式实现 |
| `mcp-client/src/main/java/com/itzixi/controller/HelloController.java` | `/hello/chat` `/hello/chatStreamStr` 测试端点 |
| `mcp-client/src/main/java/com/itzixi/aspect/TimeLogAspect.java` | AOP 环绕切面统计耗时 |
| `mcp-client/src/test/java/com/itzixi/test/TimeTest.java` | StopWatch 演示 |

## 九、FAQ

**Q1：spring-ai-starter-model-openai 和老的 spring-ai-openai 区别？**
1.0 正式版改名，老坐标已废弃。必须用 `spring-ai-starter-model-openai`，且版本由 `spring-ai-bom:1.0.0` 统一管理，别混用 snapshot。

**Q2：ChatClient.Builder 哪来的？**
SpringBoot 自动配置在你引入 starter 后注入 `ChatClient.Builder` Bean，构造器接收即可，不用自己 new。

**Q3：流式中文乱码怎么解？**
Controller 方法参数加 `HttpServletResponse response`，调 `response.setCharacterEncoding("UTF-8")`；非流式端点同理。

**Q4：Flux<ChatResponse> 和 Flux<String> 选哪个？**
前端只显示文字用 `Flux<String>`（`.stream().content()`）；需要完整元数据（角色、用量）才用 `Flux<ChatResponse>`，但别直接序列化丢前端，太大。

**Q5：AOP 切点表达式写错有何现象？**
IDEA 里切点标记点不动、无法跳转到被切方法；写对后标记可点、能双向跳转。

**Q6：StopWatch 和 AOP 手算时间差怎么选？**
单方法多业务块分段计时用 StopWatch（带占比）；统一横切所有 service 方法用 AOP 更省事。两者可结合：AOP 内用 StopWatch 算时间。

**Q7：大模型返回为什么是 markdown？**
DeepSeek / 通义千问默认输出 markdown，方便在网页渲染。后续用工具把 markdown 转 HTML 再返前端。

## 十、面试高频问答

**1. SpringAI 如何统一管理大模型版本？**
用 `spring-ai-bom` 的 `dependencyManagement` 锁版本，各 starter 不写 version；切换模型（DeepSeek/Qwen）只改 starter 与 yml，不动业务代码。

**2. 同步调用与流式调用的区别与适用场景？**
同步 `call()` 整段返回，适合后台批处理；流式 `stream()`（`Flux<String>`）逐字推送，适合聊天 UI 提升体验。流式需处理编码（UTF-8）与背压。

**3. 提示词 system/user/assistant 各自作用？**
system 设定模型角色与规则（每次都带）、user 是用户输入、assistant 是模型返回；system+user 自定义，assistant 不可控。RAG/多轮对话都基于三类组合。

**4. AOP 环绕通知如何统计方法耗时？**
`@Around("execution(...)")` 内记录 `begin = System.currentTimeMillis()`，`joinPoint.proceed()` 执行原方法，再算差值；注意必须 `return proceed()` 的结果，否则切断返回值。

**5. StopWatch 相比 currentTimeMillis 差值的优势？**
支持多任务分段、自动算时间占比与总耗时、任务数，输出 `prettyPrint()` 直观，便于性能调优；手算只能得单次差值。

**6. 为什么大模型配置要外置（为第 5-B 章铺垫）？**
密钥/网关写死 yml 不便切换模型且易误提交；外置 `.env` + 表达式注入更灵活安全，契合 12-Factor 配置原则。

## 十一、ChatModel 底层 API 对照（进阶）

`ChatClient` 是 SpringAI 1.0 的高级封装，底层是 `ChatModel` + `Prompt` + `ChatResponse`。理解底层有助于定制：

```java
@Resource
private ChatModel chatModel;   // OpenAiChatModel 实现

// 手工拼消息
Message system = new SystemMessage("你叫拉狗狗");
Message user = new UserMessage("你是谁");
Prompt prompt = new Prompt(List.of(system, user));
ChatResponse response = chatModel.call(prompt);
String text = response.getResult().getOutput().getContent();
```

| 维度 | ChatClient（高级） | ChatModel（底层） |
|---|---|---|
| 写法 | 链式 `builder().defaultSystem().build()` | 手工 `new Prompt(messages)` |
| 流式 | `.stream().content()` | `chatModel.stream(prompt)` 返回 `Flux<ChatResponse>` |
| 适用 | 业务快速接入 | 需要精细控制消息/元数据 |

> 课程全程用 `ChatClient`；底层 `ChatModel` 在要做消息历史、函数调用等精细操作时更灵活，后面章节会用到。

## 十二、错误处理：超时 / 重试 / 降级

生产调用大模型必须兜底，否则一个超时拖垮整条链路：

```yaml
spring:
  ai:
    openai:
      chat:
        options:
          model: deepseek-chat
# 超时（spring-ai 1.0 通过底层 HttpClient 配置，示例思路）
```

```java
try {
    return chatClient.prompt(p).call().content();
} catch (Exception e) {
    log.error("大模型调用失败", e);
    return "抱歉，服务暂时不可用";   // 降级文案
}
```

- **超时**：在 starter 的 HttpClient 配置 `connect/read timeout`（如 30s），避免无限等待。
- **重试**：用 Spring Retry（`@Retryable`）或 Resilience4j，对 429/5xx 指数退避。
- **降级**：捕获异常返回兜底话术，配合 AOP 切面（本章第六节）统一织入。

> 老师强调大模型「复杂问题可能等 1–2 分钟」，超时设太短会误杀长思考（reasoner）模型，按模型特性调。

## 十三、结构化输出（Structured Output）

让模型直接返回 Java 对象而非自由文本，下游好处理：

```java
public record ProductInfo(String name, double price, int stock) {}

ProductInfo info = chatClient.prompt("抽取商品：iPhone16 5999元 库存10")
    .call()
    .entity(ProductInfo.class);   // 1.0 直接 .entity(类)
```

> SpringAI 底层用 `BeanOutputConverter` 把 JSON 强转目标类。适合做「自然语言 → 结构化数据」的预处理（为前述自然语言查库铺垫）。

## 十四、多轮对话与 Message 历史

单轮 `prompt(String)` 无记忆；多轮需自己维护 `List<Message>`：

```java
List<Message> hist = new ArrayList<>();
hist.add(new SystemMessage("你是拉狗狗"));
hist.add(new UserMessage("我叫小明"));
hist.add(new AssistantMessage("你好小明"));
hist.add(new UserMessage("我刚说我叫什么"));
ChatResponse r = chatModel.call(new Prompt(hist));  // 模型记得「小明」
```

> 真要多轮记忆，需把每轮 user/assistant 落库或存 session（Redis），不然重启即失忆。这是对话系统的核心，后续可结合 Redis做会话存储。

## 十五、函数调用预览（为 MCP 铺垫）

大模型本身不能查库/调 API，靠「函数调用」把能力交给模型决定何时调用：

```java
@Bean
public FunctionCallback weatherFn() {
    return FunctionCallback.builder()
        .description("查询天气")
        .function("weather", (WeatherRequest r) -> "晴 26℃")
        .build();
}
// 调用时把 callback 注册进 ChatClient，模型自主决定调用
```

> 这正是前述 MCP 的雏形——MCP 把「函数」标准化成跨进程的「工具」。理解函数调用，前述一看就懂。

## 十六、Token 估算与成本控制

- **Token ≈ 字数 × 1.5**（中英文混合）。DeepSeek / 通义千问按输入+输出 token 计费。
- **缓存**：相同 system 提示词可缓存（部分厂商支持 `cache`）省输入费。
- **限流**：`chat.options` 控制 `max-tokens`、`temperature`；高频场景加本地限流器。
- **监控**：用本章 AOP 切面统计调用次数+耗时，结合日志算账单。

> 上线前务必评估：并发 × 平均 token × 单价，设预算告警，防刷爆。

## 十七、ChatClient 请求可观测与常见异常

### 17.1 看清发出去的请求

排查「模型答非所问 / 没带 system」时，打开 SpringAI 的 HTTP 日志看实际 payload：

```yaml
logging:
  level:
    org.springframework.ai.chat.client: DEBUG
    org.springframework.web.client: DEBUG
```

> 把 `ChatClient` 与 `RestClient` 日志开 DEBUG，能看到最终拼出的 messages、model、temperature，验证 system 是否生效。

### 17.2 常见异常速查

| 异常/HTTP | 含义 | 处理 |
|---|---|---|
| **401 Unauthorized** | key 错 / 没覆盖进 `.env` | 重填 key，确认 `System.setProperty` 路径（第 5-B 章） |
| **404 Not Found** | base-url 多了 `/v1` 或路径错 | 查 base-url（通义千问去 `/v1`） |
| **429 Too Many Requests** | 限流 | 退避重试、降并发 |
| **500 / 超时** | 模型侧抖动 / 网络 | 重试 + 降级文案 |
| **No qualifying bean ChatClient.Builder** | starter 没引入 / 版本错 | 确认 `spring-ai-starter-model-openai` + bom 一致 |
| **中文乱码** | 流式没设 UTF-8 | Controller `setCharacterEncoding("UTF-8")` |

### 17.3 工程结构回顾（衔接前述）

```
mcp-client/
├── pom.xml                      # spring-ai-starter-model-openai + aop
├── src/main/java/com/itzixi/
│   ├── Application.java         # 启动类（5-B 加载 .env）
│   ├── controller/HelloController.java
│   ├── service/ChatService.java + impl/ChatServiceImpl.java
│   └── aspect/TimeLogAspect.java
├── src/main/resources/
│   ├── application.yml          # ${OPENAI_*} 表达式
│   ├── .env / deepseek.env / qwen.env
└── src/test/java/com/itzixi/test/TimeTest.java
```

> 前述搭的空壳，本章填入「大脑」。后续前述把流式接到前端，第 7–9 章叠加 RAG / 联网 / MCP。

## 十八、ops 提示（安全与网络）

> **密钥是红线**：`api-key` 绝不硬编码进 git；
>
> **base-url 网络**：国内直连 `api.deepseek.com` 通常可达；若公司网络限制，走代理或服务器部署。课程老师强调「保证网络畅通」。
>
> **模型计费**：DeepSeek / 通义千问按 token 计费，开发期用量小；上线前评估并发与缓存（如相同 prompt 缓存），控制成本。
>
> **流式端点**：`produces = TEXT_EVENT_STREAM_VALUE` 让前端按 SSE 消费；前端用 `EventSource` 接收逐字流。

