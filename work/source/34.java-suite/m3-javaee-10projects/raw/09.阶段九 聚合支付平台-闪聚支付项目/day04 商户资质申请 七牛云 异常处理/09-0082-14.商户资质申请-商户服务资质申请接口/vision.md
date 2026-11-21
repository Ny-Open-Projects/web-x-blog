# 画面线理解：14.商户资质申请-商户服务资质申请接口

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day04 商户资质申请 七牛云 异常处理
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day04 商户资质申请 七牛云 异常处理\14.商户资质申请-商户服务资质申请接口【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:04, 01:35, 02:17, 03:05, 04:13, 04:52, 06:01, 06:49, 07:26, 08:25, 09:34, 10:05, 10:34, 11:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:10:09

1) 这一组画面整体在讲什么（一句话）：
讲解商户服务资质申请接口的定义与实现，包括接口方法签名、DTO类结构、数据校验及数据库操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT内容，标题为“3.4 资质申请”，子标题“3.4.1 商户服务资质申请(接口②)”，并列出“3.4.1.1 接口定义”和“3.4.1.2 接口实现”等小节。画面中代码片段显示在MerchantService中定义applyMerchant接口，注释为“/** 资质申请 * @param merchantId 商户id * @param merchantDTO 资质申请信息 * @throws BusinessException */ public void applyMerchant(long merchantId,MerchantDTO merchantDTO) throws BusinessException;”。

画面2：展示数据库表结构，表名为“merchant”，字段包括：MERCHANT_NAME、MERCHANT_ID、MERCHANT_ADDRESS、MERCHANT_TYPE、BUSINESS_LICENSES_IMG、ID_CARD_FRONT_IMG、ID_CARD_AFTER_IMG、USERNAME、MOBILE、CONTACTS_ADDRESS、AUDIT_STATUS、TENANT_ID等。

画面3：展示MerchantService接口定义，包含方法：queryMerchantById(Long id) 和 createMerchant(MerchantDTO merchantDTO) throws BusinessException。

画面4：展示MerchantDTO类定义，包含字段：id、merchantName、merchantNo、merchantAddress、merchantType，每个字段上都有@ApiModelProperty注解。

画面5：展示MerchantServiceImpl类中applyMerchant方法的实现，代码中使用了merchantMapper.selectById(merchantId)查询商户信息。

画面6：展示数据库表“merchant”的数据，包含两条记录，ID分别为1和121124860145481265，其他字段均为NULL。

画面7：展示PPT内容，标题为“3.4.1.2 接口实现”，并提示“实现MerchantServiceImpl 中的applyMerchant方法”。

画面8：展示MerchantServiceImpl类中applyMerchant方法的实现，代码中使用了merchantMapper.selectById(merchantId)查询商户信息。

画面9：展示MerchantDTO类定义，包含字段：id、merchantName、merchantNo、merchantAddress、merchantType，每个字段上都有@ApiModelProperty注解。

画面10：展示MerchantServiceImpl类中applyMerchant方法的实现，代码中使用了merchantMapper.selectById(merchantId)查询商户信息。

画面11：展示MerchantServiceImpl类中applyMerchant方法的实现，代码中使用了merchantMapper.selectById(merchantId)查询商户信息。

画面12：展示MerchantServiceImpl类中applyMerchant方法的实现，代码中使用了merchantMapper.selectById(merchantId)查询商户信息。

画面13：展示MerchantDTO类定义，包含字段：idCardFrontImg、idCardAfterImg、username、mobile、contactsAddress、auditStatus、tenantId，每个字段上都有@ApiModelProperty注解。

画面14：展示PPT内容，标题为“3.4.1.2 接口实现”，并提示“实现MerchantServiceImpl 中的applyMerchant方法”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面1：
```java
/**
 * 资质申请
 * @param merchantId 商户id
 * @param merchantDTO 资质申请信息
 * @throws BusinessException
 */
public void applyMerchant(long merchantId,MerchantDTO merchantDTO) throws BusinessException;
```

画面2：
无代码，仅展示数据库表结构。

画面3：
```java
/**
 * Created by Administrator.
 */
public interface MerchantService {
    /**
     * 根据id查询商户
     * @param id 商户id
     * @return 商户信息
     */
    public MerchantDTO queryMerchantById(Long id);

    /**
     * 注册商户服务多步，接收参数、密码、手机号，为了可扩展性使用@merchantId关联绑定
     * @param merchantDTO 商户注册信息
     * @return 注册成功的商户信息
     * @throws BusinessException
     */
    MerchantDTO createMerchant(MerchantDTO merchantDTO) throws BusinessException;
}
```

画面4：
```java
/**
 * 资质申请
 * @param merchantId 商户id
 * @param merchantDTO 资质申请信息
 * @throws BusinessException
 */
public class MerchantDTO implements Serializable {

    private static final long serialVersionUID = 1L;

    @ApiModelProperty(value = "主键")
    private Long id;

    @ApiModelProperty(value = "商户名称")
    private String merchantName;

    @ApiModelProperty(value = "企业编号")
    private Long merchantNo;

    @ApiModelProperty(value = "企业地址")
    private String merchantAddress;

    @ApiModelProperty(value = "商户类型")
    private String merchantType;
}
```

