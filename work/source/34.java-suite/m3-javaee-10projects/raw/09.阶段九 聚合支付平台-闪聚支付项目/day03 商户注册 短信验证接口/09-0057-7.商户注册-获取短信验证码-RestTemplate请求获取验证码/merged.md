# 7.商户注册-获取短信验证码-RestTemplate请求获取验证码

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day03 商户注册 短信验证接口
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day03 商户注册 短信验证接口\7.商户注册-获取短信验证码-RestTemplate请求获取验证码【海量资源尽在 666java.com】.mp4
- 时长 12分34秒（音频 754s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,下面呢我们来使用REST Template来向验证码服务呢发起请求来发送验证码刚才我们已经完成了REST Template一个入门程序那下面呢我们基于前面我们做的这个入门程序啊我们来看一下这个程序怎么写那么我们准备还是在我们的这个测试的类当中啊来再写一个方法这个方法呢我们准备是向验证码服务发起请求
[00:29] 来干嘛呀来获取验证码那么这个获取验证码的这个接口啊当初我们已经测试了对吧这个接口是不是就是它我们准备向它来发送那向它发送的话注意我先把这个方法写出来啊注意大家思考一下怎么来做比如说我们准备发送获取这个验证码好那我们是不是要用rest template呀
[01:01] 现在我们要怎么发呀这个接口当初大家还有印象吗它是Post的请求对吧Post的请求然后呢来请求三个参数啊一个参数是有效期还有Name另外还有一个JSON数据看见吗另外关键它的这个JSON数据你看它是作为Body内容来传到我们的接口中
[01:26] 所以这里边要注意Post的请求不是原来的get的请求所以这里边你不能用get for entity对那用哪个方法我们就用这个exchange在exchange这里边我们就可以在外边来指定我们的URL就是上面的URL这URL是不是就是通过我们的Swagger这个页面能拿到这个接口那么还有
[01:55] 那么我们指定完URL之后呢你就把URL放进去你现在要做的是POST的请求所以大家看它的第二个参数就是什么呀叫http method post然后第三个参数是什么呢第三个参数大家看它是叫rest应该是request entity是不是就是请求内容啊
[02:22] 那么这个请求内容我先写空然后后面还有一个叫响应的数据假如说响应我们最终拿到是map有时候老师为啥是map呀因为最终啊我们因为你也知道这个网页的信息你看我们现在不是拿网页的信息拿的是json这个json数据完全可以转成map对不对对所以呢我们把它转成map那这个请求的内容呢
[02:52] 请求的内容大家可以看到它是一个叫http entity这个类型看见吗所以其实它是它是可以定义成一个http entity这个类型的数据所以这里边要注意我这里边先暂时写个空不让它报错这里边我们就可以来这叫请求的信息请求的信息刚才你也看到了是http entity对吧那http entity怎么构造你打开
[03:22] 这边有很多的构造方法你可以传一个body你也可以传body header那么我们现在看到body是一个json对吧header呢因为你是body要传json数据header里头你是不是得指定叫做content type是json的所以这里边我们需要用到既有body又有header的这个构造
[03:52] 方法所以你这里边要传入一个是body一个是什么header好那么body header我们在外边定义吧一个是请求体一个是请求头对吧那请求体刚才你们说了吗它就是bodybody但是body的类型是啥呢大家看它可以指定一个范形但是你看header它是不是有一个叫multi-value map这么一个类型
[04:22] 但这个类型你看它的副类是不是map它的副类是map所以其实body和header都可以指定map所以这里边我们就可以用什么呀map来作为body看好那有的老师map是key value那这个body你要指定它的key value分别是啥呢它的key是啥你要知道body里边传的数据是什么
[04:53] body里边传的是不是一个mobile所以它的key就是mobile那它的value呢value就是一个手机号随便说对这就是body我们就构造好了那么body构造好了之后还有一个是不是就是header对header你也可以用map但是这里边有一个现成的叫做http header这个类所以你就可以直接用它那么它怎么构造呢
[05:22] 其实它的构造方法你看它也有很多的这种构造这个参数啊那这里边呢我们就可以看好啊有一个叫method我们还是看一下它的原码啊点开一个是空的是吧一个是那我是不是可以在这指定一下啊你看它有一个叫content typecontent type里边是不是有一叫medial type
[05:56] 我们是不是就可以指定你看这是不是就相当于指定它的什么刚才你看到接口当中是不是就是一个叫content type等于application怎么样-json就是它好那么现在header我也弄好了这时候请求体请求头都有了那么http entity咱们是不是就可以填进去了
[06:22] 这样的话我们是不是又可以请求就相当于向URL发起请求然后得到数据得到数据这个得到的数据那么我们是不是可以输出一下呀行不行那么这个输出的话你看这个log是不是就用了我们上面的这个注解这是longbook当初我们是不是使用了这么一个组件那只要你加一个这个注解sl4g我们就可以用
[06:50] 它给我们提供的快速输出日志的方法log.info然后这里边呢我们可以输我们说请求看好啊请求验证马夫得到响应得到响应得到什么响应那我这里边就可以来写参数啊得到它是这意思吧这个大口号就对应这个参数懂吧如果说你说我后边还有一个大口号呢这里边你可以逗号再继续写数据
[07:19] 懂吧好那这里边呢我们只有一个大口号相当于我们这里边再写一个参数对应它就可以好那么这个我们说它是一个什么类型我们是不是可以把它嗯把它转一下行不行啊这样我们把它这样是不是转成Jason输出因为它响应的结果是不是就是Jason的对不对所以我们可以把这个数据转成Jason行不行可以吧然后呢那这里边你仍然可以再继续拿
[07:50] 你看它是不是可以拿到body看到了吧这是不是就是我们说的result不是result我们就叫bodymap好那么我们现在就写到这儿这个代码我们现在运行一下试试看看能不能拿到数据这个请求就是我们用resttemplate向验证码服务来发起发送验证码的请求来看一下它能不能正常的是不是可以来看一下数据对不对
[08:21] 好正常看见吧正常然后呢这个数据有你看他的body拿到的body里边有啥有正常还有resultresult里边你看有一个keyresult有时候老师这是啥意思呀注意你拿到的这个数据啊就是你原来用Swagger测试拿到这个响应就是这阶层了只不过这阶层呢被你封装成什么呀map懂吧所以大家来看
[08:52] 他所输出的这个日志其实各位我们就可以看到你看他是不是就输出出来了这是不是我们打印的这个请求响应验证码服务得到响应是不是这个日志好那现在呢你说各位我问大家个问题啊我想把这里头的东西解析出来这么一个key我怎么解析啊有时候老是为啥解析key啊
[09:19] 因为我们当初说我们要校验验证码你是不是需要这个依据所以你就要把这个key给解析出来那咋弄看好这个body map各位我再运行一下你再看仔细观察你要知道现在这个响应的结果其实就是这个json数据了你现在要做的事是什么要把这个key给它解析出来看怎么解析看好
[09:46] 这时候我相信大家都应该比较清楚了看好bodymap当中有一个code msg result是不是就正好对应于code msg和result看见吗所以我们要做些什么事啊你要从bodymap当中我们要拿干嘛拿result就是拿我们说的这个它拿这个result
[10:12] 它也是一个json数据所以它也可以转成什么map对不对所以也可以转成map那你把它强转好这就是一个什么result那么拿到了这个result各位我们是不是再可以继续的来拿这时候它要拿的话它就直接拿什么呀result里边这端是不是也是一个map就可以拿key了
[10:39] 所以这个时候就是result再get看好key这就拿到我们想要的什么那一串key了对吧有时候老师是这么动吗来我们拭目以待看好我在这打一个断点行不行再次运行走这时候呢我们就可以来看一下你是得到信息然后干嘛解析数据
[11:09] 就这样最终能拿到通过加拉程序来请求验证码来拿到我们要的这个什么验证码所对应的key好来看一下你看是不是拿到了对所以以上呢就是我们通过rest template来请求验证码服务来发送验证码然后最终拿到验证码的这个对应的key
[11:35] 那就是说老师发送验证码那你这个控制台打印验证码了吗你看打印了吗你看我清一下行不行我清一下清完了之后啊注意看啊我再执行一下程序我执行一下程序是不是就相当于发送验证码了这个程序一执行发送验证码然后呢在这个验证码的这个控制台你看它就准备打印向哪个手机号发送验证码看见吗对这就是我们使用rest template
[12:06] 来模拟客户端来发送验证码服务最终得到验证码那么这个技术非常重要这个技术将来就是在我们整个系统交互流程这里就是我们刚才测试的程序将来我们就会在这里头去用来最终使用加码程序来向验证码服务发送请求获取验证码好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Spring 的 RestTemplate 调用远程 HTTP 服务以获取验证码，并演示了相关代码实现和调试过程。

