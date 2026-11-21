---
title: "Zipkin 与 Elasticsearch 集成：把追踪数据从易失内存搬进可检索的索引库"
date: 2026-11-18
categories: [Java后端进阶全套, M3 十大中级项目, 阶段十 万信金融项目]
tags: [Java, 项目实战]
---

# Zipkin 与 Elasticsearch 集成：把追踪数据从易失内存搬进可检索的索引库

Sleuth 与 Zipkin 集成测试跑通之后，9411 端口的 UI 上已经能看到完整调用链，但这里藏着一个容易被忽视的隐患：Zipkin 采集到的监控数据默认存在内存里。服务进程一重启，或者 Zipkin 挂掉一次，之前采集的所有数据就全部清零。要排查一个三天前才复现的问题时打开 UI 发现历史链路早没了，这套追踪系统就只剩一半价值。解决思路很直接：给 Zipkin 换一个持久化存储。

## 先给结论

- Zipkin 默认把监控数据存在内存中，服务重启或崩溃都会导致数据全部丢失，生产环境必须换成持久化存储。
- Zipkin 提供可插拔的存储方式：In-Memory、MySQL、Cassandra、Elasticsearch；本课选择 Elasticsearch，看重的是它作为全文检索引擎的查询性能。
- 集成只需两步：准备好 Elasticsearch（版本不要超过 6.0）与 head 插件，然后给 Zipkin 的启动命令追加两个参数指定存储类型与 ES 地址。
- 核心启动命令：`java -DSTORAGE_TYPE=elasticsearch -DES_HOSTS=http://localhost:9200 -jar zipkin-server-2.12.9-exec.jar`。
- 验证方式：发起几次跨服务请求，在 es-head（9100 端口）里能看到 Zipkin 自动创建的索引，浏览数据可以看到 traceId、spanId、parentId、时间戳、服务名等完整追踪字段。

## 为什么持久化是刚需

**第一，内存存储撑不起排查场景。** 问题排查最常见的需求是回看历史：这次请求慢了，上一次同样接口的表现如何？这批异常是今天才出现的还是上周就有苗头？数据放在内存里，Zipkin 进程一退出这些答案就跟着消失，只有最新采集的数据可看，历史分析无从谈起。

**第二，存储方案本身是可插拔的。** Zipkin 把存储抽象成了组件，换存储不影响客户端上报逻辑，微服务侧一行代码都不用改。MySQL、Cassandra、Elasticsearch 都在官方支持之列。课程选择 Elasticsearch 的理由有两点：它作为全文检索工具查询效率非常高，适合追踪数据这种以查询为主的场景；它与 Zipkin 的集成极其简单，两个启动参数就能搞定。

需要注意一个版本约束：Elasticsearch 的版本不要超过 6.0。Zipkin 对较新版本的 ES 适配支持还不好，版本太高集成会失败。课程资料里提供了 Elasticsearch 5.6.16 的安装包，直接使用即可。

```mermaid
flowchart LR
    A["service-a"] -->|"追踪日志"| Z["Zipkin服务端"]
    B["service-b"] -->|"追踪日志"| Z
    Z -->|"STORAGE_TYPE=elasticsearch"| E["Elasticsearch 5.6.16"]
    E --- H["es-head 插件 9100"]
```

这张图在讲数据流向的完整变化。解读关键路径：业务服务照旧把追踪日志上报给 Zipkin，变化发生在 Zipkin 落盘这一环，存储从内存换成了 Elasticsearch，es-head 作为 ES 的可视化前端负责观察索引数据。

## 集成步骤：两个启动参数

前提是手头已有运行中的 Elasticsearch 和它的 head 插件，这两样属于环境准备，配置方法在之前的 ES 课题里已经讲过。集成 Zipkin 本身只有一件事：换一种方式启动 Zipkin 服务端。

以前启动 Zipkin 用的是 `java -jar zipkin-server-2.12.9-exec.jar`，现在要在前面追加两个 `-D` 参数：

```bash
java -DSTORAGE_TYPE=elasticsearch -DES_HOSTS=http://localhost:9200 -jar zipkin-server-2.12.9-exec.jar
```

两个参数的含义一目了然。

- `STORAGE_TYPE` 指定存储类型，取值 `elasticsearch`，告诉 Zipkin 采集到的数据要持久化到哪里，如果想存 MySQL 就换成对应的取值。
- `ES_HOSTS` 指定 Elasticsearch 服务器的地址列表，本机演示就是 `http://localhost:9200`，9200 是 ES 的默认端口；集群有多个节点时用逗号分隔多个地址。

参数就位之后正常启动，控制台没有报错即为成功。此时 Zipkin 已经知道采集到数据该往哪儿送，后续的上报、存储全部自动完成，微服务侧无需任何改动。

命令里有两个实操层面的小坑值得提前交代。一个是 `-D` 参数与值之间不要加空格，`-DES_HOSTS=http://localhost:9200` 要连在一起写，写成 `-D ES_HOSTS=...` 在部分终端里会导致参数解析失败；另一个是从 PDF 讲义复制命令时空格与换行容易丢失横杠，启动报「无法访问 jarfile」时先检查 jar 包文件名和参数有没有被复制走样。

## 集成测试：从发请求到看索引

测试环境按依赖顺序起：Elasticsearch 先启动，观察控制台确认无报错；head 插件是一个前端工程，进入 elasticsearch-head 目录用 `npm run start` 拉起来，跑在 9100 端口；最后用上面的命令启动 Zipkin 服务端。

