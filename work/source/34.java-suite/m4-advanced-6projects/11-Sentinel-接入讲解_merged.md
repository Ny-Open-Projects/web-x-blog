# 11-Sentinel-接入讲解 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

我们开始讲解Sentier的使用

Sentier的使用这一块

我们将只围绕着我们项目中用的知识点来讲解

像一些基础操作

一些基础知识

我们就不去讲解了

这一块工程我们就不再手动搭建

直接将已经准备好的工程导入进来就可以了

在这一块给大家准备了一个工程

叫Sentier的工程

把它导入到我们当前Ideal里面

就可以直接去使用了

这个工程是一个非常简单的案例

里面提供了生产者

消费者

以及微服网关这一块

那等会儿我们将围绕着这几点来讲解了

首先我们来讲解一下

项目如何接入到Sentier里面去

第一个步骤要先引入依赖包

第二个步骤要开启我们Fend的一个支持

是Sentier对Fend的一个支持

还有一个是我们这一块

一会儿要开启我们的Sentier

我们要连接哪一个

这个是我们对应的Sentier的控台

哪一个Sentier的控台

同时要指定一个数据交换的一个端口

这就是彼此之间进行数据通信的端口

行

在这一块我们把它给拷贝过来

先把这个依赖包给拷贝过来

在这一块的这个依赖包呢

已经有了在上面这里

因为它是咱消费者

它这里要有那个包

这就是我们Sentier对应的包

包有了之后

紧接着我们开始做另外一个事

就是要配置一下它连接我们Sentier的控台

以及和Sentier之间进行一个数据通信的端口号

这一块呢我们把配置文件打开

在这里我们先来配置第一个

就是连接Sentier控台的地址信息

配置

好怎么配置呢

这一块我们就直接从这里接近过来就行了

拷到这个Sentier的这里就行了

OK

第一个端口我说过是通信端口

第二个端口我说过

是不是咱们当前控台的一个IP加端口啊

那这一块不要搞错IP了哈

好这一块一写之后就搞定了

我们等会还要去集成我们的份来一起使用

那集成份来使用的话

我们得

开启份让份这一块对我们当前Sentier进行一个支持

这一块拷过来就行了

好拷到这里

行

那目前这一块就算正式接入到咱们当前Sentier的控台了

我们来启动一下测试

看看效果如何启动一次

在这里呢

有这么几个方法哈

第一个方法是什么呢

第一个方法是GET1

第二个是叫ONE

我们现在来访问一下第二个

这个UE MAX

我们来访问一下

这个是18082

UE

我们看一下是不是UE哈

UE加上一个MAX

上面这里是一个Consumer

对吧

我们来把Consumer写上去

MAX来个9回车一次

哎

那这一块是不是就报出来

我们看一下看这一块报出了啊

UE9没错吧

看一下啊

必须是一个数字

这个错误就有点奇怪

对不对

我们看这里写的是GETMAPPINGUE对吧

Consumer

UE

Path variable

这个多个斜杠

对不对

来我们重新启动一下

好

我们再来进行测试一次

看现在这一块如何

行

来重新测试

这是没有问题的

对不对

这个确实没有问题

我们看它在身体论里面是怎么展示的

看有没有接入进去啊

因为刚才这里我是不是访问过很多次啊

他应该接入到身体论里面去了才对

来哎

这一块有个Consumer是不是多了个服务啊

多了个服务呢

很明显

这一块就是咱当前这一个服务Consumer

你看这里还有实时监控

这刚才请求的一个流量信息

我们可以疯狂刷新

流量也在跟着一起变

大家可以看一下啊

这是这个流量信息啊

是这一块哈

那我们这一块就接入到了咱们的一个身体论里面了

那怎么接入的呢

两个步骤

第一个先引入一代包

