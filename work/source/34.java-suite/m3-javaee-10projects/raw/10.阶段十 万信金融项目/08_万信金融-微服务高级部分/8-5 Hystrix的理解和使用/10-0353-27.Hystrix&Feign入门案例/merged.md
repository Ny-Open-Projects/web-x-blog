# 27.Hystrix&Feign入门案例

- 阶段：10.阶段十 万信金融项目
- 章节：08_万信金融-微服务高级部分/8-5 Hystrix的理解和使用
- 源文件：10.阶段十 万信金融项目\08_万信金融-微服务高级部分\8-5 Hystrix的理解和使用\27.Hystrix&Feign入门案例_【海量资源尽在 666java.com】.mp4
- 时长 14分48秒（音频 888s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们一起了解了一下Hastrix这个组件对吧那么接下来呢咱就来一个入门案例那么由于呢这个Finn和这个Hastrix大家都知道它都属于什么呀Support Cloud组件那么因此呢它俩呢就会经常作为好基友对吧一起在项目当中去使用所以咱接下来这个入门案例啊就是拿着它俩做这个什么呀机场
[00:29] 我们通过飞印去发起远程调用远程请求在这个时候呢我们通过谁啊对Hastrix组件对这个什么呀调用实施熔断和什么呀降级处理咱接下来把这个入门案例呢编写一下首先呢我们这边呢是创建了一个副工程名字叫飞印Hastrix看一下就是这个对吧
[00:58] 那在复工程的碰母链当中呢我们会做一些什么呀啊依赖管理咱整体回到i店当中咱过一遍吧比如这个碰文件呃一会呢大家会看到我们整个这个入门里当中一共会包括三个工程就是三个模块大家看一下一个是助投中心对不对然后两个微服务一个a一个b然后将来呢比如说我就可以让这个什么微服a
[01:25] 通过飞去访问什么呀微服务b在这个过程当中呢我通过黑色tricks在里面对进行熔断保护就行了啊这里面是不是只是规定了一下spin cloud的这个版本这是复工程复工程完了之后呢咱接下来一起了解一下这个什么注册中心这个注册中心还是使用的有微卡没啥好了解的跟你之前见过的这个注册中心没有任何区别啊朋友你现在就不再看了
[01:54] 你就顶多看看他的这个什么呀这个配置文件吧他的端口号是什么呀59020就行了其他我就不再说了然后呢就是这两个微服一个A一个什么B咱们把这里边的基本代码过一遍先说A吧A里边这个Po文件里边你看我们需要引入的相关的这个什么呀相关的这个jar 包你看看啊我们挑中间给他说一说就Rica Client对吧
[02:25] 纽约卡客户端吧因为对于我们这个A和B两个微服来说它都是注册中心的客户端对不对然后飞然后就是这个什么呀对Histrix这个包也需要引进来这是我都已经过了这是POM文件然后呢我们看看配置配置这里边没啥好特殊的吧没有特殊的地方啊名字啊端口号啊进门访问路径啊这是不是呢一个注册中心的地址是不是这没啥特殊的地方啊加上代码
[02:54] 成为一首加代码启动类没啥特殊的吧对不对然后还有啥Controller一个Controller和一个什么呀非音代理我们说了我们要要让微服a是吧通过这个非音代理去往哪发请求啊往微服b那边是不是你看这是不是在这个什么微服a的Controller里面这个方案里面是不是应该是通过这个非音代理是不是开始发请求了对不对
[03:23] 那么看这个飞行代理呗飞行代理大家比较熟了这是Service b 那边的这个名字对不对然后这是微服b 那边的什么呀访问路径这个大家比较熟这是微服a这边的这个代码基本代码啊然后咱看看微服b这边这边破文件它也一样是不是也需要引入这个什么呀有一个可兰他呀啊飞呢还有什么呀黑色chicks是不是都一样啊然后呢配置里边这个代码也都一样名字啊
[03:55] 端口号呀基本返回路径啊对吧这个注册中心的地址啊老闆加个代码加个代码这边更简单行动类这个没啥好说吧好抽着这边就一个扛抽着刚才这个微服a那边通过飞应是不是就是其实就是往这发清球吧对不对是往这发清球这是我们这个入门案例当中的现有的一些什么呀基本的一些代码咱整体过来一下非常简单啊说白了就是a往b发清球啊通过什么通过飞应
[04:29] 那接下来我们要思考的就是我怎么往这个案例当中加入这个什么对熔断这个功能呢对不对通过Histrix对吧把这个功能怎么加进来这个加这个功能特别简单特别简单因为我们刚才说了飞鹰和Histrix现在是不是都属于Spring Cloud的这个组织是一家人对不对一家人一家人不说两家话什么意思呢这个飞鹰和这个Histrix它俩的这个集成是怎么样
[04:57] 怎么说呢是已经都已经设计好了啊所以说他俩集成到一起非常非常的简单只需要两个步骤就行了啊第一个步骤就是加一个配置就是这把这个熔断器啊就是这个保险丝给他干什么呀启用了就行了就这么简单这第一步啊就加这么一个什么呀配置就行了在哪家是不是在配置文件里边我们找到这个谁呀配置文件配置文件在这对不对
[05:33] 先写个入是吧那就是启用什么呀其实就启动这个段路器啊怎么启用啊飞点什么呀哎就是第一项飞点我们应该给一个什么指出就表示什么呀对启用这个什么呀这个保险丝了啊启用这个段路器了这是第一步啊第一步那其实这一步你这个配置你加上之后其实这个段路器就已经干什么已经工作了已经起作用了啊
[06:08] 但是呢我们还有一步需要做哪一步呢我们前面在介绍Heads Tricks的时候我们说过啊一旦某个服务呢它这个发生了这个熔断我们是不是得进行这个什么后续的处理就是要进行什么呀降级回退对不对那一旦这个微服务熔断了我接下来要干啥呢我怎么降级怎么回退呢我们说可以返回空值返回默认值甚至什么呀把缓存当中的一些数据返回对吧总之吧
[06:37] 我们得有一个什么呀降级回退我们写代码啊搞定这个建议回退那这块代码写到哪呢写到哪呢大家想一下我们这个地方发请求是通过什么去进行请求的呀是通过这个非应代理是不是微服a这边呢就是通过这个非应代理往微服b那边发请求那熔断是不是也是在这时候起作用的对不对
[07:03] 那如果说这时候熔断发生了我要进行服务降级这个服务降级啊或者服务回退的这个代码呢我也应该写到这个什么呀对就是发请求这个地方啊就是非应代理这里那具体怎么写呢咱一起看一看咱一起看一下这个讲义吧看讲义当中是怎么实现的我们找一找这个代码在这
[07:30] 这是我们这个微服A里边这个非音代理你看在非音代理里边我们是不是之前经常会用到一个注解叫非音client是不是这边我们以前经常写的这个内幕属性那么我们要想实现这个降级回退的话需要在这个注解里边再增加一个属性叫fallback factory这个属性是干嘛的呢下面有介绍
[07:56] 他指的就是这个降级的一个什么呀工厂类啊一个工厂类一个类啊那你看后边这个值是不是就是一个类对不对这个类在哪呢这个类在下边是咱单独自己定义的一个类但是这个类呢肯定不是咱定义的一个很普通的类对吧这个类要实现这个什么呀要实现histrix的fallback factory这个接口啊同时呢要指定这个什么呀
[08:25] 这个接口啊就非音代理这个接口作为他的这个什么呀范形然后在实验这个接口的时候呢要重写他里边的这个什么方法这个方法最终就创建出来一个什么对象呢他叫降级实现对象在这个对象里边呢我们就要把具体的这个什么呀降级回退的这个什么动作啊或者这个业务放到这里就把这块代码就写到这个可以的方案里那由于呢我们这样呢是不是只是一个呆梦啊所以说我就
[08:55] 做了一个简单的处理怎么处理呢你看啊我在这里边是不是最终溜出来了一个什么呀是不是还是这个接口的一个代理对象吗你看Service b 二进了对不对然后呢在实现这个Service方案的时候呢我这里边做了一个简单处理就是输出了一个什么呀或者返回了一个字幕转就是Service b 熔断了我们将来看到啊打印出来这句话我们就知道是不是这个降级回退这个效果已经出来对不对那在真实开发的时候呢你这里边啊你这块这个逻辑啊
[09:25] 有可能你是返回一个空值有可能是返回一个默认值有可能是把缓存里边的数据干什么返回来等等等等都有可能啊我这呢只是一个demo我就返回这么一个字符串大家知道咋回事就行了那其实这大家看一下这个代码是不是不是很复杂那加上是这样当你通过这个非对不对通过这个非应代理发请求的时候一旦出现了熔断哎那这个时候呢他是不是就会找到这个类
[09:54] 是不是你看你这指定的不就是这个类吗对不对然后呢就会调用它里边的什么方法可以的方法最终呢把这个什么呀对我们说的这个降级实现对象给它创建出来而在这个降级实现对象里边我们是不是就指定了这个什么呀具体降级回退的一个什么呀动作啊我们刚才说了你可能会返回一个空值一个默认值或者说缓存当中的一些数据啊我这呢是一个demo就返回随便返回来一个字幕串而已
[10:23] 也就是将来熔断的时候啊一旦出现熔断哎这块呢就是实现降级回退的一个什么呀对一个业务逻辑的这个套路基本上是固定的就将来有可能就是这一块的代码不太一样但是其他的这个代码啊或者整体这个套路基本上都是固定的就在这啊你需要增加一个属性对吧fallback factory指定一个工厂类然后这个工厂类呢要实现这个接口在这里边重写cred的方法在这个cred的方法里边的话
[10:52] 我们是不是还是最终其实是是不是new了这个接口的一个实现类对吧匿名内部类嘛这一块这个代码是不是匿名内部类啊然后呢在这个方案里边呢具体去编码或者编写这个什么呀对降级回推的这个具体的这个动作这是咱们把这个代码大家熟悉一下咱接下来回到我们idea当中把这一块的代码呢我们给它干什么呀对给它补充上啊首先是不是这
[11:20] 我们要增加一个属性是不是叫fallback什么呀factory是不是一个这个什么呀对一个工厂类但是这个类咱还没创建啊所以说咱这样咱先把这个类呢给它创建出来class这个名字的话我们要跟讲义保持一致叫servicebargentheat tricks那这个类不是普通的类啊对不对我们说了它要实现一个接口就叫fallback什么呀factory
[11:50] 然后指定范形这个范形呢就是这个飞应接口就是它然后呢我们顺带着呢给它加上这个component这个注解那有了这个类之后呢我们这儿是不是就可以写值了啊第二什么呀对class然后大家看这儿是报错为啥报错因为我们实现了这个什么呀接口是不是就要实现它里边的这个方法我们把这个方法里面生成是不是那可以的方法呢刚才看到了在这里边是不是要创建那个降级实现对象
[12:27] 对吧那我们这里边呢很简单大家看一下是不是就是new一个这个接口的一个实现类在这个方案里边呢我们就是反而一句话就行了那我们怎么写那就是return什么呀对return newnew谁呀new这个接口就是一个匿名类分类当然你也可以用lambda的这个这个什么写法都写然后在这里边要干什么呀对在这里边我们是不是还是要重写这个什么呀
[13:01] 对重写这个方法他应该可以生成量我记得我再试一次啊s er Service哎对就是这样没生成这里边是不是具体实现这个什么呀啊服务降级回退的一个什么呀动作我这呢做了一个简化处理直接就返回了一句话对不对就是跟蒋英保是一致吧我们讲一下里边怎么写的Service b 容断这样我们看到这个字块就知道这块代码执行了啊或者说这个
[13:33] 熔断发生了啊然后呢也进行了这个什么呀就降级回退就可以了大家看一下这块代码不是很复杂吧那当然了将来你在项目开发过程当中呢这个凡是写这个什么非印代理的这个地方是不是都可以加这种代码来实现这个什么呀对来进行这个降级回退那这样子的话咱就把这个什么呀非印和
[14:02] PaceTrix这个集成的入门案例呢就给大家讲完了我把这个里边的关键步骤啊再给大家强调一下首先呢就是你的碰碰文件里边这些关键的这些依赖是不是你得导进来啊然后呢就是配置文件里边是不是开启这个什么呀这个段录器把这个功能给它启动了啊然后呢就是在分音代理这个地方
[14:27] 在费用代理当中是不是要增加代码对吧就是咱刚才写的这一块代码这一块呢是不是主要是实现降级回退这个右逻辑啊这是咱刚才就是这个入门案例当中关键的基点你把这几块代码给它写好就行了那这个例子呢咱就编写完了一会呢咱就要进行什么呀对进行测试

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Cloud 项目中集成 Feign 和 Hystrix，实现服务间的远程调用及熔断降级功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 的“3.1 父工程”章节，说明创建父工程 pom.xml。
画面 2: 在 IntelliJ IDEA 中展示父工程的 pom.xml 文件，高亮显示了 `spring-cloud-dependencies` 依赖。
画面 3: 在 IntelliJ IDEA 中展示 `Service-a` 模块的项目结构，准备创建服务代理接口。
画面 4: 在 IntelliJ IDEA 中展示 `Service-a` 模块的 `ServiceAgent.java` 文件，定义了 Feign 客户端接口。
画面 5: 在 IntelliJ IDEA 中展示 `Service-b` 模块的 `application.properties` 文件，配置了服务端口和上下文路径。
画面 6: 展示课程 PPT 的“2. 引入依赖”章节，列出父工程的依赖配置。
画面 7: 展示课程 PPT 的“3. application.properties”章节，列出 `Service-b` 的配置项。
画面 8: 在 IntelliJ IDEA 中展示 `Service-a` 的 `ServiceAgent.java` 文件，高亮显示了 `@FeignClient` 注解。
画面 9: 展示课程 PPT 的“5. Hystrix”章节，展示 `ServiceAgentHystrix` 类的代码，实现 `FallbackFactory`。
画面 10: 展示课程 PPT 的“6. Controller”章节，说明 `ServiceAgentHystrix` 类的作用。
画面 11: 展示课程 PPT 的“6. Controller”章节，再次展示 `ServiceAgentHystrix` 类的代码。
画面 12: 在 IntelliJ IDEA 中展示 `Service-a` 的 `ServiceAgent.java` 文件，高亮显示了 `@FeignClient` 注解。
画面 13: 在 IntelliJ IDEA 中展示 `Service-b` 的 `ServiceAgent.java` 文件，高亮显示了 `@FeignClient` 注解。
画面 14: 在 IntelliJ IDEA 中展示 `Service-a` 的 `ServiceAgent.java` 文件，高亮显示了 `@FeignClient` 注解。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.1.3.RELEASE</version>
</parent>

