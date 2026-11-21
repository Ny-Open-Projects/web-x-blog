# 16.商户注册-商户平台应用注册商户接口-接口实现

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day03 商户注册 短信验证接口
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day03 商户注册 短信验证接口\16.商户注册-商户平台应用注册商户接口-接口实现【海量资源尽在 666java.com】.mp4
- 时长 5分59秒（音频 359s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 下面呢我们再继续来编写商户平台应用注册商户的接口实现刚才我们完成了校验验证码的功能开发下面呢我们就可以将它远程调用double服务接口来将商户的数据呢写入数据库double服务的接口呢在之前我们已经写过了就是在merchant Service里边有一个接口这个接口呢就是create merchant这个呢大家应该还有印象对吧我们打开瞧一下
[00:28] 好那现在呢各位我们来看一下它需要的数据是DTO类型的数据而Controller呢它这是一个View虽然里边有相同的字段对吧但是呢Controller要做的是你要调用Double服务的接口你就要把数据给Double服务的接口呢提供它要的数据那怎么做呢你这是View它要的是DTO那怎么动那我们就定义一个DTO的对象吧对吧然后呢
[00:57] 这里边呢我们是不是就是像这个DTO当中写入这个商户注册的信息对不对然后呢你把它放进去是不是这么做啊那有时候老师你写啥呀那你注册的时候你有啥东西你就可以往里边写呀注册的时候他是不是就请求了一个其实手机号是不是得写进去其实当前阶段啊我们说只会向商户表写入数据但是后边还有啊还有账号嘞因为
[01:30] 你后边要接SaaS吗所以这里边呢你还要把账号也写进去对不对哎还有啥还有密码吧啊那这个也就是说他注册的时候所用到的数据都要去写吧对所以这里边呢你要注意你就需要写很多的数据啊我们先象征性的写一些啊我就点点点了回来了我们再去补那这个时候呢
[02:02] 我们是不是就把这个数据呢保存到商户信息当中大家看懂了吗那接下来呢接下来返回啥返回是不是一个叫注册的这个对象是不是就可以对这就是我们商户注册的一个实现我就写完了写完了这个实现呢我们是不是就可以来进行什么测试了吧好那我们来看一下吧那测试的话我们还用刚才Postman的这个接口
[02:32] 我们现在让他去请求是不是就可以看好啊这里边我们先打开数据库最终是不是以后把数据写到三户表啊三户表现在你看有吗有一个对吧那现在呢我们来写手机号啊看好啊123123123啊随便啊假的然后呢现在呢我们就走哎你看校验失败验证码校验失败了
[03:02] 这个验证码交易失败了我们是不是得重新再发一个验证码对不对再看这就是一个key然后我们把它写进去然后验证码你从哪拿其实专业的人员我们要做专业的事我们就可以直接用redis里面来拿了拿过来是不是走是不是没有返回老师为啥没有返回到底是成功不成功现在你看数据库就知道了
[03:37] 看一下没有吧对不对好这时候呢我们就来排错吧因为现在我们把代码写完了之后现在呢你一插入它没有返回对不对那怎么办我们得把程序重启一下吧不要着急重启一下很有可能我们刚才忘了重启程序或者啥然后一会打一个断点来测试一下好然后这里边呢我们就在这打断点然后呢我们再去请求一下可以吧执行
[04:07] 哎不好错了你看说没有提供可用的这么一个服务注意啊后面遇到这么一个错误就是我们要去调double服务的时候这个double服务要么是没有重启要么是服务没有提供所以这里边你不光要启动商户平台应用的工程你还要启动我们说的什么对double服务的这个工程好你把它起起来
[04:33] 好这个时候呢我们一起动double服务的话其实你可以通过Necros我们都可以来判定它这个服务到底有没有那当前你看一下它的服务列表你看一下当前你看它没有吗只有一个什么商户平台应用的服务所以等这个Necros里边有这个商户服务我们再看它应该就可以了这是不是就有了但是注意此时呢即使这里边有这个服务
[05:03] 那你可能有时候也需要稍等一会儿因为毕竟我们知道他要从服务注册中心来拿这个服务的实例他可能还稍微有一点延迟所以你再请求试一下就到这了到这就说明基本上是OK没有问题的那我们来看一下他这个注册的数据你看是不是已经返回过来了对返回过来之后这时候呢你再看数据库这个数据是不是就插进去了当然我们的手机号其实应该是写成功的
[05:32] 并且审核的状态是不是零到这儿你会发现这个商户就算注册成功了注册成功这个商户有时候老是这么多字段为空因为我们说了这些都是资质申请的时候我们要去干嘛填写的信息对好到这儿我们说商户平台应用写的商户注册接口以及测试就给大家写完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示商户注册功能的完整实现流程，包括 Controller 接口定义、Service 层业务逻辑、数据表结构、以及通过 Postman 调用接口并处理异常。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了课程章节“2.4.3.3 注册商户实现”，并显示了 Controller 层的 Java 代码。
- 代码内容：
  @Reference
  private MerchantService merchantService;
  @PostMapping("/merchants/register")
  public MerchantRegisterVO registerMerchant(@RequestBody MerchantRegisterVO merchantRegister){
      //校验验证码
      smsService.checkVerifyCode(merchantRegister.getVerifyKey(), merchantRegister.getVerifyCode());
      //注册商户
      MerchantDTO merchantDTO = new MerchantDTO();
      merchantDTO.setUserName(merchantRegister.getUserName());
      merchantDTO.setMobile(merchantRegister.getMobile());
      merchantDTO.setPassword(merchantRegister.getPassword());
      merchantService.createMerchant(merchantDTO);
      return merchantRegister;
  }

