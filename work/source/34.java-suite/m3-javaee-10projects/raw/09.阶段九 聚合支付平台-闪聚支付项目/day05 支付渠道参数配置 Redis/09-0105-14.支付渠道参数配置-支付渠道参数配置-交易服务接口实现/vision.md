# 画面线理解：14.支付渠道参数配置-支付渠道参数配置-交易服务接口实现

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day05 支付渠道参数配置 Redis
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day05 支付渠道参数配置 Redis\14.支付渠道参数配置-支付渠道参数配置-交易服务接口实现【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:56, 03:35, 04:12, 04:56, 05:26, 06:21, 06:47, 07:18, 07:57, 08:51, 09:48, 10:29, 11:47
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:26:28

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
