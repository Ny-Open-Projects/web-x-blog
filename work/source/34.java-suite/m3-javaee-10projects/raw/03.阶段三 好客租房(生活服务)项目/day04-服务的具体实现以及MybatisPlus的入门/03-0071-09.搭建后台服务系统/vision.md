# 画面线理解：09.搭建后台服务系统

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day04-服务的具体实现以及MybatisPlus的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day04-服务的具体实现以及MybatisPlus的入门\09.搭建后台服务系统【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 02:20, 03:31, 03:47, 04:12, 04:47, 05:06, 05:24, 05:40, 05:59, 06:23, 06:46, 07:13, 07:38
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:44:07

1) 这一组画面整体在讲什么（一句话）：
搭建基于 Spring Boot 和 Dubbo 的后台管理系统，包括创建工程、配置 Maven 依赖和模块结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PDF 文档内容，标题为“3. 搭建后台服务系统”，说明后台服务系统采用 SOA 架构，使用 Dubbo 作为服务治理框架进行搭建。同时显示了示例用户数据（JSON 格式）。
画面2：展示工程结构图，包含“itcast-haoke-manage”、“itcast-haoke-manage-api-server”和“itcast-haoke-manage-dubbo-server”三个模块。同时显示了 pom.xml 文件的开头部分。
画面3：展示 pom.xml 文件内容，包含父项目配置，<artifactId>spring-boot-starter-parent</artifactId>，<version>2.1.0.RELEASE</version>。
画面4：在 IntelliJ IDEA 中，右键点击项目目录，弹出菜单，选择“Add Framework Support...”。
画面5：在 IntelliJ IDEA 中，展示 pom.xml 文件内容，包含父项目配置和模块声明。
画面6：在 IntelliJ IDEA 中，展示 pom.xml 文件内容，包含模块声明。
画面7：展示 PDF 文档内容，显示了 Maven 依赖部分，包括 spring-boot-starter-test、zookeeper、agroal、dubbo-spring-boot-starter 等依赖。
画面8：展示 PDF 文档内容，显示了 Maven 依赖部分，包括 spring-boot-starter-test、dubbo-spring-boot-starter、dubbo、commons-lang3、zookeeper、agroal 等依赖。
画面9：在 IntelliJ IDEA 中，展示 pom.xml 文件内容，包含 spring-boot-starter-test、dubbo-spring-boot-starter、dubbo、commons-lang3、zookeeper、agroal 等依赖。
画面10：在 IntelliJ IDEA 中，展示 pom.xml 文件内容，包含 spring-boot-starter-test、dubbo-spring-boot-starter、dubbo、commons-lang3、zookeeper、agroal 等依赖。
画面11：在 IntelliJ IDEA 中，展示 pom.xml 文件内容，包含 spring-boot-starter-test、dubbo-spring-boot-starter、dubbo、commons-lang3、zookeeper、agroal 等依赖。
画面12：展示 PDF 文档内容，显示了 Maven 依赖部分，包括 spring-boot-starter-test、dubbo-spring-boot-starter、dubbo、commons-lang3、zookeeper、agroal 等依赖。
画面13：在 IntelliJ IDEA 中，展示 pom.xml 文件内容，包含 spring-boot-starter-web 依赖。
画面14：展示 PDF 文档内容，标题为“3. 搭建后台服务系统”，说明后台服务系统采用 SOA 架构，使用 Dubbo 作为服务治理框架进行搭建。同时显示了示例用户数据（JSON 格式）。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```json
User{id=1, name=John, age=18, email=test1@acmam300.com}
User{id=2, name=Jack, age=20, email=test2@acmam300.com}
User{id=3, name=Tom, age=28, email=test3@acmam300.com}
User{id=4, name=Family, age=23, email=test4@acmam300.com}
User{id=5, name=Dillo, age=24, email=test5@acmam300.com}
User{id=6, name=li1, age=28, email=zhangan@qgq.com}
```

画面2：
```xml
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>cn.itcast.haoke</groupId>
  <artifactId>itcast-haoke-manage</artifactId>
  <version>1.0-SNAPSHOT</version>
  <packaging>pom</packaging>
  <modules>
    <module>itcast-haoke-manage-api-server</module>
    <module>itcast-haoke-manage-dubbo-server</module>
  </modules>
</project>
```

画面3：
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
    <groupId>cn.itcast.haoke</groupId>
    <artifactId>itcast-haoke-manage</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>
    <modules>
        <module>itcast-haoke-manage-api-server</module>
        <module>itcast-haoke-manage-dubbo-server</module>
    </modules>
</project>
```

画面4：
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
    <groupId>cn.itcast.haoke</groupId>
    <artifactId>itcast-haoke-manage</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>
    <modules>
        <module>itcast-haoke-manage-api-server</module>
        <module>itcast-haoke-manage-dubbo-server</module>
    </modules>
</project>
```

画面5：
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
    <groupId>cn.itcast.haoke</groupId>
    <artifactId>itcast-haoke-manage</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>
    <modules>
        <module>itcast-haoke-manage-api-server</module>
        <module>itcast-haoke-manage-dubbo-server</module>
    </modules>
</project>
```

画面6：
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
    <groupId>cn.itcast.haoke</groupId>
    <artifactId>itcast-haoke-manage</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>
    <modules>
        <module>itcast-haoke-manage-api-server</module>
        <module>itcast-haoke-manage-dubbo-server</module>
    </modules>
</project>
```

画面7：
```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>org.apache.zookeeper</groupId>
        <artifactId>zookeeper</artifactId>
        <version>
