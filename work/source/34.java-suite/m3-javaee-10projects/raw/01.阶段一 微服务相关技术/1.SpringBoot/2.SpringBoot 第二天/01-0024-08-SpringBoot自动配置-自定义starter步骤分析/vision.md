# 画面线理解：08-SpringBoot自动配置-自定义starter步骤分析

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/2.SpringBoot 第二天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\2.SpringBoot 第二天\08-SpringBoot自动配置-自定义starter步骤分析_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:23, 01:52, 02:07, 02:17, 03:01, 03:13, 03:29, 03:44, 03:58, 04:14, 04:28, 04:54, 05:36, 05:48
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 08:59:49

1) 这一组画面整体在讲如何在 Spring Boot 项目中引入 MyBatis Starter 依赖，并查看其内部自动配置类的结构。

2) 按时间顺序列出每张画面的要点：
画面 1: 在 IDEA 中打开 springboot-enable 项目的 pom.xml 文件，显示了当前已有的两个依赖项。
画面 2: 浏览器打开百度链接，页面空白。
画面 3: 浏览器访问 Maven 中央仓库，查看 mybatis-spring-boot-starter 的版本列表，当前选中 1.3.2 版本。
画面 4: 在 IDEA 的 pom.xml 文件中，光标位于 </dependencies> 标签后，准备添加新的依赖。
画面 5: 在 IDEA 的 pom.xml 文件中，光标位于 </dependency> 标签后，准备添加新的依赖。
画面 6: 在 IDEA 中打开 mybatis-spring-boot-starter-1.3.2.pom 文件，查看其内部的依赖结构。
画面 7: 在 IDEA 中打开 mybatis-spring-boot-starter-1.3.2.pom 文件，光标位于 <dependency> 标签内，准备添加新的依赖。
画面 8: 在 IDEA 中查看项目依赖树，展开 mybatis-spring-boot-starter-1.3.2 的依赖项。
画面 9: 在 IDEA 中查看项目依赖树，展开 mybatis-spring-boot-starter-1.3.2 的依赖项。
画面 10: 在 IDEA 中查看项目依赖树，展开 mybatis-spring-boot-starter-1.3.2 的依赖项。
画面 11: 在 IDEA 中查看项目依赖树，展开 mybatis-spring-boot-starter-1.3.2 的依赖项。
画面 12: 在 IDEA 中查看 mybatis-spring-boot-autoconfigure-1.3.2.jar 的 META-INF/spring.factories 文件内容。
画面 13: 在 IDEA 中查看 mybatis-spring-boot-autoconfigure-1.3.2.jar 的 META-INF/spring.factories 文件内容。
画面 14: 展示 PPT 页面，标题为“SpringBoot 自动配置”，内容为“案例：需求 自定义 redis-starter，要求当导入 redis 依赖时，SpringBoot 自动创建 Jedis 的 Bean。”

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面 1:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
</dependency>

<dependency>
    <groupId>com.itheima</groupId>
    <artifactId>springboot-enable-other</artifactId>
    <version>0.1-SNAPSHOT</version>
</dependency>
```

画面 4:
```xml
<dependency>
    <groupId>org.mybatis.spring.boot</groupId>
    <artifactId>mybatis-spring-boot-starter</artifactId>
    <version>1.3.2</version>
</dependency>
```

画面 5:
```xml
<dependency>
    <groupId>org.mybatis.spring.boot</groupId>
    <artifactId>mybatis-spring-boot-starter</artifactId>
    <version>1.3.2</version>
</dependency>
```

画面 6:
```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>1.3.2</version>
</parent>
<artifactId>mybatis-spring-boot-starter</artifactId>
<name>mybatis-spring-boot-starter</name>
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-jdbc</artifactId>
    </dependency>
    <dependency>
        <groupId>org.mybatis.spring.boot</groupId>
        <artifactId>mybatis-spring-boot-autoconfigure</artifactId>
    </dependency>
    <dependency>
        <groupId>org.mybatis</groupId>
        <artifactId>mybatis</artifactId>
    </dependency>
    <dependency>
        <groupId>org.mybatis</groupId>
        <artifactId>mybatis-spring</artifactId>
    </dependency>
</dependencies>
```

画面 8:
```xml
<dependency>
    <groupId>org.mybatis.spring.boot</groupId>
    <artifactId>mybatis-spring-boot-starter</artifactId>
    <version>1.3.2</version>
</dependency>
```

画面 12:
```properties
# Auto Configure
org.springframework.boot.autoconfigure.EnableAutoConfiguration=\
org.mybatis.spring.boot.autoconfigure.MybatisAutoConfiguration
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面 14:
PPT 标题：SpringBoot 自动配置
PPT 内容：案例：需求 自定义 redis-starter，要求当导入 redis 依赖时，SpringBoot 自动创建 Jedis 的 Bean。
