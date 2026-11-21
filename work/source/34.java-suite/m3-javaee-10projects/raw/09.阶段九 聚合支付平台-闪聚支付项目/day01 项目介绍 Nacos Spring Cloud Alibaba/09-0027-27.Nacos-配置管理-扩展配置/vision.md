# 画面线理解：27.Nacos-配置管理-扩展配置

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day01 项目介绍 Nacos Spring Cloud Alibaba
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day01 项目介绍 Nacos Spring Cloud Alibaba\27.Nacos-配置管理-扩展配置【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 01:12, 01:39, 02:18, 02:56, 03:31, 04:13, 04:31, 05:13, 05:39, 06:06, 06:57, 07:22, 07:58
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:32:15

1) 这一组画面整体在讲如何在 Nacos 中配置和使用多数据源（ext-config）来管理不同服务的配置文件，并在 Spring Cloud 应用中读取这些配置。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了项目结构，重点在 `bootstrap.yml` 文件中配置了 Nacos 服务发现和负载均衡，以及 `ext-config` 配置项。
画面2: PPT 页面，讲解了通过 `spring.cloud.nacos.config.ext-config[n].data-id` 和 `group` 属性来管理多个配置文件。
画面3: Nacos 界面，新建配置，Data ID 为 `ext-config-common01.yaml`，Group 为 `COMMON_GROUP`。
画面4: Nacos 界面，配置 `ext-config-common01.yaml`，内容为 `name: zhangsan` 和 `addr: beijing`。
画面5: 项目中 `bootstrap.yml` 文件，配置了 `ext-config[0]` 使用 `ext-config-common01.yaml`。
画面6: 项目中 `bootstrap.yml` 文件，配置了 `ext-config[1]` 使用 `ext-config-common02.yaml`。
画面7: 代码中 `RestConsumerController`，使用 `@Value("${common.name}")` 注入配置值。
画面8: 控制台输出，显示服务已启动并注册到 Nacos。
画面9: Nacos 界面，显示了已配置的多个配置文件，包括 `ext-config-common01.yaml` 和 `ext-config-common02.yaml`。
画面10: PPT 页面，讲解了 `ext-config` 配置不支持多个 `data-id` 的情况。
画面11: 控制台输出，显示服务已启动并注册到 Nacos。
画面12: PPT 页面，再次强调 `ext-config` 配置不支持多个 `data-id`，但可以通过 `group` 属性自定义组。
画面13: Nacos 界面，配置 `ext-config-common02.yaml`，内容为 `name: zhangsan` 和 `addr: beijing`。
画面14: 项目中 `bootstrap.yml` 文件，配置了 `ext-config[0]` 和 `ext-config[1]` 分别指向 `ext-config-common01.yaml` 和 `ext-config-common02.yaml`。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面1:
```yaml
name: nacos-restful-consumer
#服务名
cloud:
  nacos:
    discovery:
      server-addr: 127.0.0.1:8848 #服务发现中心地址
      namespace: 1f5ec8a1-1f05-10cd-961a-8414f312a204 #指定命名空间的id
    config:
      server-addr: 127.0.0.1:8848 #配置中心地址
      file-extension: yaml #指定配置文件的扩展名，配置文件名称根据application.name的名称拼接，为nacos-restful-consumer.yaml
      ext-config[0]:
        data-id: ext-config-common01.yaml
        group: COMMON_GROUP
        refresh: true
      ext-config[1]:
        data-id: ext-config-common02.yaml
        group: COMMON_GROUP
        refresh: true
```

画面2:
```yaml
cloud:
  config:
    server-addr: 127.0.0.1:8848 # 配置中心地址
    file-extension: yaml
    # namespace: 1f5ec8a1-1f05-10cd-961a-8414f312a204 # 开发环境
    # config external configuration
    # 1. Data Id group: 组名,refresh: 动态刷新
    ext-config[0]:
      data-id: ext-config-common01.yaml
      group: COMMON_GROUP
      refresh: true
    ext-config[1]:
      data-id: ext-config-common02.yaml
      group: COMMON_GROUP
      refresh: true
```

画面3:
Data ID: ext-config-common01.yaml
Group: COMMON_GROUP

