# 画面线理解：02-Shiro与Springboot整合：配置依赖改造登录方法

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\02-Shiro与Springboot整合：配置依赖改造登录方法_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 01:00, 02:19, 02:28, 02:53, 03:17, 06:03, 06:23, 06:41, 07:15, 08:05, 08:45, 09:30, 11:20
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:27:40

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中集成 Apache Shiro 进行用户认证，重点讲解登录接口中如何使用 Shiro 的 Subject.login 方法进行认证，并展示密码加密（MD5）的实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 ShiroApplication 启动类，包含 @SpringBootApplication 和 @EntityScan 注解，以及一个自定义的 OpenEntityManagerInViewFilter。
画面2：展示 UserController 中的增删改查接口和登录接口，登录接口目前仅打印日志。
画面3：展示项目目录结构，重点指向 shiro_springboot 目录下的 pom.xml 文件。
画面4：展示 pom.xml 中的 <repositories> 配置，包含 Spring Snapshots 和 Spring Milestones 仓库。
画面5：展示 pom.xml 中的 <dependencies> 部分，包含 mysql-connector-java、shiro-spring、shiro-redis 等依赖。
画面6：展示 UserController 的登录方法，准备添加 Shiro 认证逻辑。
画面7：在登录方法中，开始使用 Shiro 的 UsernamePasswordToken 和 SecurityUtils.getSubject()。
画面8：继续编写登录方法，准备获取 Subject。
画面9：展示 IDE 中的自动补全建议，包括 Shiro 的相关工具类。
画面10：在登录方法中添加 try-catch 块，用于捕获异常。
画面11：在 try 块中，使用 SecurityUtils.getSubject() 获取当前用户 Subject。
画面12：在 try 块中，调用 subject.login(upToken) 进行认证。
画面13：在 try 块中，使用 new Md5Hash() 对密码进行加密，准备生成 UsernamePasswordToken。
画面14：在 try 块中，使用 Md5Hash 对密码、用户名和迭代次数进行加密，生成 UsernamePasswordToken。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
package cn.itcast.shiro;

import ...

@SpringBootApplication(scanBasePackages = "cn.itcast.shiro")
@EntityScan("cn.itcast.shiro.domain")
public class ShiroApplication {
    public static void main(String[] args) {
        SpringApplication.run(ShiroApplication.class, args);
    }

    @Bean
    public OpenEntityManagerInViewFilter openEntityManagerInViewFilter() { return new OpenEntityManagerInViewFilter(); }
}
```

画面2：
```java
//添加
@RequestMapping(value = "/user",method = RequestMethod.POST)
public String add() { return "添加用户成功"; }

//查询
@RequestMapping(value = "/user",method = RequestMethod.GET)
public String find() { return "查询用户成功"; }

//更新
@RequestMapping(value = "/user/{id}",method = RequestMethod.GET)
public String update(String id) { return "更新用户成功"; }

//删除
@RequestMapping(value = "/user/{id}",method = RequestMethod.DELETE)
public String delete() { return "删除用户成功"; }

//用户登录
@RequestMapping(value = "/login")
public String login(String username,String password) {
    System.out.println("用户登录");
    return "登录成功";
}
```

画面3：
```
day1
day2
day3
day4
day5
day6
day7
day8
day9
day10
day11
day12
day13
day14
shiro案例代码
shiro_springboot
idea
src
main
java
cn
itcast
shiro
controller
dao
domain
service
test
target
```

画面4：
```xml
<repositories>
    <repository>
        <id>spring-snapshots</id>
        <name>Spring Snapshots</name>
        <url>https://repo.spring.io/snapshot</url>
        <snapshots>
            <enabled>true</enabled>
        </snapshots>
    </repository>
    <repository>
        <id>spring-milestones</id>
        <name>Spring Milestones</name>
        <url>https://repo.spring.io/milestone</url>
        <snapshots>
            <enabled>false</enabled>
        </snapshots>
    </repository>
