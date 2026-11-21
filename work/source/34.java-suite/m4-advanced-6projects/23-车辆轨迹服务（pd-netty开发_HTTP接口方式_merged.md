# 23-车辆轨迹服务（pd-netty开发_HTTP接口方式 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那接下来呢咱们继续来开发我们这个PDNAT服务

刚才呢我们是把这个Kafka Center呢

这个工具类呢已经开发好了

那接下来呢我们需要来开发一个什么呢

开发一个Controller来提供一个HTTP接口对吧

好那么我们先把这个包呢来创建一下

咱们就叫Controller包

然后呢在这儿来提供一个Controller

就叫做NAT Controller吧

好

那么这个呢是我们提供这个HTTP啊

接口方式来接收什么呢

来接收我们这个四极端

四极端

然后上报的这个什么呢

位置信息对吧

好

然后呢在这儿来加一个注解REST Controller

然后呢再来一个Request Mapping吧

好

这个就叫NAT

然后呢再来加一个API

API注解吧

好

API

然后来一个Text

好

这个呢就叫什么呢

车辆轨迹服务吧

车辆轨迹服务

好

然后呢为了便于记录日志呢

我们再来一个什么Sleep for Day

好

然后这里边呢我们直接提供一个方法就可以

就是上报这个位置信息对吧

用来接收上报位置信息这么一个方法

Public

返回值呢我们来

返回值呢我们来

一个Result就可以了

在咱们这个Common里边封装的一个Result对象

好

这里边是不是有Result

然后呢我们这个方法名呢就叫Push吧

就叫Push

好

然后呢这儿来一个什么呢

Post Mapping

好

跟我们这个方法名保持一致

也叫Push

好

然后呢它这个司机端呢

它是通过那个APP对吧

就司机端APP来请求到我们当前这个接口服务

好

那么我们在这儿呢是不是封装了一个实体类来接收对吧

也就是说它提交的时候呢

肯定是按照相应的这些参数啊来进行提交

所以说呢我们在这儿呢直接啊

就可以通过一个什么呢叫做Location Entity来接收

Location Entity

好

那么因为司机端呢

这个并不是我们开发的对吧

但是我们前面的都已经这个定好了接口规范

那么它提交的时候呢是通过JSON方式来提交的

所以我们在这儿呢需要加一个Request的什么呀

Request Body对吧

然后呢来解析JSON

最终呢封装成我们这个Location Entity

这个实体对象

好

然后在这里边呢其实就非常简单了对吧

在这里边呢我们是不是就可以调用我们刚才开发的这个Kafka Center

咱这里边是不是有这个静态方法

所以说呢我们在这儿呢就可以直接通过Kafka Center

Kafka Center

点什么呢

Center对吧

然后呢

把这个消息给它

传过去对吧

给它发送到堆列当中

好

这是将我们这个消息发送到

发送到

Kafka

堆列

好

那么堆列的名称大家还记得吧

我们在这儿是不是刚才定义了一个常量对吧

所以我们就直接使用这个常量就可以了

通过这个类名

点

这个常量名

对吧

然后接下来呢我们是不是要发送消息

发送消息

我们是不是要发送消息

直接把这个实体发送过去呢

很显然应该是不行的

因为我们刚才看到这个Send的方法

它接收的第二个参数呢是String类型的对吧

所以说呢我们这个地方呢需要把这个什么呢

实体啊给它转换一下

那么给它转成什么呢

String字符串对吧

那么应该是一个String类型的

所以我们在这儿呢需要使用这个

JSON对吧

FastJSON

点什么呢

To

JSON String

然后呢

把这个实体类型的这个实体呢

传进去对吧

Location Entity

然后呢我们就可以来接收这个Message

把它转成这个String类型

然后呢就可以通过

把这个参数放在这儿

这样是不是就有接收好了

然后呢发送完之后呢

咱们是不是直接return什么呢

result

点什么呢

OK啊

咱们封装了这么一个方法

OK

你看

这个地方呢

