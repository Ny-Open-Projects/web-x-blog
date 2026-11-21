# 5.服务调用链路追踪-入门案例

- 阶段：10.阶段十 万信金融项目
- 章节：08_万信金融-微服务高级部分/8-1 服务调用链路追踪的理解和使用
- 源文件：10.阶段十 万信金融项目\08_万信金融-微服务高级部分\8-1 服务调用链路追踪的理解和使用\5.服务调用链路追踪-入门案例_【海量资源尽在 666java.com】.mp4
- 时长 14分28秒（音频 868s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们提到啊要想使用这个slose啊非常的简单是不是只需要两步就行了对不对那咱接下来呢为了最终让大家看到这个链路追踪的一个效果呀我们还是要来一个入门案例啊一个demo那咱首先先了解一下这个demo在这个demo里边呢我们准备涉及什么呀两个微幅啊一个叫A一个叫B然后呢在这两个微幅之间呢我们要形成一个什么呀调用链啊
[00:29] 就是具体来说就是前端先发一个请求到什么呀微服A当中的1这个位置啊先往这发请求然后呢这个位置啊来去干什么呀去调用微服B往这发起请求对不对然后呢他再回来啊再调微服A当中的另外一个位置这是形成了一个调用链对不对这咱就是一个demo啊这里边不涉及到什么
[00:56] 业务或者要完成什么功能纯粹呢就是让两个微服务之间发生一个相互调用的一个关系在这个过程当中呢我们就准备用这个什么呀smooth对不对让他去追踪一些什么呀对一些信息就这么一个demo那咱接下来就实现这个demo咱刚才提到是不是涉及到两个微服啊所以说你是不是也需要把这两个微服工程给先创建出来啊这个过程我就不再演示了我提前已经创建好了啊大家看一下整体先过一步
[01:28] 那一个微服务工程叫sluice demo1其实就是我们图当中的这个什么呀微服务a吧还有一个微服务工程叫sluice demo2其实就是图当中的微服务b对嗯然后现场的东西咱整体过一下吧pom文件里边大概的大家看我们就引入了spinbootspincloud它相关的一些什么呀elite和learnbook对吧等等了这个我就不再过头说了还有呢这个
[01:57] 配置文件配置文件里边大家看一下名字啊基本访问路径啊端口号这些呢大家也非常熟还有就是这个什么呀启动类启动类呢跟平时也没啥区别就是多了这么一个对象大家看一看rest template这个大家还有印象吗rest template是不是我们spring提供的一个什么呀一个工具吧通过这个工具主要是干啥的它主要起什么作用
[02:26] 对就是在微服务之间发起这个什么样远程请求远程调用的那我们这只是一个入门的一个demo吧我们就简单一些就通过这个谁啊对rest template对象完成微服务之间的一个什么呀对一个请求啊或者一个调用啊所以说呢我们在启动内当中呢把这个对象呢给他创建出来一会发起请求或者调用的时候我们通过他就可以搞定了
[02:52] 然后别的就没啥了啊那么slose demo2里边也是一样的碰碰文件跟demo1里边也一样这个什么呀这也都是一模一样的啊包括这个启动类这些都一样这是我们现在吧相当于把这两个微服工程呢都已经创建好了那把这两个微服工程都创建好之后我们首先是不是得先把这个slose先加进来是不是咱前面提到过了吗
[03:19] 要想在微服务当中去集成我们的这个slus是不是只需要两步啊是不是对只需要两步第一步呢就是加入这么一个依赖就这个要加进来那这两个微服务工程都在家吧对不对你找到他们的碰碰文件找到一个就就到这儿吧是不是然后demo2里边我们也要加一下然后还有一步啥
[03:50] 还有一步呢是不是就是需要在配置文件里边去开启这个slus对不对开启这个功能就行了很简单这个呢代码我们敲一下吧我们找到demo1的这个配置文件在这啊加个注释吧就是干什么呀对我们要开启slus怎么开启呢就是spring.slus然后点什么inable对不对给一个值就是什么呀
[04:22] 那Demo2那边是不是Demo一模一样对不对Demo2我们找一下这就搞定了对不对就这两步啊我们就在我们这两个什么微服务当中把slose给干什么呀加进来加进来它就可以工作可以干活了呀就是追踪这个什么样日志信息嘛对不对那要想看到效果我们是不是得按照刚才咱们这个案例的这个什么呀这个需求我们得让两个微服务之间产生一些什么呀调用啊这个调用的话我们是不是得
[04:54] 那我微服A这边是不是也整个Controller对不对微服B这边是不是也得整个Controller是不是然后呢前端发请求先到微服A的Controller然后微服A的Controller再通过rest的什么呀template呢对不对这个发起请求到哪到微服B这边最终是不是形成一个调用链对不对所以接下来我们要在两个微服工程里边要干什么呀对要去编写Controller这一块的这个什么呀代码我们回到这个idea当中呢我们一个一个来吧
[05:24] 大家看一下啊我在这两个微服工程当中呢其实都已经提前把扛出来类是不是创建好了对不对咱打开看看只不过里边呢都是空的这些代码咱需要编写编写啊就是按照咱刚才这个图当中的这个分析把这个代码编写完咱就可以进行什么样功能测试去看效果了啊那咱先说说这个什么呀demo1这边的这个Controller那这里边我应该最终是不是应该要定义两个方法吧demo1这边你看看
[05:56] 是不是应该有两个方法第一个方法去远程调用微服务币然后呢第二个方法呢是被微服务币去远程什么呀调用呢那咱一个一个来吧先说这个一这个方法咱这里边没啥业务没啥业务所以说咱一会呢就是打印一些东西就行public啊我们返回知识string类型发明咱就叫node1啊然后呢我们在这里边的话
[06:25] 这个参数的话我们暂时为空吧现在我们也不需要有什么参数啊空的就行了那在这里边干啥这边我们说了我们这只是一个demo吗也没啥业务我们就打印一些东西吧我们把这个这次请求涉及到的这个名字的打印一下我们涉及到是不是这个s l e u t hslus1对吧这个微服啊或者a也行啊然后呢它对应的是s e r v s e service1吧
[07:00] 就这个一图当中这个一我们就打印这么一句话就行了我们便于将来在控制台观察那在这个方里边我们主要完成的任务是啥是不是要去远程调用谁啊微服币这边是不是通过谁啊通过rest template所以我们需要把这个rest template对象给它注入进来这个rest template我们是不是放到这个启动类当中已经配置过了对吧作为币所以我们这呢直接注入进来就可以用
[07:37] 然后怎么通过他发请求啊那就是red template他有一个方法叫get哪个呢叫get for object我们用这个方法就可以发起一次什么呀对一次请求一次调用那么大家看第一个参数是不是请求的地址第二个参数呢就是参数的这个类型吧我们就是一个字符刷就行了其实我们也没传啥数据
[08:06] 好第一个是一个请求地址第二个呢是参数的类型呢我就写上tree我们都是字串类型吗tree.什么呀把这个东西扔给他就行那这个请求的地址咱一会再编写吧因为这个是不是涉及到哪边啊是不是涉及到demo2就是微幅b那边对不对这个地址咱一会再说那请求完之后的话他那边是不是应该会返回给我们一个结果就是一个字串吧我们接收一下
[08:35] 我们声明一个变量这个变量的话我们跟讲义保持一致吧咱看一看他的名字是叫sloss2service1对不对这样子我们就完成了这个什么调用然后呢我们这边是要返回一个字幕串这个字幕串呢我们要跟讲义保持一致我大家看一下啊我们就大概打印这么一个信息吧就是当前的位置是在sloss1service1是不是然后呢
[09:14] 后来去了哪就是我发的这次调用是不是去了这个地方对不对那他反为啥我这就打印啥就拼接一个搜索上去打印就行那这个方案呢就定义好定义好之后呢上面别忘了我们是不是要加上给他卖品来设置一个什么呀啊访问路径那我们这个访问路径就叫s e r v i c service1这个要加两边要加什么双引号哎大家看这个功能是不是很简单对不对嗯这个诺的一里边我就是打印一些东西然后呢就通过res template
[09:47] 网什么呀对微服币啊或者demo2那边就发请求了那咱按照这个流程去写代码那这边一发请求我们是不是应该去哪来应该去这个微服币这边这边是不是应该也有一个control对吧然后让他去调用去防了就行自然接下来就回到demo2就微服币这边我们找到他的control了在这里边我是不是应该也要定义一个什么呀防法那这个代码呢其实跟刚才这个demo1那个control里边代码差不多我就不再给大家编写了
[10:16] 我就直接拿过来用一用恢复币这边是不是Controller咱找一找其实就这块代码它这里边只需要一个方法就行了咱拿过来之后咱一起看一看这个地方咱先空的先扔到这儿你看这个代码跟咱刚才在demo1的Controller里边编的代码是一模一样是不是要住一个rest的template对不对然后给它map设置一个什么防护剂这个参数咱暂时也用不到
[10:51] 先空的啊他的名字也叫乐乐一这边是不是也打印了一个信息但是他叫sluice二Service一个Service一对应的就是这个名字了sluice二指的是咱这边是微服币码然后呢这边他其实干了一件事也是通过res template发起一个请求让大家看一下还是看这个图是不是你看微服这边是不是也要通过res的template发起请求到哪到微服a这边你看这个代码跟刚才写的一模一样的还是掉get for object
[11:23] 那这边就是请求的地址先空的啊先扔到那然后呢他返回的信息呢我在这儿是不是也做一个拼接然后返回就行这是demo2这边我们把control里边代码也写了一下那写完之后按照流程我们又要去哪又要去微服A这边是不是再次定义一个方法因为我们这个微服B这边是不是要往这发警球嘛就这个地方是不是咱们接下来要回到什么呀对demo1这边在下边是不是再加一个这个方法
[11:53] 那这个方法我也不再给大家编写了它更简单我们直接从讲义里边拿过来就行就是这个方法更简单它也不需要调用别的这个微服了就其实到这儿是不是就结束了直接返回就行Source2对不对然后这个参数呢咱暂时也用不着先不用管了就做一个打印返回一个信息就行这是两个微服工程当中的这个什么呀Controller里边的代码咱就全部编写完编完之后咱串一串那也就是说呢将来是这样前端发一次请求是不是发到这儿
[12:26] 就demo1的这control了里面啊往这发请求然后呢他是不是记录一些日志信息对不对然后呢通过rest template往哪发请求啊对往这个demo2就是v4b那边去发请求发请求这个请求地址咱现在是不是就可以给他补充上了对不对那不就是往什么呀往这发请求吗service1嘛对不对那咱就给他补充上呗那前面写啥
[12:56] 前面写的基本访问路径你应该查查配置文件对不对是这儿然后端口号是58012是不是前面你就是什么5801258012前面应该写啥大家应该都清楚了http://localhost5802没错这边一发请求是不是流程就该跳转了这应该跳转到这边这就是vfb就是demo2这边
[13:29] 然后这边也是感应日志然后呢这边也要发次发起什么呀一次请求到哪到微服A就是demo1这边你看这个图是不是又拐回来了对不对就二到三之间啊这个点那这个时候让大家看我们这个地址是不是也可以进行什么呀晚上这个我就不再给你敲了啊我们直接从讲习的边拿过来就行你对照这个配友链你就知道这个代码该怎么写就细心一点这个路径别敲错了就这个点拿过来就行
[14:07] 那这边一发请求是不是又拐回来你看它是什么呀slose1service2对不对那不就又调用跑到这了吗对不对service2那到这是不是这个调用就结束了打印一下日志然后返回一个结果搞定这是目前吧咱们把这个入门案例的代码就全部编写完毕了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过 RestTemplate 实现两个微服务之间的调用，并集成 Spring Cloud Sleuth 进行链路追踪。

