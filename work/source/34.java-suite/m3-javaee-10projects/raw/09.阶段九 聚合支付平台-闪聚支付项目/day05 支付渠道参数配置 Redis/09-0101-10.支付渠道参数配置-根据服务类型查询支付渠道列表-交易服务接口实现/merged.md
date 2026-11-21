# 10.支付渠道参数配置-根据服务类型查询支付渠道列表-交易服务接口实现

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day05 支付渠道参数配置 Redis
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day05 支付渠道参数配置 Redis\10.支付渠道参数配置-根据服务类型查询支付渠道列表-交易服务接口实现【海量资源尽在 666java.com】.mp4
- 时长 16分36秒（音频 997s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们继续来开发支付渠道参数配置那根据刚才我们系统设计啊我们说首先呢我们是要确定啊要向啊这个支付渠道参数表当中啊我们来插入参数对吧好那这里边呢我们说这张表呢我们是要知道啊是哪个商户啊然后呢是给哪个APP和哪个服务类型啊然后呢配支付渠道
[00:28] 就是这几个元素对不对好了那各位我们思考一下你知道像这个表擦了但是我们再回到我们之前啊进行业务分析的时候我们应该让大家看过这个具体的交互流程也就是说首先呢啊他把应用和服务类型绑定了之后呢在这儿看在这儿他会点击配置实际的支付渠道你看这个是不是就是我们说的服务类型啊对吧
[00:57] 当他一点这个服务类型这个时候才列出来我们说的什么支付渠道后边有一个配置参数是不是才开始配置参数所以我们知道当将来我们配置参数的时候就要把这个参数写到刚才老师给大家说的这张表当中但是在配置前你是不是需要把这个服务类型下边它所关联的什么支付渠道给查出来
[01:23] 大家懂我意思吗所以每个画面它所需要的数据呢都需要我们提供接口那好那么大家知道下边我要做的是这个页面的一个查询列表那么我们再回到第5.4小节我们应该做的事是什么呢就是要查询我们说的支付渠道那么根据什么来查吗我们说第三方支付渠道很多我们要根据什么
[01:50] 服务类型就是你当前这个应用你绑定了C扫币好那么我们就要根据C扫币这个服务类型来查出来C扫币它所对应的支付渠道由谁然后在后边你才能去配餐理解了吧好那下面我们再分析我要查某一个服务类型它所对应的什么支付渠道我怎么做
[02:18] 还回到系统设计这几张表各位你说我要从哪些表来查哪些表这是不是支付渠道这是不是服务类型服务类型和支付渠道的对应关系是不是在这看见了吗所以我们就知道了原来我们应该从什么从支付渠道和服务类型对应关系表来查询好看好我这个Circle语你看我怎么写看好也就是说现在我要查的是谁对我要查的是
[02:50] 服务类型和支付渠道服务类型和支付渠道它们对应关系而最终我要指定一个服务类型对吧指定一个服务类型那么这个服务类型呢看好这个服务类型是谁呢那么我要指定服务类型是C扫币看好C扫币在哪在这
[03:19] 各位这样我就查询出来这个服务类型下边有这两个支付渠道你告诉我这查询是不是这么长对但是你看这个界面原型上边我们看它似乎还有其他的元素你比如说这个支付渠道的名称看见了吗你刚才查的只是这个代码是不是页面上还要显示名称啊那页面上要显示名称的话你是不是就需要去干嘛
[03:49] 关联我们说的这个支付渠道表为啥因为支付渠道表当中有每个支付渠道的什么名称懂我意思吧所以现在呢我们就要来关联对这两张表那这两张表的关联怎么关联呢也就是这个
[04:14] 支付渠道和服务类型的关系表当中的这个支付渠道的代码要等于支付渠道当中的什么这个代码然后你就可以查询出什么名称了看见了吗对不对那么我们把这个名称查询出来之后呢接下来我们说是不是就可以给前端去展示了
[04:45] 再回到我们的讲义上看现在前端是不是需要一个支付渠道名称和支付渠道代码那我们是不是就可以对吧这个circle呢我们可以把这个数据呢返回给前端对不对嗯好那下面我们再来看我们还需要啊什么完善吗你看因为我们知道啊这个服务类型和支付渠道他们之间
[05:13] 这个是它的对应管理下面是不是支付渠道还差一个服务类型我建议你我建议你你也把服务类型关联一下有时候老是为啥呢因为假如说我们的页面上需要显示服务类型的名称的话那么刚才我们写那个cycle很显然是不够的懂吧所以我们为了可扩展性我们呢把这个服务
[05:41] 类型的这张表也让它干嘛也让它关联一下行吧那么这个看好我们把它写一下它们怎么关联这表比较复杂这个是PPC我就你看这个取第一个PPC行吗好 这是PC是吧这个是什么这个是PLA吧好 看好我开始写了首先我们说
[06:09] 这个PPC这张关系表要和这个支付渠道表关联那这个关系表呢也要和服务类型表关联也就是关系表分别和这两个表关联然后呢就可以让三张表进行关联对不对好那继续写啊PPC点这个是啥服务类型对吧然后等于谁服务类型服务类型的话呢就是PLA就它服务类型它的代码对吧
[06:39] 然后现在呢你再看再看看好啊哪里错了因为这个字段PPAL这个应该错了看这吧是不是啊那这个应该是谁啊这个是服务类型PLA好走你现在不是要指定服务类型吗对不对服务类型是他吧OK没有然后你把你这个信号我给你放开我让你瞧瞧你看
[07:14] 这是不是三张表的关联呀三张表的关联大家看到这是不是服务类型的名称这是不是服务类型对应的什么支付渠道他看懂了吗哎好这个Circle语句呢咱们就OK了你说老师你写Circle语句干啥因为你现在是不是要查询这个就是这个页面上边所需要的这些数据啊你最终是从数据库查嘛所以说我们先把Circle给他写出来好那下面呢我们就准备来定义这个接口吧
[07:45] 首先呢我们在交易服务当中来定义这个接口那大家思考这个接口参数这个接口的职责是干啥的就下面我要做啥事根据服务类型来查询它所对应的支付渠道下一步是不是就可以配置这个支付渠道参数了对不对好那服务类型我们是不是需要把它写进去就是这个platform channel code对吧好
[08:15] 那他返回什么呢返回啥你查出来几条记录你告诉我是不是两条是不是多条你要返回的是不是就是我们说的什么支付渠道对不对那所以说这里面你要让他返回一个什么支付渠道的DTO支付渠道DTO我们来找一下有没有支付渠道DTO要PayChannelDTO是不是就OK了
[08:45] 好这样的话我们就知道这个接口是根据服务的类型来查询支付渠道这个就是服务类型的什么代码这个就是我们说支付渠道的列表数据OK了吧好这个接口我们是不是就定义好了下面呢我们就开始接口实现那接口实现这一块的话很显然你这写了一个Service接口那我们
[09:15] 肯定要写一个Service的一个什么实现类这个是在交易服务暴露的一个double接口对吧好那么当然这里边想都不用想肯定是调Mapper对不对调用Mapper来查询数据库那我问你查询数据库查询我们数据库的哪些表刚才sql语句我查询了几张表对我要查询它对吧然后还有这个支付渠道还有这个服务类型
[09:45] 第一张表是不是就关系表这是支部渠道和服务类型的关系表这是支部渠道这是服务类型对不对好那我要查它关联查询那你用MapdeskPlus我跟你说啊它只是单表查对不对你要关联查询你就得自己写Circle语句自己写Circle语句咋写啊咋写你可以在这个Mapper当中去写你也可以干嘛你也可以自己干嘛
[10:15] 定义思考语句也就是说在这个参谋当中可以在这个麦块类当中可以来我们找一下我们现在要写的是什么呢是支付渠道和服务类型支付渠道和服务类型这个这是服务类型这是不是支付渠道表太长了刚开始你可能看着有点懵懵你要注意你现在不要看表明你就看啥你就看概念
[10:44] 服务类型支付渠道他们俩的关系对不对好在这我们准备在这写一个行不行好我在这写啥呢我就在这写一个叫做啥叫做服务根据服务类型来查询支付渠道行不行可以吧好那现在呢我们就准备在这写来看一下看一下你在这写可以
[11:14] 你在这个服务类型这写也行反正这个是你自定义的什么Mapper接口你在哪写都行懂啥意思吗所以说我们和讲义保持一致我们讲义上写的是在platform channel Mapper上来写这么一个方法那好那我们就跟讲义保持一致你在这个Mapper写行你在这也行因为都是自定义方法对不对好那现在呢我们要根据服务类型的代码
[11:44] 你是不是要传一个参数啊这就是platform code这是不是就是服务类型的代码你要让返回一个东西这个返回的数据是谁嘞啊返回的数据是不是就是我们刚才说的这个支付渠道的DTO就是我们Service定义的那个对吧关键的问题来了看好啊
[12:10] 这就是我们自定义的根据服务类型的code来查询它所对应的什么支付渠道它的信息对吧你怎么查我们说了吗你的Circle语句你看是不是写好了是不是它对啊怎么做对我们要自定义CircleSelectSelect那这里边呢我们就可以在这儿来把它写进去
[12:43] 懂吧就这么做我们把这个换行服给他干掉好那么这个circle呢我们就把它粘到了我们这个Mapper上边我们就可以让他来执行这个circle但是这个参数你要注意你可不能写死呀对不对这个参数要怎么写呢注意mybates给我们支持的我们用井号大口号我们学过mybates的时候应该都知道吧井号大口号传参
[13:11] 把这个参数传到这看懂了吧对这就是我们说的自定义Mapper的这个编写这样的话我们就可以在刚才我们写的Service里边我们就可以把它干嘛注进去刚才我们的那个什么那个Mapper对吧好现在把这个注进去之后呢我们是不是就可以怎么弄好像这个已经注进去了之前已经注过了然后我就可以来
[13:42] 调用它的方法怎么调用slag这是我们自定义的方法吧放进去OK了对不对嗯你说老师那这个怎么测一下呢这个我觉得我们完全可以进行什么单元测试是不是啊稍后呢我们进行一下单元测试好到这我们这个接口就写完了吧我们总结一下啊首先啊我们现在要做的就是要
[14:11] 根据我们的需求页面上边注意看我要根据服务类型来查出它所对应的支付渠道没错吧而服务类型和支付渠道的对应关系在这张表叫platform下滑线配下滑线channel这张表我们现在要做的是根据服务类型来查所以各位后边是不是有一个参数要输入服务类型的代码
[14:40] 对吧由于我们页面上边你看到了我们需要的不光是代码还有名称也就是支付渠道的名称对不对甚至还可能将来需要服务类型的名称也就是说我们建议你把这三张表关联这样的话这个信息的范围就非常的全看见吗这是支付渠道的名称这是服务类型对吧这是
[15:08] 有时候老是懵了懵了微信的就是支付渠道你看吧微信支付宝这些都是支付渠道对吧支付渠道谁与支付渠道对应服务类型我们散剧的都是服务类型散剧C扫币散剧C扫币散剧B扫C这些都是服务类型懂吗这是服务类型的编码对吧这些是支付渠道的代码
[15:31] 好仔细看看仔细慢慢的捋捋因为你初次接受这些概念我跟你说即使你说这个关系我听懂了但是一听这个什么各种服务类型什么支付渠道我就懵了不要着急你慢慢捋捋就OK了好了那我们是不是就把这个Circle语句就定义到了我们说的这个自定义Mapper当中这个自定义Mapper的方法大家需要掌握
[15:56] 因为你知道企业当中呢很多这种自定义的方式我们把社会语句放进去然后这里边传参MyBetisPlus这个警号搭口号我问你是MyBetisPlus给封中的当然不是的我们原来学过MyBetis嘛这是MyBetis提供的一个方法嘛传参是不是啊好然后呢在Service当中我们就让它去调用刚才我们的Mapper是不是传入了一个服务类型代码是不是就查出来了对这就是整个的什么整个的
[16:25] 交易服务所提供的一个根据服务类型来查询支付渠道列表也就是这次三张表关联查询的一个什么接口实现好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在支付系统中，通过查询服务类型与支付渠道的关联关系，实现根据服务类型获取原始支付渠道的功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：在数据库中查询 `pay_channel_param` 表，展示 `MERCHANT_ID`、`PAY_CHANNEL`、`PARAM`、`APP_PLATFORM_CHANNEL_ID` 字段数据，其中 `PAY_CHANNEL` 为 '223'，`PARAM` 为 'NULL'。
画面2：展示前端页面，步骤8为“请求交易服务获取列表”，步骤9为“返回结果给前端”，步骤10为“创建请求配置支付渠道参数”，页面中包含一个图片链接。
画面3：在数据库中执行 SQL 查询，查询结果为空。
画面4：展示 PPT 页面，标题为“5.4.2 交易服务原始支付渠道查询接口（接口⑤）”，内容说明配置参数页面会显示对应服务类型下的原始支付渠道，下方有“5.4.2.1 接口定义”小节，描述查询支付渠道以便下一步配置参数，并提示可从服务类型与支付渠道对应关系表查询。
画面5：在 IDE 中展示 `PlatformController.java` 代码，其中包含 `@PathVariable("appId") String appId` 和 `@RequestParam("platformChannelCode") String platformChannelCode` 参数，以及调用 `platformChannelService.queryAppBindPlatformChannel(appId, platformChannelCode)` 方法。
画面6：在 IDE 中展示 `PayChannelService.java` 接口定义，包含 `@RequestMapping` 注解和 `queryPayChannelByPlatformChannel` 方法签名。
画面7：在 IDE 中展示 `PayChannelServiceImpl.java` 代码，其中 `queryPayChannelByPlatformChannel` 方法体为空，仅返回 `null`。
画面8：在 IDE 中展示 `PayChannelService` 接口定义，包含 `queryPayChannelByPlatformChannel` 方法签名。
画面9：在 PPT 页面中展示 `queryPayChannelByPlatformChannel` 方法的实现，包含 SQL 查询语句。
画面10：在 IDE 中展示 `PlatformChannelMapper.java` 接口定义，包含 `selectPayChannelByPlatformChannel` 方法签名。
画面11：在 IDE 中展示 `PlatformChannelMapper.java` 接口定义，包含 `selectPayChannelByPlatformChannel` 方法的 SQL 查询语句。
画面12：在 IDE 中展示 `PayChannelServiceImpl.java` 代码，其中 `queryPlatformChannel` 方法体包含 `platformChannelMapper.selectList(...)` 调用。
画面13：展示 PPT 页面，标题为“5.4.2.1 接口定义”，内容包含三个表结构图：`pay_channel`（支付渠道）、`platform_channel`（服务类型）和 `platform_channel_pay_channel`（服务类型与支付渠道对应关系表），并用箭头表示三者之间的关联关系。
画面14：展示 PPT 页面，标题为“5.4.2.1 接口定义”，内容与画面13相同，但页面中鼠标指针位于“服务类型”表结构图上。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
无代码或配置内容。

