# 画面线理解：22.Nacos-服务发现-Dubbo服务发现-service1微服务

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day01 项目介绍 Nacos Spring Cloud Alibaba
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day01 项目介绍 Nacos Spring Cloud Alibaba\22.Nacos-服务发现-Dubbo服务发现-service1微服务【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:04, 01:13, 01:50, 02:22, 02:58, 03:31, 04:12, 04:52, 05:57, 06:27, 07:10, 07:57, 08:28, 09:41
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:28:27

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Dubbo 和 Nacos 构建微服务架构，包括创建服务接口、服务提供者、服务消费者、配置 Nacos 服务注册与发现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程目录，当前章节为“2.4.1 Dubbo服务架构”，并显示测试成功页面，请求地址为 http://127.0.0.1:56020/service2，显示“consumer dubbo invoke dubboService2 表明service2调用成功”。
画面2：在 IntelliJ IDEA 中，通过“Project Structure”对话框为项目添加新模块，当前选中“service1-server”。
画面3：在 IntelliJ IDEA 中，通过“Project Structure”对话框选择“New Module”并准备创建新模块。
画面4：展示 PPT 页面，标题为“1.1 微服务架构”，内容说明微服务架构将系统拆分为多个独立服务，并展示一个电商系统的架构图（App/Web -> Web App 1, Web App 2, Web App 3）。
画面5：展示 PPT 页面，标题为“2.4.5.2 定义service1-server”，显示 service1-server 的 Maven 项目结构和接口定义。
画面6：在 IntelliJ IDEA 中，展示 service1-server 的 pom.xml 文件，其中包含对 service1-api 和 service2-api 的依赖。
画面7：在 IntelliJ IDEA 中，展示 service1-server 的 pom.xml 文件，其中包含对 spring-cloud-starter-dubbo 和 spring-cloud-starter-alibaba-nacos-discovery 的依赖。
画面8：在 IntelliJ IDEA 中，展示 service1-server 的 ServiceImpl.java 文件，其中实现 ServiceApi 接口并返回 null。
画面9：在 IntelliJ IDEA 中，展示 service1-server 的目录结构，其中包含 bootstrap.yml 文件。
画面10：在 IntelliJ IDEA 中，展示 service1-server 的 bootstrap.yml 文件，其中配置了 dubbo 的 registry 为 Nacos，地址为 nacos://127.0.0.1:8848。
画面11：在 IntelliJ IDEA 中，展示 service1-server 的 ServiceBootstrap.java 文件，其中使用 SpringApplication.run 启动服务。
画面12：在 IntelliJ IDEA 中，展示 service1-consumer 的目录结构，其中包含 ServiceBootstrap.java 文件。
画面13：在 IntelliJ IDEA 中，展示 service1-consumer 的 RestConsumerController.java 文件，其中调用 service2Api.dubboService2()。
画面14：展示 PPT 页面，标题为“2.4.1 Dubbo服务架构”，显示 Dubbo 协议的系统架构图，包括客户端、API 网关、Application-1、Nacos Server、Service-1、Service-2 等组件。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
测试：
请求：http://127.0.0.1:56020/service2
显示：consumer dubbo invoke dubboService2 表明service2调用成功。

画面4：
1.1 微服务架构
为适应企业的业务发展，提高软件研发的生产力，降低软件研发的成本，软件架构也升级和优化，将一个独立的系统拆分成若干小的服务，每个服务运行在不同的进程中，服务与服务之间采用RESTful、RPC等协议传输数据，每个服务所拥有的功能具有独立性强的特点，这样的设计就实现了单个服务的高内聚，服务与服务之间的低耦合效果，这些小服务就是微服务，基于这种设计方法的系统架构即微服务架构。
下图是基于服务架构的电商系统：
App/Web
  ↓
Web App 1
  ↓
Web App 2
  ↓
Web App 3

画面5：
<parent>
    <artifactId>nasco dubbo service</artifactId>
    <groupId>com.ithema.nacos</groupId>
    <version>1.0-SNAPSHOT</version>
