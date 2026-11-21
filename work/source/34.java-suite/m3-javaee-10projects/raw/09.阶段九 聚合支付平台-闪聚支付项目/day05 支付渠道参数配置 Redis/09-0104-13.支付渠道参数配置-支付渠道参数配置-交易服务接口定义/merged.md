# 13.支付渠道参数配置-支付渠道参数配置-交易服务接口定义

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day05 支付渠道参数配置 Redis
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day05 支付渠道参数配置 Redis\13.支付渠道参数配置-支付渠道参数配置-交易服务接口定义【海量资源尽在 666java.com】.mp4
- 时长 8分30秒（音频 510s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,下面呢我们来实现交易服务支付渠道参数配置那么在前面呢我们已经完成了根据服务类型来查询它所对应的支付渠道那么这个画面呢大家看到这两个支付渠道一个是微信的一个是支付宝的那就是根据服务类型来查出来的支付渠道那么接下来呢我们就开始来点击后边的配置参数这个链接然后呢
[00:30] 它就会打开这个配置参数的表单那么在这里我们输入要配置的支付渠道的参数最终我们点击保存那么这样的话我们会把这个参数信息呢保存到我们的数据库具体是PayChannel下划线Param这个表当中大家看到了吗那么好那下面呢我们就来分析一下具体我们这个接口应该怎么写
[00:59] 刚才操作流程呢我给大家已经说过了最终啊其实就是要把这个表单这个信息保存到我们的这个PayChannel Param这张表中那么具体我们来看一下这个表呢它有这么多字段对吧那我们来看这些字段呢分别对应表单的哪个输入框来看一下啊首先这个配置名称啊它就正好对应
[01:28] 刚才看到的第一个输入框就这看到了吗那么下边这一堆呢注意点注意啊里边有点不太一样下边这一堆这都是微信这个支付接口所需要的参数这堆参数之前我给大家说了都需要去微信官方网站来拿这个参数对不对也就是啊这个商户在微信注册成功之后呢开通支付那微信呢就给他这些参数
[01:56] 那么这些参数你来看我们数据库呢其实是没有具体的字段和它对应的大家看所以这堆参数呢我们准备这么做除了配置名称和我们刚才表当中的这个配置名称对应这六个字段都需要前端把它格式化为json数据然后呢保存到我们这个支付渠道参数配置表的param字段中
[02:24] 大家看到这个字段是一个text的类型也就是大文本类型对不对那么有时候老师那前面的这些比如说商户ID这些支付渠道参数就是这些字段注意配置名称这是输入框填写的对吧这个商户ID是当前谁登录的系统那么也就是取出这个用户所属的商户ID这个商户ID大家应该不陌生因为原来我们写接口是不是都是从token当中来解析出来对不对
[02:55] 还有一个就是原始支付渠道编码就是说我们现在是给微信接口配参数还是支付宝接口配参数你看当你点击这个配参数的链接的时候其实这个参数都已经干嘛呀在这个表单上都已经有了也就是这个什么微信JS API这个参数懂吧这就是我们说的支付渠道对应我们刚才看到的这个表当中的这个叫原始支付渠道编码
[03:24] 支付参数刚才我说了是不是把表单的那堆填写的字段值然后格式我还为Jason然后保存到这里头对不对后面一个叫应用与服务类型的绑定ID这个也是需要我们自己去查出来的啥意思注意看首先你要知道整个的表单它是先选择了应用再选择了服务类型我说的没错吧
[03:52] 而现在我们这个表当中你会看到是不是需要一个应用服务类型绑定关系的这个ID也就是说你需要根据什么根据这里边我们一点保存提交到我们接口当中的应用和服务类型两个参数从我们的数据库当中来找到应用与服务类型的绑定ID
[04:18] 应用与服务类型的绑定ID是在这个APPPlatform Channel这张表中也就是这组件你把它找到了之后呢就填到这个参数配置表当中的这个什么就这个字段当中就行了所以根据刚才我们分析完了之后呢你会发现啊配置名称是需要在表单输入的然后呢这个param呢
[04:44] 也是需要表单输入的只不过Pyram呢它的格式呢是前端把它格式化为JSON数据然后传到这那么其他的呢都是不是表单输入的都需要提交接口的时候呢把数据提交过来那这个三户ID是从Token当中解析的对不对这个支付渠道编码呢是这个前端呢提交接口的时候把它提过来
[05:06] 那应用和服务类型绑定ID呢是前端提交的一个应用和服务类型我们呢需要根据这两个数据呢从这个应用服务类型绑定关系表当中找到这个组件我们把它保存到这张表就行了好了那么以上呢我们是不是就分析好了当它一点提交保存的时候呢这个数据如何保存到我们数据库的各个字段好了那么根据刚才我们的分析我们现在就可以写接口了那现在我们要写接口的话刚才我们说了吗需要提交哪些数据
[05:37] 需要提交应用服务类型还有配置名称还有一堆的param的参数对吧还有商户ID商户ID呢从token解析是吧好那现在呢我们来先写交易服务的接口看好啊那交易服务接口呢我们在哪里啊在交易服务的Service首先写API然后这里边呢我们首先在这儿来定义它的API接口对吧
[06:10] 那么这里边呢我们来看它需要什么参数呢我们看啊这里边讲义给出的是一个DTO类型看见了吗这个DTO类型呢是不是就正好对应于我们刚才看的支付渠道参数那个PayChannelParam的那张表是吧所以我们也用这个类型啊我们也用这个类型注意看啊那么好看一下我们这里面呢让它抛一个异常好那么如果配置失败我们再让它抛异常
[06:40] 如果成功的话这里面我们就外的啊什么就不用返回就证明配置成功了好那现在呢我们来写一下啊看好你别看这里面只有一个类型啊那我现在我的问题就来了首先这个接口呢是支付渠道参数配置对吧也就是说将来这个商户平台应用呢会掉这个double服务的接口对不对然后呢这个呢它包括了哪些信息啊这就是我们说的配置的支付渠道
[07:10] 参数对不对那这个配置的支付渠道参数包括啥首先我刚才说了嘛包括一个是应用的ID得有吧还有服务类型的code得有吧还有一个支付渠道参支付渠道的code对吧那另外刚才说了嘛这个商户的ID是不是从token解析啊所以这里边呢因为这是double接口对不对你double接口你是一定要把商户ID给我的
[07:39] 就是原来的这个商户平台应用http接口呢从talking解析到这个商户的ID那么你呢得给我所以这个是商户ID也得有商户ID应用ID服务类型code的字幕渠道然后后边就是配置名称以及配置参数刚才我说了配置参数是不是就是一个json数据啊对不对这就是我们说的什么这个接口的定义好
[08:04] 其实这里边这一堆数据非常重要啊你得知道这个接口呢我能拿到哪些数据然后呢你才知道我把这些数据呢怎么保存到数据库OK那么我们刚才呢把整个这个接口的定义呢我们就完成了其实我们在写接口定义之前我们已经也分析了啊这些数据怎么样最终保存到数据库啊后边呢我们再单独再来实现这个接口好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解如何在商户平台中为指定原始支付渠道配置参数，涉及数据库表结构、接口定义与实现代码。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示“交易服务支付渠道参数配置接口（接口⑦）”的前端页面，包含“应用设置”、“商户类型”、“支付参数”等选项卡，以及“配置参数”按钮。
画面2：在数据库管理工具中，展示 `pay_channel_param` 表的结构，包含字段如 `CHANNEL_NAME`、`MERCHANT_ID`、`PAY_CHANNEL`、`PARAM`、`APP_PLATFORM_CHANNEL_ID`。
画面3：在数据库管理工具中，展示 `pay_channel_param` 表的字段详情，其中 `PARAM` 字段类型为 `text NULL`，并有“支付参数”注释。
画面4：在数据库管理工具中，展示 `pay_channel_param` 表的字段详情，其中 `PARAM` 字段类型为 `text NULL`，并有“支付参数”注释。
画面5：展示课程PPT内容，标题为“5.4.4.1 接口定义”，描述“本接口是为应用配置支付渠道参数，前边为应用绑定了服务类型，此接口即为应用所绑定的服务类型配置支付渠道参数。”
画面6：在数据库管理工具中，展示 `app_platform_channel` 表的结构，包含字段如 `APP_ID`、`PLATFORM_CHANNEL`。
画面7：展示课程PPT内容，标题为“5.4.4.1 接口定义”，描述“本接口是为应用配置支付渠道参数，前边为应用绑定了服务类型，此接口即为应用所绑定的服务类型配置支付渠道参数。”
画面8：展示课程PPT内容，标题为“5.4.4.1 接口定义”，描述“本接口是为应用配置支付渠道参数，前边为应用绑定了服务类型，此接口即为应用所绑定的服务类型配置支付渠道参数。”
画面9：在IDE中展示 `PlatformParamController.java` 文件内容，包含 `@ApiOperation` 注解和 `queryPayChannelByPlatformChannel` 方法。
画面10：在IDE中展示 `PlatformParamController.java` 文件内容，包含 `@ApiOperation` 注解和 `queryPayChannelByPlatformChannel` 方法。
画面11：在IDE中展示 `PayChannelService.java` 文件内容，包含 `queryPayChannelByPlatformChannel` 方法。
画面12：在IDE中展示 `PayChannelParamDTO.java` 文件内容，包含 `@ApiModel` 注解和三个字段：`id`、`appId`、`platformChannelCode`。
画面13：展示课程PPT内容，标题为“5.4.4.2 接口实现”，描述“服务提供者一个接口实现支付渠道参数配置，如果该应用的服务类型已经配置呈支付渠道参数则执行更新操作，否则执行添加操作。”
画面14：展示课程PPT内容，标题为“5.4.4.2 接口实现”，描述“服务提供者一个接口实现支付渠道参数配置，如果该应用的服务类型已经配置呈支付渠道参数则执行更新操作，否则执行添加操作。”

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```sql
pc.*
platform_pay_channel ppc,
pay_channel pc,
platform_channel plc
WHERE pc.MERCHANT_ID = pc.MERCHANT_ID
AND ppc.PLATFORM_CHANNEL = plc.CHANNEL_CODE
AND plc.CHANNEL_CODE = 'ALI_PAY'
```

