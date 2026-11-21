# 画面线理解：10.功能开发之搭建开发环境

- 阶段：07.阶段七 探花交友项目
- 章节：day01 探花交友-项目搭建以及登录完善个人信息
- 源文件：07.阶段七 探花交友项目\day01 探花交友-项目搭建以及登录完善个人信息\10.功能开发之搭建开发环境_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:13, 01:41, 02:34, 02:56, 03:19, 04:03, 04:43, 05:08, 05:37, 06:23, 07:25, 07:43, 08:17, 09:24
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:04:48

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 的注册登录项目（itcast-tanhua）的 Maven 项目结构和依赖配置，包括父工程、子工程（itcast-tanhua 和 itcast-tanhua-ss0）的 pom.xml 文件内容。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示 Typora 编辑器中的文档，标题为“3、注册登录”，子标题“3.1、搭建工程”和“3.1.1、itcast-tanhua”。
- 显示了 itcast-tanhua 父工程的 pom.xml 文件开头部分，包含 XML 声明、命名空间、modelVersion、packaging 和 parent 依赖信息。
- 代码片段：
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <project xmlns="http://maven.apache.org/POM/4.0.0"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
      <modelVersion>4.0.0</modelVersion>
      <packaging>pom</packaging>
      <parent>
          <groupId>org.springframework.boot</groupId>
          <artifactId>spring-boot-starter-parent</artifactId>
          <version>2.1.0.RELEASE</version>
      </parent>
  ```

画面2：
- 继续展示 itcast-tanhua 父工程的 pom.xml 文件，聚焦在 parent 依赖块。
- 代码片段：
  ```xml
  <parent>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-parent</artifactId>
      <version>2.1.0.RELEASE</version>
  </parent>
  ```

画面3：
- 展示 itcast-tanhua 父工程的 pom.xml 文件，聚焦在 properties 依赖版本块。
- 代码片段：
  ```xml
  <!-- 集中定义依赖版本 -->
  <properties>
      <mysql.version>5.1.47</mysql.version>
      <jackson.version>2.9.9</jackson.version>
      <druid.version>1.0.9</druid.version>
      <servlet-api.version>2.5</servlet-api.version>
      <jsp-api.version>2.0</jsp-api.version>
  ```

画面4：
- 展示 itcast-tanhua 父工程的 pom.xml 文件，聚焦在 build 插件块。
- 代码片段：
  ```xml
  <build>
      <plugins>
          <plugin>
              <groupId>org.apache.maven.plugins</groupId>
              <artifactId>maven-compiler-plugin</artifactId>
              <version>3.2</version>
              <configuration>
                  <source>1.8</source>
                  <target>1.8</target>
                  <encoding>UTF-8</encoding>
              </configuration>
          </plugin>
      </plugins>
  </build>
  ```

画面5：
- 展示 IntelliJ IDEA 中的项目结构，左侧显示了项目目录树，右侧显示了 my-tanhua 的 pom.xml 文件内容。
- 代码片段：
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <project xmlns="http://maven.apache.org/POM/4.0.0"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
      <modelVersion>4.0.0</modelVersion>
      <parent>
          <groupId>org.springframework.boot</groupId>
          <artifactId>spring-boot-starter-parent</artifactId>
          <version>2.1.0.RELEASE</version>
      </parent>
      <groupId>cn.itcast.tanhua</groupId>
      <artifactId>my-tanhua</artifactId>
      <version>1.0-SNAPSHOT</version>
  ```

画面6：
- 展示 my-tanhua 的 pom.xml 文件，聚焦在依赖管理部分，显示了 junit 依赖。
- 代码片段：
  ```xml
  <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>4.12</version>
      <scope>test</scope>
  </dependency>
  ```

画面7：
- 展示 my-tanhua 的 pom.xml 文件，聚焦在依赖管理部分，显示了 mybatis-plus 依赖。
- 代码片段：
  ```xml
  <!-- mybatis-plus插件依赖 -->
  <dependency>
      <groupId>com.baomidou</groupId>
      <artifactId>mybatis-plus</artifactId>
      <version>${mybatis.mybatis-plus}</version>
  </dependency>
  ```

画面8：
- 展示 my-tanhua 的 pom.xml 文件，聚焦在依赖管理部分，显示了 MySQL、MongoDB 和 Lombok 依赖。
- 代码片段：
  ```xml
  <dependency>
      <groupId>org.mongodb</groupId>
      <artifactId>mongodb-driver-sync</artifactId>
      <version>3.9.1</version>
  </dependency>
  <dependency>
      <groupId>org.projectlombok</groupId>
      <artifactId>lombok</artifactId>
      <version>${lombok.version}</version>
      <optional>true</optional>
  </dependency>
  ```

画面9：
- 展示 my-tanhua 的 pom.xml 文件，聚焦在依赖管理部分，显示了 commons-lang3 依赖。
- 代码片段：
  ```xml
  <dependency>
      <groupId>org.apache.commons</groupId>
      <artifactId>commons-lang3</artifactId>
      <version>${commons-lang3.version}</version>
  </dependency>
  ```

画面10：
- 展示 my-tanhua 的 pom.xml 文件，聚焦在依赖管理部分，显示了 RocketMQ 和 Jackson 依赖。
- 代码片段：
  ```xml
  <!-- RocketMQ相关 -->
  <dependency>
      <groupId>org.apache.rocketmq</groupId>
      <artifactId>rocketmq-spring-boot-starter</artifactId>
      <version>2.0.0</version>
  </dependency>
  <dependency>
      <groupId>org.apache.rocketmq</groupId>
      <artifactId>rocketmq-client</artifactId>
      <version>4.3.2</version>
  </dependency>
  ```

画面11：
- 展示 my-tanhua-ss0 的 pom.xml 文件，聚焦在 parent 依赖块。
- 代码片段：
  ```xml
  <parent>
      <artifactId>my-tanhua</artifactId>
      <groupId>cn.itcast.tanhua</groupId>
      <version>1.0-SNAPSHOT</version>
  </parent>
  ```

画面12：
- 展示 my-tanhua-ss0 的 pom.xml 文件，聚焦在 dependencies 块，显示了 spring-boot-starter-web 依赖。
- 代码片段：
  ```xml
  <dependencies>
      <dependency>
          <groupId>org.springframework.boot</groupId>
          <artifactId>spring-boot-starter-web</artifactId>
      </dependency>
  </dependencies>
  ```

画面13：
- 展示 my-tanhua-ss0 的 pom.xml 文件，聚焦在 dependencies 块，显示了 Jackson、Spring Boot Data Redis 和 Commons Codec 依赖。
- 代码片段：
  ```xml
  <dependency>
      <groupId>com.fasterxml.jackson.core</groupId>
      <artifactId>jackson-databind</artifactId>
  </dependency>
  <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-data-redis</artifactId>
  </dependency>
  <dependency>
      <groupId>commons-codec</groupId>
      <artifactId>commons-codec</artifactId>
  </dependency>
  ```

画面14：
- 展示 my-tanhua-ss0 的 pom.xml 文件，聚焦在 dependencies 块，显示了 RocketMQ 依赖。
- 代码片段：
  ```xml
  <!-- RocketMQ相关 -->
  <dependency>
      <groupId>org.apache.rocketmq</groupId>
      <artifactId>rocketmq-spring-boot-starter</artifactId>
      <version>2.0.0</version>
  </dependency>
  <dependency>
      <groupId>org.apache.rocketmq</groupId>
      <artifactId>rocketmq-client</artifactId>
      <version>4.3.2</version>
  </dependency>
  ```
