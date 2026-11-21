# 06.Elasticsearch实现位置查询之工程搭建

- 阶段：07.阶段七 探花交友项目
- 章节：day10 探花交友-Elasticsearch geo实现搜附近
- 源文件：07.阶段七 探花交友项目\day10 探花交友-Elasticsearch geo实现搜附近\06.Elasticsearch实现位置查询之工程搭建_【海量资源尽在 666java.com】.mp4
- 时长 4分52秒（音频 293s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那我们接着继续那么接下来呢我们就来搭建我们的这个工程那么前面呢我们已经完成了Elixir集群的一个搭建那么下面呢我们需要搭建工程来编写这个代码那我们解释一下为什么需要重新再搭建一个工程呢原因是呢我们的Elixir它的本身的一个逻辑
[00:20] 跟我们之前这个逻辑是相对比较独立的一个逻辑所以说我们需要搭建一个工程来去写这个逻辑然后我们对外去开放一个接口然后我们只需要在我们的W中去调用这个接口服务就可以了好那么接下来我们先把这个工程创建出来那我们就叫这什么叫ITcast探花然后ElectroSearch
[00:48] 那么我们到这个位置来当然了我们就改个名字了对吧创建一个子模块有点卡稍等一下那么这个位置呢有一个创建一个module然后呢下一步然后呢我们把它设置为idcast我们把它设置为什么呢这个麦探花elastic然后点击下一步啊然后点击finish完成好那么这个工程呢就创建好了接下来呢我们把这个相关的依赖呢我们导入进来
[01:20] 拷贝一下这个不能这么抠得这么来抠我们拷贝下面的单独来拷贝下面的依赖然后我们把它拷到这里好那么接下来我们来看一下依赖有哪些那么首先引入我们web因为我们是需要对外提供接口的引入web
[01:48] 然后呢我们去引入我们的一个这个elag search这个start对吧就是spinbook的对他的一个支持然后呢下面这个是我们的测试下面是其他的一些工具包的依赖啊这个comlang包和这个langbook包那么引入完成之后呢我们就接下来创建我们的配置文件那么我们把这个配置文件呢拿过来那么这块呢我们就写一个application.publish文件
[02:18] 那么我们就把这个内容呢我们也拷贝过来来看一下这里面的配置项那么首先呢这是指定它一个application的一个name然后呢下面这个是端口然后呢这个呢是我们的集群的名字注意这个名字要和我们刚刚所创建的集群的名字呢要一致啊那么就是在这个位置啊这个名字要一致然后呢我们需要给它设置我们的一个就是nodes
[02:46] 那么要注意node时中的这个端口是9300不是9200因为他走的是我们的一个这个就是服务的一个接口并不是一个web的一个这样的一个界面的一个接口所以说呢要注意了这个是9300这个别搞错然后呢接下来呢我们来看一下这个是他的一个配置项然后呢我们再来去设置他的一个这个log4j的一个配置文件
[03:16] 那设置一个log4d的配置文件好那么哎那我们就把这个内容呢也拷贝过来好那么我这样的话呢我们是不是基本呢哎就搞定了对吧那么接下来呢我们就需要去给他设置一个启动类那我们把它设置为叫什么呢叫我们来看一下这个包啊最好和我们其他的保持一致啊那我们来看一下它那么我们就应该叫什么呢这个下面我们应该就叫
[03:46] com.tank花然后点什么呢ES吧好然后呢我们在这个下面去写一个启动类那我们就把这个启动类拷贝过来吧就它然后呢我们拷贝到这个里面来改个名字啊就叫什么呢ESESobligation啊这样的一个启动类然后呢我们来看一下这个扫描包就不需要了把一些相关的包去除掉然后呢把它呢就
[04:13] 丢过来那么这样的话我们基本的一个框架是不是就已经搭建完成了那么下面我们是不是就可以去编写具体代码了我们就把它就写到这来我们就写到这个里面来这是我们的一个启动启动类启动类好然后我们来拷贝一下
[04:38] 这个其实我们不写大家应该也是会写那么和其他是一样的好那么这样的话这个启动类就搞定了那么也就是说我们这个工程搭建是不是就完成了OK好那么关于这个工程的一个搭建那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中配置 Elasticsearch，包括修改 pom.xml 添加依赖、配置 application.properties 连接集群、配置 log4j.properties 日志以及创建 ESApplication 启动类。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 pom.xml 文件内容，其中包含父项目配置和 <artifactId>my-tanhu-Elasticsearch</artifactId>。
画面 2：展示 TodayBestService.java 代码，其中包含使用 RestTemplate 发送 HTTP 请求的逻辑。
画面 3：展示 pom.xml 文件内容，其中包含 <parent> 配置和 <artifactId>my-tanhu-Elasticsearch</artifactId>。
画面 4：展示 pom.xml 文件内容，其中包含 <dependencies> 节点下的 spring-boot-starter-web 依赖。
画面 5：展示 pom.xml 文件内容，其中包含 <dependencies> 节点下的 spring-boot-starter-data-Elasticsearch 依赖。
画面 6：展示 pom.xml 文件内容，其中包含 <dependencies> 节点下的 spring-boot-starter-test 依赖。
画面 7：展示 pom.xml 文件内容，其中包含 <dependencies> 节点下的 commons-lang3 和 lombok 依赖。
画面 8：展示 application.properties 文件内容，其中配置了 spring.application.name、server.port 和 spring.data.Elasticsearch.cluster-nodes。
画面 9：展示 application.properties 文件内容，其中 spring.data.Elasticsearch.cluster-nodes 的值被修改为 192.168.31.9300,192.168.31.9301。
画面 10：展示 application.properties 文件内容，其中 spring.data.Elasticsearch.cluster-nodes 的值被修改为 192.168.31.9300,192.168.31.9301,192.168.31.9302。
画面 11：展示 log4j.properties 文件内容，其中配置了 log4j.rootLogger、log4j.appender.A1 和 log4j.appender.A1.layout。
画面 12：展示项目结构，选中了 my-tanhu-Elasticsearch 模块下的 java 目录。
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
    <artifactId>my-tanhu-Elasticsearch</artifactId>
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
    <artifactId>my-tanhu-Elasticsearch</artifactId>
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
        <artifactId>spring-boot-starter-data-Elasticsearch</artifactId>
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
        <artifactId>spring-boot-starter-data-Elasticsearch</artifactId>
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
spring.application.name = itcast-tanhu-Elasticsearch
server.port = 18082
spring.data.Elasticsearch.cluster-name=es-tanhu-cluster
spring.data.Elasticsearch.cluster-nodes=192.168.31.9300,192.168.31.9301
```

画面 9：
```properties
spring.data.Elasticsearch.cluster-nodes=192.168.31.9300,192.168.31.9301
```

画面 10：
```properties
spring.data.Elasticsearch.cluster-nodes=192.168.31.9300,192.168.31.9301,192.168.31.9302
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
spring.application.name = itcast-tanhu-Elasticsearch
server.port = 18082
spring.data.Elasticsearch.cluster-name=es-tanhu-cluster
spring.data.Elasticsearch.cluster-nodes=192.168.31.9300,192.168.31.9301,192.168.31.9302

2.4. log4j.properties
log4j.rootLogger=DEBUG,A1
log4j.appender.A1=org.apache.log4j.ConsoleAppender
log4j.appender.A1.layout=org.apache.log4j.PatternLayout
log4j.appender.A1.layout.ConversionPattern=[%t] [%c]-%p%n

2.5. UserLocationES
package com.lanhu.es.pojo;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.Elasticsearch.common.geo.GeoPoint;
import org.springframework.data.Elasticsearch.annotations.Document;
import org.springframework.data.Elasticsearch.annotations.Field;
import org.springframework.data.Elasticsearch.annotations.FieldType;
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

