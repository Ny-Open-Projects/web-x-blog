# 画面线理解：12.万信金融P2P项目实行服务调用链路追踪

- 阶段：10.阶段十 万信金融项目
- 章节：08_万信金融-微服务高级部分/8-2 Zipkin的理解和使用
- 源文件：10.阶段十 万信金融项目\08_万信金融-微服务高级部分\8-2 Zipkin的理解和使用\12.万信金融P2P项目实行服务调用链路追踪_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:37, 02:04, 03:35, 04:35, 05:59, 06:54, 07:49, 08:23, 09:14, 10:06, 11:20, 12:17, 12:31, 13:58
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 09:11:55

1) 这一组画面整体在讲什么（一句话）：
演示万信金融P2P项目集成Spring Cloud Sleuth与Zipkin进行服务链路追踪的完整步骤。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示PPT标题“4. 万信金融P2P项目集成服务链路追踪”及“4.1 集成步骤”，内容包括在`wanxin2p-api`工程的`pom.xml`中添加Sleuth和Zipkin依赖。
画面2：在IDEA中展示`wanxin2p-api`的`pom.xml`文件，已添加`spring-cloud-starter-sleuth`和`spring-cloud-starter-zipkin`依赖。
画面3：在Apollo配置中心的`micro_service.spring-zipkin`命名空间下，配置了`spring.sleuth.enabled=true`和`spring.zipkin.base-url=http://localhost:9411`。
画面4：在Apollo配置中心的`consumer-service`应用下，展示其关联的多个命名空间，包括`micro_service.spring-boot-http`、`micro_service.spring-eureka`等。
画面5：在IDEA中展示`wanxin2p-gateway-server`的`application.yml`文件，其中配置了`spring.zipkin`相关属性。
画面6：在IDEA中展示`wanxin2p-uaa-service`的`application.yml`文件，配置了`spring.application.name=uaa-service`和`apollo.namespaces`。
画面7：在IDEA中展示`wanxin2p-uaa-service`的`application.yml`文件，配置了`spring.application.name=uaa-service`和`apollo.namespaces`。
画面8：在浏览器中展示登录页面，同时打开开发者工具查看网络请求，显示了页面加载的资源列表。
画面9：在浏览器中访问Zipkin的`/`页面，显示了服务追踪查询的表单。
画面10：在浏览器中访问Zipkin的`/traces`页面，显示了具体的追踪信息，包括`http.method=POST`、`http.path=/account/session`等。
画面11：在浏览器中访问Zipkin的`/dependency`页面，显示了服务调用关系图，`gateway-server`指向`uaa-service`，`uaa-service`指向`account-service`。
画面12：在浏览器中访问Zipkin的`/dependency`页面，显示了服务调用关系图，`gateway-server`指向`consumer-service`和`uaa-service`，`uaa-service`指向`account-service`。
画面13：在浏览器中访问Zipkin的`/dependency`页面，显示了服务调用关系图，`gateway-server`指向`consumer-service`和`uaa-service`，`uaa-service`指向`account-service`。
画面14：在浏览器中访问Zipkin的`/dependency`页面，显示了服务调用关系图，`gateway-server`指向`consumer-service`和`uaa-service`，`uaa-service`指向`account-service`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```xml
1. 在wanxin2p-api工程的pom.xml中增加如下依赖
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-sleuth</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-zipkin</artifactId>
</dependency>
```
画面2：
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-sleuth</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-zipkin</artifactId>
</dependency>
```
画面3：
```properties
# 开启Sleuth
spring.sleuth.enabled=true
# 设置zipkin服务地址
spring.zipkin.base-url=http://localhost:9411
# 采样率，取信范围[0-1]
```
画面5：
```yaml
spring:
  zipkin:
    base-url: http://localhost:9411
```
画面6：
```yaml
app:
  id: uaa-service
apollo:
  bootstrap:
    enabled: true
    eagerLoad: true
namespaces: application,micro_service.spring-boot-druid,micro_service.spring-boot-http,micro_service.spring-boot-redis,micro_service.spring-cloud-hystrix,micro_service.spring-cloud-ribbon,micro_service.spring-cloud-zipkin
spring:
  application:
    name: uaa-service
```
画面7：
```yaml
app:
  id: uaa-service
apollo:
  bootstrap:
    enabled: true
    eagerLoad: true
namespaces: application,micro_service.spring-boot-druid,micro_service.spring-boot-http,micro_service.spring-boot-redis,micro_service.spring-cloud-hystrix,micro_service.spring-cloud-ribbon,micro_service.spring-cloud-zipkin
spring:
  application:
    name: uaa-service
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题“4. 万信金融P2P项目集成服务链路追踪”及“4.1 集成步骤”。
画面11：架构图显示`gateway-server`指向`uaa-service`，`uaa-service`指向`account-service`。
画面12：架构图显示`gateway-server`指向`consumer-service`和`uaa-service`，`uaa-service`指向`account-service`。
画面13：架构图显示`gateway-server`指向`consumer-service`和`uaa-service`，`uaa-service`指向`account-service`。
画面14：架构图显示`gateway-server`指向`consumer-service`和`uaa-service`，`uaa-service`指向`account-service`。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
