# 24-车辆轨迹服务（pd-netty开发_HTTP接口方式 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么刚才咱们关于PDNet所提供的HTTP接口这种方式来上报位置信息,对吧,自己的位置信息,那么这块我们已经开发完了。

但是刚才我们是忘了一点东西,就是什么呢,咱们现在是不是想通过Swagger接口这种方式来测试一下我们当前这个push方法,对吧。

那么要想测试的话呢,我们刚才是忘了写这个SwaggerConfig,咱们这个配置类,对吧,需要开启我们这个Swagger文档的功能,否则的话咱们是没办法测试的。

所以我们这个地方呢,需要把这个配置类,那么给它拷过来,这个呢就是从我们前面这个PDBase这边拷过来的。

拷过来之后呢,主要就是检查一下咱们这个包扫描的,扫描的这个包能不能扫描到我们的Control,对吧。

那么这个包呢,检查一下是没问题的。

好,那这样的话呢,我们这个Swagger文档呢,就可以使用了,对吧。

然后呢,我这儿其实也已经把这个服务跑起来了,启动是没有问题的。

那接下来呢,我们就可以来测试一下这个方法。

首先呢,我们先来说明一下,如何,怎么能够证明,怎么能够证明我们当前这个,

呃,消息呢,是发送成功了呢。

咱们其实可以来看一下我们这个图。

你看啊,我们通过PDNet,把这个上报的信息,把它发送到卡夫卡队列当中之后啊,

那么它就会由我们这个Droid是不是来实时摄取到Droid当中。

那么当前呢,我们这个环境呢,其实已经搭建好了。

咱们刚才也看到了,在卡夫卡,卡夫卡呢,我们使用的是这台服务器,对吧。

那么并且呢,也已经把这个队列呢,给创建好了。

同时呢,我们还,

还提供了这个Droid。

这个Droid呢,是在当前这个服务上。

当然我们这是申请了一个域名,通过域名这种方式来访问。

大家可以看到啊,我们这个Droid上面呢,已经提前创建好了这么一个数据源,对吧。

叫做TMS Order Location。

并且呢,当前这个数据源里边呢,一共有这么多条数据,对吧。

是8904条数据。

那也就是说,如果说我们能够成功地把这个什么呢,消息把它发送到卡夫卡当中,

那这样的话呢,它就可以实时地,

摄取到我们Droid当中。

所以呢,我们一会儿看一下什么呢。

我发送完这个消息之后,看看我们Droid当中有没有增加数据。

如果增加了一条数据,那就说明什么呢?

那就说明我们整个这个流程是不是已经跑通了。

这也就是说明我们这个消息肯定是发送成功了。

所以说呢,我们通过这种方式来验证一下就可以了。

那接下来呢,我们来访问一下咱们这个接口文档。

当前我们这个PDNet,它所使用的这个端口呢,是多少呢?

是8104。

8192。

8192。

好。

咱们来打开,测试一下。

Login host,应该是8192。

好,这个地址,对吧。

你看这是车辆轨迹服务。

然后呢,我们现在是不是就要调用这个Push方法来测这个方法,Try it out。

这里边这个信息啊,你看它是一个JSON形式的,这个不能随便写啊,因为它是跟我们的业务相关的。

好。

在这儿呢,

我们先把这个数据呢,把它复制过来。

好,把数据复制过来。

然后呢,我们在这边来给它粘贴到这个位置。

它这个好像是这里边这个不让删。

那我只是靠这里面这点东西就可以了。

好。

它这个花块呢,在这个位置它不让删。

好。

你看这是有我们的业务ID,对吧。

还有什么Current Time,还有什么,这是纬度。

然后呢,这是车辆。

车牌号。

然后呢,这是进度。

然后呢,这个呢,是什么呢?

这是名称,对吧。

然后呢,这个是车队名。

然后呢,这个是运输ID。

运输任务的ID。

然后呢,这个是一个类型,是一个Trunk。

代表的是司机的这个坐标信息。

如果这个呢,写的是Courier,那是不是代表的就是我们的快递员,他的这个坐标信息。

好。

现在呢,我们先来刷新一下这个页面,确认一下我们当前这个什么呢,TMS Order Location啊。

