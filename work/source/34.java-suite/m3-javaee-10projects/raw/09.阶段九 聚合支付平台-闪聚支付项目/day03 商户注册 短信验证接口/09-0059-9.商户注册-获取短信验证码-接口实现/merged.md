# 9.商户注册-获取短信验证码-接口实现

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day03 商户注册 短信验证接口
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day03 商户注册 短信验证接口\9.商户注册-获取短信验证码-接口实现【海量资源尽在 666java.com】.mp4
- 时长 8分55秒（音频 535s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 下面呢我们来实现获取验证码的接口方法那么在刚才我们写的Service的这个方法当中啊我们需要在这个send msg这个方法当中啊来向验证码服务来发送什么验证码来发送请求获取验证码好那么这里边呢我们要思考一下这个代码怎么写呢代码我们之前测试过我们可以
[00:27] 看一下首先指定URL然后呢指定请求体请求头然后通过REST Template得到响应最终解析出我们要的key其实这个代码我们之前完全测试过对吧所以你把它直接可以拿过来可以吧好拿过来之后呢注意这里边呢我们把配置信息呢稍微改一下啊这个呢其实应该是叫URL这个URL是什么呀是不是就是验证码服务的URL
[00:57] 但是大家思考一个问题就是这个URL现在是在代码当中硬编码写死了对吧包括这些参数都是死的所以这里边将来如果我们比如说想调有效期包括这个验证码服务的URL变了所以你不能这样硬编码这样不好所以我们要怎么做我们要把这些URL包括有效期所用到的这些参数我们都把它给配置起来
[01:26] 那我们看讲义我们需要在NICOS里面来配置我们啊所使用的验证码服务的URL以及有效期那这个NICOS呢前边我们学习过啊这个NICOS里面呢我们可以统一管理我们的配置文件呃在我们的这个商户平台应用的配置文件当中啊你要知道啊我们的应用名是不是叫啊merchant gunapplication呢
[01:53] 所以它对应的配置文件是这个NAME的名称加上YAML就是这个文件的扩展名所以你打开Necros我们就要找到商户平台应用工程所对应的配置文件是不是就是这个merchandise-application.yaml好那么你点编辑那么在这里呢我们就要配置刚才我们看到的这个配置信息好那这个配置信息呢我建议你直接复制到我们的
[02:22] Nexus里边就行了注意啊这里边我要说一下你复制的话可能这个有点错位所以这个SMS是顶头对吧然后后边URL是空两格这是YAML的这种格式啊好那么我们这时候呢就把这个配置就配置好了配置好了之后呢那在哪用呢因为我们刚才说了嘛你主要是在写Service方法的时候啊
[02:52] 我们不想让这些URL啊包括配置参数呢硬编码所以我们是不是要在这里是不是要把它给注进来对吧那注进来怎么注啊我们当初是不是也学过这个Necros所以这里面呢我们就用这个$有value注解我们就可以把它注进来那么我们把这个注进来了之后呢这儿我是不是就可以你看这儿是不是就直接拿到
[03:21] 这个URL了好还要注入什么呀刚才你也看到了是不是还有一个有效期呀所以这里边其实我们还要注入这个什么有效期也拿到了好那现在呢我们要做的事是不是就是要把这个URL给它补充完整呀这就是向验证码服务发送请求的什么地址
[03:53] 对吧然后前边这一堆是不是就前边的URL加上加上怎么样看好啊加上这个对吧然后呢你可以颠倒一下这么写啊然后呢把有效期我们要用刚才你注进来的这个有效期我这样下大家能看懂吧这样这个URL是不是就拿到这个URL是不是我们就可以通过配置文件呢就把它拿到然后呢你把它
[04:27] 填充到我们这里头好还有呢这里边因为这是我们原来测试代码考过来了这里边这儿是不是也需要改一下这就是我们传进来的参数对吧那rest template因为我们要用它所以不用说我们肯定要把它注进来OK那到这儿为止我们是不是把
[04:50] 这个URL包括有效期包括REST的template都注进来了这个代码目前来说大家看是不是还有点报错你看有一个log那这个是当初啊我们在测试的时候你没发现吗我们是用了LongBorg的这个SL4J这个注解所以我们也可以在这儿也加一个SL4J这样它是不是就不报错了好那么我们来看这个Service的方法呢我们就
[05:17] 写好了那写好了之后呢注意啊这里边我要把这个代码稍微修整一下修整什么呢你比如说你举个例子那在执行这个请求的时候如果抛异常了那怎么办呢我们是不是就可以来做一些简单的异常处理在后边我们会详细的来讲解异常处理在那我先简单的做一个异常处理可以吧好
[05:43] 如果要抛异常了那么我们就在这呢准备让它抛出一个异常而这个异常呢我们就说叫做发送验证码失败行吗好那么后边还有那么你拿到了这个什么这个响应的结果我们是不是要解析这个body啊
[06:09] 对不对那么你解析这个body的时候这里边这非常重要哪里重要也就是说当我们要解析body最后解析redout再最后解析key这个过程那如果出错了那相当于这个验证码是不是也是没有得到正确的结果所以我们这里边也可以来做一些简单的异常处理来看我们的讲义
[06:37] 就是在这呢我们补一个异常如果说它有问题了我们又让它抛出一个异常后面我们会详细学习异常处理啊这儿我们先这样去抛出一个run time的异常然后在这呢我们也去解析一下result如果说有问题就是你拿到的结果并不是我们想要的那我们也提示一个错误懂吧所以我们把这个代码呢简单的给它稍微再调整完善一下好吧好来我们就
[07:07] 放进去这个body呢我们是不是就可以拿过来在这儿行吧然后这里边呢我们就可以在这儿继续写如果说body等于空或者说body你最终拿body拿到了之后是不是要拿result对如果拿到result它也可能是空这种情况如果都出现了那么我们就要让它来
[07:36] 报一个错叫发送验证码失败或出错好那么如果这两次异常都不抛出那这个时候呢我们就认为这个过程是不是就OK了所以我们是不是就可以来拿RELOAD并且要拿KEY那最后我们这是不是可以打一个日志啊对吧那这个日志我们是不是就叫说表示是得到发送验证码对应的KEY
[08:05] 好这个key你可以写进来对吧将来我们去排错那到这儿我们说这个方法的实现Service方法我们就写完了Service方法OK了之后呢我们是不是在control里面去调用看见在这儿是不是调一下好到这儿为止我们的整个方法实现部分就写完了总结一下在方法实现的过程当中如果用到了配置信息我们统一在Nikos配置
[08:36] 然后呢我们在写方法的时候要注意简单的一些什么异常处理后边我们会统一的来进行异常处理但是这里边呢你得有这么一个意识好到这儿我们的发送验证码的实现部分就写完了稍后我们进行测试

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在商户平台应用中通过 RestTemplate 调用短信服务接口获取验证码，并在服务层封装该逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Nacos 配置中心界面，要求编辑 merchant-application.yaml 配置文件，配置短信服务的 url 和 effectiveTime。
画面2：展示 IntelliJ IDEA 中的 RestTemplateTest.java 文件，演示如何使用 RestTemplate 发起 POST 请求获取验证码。
画面3：展示 SmsServiceImp.java 文件，正在编写获取验证码的业务逻辑，URL 中包含 effectiveTime 参数。
画面4：展示 Nacos 配置中心界面，配置文件中 url 字段被高亮显示，effectiveTime 为 600。
画面5：展示 SmsServiceImp.java 文件，正在编写获取验证码的业务逻辑，URL 中包含 effectiveTime 参数。
画面6：展示 SmsServiceImp.java 文件，正在编写获取验证码的业务逻辑，URL 中包含 effectiveTime 参数。
画面7：展示 SmsServiceImp.java 文件，正在编写获取验证码的业务逻辑，URL 中包含 effectiveTime 参数。
画面8：展示 SmsServiceImp.java 文件，正在编写获取验证码的业务逻辑，URL 中包含 effectiveTime 参数。
画面9：展示 SmsServiceImp.java 文件，正在编写获取验证码的业务逻辑，URL 中包含 effectiveTime 参数。
画面10：展示 SmsServiceImp.java 文件，正在编写获取验证码的业务逻辑，URL 中包含 effectiveTime 参数。
画面11：展示 SmsServiceImp.java 文件，正在编写获取验证码的业务逻辑，URL 中包含 effectiveTime 参数。
画面12：展示 SmsServiceImp.java 文件，正在编写获取验证码的业务逻辑，URL 中包含 effectiveTime 参数。
画面13：展示 SmsServiceImp.java 文件，正在编写获取验证码的业务逻辑，URL 中包含 effectiveTime 参数。
画面14：展示商户注册页面，用户填写手机号、账号、密码等信息，点击“注册”按钮。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
在Nacos上配置验证码的接口地址
1. 登录Nacos，编辑merchant-application.yaml配置：
2. 配置如下参数
sms:
  url: "http://localhost:56085/sailing"
  effectiveTime: 600
