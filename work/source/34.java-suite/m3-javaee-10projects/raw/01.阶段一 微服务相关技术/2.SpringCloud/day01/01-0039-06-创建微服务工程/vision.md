# 画面线理解：06-创建微服务工程

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day01
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day01\06-创建微服务工程_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:49, 01:53, 01:59, 02:35, 03:00, 03:30, 03:43, 03:59, 04:43, 05:23, 05:30, 05:42, 06:33, 06:52
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:09:55

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中创建并配置 Spring Cloud 微服务工程的父工程和子模块，包括 pom.xml 文件的结构和依赖管理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程 PPT 页面，标题为“5. Spring Cloud概述”，内容包括 Spring Cloud 的组件和版本特征。
画面2：在 IntelliJ IDEA 中，鼠标悬停在“Build”菜单上，显示下拉菜单选项。
画面3：在 IntelliJ IDEA 中，项目结构显示为“http-demo”，但未展开具体模块。
画面4：在 IntelliJ IDEA 中，右键点击项目“helma-springcloud”，弹出菜单，选择“New” -> “Module...”。
画面5：在 IntelliJ IDEA 中，打开并显示“pom.xml”文件，内容为父工程的 Maven 配置。
画面6：在 IntelliJ IDEA 中，项目结构中显示了“helma-springcloud”父工程和“user-service”、“consumer-demo”子模块。
画面7：在 IntelliJ IDEA 中，项目结构中显示了“helma-springcloud”父工程和“user-service”、“consumer-demo”子模块，但“pom.xml”文件未完全展开。
画面8：在 IntelliJ IDEA 中，显示“pom.xml”文件内容，包含父工程的 <properties> 和 <dependencyManagement> 部分。
画面9：在 IntelliJ IDEA 中，显示“pom.xml”文件内容，包含 <build> 部分，其中定义了 <plugins>。
画面10：展示课程 PPT 页面，标题为“6. 创建微服务工程”，内容包括工程需求和分析。
画面11：在 IntelliJ IDEA 中，显示“pom.xml”文件内容，包含 <dependencyManagement> 部分，其中定义了 <dependency>。
画面12：展示课程 PPT 页面，标题为“6. 创建微服务工程”，内容包括工程需求和分析，下方显示了 <dependency> 的代码片段。
画面13：在 IntelliJ IDEA 中，显示“pom.xml”文件内容，包含 <dependencyManagement> 部分，其中定义了 <dependency>。
画面14：展示课程 PPT 页面，标题为“7. 搭建配置user-service工程”，内容包括工程目标和分析，下方显示了 <dependency> 的代码片段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面5：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.itheima</groupId>
    <artifactId>helma-springcloud</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>
    <modules>
        <module>user-service</module>
        <module>consumer-demo</module>
    </modules>
</project>
```

画面8：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.itheima</groupId>
    <artifactId>helma-springcloud</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>
    <modules>
        <module>user-service</module>
        <module>consumer-demo</module>
    </modules>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.5.RELEASE</version>
        <relativePath/>
    </parent>
    <properties>
        <java.version>1.8</java.version>
        <spring-cloud.version>Greenwich.SR1</spring-cloud.version>
        <mapper-starter.version>2.1.5</mapper-starter.version>
        <mysql.version>5.1.46</mysql.version>
    </properties>
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-dependencies</artifactId>
                <version>${spring-cloud.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
            <dependency>
                <groupId>org.mybatis.spring.boot</groupId>
                <artifactId>mybatis-spring-boot-starter</artifactId>
                <version>${mapper-starter.version}</version>
            </dependency>
            <dependency>
                <groupId>mysql</groupId>
                <artifactId>mysql-connector-java</artifactId>
                <version>${mysql.version}</version>
            </dependency>
        </dependencies>
    </dependencyManagement>
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
```

画面11：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.itheima</groupId>
    <artifactId>helma-springcloud</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>
    <modules>
        <module>user-service</module>
        <module>consumer-demo</module>
    </modules>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.5.RELEASE</version>
        <relativePath/>
    </parent>
    <properties>
        <java.version>1.8</java.version>
        <spring-cloud.version>Greenwich.SR1</spring-cloud.version>
        <mapper-starter.version>2.1.5</mapper-starter.version>
        <mysql.version>5.1.46</mysql.version>
    </properties>
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-dependencies</artifactId>
                <version>${spring-cloud.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
            <dependency>
                <groupId>org.mybatis.spring.boot</groupId>
                <artifactId>mybatis-spring-boot-starter</artifactId>
                <version>${mapper-starter.version}</version>
            </dependency>
            <dependency>
                <groupId>mysql</groupId>
                <artifactId>mysql-connector-java</artifactId>
                <version>${mysql.version}</version>
            </dependency>
        </dependencies>
    </dependencyManagement>
</project>
```

画面12：
```xml
<!-- springCloud -->
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-dependencies</artifactId>
    <version>${spring-cloud.version}</version>
    <type>pom</type>
    <scope>import</scope>
</dependency>
```

画面13：
```xml
<!-- springCloud -->
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-dependencies</artifactId>
    <version>${spring-cloud.version}</version>
    <type>pom</type>
    <scope>import</scope>
</dependency>
```

画面14：
```xml
<!-- springCloud -->
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-dependencies</artifactId>
    <version>${spring-cloud.version}</version>
    <type>pom</type>
    <scope>import</scope>
</dependency>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：标题为“5. Spring Cloud概述”，内容包括：
- 目标：Spring Cloud整合的组件和版本特征。
- 小结：
  - 整合的组件可以有很多组件：常见的组件有：eureka注册中心，Gateway网关，Ribbon负载均衡，Feign服务调用，Hystrix熔断器。在有需要的时候项目添加对应的启动器依赖即可。
  - 版本特征：以英文单词命名（伦敦地铁站名）。

画面10：标题为“6