2) 按时间顺序列出每张画面的要点：
画面1：展示 PPT 页面，内容为“2.2.2.2 功能实现”下的“2.2.2.1 微服务A”，并说明需新建名为 SleuthDemo1 的 Maven 工程并引入依赖。PPT 中展示了一个调用链图，前端请求先调用微服务A（节点1和3），再由微服务A调用微服务B（节点2）。
画面2：在 IntelliJ IDEA 中，展示 SleuthDemo1 项目结构，光标位于 TestController.java 文件，该文件中定义了 @RestController 和 @RequestMapping 注解的 TestController 类。
画面3：在 IntelliJ IDEA 中，展示 SleuthDemo2 项目结构，光标位于 application.properties 文件。
画面4：展示 PPT 页面，内容为 Maven 依赖配置，包括 spring-boot-starter-web 和 spring-cloud-starter-sleuth。
画面5：在 IntelliJ IDEA 中，展示 SleuthDemo2 的 application.properties 文件，其中配置了 spring.application.name、server.servlet.context-path、server.port 和 spring.sleuth.enabled。
画面6：在 IntelliJ IDEA 中，展示 SleuthDemo1 的 TestController.java 文件，光标位于类定义处，提示符为 @RestController。
画面7：在 IntelliJ IDEA 中，展示 SleuthDemo1 的 TestController.java 文件，光标位于类定义处，提示符为 @RestController。
画面8：展示 PPT 页面，内容为“2.2.1 案例简介”，说明需创建两个微服务并通过 RestTemplate 实现调用，形成调用链。
画面9：展示 PPT 页面，内容为“4. 启动类”和“5. Controller类”，分别展示 SleuthDemo1Application 启动类和 TestController 控制器类的代码。
画面10：展示 PPT 页面，内容为“3. Spring Boot配置”和“4. 启动类”，分别展示 application.properties 文件中的配置和 SleuthDemo2Application 启动类代码。
画面11：在 IntelliJ IDEA 中，展示 SleuthDemo2 的 TestController.java 文件，光标位于 node1 方法中，代码为使用 RestTemplate 调用服务1。
画面12：在 IntelliJ IDEA 中，展示 SleuthDemo2 的 TestController.java 文件，光标位于 node2 方法中，代码为使用 RestTemplate 调用服务2。
画面13：展示 PPT 页面，内容为 Maven 依赖配置，包括 spring-cloud-starter-sleuth 和 spring-cloud-dependencies。
画面14：在 IntelliJ IDEA 中，展示 SleuthDemo2 的 TestController.java 文件，光标位于 node2 方法中，代码为使用 RestTemplate 调用服务2。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1：
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.1.3.RELEASE</version>
    <relativePath/>
