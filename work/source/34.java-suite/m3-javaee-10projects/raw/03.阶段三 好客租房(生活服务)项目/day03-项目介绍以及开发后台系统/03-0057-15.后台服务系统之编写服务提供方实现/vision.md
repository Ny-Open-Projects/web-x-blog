# 画面线理解：15.后台服务系统之编写服务提供方实现

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day03-项目介绍以及开发后台系统
- 源文件：03.阶段三 好客租房(生活服务)项目\day03-项目介绍以及开发后台系统\15.后台服务系统之编写服务提供方实现【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:00, 01:17, 02:11, 03:20, 04:26, 05:07, 06:35, 07:43, 09:06, 12:59, 14:37, 16:22, 16:55, 18:40
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:35:33

1) 这一组画面整体在讲什么（一句话）：
创建并配置一个基于 Spring Boot 和 Dubbo 的服务提供方项目，包括工程初始化、依赖管理、POJO 类定义、服务接口与实现类编写以及配置文件设置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示创建新工程的对话框，Group ID 为 cn.itcast.dubbo，Artifact ID 为 itcast-dubbo，Version 为 1.0-SNAPSHOT。
画面 2: 在 IntelliJ IDEA 中，右键点击项目，选择“Add Framework Support...”，并选择 Spring。
画面 3: 编辑父项目的 pom.xml，添加 Spring Boot 的 parent 依赖。
画面 4: 编辑父项目的 pom.xml，添加 Spring Boot Test 依赖。
画面 5: 编辑父项目的 pom.xml，添加 Dubbo Spring Boot 依赖。
画面 6: 编辑子模块的 pom.xml，添加 ZooKeeper、gRPC、Dubbo 依赖。
画面 7: 编辑 User.java 文件，定义 User 类的属性和方法。
画面 8: 编辑 UserServiceImpl.java 文件，实现 UserSerivce 接口的 queryAll 方法。
画面 9: 显示一个空白的流程图或架构图。
画面 10: 编辑 application.properties 文件，配置 Spring Boot 和 Dubbo 相关属性。
画面 11: 在 application.properties 文件中，将 dubbo.protocol.port 设置为 20880。
画面 12: 编辑 DubboProvider.java 文件，使用 @SpringBootApplication 注解并配置主方法。
画面 13: 运行 DubboProvider.java，控制台输出 Dubbo 客户端连接信息。
画面 14: 显示 User.java 文件，定义 User 类的属性和方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
Group Id: cn.itcast.dubbo
Artifact Id: itcast-dubbo
Version: 1.0-SNAPSHOT

画面 2:
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>cn.itcast.dubbo</groupId>
    <artifactId>itcast-dubbo</artifactId>
    <version>1.0-SNAPSHOT</version>
</project>

画面 3:
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <!-- 添加springBoot parent支持 -->
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.0.0.RELEASE</version>
    </parent>
    <groupId>cn.itcast.dubbo</groupId>
    <artifactId>itcast-dubbo</artifactId>
    <version>1.0-SNAPSHOT</version>
    <modules>
        <module>itcast-dubbo-service</module>
    </modules>
</project>

画面 4:
<dependencies>
    <!-- 添加springboot测试 -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
</dependencies>

画面 5:
<dependencies>
    <!-- 添加springboot测试 -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
    <!-- 添加dubbo的springboot依赖 -->
    <dependency>
        <groupId>com.alibaba.boot</groupId>
        <artifactId>dubbo-spring-boot-starter</artifactId>
        <version>0.2.0</version>
    </dependency>
</dependencies>

画面 6:
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <artifactId>itcast-dubbo</artifactId>
    <groupId>cn.itcast.dubbo</groupId>
    <version>1.0-SNAPSHOT</version>
    <artifactId>itcast-dubbo-service</artifactId>
    <dependencies>
        <!-- 添加springboot依赖，加web项目 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.apache.zookeeper</groupId>
            <artifactId>zookeeper</artifactId>
            <version>3.4.13</version>
        </dependency>
        <dependency>
            <groupId>com.github.sgroschupf</groupId>
            <artifactId>zkclient</artifactId>
            <version>0.1.0</version>
        </dependency>
    </dependencies>
</project>

画面 7:
package cn.itcast.dubbo.pojo;
/**
 * 作用：dubbo要求传输的对象必须实现序列化接口
 */
public class User implements java.io.Serializable {
    private static final long serialVersionUID = -7341603993352159322L;
    private Long id;
    private String username;
    private String password;
    private Integer age;
    public Long getId() {
        return id;
    }
    public void setId(Long id) {
        this.id = id;
    }
    public String getUsername() {
        return username;
    }
    public void setUsername(String username) {
        this.username = username;
    }
    public String getPassword() {
        return password;
    }
    public void setPassword(String password) {
        this.password = password;
    }
    public Integer getAge() {
        return age;
    }
    public void setAge(Integer age) {
        this.age = age;
    }
}

画面 8:
package cn.itcast.dubbo.service.impl;
import java.util.ArrayList;
import java.util.List;
import cn.itcast.dubbo.pojo.User;
import cn.itcast.dubbo.service.UserService;
import com.alibaba.dubbo.config.annotation.Service;
UserServiceVersion = "${dubbo.service.version}"; //声明这是一个dubbo服务
public class UserServiceImpl implements UserService {
    //实现查询，这里随机从实现，不能具体的数据库查询
    public List<User> queryAll() {
        List<User> list = new ArrayList<User>();
        for (int i = 0; i < 10; i++) {
            User user = new User();
            user.setId(Long.valueOf(i + 1));
            user.setPassword("123456");
            user.setUsername("username" + i);
            list.add(user);
        }
        return list;
    }
}

画面 10:
# Spring boot application
spring.application.name = itcast-dubbo-service
server.port = 9090
# Service version
dubbo.service.version = 1.0.0
# 服务扫描包
dubbo.scan.basePackages = cn.itcast.dubbo.service
# 应用名称
dubbo.application.name = dubbo-provider-demo
# 协议以及端口
dubbo.protocol.name = dubbo
dubbo.protocol.port = 20880
# zk注册中心
dubbo.registry.address = zookeeper://172.16.55.185:2181
dubbo.registry.client = zkclient

画面 12:
package cn.itcast.dubbo;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.WebApplicationType;
import org.springframework.boot.autoconfigure.SpringBootApplication;
@SpringBootApplication
public class DubboProvider {
    public static void main(String[] args) {
        new SpringApplicationBuilder(DubboProvider.class)
                .web(WebApplicationType.NONE) // 非 Web 应用
                .run(args);
    }
}

画面 14:
package cn.itcast.dubbo.pojo;
/**
 * 作用：dubbo要求传输的对象必须实现序列化接口
 */
public class User implements java.io.Serializable {
    private static final long serialVersionUID = -7341603993352159322L;
    private Long id;
    private String username;
    private String password;
    private Integer age;
    public Long
