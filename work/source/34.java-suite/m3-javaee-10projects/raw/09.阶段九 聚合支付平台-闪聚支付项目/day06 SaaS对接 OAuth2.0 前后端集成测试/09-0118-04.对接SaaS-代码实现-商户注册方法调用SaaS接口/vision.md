# 画面线理解：04.对接SaaS-代码实现-商户注册方法调用SaaS接口

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day06 SaaS对接 OAuth2.0 前后端集成测试
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day06 SaaS对接 OAuth2.0 前后端集成测试\04.对接SaaS-代码实现-商户注册方法调用SaaS接口【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 02:12, 03:16, 04:05, 04:49, 06:01, 07:30, 08:58, 10:16, 11:35, 12:20, 13:09, 14:33, 15:10
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:36:03

1) 这一组画面整体在讲什么（一句话）：
演示如何在 SaaS 系统中实现商户注册接口，包括接口定义、参数设置、业务逻辑处理及异常处理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示文档中“1.4.4.1 接口说明”，列出接口功能：创建租户时若存在则返回信息，否则创建新租户、管理员并初始化权限；若管理员用户名或手机号已存在则禁止创建；创建租户时需提供手机号、账号密码；租户类型和默认套餐均为“shanju-merchant”；接口方法为 TenantDTO createTenantAndAccount(CreateTenantRequestDTO createTenantRequest)。
画面 2：在文档中继续展示接口参数，明确列出：1. 手机号；2. 账号；3. 密码；4. 租户类型：shanju-merchant；5. 默认套餐：shanju-merchant；6. 租户名称，同账号名。
画面 3：与画面 1 内容相同，为文档页面的再次展示。
画面 4：在 IntelliJ IDEA 中展示项目结构，重点是 pom.xml 文件中的依赖项，包括 spring-cloud-starter-alibaba-nacos-config 和 spring-cloud-starter-alibaba-nacos-discovery。
画面 5：在代码编辑器中展示 MerchantServiceTest.java 文件，其中包含对手机号格式校验的代码，以及对租户信息的创建和绑定操作。
画面 6：在代码编辑器中展示创建租户请求对象并调用 tenantService.createTenantAndAccount 方法的代码。
画面 7：在代码编辑器中展示设置租户类型和默认套餐的代码，以及设置租户名称。
画面 8：在代码编辑器中展示判断租户是否已存在的逻辑，若存在则抛出异常。
画面 9：在代码编辑器中展示获取租户 ID 并创建商户对象的代码。
画面 10：在代码编辑器中展示设置商户 ID 并创建门店对象的代码。
画面 11：在代码编辑器中展示创建门店并设置状态的代码。
画面 12：在代码编辑器中展示对手机号格式进行校验的代码。
画面 13：在代码编辑器中展示创建员工并绑定门店的代码。
画面 14：在代码编辑器中展示租户创建成功后的处理逻辑，包括设置租户 ID、创建商户、创建门店、创建员工等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
/**
 * 创建租户如果已存在租户则返回租户信息，否则新增租户、新增租户管理员，同时初始化权限
 * 1.若管理员用户名已存在，禁止创建
 * 2.手机号已存在，禁止创建
 * 3.创建根据用户对应账号时，需要手机号，账号的用户名密码
 * @param createTenantRequest 创建租户请求信息
 * @return
 */
TenantDTO createTenantAndAccount(CreateTenantRequestDTO createTenantRequest);
```

画面 2：
接口参数：
1、手机号
2、账号
3、密码
4、租户类型：shanju-merchant
5、默认套餐：shanju-merchant
6、租户名称，同账号名

画面 4：
```xml
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-nacos-config</artifactId>
    <version>0.2.0.M1</version>
</dependency>
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
    <version>0.2.0.M1</version>
