# day03-6-校验手机号和验证码功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day03-6-校验手机号和验证码功能测试_【海量资源尽在 666java.com】.mp4
- 时长 11分20秒（音频 680s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 截止到目前呢咱把注册业务当中的第二块代码就是校验手机号和验证码整个这一块的功能全部搞定代码呢全部编写完了编完之后呢接下来咱自然就要进行对功能测试每次进行测试的时候大家一定要注意你首先要考虑好的一个问题就是我都需要启动哪些服务因为越往后咱要启动的服务越来越多
[00:30] 这个你一定要想清楚少起一个你测试的时候就要出问题那咱这块这个功能都需要启动哪些东西大家想一想首先Apollo是不一定要启动这个都不用说了吧咱以后是不是这个Apollo你不启动你的本地微服务就没配置了相当于那你启动启不起来是不是然后呢我们这个功能还要求我们启动什么呀Redis和什么服务啊对短信验证版那个服务嘛
[01:01] 是不是咱都需要启动那还有吗没了啊大概呢是这几个微服要启动那咱们这个微服工程里边都需要启动啥微服工程里边你目前只需要启动一个注册中心是不是还有一个这个account这个微服就够了大概启动这么多这个是该启动的我都提前启动过了啊为了节省时间啊刚才大家看到全都已经启动过了启动过之后呢咱接下来就该进行测试了那测测试的话咱目前无非就是
[01:31] 两个工具两个神器一个就是什么呀Swag这我都已经打开了还有一个就是什么呀对后此慢这两种呢我们尽量都给大家演示一下刚开始了那么到了以后的话我就不会说每个功能我都用这两个神器给你测测测我可能就比如说只用postman对不对这个大家注意那我先去sweat这儿sweat这我们是不是应该点击这个你看这是不是校验手机号和什么验证码大家看一下
[02:01] 这是get请求这是请求的地址对不对下面是要求我们传的参数我们说一共传几个参数三个一个就是验证码一个是交易标识一个手机号这个交易标识不就是咱之前反复给大家强调过了就是验证码微服务那边他在发送验证码的时候是不是会生成一个键对吧key会存到什么redis里前端在发请求的时候他会把这个key给发到我们的后端后端拿了这个交易标识会去redis当中取那个什么
[02:33] 正确的验证码然后跟咱这个验证码做什么呀得做对比就行了这个咱以前说过所以我们一共传过去几样东西啊三样啊三样东西那咱接下来就试一试怎么试啊在Swagger里边我们之前说try一下对吧try它啊就try it out然后这时候呢这个界面里边就要求你是不是输入三样东西是吧那大家想我要校验手机号验证码我是不是得先
[02:58] 干什么呀先发送并获取验证码对不对所以你要测这个功能你不能在这直接测呀不行你得先干什么呀先走这一步获取手机验证码那我们也是踹一下然后这儿输一个手机号15378791911这个手机号你可以输但是你一定要挑一个你表里边已经存在的好我们走这边我们应该能正常的获取到这个什么呀你看这是那个key嘛
[03:29] 对就是那个校验标识我们Ctrl C一下然后回到上边回到测试里边把这个校验标识考到这儿验证码去控制台瞅控制台这不是716354对不对然后你就粘到这里手机号还是刚才那个手机号15378791911对吧
[03:57] 好接下来咱就一Q它开始测试这个什么功能校验手机号和验证码的这个功能目前咱给的这些值应该都是正确是不是都没问题啊走好咱看看已经返回东西了哎他说验证码错误这不应该啊这个验证码错误咱这是不是刚发的验证码哎我刚才是不是考错了验证码我是不是考上以前发的那个验证码我再复制一个新的啊这没事咱正好把错误的这种情况也
[04:28] 验证一下我又换了一个验证码再次点击什么是q它走好这次我们看看这次返回到什么零没有表示是成功了就正常交易通过了是不是这个功能我们就测试通过了这是在哪测试的在sweger里边咱接下来去postman里边测试postman测试的话你看我们以前是不是测试过第一块就是获取短线验证对不对
[04:58] 那我这是不是需要新建一个什么呀请求这个请求是专门是用来干什么呀叫验手机号和什么呀对验证码供党的啊我们还是把它保存到保存到那个那个谁呀通讯账户这个微服这个集合里边然后呢我们看看啊我们可以抽抽sweat这是什么请求啊get请求给他请求不用动了然后呢请求的地址不就是这个地址吗
[05:30] 你可以从这儿沾过去这儿对这个你就不用自己手敲了嘛因为SWAG它在测试的时候它就产生这个地址了你沾到这儿明白什么意思吧这不是咱手机号吗这个不是咱那个那个什么呀那个那个胶验标识吗这个就是那个谁呀段先生嘛对不对他是在这个路径里边就把数据都传过去了是不是那咱接下来我就直接点击什么呀send了咱试一试啊在postman里边试一试点击send
[06:03] 走好你看也干什么呀0嘛也成功了是不是那你肯定呢你死来这次通过你扑腾的外没有理由不通过了是不是好这是建议通过了建议通过之后呢咱回过头来还要说说这个事什么事呢你看大家应该有印象啊我们之前是不是专门有一个视频是在讲咱们这个项目当中的一个异常处理机制的这个大家还有印象吗刚讲是不是这个图你还有印象吗有吧那咱
[06:36] 目前是不是把咱们万信金融P2P相当于相当于是第一块完整的功能目前来说第一块相对完整的功能给搞定了搞定完之后呢咱要回过来再说说这个谁啊异常处理机制其实刚才我在Spagger里边测试的时候这个异常处理机制已经工作了我不知道你有没有注意过一开始我这是不是验证码输错了你会发现他刚才怎么着我再给你演示一下你看这个验证码我现在随便填了
[07:06] 随便说这肯定是错误的对不对你看走然后你看这他提示什么呀验证码错误哎其实你看到这个提示信息的话就证明我们之前设计的那个异常处理机制已经在干什么呀在工作啊那他到底是怎么返回这么一个一个提示信息的呢那咱接下来再回顾回顾啊结合代码回顾回顾因为之前在讲的时候我们并没有结合具体的案例嘛虽然这些代码这个原理都给大家讲但是并没有
[07:36] 结合具体的案例那咱这不是有一个现场的案例吗咱说一说咱既然还可以这样啊可以哪样呢可以加断点通过断点我们就能观察出来这个过程大家看一下这是咱以前写的这个代码这是不是教研那个验证码对不对你看我们以前写的代码这是不是判断那个教研有没有通过了对不对如果教研没通过你看这这是不是我们自定义的那个异常类你还有印象吗咱当时讲的时候你看
[08:05] 这个API当中我们说了我们自定义一个异常的名字business exception你看这儿是我们自己抛了一个自定义异常对吧然后在new这个异常对象的时候我们是不是往里边封装了这个异常提示信息就是我们自定义的这个叫什么自定义的错误代码和什么提示信息你可以点进去看看你看我们这儿是不是140152验证码错误你看咱这个谁这儿返回了140152验证码错误你问什么意思
[08:37] 它其实返回来就是这个地方的东西我们这人工抛的异常那现在我们要还想要明白的就是说这个我人工抛的异常怎么就被捕获到被谁捕获到这个大家还有印象吗我们当时还在看这个图我们当时说了我们是不是设计了一个Sprint MVC的全局异常捕获类叫Global Exception Handler有印象吗在这儿在就是它这里边代码我们之前是不是讲异常处理机的时候给它过了一遍
[09:09] 我们现在只是给大家验证一下而已你看我们现在可以这么做你在这加一个断点我们是不是就可以观察到他的确是走这了吗的确是抛这个异常对吧然后呢你在这这个类当中全局异常捕获类当中在这个地方就这个方案一进来第一行代了你也可以加一个什么呀加一个断点然后我们接下来你就可以观察到这边一抛异常他就会捕获到这个异常然后呢最终把这个异常信息给封装成什么呀rest response然后给前端
[09:38] 我们可以做这么一个断点演示那既然我这就就不用动了直接再走一下不就行了吗对不对走你看这是不是走这了因为我那个验证码是错的嘛所以他这肯定是降业不通过降业不通过就要抛我们这个自定义这个异常对不对里边就是验证码错了嘛然后我在这直接给他放响直接放响我点这放响了走你看他跳到哪是不是就跳到咱们这个global exception hunter对吧我两个跳到那我们说了
[10:06] 他就是专门捕获这个全局这个一场对不对由这个方法进行捕获你看这儿是不是只要是一个塞片的子类都能捕获了我换到这儿之后他先判断是不是咱这个b那次这个这个自定义的这个一场对吧那如果是的话你还往下走走走你看这是不该进行封装了吗把那个错号就是你刚才看到这个错号还有这个什么呀错误提示信息对不对你看他都取出来出来之后封装成什么呀rest response反应力什么呀前端
[10:36] 这个异常也就处理完这一走就走啊对不对那反而前段的就这么一个东西前段是不是可以谈个对话框哎提示腌制码错误是不是很友好对吧而且呢我们说了当时我们在设计这个呃这个什么异常处理机制的时候我们是不是要解决这些问题吗你看现在这些问题解决了没有是不是都可以进去对不对啊所以说这是咱们正好了趁着这个测试什么功能对趁着测试这个校验
[11:03] 监验什么监验手机号验证码这个机会吧把咱们前面设计的那个全局异常处理机制呢也给他进行一个什么检验看他能不能正常工作这是呃监验手机号验证码整个这一块我们就测试到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在万能2P项目中，通过 Swagger UI 调用接口获取短信验证码并验证，同时展示相关的代码实现和异常处理机制。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档，标题为“4.5 注册2：校验手机号和验证码”，并指出接口定义在“wanxingp2p-api工程中的AccountAPI接口”。
画面2：展示IDE中OkHttp工具类的代码，用于发送HTTP请求。
画面3：在Swagger UI中，输入手机号参数，准备调用获取短信验证码的接口。
画面4：在Swagger UI中，输入验证码、key和手机号，点击“Execute”按钮。
画面5：展示Swagger UI中请求的Curl命令和响应体，响应体为{"code": 0, "msg": "string", "result": {}}。
画面6：展示多个窗口，包括Swagger UI、Postman、cmd、IDE等，用于调试和测试。
画面7：展示PPT中的异常处理流程图，包括SpringMVC全局异常捕获、自定义异常抛出、表现层、业务层、数据访问层。
画面8：展示Swagger UI中请求的响应体，响应码为40102，响应信息为“验证码错误”。
画面9：展示IDE中SmsService类的代码，用于验证短信验证码。
画面10：展示多个窗口，包括Swagger UI、Postman、cmd、IDE等，用于调试和测试。
画面11：展示IDE中GlobalExceptionHandler类的代码，用于处理异常。
画面12：展示IDE中SmsService类的代码，用于验证短信验证码。
画面13：展示多个窗口，包括Swagger UI、Postman、cmd、IDE等，用于调试和测试。
画面14：在Swagger UI中，输入验证码、key和手机号，点击“Execute”按钮。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
public static ResponseBody post(String url, String json) {
    OkHttpClient body = new Request.Builder().post(body).build();
    Request request = new Request.Builder().post(body).build();
    try {
        Response response = okHttp3Client.newCall(request).execute();
        if (responseBody != null) {
            return JSON.parseObject(responseBody.string(), RestResponse.class);
        }
    } catch (IOException e) {
        e.printStackTrace();
    }
    return RestResponse.validFail(CommonErrorCode.E_100106, eDesc);
}
```

画面9：
```java
public void verifySmsCode(String key, String code) {
    if (smsHttp == null) {
        StringBuilder params = new StringBuilder();
        params.append("VerificationKey=").append(key).append("VerificationCode=").append(code);
        RestResponse smsResponse = OkHttpUtil.post(url + params, json, "");
        if (smsResponse.getCode() != CommonErrorCode.SUCCESS || smsResponse.getResult().toString().equals("0")) {
            throw new BusinessException(AccountErrorCode.E_40102);
        }
    }
}
```

画面11：
```java
public RestResponse<Null> exceptionNet(HttpServletRequest request, HttpServletResponse response, Exception e) {
    if (instanceof BusinessException) {
        BusinessException be = (BusinessException) e;
        if (CommonErrorCode.CUSTOM.equals(be.getErrorCode())) {
            return new RestResponse<Null>(be.getErrorCode(), be.getMessage());
        } else {
            return new RestResponse<Null>(be.getErrorCode(), be.getMessage());
        }
    } else if (instanceof JsonBindException) {
        return new RestResponse<Null>(CommonErrorCode.E_100104, "找不到资源");
    } else if (instanceof HttpRequestMethodNotSupportedException) {
        return new RestResponse<Null>(CommonErrorCode.E_100105, "method 方法不支持");
    } else if (instanceof HttpMediaTypeNotSupportedException) {
        return new RestResponse<Null>(CommonErrorCode.E_100106, "不支持的媒体类型");
    } else {
        return new RestResponse<Null>(CommonErrorCode.E_100107, "未知异常");
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面7：
- 标题：SpringMVC 全局异常捕获 GlobalExceptionHandler
- 流程图：
  - SpringMVC 全局异常捕获 GlobalExceptionHandler → 抛出自定义异常（包含自定义错误信息）throw new BussinessException(ErrorCode)
  - 抛出自定义异常（包含自定义错误信息）throw new BussinessException(ErrorCode) → 表现层 Controller
  - 抛出自定义异常（包含自定义错误信息）throw new BussinessException(ErrorCode) → 业务层 Service
  - 抛出自定义异常（包含自定义错误信息）throw new BussinessException(ErrorCode) → 数据访问层 Mapper

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

