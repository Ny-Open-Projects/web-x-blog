# 13-SpringBoot配置-项目外部配置加载顺序

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/1.SpringBoot 第一天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\1.SpringBoot 第一天\13-SpringBoot配置-项目外部配置加载顺序_【海量资源尽在 ubkz.com】.mp4
- 时长 12分4秒（音频 724s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 介绍完项目内部的配置文件的四个加载顺序之后接下来我们来介绍外部配置的加载顺序那么这个Spring Boot它允许很多地方定义一个外部的配置那么为了方便期间我们在这个官网上来查看找到这个官方网站的配置文档在这个文档下边我们去找到一个外部的配置在这个地方
[00:27] Externalized Configuration外部的配置我们点进去点进去看一下在这个地方有17个描述这17个地方都是允许配置的地方那么这么多地方其实我们真的不需要都把它记住因为很多地方是不常用的我们首先来看第一个就是Command Line Arguments就是我们的命令行的参数那么命令行的参数就意味着我们可以在命令行参数的位置来写这个配置
[00:56] 并且呢这17个这个顺序其实呢就是我们对应的优先级那么优先级最高的是这么一个那么第四个呢它的优先级也是比较高的好嘞那么我们可以来尝试一下命令行的方式那么我们还是来使用当前的这个项目吧我们把它换到这个这个界面好configure那么为了方便起见呢我们在这个地方呢为了演示这个命令行我们刷一下刷一下之后呢我们在这个地方
[01:26] 好打一下包之后呢我们通过运行jar 包的方式来去输出输入命令行的参数来设置这些参数稍等正在打包的过程中好打完包之后呢我们进到这个target目录打开target目录那么这有一个配置的文件不是配置文件是这个jar 包那么我们在这呢直接来运行运行呢我们就java-jar
[01:59] 然后呢我们Spring那么刚才呢我们来看刚才我们如果直接来运行这个程序的话刚才如果我们直接运行这个程序的话它呢启动端口号是多少呢我们看一下启动端口号应该是8084对吧上一个小节我们运行的因为呢它会读取当前项目的根目录下的Configure目录下的那个配置文件它是8084来看OK吧
[02:26] 但是呢现在我们通过炸的方式来运行它就不是8084了我们来运行一下我们把这个停掉了好我们把最大化可以看一下它是8081为什么它又变成8081了呢原因说一下原因是因为我们当前这个项目来看这个project files当前项目的这个configure和这个application的properties这两个文件它是不会打进这个jar 包里边的
[02:55] 因为它这两个并不符合我们的Maven的一个结构它不会打进jar 包也就是说在我们当前打进的这个jar 包里边我们可以把它右键我们可以用这个打开一下打开方式我们用这个压缩文件把它打开打开之后呢我们来看当前项目的org supreme framework boot然后呢这个里边哎往上看这个地方它打进包里边应该是metinfo好来看一下这里边是没有一个配置文件的
[03:25] 往上看这个jar 包呢在boot info你看classes下面是不是只有这一个那么configure那个目录下的那个文件呢我们刚才删过了所以它没有出现所以呢我们可以看到对应的地方这个配置文件它是没有出现的对吧也就是说这两个文件它是不会打进我们的jar 包里边的所以呢现在运行呢它就会识别这个8081的这个端口号了那么当然我们想去修改它的话也是没有问题的
[03:53] 怎么改呢我们Ctrl C把它结束掉结束掉之后呢我们指定杠然后呢两个杠注意两个杠两个杠之后呢我们Server.Pod比如说我们等于8082好我们再一起动一起动了之后呢它就会优先读取这个命令行的参数通过8082的这个端口号来启动当前的这个应用我们可以看一下效果稍微等一下我们把这个关掉关掉之后呢
[04:29] 让它运行一下起动起来了起动了起来了之后呢你看现在呢server.portport写错了PORT对吧好我们Ctrl C给它结束掉结束掉之后呢PORT等于8082好现在重新来一下刚才没生效是因为这个port我们写错了好我们再来看这个效果这个启动还是比较慢的因为它可能要去加载读取这个
[05:05] 属性文件就是配置的属性所以我们稍微等一下好现在可以看到这个8082是不是就生效了没有问题对吧那么当然这个控制台这个参数你可以指定很多个很多个Ctrl C把它结束掉比如说刚才我们还配了一个还配了一个叫啥呢叫做server.server.context.path这个也是可以指定的比如说我们可以再来指定再来指定再来中间用空格隔开就可以了
[05:41] server.server.context-pass刚才那是hello我们改成-呵呵再来启动再来启动一下之后呢我们可以看一下这个效果好来看一下现在呢-呵呵是不是就生效了OK但是呢你通过这种命令行的方式来指定很多的参数那肯定是不现实的因为这两个参数比较简单将来我们的配置文件里边是有一大堆的参数的
[06:09] 那你怎么指定的过来呢所以呢在命令行这个地方呢还可以通过一种方式啊就是我们指定一个外部的配置文件是可以的那么我们看一下官网啊在官网往下边拉往下边拉之后呢这个地方就是刚才描述我们四个配置文件路径的那四个地方然后呢这个地方呢有一个地方有一个参数叫做spring configure location你可以通过这个
[06:35] 属性来去配置你外部的一个配置文件的一个路径那么比如说举个例子我们现在呢在这个地方我们复制一个配置文件出来比如说在这Ctrl C我们复制一个配置文件我们给它放到这个一盘的根目录下边好然后呢放这之后呢我们来改一下刚才如果不指定的话呢是8081对吧我们给它改成比如说我们把这个呢给它注释掉我们只看端口啊
[07:05] 我们改成8088好保存一下保存完事了之后呢这个文件呢是我们给它打开复制一下复制一下好这个名字复制完事了之后呢接下来我们重新来运行Ctrl C C结束掉结束了之后呢我们重新来运行我们把刚才那个参数都给它删掉删掉之后呢我们指定一个叫做Spring.locationSpring.configure.location这么一个参数
[07:34] 这个参数后边就是写的你的配置文件的这么一个路径一盘下的刚才我们复制的那个名字叫做application.properties好回车回车了之后呢如果它的端口改成8088了就说明我们那个配置是生效的你看生效了吧没有问题对吧OK
[08:00] 那么这个地方呢就说明我们的额外的外部的配置是不是也是生效的OK吧那么这个事呢我们就说完了第一个命令行的参数我们可以这样配置但是呢通过命令行的方式呢我们还得指定这个参数是不是感觉比较麻烦一些对吧其实呢还有第二种方式啊第二种方式呢我们再打开刚才的那个target目录好Spring Boot然后呢找到configure找到它的target
[08:29] 我们在这个位置我们可以不指定它有一个地方是默认加载的哪个地方呢可以来往上看看这个地方它只有这么四个配置这四个配置呢我们演示一个就可以了第一个呢是这前面两个是带profile的outside就是说外部的你的package的这然后呢package inside就是你内部的profile它会先加载外部带profile的这么一个文件
[08:57] 然后再加载内部就是你项目内部打进jar 包的那个profile的那个文件然后它再会去加载项目外部不带profile的文件再加载项目内部带profile的文件OK那么我们可以在这个地方来写来把这个配置文件复制过来我们Ctrl C然后我们进到这个target目录下边我们让当前这个文件配置文件跟这个configure
[09:27] 这个jar 包同级啊同级他们两个同级然后这个文件就会自动的被读取了我们可以来尝试一下这个呢我们给他前面的我们都给他改一下比如说要8010好保存保存完事了之后呢我们在这个地方直接来运行我们不加任何的参数信息看一下这个8010这个会识别吗java-炸然后呢supreme boot好走来看
[10:01] 这个8010是不是也识别了没有问题OK吧然后呢接下来我们还可以再来哈还可以呢我们在这里边呢去创建这么一个configure目录configure目录然后呢我们把这个配置文件呢放到这个configure目录下边那么同理呢我们也给它改一个比如说要8011好那么刚才我们也看到了说configure目录啊它其实的优先级呢是比这个根目录是要高的所以呢这个8011将会生效了
[10:32] 好我们再来运行这时候我们没有指定任何的参数信息它自动的就会生效来看8011是不是也生效了OK啊那么这几个大家知道了之后就可以了那么这些外部的配置有什么用呢我们简单的要来说一下外部的配置其实它和我们内部的这些配置形成了一种互补的配置什么叫互补配置呢比如说当前我的项目已经写完了
[11:00] 写完了之后呢我要部署的时候发现有一个配置啊我配错了配错了之后呢或者说我配的不是我想要的结果啊然后这个时候呢我的做法有两种第一种呢我就是进到这个项目里边去改完这个配置改完了之后呢我再来打包没有问题那么还有一种方式呢就是我比如说我在这个地方提供这么一个配置文件那么提供个配置文件之后然后呢我把某些属性给它覆盖掉是不是就可以了
[11:30] 比如说我在这儿短口号我觉得不好然后给它覆盖掉覆盖掉之后呢我一启动当前呢外部的配置就会优先的生效那么里边的配置呢也会生效它只是配置一些少量的信息修改内部的配置就可以了所以呢Spring Boot提供的这种很多位置可以配置文件的方式它形成了多文件的一种互补的优势非常的棒
[11:56] 那么对于Spring Boot的外部配置文件加载的顺序我们就简单的介绍完毕了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示 Spring Boot 外部配置文件的加载顺序和配置方式，包括通过官网文档、IDEA 项目结构、命令行参数和文件系统路径等手段进行配置管理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: PPT 页面，标题为“外部配置加载顺序”，并提供官方文档链接：https://docs.spring.io/spring-boot/docs/current/reference/html/boot-features-external-config.html。
画面 2: 官方文档页面，展示 Spring Boot 外部配置加载顺序的列表，其中第 1 项为“Devtools global settings properties on your home directory (~/.spring-boot-devtools.properties when devtools is active)”，第 2 项为“TestPropertySource attributes on your tests”，第 3 项为“properties attribute on your tests...”，第 4 项为“Command line arguments”，第 5 项为“Properties from SPRING_APPLICATION_JSON...”，第 6 项为“ServletConfig init parameters”，第 7 项为“ServletContext init parameters”，第 8 项为“JNDI attributes from java:comp/env”，第 9 项为“Java System properties (System.getProperties())”，第 10 项为“OS environment variables”，第 11 项为“A randomValuePropertySource...”，第 12 项为“Profile specific application properties...”，第 13 项为“Profile-specific application properties...”，第 14 项为“Application properties outside your packaged jar...”，第 15 项为“Application properties packaged inside your jar...”，第 16 项为“@PropertySource annotations on your @Configuration classes”，第 17 项为“(Default properties (specified by setting SpringApplication.setDefaultProperties))”。下方示例代码为：
import org.springframework.stereotype.*;
import org.springframework.beans.factory.annotation.*;
画面 3: IDEA 开发环境，显示项目结构，其中包含“application.properties”文件，内容为“server.port=8084”。控制台输出显示 Spring Boot 应用启动成功，端口为 8084。
画面 4: Windows PowerShell 窗口，显示 Spring Boot 应用启动日志，端口为 8084，无活动配置文件，回退到默认配置文件：default。
画面 5: Windows 资源管理器，显示“Spring Boot-config-0.0.1-SNAPSHOT.jar”文件，大小为 16.1 MB，修改时间为 2019-03-12 15:00:00。
画面 6: IDEA 开发环境，显示项目结构，其中包含“application.properties”文件，内容为“server.port=8084”。控制台输出显示 Spring Boot 应用启动成功，端口为 8084。
画面 7: Windows PowerShell 窗口，显示 Spring Boot 应用启动日志，端口为 8084，无活动配置文件，回退到默认配置文件：default。
画面 8: Windows PowerShell 窗口，显示 Spring Boot 应用启动日志，端口为 8082，无活动配置文件，回退到默认配置文件：default。
画面 9: 官方文档页面，展示如何使用 YAML 文件作为配置文件的替代方案，以及如何通过环境变量指定配置文件名和位置。代码示例为：
$ java -jar myproject.jar --spring.config.name=myproject
$ java -jar myproject.jar --spring.config.location=classpath:/default.properties,classpath:/override.properties
画面 10: Windows 资源管理器，显示“application.properties”文件，大小为 1 KB。
画面 11: 官方文档页面，展示如何使用 YAML 文件作为配置文件的替代方案，以及如何通过环境变量指定配置文件名和位置。代码示例为：
$ java -jar myproject.jar --spring.config.name=myproject
$ java -jar myproject.jar --spring.config.location=classpath:/default.properties,classpath:/override.properties
画面 12: Windows 资源管理器，显示“Spring Boot-config-0.0.1-SNAPSHOT.jar”文件，大小为 16.425 KB。下方打开 Windows PowerShell 窗口，提示符为“PS E:\workspace\Spring Boot-config\target>”。
画面 13: Windows PowerShell 窗口，显示 Spring Boot 应用启动日志，端口为 8010，无活动配置文件，回退到默认配置文件：default。
画面 14: PPT 页面，标题为“外部配置加载顺序”，并提供官方文档链接：https://docs.spring.io/spring-boot/docs/current/reference/html/boot-features-external-config.html。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
1 Devtools global settings properties on your home directory (~/.spring-boot-devtools.properties when devtools is active)
2 TestPropertySource attributes on your tests
3 properties attribute on your tests. Available on @SpringBootTest and the test annotations for testing a particular slice of your application
4 Command line arguments
5 Properties from SPRING_APPLICATION_JSON (inline JSON embedded in an environment variable or system property).
6 ServletConfig init parameters
7 ServletContext init parameters
8 JNDI attributes from java:comp/env
9 Java System properties (System.getProperties())
10 OS environment variables
11 A randomValuePropertySource that has properties only in random.*
12 Profile specific application properties outside your packaged jar (application-(profiles).properties and YAML variants)
13 Profile-specific application properties packaged inside your jar (application-(profiles).properties and YAML variants)
14 Application properties outside your packaged jar (application.properties and YAML variants)
15 Application properties packaged inside your jar (application.properties and YAML variants)
16 @PropertySource annotations on your @Configuration classes
17 (Default properties (specified by setting SpringApplication.setDefaultProperties))

下方示例代码为：
import org.springframework.stereotype.*;
import org.springframework.beans.factory.annotation.*;

画面 9:
$ java -jar myproject.jar --spring.config.name=myproject
$ java -jar myproject.jar --spring.config.location=classpath:/default.properties,classpath:/override.properties

画面 11:
$ java -jar myproject.jar --spring.config.name=myproject
$ java -jar myproject.jar --spring.config.location=classpath:/default.properties,classpath:/override.properties

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1 和 14: PPT 页面，标题为“外部配置加载顺序”，并提供官方文档链接：https://docs.spring.io/spring-boot/docs/current/reference/html/boot-features-external-config.html。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求完成）

