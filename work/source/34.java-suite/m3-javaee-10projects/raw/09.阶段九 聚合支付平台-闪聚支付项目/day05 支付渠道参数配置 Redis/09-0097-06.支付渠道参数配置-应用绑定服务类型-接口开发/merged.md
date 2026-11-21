# 06.支付渠道参数配置-应用绑定服务类型-接口开发

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day05 支付渠道参数配置 Redis
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day05 支付渠道参数配置 Redis\06.支付渠道参数配置-应用绑定服务类型-接口开发【海量资源尽在 666java.com】.mp4
- 时长 10分59秒（音频 659s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,下面我们继续来实现应用绑定服务类型那么接下来我们就开始来实现应用绑定服务类型的具体接口前边我们只是查询了平台所有的服务类型那么在这个界面当中大家看当点击开启服务的时候就开始执行绑定因为我们知道在当前的这个页面上面其实是已经选定了一个应用
[00:27] 当选择某一个服务类型点击开启的时候就相当于这个应用呢和这个服务类型做了一个绑定那最终绑定成功之后呢他们的关系呢会写到这个服务类型和应用的一个什么关系表当中那我们找到这个表在这就是APPPlatform Channel就它好那下面呢我们知道了这个具体的
[00:52] 需求我们现在就开始来定义接口还是我们首先在交易服务定义然后呢在商户平台应用当中来写交易服务里边定义的接口呢是暴露一个double服务对吧好那下面呢我们准备在哪里啊打开交易服务首先呢在交易服务的API当中我们在这儿来定义一个刚才我们说了它是一个什么呀是不是就应用绑定服务类型啊应用绑定服务类型我们说需要几个参数啊你思考一下需要几个参数啊
[01:25] 再回到界面注意看在这个界面当中应该是这个界面上一个界面首先选择的是应用也就是来到这个界面这儿就已经确定了一个应用了当选择开启服务当点击开启服务这时候呢它和它就开始绑定也就是说一个应用和一个服务进行绑定所以这个接口我们应该给它传入一个应用的ID和一个什么一个服务类型的标识
[01:55] 懂吧好了那现在呢应用的ID好传对吧那服务类型我们来看在哪服务类型在哪告诉我是不是就是这个platform channel那么用ID还是用code呢注意我们后边的统统都是用的这个code我们不用ID啊因为这个code就是我们系统的一个配置的一个参数啊固定死的不会改这就叫散句杠这个叫C2B也就是C扫B的意思
[02:24] 包这个B扫C好那下边呢我们就在这个接口当中啊准备来定义我们的参数两个参数吧一个是应用的ID一个是服务类型的什么code好那这个服务类型的这个参数有点长注意看这个plateformchannelcode后边有个S好那前边呢我们说最终绑定成功之后各位如果抛一场是不是就绑定不成功对吧如果绑定成功那就这个方法执行
[02:58] 成功所以我们让它返回一个外的就行这就是为应用为某个应用绑定服务类型绑定一个服务类型这我写的够明确了吧好这就是我们说的应用的ID这就是我们的服务类型的codeOK了吧好那接下来呢我们在Service当中来把这个给它完善一下好了那各位我们思考一下
[03:29] 怎么样像我们说的应用和服务类型他们之间的关系表我们是不是要插入什么呀是不是要插入记录了好注意看啊那么你要插入记录你现在插的是谁是不是就是应用和服务类型的关系表啊那表有点名字有点长啊刚开始我还是说的大家呢可能不太习惯慢慢又好了叫应用服务类型关系APP Platform Channel Map
[03:59] 这就是应用和服务类型的一个关系的买卖好那下面呢我们要插怎么插怎么插各位看就这张表就它是吧有个组件组件不用你管对吧但是有一点啊你要确定这个应用和这个服务类型是不是已经绑定如果说它已经绑定了就不要再插了如果没有绑定再插入所以我们的逻辑应该是先根据应用的ID和什么服务类型的
[04:31] code来查询对吧如果已经绑定则不再插入对吧否则插入记录懂我意思吧好那我们首先要查询嘛怎么查看一下啊select那这里边呢我们是不是就可以来查询一下select查哪个都行你是select count呀select one呢是不是都可以呀对不对
[05:03] 好那我们呢就让他查询一个select one我们查一个记录如果他为空我们就认为他没有绑定我们就查入行不行好再来one那么你有一个lambda然后这个是一个条件的一个rever好然后呢这个表是不是对应了我们app platform channel嗯好然后呢那现在我们要根据应用的ID和服务类型的code对不对所以这里边注意看啊
[05:34] 应用的ID是不是它这是一个了对不对好然后呢继续还有我们要根据除了应用的ID还有啥是不是服务类型的code看起来就看起来眼花了对不对服务类型就是这个platform channel就它然后呢就是把这个写上去各位这就得到了我们查的一条记录
[06:05] 刚开始对表不熟悉慢慢来不着急然后这里边呢我们是不是就可以来判断如果它为空各位我们是不是这个时候才开始插入啊这个时候是不是向哪个表插入啊像我们说的应用服务类型的什么啊关系表来插就这张表嗯好那现在呢我们就准备向它插入一条记录插入记录的话我们是不是首先需要嗯构造一个东西啊
[06:34] 一个我们说的应用服务类型对吧这这是不是就相当于一个NT对不对然后另一个应用服务类型那这里边呢我们要往里边放东西了首先第一个是APP ID关系啊一个应用ID一个是服务类型code放进去这是不是就是我们说的应用ID好还有一个就是我们说的服务类型的code就它对对吧
[07:07] 好那这样的话我们是不是就可以来让他调用这个Mapper insert这个接口各位就完工了是吧增三改我建议你加一个transaction好OK那么这个是交易服务提供的一个叫绑定服务类型的接口那最终前端请求的是交易我们说的商户平台吗商户平台要http接口暴露对吧然后调用我们刚才的交易服务接口好那现在呢我们是不是要
[07:38] 来再来一个接口这个接口我们要转到哪里转到商户平台的应用工程在这那么好这个是不是就是我们说的要做一件应用绑定服务类型的一个接口对吧那好那它传参传什么参大家思考传什么参我觉得跟刚才应该是我们写这个double接口差不多
[08:07] 也是要有一个什么呀应用ID对不对还有一个什么呀服务类型的code对吧好那这两个呢我们都让它传进去没错吧好那么我们再看那么最后返回啥呢如果啥也不返回如果是正常成功那么就认为绑定成功对不对如果说它没有返回但是它报错了
[08:39] 对吧但是方法执行成功是200如果是报了500错误那这一事就绑定失败前段呢就开始跑一场就开始报一个错绑定失败好现在呢有几个参数我们看一下啊有几个参数这几个参数我们先把这个URL写进去你注意看啊注意看这是不是URL啊那我好好现在根据这个呢我让你写这个Swagger它的文档的参数这么多这个是通过pass传所以你这里面想都不用想直接加pass variable
[09:12] 对不对没错吧那还有呢这个不是通过帕斯传吗这是不是通过我们说的这个什么request param这个这个把它标记一下这个我们说的这个参数OK吧好那这呢是不是有一堆的我们说的这个sweager文档的这个对不对sweager文档怎么写要求大家会写的啊一定注意这是我们说的应用的ID
[09:46] 还有一个内幕内幕是谁内幕是不是就是他他是否必填呢必填他是什么类型呢字符串对吧那他传传的方式呢pass懂吧一定要会写这个东西啊好然后继续接着写后边这个这是我们说的服务类型的代码对吧那这个就是叫啥叫服务类型的代码code
[10:20] 对吧然后呢他是他那他是B田B田那他也是个字符串那这个呢就可不是pass了啊注意他将来是在问号后边来传所以这里面要改成谁Horray大家看懂了吧对好那下面呢我们就直接让他调用这个方法就行了我们就把他绑进去了好那各位我们到这儿是不是就完成了这个接口的编写呀
[10:54] 完成了之后呢我们稍后呢来进行测试一下好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中，通过定义接口、实现类和控制器，完成商户平台绑定支付渠道的业务逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示数据库表 `platform_channel` 的数据，包含 ID、CHANNEL_NAME、CHANNEL_CODE 字段，用于存储平台支付渠道信息。
画面 2：在 IDE 中查看 `PayChannelService.java` 接口定义，包含 `queryPlatformChannel()` 方法，用于查询平台渠道。
画面 3：在 IDE 中查看 `PayChannelService.java` 接口定义，展示 `bindPlatformChannelForApp()` 方法的签名。
画面 4：在 IDE 中弹出“Select Methods to Implement”对话框，提示需要实现 `bindPlatformChannelForApp` 方法。
画面 5：在 IDE 中查看 `PayChannelServiceImpl.java` 文件，展示 `queryPlatformChannels` 方法的实现，调用 `platformChannelMapper.selectList`。
画面 6：在 Typora 中查看文档，展示 `PayChannelServiceImpl.java` 文件的代码，包含 `bindPlatformChannelForApp` 方法的实现，使用 `LambdaQueryWrapper` 查询并创建 `AppPlatformChannel` 实体。
画面 7：在 IDE 中查看 `PayChannelServiceImpl.java` 文件，展示 `LambdaQueryWrapper` 的链式调用，用于查询平台渠道。
画面 8：展示数据库表 `app_platform_channel` 的结构，包含 APP_ID、PLATFORM_CHANNEL 字段。
画面 9：在 IDE 中查看 `PayChannelServiceImpl.java` 文件，展示 `bindPlatformChannelForApp` 方法的实现，包含创建 `AppPlatformChannel` 实体并设置属性的代码。
画面 10：在 Typora 中查看文档，展示 `PlatformController.java` 中 `bindPlatformForApp` 方法的定义，包含 `@ApiImplicitParams` 注解。
画面 11：在 IDE 中查看 `PlatformController.java` 文件，展示 `bindPlatformForApp` 方法的定义，包含 `@PostMapping` 注解。
画面 12：在 IDE 中查看 `PlatformController.java` 文件，展示 `@ApiImplicitParams` 注解的定义，包含 `appID` 和 `platformChannelCodes` 参数。
画面 13：在 IDE 中查看 `PlatformController.java` 文件，展示 `bindPlatformForApp` 方法的完整实现，包含 `@PostMapping` 和 `@ApiImplicitParams` 注解。
画面 14：在 IDE 中查看 `PlatformController.java` 文件，展示 `bindPlatformForApp` 方法的完整实现，包含 `@ApiOperation` 注解和方法体。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```sql
ID	CHANNEL_NAME	CHANNEL_CODE
1	支付宝	alipay
2	微信支付	wx_native
3	银联支付	UnionPay
4	支付宝	ali_pay
```

