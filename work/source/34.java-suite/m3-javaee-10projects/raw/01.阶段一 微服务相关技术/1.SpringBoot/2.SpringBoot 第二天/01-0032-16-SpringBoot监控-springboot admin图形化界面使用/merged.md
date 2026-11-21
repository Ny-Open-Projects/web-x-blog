# 16-SpringBoot监控-springboot admin图形化界面使用

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/2.SpringBoot 第二天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\2.SpringBoot 第二天\16-SpringBoot监控-springboot admin图形化界面使用_【海量资源尽在 ubkz.com】.mp4
- 时长 15分14秒（音频 915s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才我们介绍了Spring Boot的监控发现我们可以通过这种REST的方式通过HTTP请求访问一些UIL它会给返回一些JSON的数据然后我们通过分析这些JSON的数据来得出我们想要的这个Spring Boot当前这个程序的一些运行的参数和状态信息那么这样做OK 没有问题但是拿到那些JSON数据我要分析就显得有点头疼了为啥呢太多 不好找 是吧
[00:30] 看着很不爽所以呢有一个开源的项目叫做Spring Boot Admin它呢给我们提供了一种图形化界面的方式来去查看刚才的这些监控的信息那么接下来我们就来说一下这个Spring Boot Admin那么它是一个开源的社区项目用于管理和监控Spring Boot的应用程序然后呢Spring Boot Admin呢它分两个角色一个是客户端一个是服务端先说服务端
[00:59] 服务端其实就是一个admin的一个UI界面的提供那么将来这个客户端就是你想被监控的Spring Boot的那些项目叫做Client那么Client需要把它的一些数据信息就是通过extractor获取的那些信息发送给服务端那么服务端只需要提供UI界面把那些数据解析JSON的解析展示到界面上我们方便就去点按钮来查看了就非常方便
[01:29] 所以呢应用程序我们作为client然后呢向这个server去注册注册完成了之后呢server就可以提供UI界面来展示client的这个actualitator的endpoint一些监控的信息其实还是底层原理还是他好只不过呢是提供了UI界面而已好嘞那么这个介绍完成之后呢接下来我们就来说一下这个Spring Boot Admin的使用步骤那么刚才说了
[01:58] 这玩意是不是得有两端啊所以呢这个东西的使用呢就得创建两个模块了最少得两个一个server一个client当然一个server你可以管理很多client待会我们可以来看一下首先我们先说server创建一个server的模块然后呢引入这个admin starter的server的这么一个依赖当然我们可以通过图形化界面的方式去勾选然后第三个呢要注意
[02:23] 搞完了之后你还得开启这个admin server的功能在你的引导类上加一个enable admin server这么一个注解好嘞server写完了非常简单你什么都不用干基本上然后第二个呢client你创建一个client的模块然后呢引入client的依赖然后第三个呢你需要去配置一下你把信息给谁呀是不是给这个server的地址所以你要配一个server地址配完了之后呢启动访问server看图形化界面就完事了
[02:52] 基本上学习的成本非常之低使用的成本也很低好嘞接下来我们在idea里边演示一下那么还是这样我们把这些先都给它最小化然后接下来我们把它这些都关掉然后创建这么两个模块两个模块一个是server一个是client那么接下来我们先来创建一个模块还是用快速构建的方式起个组IDcom.it黑码
[03:25] 然后呢,storing boot-admin-server好,就起这个名下一步下一步之后呢现在我们把它勾选成web的模块然后呢,在这个ops里边你选你看这个地方是不是有啊对吧admin server就可以了那这个actual呢就不用勾选了因为这里边它会依赖于它好,下一步finish完成完成了之后呢我们直接ok好,ok完事之后呢我们可以看一下这个server碰文件
[03:57] 碰文件里边呢它告诉你说引了这么一个starter进来对吧web的一个项目并且呢告诉你了这个sprint的admin的版本是2.1.5这个版本那么基本上就这么简单哈就引完了引完了之后呢接下来第二件事第二件事呢你需要在这个里边去做一个开启的动作你需要让它识别一下有一个enable admin server好嘞那么这个服务端的程序我们就写完了非常容易啊那么接下来我们
[04:27] 不要关掉不要关掉待会我们还要启动它那么接下来我们再来写这个admin的对应的client创建一下这个项目稍等有点慢那么接下来我还是拗一个模块下一步来起一个zoidcom.it黑码然后我们起名为supremeboot-admin-clientclient好
[04:57] 那么client呢同样我们搞成一个web的模块然后呢ops里边你看刚才是pcover这会我们勾web也同样不用引入这个东西好下一步finishfinish之后呢我们还是来ok一下就完事了完事了之后呢接下来我们在client里边来看一下比如说在这个地方呢我们需要去待会我们要启动这个应用那么配置文件我们就不看了其实就是一个client对吧
[05:27] 基本上就没有什么了然后呢你需要配置一下配什么东西呢首先呢第一个地方这个很重要你需要去指定一下我们的admin的server的一个地址就是你当前的这些监控信息你该发给谁啊对吧在谁的地方UI展示啊那么这个地方呢注意这两个现在是不是在我们同一个机器上所以他们默认的端口号是不是都是8080为了方便期间呢我们给它改个端口号
[05:56] 它是个web应用server.port我们改成9000可以吧那么将来呢我们要访问这个server的地址是不是就是9000呢对吧那么在这个clant里边我们给它配一下这个地址的参数很怪异啊叫做clantadminclanturl那么你注意看它叫clanturl这个地方呢后边的描述是theadmin server urlsregistered所以呢这个地方就是来配的那配谁呢http冒号
[06:26] 刚刚LOCL localhost的冒号9000完事了就写完了那么当然你要去开启哪些个配置信息呢我们还是把刚才那些配置都可以复制过来比如说你要开启所有的一个信息详细信息show details健康的检查always对吧你要开启所有的那就是endpoints.x这个玩意web的
[06:55] 然后改成新这两个我们刚才说过是吧开启所有的配置以及把这个健康检查的详细信息展示出来那么这个配置配完了之后呢最后呢我们可以好其他的就不用配了不用配了之后呢我们可以来启动一下我们先来启动这个server好server启动一下然后呢现在呢我们下来呢来启动这个client啊admin的client来启动一下启动一下之后我们直接访问server就可以看到这个client
[07:29] 这个应用程序里边的所有的信息了稍等一下注意看啊Clant马上开始启动了好启动了启动了之后呢你可以看一个日志说Application Register好注册成功了是吧注册到哪去了呢这个一个一个ID里边去了那么弄完了之后呢我们可以直接来访问一下把这些都先关掉关掉之后呢我们再重新打开打开之后呢我们Localhost然后我们这个地方就直接访问9000
[08:03] server的地址吧走你可以看到对的UI界面了对吧UI界面呢说有一个实例对吧all apps就是我们将来可以监控很多的你看这是有个列表嘛对吧并且告诉你说8080这个应用它启动了34秒你可以看这个地方37秒启动了一个实例对吧你点一下对吧点进来之后呢你可以看到对应的这么一个界面了这个界面呢首先进来这个界面好可以看到这里边呢
[08:31] 有很多的信息啊info的信息对吧健康的信息现在我们是不是只有这个磁盘的信息没有redis了对不对OK啊然后呢并且呢进程的信息然后呢Thread现成的信息是不是都可以看到然后内存的使用情况堆的非堆的等等你看非常智能是吧然后接下来还有一些比如说这个地方这个地方呢可以来过滤筛选你的一些请求的访问的次数比如说在这个地方举个例子
[08:59] 我们在这个地方呢client这个位置我们写一个Controller我们把刚才那个Controller复制过来懒得写了好就这个user Controller我们把它放到这个里边放到这个地方了之后呢我们这个Controller呢你看user然后呢find out对吧我们把这个呢client只需要把client重启一下你注意看哈重启的时候呢它会有UI的提示的比如说这个client重启了你可以看这个地方但是我看这个地方会去在这个页面上会弹出一个框框好的
[09:32] 你看这个地方呢他告诉你他没有去谈这个地方没关系他可能还没有加载到好然后呢我们没加载到我们就不管了我们来看一下看一下之后呢我们来看这个这个地方这个地方呢看一下这个URIMesser的get然后呢URIURI呢其实这都是我们访问过的一些路径呢是吧那么我们可以这样我们可以在这个地方访问一下localhost80808080
[10:03] -user-findall是这个吧好是个size然后呢我们再刷一下过来看这个地方你看user-findall是不是进来了进来了之后呢注意啊我们直接添加一个添加一个之后呢你注意看count它访问了一次吧然后呢我们在这刷你看两次吧刷三次哎三次是吧有点慢啊三次对吧所以你可以看某个路径呢被调用了多少次某个接口被调用多少次你可以挨个在这过滤啊OK
[10:33] 那么这个呢是环境的信息啊环境呢就是我们的environment刚才那些信息啊比如说我们配的那个我们自己配的那些信息呢在最下边看刚才我们配的这几个信息是不是都在这个地方有展示啊图形化界面的方式来看然后呢bin是我们的所有bin我们的bin呢有很多啊一大堆的bin而且都是图形化界面的方式啊我们来找一下我们自己的user controlleruser Controller可以看到吧user Controller没问题吧
[11:03] 然后从哪个文件过来的对吧从这个自己码文件过来的等等都可以看得到然后Configuration Properties一些配置的信息都可以看得到然后这个地方Schedule Task就是我们的任务调度现在我们没有任务调度所以这个里边啥也没有那么还有一些日志的信息我们就不看了日志你可以在这看一下我们就不看了然后JVM内存相关JVM讯息相关的信息JMX我们的一些管理信息管理信息里边比如说我们TOMCAT的一个
[11:33] 一个管理啊比如说我们的一个浪包里边的class loading啊比如说加载多少类啊8000多个类loaded class count好有很多的信息都可以看哈那么还有呢现成Thread你看这个很有意思当前这个client这个项目里边有多少现成呢一共在跑你看是不是都在走啊这些现成你看啊绿色的表示他正在运行红色黄色的表示他在等待你可以看一下绿色的你看这个地方的现成的状态是renewable
[12:03] 现在在等待
[12:32] 所以你如果将来想去观测某一个线程的情况你可以看它们是一个交替运行的过程因为如果是单核的CPU的话它是多个线程随机切换你可以看到哪个线程正在运行非常的智能还有堆栈的一些信息当然你要下载这个文件去分析的然后这个地方就是WebMappings这个Mappings就是我们的一些访问的接口路径比如说我们刚才写的user-findall
[13:03] 在这个地方可以看到对吧这是我们访问的路径没问题吧然后呢可以看到一些描述的信息然后呢HTB Trans也可以看到我们的一些Find All的访问对吧访问的一些个情况比如说他请求的一些参数啊然后呢响应的一些参数啊都可以看得到没问题是吧然后其他的呢我们就不再去看了Catchs也没有缓存哈
[13:28] 所以基本上我们就这么一些个监控平台我们就可以看到对应的一个信息了然后这个applications你可以绑定多个项目比如说你可以再创建一个项目这个地方就有两个列表了这就是二了那么同样的你也需要去指定对应的一个admin的服务器端的地址OK吧所以这个图形化界面用起来还是非常的方便的
[13:53] 但是呢如果你每一次要用的话都搭图形化界面其实还是比较麻烦一般生产环境我们才会用它那么如果做开发做测试呢我们用它其实就挺麻烦的还要去导坐标还怎么怎么着对吧而idea它给我们提供了非常强大的功能你注意看我们这个client是不是起起来了看到了吗client起起来了你看这个console旁边是不是有endpoint点一下beans健康检查mappings
[14:21] 这三个比较常用的功能它是不是给我们提供了那bin里边首先是application下面有多少bin呢很多bin是吧刚才我们也看到了比如说我们的user Controller你看没问题吧OK我们点一个比较多的多的时候你看多的如果是比较多的话它有个继承结构对吧我们可以点大一点可以看这个地方看一下对吧它这个地方呢IDR帮我们把这些endpoints的这些信息给你分析了形成了这种图形化界面的方式
[14:50] 健康检查也可以看到你看自传的信息对吧是不是都可以看到如果你加了Redis呢这个地方还有一个列表是Redis的然后呢Mappings路径是不是也有啊都有啊都有没有问题是吧所以呢这个地方呢都非常的好就是IDEA也给我们提供了这种信息让我们去看哈非常的方便好嘞那么对于这种监控功能我们就详细完毕了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Spring Boot Admin 监控一个 Spring Boot 应用，并展示其内置的 Actuator 端点和相关监控信息。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 IntelliJ IDEA 中一个名为 `Spring Boot-actuator` 的 Spring Boot 项目，其中 `UserController.java` 文件包含一个 `@RequestMapping("/user")` 和 `@GetMapping("/findAll")` 的 REST 控制器方法，返回 "success"。同时显示了项目结构和 `application.properties` 文件。
画面 2: 显示 IntelliJ IDEA 的主界面，项目结构中包含多个 Spring Boot 相关的模块，如 `Spring Boot-admin-server` 和 `Spring Boot-admin-client`。
画面 3: 显示 IntelliJ IDEA 的 "Project Structure" 对话框，正在配置 `Spring Boot-admin-server` 模块的源码目录，其中 `src/main/java` 被设置为 "Sources"。
画面 4: 显示 IntelliJ IDEA 中 `Spring Boot-admin-client` 项目的结构，其中 `src/main/java` 目录下包含 `SpringbootAdminClientApplication.java`。
画面 5: 显示 IntelliJ IDEA 中 `Spring Boot-admin-server` 项目的结构，其中 `src/main/java` 目录下包含 `SpringbootAdminServerApplication.java`。
画面 6: 显示 IntelliJ IDEA 中 `Spring Boot-admin-client` 项目的 `SpringbootAdminClientApplication.java` 文件，其中包含 `@EnableAdminClient` 注解和 `main` 方法。同时显示了控制台输出，表明客户端应用已成功启动。
画面 7: 显示浏览器中 Spring Boot Admin 的 Web 界面，左侧导航栏中选中了 "Metrics" 选项卡。
画面 8: 显示浏览器中 Spring Boot Admin 的 "Wallboard" 页面，内容为空白。
画面 9: 显示浏览器中访问 `localhost:9000/user/findAll` 端点，返回 "success"。
画面 10: 显示浏览器中 Spring Boot Admin 的 "Beans" 页面，列出了应用中的所有 Bean，如 `tomcatWebServerFactoryCustomizer`、`userController` 等。
画面 11: 显示浏览器中 Spring Boot Admin 的 "Threads" 页面，列出了应用中的线程信息，如 `http-nio-8080-exec-1`、`http-nio-8080-exec-2` 等。
画面 12: 显示浏览器中 Spring Boot Admin 的 "Mappings" 页面，列出了应用中的所有 HTTP 映射，如 `/actuator`、`/user/findAll` 等。
画面 13: 显示浏览器中 Spring Boot Admin 的 "Web" 页面，选中了 "Mappings" 选项卡，显示了应用的 Web 映射信息。
画面 14: 显示 IntelliJ IDEA 中 `Spring Boot-admin-client` 项目的 `UserController.java` 文件，其中包含 `@RequestMapping("/user")` 和 `@GetMapping("/findAll")` 的 REST 控制器方法。同时显示了控制台输出，表明客户端应用已成功启动。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
package com.ithema.springbootactuator;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RequestMapping("/user")
public class UserController {
    @GetMapping("/findAll")
    return "success";
}
```

画面 4:
```
src/main/java
com.ithema.springbootadminclient
SpringbootAdminClientApplication
```

画面 5:
```
src/main/java
com.ithema.springbootadminserver
SpringbootAdminServerApplication
```

画面 6:
```java
public class SpringbootAdminClientApplication {
    public static void main(String[] args) {
        SpringApplication.run(SpringbootAdminClientApplication.class, args);
    }
}
```

画面 10:
```
tomcatWebServerFactoryCustomizer
org.springframework.boot.autoconfigure.web.embedded.TomcatWebServerFactoryCustomizer
traceRepository
org.springframework.boot.actuate.trace.http.HttpMemoryTraceRepository
uptimeMetrics
io.micrometer.core.instrument.binder.system.UptimeMetrics
userController
com.ithema.springbootadminclient.UserController
viewControllerHandlerMapping
org.springframework.web.servlet.mvc.handle.RequestMappingHandlerMapping
viewResolver
org.springframework.web.servlet.view.ContentNegotiatingViewResolver
webEndpointDiscoverer
org.springframework.boot.actuate.endpoint.web.annotation.WebEndpointDiscoverer
webEndpointPathMapper
org.springframework.boot.actuate.endpoint.web.annotation.WebEndpointPathMapper
```

画面 11:
```
RMI TCP Accept-52782
RMI TCP Accept-0
RMI Scheduler(0)
Catalina-utility-1
Catalina-utility-2
container-0
http-nio-8080-BlockPoller
http-nio-8080-exec-1
http-nio-8080-exec-2
http-nio-8080-exec-3
http-nio-8080-exec-4
http-nio-8080-exec-5
http-nio-8080-exec-6
http-nio-8080-exec-7
```

画面 12:
```
Handler Method org.springframework.boot.actuate.endpoint.web.servlet.AbstractWebMvcEndpointHandlerMapping$OperationHandler#handle
Methods GET
Produces application/vnd.spring-boot.actuator.v1+json, application/json
Handler actuator root web endpoint
Handler Method org.springframework.boot.actuate.endpoint.web.servlet.WebMvcEndpointHandlerMapping$WebMvcLinksHandler#handle
Handler public java.lang.String com.ithema.springbootadminclient.UserController.findAll()
Handler Method org.springframework.boot.autoconfigure.web.servlet.BasicErrorController#error
Produces text/html
Handler public org.springframework.web.servlet.ModelAndView org.springframework.boot.autoconfigure.web.servlet.BasicErrorController#error(java.lang.String, java.lang.Object, javax.servlet.http.HttpServletRequest, javax.servlet.http.HttpServletResponse)
```

画面 13:
```
application
dispatcherServlet
/**/Resource
Handler ResourceHttpRequestHandler [class path resource (META-INF/resources/), class path resource (resources/), class path resource (static/), class path resource (public/), ServletContext resource []]
/actuator/audit/tenant
Methods GET
Produces application/vnd.spring-boot.actuator.v1+json, application/json
Handler Actuator web endpoint 'audit/tenant'
/actuator/beans
Methods GET
Produces application/vnd.spring-boot.actuator.v1+json, application/json
Handler Actuator web endpoint 'beans'
```

画面 14:
```java
package com.ithema.springbootadminclient;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RequestMapping("/user")
public class UserController {
    @GetMapping("/findAll")
    return "success";
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