它其实就是直接new一个result的对吧

new一个result的

然后呢这里边它的默认值呢是什么呢

是不是就是这个啊

这个message就是success

code呢就是0

好

整体来说呢这个方法其实还是非常简单的

来加一个注释吧

好

这个就是将我们这个车辆定位信息对吧

发送到Kavka对链

好

然后发送完之后呢我们可以来记录一下对吧

通过log

点什么呢

info就可以了

放个点info

这个是

这就是http啊

http接口方式来推送什么呢

推送这个位置信息到Kavka啊

然后呢我们简单记录一下就可以了

然后具体这个位置信息呢

咱们可以把这个message是不是给它放到后边

就是在这呢我们使用这种站位符这种方式对吧

然后具体这个信息给它称呼了

然后这个信息给它传进去就可以了

好

那么到这儿的话呢我们这个controller呢就已经开发好了

一会儿呢我们可以来测试一下

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

好

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是一个关于使用 Spring Boot 和 Kafka 构建车辆轨迹服务的实战教学。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何创建一个 HTTP 接口来接收车辆位置上报信息，并将这些信息通过 Kafka 队列进行异步发送。核心内容包括：
*   **创建控制器 (Controller)**：使用 `@RestController` 和 `@PostMapping` 注解定义一个接收 POST 请求的接口。
*   **定义数据模型**：创建 `LocationEntity` 类来封装车辆位置数据。
*   **集成 Kafka**：编写 `KafkaSender` 服务类，使用 `@Autowired` 注入 `KafkaTemplate`，并实现发送消息的方法。
*   **数据序列化**：使用 `JSON.toJSONString()` 方法将 Java 对象转换为 JSON 字符串，以便 Kafka 消息能正确传输。
*   **返回结果**：使用自定义的 `Result` 工具类封装 HTTP 响应，提供统一的返回格式。

整个过程旨在展示如何将前端或设备上报的车辆位置数据，通过一个轻量级的 HTTP 接口，高效、可靠地异步发送到 Kafka 消息队列中，为后续的业务处理（如轨迹存储、实时监控等）提供数据支持。

---

### 2) 按时间顺序的章节（带时间点）

*   **0:00 - 0:05**: 开场，展示项目结构，定位到 `NettyController` 文件。
*   **0:05 - 0:15**: 在 `NettyController` 中添加 `@RestController` 注解，准备创建一个 HTTP 接口。
*   **0:15 - 0:25**: 添加 `@RequestMapping("/netty")` 和 `@Api(tags = "车辆轨迹服务")` 注解，定义接口的路径和 Swagger 文档描述。
*   **0:25 - 0:35**: 添加 `@Slf4j` 注解，用于日志记录。
*   **0:35 - 0:45**: 定义 `push` 方法，声明接收 `LocationEntity` 类型的请求体。
*   **0:45 - 1:00**: 在方法中调用 `KafkaSender.send(...)` 方法，将位置实体发送到 Kafka。
*   **1:00 - 1:15**: 为 `LocationEntity` 类添加 `@Data` 注解，简化属性的 Getter/Setter。
*   **1:15 - 1:25**: 在 `KafkaSender` 类中定义常量 `MSG_TOPIC`，并初始化 `KafkaTemplate`。
*   **1:25 - 1:35**: 在 `KafkaSender` 的 `send` 方法中，使用 `template.send(topic, message)` 发送消息。
*   **1:35 - 1:45**: 在 `NettyController` 的 `push` 方法中，使用 `JSON.toJSONString(locationEntity)` 将对象序列化为 JSON 字符串。
*   **1:45 - 1:55**: 使用 `Log.info` 记录发送成功的日志。
*   **1:55 - 2:05**: 使用 `Result.ok()` 方法返回一个成功的 HTTP 响应。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **代码片段 1: `NettyController.java`**
    ```java
    @RestController
    @RequestMapping("/netty")
    @Api(tags = "车辆轨迹服务")
    @Slf4j
    public class NettyController {
        @PostMapping("/push")
        public Result push(@RequestBody LocationEntity locationEntity) {
            KafkaSender.send(KafkaSender.MSG_TOPIC, locationEntity);
            log.info("HTTP接口方式推送位置信息到kafka: {}", message);
            return Result.ok();
        }
    }
    ```

