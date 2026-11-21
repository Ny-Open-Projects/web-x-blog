# 6.商户注册-获取短信验证码-RestTemplate入门

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day03 商户注册 短信验证接口
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day03 商户注册 短信验证接口\6.商户注册-获取短信验证码-RestTemplate入门【海量资源尽在 666java.com】.mp4
- 时长 18分34秒（音频 1114s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们来实现获取验证码在整个交互流程图上边我们可以看到首先用户输入手机号点击获取验证码然后请求到商户平台应用服务商户平台应用服务呢再次请求到验证码服务然后验证码服务发送手机验证码所以其实应该这个触发发送验证码的
[00:28] 动作关键在于商户平台应用这个服务因为这个服务要直接和验证码服务进行交互也就是要调用它发送验证码的这个接口然后来完成验证码的发送好那么注意这个调用呢不是刚才我们去测试通过Swagger的这种测试方式来调用它的发送验证码的接口而是通过怎么样
[00:57] 通过加码程序就是在商户平台应用服务里边我们写一个加码程序来调用这个什么验证码服务来发送验证码所以这里边我们就需要来研究一下加码程序怎么来远程调用验证码服务来发送验证码
[01:18] 其实这里边的关键点在什么呢关键点在于我们要知道我们用什么样的技术来请求验证码服务给我们暴露的http接口这是最关键的对不对那你说我们打开浏览器输入网址就相当于是不是也可以请求这个http的接口啊因为浏览器是个客户端是吧浏览器支持http接口的请求
[01:45] 那我们通过Swagger这是不是也可以请求验证码服务的这个http接口对都可以但是现在我们需要用加拉程序来模拟类似于浏览器和Swagger它这个客户端的方式来请求http服务的接口这时候怎么办呢这时候我们就要用到一个什么http的客户端工具
[02:10] 来完成这个请求也就是我们的Java程序就是http的什么客户端他要请求我们刚才部署的验证码服务的服务端他们之间走什么呀对他们之间走的就是http好那这时候我们说那怎么实现呢
[02:36] 我们其实可以看一下Spring给我们提供了一个叫REST Template的这么一个专门用来访问http rest-foo接口的一个客户端工具那么从字面意义上我们可以知道它是一个什么它是一个模板对吧对REST接口访问的模板那么所谓模板呢其实应该说它真正它所使用的客户端工具是什么呀默认我们
[03:04] 他可以使用JDK给我们提供的http的连接的方式这个我相信学过Java基础的同学应该见过就是JDK给我们提供的一个http的一个什么对连接的一个客户端的一个类库他可以来模拟客户端请求http服务当然我们也可以使用第三方给我们提供的很多的这种工具
[03:31] 比如说有H Apache给我们提供的还有90还有OKHTTP等等所以这里边我们综合比较我们发现OKHTTP的这个HTTP的客户端的内库它的性能够一些所以我们本项目会使用OKHTTP客户端工具来请求HTTP的服务端也就是
[03:58] 接下来我们要实现的请求验证码服务来发送验证码好注意这里边我们脑子里边要明白一个事就是原来我们用浏览器用Swagger它相当于是客户端要请求http服务就是我们现在正在跑着的这个验证码服务是不是啊
[04:20] 现在我们要用加码程序来请求这个服务那么刚才我们分析加码程序我们要使用Spring给我们提供的REST Template它是一个模板但它会用第三方的HTTP客户端工具那么我们最终选择OKHTTP好所以现在我们要用REST Template以及OKHTTP我们就需要把OKHTTP的依赖包加到我们的工程中
[04:48] REST Template是Spring给我们已经提供的因为本项目的这个框架就是用的Spring框架所以我们不用加REST Template的依赖了我们只需要加OKHTTP即可好那现在呢我们说最终啊我们会让商户平台应用来请求这个验证码服务所以呢所以我们把这个依赖包呀我们把它加到我们的商户平台应用的工程中好那现在呢我们就
[05:19] 在哪里加在这加吧这是不是就是我们的OKHTTP的这个包呀那么现在我们加上去了之后呢接下来我们要做的事是什么呢我们就可以写程序了就可以来测试一下REST Template怎么样来远程请求HTTP服务好那现在呢我们就可以把它来注意啊刚才我们把它加了这个依赖啊在复工程当中我们要指定它的版本
[05:49] 就是负的怎么样这个POM文件看见吧因为我们学过MAYWAY嘛我们说POM文件负工程的POM文件这里边主要是要指定一些版本的依赖是不是啊你看这里边已经有了OKHTTP是用的3.9.1好那下面呢我们要用这个OKHTTP我们把依赖已经加进去了
[06:17] 那么这个rest template的模板它就可以去用了但是它怎么用rest template的这个模板最终我们使用spring我们会给它定义一个bin这个bin我们让它指定使用okhttp老师这bin咋定义现在我们用的是Spring Boot开发对不对所以Spring Boot我们去定义bin的方式就跟我们之前的channel方式不一样了现在我们其实就可以通过注解的方式来定义一个bin
[06:47] 现在这个死亡步骤的启动类大家知道最初是不是会先执行它呀那我们完全可以在这个启动类上面我们加一个并标签并注解然后呢这里边我们就可以让它来定义一个rest template这个rest template注意主要的是什么呢主要的是这个方法的什么内容和返回值也就是这里边我要让它返回一个rest template看见吗对
[07:18] 它就OK了这个bin就成了对但是有人说老师你不是说要用OKHTTP吗对所以其实这里边呢我们要指定它的一个构造参数注意这里边有一个叫clientHTTP request factory看见吗它是一个接口啊其实它有很多实现刚才我们引入的这个OKHTTP就是它的一个实现所以我们在定义这个resttemplate这个bin的时候我们要把这个什么
[07:47] OKHTTP的这个什么Factory这个工厂bin然后把它促使化一下然后呢通过构造方法参数传给REST Template这样的话这个REST Template呢它就知道哎将来它会使用这个什么OKHTTP来作为客户端请求服务端的一个类库来使用嗯好那现在呢我们其实就把这个bin给定义好了定义好了之后呢现在呢我们就可以来测试了
[08:16] 那怎么测试呢现在我们要测试啥呢你要注意我们要测试啥我们是不是就要测试resttemplate的使用那使用它干啥对你脑子要清楚因为我们最终的目的是不是要通过加拉程序向验证码服务发起请求发送验证码这个过程很重要的是加拉程序如何作为http的客户端向http服务端发起请求因为我们刚才选择的是什么呀是不是就是resttemplate它
[08:45] 那现在我们就要用resttemplate作为http客户端向服务端发起请求那怎么做呀各位注意看啊我现在要先建一个测试的类我在建测试类的时候你脑子边去思考一下思考啥思考我现在要做啥事要怎么测对我要测resttemplate它要作为http客户端向http服务端发请求那我这个怎么测啊怎么测
[09:14] 因为它是个内库嘛它肯定提供了很多API是不是啊对所以注意这时候呢注意看啊我在test的下边我建一个包注意这个包的路径要和我们Spring Boot的这个主工程的这个包的路径保持一致啊注意啊都是com.sangyupay.marchandcom.sangyupay.marchand然后下边我们建一个测试类注意看啊现在我加一些注解然后呢Spring Boot的test加上去然后呢还有一个
[09:44] 这个run with spring runner好然后呢为了打日志方便我们原来是不是引入了一个叫longbook我们就可以也用longbook的一个日志的将来直接方便的输出日志啊回头我们用它的时候大家就知道了现在我们先把这个注解给它写上然后接下来我们要测试什么呀测试使用rest template作为http的什么
[10:13] 客户端然后的向http服务端发起请求各位我说的这个够明确了吧对我要测试这个事那像哪个服务端发起请求呢对吧像哪个服务端发起请求呀那其实各位我们说服务端很多呀我们的验证码服务是不是就是一个服务端那我问你我们的这个黑马成学的官方网站是不是服务端是吧
[10:43] 百度是不是服务端是吧所以我们就可以干嘛呀对我们就可以像任何一个网站我们作为客户端向他发起请求发起请求来请求他的网页行不行可以原来我们是通过浏览器来浏览百度网页现在我们通过加挖程序就可以来通过加挖程序来模拟浏览器作为客户端来请求百度网站看好
[11:09] 这里边我们先把我们说的rest template给它注进来因为你现在是不是要用rest template所以你要把它注进来注进来之后怎么弄注意看现在我要来发起请求怎么发请求现在我要发起get请求你就这里边你看它有很多的API你看它有一个叫get for entity然后这里边我们就可以指定它的URL
[11:38] 那你说我要向服务http服务端地址比如说我们向百度这个网站发请求那么你就指定他的url行不行然后呢指定url那你说我向发请求他的这个参数是啥呀响应是吧他响应响应啥呀响应一个网页是吧响应一个网页的话你是不是可以响应让他响应成四五串行不行可以这就ok了看见吗
[12:08] 这就算发请求了对这就是向什么URL发送http请求得到响应结果那得到响应结果怎么解析呢这里边可以get body各位我就拿到了拿到了之后我就可以打印对所以现在我们做的是什么呀这一段程序就相当于浏览器远程来请求百度网站拿到百度的地址它的网页内容好现在走
[12:39] 注意看啊那这个我要一执行程序的话就相当于对远程发起了一个http请求哎然后呢请求百度网址然后拿到网页内容看好那最终呢他这这个网页内容呢会打印到我的控制台哎我们来看一下能不能输出出来啊因为这个过程呢他其实相当于还是要启动我们整个sprint boot的应用好注意看好像都ok了哎这个是不是就是我们说百度的网页的html内容啊大家看到了吗
[13:12] 对不对这就已经拿到了不过你看它有点乱码你看见吗但是内容各位它的确是把百度网页的内容拿到了对有人老是不相信不相信各位干这就是它的网站内容对吧但是是乱码乱码我们解决一下就好了那乱码是什么原因导致的注意看我的讲义就是rest template它默认因为我们最终拿到
[13:40] 的数据结果是封装成String类型对吧而这个String类型在REST Template里边呢它默认使用ISO8859-1字符集如果我们把它改成UTF-8就可以了那怎么改呢这个REST Template呀它呢它有很多的这个String它的消息转换器也就是说呀它最终把数据转换成String的时候呢它会通过消息转换器
[14:08] 来进行转换那这时候我们通过来指定转换季的制服级为UTF-8我们是不是就把ISSO8859-1改成了UTF-8对所以这个时候呢我们就可以怎么弄啊看好啊很有意思我们就可以这么来做在我们当初声明REST的template这个bin的地方注意看啊对我们这么玩我们原来是不是申请了声明了一个这样的一个bin呢return
[14:42] 这是原来的代码没错吧然后现在呢我们这里边要干嘛要得到它的消息转换器有人说消息转换器到底干啥呢就是得到请求响应的结果呢把它封装成String类型需要通过消息转换器那么怎么拿到它的消息转换器呢你可以get一下这里边有个叫Message Converter
[15:07] 看见吗这就拿到了消息转换器但消息转换器它不止一个我告诉你它有很多看见吗它有很多对那你说我想知道它有几个那我怎么确定呢看好啊怎么确定呢你再执行一下这个测试程序因为一执行测试程序这个程序呢它就会重新启动然后呢这个bin呢就又会实力化实力化到这的时候我打一个断裂大家可以看到这个list里面你看它的内容你就知道了看好啊拿到了吧拿到了之后呢你看
[15:39] 它这个消息转换器里面你看它有很多七个是吧其中第二个就是下标为一的第二个它就是StreamHttpMessageCommander就是这个Stream类型的消息转换器为啥要用Stream类型的消息转换器呢因为你刚才在测试的时候你是不是把数据转换成Stream数据类型看见吗所以你要怎么弄对你要这么做你要set
[16:05] 你要把这个Stream类型的消息转换器重新给它再声明一下那怎么声明一下呢对我就重新再给它构造一下行不行可以吧因为刚才你也看了这个下标是不是一个Stream类型的消息转换器对我们在声明的时候你要指定什么它的字符即为UTF-8注意看这就是指定
[16:32] 这个String类型的消息转换器的字符集为UTF-8这就OK了嗯好那么你执行完了之后呢我们就把这个REST Template返回就可以了来再次看一下看好这时候我再来启动这个测试程序那么一起动测试程序呢这个测试程序呢它就开始向百度发起请求然后呢请求拿到内容之后经过消息转换器
[17:02] 然后呢转成这个死证类型的数据看好那这时候你会发现结果拿到了吧拿到复制出来各位你来看这是不是就是他的网页的内容对其实到这儿呢你应该大概知道了这个rest template其实就是一个http的客户端它呢就相当于浏览器对吧然后来请求远程的http服务端来获取数据各位
[17:33] 爬虫大家应该听说过吧对吧也就是说啥意思就是百度它有很多的蜘蛛爬虫来爬取各个网站的数据其实就是用的这种技术就是相当于模拟http客户端来抓取网页的内容大家理解了吗对好以上就是我们对rest template简单的进行了一个测试你要知道rest template是死不用提供的一个什么
[18:03] 一个模板工具库它可以要使用第三方的一些http客户端类库这里面我们用okhttp来作为rest template的一个类库所以你要把它的依赖加进去那么我们在使用rest template上你要加它的什么它的bin的定义然后调用它的API方法就可以发起http请求好rest template的一个简单入门
[18:33] 我们就讲到这儿

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 RestTemplate 调用 HTTP 接口获取验证码，并解决因字符编码导致的中文乱码问题。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 页面，标题为“2.3 获取短信验证码”，子标题“2.3.1 RestTemplate技术预研”，介绍 RestTemplate 是 Spring 提供的用于访问 RESTful 服务的客户端。
画面 2: PPT 页面，展示在 `shaniupay-merchant-application` 工程中引入 OkHttp 依赖的 XML 配置片段，其中 `<artifactId>` 标签内容被遮挡。
画面 3: PPT 页面，展示在父工程中规范 OkHttp 版本的 XML 配置片段，其中 `<version>` 标签内容被遮挡。
画面 4: IDE 界面，显示项目结构，选中 `MerchantApplicationBootstrap.java` 文件，右侧编辑器显示依赖配置，其中 `okhttp` 依赖的版本号被高亮。
画面 5: IDE 界面，显示 `MerchantApplicationBootstrap.java` 文件，代码中定义了 `RestTemplate` Bean。
画面 6: IDE 界面，显示 `MerchantApplicationBootstrap.java` 文件，代码中将 `RestTemplate` 的构造函数改为 `new OkHttp3ClientHttpRequestFactory()`。
画面 7: IDE 界面，显示 `RestTemplateTest.java` 文件，代码中使用 `@RunWith(SpringRunner.class)` 注解。
画面 8: IDE 界面，显示 `RestTemplateTest.java` 文件，代码中定义了 `@Test` 方法 `getHtml()`，并展示 `RestTemplate` 的 `exchange` 方法签名。
画面 9: IDE 界面，显示 `RestTemplateTest.java` 文件，代码中设置 URL 为 `http://www.baidu.com/`，并调用 `getForObject` 方法获取响应体。
画面 10: IDE 界面，显示 `RestTemplateTest.java` 文件，控制台输出了百度首页的 HTML 内容。
画面 11: IDE 界面，显示 `MerchantApplicationBootstrap.java` 文件，代码中获取 `RestTemplate` 的消息转换器列表。
画面 12: PPT 页面，标题为“解决：配置 StringHttpMessageConverter 消息转换器，使用 utf-8 字符集”，并展示修改 `RestTemplate` 定义方法的代码。
画面 13: IDE 界面，显示 `RestTemplateTest.java` 文件，代码中 `getHtml()` 方法的 URL 被注释掉。
画面 14: PPT 页面，展示 `RestTemplateTest.java` 文件中 `getHtml()` 方法的代码，以及测试结果说明“网页内容中文乱码解决方案”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```xml
<dependency>
    <groupId>com.squareup.okhttp3</groupId>
    <artifactId>okhttp</artifactId>
</dependency>
```

