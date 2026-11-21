# 画面线理解：day01-21-Postman的使用

- 阶段：10.阶段十 万信金融项目
- 章节：01_万信金融-项目介绍和开发环境搭建
- 源文件：10.阶段十 万信金融项目\01_万信金融-项目介绍和开发环境搭建\day01-21-Postman的使用_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:38, 01:00, 03:11, 03:44, 04:33, 05:02, 05:43, 06:49, 07:35, 08:12, 08:27, 09:16, 10:50, 12:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:12:49

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Cloud 的微服务消费者服务的代码实现、配置文件设置以及通过 Postman 进行接口测试的过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 显示 IntelliJ IDEA 中 `application.yml` 文件的内容，主要配置了 Spring Cloud Eureka 服务发现和 Ribbon 负载均衡的相关参数。
- 代码内容：
  ```yaml
  spring.http.encoding.force=true
  # springCloud eureka配置
  eureka.client.serviceUrl.defaultZone=http://localhost:50000/eureka/
  #注册时使用ip地址，不使用服务名
  eureka.instance.preferIpAddress=true
  eureka.instance.instanceId=${spring.application.name}:${spring.cloud.client.ip-address}:${server.port}
  # springCloud ribbon配置
  #最大重试次数，当Eureka中可以找到服务，但是服务端不响应时重试
  ribbon.MaxAutoRetries=2
  #对所有操作都进行重试，如果是get可以，如果是post、put等没有实现幂等的情况下是不安全的，所以设置为false
  ribbon.OkToRetryAllOperations=false
  #超时处理的超时次数
  ribbon.ConnectTimeout=3000
  #初始重试的重试次数
  ribbon.MaxAutoRetriesNextServer=2
  ```

画面 2：
- 显示 `ConsumerController.java` 文件内容，定义了两个 REST 接口：`/hello` 和 `/hi`。
- 代码内容：
  ```java
  @RestController
  @Api(value = "用户服务的Controller", tags = "Consumer", description = "用户服务API")
  public class ConsumerController {
      @ApiOperation("测试hello")
      @GetMapping(path = "/hello")
      public String hello() { return "hello"; }
      @ApiOperation("测试hi")
      @ApiImplicitParam(name="name",value="姓名",required = true,dataType = "String")
      @PostMapping(value = "/hi")
      public String hi(String name) { return "hi,"+name; }
  }
  ```

画面 3：
- 与画面 2 内容相同，只是光标位置不同，高亮了 `@ApiImplicitParam` 注解。

画面 4：
- 显示一个工作区视图，包含多个窗口，如 Postman、ApolloPortal、SQLyog、adminService 等，用于展示不同工具的使用场景。

画面 5：
- 显示 Postman 中创建的请求，用于获取认证令牌（token），请求方法为 POST，URL 为 `http://172.16.0.130:5001/...`。

画面 6：
- 与画面 2 内容相同，只是光标位置不同，高亮了 `@ApiImplicitParam` 注解。

画面 7：
- 与画面 5 内容相同，显示 Postman 中的请求界面，等待发送。

画面 8：
- 与画面 4 内容相同，显示工作区视图。

画面 9：
- 显示 IntelliJ IDEA 中 `wanningzp_apollo` 项目的 `DiscoveryServer` 启动日志，显示 Spring Boot 启动过程。

画面 10：
- 显示 `DiscoveryServer` 启动日志的后续内容，包括 Eureka 服务注册和发现的初始化过程。

画面 11：
- 显示 Postman 中的 GET 请求，用于测试 `/hello` 接口，请求 URL 为 `http://localhost:33070/consumer/hello`，请求参数为 `name=1`，响应结果为 `Hello`。

画面 12：
- 显示 Postman 中的 POST 请求，用于测试 `/hi` 接口，请求 URL 为 `http://localhost:33070/consumer/hi`，等待发送。

画面 13：
- 显示 `ConsumerController.java` 文件内容，与画面 2 内容相同，高亮了 `@ApiImplicitParam` 注解。

画面 14：
- 显示 Postman 中的未命名请求，用于测试接口，等待设置请求参数。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
见上述第 2 点内容。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