*   **代码片段 2: `KafkaSender.java`**
    ```java
    public class KafkaSender {
        public final static String MSG_TOPIC = "tms_order_location"; // Kafka队列名称

        @Autowired
        private KafkaTemplate<String, String> kafkaTemplate;

        @PostConstruct
        public void init() {
            template = kafkaTemplate;
        }

        public static boolean send(String topic, String message) {
            try {
                template.send(topic, message);
            } catch (Exception e) {
                e.printStackTrace();
            }
            return true;
        }
    }
    ```

*   **代码片段 3: `LocationEntity.java`**
    ```java
    @Data
    public class LocationEntity {
        private String id;
        private String deviceCode;
        private String latitude;
        private String longitude;
        private String speed;
        private String direction;
        private String time;
    }
    ```

*   **代码片段 4: `Result.java` (工具类)**
    ```java
    public static Result ok(String msg) {
        Result result = new Result();
        result.put("msg", msg);
        return result;
    }

    public static Result ok(Map<String, Object> map) {
        Result result = new Result();
        result.putAll(map);
        return result;
    }

    public static Result ok() {
        return new Result();
    }

    @Override
    public Result put(String key, Object value) {
        super.put(key, value);
        log.info("key: {} value: {}", key, value);
        return this;
    }
    ```

*   **关键注解**：
    *   `@RestController`：将控制器标记为 RESTful Web 服务。
    *   `@RequestMapping`：定义接口的根路径。
    *   `@PostMapping`：定义处理 POST 请求的接口。
    *   `@RequestBody`：将 HTTP 请求体中的 JSON 数据绑定到方法参数。
    *   `@Slf4j`：自动生成日志记录器。
    *   `@Api`：Swagger 文档注解，用于描述接口。
    *   `@Autowired`：自动注入 Spring 容器中的 Bean。
    *   `@PostConstruct`：在 Bean 初始化后执行的方法。
    *   `@Data`：Lombok 注解，自动生成 Getter、Setter、toString、equals 和 hashCode 方法。

---

### 4) 关键场景与演示描述

*   **场景 1: 创建控制器**
    讲师在 IntelliJ IDEA 中打开 `NettyController.java` 文件，通过鼠标点击和键盘输入，逐步添加 `@RestController`、`@RequestMapping` 和 `@Api` 注解，为接口定义了基础的元数据。

*   **场景 2: 定义 HTTP 接口**
    讲师使用 `@PostMapping("/push")` 注解定义了一个接收 POST 请求的接口，并通过 `@RequestBody LocationEntity locationEntity` 声明了请求体的参数类型，展示了如何接收前端或设备上报的 JSON 数据。

*   **场景 3: 集成 Kafka**
    讲师切换到 `KafkaSender.java` 文件，演示了如何使用 `@Autowired` 注入 `KafkaTemplate`，并定义了常量 `MSG_TOPIC` 作为 Kafka 队列的名称。通过 `template.send(topic, message)` 方法，将消息发送到 Kafka。

*   **场景 4: 数据序列化**
    讲师在 `NettyController` 的 `push` 方法中，使用 `JSON.toJSONString(locationEntity)` 方法将 `LocationEntity` 对象转换为 JSON 字符串，确保 Kafka 能正确接收和解析数据。

*   **场景 5: 日志记录与返回结果**
    讲师在方法中添加了 `log.info` 日志语句，用于记录发送成功的消息。最后，通过 `Result.ok()` 方法返回一个标准的 HTTP 响应，实现了接口的完整闭环。

整个演示过程逻辑清晰，步骤明确，通过实际代码操作，直观地展示了如何构建一个基于 Spring Boot 和 Kafka 的车辆轨迹数据上报服务。