画面 3:
```xml
<dependency>
    <groupId>com.squareup.okhttp3</groupId>
    <artifactId>okhttp</artifactId>
    <version>3.8.1</version>
</dependency>
```

画面 4:
```xml
<dependency>
    <groupId>com.squareup.okhttp3</groupId>
    <artifactId>okhttp</artifactId>
    <version>3.8.1</version>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
    <version>2.0.2.RELEASE</version>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter</artifactId>
    <version>2.0.2.RELEASE</version>
</dependency>
```

画面 5:
```java
@Bean
RestTemplate restTemplate() {
    return new RestTemplate();
}
```

画面 6:
```java
@Bean
RestTemplate restTemplate() {
    return new RestTemplate(new OkHttp3ClientHttpRequestFactory());
}
```

画面 7:
```java
package com.shaniupay.merchant;

import lombok.extern.slf4j.Slf4j;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@Slf4j
@RunWith(SpringRunner.class)
@SpringBootTest
public class RestTemplateTest {
}
```

画面 8:
```java
exchange(String url, HttpMethod method, HttpEntity<?> requestEntity, ParameterizedTypeReference<?> responseType)
```

画面 9:
```java
String url = "http://www.baidu.com/";
ResponseEntity<String> forEntity = restTemplate.getForObject(url, String.class);
String body = forEntity.getBody();
System.out.println(body);
```

