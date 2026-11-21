# 17-Jaspersoft Studio：整合springboot搭建环境

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day09 图片上传及Jasper
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day09 图片上传及Jasper\17-Jaspersoft Studio：整合springboot搭建环境_【海量资源尽在 ubkz.com】.mp4
- 时长 5分24秒（音频 325s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那我们这个模板文件创建好了那我们这个studio的使命其实就已经结束了那接下来呢我们其实就可以把这个.jasper文件把它放入到我们的Java代码当中是不是通过咱们的一个URL地址进行访问得到一个PDF没错吧所以接下来我们关注的就是如何把生成好的.jasper文件放到
[00:28] 我们的一个工程当中并且创建出web工程可以让他访问得到pdf的最终格式那接着我们来看一下如何去做那首先呢在这边我需要去创建一个新的工程那这个工程呢我就写到刚才我们这个七牛云当中的这个工程里面了就不再去创建了好了那在这边其实呢不管是什么形式的不管是什么样的工程都可以但是应该是一个web工程才对那我这边呢就契合我们的课程
[00:56] 我通过Spring Boot的形式整合上Jasper我们完成报表PDF的一个输出那好了在这边创建一个新的工程new一个modelnextcn.itcast好了那这边呢我们就叫随便来一个吧就叫JasperJasperJSPER Jasper-Spring Boot就叫它吧工程名称OK点击
[01:31] Next好了工程呢创建好了之后我需要对这个工程当中引入箱的坐标那这个坐标在今天的资料当中都已经给各位准备好了好了我们一起来看一下配置文件呢碰文件打开它这里面呢已经给各位准备好了我要用到的碰文件直接把Jasper这相关的Ctrl Ccall到我这边的工程里好了call过来之后
[02:05] 注意这个是一个Spring Boot的程序里面引入了我们JASP的所有的依赖OK那好了接下来既然是一个Spring Boot的工程我需要填写上Spring Boot它的配置文件那这个配置文件呢我从之前的工程这边call一份过来Ctrl C随便拿一个扔到这边好了接下来呢对里面的所有内容呢做一个简单的删减这些我们都不需要我们都不需要
[02:37] 当然了我这边这个工程请求的就叫8181了我随便写的好了那我这个工程名称服务名我也call一下工程名了OK好了这边呢少一个驱动那驱动呢也添加到碰文件里好了从这边直接call过来一份吧JDBC的驱动那抱歉找错了从这边找一个JDBC的驱动Ctrl Ccall到这边
[03:13] OK那JDBC驱动也已经有了这边配置文件不会报错了那除了配置文件之外我们还需要去创建一个我们的启动类好了也从这边callCtrl Ccall到这边把它放到cn.itcast我就放到这个包下了比如说呢我起一个名称就叫做JASPOR applicationOKcall过来那我们这个代码呢我也把这个启动类里面的代码注意启动类里面只需要关注第一个启动方法其实就可以了OK
[03:50] 好了Ctrl Ccall一下名称那接着呢我们上边需要来一注解ata sprint boot application当然了里面可以指定指定我们的scan扫描的base packagescanbase package那我们就叫做cn.itcastOK那好了这样一来我这个基本的配置文件准备好了启动类我也准备好了那接下来我们就开始要做额外的一件事情
[04:22] 那我们这边呢大家都知道我们要做的事情呢其实就是围绕刚才总结的这个开发流程我们模板制作好了那接下来我们要在Java代码当中是不是要对这个模板构造数据要对这个模板进行数据的一个填充最后我们把这个模板转化成PDF那这一步我们如何去做那首先我们所有的这个模板都是以Jasper
[04:50] 文件的形式体现出来的所以我这边需要把这个JASPER文件Ctrl C也引入到我这个工程里那我放到哪我就放到resource目录下了创建一个目录比如说就叫做timelitTemp还有ATS好了放到这个里边Ctrl V那接下来我一会要生成PDF的时候是不是要去读取这个文件那接着往里面填充数据最后导出一个PDF报表
[05:16] OK那这样一来我基本的这个工程搭建的工作就已经都做好了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Spring Boot 集成 JasperReports 实现报表功能，包括项目初始化、依赖配置、数据库连接配置、主程序编写和报表模板设计。