咱们这个数据源,它最新的这个数据呢,是这个,是8904,对吧。

然后接下来呢,我们来执行一下。

咱们可以在这边来加一个断点。

先让它稍微暂停一下。

在这加一个断点,然后呢,执行。

好,我们可以看到数据已经提交过来了,对吧。

数据已经提交过来了。

那么这就是我们提交的这个JSON数据。

当然有空的,因为这个Phone我没有提交。

这个是可以为空的。

好,然后呢,我们直接给它跳过去。

好,那么来看一下控制台。

控制台是没有报错,没有报错。

然后呢,你看这个地方呢,也输出了,对吧。

什么接口推动方式,这个就是咱们这个地方输出的。

好,然后呢,把这个信息在控制台是不是输出了一下。

好,那么现在呢,我们从这个程序这边来看呢,应该是没有报错,对吧。

没有报错。

然后呢,我们就来查询一下什么呢。

查询一下我们这个DRAID。

看看DRAID当中呢,我们这个数据呢,有没有增加。

如果它增加了一条数据,这就说明我们整个流程呢,

流程跑通了,肯定是这个消息呢,就发送成功了。

刚才我们看到的这个数据呢,是8904,对吧。

然后呢,我们可以来刷新一下。

刷新一下这个页面。

刚才是8904。

稍等一下。

因为当前我们这个服务器上,哎,看这儿。

这个服务器上的数据量还是非常大的。

你看现在是变成了8905,对吧。

那么说明我们刚才整个流程呢,应该是已经跑通了。

当然你如果想看具体的数据,对吧。

可以通过这个QUERY。

这个前面我们也都讲过啊。

然后在这儿来查询具体的这个数据。

从这儿应该也都能看到。

但是它这个数据量很多啊。

所以它是做了一个分页的展示。

好,那么到这儿的话呢,我们整个这个http接口这种方式呢,

就已经开发好。

并且呢,通过我们刚才这个接口文档这种方式呢,

来进行了一个测试,对吧。

最终呢,我们观察这个DRAID当中,这个数据是多出来了一条。

这就说明整个流程已经跑通了。

好,那么关于http接口这种方式开发呢,

就说到这儿。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程是关于“品达物流TMS项目”中“车辆轨迹服务”的开发教学，具体聚焦于使用 `pd-netty` 框架实现 HTTP 接口方式接收司机上报的车辆定位信息。课程内容涵盖了从项目结构、核心代码编写（包括控制器 `NettyController` 和配置类 `SwaggerConfig`）、到接口调试（使用 Swagger UI）以及最终数据在 Druid 数据库中查询的完整流程。视频旨在演示如何构建一个基于 Spring Boot 的微服务，通过 HTTP 接口接收数据并将其发送至 Kafka，最终由 Druid 进行数据存储和查询。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 课程开场，展示项目结构和 `NettyController.java` 代码，介绍本节将实现 HTTP 接口接收司机上报的位置信息。
*   **00:05 - 00:15**: 展示 `SwaggerConfig.java` 的配置代码，用于开启 Swagger 文档并定义其基础信息，以便后续接口调试。
*   **00:15 - 00:25**: 展示 `NettyController.java` 中的 `@PostMapping("/push")` 方法，该方法接收 `LocationEntity` 对象，将其转换为 JSON 字符串后，通过 `KafkaSender` 发送到 Kafka 的 `MSG_TOPIC` 主题。
*   **00:25 - 00:35**: 在 IntelliJ IDEA 中运行项目，查看控制台日志，确认接口已成功启动并接收数据。
*   **00:35 - 00:45**: 使用浏览器访问 Swagger UI (`localhost:8192/swagger-ui.html`)，查看并测试 `/netty/push` 接口。
*   **00:45 - 00:55**: 在 Swagger UI 中输入模拟的 `locationEntity` 数据并执行 POST 请求，成功发送数据。
*   **00:55 - 01:05**: 切换到 Druid 数据库管理界面，展示如何查询刚刚写入的数据表 `tms_order_location`。
*   **01:05 - 01:15**: 展示项目配置文件 `bootstrap.yml` 和 `bootstrap-dev.yml`，说明如何配置服务名、端口、Nacos 服务发现等。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 图表**:
    *   **系统架构图**: 展示了司机App -> pd-netty -> Kafka -> Druid 的数据流向。
    *   **课程大纲**: 显示了“品达物流TMS项目”的章节结构，当前位于“5.1 pd-netty开发”下的“5.1.1 HTTP接口方式”。