画面 11:
```java
List<HttpMessageConverter<?>> messageConverters = restTemplate.getMessageConverters();
return restTemplate;
```

画面 12:
```java
@Bean
RestTemplate restTemplate() {
    RestTemplate restTemplate = new RestTemplate(new OkHttp3ClientHttpRequestFactory());
    //消息转换器列表
    List<HttpMessageConverter<?>> messageConverters = restTemplate.getMessageConverters();
    //配置消息转换器StringHttpMessageConverter，并设置utf-8
    messageConverters.set(1,
            new StringHttpMessageConverter(StandardCharsets.UTF_8));
    return restTemplate;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: 标题“2.3 获取短信验证码”，子标题“2.3.1 RestTemplate技术预研”。
画面 2: 标题“1、认识RestTemplate”，内容介绍 RestTemplate 是 Spring 提供的用于访问 RESTful 服务的客户端。
画面 3: 标题“在父工程已规范了okhttp的版本”，内容展示 XML 配置。
画面 12: 标题“解决：配置 StringHttpMessageConverter 消息转换器，使用 utf-8 字符集”，内容展示修改 `RestTemplate` 定义方法的代码。
画面 14: 标题“通过测试发现可以成功获取百度的网页内容”，内容说明“网页内容中文乱码解决方案”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）

