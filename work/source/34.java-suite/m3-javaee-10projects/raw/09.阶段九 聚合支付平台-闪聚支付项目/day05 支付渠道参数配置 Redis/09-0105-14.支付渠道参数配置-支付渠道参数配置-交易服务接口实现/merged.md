# 14.支付渠道参数配置-支付渠道参数配置-交易服务接口实现

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day05 支付渠道参数配置 Redis
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day05 支付渠道参数配置 Redis\14.支付渠道参数配置-支付渠道参数配置-交易服务接口实现【海量资源尽在 666java.com】.mp4
- 时长 11分49秒（音频 710s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们就来实现交易服务支付渠道参数配置的接口那么刚才呢我们已经把这个接口呢定义出来了那下面呢我们先把这个接口的实现方法啊然后给他写一下看好啊呃那么我们思考一下这个接口我们要怎么去实现呢我们说这个接口请求过来的数据呢包括商务ID应用ID服务类型然后呢支付渠道配置名称
[00:28] 以及配置参数的json最终啊这个配置名称和配置参数这是不是我们要进行配置的内容啊当然这些东西呢也要更新到数据库对不对那现在呢我们就来看那怎么样更新数据库呢你要知道啊这张表很有可能我们都已经配置过了那对于已经存在配置信息的那么我们要更新配置如果没有存在我们要插入对不对那好了现在问题来了那我们怎么来判断它已经是否存在配置信息呢
[00:58] 换句话说就我们应该根据什么来查询一下得到一条记录才知道它是否已经配置了呢注意看啊我们之前说过嘛其实我们在这张表当中啊包括四个要素一个是商户一个是支付渠道代码一个是应用一个是服务类型对吧但这里边的你要注意其实这里边呢这两个字段是一个唯一为啥呢因为应用和服务类型
[01:27] 他俩之间你注意他可以因为应用和绑定服务类型的嘛他们之间其实是有一个绑定ID的而这个绑定ID呢就在应用服务类型的这个绑定关系表里面是不是这个ID啊这个ID本身它就是一个什么雪花片算法生成的ID对吧那现在呢我们要拿着这个ID加上什么支付渠道他们组成一个围一这个表示是什么意思呢就是某一个商户他的什么
[01:55] 它的应用使用了我们某一个服务类型我们呢需要给某个支付渠道来配餐就这个意思懂我意思吧所以这里边呢这两个字段是唯一那这两个字段唯一的话那有人说老师那我怎么样能够得到这个绑定ID呢对吧因为这绑定ID我是不是需要从谁啊
[02:18] 这个应用和服务类型的绑定关系表里面根据应用和服务类型来查出这个ID那我们是不是就拿到了这个应用服务类型的绑定的这个ID了对不对好那么回到代码我们来看你的目的是什么呢我们要根据应用服务类型以及支付渠道是不是要查询一条记录那这条记录呢对如果存在配置我们则干嘛更新那否则
[02:48] 就添加这是不是很容易理解那现在问题是我们刚才说了嘛你要根据应用服务类型我们首先是不是需要去查一个绑定ID啊对根据应用和服务类型查询一个什么应用与服务类型的一个绑定ID然后呢你再根据这个应用服务类型的绑定ID然后呢和什么和支付渠道
[03:14] 然后呢我们再查询我们说的这个支付渠道参数表当中的一条记录懂我意思吗因为这个支付渠道参数表它是绑定ID加支付渠道组成一个唯一的约束懂吧好了那现在呢我们就来写吧那么现在我们要写的话注意现在我要做的事是什么
[03:40] 我要做的事是不是就是要首先根据应用和服务类型查询应用与服务的绑定ID然后再拿着绑定ID和支付渠道来查询这个支付参数配置表当中一条记录对好那首先这里边呢我们注意看啊我们首先看讲义这里边这个查询呢首先拿应用和服务类型来查询绑定ID啊我们呢建一个私有方法嗯建一个私有方法那这个私有方法呢它呢它的目的
[04:09] 就是来查询绑定ID那首先你得给我什么应用ID然后其次你还要给我什么你还要给我一个支付服务类型的code对不对因为应用和服务类型绑定ID嘛那你是不是得给我服务类型的code那这样的话我们是不是就可以怎么弄是不是就可以来查询一下怎么查APPPlayer Platform Channel Mapper这是不是就是应用服务类型的什么Mapper然后呢Select
[04:39] 是不是可以查然后呢Lambda然后这里面我们要查哪个表我们要查的就是这个应用服务类型关系表查他们的绑定ID嘛应用服务类型对吧然后注意然后呢这里边看好首先应用ID你得有对不对然后其次你应用和服务类型嘛你是不是还有一个什么还有一个服务类型对不对那这个服务类型呢是哪个
[05:08] 是不是它那这里边呢我们就可以拿到这个服务类型的code那我是不是就得到一条记录啊那这个我就可以判断一下如果说你刚才查到了这个对象它不为空那我问你这是不是就可以直接返回get id这个就是应用与服务类型的什么绑定id了对不对如果没有值是个空
[05:38] 那我就返回空行不行那这样的话各位这个就是我们说的根据应用和服务类型查询它的什么绑定ID好那现在呢我们就可以在这里来调用一下这个私有的方法行吧调用这个方法的话你需要给我传两个参数吗一个是什么应用ID一个是什么这个服务类型的code对吧你这时候是不是就拿到一个ID这个ID是啥ID
[06:06] 这ID是不是就是我们说的这个应用服务类型绑定关系的ID对不对好那么这个时候呢我们再根据什么这个绑定ID和支付渠道这时候在我们说的最终要更新记录的这个支付渠道参数表当中我们就能查到一个唯一记录懂我意思吧好那现在呢我们把上面把Mapper注进去现在我们要做的是不是PayChannel我们要给它从它这来查了
[06:37] 这是不是就是我们说的这个支付渠道参数表的Mapper好那现在我们在这查怎么查select对吧一样我们要查一下查这个pay channel怎么做看好不是它在这pay channel param好.ecos那现在呢我们要查的首先是绑定这个条件嘛应用和服务类型的绑定ID
[07:09] 这刚才是不是查到的ID了对然后呢接下来绑定ID和支付渠道是不是组成一个唯一对不对那所以说这个绑定ID我们先把这个条件给它加上去然后呢再加就是一颗谁呀支付渠道对不对绑定ID加支付渠道嘛那就是绑定ID加支付渠道支付渠道哪个是不是就PayChannel啊
[07:39] 配线动然后从这拿一个支付渠道就是传过来的支付渠道懂吧好现在我们在支付渠道参数表当中是不是就查到了一条记录没错吧那么查到这条记录了我们刚才说了你要判断了如果它不为空你是不是就要更新了否则你是不是就要添加了那就简单了更新的话怎么更新更新你主要更新什么你得看表单看我们的原型
[08:09] 更新你看它主要更新配置名称和我们说的一堆数据组成的json就是param这个字段对吧你看这是不是有一个param将来前段的会把这堆数据呢组成一个json然后保存到param字段所以这里边呢我们主要更新这两个啊看好set这个呢就是我们说的配置配置的名称看好get
[08:40] 这就是表单配置的名称然后还有呢再来还有啥刚才说了嘛perm这是不是就是那个json格式的这个参数啊一堆是吧这就是什么json格式的什么参数哎好那么这个呢我们就可以update对不对update直接把它放进去就行了是吧ok然后接下来呢嗯那否则要添加了那怎么添加
[09:11] insert嘛对不对insert的话注意这个是不是就是表单传过来的数据啊那么我们完全是不是可以怎么做呀我们是不是就可以用我们之前学习的这个converter然后呢把它转成我们要的entity行不行对吧哎好那现在呢我们就把它转成了这么一个什么entity就是一个新的对象对吧新的对象那现在呢我们是不是就可以怎么动啊怎么做
[09:41] 哎直接可以insert就可以吧但是注意这里边有有有问题我一说一下就是说在这个转层的这个对象你看啊这个DTO里头你看这一堆都需要去插入的就这个组件其实在插入的时候我觉得就不用设置这个DTO里边包括这个组件这个组件因为我们在怎么弄插入的时候是不是myvtes plus要生成一个这个组件啊所以这里边呢我们在插入之前我建议你把这个组件置空
[10:10] 以免影响我们的操作是吧然后这样的话我们就可以怎么弄insert然后把它放进去我问你这是不是就是插入成功插入配置以上是不是就是我们说的支付渠道参数配置的一个具体的方法我们来梳理一下流程目的我们要向这张表写数据首先你要找到这张表唯一的ID对吧我们要根据这两个字段查出一条记录如果存在就更新不存在则插入
[10:40] 那问题是这个ID这个ID是没有前端是不可能给你传过来的那我们需要根据前端传入的怎么样应用和服务类型找到这个绑定ID就是应用和服务类型的绑定关系ID拿着这个绑定关系ID然后呢我们再和这个支付渠道来查最终查到刚才说的支付渠道参数配置里面的一张
[11:03] 一条记录拿了这个记录我们判断如果不为空我们就更新如果为空我们就插入对不对插入的时候我们要看表配置名称页面传的插吧散户ID在里边也有对不对这个编码也是前段传过来的支付参数也是那这个绑定ID这是我们刚才查数据库查出来的对不对所以这里边我们还是你要扫set一个东西就是这个绑定关系的ID这就是我们说的什么
[11:32] 应用与服务类型绑定关系的ID你必须在这手动的把它设置进去好了这就是交易服务提供的一个什么支付渠道参数配置的接口我们就实现完了好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在交易服务中实现支付渠道参数的增删改查功能，重点是通过代码逻辑操作数据库表 pay_channel_param 和 app_platform_channel。