*   **代码**:
    *   **`NettyController.java`**:
        ```java
        @RestController
        @RequestMapping("/netty")
        @Api(tags = "车辆轨迹服务")
        public class NettyController {
            @PostMapping("/push")
            public Result push(@RequestBody LocationEntity locationEntity) {
                String message = JSON.toJSONString(locationEntity);
                KafkaSender.send(KafkaSender.MSG_TOPIC, message); // 将消息发送到Kafka队列
                log.info("HTTP接口方式推送位置信息到kafka: [{}]", message);
                return Result.ok();
            }
        }
        ```
    *   **`SwaggerConfig.java`**:
        ```java
        @Configuration
        @EnableSwagger2
        public class SwaggerConfig extends WebMvcConfigurationSupport {
            private static final String splitter = ",";

            @Bean
            public Docket createRestApi() {
                return new Docket(DocumentationType.SWAGGER_2)
                        .apiInfo(apiInfo())
                        .select()
                        .apis(RequestHandlerSelectors.basePackage("com.iteima.pinda.controller"))
                        .paths(PathSelectors.any())
                        .build();
            }

            private ApiInfo apiInfo() {
                return new ApiInfoBuilder()
                        .title("车辆轨迹服务")
                        .description("提供车辆轨迹信息的API")
                        .version("1.0")
                        .build();
            }
        }
        ```
    *   **`bootstrap.yml`**:
        ```yaml
        server:
          port: 8192
          uri-encoding: UTF-8
        spring:
          application:
            name: pd-netty
            profiles:
              active: dev
          main:
            allow-bean-definition-overriding: true
        ```

*   **公式 / 数据**:
    *   **Swagger UI 示例数据**: 在测试接口时，输入的 `locationEntity` 示例数据，包含 `businessId`, `currentTime`, `lat`, `lng`, `licensePlate`, `name`, `range`, `transportTaskId`, `type` 等字段。

---

### 4) 关键场景与演示描述

*   **场景一：接口开发与调试**
    *   **描述**: 教师首先在 IntelliJ IDEA 中展示了 `NettyController` 的核心代码，该代码定义了一个 `@PostMapping("/push")` 接口，用于接收司机上报的车辆位置信息。接着，通过 `SwaggerConfig` 配置了 Swagger 文档，以便后续调试。
    *   **技术点**: 展示了 Spring Boot 中如何使用 `@RestController` 和 `@PostMapping` 注解定义 RESTful API，以及如何使用 Swagger 生成和调试 API 文档。

*   **场景二：接口测试**
    *   **描述**: 教师启动项目后，通过浏览器访问 Swagger UI (`localhost:8192/swagger-ui.html`)，并导航到 `/netty/push` 接口。在接口的请求体中，输入一个模拟的 `locationEntity` 对象，然后点击“Execute”按钮。
    *   **技术点**: 展示了如何使用 Swagger UI 进行 HTTP 接口的测试，包括设置请求体、选择 Content-Type 并发送请求。

*   **场景三：数据持久化与查询**
    *   **描述**: 在成功发送数据后，教师切换到 Druid 数据库管理界面，执行 SQL 查询语句 `SELECT * FROM tms_order_location`，并成功获取到刚刚写入的数据。
    *   **技术点**: 展示了数据从 HTTP 接口 -> Kafka -> Druid 的完整数据流，以及如何通过 Druid 查询存储的数据。

*   **场景四：项目配置**
    *   **描述**: 教师展示了项目的配置文件 `bootstrap.yml` 和 `bootstrap-dev.yml`，说明了如何配置服务端口、服务名、Nacos 服务发现等。
    *   **技术点**: 展示了 Spring Cloud 中如何通过配置文件进行服务配置和管理。

---

以上是根据视频画面整理出的结构化技术课程分析。
