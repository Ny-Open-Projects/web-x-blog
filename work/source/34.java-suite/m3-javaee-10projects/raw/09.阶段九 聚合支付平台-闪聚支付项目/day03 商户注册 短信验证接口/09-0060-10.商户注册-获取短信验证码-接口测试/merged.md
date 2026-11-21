# 10.商户注册-获取短信验证码-接口测试

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day03 商户注册 短信验证接口
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day03 商户注册 短信验证接口\10.商户注册-获取短信验证码-接口测试【海量资源尽在 666java.com】.mp4
- 时长 5分1秒（音频 301s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们来测试一下接口那刚才我们来写完了整个发送验证码的接口方法然后我们把工程呢也重启之后呢我们就可以来测试这个接口具体的测试方法我们第一可以通过Swagger文档来进行测试其实这里边大家可以看到是不是有一个叫获取手机验证码那么也可以通过Postman来进行测试
[00:31] 那这里边我更推荐你用Postman来测试因为在这个Postman里边它提供的功能还是比较丰富的所以这里边呢我们用Postman来测试好那么具体怎么做呢看好啊所以这里边我们新建一个collection在当初我们学习这个Postman的时候呢我们其实当初已经简单的来看了一下Postman的一个使用方法
[01:01] 对吧所以这里边呢我们要正式的去使用这个Postman我们要先借一个Clackson这个接口测试的一个集合然后这里边我们起一个名字叫散聚支付开发然后呢叫我加一个标记吧叫M2然后呢来创建然后在这个散聚支付开发M2这个集合下边呢我们要去
[01:31] 创建一些什么具体的接口了那么我们为了方便来管理这些接口呢我建一个目录这个目录呢就叫做商户注册可以吧在这个商户注册下边我们就会创建请求这个请求我们现在要做的是不是就是发送验证码呀发送验证码这里面呢我们你要选请求所归属的这个集合
[02:01] 刚才我们是不是有一个叫散具支付开发M2商户注册来创建这就OK了然后呢点击保存然后这里边我们要输入我们的地址好这个地址呢就是我们的URL地址URL地址的话大家注意看啊你可以在这里获取来注意看然后你拿到这是不是就是我们的地址对不对然后呢
[02:31] 你把它贴到这儿这个这个份子里头呢我们就输入手机号随便输啊现在反正这个手机号目前来说我们是没有向手机来发送验证码我们是通过控制台打印的方式对吧好然后把它写好了之后呢接下来我们来看我们在这儿把这个日志清一下然后把验证码也清一下好也清一下现在我们是不是就可以来点击发送点击发送好
[03:02] 那这时候你看它是不是得到一个响应这就是一个我们说验证码对应的key然后在验证码服务的控制台上面我们来看这是不是打印的日志这就是最终它是不是就可以我们现在要让它发送验证码在验证码服务在这个selling里头是吧在这是不是有一个叫给手机号124432发送这个验证码那它这是不是就说明我们的这个
[03:33] 整个发送验证码的流程就测试通过了当然你也可以观察Redis因为我们说它这个Redis里边就存了它的什么验证码可以看一下这里边我们刚才返回的这个key是不是叫做末尾是第6A1第6A1你看是不是它这个验证码是不是就是670650看一下它控制台打印的670650正确吧好那其实到这儿
[04:02] 我们说这个接口基本上就测试通过了当然我们在测试接口的时候我们如果遇到问题是需要在这里打断点来一步一步调试的那首先比如说我想看看参数传递是否有问题你就在Controller打一个断点一点然后这时候呢它就会进到Controller然后呢在这儿我们来看它是不是就
[04:30] 可以看到这个手机号已经传进来了对然后呢继续我们在Service上边也打断点然后让它往前走到这你就可以断点的一步一步的来执行调试大家能看懂吗对这就是整个的具体的一个什么调试的过程那后边呢我们会经常来调试我们的程序好那么到这为止我们的发送验证码的接口测试
[05:00] 完成了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Postman 测试获取短信验证码的接口，并展示后端 Java 代码实现逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示课程文档，内容为“2.3.2.3 接口测试”，说明使用 Postman 测试获取验证码接口：http://localhost:57010/merchant/sms?phone=17717171717。
画面 2：IDE 中显示 MerchantController.java 代码，包含注释“发送手机验证码”和“Return 验证码对应的key”，以及方法 `public String sendMsg(String phone)`。
画面 3：Swagger UI 页面，显示“闪聚支付-商户应用API文档”，包含接口 /hello、/h1、/merchants/{id}、/sms。
画面 4：Postman 界面，显示“Create New”窗口，包含“Request”、“Collection”、“Environment”等选项。
画面 5：Postman 界面，鼠标悬停在“API Documentation”选项上。
画面 6：Swagger UI 页面，显示 GET /sms 接口，参数为 phone（手机号），并有“Execute”按钮。
画面 7：IDE 中显示 MerchantController.java 代码，包含注释“获取手机验证码”和“Return 验证码对应的key”，以及方法 `public String sendMsg(String phone)`。
画面 8：Postman 界面，显示 GET 请求，URL 为 http://localhost:57010/merchant/sms?phone=124432，Body 中包含 JSON 数据。
画面 9：Redis Desktop Manager 界面，显示连接到 localhost:6379，选中 redis-01，日志显示连接成功。
画面 10：课程文档页面，内容为“2.3.2.3 接口测试”，说明使用 Postman 测试获取验证码接口：http://localhost:57010/merchant/sms?phone=17717171717。
画面 11：IDE 中显示 MerchantController.java 代码，包含注释“获取手机验证码”和“Return 验证码对应的key”，以及方法 `public String sendMsg(String phone)`。
画面 12：IDE 中显示 SendService.java 代码，包含注释“发送验证码”，以及方法 `public String sendMsg(String phone)`。
画面 13：IDE 中显示 SendService.java 代码，包含注释“发送验证码”，以及方法 `public String sendMsg(String phone)`。
画面 14：课程文档页面，内容为“2.3.2.3 接口测试”，说明使用 Postman 测试获取验证码接口：http://localhost:57010/merchant/sms?phone=17717171717。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2：
```java
/**
 * 发送手机验证码
 * @param phone 手机号
 * @return 验证码对应的key
 */
@Override
public String sendMsg(String phone) {
    // 同验证短信发送请求的地址
    String sms_url = url + "/generate?name=" + sms + "&effectiveTime=" + effectiveTime;
    ...
}
```

画面 7：
```java
/**
 * 获取手机验证码
 * @param id
 * @return
 */
@GetMapping("/sms")
public String getSmsCode(@RequestParam(value = "phone", required = true, dataType = "string") String phone) {
    return smsService.sendMsg(phone);
}

@GetMapping("/hello")
public String hello() {
    return "hello";
}
```

画面 12：
```java
/**
 * 发送验证码
 * @param phone 手机号
 * @return 验证码对应的key
 */
@Override
public String sendMsg(String phone) {
    // 同验证短信发送请求的地址
    String sms_url = url + "/generate?name=" + sms + "&effectiveTime=" + effectiveTime;
    ...
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

