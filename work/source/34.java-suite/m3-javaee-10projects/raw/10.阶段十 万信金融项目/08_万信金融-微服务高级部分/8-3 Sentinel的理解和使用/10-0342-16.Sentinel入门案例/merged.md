# 16.Sentinel入门案例

- 阶段：10.阶段十 万信金融项目
- 章节：08_万信金融-微服务高级部分/8-3 Sentinel的理解和使用
- 源文件：10.阶段十 万信金融项目\08_万信金融-微服务高级部分\8-3 Sentinel的理解和使用\16.Sentinel入门案例_【海量资源尽在 666java.com】.mp4
- 时长 18分36秒（音频 1116s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们整体上了解了一下阿里巴巴的Sentino框架那接下来呢就通过Sentino实现一个入门案例具体的了解一下如何通过Sentino实现限流来看看吧使用Sentino来实现限流主要分为几个步骤第一步呢就是定义资源那什么是资源呢他说了资源可以是任何东西这么解释的话好像我们还不太清楚啥是资源对吧
[00:31] 然后后边他举例子啊比如说某个服务哎这个呢我就明白了这个资源比如说就可以是我们某一个什么呀很具体的某个什么呀微服务对吧那我们将来是不是可以发请求到这个什么呀到这个微服务那么这个微服务呢就称之为是一个什么呀资源那当当然呢他还他说他还可以是某一个什么呀方法哎大家知道呢我发请求给某个微服务哎某个微服务呢他是不是还可以调用他里边的一些什么呀方法
[01:00] 那这个方法呢也可以当成是一个资源甚至是一段什么呀代码对吧都可以当成资源那我们要想实现限流啊必须先把这个资源给它明确了什么意思呢举个例子啊我们前面说过这个故宫对吧我们去故宫旅游那么故宫其实就是一个什么呀资源那我们要进行限流是不是就是为了保护故宫这个什么呀资源
[01:31] 明白吧那我们在软件系统当中也是一样的呀那我可以往微服务上发请求我也可以去调用什么呀某个方法那么这个微服务还有这个方法就是我们要保护的这个什么呀资源那将来我们限流也是针对这个资源进行什么呀限流的所以说第一步我们要明确资源那明确资源之后怎么保护它呀那我们就需要进行第二步就是定义这个什么呀对限流的这个什么呀规则
[02:00] 为了保护这个资源我要定义这个什么限流的规则举个例子我们刚才说了故宫就是一个资源对吧那我怎么保护它我就要进行限流那你就需要指定什么规则比如说故宫一天只接待5000个游客对吧5000名游客这个就是一个什么规则超过5000名我可以不接待对吧或者你排队这就是什么定义什么定义规则那我们这个软件系统也是一样的比如我可以设置一下这个我一秒钟对吧我一秒钟
[02:30] 最多处理1000个项目再多我拒绝啊或者说也让你等待对吧这就是什么规则第二步呢就是定义规则这两步搞定之后你接下来就是试试看看这个限流是否什么生效就行了啊这是咱大概吧了解一下使用Centino实现限流的话需要大概这几个步骤那咱接下来的话就开始编写这个什么呀入门案例啊我们需要单独创建一个Maven工程名字叫Centino Demo
[03:00] 这个工程呢我已经在ID当中创新好了咱们进来一起看一看先看它最基本的一些代码好大家看一下POM文件对吧这里边没啥好丑的Spring Boot Spring CloudWeb对吧大概引入的一些基本的一些依赖然后配置文件呢丑丑跟平时没啥区别吧对吧名字啊端口号啊基本访问路径还有什么呀这是什么呀启动类吧启动类没任何特殊的地方吧
[03:31] 然后一个Controller一个什么呀Service大家注意我们这就是一个demo我就我就不再进行分包了就全部扔到这一个包里边Controller咱看controllercontroller里边是不是就一个方法对吧hello方法然后注进来什么呀Service然后调用Service的hello方法这很简单吧然后咱看看这个什么要求要求就是一个hello方法然后返回了一个字母串叫什么呀hello Sentinel这个代码足够简单吗对非常非常简单
[04:02] 那咱接下来呢就是在这个例子的基础上呢我们把这个什么呀Centino框架加进来实现一个什么呀对一个限流的这么一个效果咱参考一下讲义看看具体该怎么做首先我们要引入Centino的这个什么依赖对不对阿里巴巴Centino这个依赖大家找一找在这儿是这个吧阿里巴巴Centino对不对需要先把依赖给导入进来那我们找到碰文件对不对就放到这儿吧
[04:33] 版本是2.1.0这是依赖导进来导进来之后呢我们看看啊配置不用动然后接下来还有什么呀Sorry 我们一会儿要写代码对不对我们大概过一遍Controller不用动那接下来咱看这个代码是不是主要编写在业务层咱去业务层瞅瞅吧我们准备怎么办呢大家看一下啊我们将来在测试的时候我是不是应该通过浏览器是不是往这发酵没错吧
[05:04] 你一往这发起来他是不是就调用业务层的这个什么呀哈喽方法对吧那现在我准备这样子啊我准备呢把这个哈喽方法定义成一个什么呀受保护的资源咱刚才不是提到过吗我们要使用Centino的话首先你得先干什么呀对定义资源然后他说资源可以是某个服务也可以是某个什么呀方法那我准备呢就是把业务层的哈喽方法定义成一个资源
[05:32] 那么将来你发请求到这然后他又会去调用这个什么呀对调用这个海楼方法哎我准备把它保护起来这是我们说的资源那定义好资源之后我们刚才说了要干什么呀接下来是不是你要定义这个什么呀限流规则那这个规则我准备这样子啊我为了保护这个海楼方法我准备定义这么一个限流规则就是一秒钟之内啊你最多只能调用两次这个海楼方法最多只能调用两次啊那如果超过两次的话就要进行什么呀
[06:04] 非常简单的一个规则咱就假设吧咱要实现最重要实现这么一个功能那怎么把它当成一个资源呢对不对又怎么为了保护这个资源去定义规则呢那这里边其实主要就是靠注解还有这个Centino的一些什么API咱接下来看看讲义这里边首先我们要用到的一个注解就是这个注解叫Centino什么呀Resource大家瞅一眼
[06:34] 那这个注解的话其实就是定义什么呀对资源呢你看这个单词是吧然后呢有两个常用的属性是不是那咱接下来呢把这个代码呢我们写一下要加到这个哈喽方案上面对吧我们说的这个哈喽方案就是什么呀注解就是这个资源对不对叫什么名叫centinoresource是不是然后呢这里边呢有两个常用的属性一个属性叫value这个value是用来
[07:04] 设置这个资源的名字资源总得有个名字而且这个名字呢一会我们在定义呃限流规则的时候要用那这个名字你可以随意命名啊这个没有啥规定我这还叫什么呀哈喽吧那后边第二个参数是干嘛的呢咱看看啊他叫blockhander啊然后后边是不是一个字符算那实际上呢他不是一个字符算啊呃我的意思是放到这儿他是一个字符算类型的一个值但是他本质上其实是一个什么呀你往这看
[07:34] 对它是一个方法它是一个方法那第二个属性的作用是用来设置限流的后续动作那你比如说啊假设这个这个资源被限流了那限流之后呢限流之后可能还会有不断的请求不断的调用过来怎么办呢你可以拒绝它你可以让它干什么呀排队总之你一定会有什么呀要做什么要做限流的后续动作对不对那么这个后续的动作你可以定义到一个方法里边然后呢在这儿
[08:04] 指定这个方法的名字都行那将来一旦出现限流了那么他就会去自动调用这个方法执行这里面的逻辑那由于呢咱这只是一个demo所以这我这也没啥逻辑就是直接返回来一个什么字母串系统繁忙请稍候这个大家知道了咋回事就行了那接下来呢我们把这个属性呢把它补上这个发明咱跟讲义保持一致吧这是大家可以随意命名的那接下来是不是需要把这个方法呢顺手给它定义出来
[08:36] 那在定义这个方案的时候呢有一个注意事项大家需要注意的就是这个方案的参数那这个方案的参数是有规定的啊有什么规定呢大家注意一下你看它这里边是不是有一个叫block exception的这么一个什么呀参数那具体来说是这样子的啊大家注意听如果说你受保护的这个方法是无参的那么这个方法至少得有这么一个参数那如果你受保护的方法本身就一个参数那么
[09:06] 这个方法是需要有什么样有两个参数其中一个参数就第一个参数跟这儿是保持一致的然后再加上这么一个参数那如果说受保护的方法本身有两个参数一个A一个B那么这个地方也是首先有个A然后有个B参数然后再加上一个什么呀block一个Service总结一句话就是说呢这个方法的参数永远要比受保护的方法的参数要多这么一个参数这是需要大家注意的
[09:34] 那这里边呢我们刚才说了我们这是一个demo吧我们也不做任何事情我们就基本上就反过来这么一句话就是作为我们这个限流的这个什么呀后续处理啊后续动作这是第一步吧对吧我们通过一个注解啊去定义了这个什么呀资源啊以及明确了限流后的这个什么后续动作那接下来该干嘛接下来的话我们刚才也说了第二步是不是该定义这个什么呀规则啊
[10:07] 没有这个规则的话我们就无法实现这个什么呀限流我们刚才说了我们准备定义一个什么规则对就是一秒钟之内最多要用两次这个什么呀哈喽方法超过了我就要进行什么呀限流当然实际开发的时候这个两次有点少啊我们这毕竟是一个demo为了变异大家看到效果啊我就定义成两次那具体这个规则咋定义呢这个地方呢我们就需要用到Centino的API了我们看看讲意义
[10:38] 看这你看它是不是还是在这个Service这个类里对不对然后定义了一个方法方案名字随便起然后在这里边你看是不是写了几行代码那这块代码其实就是Centino的这个API通过它的API具体把这个限流规则给它对定义出来而且你还要注意这个细节这个方案上面我是不是加了一个注解叫post construct这个注解大家见过吗知道什么意思吗
[11:09] 大家知道这是一个方法对吧那这个方法里边代码我们要想运行常规情况下是不是得去人工去调用一下这个方法对不对这里边代码就执行但这个地方呢我们不准备这么做啊这个地方呢我就加了一个post construct这个注解那这个注解起什么作用呢注意听了啊将来我们starbase这个对象是不是由sprint框架去创建了他创建的时候是不是会调用他的构造方法当构造方法调完之后呢这个方法就会被自动干什么呀
[11:39] 运行这个就是post construct这个注解的作用注意听啊再给大家强调一下这个注解能保证这个方法会被自动干什么调用就是不需要我们人工去调用而且它是在什么时候调用的就是在当前这个对象的什么样构造方法调用完这个方法就会被自动调用不难接下来的话就把这个方法里边的这个代码呢我们编写一下我们就写到这儿了
[12:09] 这里边呢就是具体用Centino的API来定义线流规则具体怎么定义呢其实它这里边封装好的这个有类啊叫follow什么呀入啊直接new就行了这个follow就是什么呀流量的意思对吧这个iol1入就是什么意思规则嘛简明之一那么这个类啊或者这个对象是干嘛的呀它就是专门用来封装什么呀对线流
[12:44] 规则就是靠这个对象那具体怎么封装呢我们既然就是要调用它的什么呀对调用它的方法比如说啊我们要调用的第一个方法就叫set找一找对set resource这个发明啊建名之意是并来设置什么呀资源的名字你看你要定义这个什么呀限定规则你得知道啊或者你得告诉他你这个规则是针对哪个资源的
[13:16] 咱是不是针对这个资源就是这个方法那这个资源有名字吗有对吧我们刚才在介绍这个注解的时候我们说了这个就是value属性的值就是用来定义资源名的我们把它放到这就行那也就是说呢这个地方的值要跟这保持什么一致没错这是我们把什么资源名给设置好了然后呢我们需要这不对啊我们应该是r u l e对不对
[13:52] 我们接下来调用它的方法还需要设置啥呢咱一起看一看接下来需要设置一个set什么setgrid啊就是设置这个限流的模式限流的模式呃这个限流模式呢有好几种那么而且呢这个限量模式呢它已经封装到一个什么呀以及个类当中的啊现成的一个类我们直接从里边取它的常量值就行了这个类的名字叫iuleconsonant常量值对不对你点一下
[14:23] 你看这里边是不是有各种各样的封装好了这个什么呀限流模式有的同学说老师这我也看不懂啥意思啊没有关系我这里边呢有一个中文的注释啊在这大家可以看一下这就是这个这个什么呀这个类的圆嘛只不过我在这里边是不是给给加上这个什么呀对加上这个中文注释这里边就是他定义好的一堆限流模式那我们这给大家用的是这种QPS啊QPS
[14:56] QPS是啥意思咱们前面是不是提到过QPS就是根据什么呀是判断每秒钟的这个什么呀访问量的每秒钟的这个请求量我们是基于这种模式来进行什么呀限流的啊所以说我们应该取这个值Follow什么呀Grade QPS当然将来的话这个你在骑灯11开2时候呢不一定会用这个值你要看具体的业务需求那咱接下来的话这儿我们就要
[15:28] 点那个QPS了是哪个呀就是这个这是限量模式那限量模式设置好之后呢我们说了是不是要设置每秒钟我们说了每秒钟最多我们只允许调用几次这个哈罗方法刚才说两次是不是那么这个值怎么设置既然你需要调用一个方法叫set count见面之一吧对不对二你写个二就表示每秒钟最多可以调用这个哈罗方法几次对两次
[15:59] 你看这样子的话我们就把一个限流规则给它定义好定义好之后怎么让它起作用呢怎么起作用呢我们这需要这么做我需要定义一个集合啊list的集合这个集合的范型啊就是这个follow这个类型直接拗对吧那sending的这个框架它在设计的时候呢它是允许对一个资源定义多个什么呀规则的也就是说呢这个对象你可以拗多次
[16:35] 然后呢每个对象里边封中的规则都是可以不一样但是呢可以作用于同一个什么呀对同一个资源还比较灵活那我们这是不是定义了一个规则对吧定义完规则之后呢你需要把这个规则呢这个对象呢给它存到这个什么集合里那有的同学会说老师我就定义一个规则那也需要这个集合吗对不对我就只需要一个规则就行那也需要啊为啥需要呢因为我们最后一步我们这个代码一起你就明白了啊最后一步要干什么呀
[17:10] 就是加载这个什么呀对限流规则是其干什么呀对起用那怎么加载限流规则让它起作用呢那我们这呢有一个现成的一个类啊一个管理器类叫follow rule manager就是这个它呢有一个方法叫load什么呀就是这个方直接调用就行了啊
[17:47] 然后你看这里边他要的就是一个什么呀对他要的是一个集合不是一个什么呀否则入对象要的是一个集合所以说你即使定义的是一个规则你也得先把它干什么对存到集合里边然后呢把这个什么呀集合往这一放哎那我们刚才定义的这个限流规则就起作用了啊就被加载了就被起作用了所以说这就是第几步第二步啊定义限流规则
[18:16] 然后这就是我们刚才说的第几步啊对第一步定义资源然后呢这呢是为这个资源定义了这个什么呀新的规则那这两步搞完之后呢其实咱们这个Centino的入门案例呢咱就搞定了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 Sentinel 实现流量控制，包括创建项目、引入依赖、编写代码定义资源和配置限流规则。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 第 2 页“快速入门”，说明使用 Sentinel 实现流控的三个步骤：定义资源、定义规则、检验规则是否生效。列出 Sentinel 支持的主流框架：Web Servlet、Dubbo、Spring Boot / Spring Cloud、Spring WebFlux、gRPC。
画面 2: 在 IntelliJ IDEA 中展示 TestController.java 代码，包含 @RestController、@GetMapping、@Autowired 注解，以及一个返回 "hello" 的方法。
画面 3: 展示 PPT 第 3 页“2.1 入门案例”，内容为创建 Maven 工程和引入依赖的说明。同时展示 TestService.java 代码，其中包含 @SentinelResource 注解和 exceptionHandler 方法。
画面 4: 在 IntelliJ IDEA 中展示 TestService.java 代码，其中方法返回 "Hello Sentinel"。
画面 5: 在 IntelliJ IDEA 中展示 TestService.java 代码，光标位于方法名 "hello" 上。
画面 6: 展示 PPT 第 3 页“2.1 入门案例”的内容，同时在 IDEA 中展示 TestService.java 代码，光标位于 @PostConstruct 方法的开头。
画面 7: 展示 PPT 第 3 页“2.1 入门案例”，内容为创建 Maven 工程和引入依赖的说明。同时展示 TestService.java 代码，光标位于 @SentinelResource 注解的 value 属性。
画面 8: 展示 PPT 第 3 页“2.1 入门案例”，内容为创建 Maven 工程和引入依赖的说明。同时展示 TestService.java 代码，光标位于 @PostConstruct 方法的开头。
画面 9: 在 IntelliJ IDEA 中展示 TestService.java 代码，光标位于 @PostConstruct 方法的开头。
画面 10: 在 IntelliJ IDEA 中展示 TestService.java 代码，光标位于 @PostConstruct 方法的开头。
画面 11: 在 IntelliJ IDEA 中展示 TestService.java 代码，光标位于 @PostConstruct 方法的开头。
画面 12: 在 IntelliJ IDEA 中展示 TestService.java 代码，光标位于 @PostConstruct 方法的开头。
画面 13: 在 IntelliJ IDEA 中展示 TestService.java 代码，光标位于 @PostConstruct 方法的开头。
画面 14: 在 IntelliJ IDEA 中展示 TestService.java 代码，光标位于 @PostConstruct 方法的开头。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
控制台（Dashboard）基于 Spring Boot 开发，打包后可以直接运行，不需要额外的 Tomcat 等
应用容器。
2 快速入门
使用 Sentinel 来实现流控，主要分为几个步骤：
1. 定义资源，这里的资源可以是任何东西，例如某个服务，某个服务里的方法，甚至是一段代码。
2. 定义规则，指的是流量控制规则
3. 检验规则是否生效
先把可能需要保护的资源定义好，之后再配置规则。也可以理解为，只要有了资源，我们就可以在任何
时候灵活地定义各种流量控制规则。在编码的时候，只需要考虑这个代码是否需要保护，如果需要保护，
就将之定义为一个资源。
对于主流框架，Sentinel 都提供了适配，只需要按照适配中的说明配置，Sentinel 就会默认支持提供的
服务，方法等为资源。Sentinel 支持的主流框架适配列表如下：
• Web Servlet
• Dubbo
• Spring Boot / Spring Cloud
• Spring WebFlux
• gRPC
```

画面 2:
```
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TestController {
    @Autowired
    private TestService testService

    @GetMapping("hello")
    public String hello() { return testService.hello(); }
}
```

画面 3:
```
@SentinelResource(value = "hello",blockHandler = "exceptionHandler")
public String hello() {
    return "hello Sentinel";
}

