# 07.支付渠道参数配置-应用绑定服务类型-测试

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day05 支付渠道参数配置 Redis
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day05 支付渠道参数配置 Redis\07.支付渠道参数配置-应用绑定服务类型-测试【海量资源尽在 666java.com】.mp4
- 时长 4分1秒（音频 241s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好刚才呢我们完成了应用绑定服务类型接口的开发下面呢我们来测试一下这个接口那么要测试呢我们首先需要把交易服务呢重启一下然后呢再把我们的商户平台应用重启一下好那么我们再回到讲义上来我们来看一下当前我们要做的是什么事呢我们现在要做的话就是要首先呢我们测试的是一个什么呀
[00:30] 就是应用和一个服务类型的绑定对吧所以我们传参是传两个参数一个应用的ID一个是服务类型的code好当它起来之后呢我们来看一下我们的Swagger看一下然后呢这个Swagger这里边呢有一个叫做什么叫做渠道和支付参数相关的好我们刚才应该是这个这个就是绑定服务类型对吧好
[00:56] 那现在呢我们准备在Postman当中来把这个接口测试一下好那么我们新建一个request新建一个request然后这里边呢我们叫绑定应用绑定服务类型对吧好那么这个呢是我看一下啊是Post对吧然后这个是它的这个URL嗯那它前边的这个呢我们从其他地方呢拷一个就行了然后放到前头对吧
[01:32] 那这里边呢我们要怎么设置这个参数呢这个是不是就是一个通过pass来传应用ID通过pass传应用ID的话应用大家需要从数据库找一个应用这个应用IDAPPID对吧然后呢你把它拿到这儿而后边我们要绑定的这个什么服务类型的代码的话你注意看它的参数名然后看啊这是这个咱们写的Controller接口啊应该是它对吧所以这里边呢我们应该在用问号就是用query的方式来传
[02:03] 那么它等于什么呢就是服务类型我们系统当中的服务类型有这么多假如我们让它绑一个散聚下滑线C扫B这个服务类型那么你应该把它填进去大家看懂了吗对好那下边我要做的事是不是就要进行测试了因为它没有一个返回值只要你执行成功我们说http是不是返回200
[02:30] 所以前段就认为绑定成功如果是500就认为错误对吧所以这里边我准备在最后Service double服务接口这儿我打一个断点我跟他只要他能执行完成就认为OK好那下面我们执行那么就到这一步他首先现在应用和服务类型是没绑定的所以他肯定进去了大家看到了吗最后是不是执行了一个插入操作那么执行一个插入操作有时候老师怎么为之错误了
[03:00] 那你先不要着急你先看数据库就应用和服务类型的一个绑定你是不是已经插进去了因为之前我也说过这个是打断点嘛断点的话这里面有一个什么有一个超时时间就是接口调用超时时间他可能报了一个错那现在我们再执行其实这时候他怎么执行他都会成功为什么因为他已经绑定成功了所以他不会再往里边插新的记录了大家看懂了吗对如果说你说我把它删掉了那这时候相当于这个应用和服务类型没有绑定所以这时候呢你再执行
[03:30] 它又会把它给插进去这就是我们说的应用绑定服务类型是不是就成功了也就是当你点开启服务的时候呢就会在后台执行刚才咱们这个接口好那么以上呢就是我们说的应用绑定服务类型的测试咱们就完成了那这个功能完成之后呢应该说应用绑定服务类型就成功了最终会写到APP Platform Channel这张表当中
[04:00] 好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过代码定义接口、使用 Swagger 查看 API 文档、并在 Postman 中调用接口，最终在数据库中验证数据插入结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 显示 Typora 文档，内容为 Java 代码，定义了 `AppController` 类中的 `bindPlatformForApp` 方法。
- 代码内容：
  ```java
  @Reference
  private PayChannelService payChannelService;

  @ApiOperation("绑定服务类型")
  @PostMapping(value="/my/apps/{appId}/platform-channels")
  @ApiImplicitParams({
  @ApiImplicitParam(value = "应用ID", name = "appId", dataType = "string", paramType = "path"),
  @ApiImplicitParam(value = "服务类型code", name = "platformChannelCodes", dataType = "string", paramType = "query")
  })
  public void bindPlatformForApp(@PathVariable("appId") String appid,
  @RequestParam("platformChannelCodes") String platformChannelCodes){
  payChannelService.bindPlatformChannelForApp(appid,platformChannelCodes);
  }
  ```