2) 按时间顺序列出每张画面的要点：
画面1：展示 JasperReports 报表生成三阶段（设计、编译、填充）的流程图，并附带文字说明各阶段作用。
画面2：在 IntelliJ IDEA 中创建新 Maven 项目，选择 Maven 模板。
画面3：在 Windows 资源管理器中浏览项目目录结构，右键点击“day1”文件夹。
画面4：在 IntelliJ IDEA 中打开 `pom.xml` 文件，展示已添加的 JasperReports 依赖。
画面5：在 IntelliJ IDEA 中显示项目结构，`pom.xml` 文件位于 `src/main/resources` 目录下。
画面6：在 IntelliJ IDEA 中打开 `application.yml` 文件，展示数据库连接配置和 JWT 配置。
画面7：在 IntelliJ IDEA 中编辑 `pom.xml` 文件，展示 JasperReports 依赖的版本号。
画面8：在 IntelliJ IDEA 中打开 `pom.xml` 文件，展示 `shiro-spring`、`shiro-core`、`shiro-redis` 等依赖。
画面9：在 IntelliJ IDEA 中编辑 `application.yml` 文件，展示 Spring Boot 的 server 和 datasource 配置。
画面10：在 IntelliJ IDEA 中打开 `JasperApplication.java` 文件，展示主类的包名。
画面11：在 IntelliJ IDEA 中编辑 `JasperApplication.java` 文件，添加 Spring Boot 启动注解。
画面12：在 IntelliJ IDEA 中编辑 `JasperApplication.java` 文件，设置 `@SpringBootApplication(scanBasePackages = "cn.itcast")`。
画面13：在 JasperReports Studio 中打开一个空白报表模板，左侧显示项目结构。
画面14：在 IntelliJ IDEA 中打开 `templates` 目录下的 `JasperApplication.java` 文件。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面1：
无代码或配置。

画面2：
无代码或配置。

画面3：
无代码或配置。

画面4：
```xml
<dependency>
    <groupId>org.olap4j</groupId>
    <artifactId>olap4j</artifactId>
    <version>1.2.0</version>
</dependency>
<dependency>
    <groupId>com.lowagie</groupId>
    <artifactId>itext</artifactId>
    <version>2.1.7</version>
</dependency>
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi</artifactId>
    <version>4.0.1</version>
</dependency>
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi-ooxml</artifactId>
    <version>4.0.1</version>
</dependency>
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi-ooxml-schemas</artifactId>
    <version>4.0.1</version>
</dependency>
</dependencies>
```

画面5：
无代码或配置。

画面6：
```yaml
driver-class-name: com.mysql.jdbc.Driver
url: jdbc:mysql://localhost:3306/ihrm?useUnicode=true&characterEncoding=utf8
username: root
password: 111111
jpa:
  database: MySQL
  show-sql: true
  open-in-view: true
  redis:
    host: 127.0.0.1
    port: 6379
  jut:
    config:
      key: saas-ihrm
      ttl: 3600000
    ai:
      appId: 15191975
      apiKey: cy0SlGac93Vtdm420ublbpU
      secretKey: yf1GusMvLbD0nyuLFubhyOd9LEDEZH
    qr:
      url: http://localhost:8080/#/facelogin
```

画面7：
```xml
<dependency>
    <groupId>org.olap4j</groupId>
    <artifactId>olap4j</artifactId>
    <version>1.2.0</version>
</dependency>
<dependency>
    <groupId>com.lowagie</groupId>
    <artifactId>itext</artifactId>
    <version>2.1.7</version>
</dependency>
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi</artifactId>
    <version>4.0.1</version>
</dependency>
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi-ooxml</artifactId>
    <version>4.0.1</version>
</dependency>
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi-ooxml-schemas</artifactId>
    <version>4.0.1</version>
</dependency>
</dependencies>
```

画面8：
```xml
<dependency>
    <groupId>org.apache.shiro</groupId>
    <artifactId>shiro-spring</artifactId>
    <version>1.3.2</version>
</dependency>
<dependency>
    <groupId>org.apache.shiro</groupId>
    <artifactId>shiro-core</artifactId>
    <version>1.3.2</version>
</dependency>
<dependency>
    <groupId>org.apache.shiro</groupId>
    <artifactId>shiro-redis</artifactId>
    <version>3.0.0</version>
</dependency>
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi</artifactId>
    <version>4.0.1</version>
</dependency>
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi-ooxml</artifactId>
    <version>4.0.1</version>
</dependency>
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi-ooxml-schemas</artifactId>
    <version>4.0.1</version>
</dependency>
</dependencies>
```

画面9：
```yaml
server:
  port: 8081
spring:
  application:
    name: jasper-Spring Boot #指定服务名
  datasource:
    driver-class-name: com.mysql.jdbc.Driver
    url: jdbc:mysql://localhost:3306/ihrm?useUnicode=true&characterEncoding=utf8
    username: root
    password: 111111
```

画面10：
无代码或配置。

画面11：
```java
package cn.itcast;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class JasperApplication {
    public static void main(String[] args) {
        SpringApplication.run(JasperApplication.class, args);
    }
}
```

画面12：
```java
package cn.itcast;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication(scanBasePackages = "cn.itcast")
public class JasperApplication {
    public static void main(String[] args) {
        SpringApplication.run(JasperApplication.class, args);
    }
}
```

画面13：
无代码或配置。

画面14：
无代码或配置。

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1：
标题：“4.2 JasperReport原理简述”
流程图：设计阶段（MyReport.jrxml）→ 编译阶段（MyReport.jasper）→ 执行阶段（Data）→ 输出阶段（MyReport.pdf）

5) 不要评价画面美观，不要输出与课程无关的内容。