public String exceptionHandler(BlockException ex){
    ex.printStackTrace();
    return "系统繁忙，请稍候";
}

@PostConstruct
public void initFlowRules(){
    List<FlowRule> rules=new ArrayList<>();
    //创建FlowRule对象封装限流规则
    FlowRule rule=new FlowRule();
    rule.setResource("hello");
    rule.setGrade(RuleConstant.FLOW_GRADE_QPS);
    rule.setCount(2);
    rules.add(rule);
}
```

画面 4:
```
public String hello() {
    return "Hello Sentinel";
}
```

画面 5:
```
public String hello() {
    return "Hello Sentinel";
}
```

画面 6:
```
@SentinelResource(value = "hello",blockHandler = "exceptionHandler")
public String hello() {
    return "hello Sentinel";
}

public String exceptionHandler(BlockException ex){
    ex.printStackTrace();
    return "系统繁忙，请稍候";
}

@PostConstruct
public void initFlowRules(){
    List<FlowRule> rules=new ArrayList<>();
    //创建FlowRule对象封装限流规则
    FlowRule rule=new FlowRule();
    rule.setResource("hello");
    rule.setGrade(RuleConstant.FLOW_GRADE_QPS);
    rule.setCount(2);
    rules.add(rule);
}
```

画面 7:
```
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.1.3.RELEASE</version>
</parent>

