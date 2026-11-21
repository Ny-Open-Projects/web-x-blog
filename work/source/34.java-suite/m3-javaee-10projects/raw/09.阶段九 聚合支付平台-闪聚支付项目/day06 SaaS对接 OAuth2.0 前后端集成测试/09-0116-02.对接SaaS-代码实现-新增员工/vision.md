# 画面线理解：02.对接SaaS-代码实现-新增员工

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day06 SaaS对接 OAuth2.0 前后端集成测试
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day06 SaaS对接 OAuth2.0 前后端集成测试\02.对接SaaS-代码实现-新增员工【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:21, 01:06, 02:52, 03:34, 04:31, 05:33, 06:54, 07:36, 08:19, 09:02, 09:45, 10:34, 11:48, 12:39
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:34:42

1) 这一组画面整体在讲什么（一句话）：
讲解商户服务中新增员工接口的实现，包括接口定义、StaffDTO数据结构、业务校验逻辑（手机号与用户名唯一性）及数据库操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示文档“1.4.2 商户服务新增员工接口”的“1.4.2.1 接口定义”部分，说明接口需接收员工数据、请求新增员工、并返回结果。同时指出在MerchantService接口类中定义该接口，代码片段为：
```java
/**
 * 商户新增员工
 * @param staffDTO
```

画面2：展示IDE中MerchantService接口定义，包含方法：
```java
StoreDTO createStore(StoreDTO storeDTO) throws BusinessException.
//新增员工
StaffDTO createStaff(StaffDTO staffDTO) throws BusinessException;
```

画面3：展示MerchantServiceImpl.java中createStaff方法的实现，包含参数校验：
```java
public StaffDTO createStaff(StaffDTO staffDTO) throws BusinessException {
    //参数合法性校验
    if(staffDTO == null || ...)
```

画面4：展示StaffDTO类的定义，包含字段及注解：
```java
/**
 * StaffDTO
 */
public class StaffDTO implements Serializable {
    private static final long serialVersionUID = 10L.
    @ApiModelProperty(value = "主键")
    private Long id;
    @ApiModelProperty(value = "商户ID")
    private Long merchantId;
    @ApiModelProperty(value = "姓名")
    private String fullName;
    @ApiModelProperty(value = "职位")
    private String position;
    @ApiModelProperty(value = "用户名(关联统一用户)")
    private String username;
```

画面5：展示createStaff方法中对手机号的校验逻辑，包含注释和代码：
```java
//手机号格式校验
if (!StringUtils.isMobilePhone(mobile)) {
    throw new BusinessException(CommonErrorCode.E_10011);
}
//手机号是否已存在
if (StringUtils.isNotBlank(mobile)) {
    if (count > 0) {
        throw new BusinessException(CommonErrorCode.E_10012);
    }
}
```

画面6：展示文档“1.4.4.1 接口说明”，说明SaaS系统为用户提供注册租户的接口，包含注释：
```java
/**
 * 创建租户如果已存在则返回租户信息，否则新增租户、新增租户管理员，同时初始化权限
 * 2.手机号已存在，禁止创建
 * 3.创建租户对应账号时，需要手机号，账号的用户名密码
 * @param createTenantRequest 创建租户请求信息
 * @return
 */
TenantDTO createTenantAndAccount(CreateTenantRequestDTO createTenantRequest);
```

画面7：展示MerchantService接口中queryMerchantById方法的实现：
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

画面8：展示isExistStaffByMobile方法的实现，包含注释和代码：
```java
Boolean isExistStaffByMobile(String mobile, String merchantId) {
    staffMapper.selectCount(new LambdaQueryWrapper<Staff>().eq(Staff::getMobile, mobile).eq(Staff::getMerchantId, merchantId));
}
```

画面9：展示isExistStaffByMobile方法的实现，包含注释和代码：
```java
//在同一个商户下员工的手机号唯一
Boolean existStaffByMobile(String mobile, Long merchantId) {
    staffMapper.selectCount(new LambdaQueryWrapper<Staff>().eq(Staff::getMobile, mobile).eq(Staff::getMerchantId, merchantId));
}
```

画面10：展示isExistStaffByMobile方法的实现，包含注释和代码：
```java
//在同一个商户下员工的手机号唯一
Boolean existStaffByMobile(String mobile, Long merchantId) {
    if (existStaffByMobile(mobile, merchantId)) {
        throw new BusinessException(CommonErrorCode.E_10013);
    }
    return null;
}
```

画面11：展示isExistStaffByUserName方法的实现，包含注释和代码：
```java
Boolean isExistStaffByUserName(String username, Long merchantId) {
    Integer count = staffMapper.selectCount(new LambdaQueryWrapper<Staff>().eq(Staff::getUsername, username).eq(Staff::getMerchantId, merchantId));
    return count > 0;
}
```

画面12：展示createStaff方法中对用户名的校验逻辑，包含注释和代码：
```java
//在同一个商户下员工的用户名唯一
Boolean existStaffByUserName(String username, Long merchantId) {
    if (existStaffByUserName(username, merchantId)) {
        throw new BusinessException(CommonErrorCode.E_10014);
    }
}
```

画面13：展示createStaff方法中对员工信息的插入操作，包含注释和代码：
```java
//员工手机号在同一个商户下唯一
Boolean existStaffByMobile(String mobile, Long merchantId) {
    if (existStaffByMobile(mobile, merchantId)) {
        throw new BusinessException(CommonErrorCode.E_10019);
    }
    //设置员工工作部门
    Staff staff = StaffConvert.INSTANCE.dto2Entity(staffDTO);
    staffMapper.insert(staff);
    return StaffConvert.INSTANCE.entity2DTO(staff);
}
```

画面14：展示isExistStaffByUserName方法的实现，包含注释和代码：
```java
/**
 * 根据账号判断员工是否在指定商户存在
 * @param username
 * @param merchantId
 * @return
 */
private boolean isExistStaffByUserName(String username, Long merchantId) {
    LambdaQueryWrapper<Staff> lambdaQueryWrapper = new LambdaQueryWrapper<Staff>();
    lambdaQueryWrapper.eq(Staff::getUsername, username).eq(Staff::getMerchantId, merchantId);
    int i = staffMapper.selectCount(lambdaQueryWrapper);
}
```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
（已在上文要点中完整抄录）

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
（无PPT或架构图/流程图）

5) 不要评价画面美观，不要输出与课程无关的内容。
（已遵守）