测试前还要处理一个遗留问题：上一课为了验证异常链路在服务 B 的 Controller 里埋了一句除零代码，这次测试要保证代码是正常的，把那行注释掉并重启服务 B：

```java
@GetMapping("service")
public String service() {
    // int i = 1 / 0; // 注释掉除零异常 恢复正常链路
    String service = serviceAgent.service();
    return "service-b-service" + "===" + service;
}
```

接着清空 service-a 的控制台，浏览器访问 `http://localhost:58021/service-a/service1`，让链路产生几次请求。观察数据不进 Zipkin 的 UI，而是打开 es-head：刷新后索引列表里多出了名字带 zipkin 的索引，里面躺着刚采集到的 5 条数据。

浏览这些文档，能看懂的字段非常多：traceId 与 spanId 构成链路标识，parentId 记录调用层级，timestamp 是时间戳，还有请求类型（GET）以及涉及到的微服务名 service-a、service-b。说白了，Zipkin UI 上图形化展示的那些数据，现在以文档形式全部落到了 Elasticsearch 里，这就是持久化存储。数据进了索引库，就再也不用担心 Zipkin 重启把它们弄丢，任何时候都能查询历史链路。

## 内存态与 ES 态的行为差异

换存储之后，客户端上报链路完全不变，变化都在服务端内部，但有两个行为差异要心里有数。

**第一，数据可见的时机取决于写入节奏。** Zipkin 客户端上报是异步的，服务端写入 ES 也有一小段延迟，发起请求后立刻去 es-head 刷新可能还看不到索引或文档，稍等片刻再查是正常现象，不要据此误判集成失败。

**第二，依赖分析功能会失效，这是下一课的主角。** Zipkin 的依赖分析默认从内存读数据做分析，数据一旦搬进 ES，内存里空空如也，依赖图就点不出来了。这个问题有专门的工具解决，即 zipkin-dependencies，它在依赖分析一课展开。

## 常见误区

- **以为要升级到最新的 Elasticsearch 才好。** 错例：装了 ES 7.x 再来接 Zipkin，集成失败排查半天。正解：这个版本的 Zipkin 对较新的 ES 适配不佳，版本不要超过 6.0，课程提供的 5.6.16 直接可用。
- **以为集成要在微服务里改代码或加依赖。** 错例：去每个微服务的 pom 里找「ES 存储的依赖」。正解：存储是 Zipkin 服务端的事，只改启动命令，客户端侧零改动。
- **以为 `-D` 参数写法随意。** 错例：从讲义复制命令时写成 `-D ES_HOSTS=...` 或横杠丢失，启动报无法访问 jarfile。正解：参数紧跟 `-D` 不加空格，粘贴后先检查命令完整再回车。
- **以为数据进 ES 后依赖图还在。** 错例：集成 ES 后点依赖菜单发现空白，以为出了故障。正解：依赖分析默认读内存数据，ES 集成后需借助 zipkin-dependencies 工具重新分析，属预期行为。

## 面试可能被问到的问题

1. 面试官追问：「Zipkin 的监控数据默认存在哪里，有什么问题？」
   答：默认存在内存中，Zipkin 服务重启或挂掉数据就会全部丢失，无法支撑历史链路排查。生产环境要用它提供的可插拔存储换成持久化方案，如 MySQL、Cassandra 或 Elasticsearch。
2. 面试官追问：「你们为什么选 Elasticsearch 作为 Zipkin 的存储？」
   答：一是 ES 作为全文检索引擎查询性能好，适合追踪数据以查询为主的场景；二是与 Zipkin 集成成本极低，启动命令加 STORAGE_TYPE 和 ES_HOSTS 两个参数即可，微服务侧不用改任何代码。
3. 面试官追问：「集成 ES 存储具体怎么做？」
   答：准备好 Elasticsearch（版本不超过 6.0），启动 Zipkin 时追加 java -DSTORAGE_TYPE=elasticsearch 和 -DES_HOSTS 指定 ES 地址列表，多个节点逗号分隔。启动后 Zipkin 自动创建索引并写入追踪数据。
4. 面试官追问：「怎么验证追踪数据真的存进了 ES？」
   答：先发起几次跨服务请求产生追踪数据，再通过 es-head 插件（9100 端口）查看索引列表，能看到 Zipkin 创建的名字带 zipkin 的索引，浏览文档可见 traceId、spanId、parentId、时间戳、服务名等字段。
5. 面试官追问：「数据存进 ES 后，Zipkin 的依赖分析为什么用不了？」
   答：依赖分析功能默认从内存读取数据进行分析，数据存储切到 ES 后内存里没有数据，依赖图自然空白。官方提供 zipkin-dependencies 工具从 ES 等数据源读取数据完成依赖分析，需要单独运行。

## 配套资料

- 讲义：`materials/docs/10/服务调用链路追踪.md`，「3.3 Zipkin&Elasticsearch 集成」章节（持久化背景、集成步骤、STORAGE_TYPE 与 ES_HOSTS 参数说明、集成测试全过程）。
- 说明：本课无独立源码包，除注释除零代码的服务 B 方法为入门案例原码外，命令与验证步骤均以讲义口径为准；案例工程结构沿用 `materials/docs/10/服务调用链路追踪.md` 中 Sleuth 与 Zipkin 集成章节的入门案例，包名按 `com.study.finance` 系改写。
