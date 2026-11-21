# 18.日志规范之slf4j整合Log4j以及Logback

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day19-MongoDB集群以及日志、异常规范
- 源文件：03.阶段三 好客租房(生活服务)项目\day19-MongoDB集群以及日志、异常规范\18.日志规范之slf4j整合Log4j以及Logback【海量资源尽在 ubkz.com】.mp4
- 时长 4分2秒（音频 243s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下萨拉芬呢去整合log4j那么整合log4j呢其实跟我们前面去整合JDK14以及这个symbol差不多那我们需要导入这个依赖我们来看一下那我们来导入的是我们的log4j的这个依赖那么前面的这个symbol呢就需要把它注释掉OK那么我们把它拷到这个位置来OK好那么这样的话呢我们就会
[00:27] 把我们这个Sarafn呢去整合log4j这样的一个我们那个依赖就导入进来了那我们来刷新一下看一下那么这个位置可以看到是不是就导入了log4j这个依赖好那我们可以来执行一下走那么执行呢就可以看到我们去通过log4j去打印的这样的一个日志但是呢比较遗憾的是我们并没有去打印出相应的一个日志原因是什么呢原因是我们并没有去
[00:55] 给他去写他的一个什么的配置文件啊那么我们知道log4j呢其实需要去写一个log4j.publish这样的一个配置文件的对吧那么我们来写一个文件那么这个文件呢放到我们resource下面去写一个这个log4j.publish文件那把这个内容呢我们拷贝过来放到这哎呦ok好那么我们呢就可以去做一个执行了那么大家我们可以简单来看一下啊那么这个配置文件中呢我们去设置了我们的
[01:24] root这个login呢是debug模式那么下面我们设置了一个AE给AE呢做了一系列的设置啊包括它的一些这个就是我们这个append的这个lay呢是console就是打印的控制台然后呢这个呢通过这个panty的layout去做一个这个layout然后呢这个是我们的日期的格式化的一个格就是我们打印的一个日期的一个格式啊ok好然后呢我们去做一个执行走来看一下效果
[01:51] 那么这一次可以看到这个就是我们所打印的一个日志效果那么这个是不是打印日志对吧那么这个打印日志那么下面这个也是打印日志OK好那么由此可见我们是不是已经就整合了我们的log4jok好那么接着我们继续往下面看如果我们要去整合logback怎么去做那么要注意的是还是导入依赖但是这个依赖并不是萨拉芬所提供的依赖
[02:19] 而是他自己自身的依赖那么我们需要把两个依赖拷贝过来然后去找到POM文件去做一个修改那么把这个注释掉我们只需要再添加一个logback就可以了然后我们去刷新一下这两个导入进来没有问题然后我们再去运行走那我们来看一下它的一个结果将会是怎么样的
[02:45] 那么其实可以看到那么现在呢我们是不是通过这个logback这个去做一个打印啊那么可以看到我们的这个代码是不是并没有做出任何的改变那么就可以去替换掉在底层所工作的一个log的框架那么这个呢就是log分这个沙拉分沙拉分它的一个这个优势所在对不对啊所以说呢最后我们来一个小结呢就是无论和什么日期框架做整合
[03:13] 那么我编写的代码是不需要做任何的修改那我们只需要去更改底层的日志框架的依赖就可以了这个呢就是沙拉芬框架所存在的一个意义那么其实也就可以解释那么为什么在阿里巴巴的这个开发手册中呢在第一条的时候那么就去指定说我们必须强制使用的是沙拉芬中的API而不能直接使用日志系统中的
[03:42] 一些API那么原因是不是就这样的原因OK好那么我们在使用的时候我们需要注意的是我们所有使用的API对象API都是Sarafn所提供的APIOK好那么关于Sarafn的具体的一些使用我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

