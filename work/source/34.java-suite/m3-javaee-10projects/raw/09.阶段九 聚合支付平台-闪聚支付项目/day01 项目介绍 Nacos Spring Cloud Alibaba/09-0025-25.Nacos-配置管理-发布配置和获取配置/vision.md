# 画面线理解：25.Nacos-配置管理-发布配置和获取配置

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day01 项目介绍 Nacos Spring Cloud Alibaba
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day01 项目介绍 Nacos Spring Cloud Alibaba\25.Nacos-配置管理-发布配置和获取配置【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:08, 02:13, 03:08, 04:00, 04:45, 05:58, 06:41, 08:04, 08:40, 10:19, 11:30, 12:32, 13:14, 14:03
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:30:41

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Nacos 配置中心发布和获取配置，并通过 Spring Cloud Alibaba 实现配置的动态刷新。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示课程 PPT，讲解 Nacos 配置管理的优劣势，引导进入 Nacos 世界。
画面 2：展示 Nacos 控制台，准备发布配置。
画面 3：在 IDE 中查看 `application.yml`，其中包含 Nacos 配置信息。
画面 4：展示 `RestConsumerController` 中使用 `@Value("${common.name}")` 注解获取配置。
画面 5：在 `application.yml` 中配置 Nacos 服务发现和配置中心地址。
画面 6：运行服务后，控制台报错，提示无法解析占位符 `common.name`。
画面 7：在 `application.yml` 中配置 `config` 服务地址。
画面 8：控制台报错，提示无法解析占位符 `common.name`。
画面 9：在 PPT 中展示如何添加 `spring-cloud-starter-alibaba-nacos-config` 依赖，并在 `bootstrap.yml` 中配置 Nacos。
画面 10：在 IDE 中右键 `application.yml`，选择“Make as Plain Text”。
画面 11：在 Nacos 控制台中进行配置内容对比，准备发布。
画面 12：在 IDE 中查看 `RestConsumerController`，展示 `@Value` 注解和 `@Autowired` 注解。
画面 13：在 Nacos 控制台中发布配置。
画面 14：在 PPT 中展示如何通过 `@Autowired` 注入 `ConfigurableApplicationContext` 实现配置动态刷新。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3：
```yaml
nacos:
  discovery:
    server-addr: 127.0.0.1:8848
  namespace: f5eec3c1-if05-4cc0-964a-c8d41f312ab4
  config:
    server-addr: 127.0.0.1:8848
```

画面 5：
```yaml
application:
  name: nacos-restful-consumer #服务名
cloud:
  nacos:
    discovery:
      server-addr: 127.0.0.1:8848 #服务发现中心地址
      namespace: f5eec3c1-if05-4cc0-964a-c8d41f312ab4 #指定命名空间ID
    config:
      server-addr: 127.0.0.1:8848 #配置中心地址
```

画面 7：
```yaml
provider:
  address: 127.0.0.1:58010
spring:
  application:
    name: nacos-restful-consumer #服务名
  cloud:
    nacos:
      discovery:
        server-addr: 127.0.0.1:8848 #服务发现中心地址
        namespace: f5eec3c1-if05-4cc0-964a-c8d41f312ab4 #指定命名空间ID
      config:
        server-addr: 127.0.0.1:8848 #配置中心地址
```

画面 9：
```xml
<dependency>
  <groupId>com.alibaba.cloud</groupId>
  <artifactId>spring-cloud-starter-alibaba-nacos-config</artifactId>
</dependency>
```

```yaml
spring:
  cloud:
    nacos:
      config:
        server-addr: 127.0.0.1:8848 # 配置中心地址
        file-extension: yaml
        group: DEFAULT_GROUP
```

画面 12：
```java
@Value("${common.name}")
private String common_name;

@GetMapping(value = "/configs")
public String getValue() {
  return common_name;
}
```

画面 14：
```java
// 注入配置文件上下文
@Autowired
private ConfigurableApplicationContext applicationContext;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1：
标题：3.2 Nacos配置管理
子标题：3.2.1 发布配置
内容：首先在nacos发布配置，nacos-restful-consumer服务从nacos读取配置。
内容：浏览添加 http://127.0.0.1:8848/nacos，打开nacos控制台，并点击菜单配置管理->配置列表。

画面 9：
标题：在bootstrap.yml添加配置：
内容：展示 `spring.cloud.nacos.config` 配置项。

画面 14：
标题：基于上面的例子，若要实现配置的动态更新，只需要进行如下改造：
内容：展示 `@Autowired` 注入 `ConfigurableApplicationContext` 的代码。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
