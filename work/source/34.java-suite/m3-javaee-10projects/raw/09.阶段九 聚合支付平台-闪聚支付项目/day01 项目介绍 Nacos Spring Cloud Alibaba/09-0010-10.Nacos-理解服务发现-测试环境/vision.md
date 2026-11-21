# 画面线理解：10.Nacos-理解服务发现-测试环境

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day01 项目介绍 Nacos Spring Cloud Alibaba
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day01 项目介绍 Nacos Spring Cloud Alibaba\10.Nacos-理解服务发现-测试环境【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 02:56, 04:20, 05:46, 06:43, 07:57, 08:57, 10:02, 10:55, 11:59, 13:37, 14:47, 16:15, 17:17
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:20:45

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Spring Boot 和 Nacos 实现服务发现，包括创建父工程、配置依赖、编写服务提供者和消费者代码。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT，标题为“1.2 理解服务发现”，子标题“1.2.1 测试环境”，图示说明服务A调用服务B，服务B的配置文件包含IP和端口。
画面2：展示父工程的pom.xml文件，其中定义了groupId、artifactId、version和packaging，以及依赖管理部分，包含spring-boot-dependencies。
画面3：展示父工程的pom.xml文件，其中定义了groupId、artifactId、version和packaging，以及依赖管理部分，包含spring-boot-dependencies。
画面4：在IDEA中，创建名为“nacos-restful-provider”的模块，设置其为Spring Web项目。
画面5：在IDEA中，打开“Build, Execution, Deployment”设置，配置Maven导入选项。
画面6：在IDEA中，打开“nacos-restful-provider”项目的“RestProviderController.java”文件，准备编写代码。
画面7：在IDEA中，打开“SpringRestProviderBootstrap.java”文件，显示@SpringBootApplication注解和main方法。
画面8：在IDEA中，运行“SpringRestProviderBootstrap”类，控制台显示已连接到目标VM。
画面9：展示父工程的pom.xml文件，其中定义了<parent>标签和<artifactId>nacos-restful-consumer</artifactId>，并展示创建controller的代码。
画面10：展示“RestConsumerController”类的代码，包含@Value("${provider.address}")注解和@GetMapping方法。
画面11：在IDEA中，打开“RestConsumerController.java”文件，显示代码内容。
画面12：在IDEA中，打开“RestConsumerController.java”文件，光标位于restTemplate.getForObject()方法上。
画面13：在IDEA中，打开“SpringRestProviderBootstrap.java”文件，光标位于main方法的return语句上。
画面14：展示课程PPT，标题为“1.2 理解服务发现”，子标题“1.2.1 测试环境”，图示说明服务A调用服务B，服务B的配置文件包含IP和端口。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.ithema.nacos</groupId>
    <artifactId>nacos-discovery</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>

    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-dependencies</artifactId>
                <version>2.1.3.RELEASE</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>
```

画面3：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.ithema.nacos</groupId>
    <artifactId>nacos-discovery</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>

    <dependencyManagement>
        <dependencies>
        </dependencies>
    </dependencyManagement>
```

画面9：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.ithema.nacos</groupId>
        <artifactId>nacos-discovery</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>nacos-restful-consumer</artifactId>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
    </dependencies>
</project>
```

画面10：
```java
package com.ithema.nacos.consumer.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

@RestController
public class RestConsumerController {
    @Value("${provider.address}")
    private String providerAddress;

    @GetMapping(value = "/service")
    public String service() {
        RestTemplate restTemplate = new RestTemplate();
        String providerResult = restTemplate.getForObject("http://" + providerAddress + "/service", String.class);
        return "consumer invoke:" + providerResult;
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：
标题：1.2 理解服务发现
子标题：1.2.1 测试环境
图示：Service A → 调用 Service B
Service B 的配置文件：Service-B 192.168.25.4:8080

画面14：
标题：1.2 理解服务发现
子标题：1.2.1 测试环境
图示：Service A → 调用 Service B
Service B 的配置文件：Service-B 192.168.25.4:8080

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