第二个配置一下身体的一个地址以及通信端口就行了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于 **Spring Cloud Alibaba Sentinel** 的技术教程，主要讲解如何在 **Feign 消费者服务** 中集成 Sentinel 进行流量控制和降级。讲师通过演示一个名为 `consumer` 的 Spring Boot 项目，展示了如何在 `pom.xml` 中添加依赖、在 `bootstrap.yml` 中配置 Sentinel 控制台地址和 Feign 支持，以及如何在代码中定义降级逻辑。视频的目的是让开发者理解 Sentinel 如何与 Feign 集成，并在服务调用失败时提供降级响应。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开头，讲师展示了课程大纲，当前章节为“3.3.1 基于Feign的服务降级”，并切换到文件资源管理器，准备下载 Sentinel 控制台的 JAR 包。
*   **00:05 - 00:15**: 讲师在 `consumer` 项目的 `pom.xml` 文件中，演示如何添加 `spring-cloud-starter-alibaba-sentinel` 依赖。
*   **00:15 - 00:25**: 讲师在 `bootstrap.yml` 文件中配置 Sentinel，包括 `transport.port` 和 `dashboard` 地址，并开启 Feign 对 Sentinel 的支持。
*   **00:25 - 00:35**: 讲师在 `GoodsConsumerController` 中编写了一个带有 `@GetMapping` 注解的测试方法，用于演示降级逻辑。
*   **00:35 - 00:45**: 讲师在控制台中执行 `deregistering service` 命令，模拟服务降级。
*   **00:45 - 00:55**: 讲师在浏览器中访问 `localhost:18082/consumer/`，验证降级逻辑是否生效，页面返回了“`No`”的响应。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   课程大纲：第5章“熔断限流、高并发处理”下的“3.3.1 基于Feign的服务降级”。
    *   配置说明：在 `bootstrap.yml` 中配置 Sentinel 控制台地址和 Feign 支持。

*   **关键代码**:

    **1. Maven 依赖 (pom.xml)**:
    ```xml
    <dependency>
        <groupId>com.alibaba.cloud</groupId>
        <artifactId>spring-cloud-starter-alibaba-sentinel</artifactId>
    </dependency>
    ```

    **2. Sentinel 配置 (bootstrap.yml)**:
    ```yaml
    spring:
      cloud:
        sentinel:
          transport:
            port: 8719
            dashboard: 192.168.211.137:8858
          feign:
            sentinel:
              enabled: true
    ```

    **3. 控制器代码 (GoodsConsumerController.java)**:
    ```java
    @GetMapping(value = "/ue/{max}")
    public String one(@PathVariable(value = "max") Integer max) {
        return "No" + max;
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：项目初始化与依赖添加**
    *   讲师在 IDE 中打开 `consumer` 项目的 `pom.xml` 文件。
    *   他将 `spring-cloud-starter-alibaba-sentinel` 依赖添加到 `<dependencies>` 标签内，以使项目能够使用 Sentinel 功能。

*   **场景二：Sentinel 配置**
    *   讲师切换到 `bootstrap.yml` 文件。
    *   他配置了 `spring.cloud.sentinel.transport.port` 为 `8719`，并设置了 `dashboard` 地址为 `192.168.211.137:8858`。
    *   他还配置了 `feign.sentinel.enabled: true`，以启用 Feign 对 Sentinel 的支持。

*   **场景三：代码降级逻辑演示**
    *   讲师在 `GoodsConsumerController` 中编写了一个简单的 `@GetMapping` 方法，该方法接收一个参数 `max`。
    *   他通过在方法中直接返回字符串 `"No" + max` 来模拟一个简单的降级逻辑。

*   **场景四：服务降级与结果验证**
    *   讲师在控制台中执行了 `deregistering service` 命令，模拟服务降级。
    *   他随后在浏览器中访问 `localhost:18082/consumer/`。
    *   页面返回了“`No1`”的响应，这表明降级逻辑已经生效，服务调用失败时返回了预设的降级响应。

---

通过以上分析，我们可以清晰地看到讲师是如何一步步地将 Sentinel 集成到 Feign 消费者服务中，并通过代码和配置实现服务降级功能的。
