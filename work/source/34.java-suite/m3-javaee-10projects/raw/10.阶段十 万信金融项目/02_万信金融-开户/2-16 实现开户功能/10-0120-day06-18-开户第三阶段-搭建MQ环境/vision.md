# 画面线理解：day06-18-开户第三阶段-搭建MQ环境

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-16 实现开户功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-16 实现开户功能\day06-18-开户第三阶段-搭建MQ环境_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:23, 02:14, 02:36, 03:29, 04:05, 04:39, 05:32, 06:09, 07:05, 07:30, 08:52, 09:41, 10:01, 10:20
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:25:55

1) 这一组画面整体在讲什么（一句话）：
演示如何在本地环境安装并启动 RocketMQ，并配置用户中心和存管代理服务以接入 RocketMQ 消息队列。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档，讲解 RocketMQ 环境搭建步骤，列出启动命令。
画面2：展示 RocketMQ 安装目录下的 bin 文件夹，列出启动脚本。
画面3：在命令行中执行启动命令，成功启动 Broker。
画面4：在命令行中执行启动命令，成功启动 NameServer。
画面5：在 IDEA 中查看 pom.xml 文件，展示依赖项。
画面6：展示 PPT 页面，列出 RocketMQ 启动步骤和配置检查项。
画面7：展示课程文档，内容模糊，无法识别具体信息。
画面8：展示课程文档，讲解存管代理服务的配置。
画面9：在浏览器中打开 Apollo 配置中心，显示空页面。
画面10：在 Apollo 配置中心，显示 application 的配置项列表。
画面11：展示课程文档，重复讲解 RocketMQ 启动命令。
画面12：在 IDEA 中查看 application.yml 文件，显示配置内容。
画面13：在 IDEA 控制台中显示配置加载失败的错误日志。
画面14：展示课程文档，讲解存管代理服务的配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
start mqnamesrv.cmd
start mqbroker.cmd -n 127.0.0.1:9876 autoCreateTopicEnable=true
java -jar rocketmq-console-ng-1.0.1.jar --server.port=60000 --rocketmq.config.namesrvAddr=127.0.0.1:9876

画面2：
（无代码或配置）

画面3：
start mqbroker.cmd -n 127.0.0.1:9876 autoCreateTopicEnable=true
The broker[00000000000000000000000000000000] boot success. serializetype=JSON and name server is 127.0.0.1:9876

画面4：
start mqnamesrv.cmd
start mqbroker.cmd -n 127.0.0.1:9876 autoCreateTopicEnable=true
The broker[00000000000000000000000000000000] boot success. serializetype=JSON and name server is 127.0.0.1:9876

画面5：
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-openfeign</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-consul-discovery</artifactId>
</dependency>

画面6：
（无代码或配置）

画面7：
（无代码或配置）

画面8：
<dependency>
    <groupId>org.apache.rocketmq</groupId>
    <artifactId>rocketmq-spring-boot-starter</artifactId>
</dependency>

rocketmq.consumer.group = CTD_P2P_GATEWAY_NOTIFY

画面9：
（无代码或配置）

画面10：
（无代码或配置）

画面11：
start mqnamesrv.cmd
start mqbroker.cmd -n 127.0.0.1:9876 autoCreateTopicEnable=true
java -jar rocketmq-console-ng-1.0.1.jar --server.port=60000 --rocketmq.config.namesrvAddr=127.0.0.1:9876

画面12：
spring:
  application:
    name: warningzp-depository-agent-service
  datasource:
    driver-class-name: com.mysql.cj.jdbc.Driver
    url: jdbc:mysql://localhost:3306/warningzp?useUnicode=true&characterEncoding=utf8&useSSL=false&serverTimezone=Asia/Shanghai
    username: root
    password: 123456
  jpa:
    hibernate:
      ddl-auto: update
    properties:
      hibernate:
        dialect: org.hibernate.dialect.MySQL8Dialect
  redis:
    host: 127.0.0.1
    port: 6379
  rocketmq:
    namesrv-addr: 127.0.0.1:9876
    producer:
      group: CTD_P2P_GATEWAY_NOTIFY
    consumer:
      group: CTD_P2P_GATEWAY_NOTIFY

画面13：
（无代码或配置）

画面14：
<dependency>
    <groupId>org.apache.rocketmq</groupId>
    <artifactId>rocketmq-spring-boot-starter</artifactId>
</dependency>

rocketmq.consumer.group = CTD_P2P_GATEWAY_NOTIFY

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面6：
标题：1. 自行安装和配置 RocketMQ，然后去安装目录的 bin 文件中执行下面命令启动 RocketMQ
标题：4. 检查用户中心和存管代理服务 application.yml 中是否引入 mq 的名称空间
内容：（无具体架构图或流程图）

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