画面3：
```sql
Columns (6)
Field          Type               Comment
ID             bigint(20) NOT NULL
CHANNEL_NAME   varchar(50) NULL    渠道名称
MERCHANT_ID    bigint(20) NULL     商户ID
PAY_CHANNEL    varchar(50) NULL    支付渠道
PARAM          text NULL          支付参数
APP_PLATFORM_CHANNEL_ID bigint(20) NULL  应用平台渠道ID
```

画面4：
```sql
Columns (6)
Field          Type               Comment
ID             bigint(20) NOT NULL
CHANNEL_NAME   varchar(50) NULL    渠道名称
MERCHANT_ID    bigint(20) NULL     商户ID
PAY_CHANNEL    varchar(50) NULL    支付渠道
PARAM          text NULL          支付参数
APP_PLATFORM_CHANNEL_ID bigint(20) NULL  应用平台渠道ID
```

画面6：
```sql
Columns (3)
Field          Type               Comment
ID             bigint(20) NOT NULL
APP_ID         varchar(50) NULL    应用ID
PLATFORM_CHANNEL varchar(50) NULL  平台渠道
```

画面9：
```java
return payChannelService.queryPayChannelByPlatformChannel(
    @ApiOperation("模板服务类查询支付渠道", value = "服务")
    @GetMapping(value = "/my/pay/channel/platform-channel/plat!")
    List<PayChannelDTO> queryPayChannelByPlatformChannel(@PathVariable String platformChannelCode);
```