</parent>
<modelVersion>4.0.0</modelVersion>
<artifactId>service1-api</artifactId>

3、定义接口
package com.ithema.microservice.service1.api;
public interface ServiceApi {
    public String dubboService();
}

画面6：
<modelVersion>4.0.0</modelVersion>
<artifactId>service1-server</artifactId>
<dependencies>
    <dependency>
        <groupId>com.ithema.nacos</groupId>
        <artifactId>service1-api</artifactId>
        <version>1.0-SNAPSHOT</version>
    </dependency>
    <dependency>
        <groupId>com.ithema.nacos</groupId>
        <artifactId>service2-api</artifactId>
        <version>1.0-SNAPSHOT</version>
    </dependency>
</dependencies>

画面7：
<dependencies>
    <dependency>
        <groupId>com.ithema.nacos</groupId>
        <artifactId>service1-api</artifactId>
        <version>1.0-SNAPSHOT</version>
    </dependency>
    <dependency>
        <groupId>com.ithema.nacos</groupId>
        <artifactId>service2-api</artifactId>
        <version>1.0-SNAPSHOT</version>
    </dependency>
    <dependency>
        <groupId>com.alibaba.cloud</groupId>
        <artifactId>spring-cloud-starter-dubbo</artifactId>
    </dependency>
    <dependency>
        <groupId>com.alibaba.cloud</groupId>
        <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
    </dependency>
</dependencies>

画面8：
package com.ithema.microservice.service1.service;
import com.ithema.microservice.service1.api.ServiceApi;
@Service
public class ServiceImpl implements ServiceApi {
    public String dubboService() {
        return null;
    }
}

画面9：
resources
  api
    ServiceApi.java
  service1-server
    pom.xml
    service1-server.iml
  src
    main
      java
        com.ithema
          microservice
            service1
              service
                ServiceApiImpl.java

画面10：
main:
allow-bean-definition-overriding: true # Spring Boot 2.1 需要开启
cloud:
  nacos:
    server-addr: 127.0.0.1:8848
dubbo:
  scan:
    base-packages: com.ithema.microservice.service1.service
  protocol:
    name: dubbo
    port: 2000
  registry:
    address: nacos://127.0.0.1:8848
    application:
      name: dubbo
      qos-enable: false # Dubbo远程服务也开启
    consumer:
      # 其他配置

画面11：
package com.ithema.microservice.service1;
import ...
@SpringBootApplication
public class ServiceBootstrap {
    public static void main(String[] args) {
        SpringApplication.run(ServiceBootstrap.class, args);
    }
}

画面12：
resources
  bootstrap.yml

画面13：
@GetMapping(value = "/service2")
public String service2(){
    String providerResult = serviceApi.dubboService2();
    return "consumer dubbo invoke " + providerResult;
}

画面14：
2.4.1 Dubbo服务架构
下图是做服务采用Dubbo协议的系统架构图：
客户端
  ↓ HTTP
API网关
  ↓ RESTful
Application-1
  ↓ dubbo
Service-1
  ↓ dubbo
Service-2
组件说明：

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面4：
标题：1.1 微服务架构
内容：
- 说明微服务架构将系统拆分为多个独立服务。
- 展示电商系统的架构图：
  - App/Web 指向 Web App 1、Web App 2、Web App 3。
  - Web App 1、Web App 2、Web App 3 之间通过 REST API 互相连接。

画面14：
标题：2.4.1 Dubbo服务架构
内容：
- 展示 Dubbo 协议的系统架构图：
  - 客户端通过 HTTP 指向 API 网关。
  - API 网关通过 RESTful 指向 Application-1。
  - Application-1 通过 dubbo 指向 Service-1。
  - Service-1 通过 dubbo 指向 Service-2。
  - Service-1 和 Service-2 都指向 Nacos Server（服务发现中心）。
- 组件说明：无具体说明。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）
