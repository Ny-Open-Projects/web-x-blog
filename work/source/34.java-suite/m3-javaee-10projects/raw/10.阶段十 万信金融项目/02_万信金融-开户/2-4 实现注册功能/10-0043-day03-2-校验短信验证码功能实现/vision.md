# 画面线理解：day03-2-校验短信验证码功能实现

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day03-2-校验短信验证码功能实现_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:02, 01:11, 03:34, 04:42, 05:33, 06:29, 07:24, 08:48, 09:47, 10:29, 11:24, 11:51, 12:27, 13:25
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:28:28

1) 这一组画面整体在讲什么（一句话）：
在 wanning2p-account-service 项目中，实现短信验证码功能的前后端代码逻辑，包括发送和校验验证码的接口、服务层实现、统一响应封装及自定义异常处理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了项目结构目录，当前选中的是 wanning2p-account-service。
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