画面 2：
- 展示了 Service 层的 Java 代码，其中包含商户实体的插入操作。
- 代码内容：
  public Merchant createMerchant(MerchantDTO merchantDTO) {
      Merchant merchant = new Merchant();
      merchant.setMobile(merchantDTO.getMobile());
      //... 填入其它属性
      //审核状态为0未进行投资申请
      merchant.setAuditStatus("0");
      //操作员向数据库写入记录
      merchantMapper.insert(merchant);
      //有dto中写入新商户的id
      merchantDTO.setId(merchant.getId());
      return merchantDTO;
  }

画面 3：
- 展示了 Controller 层的 Java 代码，其中包含 @ApiOperation 注解和 @PostMapping 注解。
- 代码内容：
  @ApiOperation(value = "商户注册信息", name = "merchantRegisterVO", required = true, dataType = "MerchantRegisterVO")
  @PostMapping("/merchants/register")
  public MerchantRegisterVO registerMerchant(@RequestBody MerchantRegisterVO merchantRegisterVO) {
      //校验验证码
      smsService.checkVerifyCode(merchantRegisterVO.getVerifyKey(), merchantRegisterVO.getVerifyCode());
      //... 其它代码
  }

画面 4：
- 展示了 MerchantRegisterVO 类的属性列表，包括 setUserName、setMobile、setPassword、setVerifyCode、setVerifyKey 等方法。
- 代码内容：
  setUserName()
  setMobile()
  setPassword()
  setVerifyCode()
  setVerifyKey()
  getClass()
  Class<?> extends MerchantRegisterVO

画面 5：
- 展示了 Controller 层的 Java 代码，其中包含 @ApiOperation 注解和 @GetMapping 注解。
- 代码内容：
  @ApiOperation("测试")
  @GetMapping(path = "/hello")
  public String hello() { return "hello"; }

画面 6：
- 展示了数据库表 app 的结构，包含字段 ID、APP_ID、MERCHANT_ID、PUBLIC_KEY、NOTIFY_URL。
- 表结构：
  Columns (6)
  ID
  APP_ID
  MERCHANT_ID
  PUBLIC_KEY
  NOTIFY_URL
  Indexes (2)

画面 7：
- 展示了 Postman 中发送 POST 请求的 Body 部分，请求地址为 http://localhost:5010/merchant/merchants/register。
- 请求体内容：
  {
    "mobile": "123123123",
    "password": "123456",
    "username": "tccostest02",
    "verifyCode": "666666",
    "verifyKey": "sms:e9a478b1c0f445648e6bd795287c3a9ed34"
  }

画面 8：
- 展示了 Controller 层的 Java 代码，其中包含 @ApiOperation 注解和 @PostMapping 注解。
- 代码内容：
  @ApiOperation(value = "商户注册信息", name = "merchantRegisterVO", required = true, dataType = "MerchantRegisterVO")
  @PostMapping("/merchants/register")
  public MerchantRegisterVO registerMerchant(@RequestBody MerchantRegisterVO merchantRegisterVO) {
      //校验验证码
      smsService.checkVerifyCode(merchantRegisterVO.getVerifyKey(), merchantRegisterVO.getVerifyCode());
      //... 其它代码
  }

画面 9：
- 展示了 Controller 层的 Java 代码，其中包含 @ApiOperation 注解和 @PostMapping 注解。
- 代码内容：
  @ApiOperation("商户注册信息", name = "merchantRegisterVO", required = true, dataType = "MerchantRegisterVO")
  @PostMapping("/merchants/register")
  public MerchantRegisterVO registerMerchant(@RequestBody MerchantRegisterVO merchantRegisterVO) {
      //校验验证码
      smsService.checkVerifyCode(merchantRegisterVO.getVerifyKey(), merchantRegisterVO.getVerifyCode());
      //... 其它代码
  }

画面 10：
- 展示了 Spring Boot 启动日志，包含项目名称、端口号、以及服务注册信息。
- 日志内容：
  [project.name] {new.SERVER_PORT} 2020-12-28 16:32:28.154 WARN [Thread Pool Task Scheduler-1] (DubboServiceMetaRepository.java:114) - Current application name is: [project.name]

画面 11：
- 展示了 Controller 层的 Java 代码，其中包含 @ApiOperation 注解和 @GetMapping 注解。
- 代码内容：
  @ApiOperation("测试")
  @GetMapping(path = "/hello")
  public String hello() { return "hello"; }

画面 12：
- 展示了 Nacos 服务注册页面，显示服务名 merchant-application 已注册。
- 页面内容：
  服务列表 | dev | f58c3c1-4f05-4c0d-964a-c8444f42ab4
  服务名：merchant-application
  分组：DEFAULT_GROUP
  集群数：1
  实例数：1
  健康状态：1

画面 13：
- 展示了 Postman 中发送 POST 请求的 Body 部分，请求地址为 http://localhost:5010/merchant/merchants/register。
- 请求体内容：
  {
    "mobile": "123123123",
    "password": "123456",
    "username": "tccostest02",
    "verifyCode": "666666",
    "verifyKey": "sms:e9a478b1c0f445648e6bd795287c3a9ed34"
  }

画面 14：
- 展示了课程章节“2.4.4 MapStruct对象转换”，并显示了注册成功的提示。
- 代码内容：
  3. 注册成功
  2.4.4 MapStruct对象转换
  2.4.4.1 数据传输对象
  在商户注册并发过程中用于数据传输的对象有MerchantRegisterVO、MerchantDTO、entity(实体类)，它们的用途如下：

