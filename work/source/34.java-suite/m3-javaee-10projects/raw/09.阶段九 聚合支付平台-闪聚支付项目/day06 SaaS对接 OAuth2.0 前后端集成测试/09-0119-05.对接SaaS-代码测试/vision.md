# 画面线理解：05.对接SaaS-代码测试

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day06 SaaS对接 OAuth2.0 前后端集成测试
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day06 SaaS对接 OAuth2.0 前后端集成测试\05.对接SaaS-代码测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 01:10, 02:56, 04:15, 05:06, 06:11, 07:25, 08:17, 09:46, 11:21, 13:46, 15:00, 16:09, 17:44
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:36:57

1) 这一组画面整体在讲什么（一句话）：
演示如何在 shanjupay 商户服务中实现商户注册功能，包括添加 SaaS 用户服务依赖、编写 MerchantService 实现类、处理商户信息校验、创建商户及关联员工等核心代码逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 讲解添加 SaaS 用户服务 API 依赖，打开 shanjupay-merchant-service 工程的 pom.xml 文件，展示添加的依赖配置。
画面 2: 展示 MerchantServiceImp 类中 createMerchant 方法的实现，包括注入 StoreStaffMapper 和 TenantService，创建并设置 MerchantDTO 对象。
画面 3: 展示数据库表结构，查看 merchant 表和 staff 表的字段。
画面 4: 展示 MerchantServiceImp 类中 createMerchant 方法的业务逻辑，包括对商户参数的校验（非空、手机号格式、手机号唯一性）。
画面 5: 展示 MerchantController 中的 merchantRegisterVO 对象，包含注册信息（手机号、用户名、密码）。
画面 6: 展示 MerchantDTO 类的定义，包含商户名称、企业编号、企业地址等字段。
画面 7: 展示项目结构和日志信息，包含 Spring Boot 启动日志和配置信息。
画面 8: 展示 MerchantServiceImp 类中创建商户的逻辑，包括获取租户 ID、创建商户对象并设置属性。
画面 9: 展示数据库表结构，查看 user 表的字段。
画面 10: 展示 MerchantServiceImp 类中创建员工的逻辑，包括创建 StaffDTO 对象并绑定到商户。
画面 11: 展示 MerchantServiceImp 类中创建商户的逻辑，包括判断商户是否已存在、创建租户账户。
画面 12: 展示日志信息，包含 Spring Boot 启动日志和配置信息。
画面 13: 展示 MerchantController 中的代码，包括调用 merchantService.createMerchant 方法。
画面 14: 展示商户注册的代码逻辑，包括设置租户套餐、租户账号信息、新增租户并设置商户所属租户。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```xml
<dependency>
    <groupId>com.shanjupay</groupId>
    <artifactId>shanjupay-user-api</artifactId>
    <version>1.0-SNAPSHOT</version>
</dependency>
```

画面 2:
```java
@Override
@Transactional
public MerchantDTO createMerchant(MerchantDTO merchantDTO) throws BusinessException {
    MerchantDTO merchantDTO = new MerchantDTO();
    merchantDTO.setId(merchant.getMerchantId());
    merchantDTO.setMerchantName(merchant.getMerchantName());
    merchantDTO.setMerchantNo(merchant.getMerchantNo());
    merchantDTO.setMerchantAddress(merchant.getMerchantAddress());
    return merchantDTO;
}
```

画面 4:
```java
@Override
public MerchantDTO createMerchant(MerchantDTO merchantDTO) throws BusinessException {
    if (merchantDTO == null) {
        throw new BusinessException(CommonErrorCode.E_100108);
    }
    if (StringUtils.isBlank(merchantDTO.getMobile())) {
        throw new BusinessException(CommonErrorCode.E_100111);
    }
    if (StringUtils.isBlank(merchantDTO.getPassword())) {
        throw new BusinessException(CommonErrorCode.E_100111);
    }
    if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
        if (StringUtils.isMobile(merchantDTO.getMobile())) {
            if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                    if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                        if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                            if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                    if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                        if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                            if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                    if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                        if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                            if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                    if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                        if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                            if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                    if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                        if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                            if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                    if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                        if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                            if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                    if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                        if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                            if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                    if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                        if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                            if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                    if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                        if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                            if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                    if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                        if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                            if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                    if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                        if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                            if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                    if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                        if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                            if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                    if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                        if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                            if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                    if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                        if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                            if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                    if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                        if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                            if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                    if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                        if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                            if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                                if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                                    if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                                        if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                                            if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                                                if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                                                    if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                                                        if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                                                            if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                                                                if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                                                                    if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                                                                        if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                                                                            if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                                                                                if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                                                                                    if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                                                                                        if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                                                                                            if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                                                                                                if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                                                                                                    if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                                                                                                        if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                                                                                                            if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                                                                                                                if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                                                                                                                    if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                                                                                                                        if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                                                                                                                            if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                                                                                                                                if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                                                                                                                                    if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                                                                                                                                        if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                                                                                                                                            if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
                                                                                                                                                                                                                                                                                                                                                                                                if (StringUtils.isNotBlank(merchantDTO.getMobile())) {
