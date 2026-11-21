# 20.Sentinel动态规则

- 阶段：10.阶段十 万信金融项目
- 章节：08_万信金融-微服务高级部分/8-3 Sentinel的理解和使用
- 源文件：10.阶段十 万信金融项目\08_万信金融-微服务高级部分\8-3 Sentinel的理解和使用\20.Sentinel动态规则_【海量资源尽在 666java.com】.mp4
- 时长 6分37秒（音频 398s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 接下来呢我们给大家介绍一个Centino框架道中一个非常好用的一块内容叫动态规则那啥是动态规则呢咱先看看咱刚才写的这个什么呀入门案例里边的这个这块代码这块代码大家知道是不是通过它的API来设置这个什么呀限流规则大家想一下这种方式是可以我们刚才测试通过了对不对但是这种方式有一个很不好的地方就是它不灵活
[00:33] 是不是这些规则里边的这些什么呀值是不是相当于我是不是写死到这个加了代码里边明白什么意思吧还有一个就是这都需要我们这个什么呀人工的去进行修改那将来如果我这个规则经常需要变化那你是不是每次都得改这个什么呀加了代码这也很什么呀很麻烦对吧一个是什么呀一个是不灵活一个是什么呀很麻烦对吧这些值呢都写死到这个加了代码里边啊
[01:04] 这个对于我们家的成员我们能忍吗我们肯定不能忍是不是那怎么办呢我们就想到要干啥这个大家以前经常干你可以把这些值给它存到什么数据库里边可以吧将来我把这些值从数据库里边读取出来可以不然后你还可以把这些值作为配置给它存到什么Apollo上Apollo大家知道吧我们在万信金融P2P项目当中是不是就用到了Apollo你就可以把这些值给它配到什么
[01:32] Apollo上将来呢我从Apollo里边是不是就可以获取到这些值那你看我们这么子做总比把这些值写死到这个什么呀加大门里边要灵活的多或者要干什么呀方便的多那你要想实现这种效果你就需要用到Centino当中的这个什么呀对动态规则所以你看他说了前面你不管是用加大门还是用那个控制台对吧你在设置这个限量规则的时候都属于手动的方式
[02:02] 不灵活也很干什么呀麻烦我们让他说代码都写死了我一般呢你就是测试也是使用就行了那在企业真实的生产环境当中呢我们一般都要采用这个什么呀对动态规则什么叫动态规则呢我们刚才说了就是把规则当中所涉及到什么参数啊以他的值啊给他存到什么存到文件里边存到数据库里边存到这个什么呀配置中心当中将来呢我们从这里边是不是动态的获取那些数据就OK了这样子呢非常的灵活非常的什么呀
[02:32] 方便啊这就叫动态规则整体呢它这儿有一个架构我们看一看呃它的建议是这样子的啊你可以通过这个什么dashboard就是这个什么呀图形化的这个控制台我们刚才演示了你在这儿是不是可以新建这个规则编辑这个规则对吧当你点击这个什么呀保存的时候对不对或者点击这个新增的时候呢它建议这么做啊你把这里边你设置好的这个规则这些数据啊给它干什么呀给它保存到比如说Apollo当中
[03:04] 可以吧你给他保存到Apollo当中然后呢然后呢这些规则毕竟是要在我们的微服务就是我们的应用程序当中要用嘛那我怎么用呢那你就从Apollo当中把这些数据干干什么呀读取出来就行了呗是不是读取出来读取出来之后呢哎我们最终还是给谁给这个入什么呀manager就这个对象呢是不是还是给他然后这个规则一样能干什么呀对起作用啊所以说主要的区别就是
[03:33] 这些规则你不要给它写死到加代码里边不要给它写死到本地而是要把它干什么呀保存到文件里边保存到数据库里边或者保存到什么配置中心都是可以的我们推荐这种做法这就叫什么呀对动态规则那我们这还给大家举了一个例子就是以Apollo为例Apollo我们说了它是在我们项目当中经常用到的一个什么呀配置中心我们的P2P项目
[04:02] 所有的配置不能说所有就是大部分的配置是不是都在Apollo配置中心当中存在的对不对那现在我们也可以这么做呀那具体啊就是Centino如何跟Apollo进行这个什么呀适配是不是那具体我们大概需要做两件事啊第一件事呢就是你需要引入一个依赖就是把Apollo作为什么呀作为动态规则的这个一个什么呀数据源对吧存储的一个数据源
[04:32] 你需要把这个依赖呢给它倒进来然后呢接下来呢我们还是需要写一些什么呀对加二代码但是这块加二代码它的主要作用呢就是从什么呀对从Apollo当中你存进去的那些规则那些参数那些值给它干什么呀读取出来怎么读取呢这里边呢就需要你设置什么呀这个代码你先不用管啊我们一会会编写你大概知道它的原理就行了
[05:03] 你大概需要知道什么呀name space这个大家应该有印象吧我们不管什么配置啊不管什么配置是不是都是存在某一个什么呀对name space里面你首先要告诉他哎你的这个什么呀规则配置在哪个name space里面把这个名字告诉他然后呢你还要告诉他这个什么呀对告诉他这个k其实就是这个等号钱这个东西啊那咱这个规则也是相当于是这个什么建制段啊你看看比如这个resource他就是
[05:34] key这个hello就是什么呀值对不对这count就是key这个2就是什么呀值那你接下来啊你如果想想取hello想取2你是不是要根据这个key这就可以得到这个值了对不对所以说当将来你在写这块加拿大码的时候呢你主要是要告诉他什么呀namespace的名字还有这个什么呀key啊规则的这个key那么通过这一块加拿大码我们就能从Apollo当中干什么呀对把我们的这个什么呀
[06:03] 对把我们定义好的这个线流规则给获取到啊这就是什么呀对Sentino当中的动态规则啊这就是什么呀啊对动态规则如何跟Apollo干什么呀对做适配那这块例子呢我们不单独给大家编写了一会儿呢我们在万信金融P2P当中我们要实现网关线流啊在实现这个网关线流的时候呢我们就会用到这个什么呀
[06:31] 动态规则所以说到那时候呢大家再看这块具体是怎么实现的

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中通过 Sentinel 控制台和 Apollo 配置中心动态管理限流规则。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 IntelliJ IDEA 中，展示 TestService.java 文件中 initFlowRules() 方法的代码，用于定义一个 QPS 为 2 的限流规则，资源名为 "hello"。代码中注释说明“测试限流规则”和“加载限流规则，使其生效”。
画面 2: 同画面 1，但光标位置在 rule.setCount(2); 行，强调设置 QPS 为 2。
画面 3: 同画面 1，光标在 rule.setResource("hello"); 行，强调资源名。
画面 4: 同画面 1，光标在 rule.setResource("hello"); 行，强调资源名。
画面 5: 同画面 1，光标在 rule.setResource("hello"); 行，强调资源名。
画面 6: 展示 PPT 页面，标题为“2.3.3 动态规则”，内容说明通过 Dashboard 手动设置规则不够灵活，官方推荐通过 DataSource 接口实现动态规则管理。
画面 7: 展示 Sentinel 控制台界面，显示“SentinelDemo”应用的限流规则，资源名为 "hello"，QPS 为 2，效果为“单机”，并有“编辑”和“删除”按钮。
画面 8: 展示多窗口界面，包括 IntelliJ IDEA、Sentinel 控制台、Apollo 配置中心和 PowerShell，说明动态规则的实现涉及多个组件。
画面 9: 同画面 1，光标在 rule.setCount(2); 行，强调设置 QPS 为 2。
画面 10: 展示 Sentinel 控制台的“新增流控规则”弹窗，包含“资源名”、“针对来源”、“阈值类型”、“阈值”等字段。
画面 11: 展示 PPT 页面，标题为“达生演示如何使用 Apollo 配置中心”，内容说明 Sentinel 可以通过 Apollo 作为规则配置数据源，并展示相关依赖和代码示例。
画面 12: 展示 Apollo 配置中心的“application”配置页面，其中配置了多个路由规则，如 zull.routes.account-Service.path = /account/**。
画面 13: 同画面 11，展示 PPT 页面，内容说明 Sentinel 与 Apollo 的集成方式。
画面 14: 同画面 13，展示 PPT 页面，内容说明 Sentinel 与 Apollo 的集成方式。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
List<FlowRule> rules=new ArrayList<>();
//测试限流规则
FlowRule rule=new FlowRule();
rule.setResource("hello");
rule.setGrade(RuleConstant.FLOW_GRADE_QPS);
rule.setCount(2);
rules.add(rule);
//加载限流规则，使其生效
FlowRuleManager.loadRules(rules);
```

画面 6:
```text
2.3.3 动态规则

前面不管是通过java代码还是通过Dashboard的方式去设置限流规则，都属于手动方式，不够灵活。这种方式一般仅用于测试和演示，生产环境上一般通过动态规则的方式来动态管理限流规则。也就是说，很多时候限流规则会被存储在文件、数据库或者配置中心当中。Sentinel的DataSource接口提供了对接任意配置源的能力。

官方推荐通过控制台设置规则后将规则推送到统一的规则中心，客户端实现 ReadableDataSource 接口监听规则中心实时获取变更，流程如下：
```

画面 11:
```xml
<dependency>
    <groupId>com.alibaba.csp</groupId>
    <artifactId>Sentinel-datasource-apollo</artifactId>
    <version>1.6.2</version>
</dependency>
```

```java
// namespaceName 对应Apollo的命名空间名称
// ruleKey 对应规则存储的key
// defaultRules 对应连接不上Apollo时的默认规则
ReadableDataSource<String, List<FlowRule>> flowRuledataSource = new ApolloDataSource<>(namespaceName, ruleKey, defaultRules, source -> {
    return JSON.parseObject(source, new TypeReference<List<FlowRule>>() {});
});
FlowRuleManager.registerProperty(flowRuledataSource.getProperty());
```

画面 12:
```properties
zull.routes.account-Service.stripPrefix = false
zull.routes.account-Service.path = /account/**
zull.routes.consumer-Service.stripPrefix = false
zull.routes.consumer-Service.path = /consumer/**
zull.routes.transaction-Service.stripPrefix = false
zull.routes.transaction-Service.path = /transaction/**
zull.routes.repayment-Service.stripPrefix = false
zull.routes.repayment-Service.path = /repayment/**
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 6:
标题：2.3.3 动态规则
内容：说明动态规则的必要性，推荐通过 DataSource 接口实现动态规则管理。

画面 11:
标题：达生演示如何使用 Apollo 配置中心
内容：说明 Sentinel 与 Apollo 的集成方式，展示依赖和代码示例。

画面 12:
标题：Apollo 配置中心
内容：展示路由规则配置，如 zull.routes.account-Service.path = /account/**。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

