# 画面线理解：06.支付渠道参数配置-应用绑定服务类型-接口开发

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day05 支付渠道参数配置 Redis
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day05 支付渠道参数配置 Redis\06.支付渠道参数配置-应用绑定服务类型-接口开发【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:38, 01:23, 02:34, 03:39, 04:03, 05:02, 05:36, 06:21, 06:58, 07:40, 08:21, 09:24, 10:14, 10:56
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:20:36

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
import com.shanju.pay.transaction.mapper.AppPlatformChannelMapper;
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
