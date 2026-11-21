# day09-5-审核标的-存管代理-功能实现2

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-10 实现审核标的功能
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-10 实现审核标的功能\day09-5-审核标的-存管代理-功能实现2_【海量资源尽在 666java.com】.mp4
- 时长 13分2秒（音频 782s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 刚才呢我们把前两步的代码编写完了那接下来就要进行第三步那么第三步呢就是存款代理服务这边要往银行那边发数据据点来说就是主要发送这个标题信息了银行那边是要做保存那这边我们就要先确定两块内容了哪两块内容呢第一块就是发送的地址就是你往哪发这个URL地址第二个呢就是发送哪些数据这很自然的事嘛对吧
[00:31] 这个URL地址呢怎么确定呢咱几个也来URL地址大家不知道有没有印象啊在开会的时候这个URL地址就银行那边的那个请求地址我们是不是配到阿卜罗里边去阿卜罗里边瞅一瞅再再再存款代理服务咱们找一找稍等片刻啊是这吧depository什么呀对没错就是他那这个呢是银行那边的基本访问路径那我们得先获得这个路径啊
[01:07] 这个路径怎么获得呢这个路径呢跟咱之前的套路是一样这个路径我们这提前准备了一个看飞格Service还有印象吧那之前用过通过它是不是就可以从Apollo上取一些数据比如说这个值咱是不是就叫这个值呢刚才让大家瞅了一眼对不对咱直接住他然后调用他的这个方法就OK了咱看咱前面住过没已经住过是不是开户的时候之前晚上用过啊
[01:37] 然后呢咱就直接往这儿啊调用一下对他什么呀地poster1 l 但是你导到这个地址还不够啊我们是不是还要访问他具体的某个什么呀呀呃具体的某个Controller对不对那他扛出来的那个地址呢我在这直接给大家写一下就是s e r v s e sservice没有这个s Service
[02:09] 那有同学老师这个地址你你自己写的我哪知道你是照哪写的这个呢是银行那边的一个一个路径那你要想看这个东西你得打开银行存款那个那个服务那这样呢我打开了你可以看看虽然银行这边这个系统不需要大家去管也不需要你编写但是这个代码你还可以打开看看啊就这个卡车了Service咱这儿是使用它的这个直连的这个接口啊你看这儿你看这儿是不是创建标的嘛对不对你看这儿
[02:37] 这个get mapping 这个路径是不是 Service对不对其实是照这写的啊比如我们将来呢发请求就是往这发具体位置就往这发那我们就可以先把它拼接成一个地址先存起来吧url 吧这是发送的地址或者请求地址我们确定确定完之后呢我们就要说发送哪些数据这个发送的数据呢相来说会多一些啊这个你也可以看一下银行存款系统是不是刚才不是找到这个kontrol 了这个方法了吗创建标题这个方法
[03:13] 你看这里面都要都要啥什么呀这是什么呀这是那个接口名称就是你是开户的还是发标的还是投标的还是要呃曲线对不对还是要充值啊第二层就是平台的编号平台编号呢咱之前说过银行人家那边对接的这个p2p平台多了去了咱们万信金融这个p2p平台对于人家银行来说是不是只是其中一个这是咱们平台的一个编号
[03:42] 然后这是签名数据这就是咱们发送的那个什么呀对业务上的数据啊JSON格式他这边是at request的perm证明都是问号那种形式传过来的1234四大参数是不是银行那边一般要的都是四大参数这他要的一些数据咱基本上也确定这啊咱基本确定那接下来就是怎么发的怎么发那就要用到什么呀OK
[04:20] http client发送什么呀对http请求我们要用到http client这样一个一个一个工具包吧相当于通过它发起http请求然后往这发请求把刚才我说的四大参数那些数据呢给捎带过去就行那这块代码的话我们提前做了封桌咱看一看讲义大家看这
[04:51] 我们给大家提供两个类大家呢直接拿过来用给它复制到这个存款代理工程当中就行了我们来介绍一下这个OKHTTP Service呢它就是主要通过OKHTTP Client来发送什么呀HTTP请求这是这个类所起的作用而第二个类这个名字比较长就是一个大家看这个名字是不是叫签名拦截器这个类的作用就是在你发请求的时候对数据进行签名有的学员说老师咱刚才第二步不是搞过签名了吗
[05:22] 那大家看一下第二步其实咱这个签名其实做的不彻底其实咱第二步这个相当于是做了一些什么签名的准备工作其实还没签名因为我们把签名的这个功能给抽取出来放到这个什么呀拦截器里边就这个拦截器里边有时候将来呢我们通过这个类去发请求这个请求在发出去之前呢这个拦截器会自动拦截住这个请求然后对里边的数据进行什么呀签名
[05:51] 所以这个事咱不用管但是呢我们的确是用到他俩所以说呢这两个类呢我们直接给他考到咱这个从管代理工程当中直接拿用就行我看我这里边考过了没有我这里边应该是应该是没有对吧没有的话咱还是去资料文件夹里边找一找分别是谁啊在在这一个是吧
[06:21] 我先打开看一看应该考到什么地方应该是在右层吧Service 是吧右层还有一个谁还有一个拦截器应该放到是 intercept 一个包里的 intercept是不是拦截就把它先考到工程里边再说一个是 Service 这已经有了这已经有了那这个来源器有吗来源器也一定有了这都有了那不用考那咱打开看一下ok Service你看这里边就封装了一个方法
[06:55] 专门发这个ATB请求了啊主要是给他请这里边就是OKHTB client工具类里边的一些API然后呢咱看看这个谁呀这个签名来年期这个签名来年期是这样子的当这个我们通过OK一句siris发请求的时候啊那么这个来年期就会进行拦截拦截完之后呢他在这里边就会进行数据的一个什么呀签名你看这个代码来抽到这里来这样更方便吗
[07:26] 因为我们这个存管代理服务这边他不经常都得进行这个数据签名了所以咱把它抽取出来放到一个蓝银器里边将来你发请求的时候你就不用管这个事他就自动蓝银请求进行数据签名我这个代码呢大家也不用管他你直接拿用就行说这个就我们就把这个代码考进来考进来之后呢那这个具体这个第三步这个代码具体怎么编写呢我们是建议大家给抽取出来一个方法
[07:56] 因为这个代码写下来稍微有点复杂吧大家看这就这个方在这个方案里边呢我们说了就要用到okhttp Service还有这个什么呀来年期啊当然代码里边其实只是体验出来了okhttp Service啊这个来信呢你体验不出来因为他是自动工作你看这里边代码的话嗯其实发送数据倒不是很多关键是他后续是不是做了很多这个呃就是产生结果之后做了一些业务处理
[08:27] 要做两种判断加起来这个代码有点多了咱过一遍你看这里边首先我们说了银行那边是不是有四大参数你看这里边这是四个参数一个都不少对不对然后就是这里边还缺一个什么平台平台编号我们是从config Service从通过它从安波罗里边取出来然后具体发请求就是这OKHTPService是不是我们刚才看了它里边封装这么一个方法请求地址我们刚才是不形容好了
[09:00] 然后把这个四大参数来拼击到一起发过去就行了发完之后呢这边是不是有反对数据的一个字母串啊就是银行那边反对数据反对数据呢我们怎么用呢咱们前面在定义什么定义接口的时候跟大家介绍过啊我们最终是不是要封装成这种类型这种类型范围形呢是depository based response最终呢是要封装成depository response DTO那我们就要用到发送的json就是parts object
[09:30] 把银行返回的这个数据转移成这个对象当然你在这要指定这个范想告诉他你要转移成什么类型其实到这的话我们这个就已经把数据发到银行那边而且已经接收到了银行返回的这个数据了后面这一块if else是干嘛这个代码你看多但是其实比较好一点这边是判断银行那边返回的结果解析一下嘛这是解析验签嘛看它是什么呀true还是false你就判断成功还是什么呀
[10:01] 对还是失败啊上面这个是成功这加了一个非啊看上面是成功下面这个是什么呀失败这是咱声明了一个变量声明了一个变量当然你这也可以直接写false一个字符号false就行了他这是专门还定义了一个静态常量吧啊这无所谓那那成功的情况下你看我们是要做一些状态的更新啊还要更新一个时间对不对这就是做这就更新了一个一个那个状态原来是未同步现在改成已同步
[10:35] 失败的时候呢我们都做了什么事失败的时候呢就是改成失败的那个状态对不对四样然后也是这个确认的时间然后也要更新这个什么呀数据库就是这这这个谁呀这个depository recorder这个交易记录嘛他这个数据你怎么着都是要更新的就是这个状态不管成功失败成功是成功的值失败失败的值嘛包括这个时间也是一样都需要进行更新这是这一块的代码
[11:03] 不要求大家能编写啊但是要求呢你这个代码从上大家过一遍能看到因为这个呢主要是跟银行那边的系统打交道而银行那边系统呢这个咱们又开发嘛是不是不然进来把这块代码咱粘过来我们就放到下边吧放到下边放到下边之后是这样子的啊里边呢你像这个地方像这个地方你其实你要么就是声明一个什么呀精彩常亮你要么这直接就写一个什么呀写一个fos也可以
[11:49] 然后这边呢是需要注入吗OKHTTP Service我们前面需要注入一下这还没有注入过这一代你自己补一下就行这儿呢我们要注入进来的就是OKHTTP Service注进来下面应该就不包错了吧是吧这边就可以啊这儿应该是需要再导个包导这个发色的jason就包别导错然后这个代码的话你像你自己这个格上整理一下就行
[12:28] 关键就是我刚才给大家说的这块代码大家一定要能看明白啊他是干啥了主要是用来往银行存款系统那边发送数据然后接收结果然后呢进行后续数据的比如状态的一些处理一些更新之类的这个功能其实跟我们这个食欲图里边是不是一一对应呢对不对你看这儿是发送请求的这边是更新什么呀交易记录更新什么状态所以我们在编译代码的时候还要结合这个食欲图
[12:58] 来去理解就行

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个项目中如何通过拦截器对请求进行签名验证，并调用银行存管系统接口完成项目创建的完整流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示IDE中`DepositoryRecordServiceImpl.java`文件，代码中将`ProjectDTO`转换为`ProjectRequestDataDTO`，并将其转为JSON字符串，然后使用`EncryptUtil.decodeUTF8StringBase64`解码。
画面2：在IDE中选中`DepositoryRecordServiceImpl.java`文件，同时显示了两个窗口，其中一个为`wanningzp_apollo`项目，另一个为`wanningzp`项目。
画面3：在IDE中选中`ServiceController.java`文件，显示了`@ApiOperation`注解和`createProject`方法的代码，其中包含对请求参数的校验和业务逻辑。
画面4：在IDE中选中`DepositoryRecordServiceImpl.java`文件，代码中调用`configService.getDepositoryUrl()`获取银行存管系统的URL，并准备发送HTTP请求。
画面5：在IDE中选中`DepositoryRecordServiceImpl.java`文件，代码中使用`OkHttpClient`发送HTTP请求，并处理响应。
画面6：显示了Windows文件资源管理器，路径为`wanningzp\day06\资料`，其中包含三个项目文件夹。
画面7：在IDE中选中`DepositoryRecordServiceImpl.java`文件，代码中使用`configService.getDepositoryUrl()`获取银行存管系统的URL，并准备发送HTTP请求。
画面8：在IDE中选中`SignatureInterceptor.java`文件，代码中定义了拦截器的`intercept`方法，用于处理HTTP请求。
画面9：在IDE中选中`SignatureInterceptor.java`文件，代码中解析响应数据并提取签名信息，然后进行签名验证。
画面10：在PDF阅读器中显示了文档内容，其中包含`sendToBank`方法的代码，用于向银行存管系统发送数据。
画面11：在PDF阅读器中显示了文档内容，其中包含`depositoryRecord`对象的状态更新和异常处理代码。
画面12：在IDE中选中`DepositoryRecordServiceImpl.java`文件，代码中定义了`createConsumer`方法，用于创建消费者。
画面13：在IDE中选中`DepositoryRecordServiceImpl.java`文件，代码中使用`TypeReference`类处理响应数据，并根据响应结果更新记录状态。
画面14：显示了银行存管系统的流程图，其中包含“调用源/APP”、“交易中心”、“存管代理服务”、“标的的存管服务”和“银行存管系统”等节点。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
// 签名数据
// ProjectDTO 转换为 ProjectRequestDataDTO
ProjectRequestDataDTO projectRequestDataDTO =
convertProjectDTOToProjectRequestDataDTO(projectDTO,
depositoryRecord.getRequestNo());
// 转换为 JSON
String jsonString = JSON.toJSONString(projectRequestDataDTO);
// base64
String reda = EncryptUtil.decodeUTF8StringBase64(jsonString);
```

画面4：
```java
// 3. 往银行存管系统发送数据 (新的信息)
// url地址
String url = configService.getDepositoryUrl() + "/Service";
// 4. 根据结果修改状态并返回结果
```

画面5：
```java
// 3. 往银行存管系统发送数据 (新的信息)
// url地址
String url = configService.getDepositoryUrl() + "/Service";
// 4. 根据结果修改状态并返回结果
```

画面7：
```java
// 3. 往银行存管系统发送数据 (新的信息)
// url地址
String url = configService.getDepositoryUrl() + "/Service";
// 4. 根据结果修改状态并返回结果
```

画面8：
```java
public class SignatureInterceptor implements Interceptor {
    private final String METHOD_GET = "GET";
    @Autowired
    private ConfigService configService;
    // 签名的编码
    private final String INPUT_CHARSET = "UTF-8";
    @Override
    public Response intercept(Chain chain) throws Exception {
        // 拦截请求，获取多次请求的request
        Request request = chain.request();
        Response response = null;
        Request requestProcess = null;
        if (METHOD_GET.equals(request.method())) {
            // 获取请求参数
            String requestUrl = request.url().toString();
            // 获取请求参数
            String requestParams = request.url().query();
            // 获取请求头
            Headers headers = request.headers();
            // 获取请求体
            String body = request.body().string();
            // 获取请求方法
            String method = request.method();
            // 获取请求头
            String contentType = request.headers().get("Content-Type");
            // 获取请求头
            String accept = request.headers().get("Accept");
            // 获取请求头
            String userAgent = request.headers().get("User-Agent");
            // 获取请求头
            String referer = request.headers().get("Referer");
            // 获取请求头
            String host = request.headers().get("Host");
            // 获取请求头
            String connection = request.headers().get("Connection");
            // 获取请求头
            String cacheControl = request.headers().get("Cache-Control");
            // 获取请求头
            String pragma = request.headers().get("Pragma");
            // 获取请求头
            String upgrade = request.headers().get("Upgrade");
            // 获取请求头
            String contentLength = request.headers().get("Content-Length");
            // 获取请求头
            String transferEncoding = request.headers().get("Transfer-Encoding");
            // 获取请求头
            String acceptEncoding = request.headers().get("Accept-Encoding");
            // 获取请求头
            String acceptLanguage = request.headers().get("Accept-Language");
            // 获取请求头
            String cookie = request.headers().get("Cookie");
            // 获取请求头
            String authorization = request.headers().get("Authorization");
            // 获取请求头
            String xRequestedWith = request.headers().get("X-Requested-With");
            // 获取请求头
            String xForwardedFor = request.headers().get("X-Forwarded-For");
            // 获取请求头
            String xRealIp = request.headers().get("X-Real-IP");
            // 获取请求头
            String xForwardedProto = request.headers().get("X-Forwarded-Proto");
            // 获取请求头
            String xForwardedHost = request.headers().get("X-Forwarded-Host");
            // 获取请求头
            String xForwardedPort = request.headers().get("X-Forwarded-Port");
            // 获取请求头
            String xForwardedProto = request.headers().get("X-Forwarded-Proto");
            // 获取请求头
            String xForwardedHost = request.headers().get("X-Forwarded-Host");
            // 获取请求头
            String xForwardedPort = request.headers().get("X-Forwarded-Port");
            // 获取请求头
            String xForwardedProto = request.headers().get("X-Forwarded-Proto");
            // 获取请求头
            String xForwardedHost = request.headers().get("X-Forwarded-Host");
            // 获取请求头
            String xForwardedPort = request.headers().get("X-Forwarded-Port");
            // 获取请求头
            String xForwardedProto = request.headers().get("X-Forwarded-Proto");
            // 获取请求头
            String xForwardedHost = request.headers().get("X-Forwarded-Host");
            // 获取请求头
            String xForwardedPort = request.headers().get("X-Forwarded-Port");
            // 获取请求头
            String xForwardedProto = request.headers().get("X-Forwarded-Proto");
            // 获取请求头
            String xForwardedHost = request.headers().get("X-Forwarded-Host");
            // 获取请求头
            String xForwardedPort = request.headers().get("X-Forwarded-Port");
            // 获取请求头
            String xForwardedProto = request.headers().get("X-Forwarded-Proto");
            // 获取请求头
            String xForwardedHost = request.headers().get("X-Forwarded-Host");
            // 获取请求头
            String xForwardedPort = request.headers().get("X-Forwarded-Port");
            // 获取请求头
            String xForwardedProto = request.headers().get("X-Forwarded-Proto");
            // 获取请求头
            String xForwardedHost = request.headers().get("X-Forwarded-Host");
            // 获取请求头
            String xForwardedPort = request.headers().get("X-Forwarded-Port");
            // 获取请求头
            String xForwardedProto = request.headers().get("X-Forwarded-Proto");
            // 获取请求头
            String xForwardedHost = request.headers().get("X-Forwarded-Host");
            // 获取请求头
            String xForwardedPort = request.headers().get("X-Forwarded-Port");
            // 获取请求头
            String xForwardedProto = request.headers

