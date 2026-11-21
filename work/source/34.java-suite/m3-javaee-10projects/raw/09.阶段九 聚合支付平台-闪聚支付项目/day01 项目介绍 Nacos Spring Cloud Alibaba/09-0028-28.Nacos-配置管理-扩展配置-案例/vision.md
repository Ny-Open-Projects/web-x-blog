# 画面线理解：28.Nacos-配置管理-扩展配置-案例

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day01 项目介绍 Nacos Spring Cloud Alibaba
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day01 项目介绍 Nacos Spring Cloud Alibaba\28.Nacos-配置管理-扩展配置-案例【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:36, 01:01, 01:20, 01:54, 02:16, 02:37, 02:56, 03:24, 03:57, 04:16, 04:40, 05:05, 05:24
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:32:56

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Nacos 配置中心使用 ext-config 功能，为 Spring Cloud 应用配置多个独立的配置文件，并通过 Nacos 管理这些配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 的目录结构，当前章节为“3.2 Nacos 配置管理”，具体到“3.3.1 ext-config 扩展配置”。
画面 2: 浏览器访问 Nacos 配置中心的页面，显示应用名为 application1 configzhengzhou。
画面 3: 在 Nacos 界面创建新配置，Data ID 为 ext-config-http.yaml，Group 为 COMMON_GROUP。
画面 4: IDE 中展示 bootstrap.yaml 配置文件，其中包含两个 ext-config 配置项，分别指向 ext-config-common01.yaml 和 ext-config-common02.yaml。
画面 5: 在 Nacos 界面编辑配置，配置内容为 HTTP 和 server 相关的设置，包括 encoding、remote_ip_header、protocol_header、context-path 等。
画面 6: IDE 中展示 bootstrap.yaml 配置文件，其中 server.port 设置为 9002，provider.address 设置为 127.0.0.1:9001。
画面 7: IDE 中展示 bootstrap.yaml 配置文件，其中 http 和 server 配置项被高亮显示，包括 encoding、remote_ip_header、context-path 等。
画面 8: 浏览器访问 Nacos 配置中心的页面，显示应用名为 application1 configzhengzhou。
画面 9: 在 Nacos 界面编辑配置，Data ID 为 ext-config-http.yaml，Group 为 COMMON_GROUP。
画面 10: 在 Nacos 界面编辑配置，Data ID 为 ext-config-http.yaml，Group 为 COMMON_GROUP。
画面 11: 在 Nacos 界面编辑配置，Data ID 为 nacos-restful-consumer.yaml，Group 为 DEFAULT_GROUP。
画面 12: IDE 中展示 bootstrap.yaml 配置文件，其中 server.addr 设置为 127.0.0.1:8888，配置文件名与 application.name 对应。
画面 13: 展示课程 PPT 的内容，说明如何将 servlet 公用配置抽离到独立的配置文件。
画面 14: 展示课程 PPT 的内容，介绍 Nacos Server 的安装准备，包括支持的 OS、JDK 版本和 Maven 版本。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4:
```yaml
config:
  server-addr: 127.0.0.1:8888  # 配置中心地址
  file-extension: yaml
  # 指定配置文件的扩展名，配置文件名会根据application.name的值自动加前缀
  ext-config[0]:
    data-id: ext-config-common01.yaml
    group: COMMON_GROUP
    refresh: true
  ext-config[1]:
    data-id: ext-config-common02.yaml
    group: COMMON_GROUP
    refresh: true
```

画面 5:
```yaml
http:
  encoding:
    charset: UTF-8
    force: true
    enabled: true
  messages:
    encoding: UTF-8
server:
  local:
    remote_ip_header: x-forwarded-for
    protocol_header: x-forwarded-proto
    servlet:
      context-path: /
      use-forward-headers: true
```

画面 6:
```yaml
server:
  port: 9002
provider:
  address: 127.0.0.1:9001
spring:
  application:
    name: nacos-restful-consumer  # 服务名
  cloud:
    nacos:
      discovery:
        server-addr: 127.0.0.1:8888  # 服务发现中心地址
        namespace: f8ee3c1-1005-40c9-96a6-8c81f1512ab1  # 指定命名空间的id
      config:
        server-addr: 127.0.0.1:8888  # 配置中心地址
        file-extension: yaml  # 指定配置文件的扩展名，配置文件名会根据application.name的值自动加前缀
        ext-config[0]:
          data-id: ext-config-common01.yaml
          group: COMMON_GROUP
          refresh: true
        ext-config[1]:
          data-id: ext-config-common02.yaml
          group: COMMON_GROUP
          refresh: true
```

画面 7:
```yaml
http:
  encoding:
    charset: UTF-8
    force: true
    enabled: true
  messages:
    encoding: UTF-8
server:
  local:
    remote_ip_header: x-forwarded-for
    protocol_header: x-forwarded-proto
    servlet:
      context-path: /
      use-forward-headers: true
```

画面 12:
```yaml
spring:
  cloud:
    nacos:
      discovery:
        server-addr: 127.0.0.1:8888  # 服务发现中心地址
        namespace: f8ee3c1-1005-40c9-96a6-8c81f1512ab1  # 指定命名空间的id
      config:
        server-addr: 127.0.0.1:8888  # 配置中心地址
        file-extension: yaml  # 指定配置文件的扩展名，配置文件名会根据application.name的值自动加前缀
        ext-config[0]:
          data-id: ext-config-common01.yaml
          group: COMMON_GROUP
          refresh: true
        ext-config[1]:
          data-id: ext-config-common02.yaml
          group: COMMON_GROUP
          refresh: true
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“3.2 Nacos 配置管理”，子标题包括“3.3.1 ext-config 扩展配置”。
画面 13: PPT 标题为“4. 服务和元数据管理”，子标题为“2.2.1 安装 Nacos Server”，内容包括“Nacos 预备 Java 环境来运行”，并列出支持的 OS、JDK 版本和 Maven 版本。
画面 14: PPT 标题为“2.2.2 下载源码或者安装包”，内容包括“你可以通过源码和发行包两种方式来获取 Nacos”，并列出从 GitHub 下载源码的方式。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
