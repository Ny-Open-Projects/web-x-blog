# 画面线理解：23.支付参数配置-应用查询

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day04 商户资质申请 七牛云 异常处理
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day04 商户资质申请 七牛云 异常处理\23.支付参数配置-应用查询【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:11, 00:53, 01:34, 02:27, 03:13, 03:54, 04:38, 05:26, 06:34, 07:33, 08:00, 08:22, 09:41, 10:11
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:16:47

1) 这一组画面整体在讲什么（一句话）：
演示商户服务应用查询接口的定义、实现及调用过程，包括服务层接口、控制层接口、数据库操作及接口测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程大纲，当前章节为“4.3 应用查询”，子章节“4.3.1 商户服务应用查询接口”下的“4.3.1.1 接口定义”，并显示了接口定义代码：List<AppDTO> queryAppByMerchant(Long merchantId) throws BusinessException;
画面2：在IDE中展示AppService接口定义，包含createApp和queryAppByMerchant方法，鼠标悬停在queryAppByMerchant方法上。
画面3：在IDE中展示AppService接口定义，鼠标悬停在queryAppByMerchant方法上，显示方法签名。
画面4：在IDE中展示AppService接口定义，鼠标悬停在queryAppByMerchant方法上，显示方法签名。
画面5：在IDE中展示AppService接口实现，显示queryAppByMerchant方法的实现，使用了LambdaQueryWrapper和selectList。
画面6：在IDE中展示AppService接口实现，显示getAppById方法的实现，使用了LambdaQueryWrapper和selectOne。
画面7：展示课程大纲，当前章节为“4.3.2 商户平台应用查询接口”，子章节“4.3.2.1 接口定义”，并显示了接口定义代码：@ApiOperation("查询商户下的应用列表") @GetMapping(value = "/my/apps") public List<AppDTO> queryByApps() { Long merchantId = SecurityUtil.getMerchantId(); return appService.queryAppByMerchant(merchantId); }
画面8：在IDE中展示AppController类，显示queryByApps方法的实现，调用appService.queryAppByMerchant。
画面9：在IDE中展示AppController类，显示getApp方法的实现，调用appService.getAppById。
画面10：在IDE中展示AppController类，显示getApp方法的实现，调用appService.getAppById。
画面11：在IDE中展示AppController类，显示getApp方法的实现，调用appService.getAppById。
画面12：在Swagger UI中展示GET /my/apps/{appId}接口，显示参数appId和响应示例。
画面13：在Postman中展示GET请求，地址为http://localhost:57010/merchant/my/apps，请求头Authorization包含Bearer token，请求体为JSON格式。
画面14：展示课程大纲，当前章节为“4.3 应用查询”，子章节“4.3.1 商户服务应用查询接口”，并显示了“二、商户应该配置哪些第三方支付渠道的参数呢？”的内容。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
/**
 * 查询商户下的应用列表
 * @param merchantId
 * @return
 */
List<AppDTO> queryAppByMerchant(Long merchantId) throws BusinessException;
```
画面2：
```java
/**
 * 应用管理相关的接口。
 * Created by Administrator.
 */
public interface AppService {

    /**
     * 创建应用
     * @param merchantId 商户id
     * @param appDTO 应用信息
     * @return 创建成功的应用信息
     * @throws BusinessException
     */
    AppDTO createApp(Long merchantId, AppDTO appDTO) throws BusinessException;

    List<AppDTO> queryAppByMerchant(Long merchantId) throws BusinessException;
```
画面3：
```java
/**
 * 应用管理相关的接口。
 * Created by Administrator.
 */
public interface AppService {

    /**
     * 创建应用
     * @param merchantId 商户id
     * @param appDTO 应用信息
     * @return 创建成功的应用信息
     * @throws BusinessException
     */
    AppDTO createApp(Long merchantId, AppDTO appDTO) throws BusinessException;

    List<AppDTO> queryAppByMerchant(Long merchantId) throws BusinessException;
```
画面4：
```java
/**
 * 应用管理相关的接口。
 * Created by Administrator.
 */
public interface AppService {

    /**
     * 创建应用
     * @param merchantId 商户id
     * @param appDTO 应用信息
     * @return 创建成功的应用信息
     * @throws BusinessException
     */
    AppDTO createApp(Long merchantId, AppDTO appDTO) throws BusinessException;

    List<AppDTO> queryAppByMerchant(Long merchantId) throws BusinessException;
```
画面5：
```java
@Override
public List<AppDTO> queryAppByMerchant(Long merchantId) throws BusinessException {
    List<AppDTO> apps = appMapper.selectList(new LambdaQueryWrapper<App>().eq(App::getMerchantId, merchantId));
    return apps;
}
```
画面6：
```java
@Override
public AppDTO getAppById(String appId) throws BusinessException {
    App app = appMapper.selectOne(new LambdaQueryWrapper<App>().eq(App::getAppId, appId));
    return app;
}
```
画面7：
```java
@ApiOperation("查询商户下的应用列表")
@GetMapping(value = "/my/apps")
public List<AppDTO> queryByApps() {
    Long merchantId = SecurityUtil.getMerchantId();
    return appService.queryAppByMerchant(merchantId);
}
```
画面8：
```java
@ApiOperation("查询商户下的应用列表")
@GetMapping(value = "/my/apps")
public List<AppDTO> queryByApps() {
    Long merchantId = SecurityUtil.getMerchantId();
    return appService.queryAppByMerchant(merchantId);
}
```
画面9：
```java
@ApiOperation("根据应用id查询应用信息")
@GetMapping(value = "/my/apps/{appId}")
public AppDTO getApp(@PathVariable("appId") String appId) {
    return appService.getAppById(appId);
}
```
画面10：
```java
@ApiOperation("根据应用id查询应用信息")
@GetMapping(value = "/my/apps/{appId}")
public AppDTO getApp(@PathVariable("appId") String appId) {
    return appService.getAppById(appId);
}
```
画面11：
```java
@ApiOperation("根据应用id查询应用信息")
@GetMapping(value = "/my/apps/{appId}")
public AppDTO getApp(@PathVariable("appId") String appId) {
    return appService.getAppById(appId);
}
```
画面12：
```json
{
  "appId": "string",
  "appname": "string",
  "merchantId": 0,
  "notifyUrl": "string",
  "publicKey": "string"
}
```
画面13：
```json
{
  "appId": "merchant-0812-40ab-9811-478a6b57fe",
  "appname": "充值网银",
  "merchantId": 12112208148344425,
  "notifyUrl": "string",
  "publicKey": "string"
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“4.3 应用查询”，子标题“4.3.1 商户服务应用查询接口”，子子标题“4.3.1.1 接口定义”。
画面7：PPT标题为“4.3.2 商户平台应用查询接口”，子标题“4.3.2.1 接口定义”。
画面14：PPT标题为“4.3 应用查询”，子标题“4.3.1 商户服务应用查询接口”，子子标题“4.3.1.1 接口定义”，并显示了“二、商户应该配置哪些第三方支付渠道的参数呢？”的内容。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
