# 画面线理解：13.商户注册-商户服务注册商户接口-接口实现

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day03 商户注册 短信验证接口
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day03 商户注册 短信验证接口\13.商户注册-商户服务注册商户接口-接口实现【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:11, 00:23, 00:39, 00:44, 00:55, 01:35, 01:53, 02:16, 02:36, 02:41, 03:46, 04:05, 04:10
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:56:22

1) 这一组画面整体在讲商户注册接口的实现，包括接口定义、数据模型设计和代码编写。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了系统交互流程图，其中包含“账号注册”界面和“商户表”、“员工表”、“SaaS系统”三个数据实体，用箭头表示数据流向。
画面2: IDE中显示MerchantService接口定义，代码中注释说明了接口功能，方法createMerchant接收MerchantDTO参数并返回MerchantDTO。
画面3: IDE中显示MerchantServiceImpl类中queryMerchantById方法的实现，用于根据ID查询商户信息。
画面4: IDE中显示MerchantServiceImpl类中createMerchant方法的实现，注释说明了方法功能。
画面5: IDE中显示MerchantServiceImpl类中createMerchant方法的实现，光标位于方法体中。
画面6: IDE中显示MerchantServiceImpl类中createMerchant方法的实现，光标位于方法体中，弹出的自动补全建议列表显示了Merchant类的属性和方法。
画面7: IDE中显示Merchant实体类的代码，定义了商户的属性和注解。
画面8: IDE中显示MerchantServiceImpl类中createMerchant方法的实现，光标位于方法体中。
画面9: IDE中显示MerchantServiceImpl类中createMerchant方法的实现，光标位于方法体中，弹出的自动补全建议列表显示了Merchant类的属性和方法。
画面10: PPT页面，标题为“2.4.2.2 接口实现”，内容为“实现MerchantServiceImpl中的createMerchant方法：”，并展示了代码。
画面11: PPT页面，标题为“商户注册表的数据模型如下：”，并展示了商户表的字段、类型和注释。
画面12: 数据库管理工具中显示merchant表的结构，列出了字段、类型和注释。
画面13: PPT页面，标题为“商户注册表的数据模型如下：”，并展示了商户表的字段、类型和注释。
画面14: PPT页面，标题为“2.4.3 商户平台应用注册商户(接口③)”，并展示了接口定义和代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2:
```java
// 注册商户服务接口，接收账号、密码、手机号，为了可扩展性使用merchantDto接收数据
@Override
public MerchantDTO createMerchant(MerchantDTO merchantDTO) {
    // Mapper向数据库写入记录
    return null;
}
```

画面3:
```java
@Authorized
MerchantMapper merchantMapper;
@Override
public MerchantDTO queryMerchantById(Long id) {
    MerchantDTO merchantDTO = new MerchantDTO();
    merchantDTO.setMerchantBase(merchant.getMerchantBase());
    merchantDTO.setMerchantName(merchant.getMerchantName());
    ...
    return merchantDTO;
}
```

画面4:
```java
// 注册商户服务接口，接收账号、密码、手机号，为了可扩展性使用merchantDto接收数据
// Return 注册成功的商户信息
@Override
public MerchantDTO createMerchant(MerchantDTO merchantDTO) {
    // Mapper向数据库写入记录
    return null;
}
```

画面5:
```java
Merchant merchant = new Merchant();
merchant.setMobile(merchantDTO.getMobile());
merchantMapper.insert(merchant);
return null;
```

画面6:
```java
Merchant merchant = new Merchant();
merchant.setMobile(merchantDTO.getMobile());
merchantMapper.insert(merchant);
return null;
```

画面7:
```java
package com.shanjugy.merchant.entity;
import ...
@TableName("merchant")
public class Merchant implements Serializable {
    private static final long serialVersionUID = 1L;
    // 主键
    @TableId(value = "ID", type = IdType.ID_WORKER)
    private Long id;
    // 商户名称
    @TableField("MERCHANT_NAME")
    private String merchantName;
```

画面8:
```java
@Override
public MerchantDTO createMerchant(MerchantDTO merchantDTO) {
    Merchant merchant = new Merchant();
    merchant.setMobile(merchantDTO.getMobile());
    // Mapper向数据库写入记录
    merchantMapper.insert(merchant);
    // 将新商户id返回
    merchantDTO.setId(merchant.getId());
    return merchantDTO;
}
```