画面5：
```java
/**
 * 资质申请
 * @param merchantId 商户id
 * @param merchantDTO 资质申请信息
 * @throws BusinessException
 */
public void applyMerchant(Long merchantId, MerchantDTO merchantDTO) throws BusinessException {
    if (merchantId == null || merchantDTO == null) {
        throw new BusinessException(CommonErrorCode.E_300009);
    }

    //校验merchantId合法性，查询商户表，如果查询不到记录，认为非法
    Merchant merchant = merchantMapper.selectById(merchantId);
    if (merchant == null) {
        throw new BusinessException(CommonErrorCode.E_200002);
    }

    //转换entity
    Merchant entity = MerchantConvert.INSTANCE.dtoEntity(merchantDTO);
    //有必要参数强制赋值
    merchantDTO.setMerchantName(entity.getMerchantName());
    merchantDTO.setMerchantNo(entity.getMerchantNo());
    merchantDTO.setMerchantAddress(entity.getMerchantAddress());
    merchantDTO.setMerchantType(entity.getMerchantType());
    merchantDTO.setMobile(entity.getMobile());
    merchantDTO.setAuditStatus("1"); //审核状态：已申请待审核
    //调用mapper更新商户
    merchantMapper.updateById(entity);
}
```

画面6：
无代码，仅展示数据库表数据。

画面7：
```java
/**
 * 资质申请
 * @param merchantId 商户id
 * @param merchantDTO 资质申请信息
 * @throws BusinessException
 */
public void applyMerchant(long merchantId,MerchantDTO merchantDTO) throws BusinessException;
```

画面8：
```java
/**
 * 资质申请
 * @param merchantId 商户id
 * @param merchantDTO 资质申请信息
 * @throws BusinessException
 */
public void applyMerchant(Long merchantId, MerchantDTO merchantDTO) throws BusinessException {
    if (merchantId == null || merchantDTO == null) {
        throw new BusinessException(CommonErrorCode.E_300009);
    }

    //校验merchantId合法性，查询商户表，如果查询不到记录，认为非法
    Merchant merchant = merchantMapper.selectById(merchantId);
    if (merchant == null) {
        throw new BusinessException(CommonErrorCode.E_200002);
    }

    //转换entity
    Merchant entity = MerchantConvert.INSTANCE.dtoEntity(merchantDTO);
    //有必要参数强制赋值
    merchantDTO.setMerchantName(entity.getMerchantName());
    merchantDTO.setMerchantNo(entity.getMerchantNo());
    merchantDTO.setMerchantAddress(entity.getMerchantAddress());
    merchantDTO.setMerchantType(entity.getMerchantType());
    merchantDTO.setMobile(entity.getMobile());
    merchantDTO.setAuditStatus("1"); //审核状态：已申请待审核
    //调用mapper更新商户
    merchantMapper.updateById(entity);
}
```

画面9：
```java
/**
 * 资质申请
 * @param merchantId 商户id
 * @param merchantDTO 资质申请信息
 * @throws BusinessException
 */
public class MerchantDTO implements Serializable {

    private static final long serialVersionUID = 1L;

    @ApiModelProperty(value = "主键")
    private Long id;

    @ApiModelProperty(value = "商户名称")
    private String merchantName;

    @ApiModelProperty(value = "企业编号")
    private Long merchantNo;

    @ApiModelProperty(value = "企业地址")
    private String merchantAddress;

    @ApiModelProperty(value = "商户类型")
    private String merchantType;
}
```

画面10：
```java
/**
 * 资质申请
 * @param merchantId 商户id
 * @param merchantDTO 资质申请信息
 * @throws BusinessException
 */
public void applyMerchant(Long merchantId, MerchantDTO merchantDTO) throws BusinessException {
    if (merchantId == null || merchantDTO == null) {
        throw new BusinessException(CommonErrorCode.E_300009);
    }

    //校验merchantId合法性，查询商户表，如果查询不到记录，认为非法
    Merchant merchant = merchantMapper.selectById(merchantId);
    if (merchant == null) {
        throw new BusinessException(CommonErrorCode.E_200002);
    }

    //转换entity
    Merchant entity = MerchantConvert.INSTANCE.dtoEntity(merchantDTO);
    //有必要参数强制赋值
    merchantDTO.setMerchantName(entity.getMerchantName());
    merchantDTO.setMerchantNo(entity.getMerchantNo());
    merchantDTO.setMerchantAddress(entity.getMerchantAddress());
    merchantDTO.setMerchantType(entity.getMerchantType());
    merchantDTO.setMobile(entity.getMobile());
    merchantDTO.setAuditStatus("1"); //审核状态：已申请待审核