画面 2：
```java
public interface PayChannelService {
    @Return
    @Throws BusinessException
    List<PlatformChannelDTO> queryPlatformChannel() throws BusinessException;
    void bindPlatformChannelForApp(String appid, String platformChannelCodes) throws BusinessException;
}
```

画面 3：
```java
public interface PayChannelService {
    @Return
    @Throws BusinessException
    List<PlatformChannelDTO> queryPlatformChannel() throws BusinessException;
    void bindPlatformChannelForApp(String appid, String platformChannelCodes) throws BusinessException;
}
```

画面 4：
```java
void bindPlatformChannelForApp(String appid, String platformChannelCodes) throws BusinessException;
```

画面 5：
```java
public List<PlatformChannelDTO> platformChannels = platformChannelMapper.selectList(null);
```

画面 6：
```java
import com.shanju.pay.transaction.entity.AppPlatformChannel;
import com.shanju.pay.transaction.Mapper.AppPlatformChannelMapper;
import org.apache.dubbo.config.annotation.Service;
import org.springframework.beans.factory.annotation.Autowired;
import java.util.ArrayList;
import java.util.List;

@Service
public class PayChannelServiceImpl implements PayChannelService {

    @Autowired
    private AppPlatformChannelMapper appPlatformChannelMapper;

    @Override
    @Transactional
    public void bindPlatformChannelForApp(String appid, String platformChannelCodes) throws BusinessException {
        //根据appid和平台服务类型code查询app_platform_channel
        AppPlatformChannel appPlatformChannel = appPlatformChannelMapper.selectOne(new LambdaQueryWrapper<AppPlatformChannel>()
                .eq(AppPlatformChannel::getAppId, appid)
                .eq(AppPlatformChannel::getPlatformChannelCode, platformChannelCodes));
        if (appPlatformChannel == null) {
            AppPlatformChannel entity = new AppPlatformChannel();
            entity.setAppId(appid);
            entity.setPlatformChannelCode(platformChannelCodes);
            entity.setPlatformChannelName(platformChannelName);
            appPlatformChannelMapper.insert(entity);
        }
    }
}
```