画面4:
配置ext-config-common01.yaml :
Data ID: ext-config-common01.yaml
Group: COMMON_GROUP
配置格式: YAML
配置内容:
```yaml
common:
  name: zhangsan
  addr: beijing
```

画面5:
```yaml
name: nacos-restful-consumer
#服务名
cloud:
  nacos:
    discovery:
      server-addr: 127.0.0.1:8848 #服务发现中心地址
      namespace: 1f5ec8a1-1f05-10cd-961a-8414f312a204 #指定命名空间的id
    config:
      server-addr: 127.0.0.1:8848 #配置中心地址
      file-extension: yaml #指定配置文件的扩展名，配置文件名称根据application.name的名称拼接，为nacos-restful-consumer.yaml
      ext-config[0]:
        data-id: ext-config-common01.yaml
        group: COMMON_GROUP
        refresh: true
```

画面6:
```yaml
name: nacos-restful-consumer
#服务名
cloud:
  nacos:
    discovery:
      server-addr: 127.0.0.1:8848 #服务发现中心地址
      namespace: 1f5ec8a1-1f05-10cd-961a-8414f312a204 #指定命名空间的id
    config:
      server-addr: 127.0.0.1:8848 #配置中心地址
      file-extension: yaml #指定配置文件的扩展名，配置文件名称根据application.name的名称拼接，为nacos-restful-consumer.yaml
      ext-config[0]:
        data-id: ext-config-common01.yaml
        group: COMMON_GROUP
        refresh: true
      ext-config[1]:
        data-id: ext-config-common02.yaml
        group: COMMON_GROUP
        refresh: true
```

画面7:
```java
@Value("${common.name}")
private String common_name;

@Autowired
ConfigurableApplicationContext applicationContext;

@GetMapping(value = "/configs")
public String getValue() {
    String name = applicationContext.getEnvironment().getProperty("common.name");
    String addr = applicationContext.getEnvironment().getProperty("common.addr");
    return name+addr;
}
```

画面8:
```text
2019-11-28 20:54:35.195 INFO 7392 --- [TaskScheduler-1] a.r.c.n.NacosServiceMetadataRepository : Current application will subscribe all services(size: 0)
2019-11-28 20:54:35.212 INFO 7392 --- [TaskScheduler-1] a.r.c.n.NacosServiceMetadataRepository : Current application will subscribe all services(size: 0)
ServiceBootstrap: 0 classes reloaded
SpringRestConsumerBootstrap: 0 classes reloaded
SpringRestConsumerBootstrap: 0 classes reloaded
SpringRestConsumerBootstrap: 0 classes reloaded
```

画面9:
Data ID: nacos-restful-consumer.yaml
Group: DEFAULT_GROUP
Data ID: ext-config-common01.yaml
Group: COMMON_GROUP
Data ID: ext-config-common02.yaml
Group: COMMON_GROUP

画面10:
```yaml
application:
  name: service2
cloud:
  nacos:
    config:
      server-addr: 127.0.0.1:8848 # 配置中心地址
      file-extension: yaml
      namespace: 1f5ec8a1-1f05-10cd-961a-8414f312a204 # 开发环境
      # config external configuration
      # 1. Data Id group: 组名,refresh: 动态刷新
      ext-config[0]:
        data-id: ext-config-common01.yaml
        group: COMMON_GROUP
        refresh: true
      ext-config[1]:
        data-id: ext-config-common02.yaml
        group: COMMON_GROUP
        refresh: true
```

画面11:
```text
2019-11-28 20:55:35.203 WARN 7392 --- [TaskScheduler-1] a.r.c.n.NacosServiceMetadataRepository : Current application will subscribe all services(size: 0)
2019-11-28 20:55:35.212 WARN 7392 --- [TaskScheduler-1] a.r.c.n.NacosServiceMetadataRepository : Current application will subscribe all services(size: 0)
ServiceBootstrap: 0 classes reloaded
SpringRestConsumerBootstrap: 0 classes reloaded
SpringRestConsumerBootstrap: 0 classes reloaded
SpringRestConsumerBootstrap: 0 classes reloaded
```

画面12