画面9:
```java
@Override
public MerchantDTO createMerchant(MerchantDTO merchantDTO) {
    Merchant merchant = new Merchant();
    merchant.setMobile(merchantDTO.getMobile());
    // Mapper向数据库写入记录
    merchantMapper.insert(merchant);
    // 将新商户id返回
    merchantDTO.setId(merchant.getId());
    return merchantDTO;
}
```

画面10:
```java
@org.apache.dubbo.config.annotation.Service
@Sifaj
public class MerchantServiceImpl implements MerchantService {
    @Override
    @Transactional
    public MerchantDTO createMerchant(MerchantDTO merchantDTO) {
        Merchant merchant = new Merchant();
        // 设置审核状态0-未申请,1-已申请待审核,2-审核通过,3-审核拒绝
        merchant.setAuditStatus("0");
        // 设置手机号
        merchant.setMobile(merchantDTO.getMobile());
        ...
        // 保存商户
        merchantMapper.insert(merchant);
        // 将新商户id返回
        merchantDTO.setId(merchant.getId());
        return merchantDTO;
    }
}
```

画面11:
```text
Field	Type	Comment
ID	bigint(20)	主键
MERCHANT_NAME	varchar(50)	商户名称	资质申请时完善
MERCHANT_NO	bigint(20)	企业编号	资质申请时完善
MERCHANT_ADDRESS	varchar(255)	企业地址	资质申请时完善
MERCHANT_TYPE	varchar(50)	商户类型	资质申请时完善
BUSINESS_LICENSES_IMG	varchar(100)	营业执照（企业证明）	资质申请时完善
ID_CARD_FRONT_IMG	varchar(100)	法人身份证正面照片	资质申请时完善
ID_CARD_AFTER_IMG	varchar(100)	法人身份证反面照片	资质申请时完善
USERNAME	varchar(50)	联系人姓名	资质申请时完善
MOBILE	varchar(50)	联系人手机号（关联第一账号）	注册时写入。
CONTACTS_ADDRESS	varchar(255)	联系人地址	资质申请时完善
AUDIT_STATUS	varchar(20)	审核状态 0-未申请,1-已申请待审核,2-审核通过,3-审核拒绝	注册成功的默认为0
TENANT_ID	bigint(20)	租户ID，关联统一用户	关联SaaS
```

画面12:
```text
Columns (13)
Field	Type	Comment
ID	bigint(20)	主键
MERCHANT_NAME	varchar(50)	商户名称
MERCHANT_NO	bigint(20)	企业编号
MERCHANT_ADDRESS	varchar(255)	企业地址
MERCHANT_TYPE	varchar(50)	商户类型
BUSINESS_LICENSES_IMG	varchar(100)	营业执照（企业证明）
ID_CARD_FRONT_IMG	varchar(100)	法人身份证正面照片
ID_CARD_AFTER_IMG	varchar(100)	法人身份证反面照片
USERNAME	varchar(50)	联系人姓名
MOBILE	varchar(50)	联系人手机号（关联第一账号）
CONTACTS_ADDRESS	varchar(255)	联系人地址
AUDIT_STATUS	varchar(20)	审核状态 0-未申请,1-已申请待审核,2-审核通过,3-审核拒绝
TENANT_ID	bigint(20)	租户ID，关联统一用户
```

画面13:
```text
Field	Type	Comment
ID	bigint(20)	主键
MERCHANT_NAME	varchar(50)	商户名称	资质申请时完善
MERCHANT_NO	bigint(20)	企业编号	资质申请时完善
MERCHANT_ADDRESS	varchar(255)	企业地址	资质申请时完善
MERCHANT_TYPE	varchar(50)	商户类型	资质申请时完善
BUSINESS_LICENSES_IMG	varchar(100)	营业执照（企业证明）	资质申请时完善
ID_CARD_FRONT_IMG	varchar(100)	法人身份证正面照片	资质申请时完善
ID_CARD_AFTER_IMG	varchar(100)	法人身份证反面照片	资质申请时完善
USERNAME	varchar(50)	联系人姓名	资质申请时完善
MOBILE	varchar(50)	联系人手机号（关联第一账号）	注册时写入。
CONTACTS_ADDRESS	varchar(255)	联系人地址	资质申请时完善
AUDIT_STATUS	varchar(20)	审核状态 0-未申请,1-已申请待审核,2-审核通过,3-审核拒绝	注册成功的默认为0
TENANT_ID	bigint(20)	租户ID，关联统一用户	关联SaaS
```

画面14:
```java
@Transactional
public MerchantDTO createMerchant(MerchantDTO merchantDTO) {
    Merchant merchant = new Merchant();
    // 设置审核状态0-未申请,1-已申请待审核,2-审核通过,3-审核拒绝