<groupId>com.itheima.msa.Sentinel</groupId>
<artifactId>Sentinel-demo</artifactId>
<version>0.0.1-SNAPSHOT</version>
<name>Sentinel-demo</name>

<properties>
    <java.version>1.8</java.version>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
</properties>
```

画面 8:
```
@SentinelResource(value = "hello",blockHandler = "exceptionHandler")
public String hello() {
    return "hello Sentinel";
}

public String exceptionHandler(BlockException ex){
    ex.printStackTrace();
    return "系统繁忙，请稍候";
}

@PostConstruct
public void initFlowRules(){
    List<FlowRule> rules=new ArrayList<>();
    //创建FlowRule对象封装限流规则
    FlowRule rule=new FlowRule();
    rule.setResource("hello");
    rule.setGrade(RuleConstant.FLOW_GRADE_QPS);
    rule.setCount(2);
    rules.add(rule);
}
```

画面 9:
```
@PostConstruct
public void initFlowRules() {
    List<FlowRule> rules=new ArrayList<>();
    //创建限流规则
    FlowRule rule=new FlowRule();
    rule.setResource("hello");
}
```

画面 10:
```
@PostConstruct
public void initFlowRules() {
    List<FlowRule> rules=new ArrayList<>();
    //创建限流规则
    FlowRule rule=new FlowRule();
    rule.setResource("hello");
}
```

画面 11:
```
@PostConstruct
public void initFlowRules() {
    List<FlowRule> rules=new ArrayList<>();
    //创建限流规则
    FlowRule rule=new FlowRule();
    rule.setResource("hello");
    rule.setGrade(RuleConstant.FLOW_GRADE_QPS);
}
```

画面 12:
```
@PostConstruct
public void initFlowRules() {
    List<FlowRule> rules=new ArrayList<>();
    //创建限流规则
    FlowRule rule=new FlowRule();
    rule.setResource("hello");
    rule.setGrade(RuleConstant.FLOW_GRADE_QPS);
    rule.setCount(2);
}
```

画面 13:
```
@PostConstruct
public void initFlowRules() {
    List<FlowRule> rules=new ArrayList<>();
    //创建限流规则
    FlowRule rule=new FlowRule();
    rule.setResource("hello");
    rule.setGrade(RuleConstant.FLOW_GRADE_QPS);
    rule.setCount(2);
}
```

画面 14:
```
@PostConstruct
public void initFlowRules() {
    List<FlowRule> rules=new ArrayList<>();
    //创建限流规则
    FlowRule rule=new FlowRule();
    rule.setResource("hello");
    rule.setGrade(RuleConstant.FLOW_GRADE_QPS);
    rule.setCount(2);
    rules.add(rule);
    //加载限流规则，作用于
    FlowRuleManager.loadRules(rules);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“2 快速入门”，内容包括三个步骤：定义资源、定义规则、检验规则是否生效。列出 Sentinel 支持的主流框架。
画面 7: PPT 标题为“2.1 入门案例”，内容为创建 Maven 工程和引入依赖的说明。
画面

