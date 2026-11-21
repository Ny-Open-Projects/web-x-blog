# 画面线理解：16.后台服务系统之编写服务消费方实现

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day03-项目介绍以及开发后台系统
- 源文件：03.阶段三 好客租房(生活服务)项目\day03-项目介绍以及开发后台系统\16.后台服务系统之编写服务消费方实现【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:53, 02:45, 03:33, 04:08, 07:18, 08:14, 08:54, 09:21, 09:56, 10:36, 11:13, 11:44, 12:40
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:36:02

1) 这一组画面整体在讲如何创建并测试一个基于 Spring Boot 和 Dubbo 的消费者服务，包括添加依赖、编写测试类、配置注册中心以及使用 Dubbo Admin 管理服务。

2) 按时间顺序列出每张画面的要点：
画面1：创建新模块，展示项目结构和启动类代码。
画面2：在 pom.xml 中添加 Dubbo 依赖。
画面3：在 pom.xml 中添加 Zookeeper、ZKClient 和自定义服务依赖。
画面4：创建测试类 UserServicetest.java，导入相关包。
画面5：在测试类中声明 UserService 接口并设置 @Reference 注解。
画面6：使用 7zInspector 查看对象结构。
画面7：在测试类中编写测试方法 testQueryAll。
画面8：在测试方法中添加打印语句并运行测试。
画面9：测试失败，提示 Dubbo 协议创建服务器失败。
画面10：在 Typora 中查看文档，说明已成功调用服务。
画面11：在 application.properties 中配置 dubbo.registry.address 和 dubbo.registry.client。
画面12：测试再次运行，日志显示客户端连接成功。
画面13：测试通过，控制台输出查询到的用户列表。
画面14：在 Typora 中查看 Dubbo Admin 的安装和配置说明。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面2：
```xml
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>dubbo</artifactId>
    <version>2.6.4</version>
</dependency>
```

画面3：
```xml
<dependency>
    <groupId>cn.itcast.dubbo</groupId>
    <artifactId>itcast-dubbo-service</artifactId>
    <version>1.0-SNAPSHOT</version>
</dependency>
```

画面4：
```java
package cn.itcast.dubbo;

import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;
```

画面5：
```java
import cn.itcast.dubbo.service.UserService;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;
```

画面6：
（无代码）

画面7：
```java
import cn.itcast.dubbo.service.UserService;
import com.alibaba.dubbo.config.annotation.Reference;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;
```

画面8：
```java
@Reference(version = "1.0.0")
private UserService userService;
```

画面9：
```java
com.alibaba.dubbo.rpc.protocol.dubbo.DubboProtocol.java:100
```

画面10：
（无代码）

画面11：
```properties
dubbo.registry.address = zookeeper://172.16.55.185:2181
dubbo.registry.client = zkclient
```

画面12：
（无代码）

画面13：
（无代码）

画面14：
```properties
dubbo.registry.address = zookeeper://172.16.55.185:2181
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面14：PPT 标题为“3.2.6. dubbo Admin”，内容包括 Dubbo Admin 的介绍、下载地址和安装步骤。

5) 不要评价画面美观，不要输出与课程无关的内容。