画面 7：
```java
LambdaQueryWrapper<AppPlatformChannel> wrapper = new LambdaQueryWrapper<AppPlatformChannel>();
wrapper.eq(AppPlatformChannel::getAppId, appid)
       .eq(AppPlatformChannel::getPlatformChannelCode, platformChannelCodes);
```

画面 8：
```sql
APP_ID	PLATFORM_CHANNEL
```

画面 9：
```java
if (appPlatformChannel == null) {
    AppPlatformChannel entity = new AppPlatformChannel();
    entity.setAppId(appid);
    entity.setPlatformChannelCode(platformChannelCodes);
    entity.setPlatformChannelName(platformChannelName);
    appPlatformChannelMapper.insert(entity);
}
```

画面 10：
```java
@ApiImplicitParams({
    @ApiImplicitParam(value = "应用ID", name = "appid", required = true, dataType = "String"),
    @ApiImplicitParam(value = "服务类型code", name = "platformChannelCodes", required = true, dataType = "String")
})
```

画面 11：
```java
@PostMapping("/my/apps/{appid}/platform-channels")
void bindPlatformForApp(@PathVariable("appid") String appid, @RequestParam("platformChannelCodes") String platformChannelCodes) {
```

画面 12：
```java
@ApiImplicitParams({
    @ApiImplicitParam(value = "应用ID", name = "appid", required = true, dataType = "String"),
    @ApiImplicitParam(value = "服务类型code", name = "platformChannelCodes", required = true, dataType = "String")
})
```