画面2：
无代码或配置内容。

画面3：
无代码或配置内容。

画面4：
无代码或配置内容。

画面5：
```java
@GetMapping("/platformChannel")
public String queryPlatformChannel(@PathVariable("appId") String appId,
                                   @RequestParam("platformChannelCode") String platformChannelCode) {
    return platformChannelService.queryAppBindPlatformChannel(appId, platformChannelCode);
}
```

画面6：
```java
// 根据绑定服务类型的参数
@RequestMapping("/platformChannel")
public List<PayChannelDTO> queryPayChannelByPlatformChannel(String appId, String platformChannelCode) {
    return platformChannelMapper.selectPayChannelByPlatformChannel(platformChannelCode);
}
```

画面7：
```java
@Override
public List<PayChannelDTO> queryPayChannelByPlatformChannel(String appId, String platformChannelCode) {
    return null;
}
```

画面8：
```java
// 根据服务类型查询支付渠道
@Override
public List<PayChannelDTO> queryPayChannelByPlatformChannel(String platformChannelCode) {
    return null;
}
```

画面9：
```java
// 根据平台服务类型获取原始支付渠道
@Override
public List<PayChannelDTO> queryPayChannelByPlatformChannel(String platformChannelCode) {
    return platformChannelMapper.selectPayChannelByPlatformChannel(platformChannelCode);
}
```