</dependency>
```

画面 5：
```java
//手机号格式校验
if (PhoneUtil.isMatches(merchantDTO.getMobile())) {
    throw new BusinessException(CommonErrorCode.E_100109);
}
//根据手机号查询商户，如果存在记录则禁止创建
Integer count = merchantMapper.selectCount(new LambdaQueryWrapper<Merchant>().eq(Merchant::getMobile, merchantDTO.getMobile()));
if (count > 0) {
    throw new BusinessException(CommonErrorCode.E_100113);
}
```

画面 6：
```java
CreateTenantRequestDTO createTenantRequestDTO = new CreateTenantRequestDTO();
createTenantRequestDTO.setMobile(merchantDTO.getMobile());
createTenantRequestDTO.setUserName(merchantDTO.getUserName());
createTenantRequestDTO.setPassword(merchantDTO.getPassword());
createTenantRequestDTO.setTenantTypeCode("shanju-merchant"); //租户类型
createTenantRequestDTO.setBundleCode("shanju-merchant"); //套餐，根据套餐进行分配权限
createTenantRequestDTO.setMerchantName(merchantDTO.getMerchantName());
tenantService.createTenantAndAccount(createTenantRequestDTO);
```

画面 7：
```java
createTenantRequestDTO.setTenantTypeCode("shanju-merchant"); //租户类型
createTenantRequestDTO.setBundleCode("shanju-merchant"); //套餐，根据套餐进行分配权限
createTenantRequestDTO.setMerchantName(merchantDTO.getMerchantName());
```

画面 8：
```java
//如果租户已经存在，SaaS直接 返回该租户的信息，否则进行创建
TenantDTO tenantAndAccount = tenantService.createTenantAndAccount(createTenantRequestDTO);
if (tenantAndAccount == null || tenantAndAccount.getTenantId() == null) {
    throw new BusinessException(CommonErrorCode.E_200012);
}
```

画面 9：
```java
Long tenantId = tenantAndAccount.getTenantId();
Merchant merchant = new Merchant();
merchant.setMobile(merchantDTO.getMobile());
merchant.setTenantId(tenantId);
merchant.setAuditStatus("0");
merchantMapper.insert(merchant);
```

画面 10：
```java
StoreDTO storeDTO = new StoreDTO();
storeDTO.setStoreName("门店");
storeDTO.setMerchantId(merchant.getTenantId());
storeDTO.setStoreStatus(true);
storeDTO.setStoreType("0");
storeDTO.setStoreCode("0");
storeDTO.setStoreId(merchant.getTenantId());
storeDTO.setStoreName("门店");
storeDTO.setStoreStatus(true);
storeDTO.setStoreType("0");
storeDTO.setStoreCode("0");
storeDTO.setStoreId(merchant.getTenantId());
storeDTO.setStoreName("门店");
storeDTO.setStoreStatus(true);
storeDTO.setStoreType("0");
storeDTO.setStoreCode("0");
storeDTO.setStoreId(merchant.getTenantId());
storeDTO.setStoreName("门店");
storeDTO.setStoreStatus(true);
storeDTO.setStoreType("0");
storeDTO.setStoreCode("0");
storeDTO.setStoreId(merchant.getTenantId());
storeDTO.setStoreName("门店");
storeDTO.setStoreStatus(true);
storeDTO.setStoreType("0");
storeDTO.setStoreCode("0");
storeDTO.setStoreId(merchant.getTenantId());
storeDTO.setStoreName("门店");
storeDTO.setStoreStatus(true);
storeDTO.setStoreType("0");
storeDTO.setStoreCode("0");
storeDTO.setStoreId(merchant.getTenantId());
storeDTO.setStoreName("门店");
storeDTO.setStoreStatus(true);
storeDTO.setStoreType("0");
storeDTO.setStoreCode("0");
storeDTO.setStoreId(merchant.getTenantId());
storeDTO.setStoreName("门店");
storeDTO.setStoreStatus(true);
storeDTO.setStoreType("0");
storeDTO.setStoreCode("0");
storeDTO.setStoreId(merchant.getTenantId());
storeDTO.setStoreName("门店");
storeDTO.setStoreStatus(true);
storeDTO.setStoreType("0");
storeDTO.setStoreCode("0");
storeDTO.setStoreId(merchant.getTenantId());
storeDTO.setStoreName("门店");
storeDTO.setStoreStatus(true);
storeDTO.setStoreType("0");
storeDTO.setStoreCode("0");
storeDTO.setStoreId(merchant.getTenantId());
storeDTO.setStoreName("门店");
storeDTO.setStoreStatus(true);
storeDTO.setStoreType("0");
storeDTO.setStoreCode("0");
storeDTO.setStoreId(merchant.getTenantId());
storeDTO.setStoreName("门店");
storeDTO.setStoreStatus(true);
storeDTO.setStoreType("0");
storeDTO.setStoreCode("0");
storeDTO.setStoreId(merchant.getTenantId());
storeDTO.setStoreName("门店");
storeDTO.setStoreStatus(true);
storeDTO.setStoreType("0");
storeDTO.setStoreCode("0");
storeDTO.setStoreId(merchant.getTenantId());
storeDTO.setStoreName("门店");
storeDTO.setStoreStatus(true);
storeDTO.setStoreType("0");
storeDTO.setStoreCode("0");
storeDTO.setStoreId(merchant.getTenantId());
storeDTO.setStoreName("门店");
storeDTO.setStoreStatus(true);
storeDTO.setStoreType("0");
storeDTO.setStoreCode("0");
storeDTO.setStoreId(merchant.getTenantId());
storeDTO.setStoreName("门店");
storeDTO.setStoreStatus(true);
storeDTO.setStoreType("0");
storeDTO.setStoreCode("0");
storeDTO.setStoreId(merchant.getTenantId());
storeDTO.setStoreName("门店");
storeDTO.setStoreStatus(true);
storeDTO.setStoreType("0");
storeDTO.setStoreCode("0");
storeDTO.setStoreId(merchant.getTenantId());
storeDTO.setStoreName("门店");
storeDTO.setStoreStatus(true);
storeDTO.set