<modelVersion>4.0.0</modelVersion>

<groupId>com.itheima.msa.hystrix</groupId>
<artifactId>feign-hystrix</artifactId>
<version>1.0-SNAPSHOT</version>
<packaging>pom</packaging>
```

画面 2:
```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-dependencies</artifactId>
            <version>Greenwich.RELEASE</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

画面 4:
```java
@FeignClient(name = "feign-hystrix-Service-b")
public interface ServiceAgent {
    @GetMapping("/Service-b/Service")
    String Service();
}
```

画面 5:
```properties
server.port=9002
server.servlet.context-path=/Service-b
```

画面 6:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>

<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-Eureka-client</artifactId>
</dependency>

<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-openfeign</artifactId>
</dependency>

<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
</dependency>
```

画面 9:
```java
@Component
class ServiceAgentHystrix implements FallbackFactory<ServiceAgent> {
    @Override
    public ServiceAgent create(Throwable throwable) {
        return new ServiceAgent() {
            @Override
            public String Service() {
                return "Service-b熔断...";
            }
        };
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: 标题为“3.1 父工程”，内容为“创建一个名为FeignHystrix的maven工程作为父工程，pom.xml如下所示：”。
画面 6: 标题为“2. 引入依赖”，内容为列出父工程的依赖配置。
画面 7: 标题为“3. application.properties”，内容为列出 `Service-b` 的配置项。
画面 9: 标题为“5. Hystrix”，内容为展示 `ServiceAgentHystrix` 类的代码。
画面 10: 标题为“6. Controller”，内容为说明 `ServiceAgentHystrix` 类的作用。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