```

画面2：
```
Map<String, Object> body = new HashMap<>();
body.put("mobile", "133456");
//请求头
HttpHeaders httpHeaders = new HttpHeaders();
//指定Content-Type: application/json
httpHeaders.setContentType(MediaType.APPLICATION_JSON);
//请求体
HttpEntity<Map<String, Object>> httpEntity = new HttpEntity<>(body, httpHeaders);
//向后端请求
ResponseEntity<Map> exchange = restTemplate.exchange(url, HttpMethod.POST, httpEntity, Map.class);
log.info("请求验证码服务，得到响应:{}", JSON.toJSONString(exchange));
Map bodyMap = exchange.getBody();
System.out.println(bodyMap);
Map result = (Map) bodyMap.get("result");
Map bodyMap = exchange.getBody();
Map result = (Map) bodyMap.get("result");
String key = (String) result.get("key");
System.out.println(key);
return key;
```

画面3：
```
//向短信服务发送请求获取验证码
String url = "http://localhost:56085/sailing/generate?effectiveTime=600&name=sms";
```

画面4：
```
sms:
  url: "http://localhost:56085/sailing"
  effectiveTime: 600
```

画面5：
```
//向短信服务发送请求获取验证码
String url = "http://localhost:56085/sailing/generate?effectiveTime=600&name=sms";
```

画面6：
```
//向短信服务发送请求获取验证码
String url = "http://localhost:56085/sailing/generate?effectiveTime=600&name=sms";
```

画面7：
```
//请求体
HttpHeaders httpHeaders = new HttpHeaders();
//指定Content-Type: application/json
httpHeaders.setContentType(MediaType.APPLICATION_JSON);
//请求体
HttpEntity<Map<String, Object>> httpEntity = new HttpEntity<>(body, httpHeaders);
//向后端请求
ResponseEntity<Map> exchange = restTemplate.exchange(sms_url, HttpMethod.POST, httpEntity, Map.class);
```

画面8：
```
import java.util.Map;
//Author Administrator
//@version 1.0
//服务
public class SmsServiceImpl implements SmsService{
    @Value("${sms.url}")
    String url;
    @Value("${sms.effectiveTime}")
    String effectiveTime;
}
```

画面9：
```
//向短信服务发送请求获取验证码
String sms_url = url + "/generate?name=sms&effectiveTime=" + effectiveTime;
```

画面10：
```
//请求体
HttpHeaders httpHeaders = new HttpHeaders();
//指定Content-Type: application/json
httpHeaders.setContentType(MediaType.APPLICATION_JSON);
//请求体
HttpEntity<Map<String, Object>> httpEntity = new HttpEntity<>(body, httpHeaders);
//向后端请求
ResponseEntity<Map> exchange = restTemplate.exchange(sms_url, HttpMethod.POST, httpEntity, Map.class);
```

画面11：
```
//请求体
HttpHeaders httpHeaders = new HttpHeaders();
//指定Content-Type: application/json
httpHeaders.setContentType(MediaType.APPLICATION_JSON);
//请求体
HttpEntity<Map<String, Object>> httpEntity = new HttpEntity<>(body, httpHeaders);
//向后端请求
ResponseEntity<Map> exchange = restTemplate.exchange(sms_url, HttpMethod.POST, httpEntity, Map.class);
```

画面12：
```
log.info("请求验证码服务，得到响应:{}", JSON.toJSONString(exchange));
Map bodyMap = exchange.getBody();
System.out.println(bodyMap);
Map result = (Map) bodyMap.get("result");
String key = (String) result.get("key");
System.out.println(key);
return key;
```

画面13：
```
//向短信服务发送请求获取验证码
String sms_url = url + "/generate?name=sms&effectiveTime=" + effectiveTime;
```

画面14：
无代码或配置内容。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：
标题：2.3.2.2 接口实现
子标题：1. 配置验证码服务的接口地址
内容：在Nacos上配置验证码的接口地址
步骤：
1. 登录Nacos，编辑merchant-application.yaml配置：
2. 配置如下参数

画面14：
标题：商户注册成功
内容：1、用户填写手机号、账号、密码等信息
表单字段：
- 账号
- 密码
- 手机号
- 验证码
按钮：
- 注册

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）

