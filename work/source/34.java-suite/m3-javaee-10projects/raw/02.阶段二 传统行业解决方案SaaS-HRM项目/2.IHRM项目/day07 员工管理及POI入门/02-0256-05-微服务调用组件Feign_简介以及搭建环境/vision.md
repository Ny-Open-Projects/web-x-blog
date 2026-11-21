# 画面线理解：05-微服务调用组件Feign：简介以及搭建环境

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day07 员工管理及POI入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day07 员工管理及POI入门\05-微服务调用组件Feign：简介以及搭建环境_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:07, 01:15, 02:21, 02:57, 03:24, 04:15, 04:54, 05:07, 05:52, 06:15, 06:49, 08:07, 09:10, 09:36
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:49:54

1) 这一组画面整体在讲什么（一句话）：
演示如何在微服务架构中使用 Feign 组件实现服务间的远程调用，具体操作包括添加依赖、配置注解、创建接口和修改控制器。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Eureka 服务注册中心页面，显示三个服务实例（IHRM-COMPANY、IHRM-EMPLOYEE、IHRM-SYSTEM）均处于 UP 状态，同时显示了 Windows 开始菜单。
画面2：展示一个流程图，描述 Eureka 服务注册中心与三个微服务（企业微服务、系统微服务、员工微服务）之间的注册关系，以及各服务与对应数据库的连接。
画面3：展示 PPT 页面，标题为“1.5 微服务调用组件Feign”，内容包括 Feign 的简介和快速体验步骤，其中包含添加依赖的 Maven 代码片段。
画面4：展示流程图，与画面2类似，但“企业微服务”框内文字被修改为“根据id请求部门 http接口”。
画面5：展示 PPT 页面，内容为修改 hrm_system 模块启动类添加注解的步骤，包含 @EnableDiscoveryClient 和 @EnableFeignClients 注解。
画面6：展示 PPT 页面，内容为在 hrm_system 模块中创建 com.ihrm.system.client 包并创建接口，以及修改 UserController 的代码。
画面7：展示 Notepad++ 编辑器中的配置文件，内容为服务注册到 Eureka 的配置，包含 server.port、eureka.client.service-url 等配置项。
画面8：展示 IntelliJ IDEA 中的项目结构，显示 hrm_system 模块的目录结构，包括 src/main/java 和 src/main/resources。
画面9：展示 Windows 系统的“显示桌面”功能，显示多个打开的窗口，包括 PPT、IDEA、Notepad++ 等。
画面10：展示 IntelliJ IDEA 中的 SystemApplication.java 文件，包含 Spring Boot 启动类代码，包括 @EnableDiscoveryClient 和 @EnableFeignClient 注解。
画面11：展示 IntelliJ IDEA 中的 DepartmentController.java 文件，包含两个 RESTful 接口方法：findALL 和 findById。
画面12：展示 IntelliJ IDEA 中的 DepartmentFeignClient.java 文件，正在输入 @FeignClient 注解。
画面13：展示 IntelliJ IDEA 中的 DepartmentController.java 文件，显示了 update 和 delete 接口方法。
画面14：展示 IntelliJ IDEA 中的 DepartmentFeignClient.java 文件，显示了 @FeignClient 注解和 findById 接口方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-openfeign</artifactId>
</dependency>
```
画面5：
```java
@EnableDiscoveryClient
@EnableFeignClients
```
画面6：
```java
//测试通过系统微服务调用企业微服务方法
@RequestMapping(value = "/test/{id}")
public void findDeptById(@PathVariable String id){
    Department dept = departmentFeignClient.findById(id);
    System.out.println(dept);
}
```
画面7：
```yaml
#eureka服务的配置文件
server:
  port: 8888 #服务端口
eureka:
  client:
    registerWithEureka: false #是否将自己注册到Eureka服务中，本身就是所有无需注册
    fetchRegistry: false #是否从Eureka中获取注册信息
    serviceUrl:
      defaultZone: http://127.0.0.1:6888/eureka/
#微服务注册到eureka配置
eureka:
  client:
    service-url:
      defaultZone: http://localhost:6888/eureka/
```
画面10：
```java
package com.ihrm.system;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.cloud.openfeign.EnableFeignClients;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication
@EnableDiscoveryClient
@EnableFeignClients
@ComponentScan(basePackages = "com.ihrm")
public class SystemApplication {
    public static void main(String[] args) {
        SpringApplication.run(SystemApplication.class, args);
    }
}
```
画面11：
```java
//企业id，目前使用固定值1，以后会根据企业id查询
//调用service完成保存企业
departmentService.save(department);
return new Result(ResultCode.SUCCESS);
```
画面12：
```java
package com.ihrm.system.client;

import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.PathVariable;

@FeignClient("ihrm-company")
public interface DepartmentFeignClient {

    @RequestMapping(value = "/department/{id}", method = RequestMethod.GET)
    public Result findById(@PathVariable(value = "id") String id);
}
```
画面13：
```java
//根据id删除department
@RequestMapping(value = "/department/{id}", method = RequestMethod.DELETE)
public Result delete(@PathVariable(value = "id") String id) {
    departmentService.delete(id);
    return new Result(ResultCode.SUCCESS);
}
```
画面14：
```java
package com.ihrm.system.client;

import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.PathVariable;

@FeignClient("ihrm-company")
public interface DepartmentFeignClient {

    @RequestMapping(value = "/department/{id}", method = RequestMethod.GET)
    public Result findById(@PathVariable(value = "id") String id);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：流程图结构：
- “eureka 服务”指向“企业微服务”、“系统微服务”、“员工微服务”，标注“注册”；
- “企业微服务”指向“企业库”，标注“根据id请求部门 http接口”；
- “系统微服务”指向“系统库”，标注“根据id请求部门 http接口”；
- “员工微服务”指向“员工”，标注“根据id请求部门 http接口”。

画面3：PPT标题为“1.5 微服务调用组件Feign”，内容包括：
- 1.5.1 简介：Feign 是简化 Java HTTP 客户端开发的工具，灵感来自 Retrofit、JAXRS-2.0 和 WebSocket。
- 1.5.2 快速体验：包括三个步骤，分别对应添加依赖、修改启动类、创建接口。

画面6：PPT标题为“1.5.2 快速体验”，内容包括：
- （4）修改 hrm_system 模块的 UserController，包含测试通过系统微服务调用企业微服务方法的代码。

画面10：PPT标题为“1.5.2 快速体验”，内容包括：
- （2）修改 hrm_system 模块的启动类，添加注解 @EnableDiscoveryClient 和 @EnableFeignClients。

画面12：PPT标题为“1.5.2 快速体验”，内容包括：
- （3）在 hrm_system 模块创建 com.ihrm.system.client 包，包内创建接口。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