画面10：
```java
return payChannelService.queryPayChannelByPlatformChannel(
    @ApiOperation("模板服务类查询支付渠道", value = "服务")
    @GetMapping(value = "/my/pay/channel/platform-channel/plat!")
    List<PayChannelDTO> queryPayChannelByPlatformChannel(@PathVariable String platformChannelCode);
```

画面11：
```java
public class PayChannelService {
    @Override
    public List<PayChannelDTO> queryPayChannelByPlatformChannel(String platformChannelCode) {
        return payChannelRepository.queryPayChannelByPlatformChannel(platformChannelCode);
    }
}
```

画面12：
```java
package com.shanjiuy.transaction.api.dto;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

@ApiModel(value = "商户原始支付渠道参数配置", description = "商户原始支付渠道参数配置")
public class PayChannelParamDTO implements Serializable {
    @ApiModelProperty("参数配置id，新增时无用")
    private Long id;
    @ApiModelProperty("应用的appid，是业务id")
    private String appId;
    @ApiModelProperty("应用绑定的服务类型对应的code")
    private String platformChannelCode;
}
```

画面13：
```java
/**
 * 保存支付渠道参数
 * @param payChannelParam 商户原始支付渠道参数
 */
void savePayChannelParam(PayChannelParamDTO payChannelParam) throws BusinessException;
```

画面14：
```java
/**
 * 保存支付渠道参数
 * @param payChannelParam 商户原始支付渠道参数
 */
void savePayChannelParam(PayChannelParamDTO payChannelParam) throws BusinessException;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面5：
标题：5.4.4.1 接口定义
内容：本接口是为应用配置支付渠道参数，前边为应用绑定了服务类型，此接口即为应用所绑定的服务类型配置支付渠道参数。

画面13：
标题：5.4.4.2 接口实现
内容：服务提供者一个接口实现支付渠道参数配置，如果该应用的服务类型已经配置呈支付渠道参数则执行更新操作，否则执行添加操作。
示例：在 `PayChannelServiceImpl` 类中定义 `savePayChannelParam` 实现方法：
```java
@Autowired
private PayChannelParamMapper payChannelParamMapper;
```

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