画面10：
```java
// Mapper 接口
@Mapper
public interface PlatformChannelMapper extends BaseMapper<PlatformChannel> {
    List<PayChannelDTO> selectPayChannelByPlatformChannel(String platformChannelCode);
}
```

画面11：
```java
// 根据服务类型code查询对应的支付渠道
@Override
public List<PayChannelDTO> selectPayChannelByPlatformChannel(String platformChannelCode) {
    return platformChannelMapper.selectPayChannelByPlatformChannel(platformChannelCode);
}
```

画面12：
```java
@Autowired
PlatformChannelMapper platformChannelMapper;

@Autowired
AppPlatformChannelMapper appPlatformChannelMapper;

// 查询平台的服务类型
@Override
public List<PlatformChannel> queryPlatformChannel() throws BusinessException {
    List<PlatformChannel> platformChannels = platformChannelMapper.selectList(new QueryWrapper<PlatformChannel>().eq("platform_code", "shanjuy"));
    return platformChannels;
}
```

画面13：
无代码或配置内容。

画面14：
无代码或配置内容。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面4：
标题：5.4.2 交易服务原始支付渠道查询接口（接口⑤）
内容：配置参数页面会显示对应服务类型下的原始支付渠道。
子标题：5.4.2.1 接口定义
内容：这里是查询交易服务类型下的支付渠道，以便下一步为某支付渠道配置参数。可从服务类型与支付渠道对应关系表查询。