画面 2：
- 鼠标悬停在文档目录结构中的“5.4.1 系统设计”条目上，但未点击。
- 未显示任何代码或配置。

画面 3：
- 鼠标悬停在文档目录结构中的“5.4.1 交易服务绑定服务类型接口”条目上。
- 未显示任何代码或配置。

画面 4：
- 显示 Swagger UI 页面，标题为“闪聚支付-商户应用API文档 1.0.0”。
- 页面显示了 API 接口列表，包括：
  - POST `/my/apps/{appId}/platform-channels`
  - GET `/my/platform-channels`

画面 5：
- 显示 Postman 的“Create New”界面，提示用户可以创建请求、集合、环境等。

画面 6：
- 显示 Postman 的“Collections”界面，左侧列出了多个请求，右侧是“POST”请求的编辑区。
- 未填写 URL 和参数。

画面 7：
- 在 Postman 中，URL 已填写为 `http://localhost:57010/merchant/my/apps/...`。
- 未填写任何请求头或参数。

画面 8：
- 显示数据库管理工具（可能是 Navicat），连接到 `shanjupay_transaction` 数据库。
- 当前查看的表是 `app`，显示了一条记录，其中 `APP_ID` 为 `abcceddd-3032-48a6-9691-4770e66577af`，`MERCHANT_ID` 为 `1211220010036162226`。

画面 9：
- 显示 IntelliJ IDEA 的代码编辑器，打开的是 `PlatformChannelController.java` 文件。
- 代码内容：
  ```java
  @ApiImplicitParams({
  @ApiImplicitParam(value = "应用ID", name = "appId", required = true, dataType = "String"),
  @ApiImplicitParam(value = "服务类型code", name = "platformChannelCodes", required = true, dataType = "String")
  })
  @PostMapping(value="/my/apps/{appId}/platform-channels")
  public void bindPlatformForApp(@PathVariable("appId") String appid,
  @RequestParam("platformChannelCodes") String platformChannelCodes){
  payChannelService.bindPlatformChannelForApp(appid,platformChannelCodes);
  }
  ```

画面 10：
- 显示 Postman 中的“Sending...”状态，表示请求正在发送。
- 未显示任何响应数据。

画面 11：
- 显示 IntelliJ IDEA 的代码编辑器，打开的是 `PayChannelServiceImpl.java` 文件。
- 代码内容：
  ```java
  //根据应用ID和平台类型code查询，如果已经绑定则不再插入，否则插入记录
  AppPlatformChannel appPlatformChannel = appPlatformChannelMapper.selectOne(new LambdaQueryWrapper<AppPlatformChannel>().eq(AppPlatformChannel::getAppId, appId).eq(AppPlatformChannel::getPlatformChannelCode, platformChannelCodes));
  if(appPlatformChannel == null) {
  //平台渠道实体
  AppPlatformChannel entity = new AppPlatformChannel();
  entity.setAppId(appId); //应用ID
  entity.setPlatformChannel(platformChannelCodes); //服务类型code
  appPlatformChannelMapper.insert(entity);
  }
  ```

画面 12：
- 显示数据库管理工具，连接到 `shanjupay_transaction` 数据库。
- 当前查看的表是 `app_platform_channel`，显示了一条记录，其中 `APP_ID` 为 `abcceddd-3032-48a6-9691-4770e66577af`，`PLATFORM_CHANNEL` 为 `kangyu_25`。

画面 13：
- 显示数据库管理工具，连接到 `shanjupay_transaction` 数据库。
- 当前查看的表是 `app_platform_channel`，显示了一条记录，其中 `APP_ID` 为 `abcceddd-3032-48a6-9691-4770e66577af`，`PLATFORM_CHANNEL` 为 `kangyu_25`。

画面 14：
- 显示数据库管理工具，连接到 `shanjupay_transaction` 数据库。
- 当前查看的表是 `app_platform_channel`，显示了一条记录，其中 `APP_ID` 为 `abcceddd-3032-48a6-9691-4770e66577af`，`PLATFORM_CHANNEL` 为 `kangyu_25`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
见上文第 2 点中各画面的代码内容。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
- PPT 标题：在画面 1、2、3 中显示为“5.3.5.2 接口测试”。
- Swagger UI 页面标题：在画面 4 中显示为“闪聚支付-商户应用API文档 1.0.0”。
- 表格数据：在画面 8、12、13、14 中显示了数据库表 `app` 和 `app_platform_channel` 的数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
已按要求输出。

