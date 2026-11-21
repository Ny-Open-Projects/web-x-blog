# 12-SpringBoot配置-项目内部配置文件加载顺序

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/1.SpringBoot 第一天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\1.SpringBoot 第一天\12-SpringBoot配置-项目内部配置文件加载顺序_【海量资源尽在 ubkz.com】.mp4
- 时长 9分35秒（音频 575s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 接下来我们来介绍Spring Boot配置的加载顺序Spring Boot它允许我们在项目内部进行一些配置文件的书写也可以把一些配置写到外边就是项目的外边去进行一些配置比如说刚才我们写的那个命令行参数就是外部的配置那么在这一小节我们先来介绍内部配置的加载顺序Spring Boot它允许我们在很多地方都写配置文件
[00:31] 那么有这么四个地方我们挨个来说一下第一个就是当前项目的configure目录下边第二个是当前项目的根目录下第三个是classpath的configure目录下第四个是classpath的根目录其实我们之前一直用的那个配置文件比如说application.properties或者yaml都写到了resources目录下那么那个resources将来呢都会打包打到classpath这个目录我们一直用的是第四个
[01:01] 那么这四个的顺序也是它们的优先级也就意味着最高优先级的是这个configure这个目录下的这么一个优先级那么高的优先级的属性会覆盖低优先级属性也就是说它读取的时候发现高的有了低的它就自动忽略掉了但是这四个文件都会读取的那么也就意味着比如说我在每一个文件这四个里边比如说每一个都有一个application.properties
[01:30] 我都配了server.port这个属性那么只有在第一个里边会生效其他的三个里边的server.port属性就不会生效但是呢你在其他三个文件里边去配置一些其他的属性它们是会生效的介绍完了这个加载的顺序接下来我们就来演示一下打开我们的idea我们重新去创建这么一个模块吧新建这么一个模块还是用这种sprint的快速创建方式
[02:02] 下一步写一个group id com.it黑码然后呢我们起名叫supremeboot-configure好起完名之后呢我们下一步我们为了方便测试我们加一个web的stutter elan下一步finish稍等这个地方我们刚才可能没有去改这个名字我们可能创建到init里边了我们重新来创建一下重新来创建一下新建一个模块
[02:39] 然后呢下一步然后稍等一下com.it黑码然后呢sprintboot-configure好下一步下一步之后呢我们勾选一个web下一步下一步之后注意看哈这个地方它的一个路径得对啊刚才这个路径写成init了这个地方的路径呢应该是configure好改一下
[03:09] 不要忘记这个事,finish你看现在项目是不是就创建出来了创建出来了之后呢接下来我们来演示这些配置文件的一个顺序的问题那么在resource目录下将来这个resource和java这两个目录里边的内容都会打包打进我们的classes的目录那么首先呢我们先来看最后一个最低优先级的就是这个resources的根目录里边有一个application.properties我们给它配置一个server.port
[03:38] 比如说8081好配完了之后呢接下来我们来启动当前的这个应用它正在加载稍等一下启动好右键我们来运行一下运行一下之后呢我们来看这个端口肯定会改成8081这个之前我们已经测试过很多次了可以来看一下端口已经改变成为了8081了OK这个没有问题那么接下来我们来测倒数第二个倒数第二个就是在当前的class pass的config目录下
[04:14] 那么我们可以在这个地方创建一个目录叫做config好config里边我们把这个properties文件呢给它复制过去复制过去改个名改个值叫8082那么我们再一重启那么这个8082就会生效因为config目录下的这个文件的优先级比根目录下的这个application.properties的优先级要高你看8082是不是就生效了
[04:40] 那么倒数后边两个第三第四个我们就测试完了那么测试完了之后呢在当前项目下还有两个位置可以写配置文件一个是当前项目的config目录和当前项目的根目录我们来测试一下那么当前项目它指的是当前这个大的项目我们现在这里边这几个都是模块它并不是一个项目其实我们这几个模块呢都属于同一个项目我们可以看一下它都属于Spring Boot这个项目这是一个空的项目
[05:10] 然后这个项目下的文件才会生效我们想快速创建的话我们可以点这个地方点这个箭头下面有个project files可以点进来点进来之后呢这就是一个项目Spring Boot这个项目然后我们在这里边可以来创建这么一些文件比如说这个文件呢我们这样为了方便期间我们把它直接复制过来就可以了好复制一下把它放这个地方放这个地方之后呢我们在这里边改一下8083
[05:39] 那么这个时候你会发现这个8083的优先级比这两个都是要高的我们再来重新启动一下来看8083就生效了那么同理我们可以把这个configure的目录直接给它复制到当前项目的根目录下复制过来复制过来之后呢我们在这里边把它改成8084那么最终呢这个8084就会生效可以看一下8084是不是也生效了OK生效了之后呢我们再来演示
[06:15] 另外一件事就是说现在呢我们可以看到优先级的一个问题然后呢我们再来看一下这几个文件其实它都是会被加载的哈我们在最低优先级的这个application.properties里边我们配置另外一个属性看这个属性能否生效如果它生效的话就证明我们当前这个值它是这个文件是被加载了只不过这个值没有被加载好我们这样它现在变成这个样子了其实就没有提示了
[06:44] 没有提示了我们看一下我们把这个值呢刚才给它删掉了好 粘过来粘过来之后呢来看你看现在这个样子它是没有提示的没有提示我们想个办法让它有提示这样我们现在把这个文件先给它删掉好 删掉删掉之后呢好 删掉删掉之后呢我们把这里边的内容呢给它干掉你看现在是不是又变回这个样子来了变回来了之后呢我们在这里边写另外一个配置这个配置呢比如说我们去修改一下
[07:14] 我们的项目的访问路径这个项目访问路径默认值为这个斜杠我们之前什么都没输我们直接输的Controller里边的资源来访问的默认值为斜杠我们给它修改一下这个值呢叫做context pass好看一下就这么一个值这个值呢我们给它改为hello好改完了之后呢同样我们也可以在里边改一下端口serve the port
[07:40] 当然这个端口改了之后是不生效的因为它有更高优先级的这个属性存在其实现在我们就想测试一下这个-hello生不生效那么这个-hello要想生效的话我们可能需要去写一个Controller我们在这个地方写这么一个Controller写一个hello Controller写完的Controller之后我们在这里边加一个rest Controller
[08:07] 弄完了之后我们在里边再定义一个方法parbleck string hello好我们直接返回一句话hello configure弄完了之后我们在上面加一个request mapping好这个访问的路径呢我们也叫杠hello好这个杠hello是资源的访问路径而我们刚才在配置文件里边配的配的这个地方的
[08:35] Gang Halo呢是我们整个项目的访问路径它们是不一样的那么现在呢写完了之后我们重新来启动一下启动一下其实我们从这个控制台就可以看出来它的端口你看是不是8084说明是这个文件生效了对吧8084然后呢后边这个context path你看是不是也加载到了Gang Halo啊所以现在我们想访问我们这个资源呢我们应该写localhost然后呢8084Gang
[09:09] 哈喽这是第一集哈喽第一集哈喽呢就是我们的项目的访问方式然后第二集呢是资源资源好这样呢我们就访问到了这个资源的路径所以呢你会发现这多个文件他们都会加载而且呢他们形成了一种互补的配置好嘞那么这个配置文件的一个加载的这个顺序呢我们就介绍完毕了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 Spring Boot 项目的配置文件加载顺序及如何通过配置文件修改应用端口。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示 PPT 标题页，内容为“Spring Boot 配置”，子标题“内部配置加载顺序”，并列出 Spring Boot 启动时加载配置文件的四个优先级顺序。
画面 2: 在 IntelliJ IDEA 中创建新模块，选择依赖项，准备创建 Spring Boot 项目。
画面 3: 在 IntelliJ IDEA 中点击“File”菜单，准备进行项目设置或打开项目。
画面 4: IntelliJ IDEA 主界面，显示项目结构和欢迎页面。
画面 5: 在 IntelliJ IDEA 中打开项目，显示项目结构，当前选中的是 `SpringbootConfigApplication.java`。
画面 6: 在 IntelliJ IDEA 中，选中 `application.properties` 文件，准备编辑。
画面 7: 在 IntelliJ IDEA 中，右键点击 `application.properties` 文件，弹出上下文菜单。
画面 8: 在 IntelliJ IDEA 中，显示 `application.properties` 文件内容为 `server.port=8082`，并显示控制台输出 Spring Boot 启动日志。
画面 9: 在 IntelliJ IDEA 中，显示 `application.properties` 文件内容为 `server.port=8084`，并显示控制台输出 Spring Boot 启动日志。
画面 10: 在 IntelliJ IDEA 中，显示 `application.properties` 文件内容，包含注释和多个配置项，如 `server.servlet.context-path`、`server.Tomcat.redirect-context-root` 等。
画面 11: 在 IntelliJ IDEA 中，打开 `HelloController.java` 文件，显示代码内容，包含 `@Component`、`@Value`、`@PropertySource` 等注解。
画面 12: 在 IntelliJ IDEA 中，显示 `application.properties` 文件内容为 `server.port=8084`。
画面 13: 在浏览器中打开 Spring Boot 官方参考指南文档首页。
画面 14: 展示 PPT 标题页，内容为“Spring Boot 配置”，子标题“内部配置加载顺序”，并列出 Spring Boot 启动时加载配置文件的四个优先级顺序。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**：
画面 5:
```
server.port=8081
```
画面 6:
```
server.port=8082
```
画面 8:
```
server.port=8082
```
画面 9:
```
server.port=8084
```
画面 10:
```
# 解决访问许可问题，设置访问路径为/
server.servlet.context-path=/context
server.Tomcat.redirect-context-root=true
spring.freemarker.request-context-attribute=javax.servlet.http.HttpServletRequest
spring.groovy.template.request-context-attribute=javax.servlet.http.HttpServletRequest
spring.mvc.content-negotiation.favor-path-extension=false
spring.mvc.content-negotiation.favor-parameter=true
spring.mvc.content-negotiation.media-type=application/json
```
画面 11:
```
package com.ithema.springbootconfig;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.PropertySource;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.ServletRequestAttributes;
import org.springframework.web.context.request.RequestScope;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.RequestContextHolder