2) 按时间顺序列出每张画面的要点：
画面1：展示文档“5.4.4.2 接口实现”部分，说明服务需提供接口实现支付渠道参数配置，并给出在 PayChannelServiceImpl 中定义 savePayChannelParam 方法的代码示例。
画面2：展示数据库表 pay_channel_param 的结构，包含字段 ID、CHANNEL_NAME、MERCHANT_ID、PAY_CHANNEL、PARAM、APP_PLATFORM_CHANNEL_ID。
画面3：展示代码编辑器中 PayChannelServiceImpl.java 文件，显示 savePayChannelParam 方法的注释和部分代码，其中包含对参数的校验逻辑。
画面4：在代码编辑器中，光标位于方法内部，显示了对 appPlatformChannelMapper 的调用，下方弹出的自动补全建议中包含 String、StringBuilder 等类。
画面5：在代码编辑器中，光标位于方法内部，显示了对 appPlatformChannelMapper 的调用，下方弹出的自动补全建议中包含 AppPlatformChannel、AppPlatformChannelMapper 等类。
画面6：在代码编辑器中，光标位于方法内部，显示了对 appPlatformChannelMapper 的调用，下方弹出的自动补全建议中包含 AppPlatformChannel、AppPlatformChannelMapper 等类。
画面7：展示数据库表 app_platform_channel 的结构，包含字段 ID、APP_ID、PLATFORM_CHANNEL，以及主键索引。
画面8：在代码编辑器中，光标位于方法内部，显示了对 payChannelParamMapper 的调用，下方弹出的自动补全建议中包含 PayChannelParam、PayChannelParamMapper 等类。
画面9：在代码编辑器中，光标位于方法内部，显示了 queryPayChannelByPlatformChannel 方法的注释和部分代码。
画面10：在代码编辑器中，光标位于方法内部，显示了对 entity 变量的判断，下方弹出的自动补全建议中包含 NullPointerException、NumberFormatException 等类。
画面11：在代码编辑器中，光标位于方法内部，显示了对 entity 变量的判断，下方弹出的自动补全建议中包含 PayChannelParam、PayChannelParamMapper 等类。
画面12：在代码编辑器中，光标位于方法内部，显示了对 entity 变量的判断，下方弹出的自动补全建议中包含 PayChannelParam、PayChannelParamMapper 等类。
画面13：展示数据库表 pay_channel_param 的结构，包含字段 ID、CHANNEL_NAME、MERCHANT_ID、PAY_CHANNEL、PARAM、APP_PLATFORM_CHANNEL_ID。
画面14：展示文档“5.4.4.1 接口定义”部分，说明本接口用于为应用绑定服务类型后配置支付渠道参数，并给出在 PayChannelService 中定义 createPayChannelParam 方法的代码示例。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
/**
 * 保存支付渠道参数
 * @param payChannelParamDTO 支付渠道参数
 * @throws BusinessException
 */
