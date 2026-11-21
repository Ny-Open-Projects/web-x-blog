# 画面线理解：12.前后端集成测试-前期准备

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day06 SaaS对接 OAuth2.0 前后端集成测试
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day06 SaaS对接 OAuth2.0 前后端集成测试\12.前后端集成测试-前期准备【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:07, 03:08, 04:23, 05:08, 05:55, 06:33, 07:08, 07:30, 08:40, 09:19, 09:55, 10:41, 11:20, 11:57
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:41:13

1) 这一组画面整体在讲什么（一句话）：
讲解商户平台应用如何通过集成测试获取商户信息，涉及服务层、控制器层代码及Token解析的实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT，章节为“1.1 测试需求”，说明本次测试是前后端联调测试，重点是商户平台应用获取登录商户信息。
画面2：PPT内容延续，展示在MerchantServiceImpl中定义queryMerchantById方法，用于根据商户id查询商户信息。
画面3：IDE中展示MerchantServiceImpl.java代码，包含queryMerchantById方法，其中调用merchantMapper.selectById，并将查询结果转换为MerchantDTO。
画面4：IDE中展示MerchantServiceImpl.java代码，光标在return merchantDTO;语句处，下方有注释说明该方法用于注册商户成功后获取商户信息。
画面5：IDE中展示MerchantController.java代码，包含getMyMerchantInfo接口，用于获取当前用户的商户信息。
画面6：IDE中展示MerchantController.java代码，光标在getMyMerchantInfo方法中，注释说明从token中提取商户id。
画面7：IDE中展示SecurityUtil.java代码，包含getMerchantId方法，用于从请求头的Authorization中解析并提取商户id。
画面8：IDE中展示SecurityUtil.java代码，光标在getMerchantId方法中，下方有getUserId方法的代码片段。
画面9：IDE中展示MerchantController.java代码，光标在getMyMerchantInfo方法中，注释说明从token中提取商户id。
画面10：文件资源管理器中显示TokenAuthenticationFilter.java文件，用于解析token。
画面11：IDE中展示TokenAuthenticationFilter.java代码，包含从userMap中获取权限信息并设置到request的逻辑。
画面12：IDE中展示MerchantServiceImpl.java代码，光标在queryMerchantByTenantId方法中，展示查询商户信息的SQL语句。
画面13：IDE中展示MerchantServiceImpl.java代码，光标在queryMerchantByTenantId方法中，展示使用LambdaQueryWrapper进行条件查询的代码。
画面14：PPT内容，章节为“1.2.2 服务端解析Token”，说明在进行功能测试时需要修改SecurityUtil及TokenAuthenticationFilter.java文件。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
@Override
public MerchantDTO queryMerchantById(Long merchantId) {
    Merchant merchant = merchantMapper.selectById(merchantId);
    MerchantDTO merchantDTO = MerchantConvert.INSTANCE.entity2dto(merchant);
    return merchantDTO;
}
```

画面3：
```java
@Override
public MerchantDTO queryMerchantById(Long id) {
    Merchant merchant = merchantMapper.selectById(id);
    MerchantDTO merchantDTO = new MerchantDTO();
    merchantDTO.setId(merchant.getId());
    merchantDTO.setMerchantName(merchant.getMerchantName());
    return merchantDTO;
}
```

画面5：
```java
@GetMapping(value = "/my/merchants")
public MerchantDTO getMyMerchantInfo() {
    //从token中提取商户id
    Long merchantId = SecurityUtil.getMerchantId();
    return merchantService.queryMerchantById(merchantId);
}
```

画面6：
```java
@GetMapping(value = "/my/merchants")
public MerchantDTO getMyMerchantInfo() {
    //从token中提取商户id
    Long merchantId = SecurityUtil.getMerchantId();
    return merchantService.queryMerchantById(merchantId);
}
```

画面7：
```java
public class SecurityUtil {
    @Test
    public static Long getMerchantId() {
        HttpServletRequest request = (HttpServletRequest) RequestContextHolder.currentRequestAttributes().getRequest();
        String jsonToken = request.getHeader("authorization");
        if (StringUtils.isEmpty(jsonToken) || !jsonToken.startsWith("Bearer ")) {
            throw new RuntimeException("token is not as expected");
        }
        jsonToken = jsonToken.substring(7);
        jsonToken = EncryptUtil.decodeStringBase64(jsonToken);
        JSONObject jsonObject = JSON.parseObject(jsonToken);
        return jsonObject.getLong("merchantId");
    }
}
```

画面8：
```java
public static LoginUser getUser() {
    ServletRequestAttributes servletRequestAttributes = (ServletRequestAttributes) RequestContextHolder.currentRequestAttributes();
    if (servletRequestAttributes == null) {
        HttpServletRequest request = servletRequestAttributes.getRequest();
    }
}
```

画面11：
```java
Map<String, List<String>> userMap = (Map<String, List<String>>) request.getAttribute("user_authorities");
if (userMap == null) {
    log.error("json-token中该用户（）没有权限信息", tenantId);
    throw new BusinessException(code: 99991, desc: "调用服务方json-token中没有权限信息");
}
return userMap;
```

画面12：
```java
public MerchantDTO queryMerchantByTenantId(String tenantId) {
    merchantMapper.selectOne(new LambdaQueryWrapper<Merchant>().eq(Merchant::getTenantId, tenantId));
    return null;
}
```

画面13：
```java
public MerchantDTO queryMerchantByTenantId(String tenantId) {
    merchantMapper.selectOne(new LambdaQueryWrapper<Merchant>().eq(Merchant::getTenantId, tenantId));
    return null;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“1 集成测试”，子标题“1.1 测试需求”，内容说明本次测试是前后端联调测试，重点是商户平台应用获取登录商户信息。
画面2：PPT标题为“1.2.1 商户平台应用获取登录商户信息”，内容说明在MerchantServiceImpl中定义queryMerchantById方法，根据商户id查询商户信息。
画面14：PPT标题为“1.2.2 服务端解析Token”，内容说明在进行功能测试时需要修改SecurityUtil及TokenAuthenticationFilter.java文件。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