2) 按时间顺序列出每张画面的要点：
画面1：介绍 RestTemplate 技术预研，说明使用 OkHttp 作为 HTTP 客户端，并给出引入依赖的 Maven 配置。
画面2：在 Swagger UI 中配置生成验证码的 POST 请求，参数包括 effectiveTime 和 name。
画面3：在 IDE 中展示 RestTemplateTest.java 代码，调用生成验证码的接口。
画面4：在 IDE 中展示 RestTemplateTest.java 代码，准备调试。
画面5：在 IDE 中展示 RestTemplateTest.java 代码，使用 HttpEntity 构建请求体。
画面6：在 IDE 中展示 HttpHeaders 类的源码，查看其构造函数和 setAccept 方法。
画面7：在 Swagger UI 中展示请求的 curl 命令和响应。
画面8：在 IDE 中展示 RestTemplateTest.java 代码，使用 HttpEntity 构建请求体。
画面9：在 IDE 中展示 RestTemplateTest.java 代码，调试时查看 ResponseEntity 的 bodyMap。
画面10：在 IDE 中展示测试通过的日志。
画面11：在 IDE 中展示 RestTemplateTest.java 代码，调试时查看 Map 的方法。
画面12：在 IDE 中展示 RestTemplateTest.java 代码，调试时查看 ResponseEntity 的 bodyMap。
画面13：在 IDE 中展示 Sailing 应用启动日志。
画面14：展示系统交互流程图，说明商户注册流程。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```xml
<!-- okhttp3依赖 -->
<dependency>
    <groupId>com.squareup.okhttp3</groupId>
    <artifactId>okhttp3</artifactId>
</dependency>
```