@Override
public void savePayChannelParam(PayChannelParamDTO payChannelParamDTO) throws BusinessException {
    if (StringUtils.isBlank(payChannelParamDTO.getAppId()) || StringUtils.isBlank(payChannelParamDTO.getPlatformChannelCode())) {
        throw new BusinessException("应用ID或平台渠道编码不能为空");
    }
    // 根据应用、服务类型、支付渠道编码查询是否存在记录
    AppPlatformChannel appPlatformChannel = appPlatformChannelMapper.selectOne(new LambdaQueryWrapper<AppPlatformChannel>().eq(AppPlatformChannel::getAppId, payChannelParamDTO.getAppId()).eq(AppPlatformChannel::getPlatformChannelCode, payChannelParamDTO.getPlatformChannelCode()));
    if (appPlatformChannel == null) {
        throw new BusinessException("应用或服务类型不存在");
    }
    PayChannelParam entity = payChannelParamMapper.selectOne(new LambdaQueryWrapper<PayChannelParam>().eq(PayChannelParam::getAppId, payChannelParamDTO.getAppId()).eq(PayChannelParam::getPlatformChannelCode, payChannelParamDTO.getPlatformChannelCode()));
    if (entity == null) {
        // 不存在则新增
        entity = new PayChannelParam();
        entity.setAppId(payChannelParamDTO.getAppId());
        entity.setPlatformChannelCode(payChannelParamDTO.getPlatformChannelCode());
        entity.setChannelName(payChannelParamDTO.getChannelName());
        entity.setParam(payChannelParamDTO.getParam());
        payChannelParamMapper.insert(entity);
    } else {
        // 存在则更新
        entity.setChannelName(payChannelParamDTO.getChannelName());
        entity.setParam(payChannelParamDTO.getParam());
        payChannelParamMapper.updateById(entity);
    }
}
```

画面3：
```java
/**
 * @param payChannelParam 配置支付渠道参数：包括：商户id、应用id、服务类型code、支付渠道code、配置参数、配置参数(json)
 * @throws BusinessException
 */
