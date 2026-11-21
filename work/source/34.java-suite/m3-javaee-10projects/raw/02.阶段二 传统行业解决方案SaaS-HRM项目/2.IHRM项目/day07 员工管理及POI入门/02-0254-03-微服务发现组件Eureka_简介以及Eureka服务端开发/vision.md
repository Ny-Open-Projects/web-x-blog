# 画面线理解：03-微服务发现组件Eureka：简介以及Eureka服务端开发

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day07 员工管理及POI入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day07 员工管理及POI入门\03-微服务发现组件Eureka：简介以及Eureka服务端开发_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:48, 03:00, 03:34, 03:48, 04:06, 04:36, 04:59, 05:16, 06:24, 06:57, 07:31, 08:10, 08:25
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:48:36

1) 这一组画面整体在讲什么（一句话）：
讲解基于 Spring Cloud 的微服务架构中，Eureka 服务注册与发现机制的配置与启动过程，以及 POI 报表的入门知识。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程 PPT 第7章“POI报表的入门”，内容包括“员工管理”、“需求分析”和“数据库表概述”，其中数据库表包括 em_archive、em_positive、em_resignation、em_transferposition。
画面2：与画面1内容相同，为同一页面的重复展示。
画面3：在 IntelliJ IDEA 中，右键点击项目根目录“ihrm_parent”，弹出“New”菜单，准备创建新模块。
画面4：在文件资源管理器中，显示项目目录结构，当前选中“Sql”文件夹，其中包含“员工管理.sql”文件。
画面5：在 IntelliJ IDEA 中打开“ihrm_parent”的 pom.xml 文件，展示父工程的依赖管理，包括 Spring Boot Web、Logging、Test、Fastjson 等依赖。
画面6：在 Notepad++ 中打开“ihrm_parent”的 pom.xml 文件，展示子工程的依赖配置，包括 Spring Cloud Dependencies、Eureka Client、Feign。
画面7：在课程 PPT 中，展示“ihrm_eureka”模块的 pom.xml 文件内容，其中包含 Eureka Server 依赖，并提示“（3）添加 application.yml”。
画面8：在 IntelliJ IDEA 中，右键点击“ihrm_eureka”模块，弹出上下文菜单，准备进行操作。
画面9：在 IntelliJ IDEA 中，打开“ihrm_eureka”模块下的“application.yml”文件，准备进行配置。
画面10：在 IntelliJ IDEA 中，编辑“application.yml”文件，内容为 Eureka 服务的配置，包括 server.port、eureka.client.registerWithEureka、fetchRegistry、serviceUrl、defaultZone。
画面11：在 IntelliJ IDEA 中，打开“EurekaServer.java”文件，准备编写主类。
画面12：在课程 PPT 中，展示“1.4.2 微服务注册”章节，内容为“（1）将其其他微服务模块添加依赖”。
画面13：在浏览器中打开新标签页，准备访问服务。
画面14：在浏览器中访问 Eureka 服务的管理页面，显示“Instances currently registered with Eureka”为空，以及“General Info”中的系统信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面5：
```xml
<parent>
    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
        <java.version>1.8</java.version>
        <fastjson.version>1.2.47</fastjson.version>
    </properties>
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-dependencies</artifactId>
                <version>Finchley.SR1</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>
</parent>
```
画面6：
```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-dependencies</artifactId>
            <version>Finchley.SR1</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-openfeign</artifactId>
</dependency>
```
画面7：
```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-netflix-eureka-server</artifactId>
    </dependency>
</dependencies>
```
画面10：
```yaml
server:
  port: 8888 #服务端口
eureka:
  client:
    registerWithEureka: false #是否将自己注册到Eureka服务中，本身是所有无需注册
    fetchRegistry: false #是否从Eureka中获取注册信息，本身是所有无需注册
    serviceUrl:
      defaultZone: http://127.0.0.1:$(server.port)/eureka/
```
画面11：
```java
package com.ihrm.eureka;
import org.springframework.boot.SpringApplication;
public class EurekaServer {
    public static void main(String[] args) {
        SpringApplication.run(EurekaServer.class, args);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“第7章 POI报表的入门”，子标题包括“1 员工管理”、“1.1 需求分析”、“1.2 数据库表概述”。
画面7：PPT标题为“ihrm_eureka模块pom.xml引入eureka-server”，下方提示“（3）添加application.yml”。
画面12：PPT标题为“1.4.2 微服务注册”，内容为“（1）将其其他微服务模块添加依赖”。
画面14：Eureka 管理页面表格数据包括“Instances currently registered with Eureka”（无实例）和“General Info”（包含 total-avail-memory、environment、num-of-cpus、current-memory-usage）。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
