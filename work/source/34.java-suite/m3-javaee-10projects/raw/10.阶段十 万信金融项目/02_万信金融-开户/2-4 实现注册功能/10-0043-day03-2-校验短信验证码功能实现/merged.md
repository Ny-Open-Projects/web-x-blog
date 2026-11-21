# day03-2-校验短信验证码功能实现

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day03-2-校验短信验证码功能实现_【海量资源尽在 666java.com】.mp4
- 时长 13分28秒（音频 808s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢咱们把这个校验手机号和短信验证码功能的接口给订好订好之后呢咱们就该实现功能那这个功能很明显是不是也是两个吧是不是一个叫校验手机号是否存在一个是校验这个验证码是否正确那咱先实现这个就是校验这个短信验证码是否正确那这个代码应该写到哪大家想这个功能应该跟数据库没关系吧
[00:31] 不涉及到操作数据库吧应该是不是根据我们的这个图是不是应该是跟谁打交道跟验证码服务打交道对不对那咱就不用管数据访问层了那就应该往哪写这个代码写往这个什么右层是不是那右层咱应该写到哪不知道大家记不记得咱当时在实现第一个就是发送命货去短信验证码的时候我们说过凡是跟验证码有关的这个代码咱是单独抽取出来放到SMSservice这个类当中了
[01:02] 有印象吧那所以说呢咱接下来校验这个验证码是否正确这个代码呢咱也放到这个类别单独定义一个方法就OK了还是写到这那咱就定义一个方法吧我把这个注释补一补吧上面这个是干嘛的上面这个是第一个功能咱当时是叫发送并获取短信验证码咱接下来的话再
[01:32] 定义一个方法叫什么呀校验验证码能开始定义方法pubrc publicvoid然后呢发明咱就叫verify就是校验的意思啊教练啥呢教验smscod就是验证码对不对短信验证码那咱接下来分析分析这个这个不要反问值吧这个不得有个教练的结果通过还是不通过
[02:07] 我们这儿是这么设计的如果建议不多直接抛一场直接抛一场所以说不需要反而值那要参数吗那肯定得要参数咱们前面在定义接口的时候你看这儿一共几个参数三个参数对不对但是咱这儿是不是只实现谁叫验证码因此的话这个参数要吗这个参数就不要验证码是不是只跟这两个参数有关所以咱需要这两个参数给它拨过来对不对
[02:36] 那这两个参数分别表是什么意思啊咱前面在定义接口的时候大家说过没有说过吧来我再给大家强调一次啊这key是表示什么呀对叫验标识其实就是i1 d i sreadies中的什么呀键还有最后一个参数叫code这个大家都知道了什么呀就是什么呀对这个就是短信验证码
[03:10] 我是说呃当时在定义接口的时候我们说他是怎么校验这个验证码正确不正确的对他是那个谁啊短信任何服务会拿着这个key从redis当中是不是取那个那个值那个值不就是短信验证码然后跟这做一个什么相当判断就OK了反正这个活不用咱干啊不用咱干那不用咱干那那咱接下来这里边写下代码大家看这看这个指南啊看这个指南指南这个地方咱前面是不是用过这个接口吧
[03:42] 这是发送并获取短信验证码的接口那咱接下来就得用这个接口就是校验短信验证码那也就是说呢我们接下来只需要往这儿发个请求然后呢把这个什么呀就是那个校验标识就是那个key还有咱们填的那个验证码传过去传给谁呀那肯定是发到这儿了呗发到短信验证码服务这边了对不对发给他剩下任何人问我他里边会帮我们进行什么呀对进行校验然后还会返回给我们
[04:14] 结果所以说呢这个代码其实我们完全可以参考是不是这块代码来写就行了对不对所以说呢我们直接也是先做一个判断呗就是如果你开启了这个什么呀短信验证码这个功能的话我才做这个教验的这个事情那么怎么进行教验呢我们是不是还是通过OKHTB YouTube它的pose的方法是不是往什么呀就我们来看这个指南是不是往这发什么呀
[04:44] 他请求把数据传回去就OK了那咱怎么办啊咱就是这个是不是后边还要拼这个参数啊是不是有点麻烦啊对不对那咱这样咱参考讲义跟讲义保持一致吧好像这个这个参数的拼接你有很多种方式嘛第一种呢你就是跟咱之前这个地方一样啊直接用自主串就这么拼就行了那还有一种就是咱这次讲义里面他是用什么来拼接啊是用是用builder
[05:16] 通过stream builder这个耳喷的方法进行拼接可以吗这也可以嘛一样的啊要么你用字母刷加直接拼接要么用耳喷的方法拼接都可以那咱就先拼这个参数吧可不可以先拼这个参数啊那我就先来给stream builder啊buffet行但是咱是应该要用builder的p i m s就拼参数了直接6对不对neal stream builder
[05:44] 那么这个参数呢一开始呢是这个样子我们参考这个谁啊这个指南啊这个参数应该一开始这块是固定的吧是不是这内部的sms跟这是一样的固定的一个写法我们的粘到这这是参数的其中相当于是第一部分吧直接就写到这其实这个接口就是具体来负责什么呀校验的
[06:13] 然后呢后边是还要拼什么呀拼这个什么呀key啊拼这个code是不是这东西的话你刚才说你要么直接用加号直接往后拼也可以用什么呀耳喷的方法耳喷的方法一点一点在这拼呗首先你就粘这个东西呗首先是拼这部分对吧空格最好的就去了啊然后呢再拼直嘛直不就是这个谁啊key吗是不是然后接着接着拼
[06:50] 这一部分等号可别忘了啊这是字符串他也怪智能了对不对那我这呢我就不需要让他给我换行了我是可以写了下然后后边再耳喷的这个值就是这个谁啊扣的呗你看这是不是就拼好了吧拼好没有对这个拼好那接下来呢咱就该调用这个okhttp youtube的pose方法开始发请求了对不对那咱就ok
[07:25] http youtube 啊第二普测法这个话我们前面说过是不是有两个参数第一个参数是那个请求地址第二个参数是那个什么那个尖层数据啊这次呢咱第二个参数是哭那咱重点关注第一个参数第一个参数的话是不是首先要拼接这个啊验证码微服的那个基本路径是不是然后呢往后边再拼这个谁啊params是不是拼这一堆东西了
[07:56] 我们把它给他加进来后边第二个参数给个空就完事这就完事了啊然后呢我们请求发过去之后那边会进行验证了一个交易这样完之后呢那这个结果呢他会返回给我们这个类型呢还是这个rest response我们接收一下这个结果就在这里边那我怎么知道他那边这个成功不成功或者说这个执行有没有什么问题啊那我们这里边要
[08:31] 要进行判断根据什么来进行判断呢那咱看一下这个类这个类呢咱当时给大家介绍过是不是这里边有三个属性嘛第一个属性是不是要表示状态码比如说零就是正常非零呢就表示失败嘛这是那个什么呀提示信息这是具体的这个什么呀数据对不对那咱接下来的话其实主要是判断一下code的值或者说这个谁啊result这个值就行了
[09:03] 那咋判断呢那就是从从这里边咱要取值吧response.get什么code就得到那个状态码了这个状态码我就说呢是什么呀0表示正常对吧非0就表示不正常其实你这也可以直接这么写也就是说不等于什么呀0不等于0对吧也可以这么写但是呢我们这呢用了一种
[09:36] 更好的这种写法就是把这个零啊就是这个数字这个值给它定义到了一个枚举当中啊这个枚举呢是叫cormancorman error code这个类是给大家提供好的你谁哪用啊corman error code. 点谁呢我们应该点这个谁啊success呀他表示成功嘛明明成功对不对啊还要接着点get code啊其实get code的话最终反而在才是零也就是说呢其实我们写了这一堆
[10:07] 其实就等下于这个谁呀0但是呢我们不建议你这直接写个0是通过这个枚举获取到这个0然后呢我们还可以再加上一个什么呀判断吧判断这个谁呀rest response的什么呀get raise out判断它啥呢判断我们先给它转成字母串吧判断它的值是不是falseequalsignore casefalsefalse也表示失败
[10:43] 0.失败那我看我这个条件写的对不对咱整体看一下因为我是想让这个条件成立的时候相当于是交易失败了交易失败我在这要跑一场所以我这个判断是失败的情况那怎么着表示失败呢就是这个值不等于0是吧不等于00表示正常不等于0就表示失败了或者说这个result的值它是多少它是falsefalse也表示失败这个条件应该没写错
[11:13] 那如果卷失败的话怎么办呢我不返回东西我给他抛一个异常抛一个咱自己定义的一个异常叫businessbusinessexception这个异常类呢也是我们直接定义好的啊也是放到那个苦慢工程里边大家可以看一下我们可以去看一下这个咱以后会经常用苦慢对不对business你看他是不是继承了谁啊run timeexception这边有很多方法分装好了各种各样的方法
[11:50] 然后呢你看他这个方案里边他是不是要一个什么呀error code你看这个地方是不是这个error code是个啥东西呢也是我们提供好的一个类我们应该目前应该用的是这个哪应该是用的account同样账户这一块里边你看咱应该要的是这个验证码错对不对要的是这个东西所以说呢这儿呢我们在new这个异常对象的时候呢需要给他传入这个提示信息嘛
[12:19] 就是ALC COUNTALCountal errorACC O U N TE R R error code. 点谁呢一点你就知道应该点他对吧140152要验证码错误我们把这个异常的抛出来就行那这个就是什么代码这个就是我们把校验验证码是否正确的这个功能给现完那基本上是这个样子就是将来啊
[12:53] 他们这个什么呀前端是不是手机号和验证码连同那个验证标识对吧一块就发过来发来之后呢当我们大家走到这的时候是不是这是那个验证标识这是那个验证码对不对然后呢我们通过OKHTB YouTube把这个什么呀把这个什么呀验证标识还有验证码一块发到哪边发到那个验证码微服那边那边会帮我们进行验证这个事我们不用管验证者会反问我们结果反问结果之后我们就判断有没有验证通过不通过的话抛一个异常就OK了
[13:23] 也没讲呢

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在 wanning2p-account-Service 项目中，实现短信验证码功能的前后端代码逻辑，包括发送和校验验证码的接口、服务层实现、统一响应封装及自定义异常处理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了项目结构目录，当前选中的是 wanning2p-account-Service。
- 右侧弹窗显示了“短信验证码”相关说明，包括功能分块（注册、登录、开户）、用户信息字段、注册流程和条件。
- 代码片段：public class UserServiceImpl { @Autowired private UserMapper usermapper; public void save() { ... } }

