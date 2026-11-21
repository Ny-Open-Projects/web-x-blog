# 画面线理解：14.前后端集成测试-功能测试-注册和登录

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day06 SaaS对接 OAuth2.0 前后端集成测试
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day06 SaaS对接 OAuth2.0 前后端集成测试\14.前后端集成测试-功能测试-注册和登录【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:27, 01:00, 01:19, 01:38, 02:04, 02:20, 02:41, 03:07, 03:35, 04:13, 04:48, 05:39, 06:13
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:42:05

1) 这一组画面整体在讲什么（一句话）：
演示如何通过代码实现商户注册功能，并展示前端登录、注册及后台数据操作流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示文档“1.2.4 启动服务端”和“1.3 商户注册”章节，列出测试接口列表，包括“注册获取手机验证码”（GET /merchant/sms）和“注册商户”（POST /merchant/merchants/register）。
画面2：在IDE中查看MerchantController.java代码，展示获取商户ID的逻辑，其中调用merchantService.queryMerchantByTenantId方法。
画面3：在IDE中查看MerchantService.java代码，展示queryMerchantByTenantId方法的实现，使用merchantMapper.selectOne方法查询数据。
画面4：在IDE的控制台中显示启动日志，包含Dubbo Spring Boot版本信息和配置被覆盖的警告。
画面5：在IDE中右键点击“GatewayBootstrap”并选择“Edit Configuration...”，准备修改配置。
画面6：再次展示文档“1.3 商户注册”章节，强调测试接口列表。
画面7：在前端页面展示“资质申请”表单，要求填写基本信息和上传证件。
画面8：在浏览器中打开登录页面，使用开发者工具查看登录容器的样式。
画面9：展示文档“1.6 支付渠道参数配置”章节，列出相关测试接口。
画面10：在浏览器中查看登录页面，开发者工具显示网络请求。
画面11：在浏览器中打开“注册商户”页面，填写用户名、密码等信息。
画面12：在数据库管理工具中查看merchant表，显示商户信息。
画面13：在浏览器中查看用户个人中心页面，显示账户信息和交易数据。
画面14：在浏览器中查看用户个人中心页面，开发者工具显示请求头中包含的merchantTenantId参数。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2代码：
```java
return LoginUser jwt;
return new LoginUser();
public static Long getMerchantId() {
    MerchantService merchantService = ApplicationContextHelper.getApplicationContext().getBean(MerchantService.class);
    MerchantDTO merchant = merchantService.queryMerchantByTenantId(getUser().getTenantId());
    Long merchantId = null;
    if (merchant != null) {
        merchantId = merchant.getId();
    }
    return merchantId;
}
// 降级为JSON对象用户对象
// @param token
// @return
public static LoginUser convertToLoginUser(String token) {
```
画面3代码：
```java
@Override
public MerchantDTO queryMerchantByTenantId(Long tenantId) {
    Merchant merchant = merchantMapper.selectOne(new LambdaQueryWrapper<Merchant>().eq(Merchant::getTenantId, tenantId));
    return MerchantConvert.INSTANCE.entityToDto(merchant);
}
@Override
public MerchantDTO createMerchant(MerchantDTO merchantDTO) throws BusinessException {
    // 校验参数的合法性
    if (merchantDTO == null) {
        throw new BusinessException(CommonErrorCode.E_100108);
    }
```
画面5配置：
```java
Edit Configuration... Configuration
```
画面12 SQL：
```sql
MERCHANT_ID MERCHANT_NAME MERCHANT_TYPE BUSINESS_LICENSE_IMG ID_CARD_PRINT_IMG
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1 PPT标题：
- 1.2.4 启动服务端
- 1.3 商户注册
- 1.3 商户注册
- 1.6 支付渠道参数配置

画面9 PPT标题：
- 1.6 支付渠道参数配置
- 1.6 支付渠道参数配置

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
