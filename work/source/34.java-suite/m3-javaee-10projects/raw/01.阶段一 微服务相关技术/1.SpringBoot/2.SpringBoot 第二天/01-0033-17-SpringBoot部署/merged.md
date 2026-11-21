# 17-SpringBoot部署

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/2.SpringBoot 第二天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\2.SpringBoot 第二天\17-SpringBoot部署_【海量资源尽在 ubkz.com】.mp4
- 时长 11分7秒（音频 667s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 接下来我们来介绍一下Spring Boot的项目部署的这种方式那么比如说你把Spring Boot的项目开发完了那你应该怎么样把它放到服务器上或者是生产环境上让它运行起来跑起来那么这个地方就要牵扯到项目部署打包的一些方式了而Spring Boot呢它支持两种打包的方式来进行项目的部署第一种打jar 包第二种打挖包打jar 包呢就是说你项目开发完
[00:31] 打个jar 包Spring Boot默认是不是就是打jar 包的方式然后呢你通过渣挖杠渣的命令把这个jar 包骑起来就OK了那你要启动的话呢你将来的服务器上安个JDK是不是就完事了官方推荐打jar 包当然啊你说你不想打jar 包你不想要内置的Tomcat你想打挖包可不可以啊也可以你打个挖包之后呢你放在外部的Tomcat里边去运行Spring Boot的项目也是没有问题的
[00:57] 那么接下来我们就来演示一下这么两种不同的方式还是来创建这个模块啊好我们来创建一个部署相关的模块吧稍等一下这个地方嗯好加一个哈加一个模块这样的模块呢我们下一步下一步之后呢起个com.it黑码然后呢spreetboot-deploy好就这个名啊部署
[01:33] 下一步然后我们把web勾上因为我们要部署的是web项目走弄完了之后finish好再初始化模板弄完了之后OKOK了之后首先我们来演示一下打包打包打什么包呢打一个jar 包的方式因为我们都知道deploy我们引入了web的模块web的模块里边是不是内置的有内置的服务器它默认依赖的是TomcatOK
[02:02] 默认一来Tomcat我们将来一启动是不是就以内置的Tomcat来启动这个项目了那么当然我们可以在这个地方来创建一个Controller来访问一下比如说我们就创建一个user-Controller然后把它的配置给它写上request-mapping然后叫-user下来叫做rest-Controller
[02:29] 加上之后提供一个简单的方法public string叫做findall非常简单return一下success写完了之后加一个request mapping把对应的路径findall给它加上那么这个就写完了写完了之后接下来我们来部署比如说项目就写完了写完了你要把这个项目部署到生产环境上怎么弄呢打个包对吧
[02:59] 我们可以这样做我们在这个地方呢打开这个Mavenproject来刷一下Deploy有了有了之后Left Circle然后在这个地方呢我们直接来Package打下包打下包之后呢打就行了打完了之后呢它默认是个打个jar 包因为我们没有配置Maven的打包方式默认就是打jar 包测试然后测试完了之后呢如果成功就可以成功的打出来这个包你看这个地方Success了打包在哪呢在这个位置
[03:28] 在你当前项目的一个target目录下,Ctrl C复制一下,打开我们的文件夹,然后呢,把它访问一下那么这个包,就是我们对应的一个炸的包那么这个jar 包将来你给别人就可以了比如说你把它放到生产环境,比如说我们换个位置,放到桌面上我们在桌面上比如说建个文件夹,好,建个文件夹,Project,可以吧然后呢我们把这个jar 包放在这儿了将来你要运行这个jar 包,怎么办呢
[03:58] 比如说这就是服务器的目录了Linux环境下的然后呢你只需要来执行这个jar 包就可以了我们进到这个目录里边在此处打开这个DOS窗口打开了之后呢我们直接来执行Java-jar然后呢Spring Boot这个好启动就行了就完事了对吧那么启动完事了之后呢你可以看一下Tomcat已经起起来了在哪个端口上呢8080没问题吧弄完了之后呢访问就行了就比较简单啊
[04:27] 我们在这访问一下localhost8080下的user翻到之前是有这个路径那么这个地方稍等一下它这个启动启动完了之后卡了一下卡了一下好了那么现在你看success没有问题了吧这个界面你点了之后它会卡住你再点一下就好了
[04:51] 那么这个就访问到了非常的容易打jar 包的方式他使用的是这个jar 包内置的那个Tomcat对吧好这是打jar 包的方式我们再切回到idea里边来在切回到idea里边来我们来说一个打袜包的方式那现在我不想用内置的Tomcat我就想打袜包怎么办呢也比较容易那么首先你要干第一件事你得把这个POM里边的打包方式改一下改成一个VAR这是第一件事对吧
[05:21] 将来他打出来的包就是挖包而这个挖包要想让被Tomcat识别到那么你需要去对你的核心的这个启动类做一个小手术怎么办呢在这个地方我们去实现这么一个叫做叫做SpriteSprite叫做ApplicationApplicationSpriteSpriteSpriteSprite好这么一个东西
[05:52] 这个玩意是一个类,我们把它继承一下就行了继承一些这个类,Spring Boot Servlet Initializer继承完了之后,你需要干一个事,写一个方法在这里复写一个方法就可以了复写哪个方法呢?
[06:10] 这个地方叫做Override Master有一个叫做Configure这个方法告诉它这个主类就可以了这个地方这个方法里有个参数,叫做Build
[06:23] 这个build呢你只需要调用一个sauce方法然后把你这个入口这个类呢的字节码文件给它放里边好嘞就做完了其实呢也非常简单啊继承了这么一个类然后呢写了这么一个方法然后呢把这个pom文件里边的这个warp包给它改了一下就是打包方式改了一下那么现在呢我们再来去打包注意看啊我们是不是重新打包了重新打包的话呢它就会打成一个warp包而且这个warp包呢是可以被外部的Tomcat所识别到的好
[06:59] 这个地方呢包就打成功了还是在这个目录下边是吧还是在这个目录下边这个目录下边呢你可以看一下现在呢是不是就有一个VAR的包了我们打开好打开打开之后呢走来看这个地方来看一下VAR包有没有有吧有这个VAR包没问题是吧当然你觉得这个名字不好看的话呢你可以在这个打包的时候呢给它指定一下当然你可以手动改比如说你再指定一下这个file namefile name比如说你叫
[07:29] Spring Boot那么将来打出来包的名字挖包的名字叫Spring Boot了我们可以重新试一下这个比较简单就说一下就可以了那么将来这两种方式的部署的项目都可以但是推荐你使用打jar 包的方式内置的Tomcat来起作用好来你看这个现在打到包名字是不是叫Spring Boot.var了那么我们切到这个目录里边来看Spring Boot.var是不是在这个地方OK啊那么现在你想运行它怎么办呢
[08:00] 那我们在这个地方啊找到我们资料里边今天提供好的这个Tomcat好Tomcat8然后我们把它直接放到这个webapps下完事了然后你启动Tomcat就完事了以前这样做就可以哈那么startup.bat我们把这个Tomcat呢给它启动一下启动一下之后呢它说address already in use为啥呢起了一个了是吧我把这个呢给它关了关了之后呢我们再来启动再来启动应该就没有什么问题了
[08:29] 这个控制台乱码是编码的问题这个不用管你看Splitboot项目是不是在启动啊好那么这个玩意弄完了之后呢我们来访问一下先访问这个Tomcat Logo House的8080那么这玩意是不是相当于我们的Tomcat外置的这个Tomcat对吧这个地方正在启可能得等一下下了你看正在启动一大堆东西好启完了之后呢外置的这个Tomcat是不是就访问到了这只猫对吧然后呢现在啊现在
[09:03] 我们在这个地方访问一下user-fanall来看他说404为啥呢为啥404呢因为你现在这个项目的路径啊虚拟目录它已经不再是斜杠了而是谁呢而是你这个地方的webapps下边的这个目录是不是有个sprintboot目录那么sprintboot目录下边webinfo下边的classes里边才有对应的我们刚才那个fanall是这样的吧
[09:30] 所以你需要加一层目录这个地方要注意好 加一个smash boot再访问你看四个size没有问题吧OK 这是第一个事虚拟目录发生了变化那第二个事呢你注意现在你这个Tomcat比如说你的挖包里边就是你这个项目里边配的什么server.port还能生效吗比如说你在这配个server.port对吧 四个挖你觉得它会生效吗肯定不会 是吧因为这是配置内置的Tomcat的路径
[10:01] 那么现在你用的外置的Tomcat你要改它的端口号的话你需要在它外置的Tomcat的配置文件里面去改你内置的这个肯定是不生效的这个我就不再演示了下来各位可以自己尝试一下所以对于打jar 包方式非常简单直接打包 扎挖杠炸 启动就行了而打挖包也非常简单你只需要让你的
[10:25] 当前的启动类引导类啊继承这么一个SupremeBootServerLine的InitialLine这么一个这个类啊继承这个类不是接口然后呢你去复写这么一个方法并且呢使用这个方法的参数Build的Source方法把我们的这个引导类的Class传进来就完事了然后呢最需要干的一件事就是改一下这个打包方式改成对应的Var的方式好嘞那么这样我们就可以
[10:53] 打成一个挖包并且把这个挖包部署到外部的Tomcat去使用了那么对于Spring的boot的项目的两种部署方式打jar 包打挖包我们就介绍完毕了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Maven 将 Spring Boot 项目打包成 jar 和 war 两种格式并部署运行。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PPT 标题页，说明 Spring Boot 项目部署支持 jar 和 war 两种方式。
画面 2: 在 IDEA 中展示项目结构，选中 Spring Boot-deploy 模块，准备进行打包。
画面 3: 在 IDEA 中打开 UserController.java，展示其代码内容。
画面 4: 在 IDEA 中展示 Maven 编译日志，显示项目已成功编译。
画面 5: 展示桌面，有一个名为 "project" 的文件夹。
画面 6: 在浏览器中访问 localhost:8080/user/findAll，页面显示百度首页。
画面 7: 在 IDEA 中展示 Maven 打包日志，显示正在构建 jar 包。
画面 8: 在 IDEA 中展示 SpringBootServiceInitializer 类的代码，显示其构造函数。
画面 9: 在 IDEA 中展示 pom.xml 文件，显示 <packaging>jar</packaging>。
画面 10: 在 IDEA 中展示 pom.xml 文件，显示 <packaging>war</packaging>。
画面 11: 在 Windows 命令行中运行 jar 包，显示 Spring Boot 启动日志。
画面 12: 在命令行中运行 war 包，显示 Spring Boot 部署日志。
画面 13: 在 Windows 资源管理器中展示 apache-Tomcat-8.5.46 的 WEB-INF/classes 目录，包含 application.properties 文件。
画面 14: 在 IDEA 中展示 pom.xml 文件，显示 <packaging>war</packaging>，并显示 Maven 打包成功日志。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
Spring Boot 项目开发完毕后，支持两种方式部署到服务器：
① jar包(官方推荐)
② war包