@Override
public void savePayChannelParam(PayChannelParamDTO payChannelParam) throws BusinessException {
    // 根据应用、服务类型、支付渠道编码查询是否存在记录
    Long appPlatformChannelId = selectByIdAppPlatformChannel(payChannelParam.getAppId(), payChannelParam.getPlatformChannelCode());
    // 根据应用用户财务类型的类型id和支付渠道查询PayChannelParam的一条记录
    PayChannelParam entity = payChannelParamMapper.selectOne(new LambdaQueryWrapper<PayChannelParam>().eq(PayChannelParam::getAppId, payChannelParam.getAppId()).eq(PayChannelParam::getPlatformChannelCode, payChannelParam.getPlatformChannelCode()));
    // 如果存在配置则更新
    // 否则添加配置
    // 根据应用、服务类型查询app_platform_channel表中id
    private Long selectByIdAppPlatformChannel(String appId, String platformChannelCode) {
        AppPlatformChannel appPlatformChannel = appPlatformChannelMapper.selectOne(new LambdaQueryWrapper<AppPlatformChannel>().eq(AppPlatformChannel::getAppId, appId).eq(AppPlatformChannel::getPlatformChannelCode, platformChannelCode));
        if (appPlatformChannel == null) {
            return -1;
        }
        return appPlatformChannel.getId();
    }
```

画面6：
```java
private Long selectByIdAppPlatformChannel(String appId, String platformChannelCode) {
    AppPlatformChannel appPlatformChannel = appPlatformChannelMapper.selectOne(new LambdaQueryWrapper<AppPlatformChannel>().eq(AppPlatformChannel::getAppId, appId).eq(AppPlatformChannel::getPlatformChannelCode, platformChannelCode));
    if (appPlatformChannel == null) {
        return -1;
    }
    return appPlatformChannel.getId();
}
```

画面8：
```java
/**
 * @param payChannelParam 配置支付渠道参数：包括：商户id、应用id、服务类型code、支付渠道code、配置参数、配置参数(json)
 * @throws BusinessException
 */
@Override
public void savePayChannelParam(PayChannelParamDTO payChannelParam) throws BusinessException {
    // 根据应用、服务类型、支付渠道编码查询是否存在记录
    Long appPlatformChannelId = selectByIdAppPlatformChannel(payChannelParam.getAppId(), payChannelParam.getPlatformChannelCode());
    // 根据应用用户财务类型的类型id和支付渠道查询PayChannelParam的一条记录
    PayChannelParam entity = payChannelParamMapper.selectOne(new LambdaQueryWrapper<PayChannelParam>().eq(PayChannelParam::getAppId, payChannelParam.getAppId()).eq(PayChannelParam::getPlatformChannelCode, payChannelParam.getPlatformChannelCode()));
    // 如果存在配置则更新
    // 否则添加配置
    // 根据应用、服务类型查询app_platform_channel表中id
    private Long selectByIdAppPlatformChannel(String appId, String platformChannelCode) {
        AppPlatformChannel appPlatformChannel = appPlatformChannelMapper.selectOne(new LambdaQueryWrapper<AppPlatformChannel>().eq(AppPlatformChannel::getAppId, appId).eq(AppPlatformChannel::getPlatformChannelCode, platformChannelCode));
        if (appPlatformChannel == null) {
            return -1;
        }
        return appPlatformChannel.getId();
    }
```

画面10：
```java
if (entity == null) {
    // 不存在则新增
    entity = new PayChannelParam();
    entity.setAppId(payChannelParam.getAppId());
    entity.setPlatformChannelCode(payChannelParam.getPlatformChannelCode());
    entity.setChannelName(payChannelParam.getChannelName());
    entity.setParam(payChannelParam.getParam());
    payChannelParamMapper.insert(entity);
} else {
    // 存在则更新
    entity.setChannelName(payChannelParam.getChannelName());
    entity.setParam(payChannelParam.getParam());
    payChannelParamMapper.updateById(entity);
}
```

画面12：
```java
if (entity == null) {
    // 不存在则新增
    entity = new PayChannelParam();
    entity.setAppId(payChannelParam.getAppId());
    entity.setPlatformChannelCode(payChannelParam.getPlatformChannelCode());
    entity.setChannelName(payChannelParam.getChannelName());
    entity.setParam(payChannelParam.getParam());
    payChannelParamMapper.insert(entity);
} else {
    // 存在则更新
    entity.setChannelName(payChannelParam.getChannelName());

