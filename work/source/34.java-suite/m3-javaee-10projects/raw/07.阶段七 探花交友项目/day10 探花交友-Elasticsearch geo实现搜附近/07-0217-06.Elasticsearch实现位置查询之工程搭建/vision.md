# 画面线理解：06.Elasticsearch实现位置查询之工程搭建

- 阶段：07.阶段七 探花交友项目
- 章节：day10 探花交友-Elasticsearch geo实现搜附近
- 源文件：07.阶段七 探花交友项目\day10 探花交友-Elasticsearch geo实现搜附近\06.Elasticsearch实现位置查询之工程搭建_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:44, 00:56, 01:13, 01:26, 01:36, 01:58, 02:13, 02:32, 02:46, 03:17, 03:31, 03:52, 04:22, 04:41
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:25:12

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中配置 Elasticsearch，包括修改 pom.xml 添加依赖、配置 application.properties 连接集群、配置 log4j.properties 日志以及创建 ESApplication 启动类。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 pom.xml 文件内容，其中包含父项目配置和 <artifactId>my-tanhu-elasticsearch</artifactId>。
画面 2：展示 TodayBestService.java 代码，其中包含使用 RestTemplate 发送 HTTP 请求的逻辑。
画面 3：展示 pom.xml 文件内容，其中包含 <parent> 配置和 <artifactId>my-tanhu-elasticsearch</artifactId>。
画面 4：展示 pom.xml 文件内容，其中包含 <dependencies> 节点下的 spring-boot-starter-web 依赖。
画面 5：展示 pom.xml 文件内容，其中包含 <dependencies> 节点下的 spring-boot-starter-data-elasticsearch 依赖。
画面 6：展示 pom.xml 文件内容，其中包含 <dependencies> 节点下的 spring-boot-starter-test 依赖。
画面 7：展示 pom.xml 文件内容，其中包含 <dependencies> 节点下的 commons-lang3 和 lombok 依赖。
画面 8：展示 application.properties 文件内容，其中配置了 spring.application.name、server.port 和 spring.data.elasticsearch.cluster-nodes。
画面 9：展示 application.properties 文件内容，其中 spring.data.elasticsearch.cluster-nodes 的值被修改为 192.168.31.9300,192.168.31.9301。
画面 10：展示 application.properties 文件内容，其中 spring.data.elasticsearch.cluster-nodes 的值被修改为 192.168.31.9300,192.168.31.9301,192.168.31.9302。
画面 11：展示 log4j.properties 文件内容，其中配置了 log4j.rootLogger、log4j.appender.A1 和 log4j.appender.A1.layout。
画面 12：展示项目结构，选中了 my-tanhu-elasticsearch 模块下的 java 目录。
画面 13：展示 day10.md 文档内容，其中列出了 2.3 application.properties、2.4 log4j.properties 和 2.5 UserLocationES 的标题。
画面 14：展示 day10.md 文档内容，其中列出了 2.4 log4j.properties 和 2.5 UserLocationES 的标题，并显示了 UserLocationES 类的代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <parent>
        <artifactId>my-tanhu</artifactId>
        <groupId>cn.itcast.tanhu</groupId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    <modelVersion>4.0.0</modelVersion>
    <artifactId>my-tanhu-elasticsearch</artifactId>
</project>
```

画面 3：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <parent>
        <artifactId>my-tanhu</artifactId>
        <groupId>cn.itcast.tanhu</groupId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    <modelVersion>4.0.0</modelVersion>
    <artifactId>my-tanhu-elasticsearch</artifactId>
</project>
```

画面 4：
```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
</dependencies>
```

画面 5：
```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-elasticsearch</artifactId>
    </dependency>
</dependencies>
```

画面 6：
```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
</dependencies>
```

画面 7：
```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-elasticsearch</artifactId>
    </dependency>
    <dependency>
        <groupId>org.apache.commons</groupId>
        <artifactId>commons-lang3</artifactId>
    </dependency>
    <dependency>
        <groupId>org.projectlombok</groupId>
        <artifactId>lombok</artifactId>
    </dependency>
</dependencies>
```

画面 8：
```properties
spring.application.name = itcast-tanhu-elasticsearch
server.port = 18082
spring.data.elasticsearch.cluster-name=es-tanhu-cluster
spring.data.elasticsearch.cluster-nodes=192.168.31.9300,192.168.31.9301
```

画面 9：
```properties
spring.data.elasticsearch.cluster-nodes=192.168.31.9300,192.168.31.9301
```

画面 10：
```properties
spring.data.elasticsearch.cluster-nodes=192.168.31.9300,192.168.31.9301,192.168.31.9302
```

画面 11：
```properties
log4j.rootLogger=DEBUG,A1
log4j.appender.A1=org.apache.log4j.ConsoleAppender
log4j.appender.A1.layout=org.apache.log4j.PatternLayout
log4j.appender.A1.layout.ConversionPattern=[%t] [%c]-%p%n
```

画面 13：
```markdown
2.3. application.properties
spring.application.name = itcast-tanhu-elasticsearch
server.port = 18082
spring.data.elasticsearch.cluster-name=es-tanhu-cluster
spring.data.elasticsearch.cluster-nodes=192.168.31.9300,192.168.31.9301,192.168.31.9302

2.4. log4j.properties
log4j.rootLogger=DEBUG,A1
log4j.appender.A1=org.apache.log4j.ConsoleAppender
log4j.appender.A1.layout=org.apache.log4j.PatternLayout
log4j.appender.A1.layout.ConversionPattern=[%t] [%c]-%p%n

2.5. UserLocationES
package com.lanhu.es.pojo;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.elasticsearch.common.geo.GeoPoint;
import org.springframework.data.elasticsearch.annotations.Document;
import org.springframework.data.elasticsearch.annotations.Field;
import org.springframework.data.elasticsearch.annotations.FieldType;
```

画面 14：
```java
package com.lanhu.es;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class ESApplication {
    public static void main(String[] args) {
        SpringApplication.run(ESApplication.class, args);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 13 和 14：显示了 day10.md 文档中的标题和内容，包括 2.3 application.properties、2.4 log4j.properties 和 2.5 UserLocationES 的标题。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
