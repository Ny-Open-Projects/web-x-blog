# 14.前后端集成测试-功能测试-注册和登录

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day06 SaaS对接 OAuth2.0 前后端集成测试
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day06 SaaS对接 OAuth2.0 前后端集成测试\14.前后端集成测试-功能测试-注册和登录【海量资源尽在 666java.com】.mp4
- 时长 6分20秒（音频 381s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 下面呢我们继续来进行前后端分离测试那么接下来呢我们要把我们的服务端呢都提起来好 那这里边大家来看这还有个报错嘞看一下啊这是啥错这是我们在做前期准备工作的时候对吧然后呢大家看啊这个是啥意思呀它是个浪 对吧这里边呢我们来看啊它呢需要一个字符串应该嘛
[00:37] 然后这里面应该是我们的参数定义错了对吧这个参数我们把这个参数换一下这个应该变成浪这样是不是就行了这样它就没有错了没有错了来我们捋一下看一下我们是需要把我们的服务端都起起来首先起NetCourse然后这里边先把SaaS起起来Gateway然后再有就是User
[01:17] 这边我们需要起Gateway User UA这是SaaS系统的三个服务对吧好 接下来起我们商户平台的商户平台的首先是商户服务对然后呢是商户平台应用但其实商户平台应用它还需要一个叫交易服务大家有印象吧我们当时做这个参数配置的时候是吧
[01:46] 然后呢这是商户服务交易服务最后我们起商户平台应用就这个对那我们把它起起来之后呀那我们呢就可以来进行什么测试了注意打开我们集中测试文档看好啊我们从商户注册开始测行不行商户注册用户登录注册成功了之后我们是不是可以拿到账号来登录登录完了之后资质申请
[02:19] 好然后渠道参数配置对吧好那现在我们就打开前端原来我们是不是把前端工程已经布好了然后打开调试的窗口注意这个调试窗口注意这里边呢大家原来的默认可能是这样一个就是调试的这个在最下边你能把它放到怎么右侧吧好然后呢你你打开这个network
[02:46] 为啥一会呢你在请求的时候呀他这就会发一堆的这个请求链接我们请求链接不就是我们服务端地址吗我们要跟踪一下看看他是不是正确的或者说有问题的我们要排错好了那下面我们来看吧这儿呢这个服务是不是都OK了那接下来我们就按照我们文档上说的接口商户注册的测试商户注册的话这里面你看还要获取手机验证码对吧那各位
[03:17] 验证码服务是不是也要起来是吧我们要起来验证码服务好那下边呢我们就准备来注册一个吧那这里边各位看一下啊有个注册账号看到吗然后我们现在叫test test03看数据库现在有吗看一下我们这个员工
[03:52] 员工表这里边TES0102我们注册一个TES03可以吧密码123456手机号这个不能重复手机号手机号的话你要知道在我们商务表手机号也是唯一的对吧所以这里边呢我们往后来加比如说6行吧然后呢获取验证码你把这清一下啊把这清一下获取验证码这时候一点
[04:22] 这个就是获取验证码看下吧你看已经发动成功发动成功这个时候我们不是说验证码是在控制台输出的吗来控制台拿到验证码然后你填进去对不对然后点击注册这个是不是就是我们注册的接口对不对我们注册三户吧成功了这时候呢我们就可以来到三户表来看一下三户表哪个是我们的呀这是6吧你看这个是吧
[04:56] 它对应的商户是叫07106这个商户ID你找到商户表07106就是它并且我们已经和这个SaaS系统做对接你看SaaS系统给它返回的租户ID是不是没错吧包括默认的门店对吧他们之间的关系都OK了这就是我们的注册就成功了那接下来我们要做什么事是不是登录
[05:27] 登录刚才是不是有一个test03密码是123456然后点击登录对吧这时候呢你看拿到talk登录成功对吧大家看到这里边的画面其实就是我们刚才写的那个获取三户信息的一个接口前段呢去请求然后呢拿到来看到这个结果你看在这呢然后呢他传了一个租户ID然后呢我们根据租户ID来拿到
[05:58] 对应的商户信息那各位到这儿我们测试的是什么呀是不是就是商户注册和商户的什么登录吧那我们就测试通过了那么这个整个测试的过程呢大家一定要在这儿跟踪这个发出的请求URL好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