画面13：
标题：5.4.2.1 接口定义
内容：这里是查询交易服务类型下的支付渠道，以便下一步为某支付渠道配置参数。可从服务类型与支付渠道对应关系表查询。
架构图：
- 三个表结构图：
  - `pay_channel`（支付渠道）：包含字段 ID、CHANNEL_NAME、CHANNEL_CODE。
  - `platform_channel`（服务类型）：包含字段 ID、CHANNEL_NAME、CHANNEL_CODE。
  - `platform_channel_pay_channel`（服务类型与支付渠道对应关系）：包含字段 ID、PLATFORM_CHANNEL、PAY_CHANNEL。
- 箭头关系：
  - `pay_channel` 表指向 `platform_channel_pay_channel` 表。
  - `platform_channel` 表指向 `platform_channel_pay_channel` 表。
  - `platform_channel_pay_channel` 表指向 `pay_channel` 表。
  - `platform_channel_pay_channel` 表指向 `platform_channel` 表。
- 文字说明：
  - 服务类型与支付渠道对应关系：多对多。
  - 一种服务类型可以绑定多个支付渠道。
  - 一个支付渠道可以绑定多种服务类型。

画面14：
标题：5.4.2.1 接口定义
内容：这里是查询交易服务类型下的支付渠道，以便下一步为某支付渠道配置参数。可从服务类型与支付渠道对应关系表查询。
架构图：
- 三个表结构图：
  - `pay_channel`（支付渠道）：包含字段 ID、CHANNEL_NAME、CHANNEL_CODE。
  - `platform_channel`（服务类型）：包含字段 ID、CHANNEL_NAME、CHANNEL_CODE。
  - `platform_channel_pay_channel`（服务类型与支付渠道对应关系）：包含字段 ID、PLATFORM_CHANNEL、PAY_CHANNEL。
- 箭头关系：
  - `pay_channel` 表指向 `platform_channel_pay_channel` 表。
  - `platform_channel` 表指向 `platform_channel_pay_channel` 表。
  - `platform_channel_pay_channel` 表指向 `pay_channel` 表。
  - `platform_channel_pay_channel` 表指向 `platform_channel` 表。
- 文字说明：
  - 服务类型与支付渠道对应关系：多对多。
  - 一种服务类型可以绑定多个支付渠道。
  - 一个支付渠道可以绑定多种服务类型。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求完成）