</parent>
<groupId>com.ithema.msa.sleuthdemo</groupId>

画面4：
<java.version>1.8</java.version>
<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
<project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
<spring-cloud.version>Greenwich.RELEASE</spring-cloud.version>
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-sleuth</artifactId>
    </dependency>
</dependencies>
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-dependencies</artifactId>
            <version>${spring-cloud.version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>

画面5：
spring.application.name=SleuthDemo2
server.servlet.context-path=/sleuth2
server.port=58012
#是否开启sleuth
spring.sleuth.enabled=true

画面9：
@SpringBootApplication
public class SleuthDemo1Application {
    public static void main(String[] args) {
        SpringApplication.run(SleuthDemo1Application.class, args);
    }
    @Bean
    public RestTemplate getRestTemplate() {
        return new RestTemplate();
    }
}

画面10：
spring.application.name=SleuthDemo2
server.servlet.context-path=/sleuth2
server.port=58012
#是否开启sleuth
spring.sleuth.enabled=true

画面11：
@GetMapping("service1")
public String node1(){
    log.info("sleuth_service1");
    String sleuth_service1 = restTemplate.getForObject(url, String.class);
    return "sleuth_service1---"+sleuth_service1;
}

画面12：
@GetMapping("service2")
public String node2(){
    log.info("sleuth_service2");
    return "sleuth_service2";
}

画面13：
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-dependencies</artifactId>
    <version>${spring-cloud.version}</version>
</dependency>

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1：标题为“2.2.2.2 功能实现”，子标题“2.2.2.1 微服务A”，图示为前端请求调用微服务A（节点1和3），再由微服务A调用微服务B（节点2）。
画面8：标题为“2.2.1 案例简介”，图示为前端请求调用微服务A（节点1和3），再由微服务A调用微服务B（节点2）。
画面9：标题为“4. 启动类”和“5. Controller类”，分别展示 SleuthDemo1Application 启动类和 TestController 控制器类的代码。
画面10：标题为“3. Spring Boot配置”和“4. 启动类”，分别展示 application.properties 文件中的配置和 SleuthDemo2Application 启动类代码。

5) 无。