画面 13：
```java
@PostMapping("/my/apps/{appid}/platform-channels")
void bindPlatformForApp(@PathVariable("appid") String appid, @RequestParam("platformChannelCodes") String platformChannelCodes) {
```

画面 14：
```java
@ApiOperation(value = "商户平台-渠道和支付参数相关", tags = {"商户平台-渠道和支付参数"}, description = "商户平台-渠道和支付参数")
public class PlatformParamController {

    @ApiOperation("获取平台服务类型")
    @GetMapping("/my/platform-channels")
    public List<PlatformChannelDTO> queryPlatformChannel() {
        return payChannelService.queryPlatformChannel();
    }

    @ApiOperation("绑定服务类型")
    @PostMapping("/my/apps/{appid}/platform-channels")
    void bindPlatformForApp(@PathVariable("appid") String appid, @RequestParam("platformChannelCodes") String platformChannelCodes) {
        payChannelService.bindPlatformChannelForApp(appid, platformChannelCodes);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 10：
标题：2. 接口定义如下：
内容：
在 AppController 类中定义 bindPlatformForApp 方法：
```java
@ApiImplicitParams({
    @ApiImplicitParam(value = "应用ID", name = "appid", required = true, dataType = "String"),
    @ApiImplicitParam(value = "服务类型code", name = "platformChannelCodes", required = true, dataType = "String")
})
public void bindPlatformForApp(@PathVariable("appid") String appid, @RequestParam("platformChannelCodes") String platformChannelCodes) {
    payChannelService.bindPlatformChannelForApp(appid, platformChannelCodes);
}
```

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

