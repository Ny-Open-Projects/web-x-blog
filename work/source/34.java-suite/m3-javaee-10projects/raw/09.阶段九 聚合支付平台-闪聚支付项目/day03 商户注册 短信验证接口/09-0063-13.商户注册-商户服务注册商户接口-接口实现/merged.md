# 13.商户注册-商户服务注册商户接口-接口实现

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day03 商户注册 短信验证接口
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day03 商户注册 短信验证接口\13.商户注册-商户服务注册商户接口-接口实现【海量资源尽在 666java.com】.mp4
- 时长 4分16秒（音频 256s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下边呢我们就开始来写商户服务注册商户的接口实现部分好那么我们来看一下首先我们进入商户服务的这个工程然后呢在这儿我们要写这个接口实现那么这个接口的实现呢大家思考一下要怎么写呢其实很简单就是调用mappermapper呢其实就是我们看到的这个merchant Mapper对吧然后呢调用它干嘛是不是有一个叫insert方法哎那你就知道了
[00:32] 也就是上面我要定义一个什么insert的方法所需要的这个merchant这个类型的对象然后将来呢我们就在这个对象当中我们去set一些数据那比如说我要set手机号吧因为我们说手机号最终是不是要写到这个商户表啊所以那我就放你这大家看懂了吗那最终你是不是要把什么
[01:04] 要把这个对象呢再传回去但是在传回这个对象的时候你看啊要向DTO当中写入新增商户的ID要再返回所以这里边呢你要set一下IDID呢其实就是这个merchant这个里边的ID这个大家能看懂吗就是这里边执行insert之后呢这个merchant的对象原来你6的时候它肯定是一个空对象吧但是你insert之后呢
[01:34] 这个组件呢就已经写进去了就是myvts plus帮助我们做完了所以你把这个写入成功的这个对象里面的ID然后写到DTO然后呢再回传回去再传回去作为返回数据那好其实这就是我们的这个什么注册的代码就很简单那后期如果说我们的需求有变更我们说啊你注册的时候不光要写手机号你还要写一些其他的
[02:05] 属性那这个时候我们就可以继续往这加代码就行了比如说在set比如说写username那你这里边的你就是get username大家看懂了吗对就这样好那这个呢就是我们说的什么啊哎商户注册在商户服务当中的一个什么接口的实现是不是很简单呀对好那这个商户注册哎
[02:35] 商户服务的接口我们写完了之后呢我们再回到原来的这个需求里头啊我们来看一下刚才我们写的代码是不是把手机号写到数据库了这些你一看是不是都是资质申请的时候才写了我们就可以不管但是有一个你好像落了就是这个什么申请的状态这个审核申请的状态默认就是零就是未申请啥意思啊就表示这个商户只是注册成功还没有进行资质申请所以
[03:04] 我们应该在哪里呀对在这儿看好啊在这儿我们要设置三审核的状态为什么呢为零为零是不是就是未申请啊未进行资质申请好那其实你只要把这个代码给他写死就行了那你说老师你写死了这是不是就算硬编码了呀
[03:38] 怎么写死那我就写零吧对所以这里面就不是硬编码虽然你写的是硬编码但是呢我们说其实在你的数据规范约定当中你就已经约定好了说什么呀这个零啊就表示未申请就相当于我们的系统代码了所以这里面虽然是硬编码但是呢我们这样写也没有问题零就代表我们说的未进行自制申请你这样写是可以的好这就是我们说的这个
[04:06] 商户服务的商户定义商户注册的一个定义开发好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