画面3：
```java
String url = "http://www.baidu.com/";
// (1)生成验证码，作为http请求
// http://localhost:56085/sailing/generate/effectiveTime=600&name=sms
String url = "http://localhost:56085/sailing/generate/effectiveTime=600&name=sms";
restTemplate.exchange(url, HttpMethod.GET, null, String.class);
```

画面5：
```java
//请求体
//请求头，传入body，header
HttpEntity httpEntity = new HttpEntity(body, headers);
ResponseEntity<Map> exchange = restTemplate.exchange(url, HttpMethod.POST, httpEntity, Map.class);
```

画面6：
```java
public HttpHeaders() {
    this.collection = new LinkedMultiValueMap<>(initialCapacity, Locale.ENGLISH);
}

public HttpHeaders(MultiValueMap<String, String> headers) {
    Assert.notNull(headers, "MultiValueMap must not be null");
    this.headers = headers;
}
```

画面8：
```java
//请求体
//请求头，传入body，header
HttpEntity httpEntity = new HttpEntity(body, httpHeaders);
ResponseEntity<Map> exchange = restTemplate.exchange(url, HttpMethod.POST, httpEntity, Map.class);
```

画面9：
```java
Map bodyMap = exchange.getBody();
System.out.println(bodyMap);
```

画面11：
```java
Map result = (Map) bodyMap.get("result");
String key = (String) result.get("key");
System.out.println(key);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14：
架构图标题：2.1.1 系统交互流程
流程图结构：
- 淘宝商户APP → 商户平台应用 → 商户服务 → SaaS平台 → 验证码服务
- 验证码服务 → 发送于手机端
- 商户平台应用 → 新增商户 → 商户服务 → SaaS平台 → 验证码服务
- 验证码服务 → 发送于手机端
- 商户平台应用 → 新增商户 → 商户服务 → SaaS平台 → 验证码服务
- 验证码服务 → 发送于手机端

5) 不要评价画面美观，不要输出与课程无关的内容。

