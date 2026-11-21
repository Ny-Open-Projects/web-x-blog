# 画面线理解：18.日志规范之slf4j整合Log4j以及Logback

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day19-MongoDB集群以及日志、异常规范
- 源文件：03.阶段三 好客租房(生活服务)项目\day19-MongoDB集群以及日志、异常规范\18.日志规范之slf4j整合Log4j以及Logback【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:15, 00:20, 00:36, 00:59, 01:08, 01:20, 01:50, 02:07, 02:24, 02:32, 02:38, 02:55, 03:28, 03:58
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 00:12:38

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中集成 Log4j 和 Logback 日志框架，并对比它们的配置与运行效果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了使用 SLF4J + Log4j 的 Java 代码和运行日志，日志输出显示在控制台。
画面 2: 在 pom.xml 中添加了 slf4j-api 和 slf4j-simple 依赖。
画面 3: 在 Maven Projects 面板中显示了已添加的 slf4j-simple 依赖。
画面 4: 显示了 Typora 中的文档内容，包含 Log4j 的配置示例和与 Logback 整合的章节标题。
画面 5: 在 IntelliJ IDEA 中，通过“File”菜单创建了 log4j.properties 文件。
画面 6: 展示了 log4j.properties 文件内容，但未配置 appender，导致运行时出现警告。
画面 7: 展示了 Demo.java 代码，准备运行。
画面 8: 显示了 Typora 文档中 Log4j 的配置示例。
画面 9: 运行程序后，控制台输出了带有时间戳和日志级别的信息，表明 Log4j 配置成功。
画面 10: 展示了 pom.xml 中添加了 Logback 的依赖。
画面 11: 在 Maven Projects 面板中显示了已添加的 logback-core 和 logback-classic 依赖。
画面 12: 运行程序后，控制台输出了带有时间戳和日志级别的信息，表明 Logback 配置成功。
画面 13: 显示了《阿里巴巴 Java 开发手册》中关于日志规范的章节内容。
画面 14: 显示了 Typora 文档中关于日志规范的总结，与画面 13 内容一致。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
package cn.itcast.log;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
public class Demo {
    private static final Logger LOGGER = LoggerFactory.getLogger(Demo.class);
    public static void main(String[] args) {
        LOGGER.info("这是info日志信息。代码之前进行打印信息。");
        System.out.println("测试代码");
    }
}
```

画面 2:
```xml
<dependency>
    <artifactId>slf4j-api</artifactId>
    <version>1.7.26</version>
</dependency>
<dependency>
    <groupId>org.slf4j</groupId>
    <artifactId>slf4j-simple</artifactId>
    <version>1.7.26</version>
</dependency>
```

画面 3:
```xml
<dependency>
    <groupId>org.slf4j</groupId>
    <artifactId>slf4j-log4j12</artifactId>
    <version>1.7.26</version>
</dependency>
```

画面 4:
```xml
<dependency>
    <groupId>org.slf4j</groupId>
    <artifactId>slf4j-log4j12</artifactId>
    <version>1.7.26</version>
</dependency>
```

画面 6:
```properties
log4j.rootLogger=DEBUG,A1
log4j.appender.A1=org.apache.log4j.ConsoleAppender
log4j.appender.A1.layout=org.apache.log4j.PatternLayout
log4j.appender.A1.layout.ConversionPattern=%d{yyyy-MM-dd HH:mm:ss,SSS} [%t] [%c] - %p %m%n
```

画面 8:
```xml
<dependency>
    <groupId>org.slf4j</groupId>
    <artifactId>slf4j-log4j12</artifactId>
    <version>1.7.26</version>
</dependency>
```

画面 10:
```xml
<dependency>
    <groupId>ch.qos.logback</groupId>
    <artifactId>logback-core</artifactId>
    <version>1.1.9</version>
</dependency>
<dependency>
    <groupId>ch.qos.logback</groupId>
    <artifactId>logback-classic</artifactId>
    <version>1.1.9</version>
</dependency>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 4: 标题为“3.3.5、与Log4j整合”和“3.3.6、与Logback整合”。
画面 13: 标题为“（二）日志规约”，内容包括三条强制规范。
画面 14: 标题为“3.3.7、小结”和“3.4、手册中的其它规范”，内容与画面 13 一致。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