</repositories>

<pluginRepositories>
    <pluginRepository>
        <id>spring-snapshots</id>
        <name>Spring Snapshots</name>
        <url>https://repo.spring.io/snapshot</url>
        <snapshots>
            <enabled>true</enabled>
        </snapshots>
    </pluginRepository>
</pluginRepositories>
```

画面5：
```xml
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>5.1.16</version>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
<dependency>
    <groupId>org.apache.shiro</groupId>
    <artifactId>shiro-spring</artifactId>
    <version>1.3.2c</version>
</dependency>
<dependency>
    <groupId>org.apache.shiro</groupId>
    <artifactId>shiro-core</artifactId>
    <version>1.3.2c</version>
</dependency>
<dependency>
    <groupId>org.apache.shiro</groupId>
    <artifactId>shiro-redis</artifactId>
    <version>3.0.0</version>
</dependency>
```

画面6：
```java
//用户登录
@RequestMapping(value = "/login")
public String login(String username,String password) {
    System.out.println("用户登录");
    return "登录成功";
}
```

画面7：
```java
//用户登录
@RequestMapping(value = "/login")
public String login(String username,String password) {
    //构造登录令牌
    UsernamePasswordToken upToken = new UsernamePasswordToken(username,password);
    //获取subject
    Subject subject = SecurityUtils.getSubject();
    //2.调用subject进行登录
    subject.login(upToken);
    return "登录成功";
}
```

画面8：
```java
//用户登录
@RequestMapping(value = "/login")
public String login(String username,String password) {
    //构造登录令牌
    UsernamePasswordToken upToken = new UsernamePasswordToken(username,password);
    //获取subject
    Subject subject = SecurityUtils.getSubject();
    //2.调用subject进行登录
    subject.login(upToken);
    return "登录成功";
}
```

画面9：
```java
//用户登录
@RequestMapping(value = "/login")
public String login(String username,String password) {
    //构造登录令牌
    UsernamePasswordToken upToken = new UsernamePasswordToken(username,password);
    //获取subject
    Subject subject = SecurityUtils.getSubject();
    //2.调用subject进行登录
    subject.login(upToken);
    return "登录成功";
}
```

画面10：
```java
//用户登录
@RequestMapping(value = "/login")
public String login(String username,String password) {
    try {
    } catch (Exception e) {
    }
}
```

画面11：
```java
//用户登录
@RequestMapping(value = "/login")
public String login(String username,String password) {
    try {
        //获取subject
        Subject subject = SecurityUtils.getSubject();
        //2.调用subject进行登录
        subject.login(upToken);
        return "登录成功";
    } catch (Exception e) {
        return "用户登录失败";
    }
}
```

画面12：
```java
//用户登录
@RequestMapping(value = "/login")
public String login(String username,String password) {
    try {
        //获取subject
        Subject subject = SecurityUtils.getSubject();
        //2.调用subject进行登录
        subject.login(upToken);
        return "登录成功";
    } catch (Exception e) {
        return "用户登录失败";
    }
}
```

画面13：
```java
//用户登录
@RequestMapping(value = "/login")
public String login(String username,String password) {
    try {
        //构造登录令牌
        UsernamePasswordToken upToken = new UsernamePasswordToken(username,password);
        //获取subject
        Subject subject = SecurityUtils.getSubject();
        //2.调用subject进行登录
        subject.login(upToken);
        return "登录成功";
    } catch (Exception e) {
        return "用户登录失败";
    }
}
```

画面14：
```java
//用户登录
@RequestMapping(value = "/login")
public String login(String username,String password) {
    try {
        //构造登录令牌
        UsernamePasswordToken upToken = new UsernamePasswordToken(username,password);
        //获取subject
        Subject subject = SecurityUtils.getSubject();
        //2.调用subject进行登录
        subject.login(upToken);
        return "登录成功";
    } catch (Exception e) {
        return "用户登录失败";
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