画面 2：
- 展示了 SmsService 类的代码，其中定义了 smsURL 和 smsEnable 字段，并实现了 getSmCode 方法。
- 代码片段：
  public class SmsService {
      @Value("${sms.url}")
      private String smsURL;
      @Value("${sms.enable}")
      private Boolean smsEnable;
      public RestResponse getSmCode(String mobile) {
          if(smsEnable){
              return OHttUtil.post(smsURL+"/generate?effectiveTime=300&name=sms", "json: {"mobile": ... });
          }
          return RestResponse.success();
      }
  }

画面 3：
- 展示了 PPT 页面，标题为“4.5.3 功能实现”，内容说明在 SmsService 类中定义 VerifySmsCode 方法以实现验证码功能。
- 代码片段：
  // 校验验证码
  @param key
  @param code

画面 4：
- 展示了 PPT 页面，标题为“3 API接口”，包含“3.1 发送短信验证码”和“3.2 校验短信验证码”两个小节。
- 3.1 节：访问路径为 http://localhost:56085/sailing / generate?effectiveTime=300&name=sms，JSON参数为 {"mobile": "15378791911"}。
- 3.2 节：访问路径为 http://localhost:56085/sailing / verify?name=sms & verificationKey=xxx & verificationCode=xxx，说明 verificationKey 和 verificationCode 分别表示校验标识和验证码。

画面 5：
- 展示了 SmsService 类中 verifySmsCode 方法的代码，其中包含参数 key 和 code。
- 代码片段：
  public void verifySmsCode(String key, String code) {
      if(smsEnable) {
          StringBuiler params = new StringBuilder("/verify?name=sms");
          params.append("&VerificationKey=").append(key).append("&VerificationCode=").append(code);
          RestResponse restResponse = OHttUtil.post(url, params.toString());
      }
  }

画面 6：
- 与画面 4 内容相同，为 PPT 页面“3 API接口”的“3.1 发送短信验证码”和“3.2 校验短信验证码”部分。

画面 7：
- 展示了 SmsService 类中 verifySmsCode 方法的代码，其中包含对 RestResponse 对象的判断。
- 代码片段：
  if(restResponse.getCode() != CommonErrorCodes.SUCCESS.getCode()) {
      throw new BusinessException(AccountErrorCodes.E_140152);
  }

画面 8：
- 展示了 RestResponse 类的代码，其中定义了 code、msg、result 字段，并提供了 success() 静态方法。
- 代码片段：
  package cn.ictast.wanning2p.common.domain;
  import ...
  @JsonInclude(Include.NON_NULL)
  @ApiModel(value = "RestResponse(T)", description = "响应通用参数(封装)")
  public class RestResponse<T> {
      @ApiModelProperty(value = "响应错误编码, 0为正常")
      private int code;
      @ApiModelProperty(value = "响应错误信息")
      private String msg;
      @ApiModelProperty(value = "响应内容")
      private T result;
      public static <T> RestResponse<T> success() { return new RestResponse<T>(); }
  }

画面 9：
- 展示了 SmsService 类中 verifySmsCode 方法的代码，其中包含对 RestResponse 对象的判断。
- 代码片段：
  if(restResponse.getCode() != CommonErrorCodes.SUCCESS.getCode()) {
      throw new BusinessException(AccountErrorCodes.E_140152);
  }

画面 10：
- 展示了 SmsService 类中 verifySmsCode 方法的代码，其中包含对 RestResponse 对象的判断。
- 代码片段：
  if(restResponse.getCode() != CommonErrorCodes.SUCCESS.getCode()) {
      throw new BusinessException(AccountErrorCodes.E_140152);
  }

画面 11：
- 展示了 SmsService 类中 verifySmsCode 方法的代码，其中包含对 RestResponse 对象的判断。
- 代码片段：
  if(restResponse.getCode() != CommonErrorCodes.SUCCESS.getCode()) {
      throw new BusinessException(AccountErrorCodes.E_140152);
  }

画面 12：
- 展示了 BusinessException 类的代码，其中定义了多个构造函数和 getErrorCode、setErrorCode 方法。
- 代码片段：
  public BusinessException(String arg0) { super(arg0); }
  public BusinessException(ErrorCode errorCode, String arg0) { super(arg0); }
  public BusinessException(Trowable arg0) { super(arg0); }
  public ErrorCode getErrorCode() { return errorCode; }
  public void setErrorCode(ErrorCode errorCode) { this.errorCode = errorCode; }

画面 13：
- 展示了 SmsService 类中 verifySmsCode 方法的代码，其中包含对 RestResponse 对象的判断。
- 代码片段：
  if(restResponse.getCode() != CommonErrorCodes.SUCCESS.getCode()) {
      throw new BusinessException(AccountErrorCodes.E_140152);
  }

画面 14：
- 展示了 SmsService 类中 verifySmsCode 方法的代码，其中包含对 RestResponse 对象的判断。
- 代码片段：
  if(restResponse.getCode() != CommonErrorCodes.SUCCESS.getCode()) {
      throw new BusinessException(AccountErrorCodes.E_140152);
  }

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
（已在上文要点中完整抄录）

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
（已在上文要点中完整写清）

5) 不要评价画面美观，不要输出与课程无关的内容。
（已遵守）