画面 2:
Name: Spring Boot-deploy
Sources: src/main/java
Test Resources: src/test/resources

画面 3:
package com.ithema.springbootdeploy;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RequestMapping("/user")
@RestController
public class UserController {

画面 4:
[INFO] --- maven-resources-plugin:3.0.1:testResources (default-testResources) @ Spring Boot-deploy ---
[INFO] Using UTF-8 encoding to copy filtered resources
[INFO] skip non existing resourcesDirectory
[INFO] --- maven-compiler-plugin:3.0.1:testCompile (default-testCompile) @ Spring Boot-deploy ---
[INFO] Changes detected - recompiling the module...
[INFO] Compiling 1 source file to E:\workspace\springboot02\Spring Boot-deploy\target\test-classes
[INFO] --- maven-surefire-plugin:2.22.1:test (default-test) @ Spring Boot-deploy ---
[INFO] T T T T S
[INFO] Running com.ithema.springbootdeploy.SpringbootDeployApplicationTests

画面 7:
[INFO] --- maven-jar-plugin:3.1.2:jar (default-jar) @ Spring Boot-deploy ---
[INFO] Building jar: E:\workspace\springboot02\Spring Boot-deploy\target\Spring Boot-deploy-0.0.1-SNAPSHOT.jar
[INFO] --- spring-boot-maven-plugin:2.1.0.RELEASE:repackage (repackage) @ Spring Boot-deploy ---
[INFO] Replacing main artifact with repackaged archive

画面 8:
public class SpringBootServiceInitializer {
    public SpringBootServiceInitializer() {
        SpringApplication application = new SpringApplication(SpringbootDeployApplication.class, args);
        application.run(args);
    }
}

画面 9:
<packaging>jar</packaging>

画面 10:
<packaging>war</packaging>

画面 11:
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : Starting SwaggerAutoConfiguration on ithema with PID 11344
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : No active profile set, falling back to default profiles: default
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : Starting SpringBootDeployApplication on ithema with PID 11344
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : Started SpringBootDeployApplication in 2.009 seconds (JVM running for 4.448)
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : Started SpringBootDeployApplication on ithema with PID 11344
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : No active profile set, falling back to default profiles: default
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : Starting SpringBootDeployApplication on ithema with PID 11344
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : Started SpringBootDeployApplication in 2.009 seconds (JVM running for 4.448)
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : Started SpringBootDeployApplication on ithema with PID 11344
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : No active profile set, falling back to default profiles: default
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : Starting SpringBootDeployApplication on ithema with PID 11344
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : Started SpringBootDeployApplication in 2.009 seconds (JVM running for 4.448)
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : Started SpringBootDeployApplication on ithema with PID 11344
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : No active profile set, falling back to default profiles: default
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : Starting SpringBootDeployApplication on ithema with PID 11344
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : Started SpringBootDeployApplication in 2.009 seconds (JVM running for 4.448)
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : Started SpringBootDeployApplication on ithema with PID 11344
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.SwaggerAutoConfiguration : No active profile set, falling back to default profiles: default
2019-06-28 12:00:34.661 INFO 11344 --- [           main] o.s.b.S

