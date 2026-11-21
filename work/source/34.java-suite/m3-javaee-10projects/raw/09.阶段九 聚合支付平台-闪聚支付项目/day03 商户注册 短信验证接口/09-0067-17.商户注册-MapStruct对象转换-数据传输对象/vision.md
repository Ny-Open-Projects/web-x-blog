# 画面线理解：17.商户注册-MapStruct对象转换-数据传输对象

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day03 商户注册 短信验证接口
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day03 商户注册 短信验证接口\17.商户注册-MapStruct对象转换-数据传输对象【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:18, 00:37, 01:08, 01:18, 03:09, 03:35, 03:42, 03:47, 03:59, 04:03, 04:09, 04:14, 04:46, 05:00
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:59:13

1) 这一组画面整体在讲什么（一句话）：
讲解商户注册功能中数据传输对象（DTO）的定义、使用规范及在不同层级（应用层、服务层、持久层）的传输规则。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示PPT内容，讲解数据传输对象（DTO）的三种类型：MerchantRegisterVO、MerchantDTO、entity，并附带一个应用层→服务层→持久层的流程图。
画面2：展示IDE中MerchantController.java的代码，其中包含一个用于测试的@GetMapping("/hello")方法和一个用于商户注册的@PostMapping("/merchants/register")方法，该方法中使用了merchantService.createMerchant(merchantDTO)。
画面3：IDE中展示项目结构，鼠标悬停在“Merchant”包上。
画面4：PPT内容，继续讲解数据传输对象的定义和用途。
画面5：PPT内容，展示本项目数据传输对象的规范，包括应用层、服务层和持久层的传输规则。
画面6：PPT内容，展示数据传输对象的规范，强调应用层使用DTO结尾的对象传输。
画面7：IDE中展示MerchantController.java的代码，其中包含一个用于商户注册的@PostMapping("/merchants/register")方法，该方法中使用了merchantService.createMerchant(merchantDTO)。
画面8：IDE中展示MerchantRegisterVO类的代码，其中包含多个字段，如mobile、username、password、verifyKey、verifyCode。
画面9：PPT内容，展示数据传输对象的规范，强调应用层使用DTO结尾的对象传输。
画面10：IDE中展示MerchantRegisterVO类的代码，其中包含多个字段，如mobile、username、password、verifyKey、verifyCode。
画面11：IDE中展示Merchant类的代码，其中包含多个字段，如merchantName、merchantNo、merchantAddress。
画面12：IDE中展示Merchant类的代码，其中包含多个字段，如idCardFrontImg、idCardAfterImg、username。
画面13：PPT内容，展示数据传输对象的规范，包括应用层、服务层和持久层的传输规则。
画面14：PPT内容，展示数据传输对象的定义和用途。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2代码：
```java
@PostMapping("/merchants/register")
public MerchantRegisterVO registerMerchant(@RequestBody MerchantRegisterVO merchantRegisterVO) {
    //校验验证码
    smsService.checkVerifyCode(merchantRegisterVO.getVerifykey(), merchantRegisterVO.getPhone());
    //传入商户信息
    MerchantDTO merchantDTO = new MerchantDTO();
    merchantDTO.setMobile(merchantRegisterVO.getMobile());
    merchantDTO.setUserName(merchantRegisterVO.getUserName());
    merchantDTO.setPassword(merchantRegisterVO.getPassword());
    merchantDTO.setVerifyKey(merchantRegisterVO.getVerifyKey());
    merchantDTO.setVerifyCode(merchantRegisterVO.getVerifyCode());
    //调用服务层
    return merchantService.createMerchant(merchantDTO);
}
```

画面7代码：
```java
@PostMapping("/merchants/register")
public MerchantRegisterVO registerMerchant(@RequestBody MerchantRegisterVO merchantRegisterVO) {
    //校验验证码
    smsService.checkVerifyCode(merchantRegisterVO.getVerifykey(), merchantRegisterVO.getPhone());
    //传入商户信息
    MerchantDTO merchantDTO = new MerchantDTO();
    merchantDTO.setMobile(merchantRegisterVO.getMobile());
    merchantDTO.setUserName(merchantRegisterVO.getUserName());
    merchantDTO.setPassword(merchantRegisterVO.getPassword());
    merchantDTO.setVerifyKey(merchantRegisterVO.getVerifyKey());
    merchantDTO.setVerifyCode(merchantRegisterVO.getVerifyCode());
    //调用服务层
    return merchantService.createMerchant(merchantDTO);
}
```

画面8代码：
```java
public class MerchantRegisterVO implements Serializable {
    @ApiModelProperty("商户手机号")
    private String mobile;
    @ApiModelProperty("商户用户名")
    private String username;
    @ApiModelProperty("商户密码")
    private String password;
    @ApiModelProperty("验证码key")
    private String verifyKey;
    @ApiModelProperty("验证码")
    private String verifyCode;
}
```

画面11代码：
```java
@TableField("MERCHANT_NAME")
private String merchantName;
@TableField("MERCHANT_NO")
private Long merchantNo;
@TableField("MERCHANT_ADDRESS")
private String merchantAddress;
```

画面12代码：
```java
@TableField("ID_CARD_FRONT_IMG")
private String idCardFrontImg;
@TableField("ID_CARD_AFTER_IMG")
private String idCardAfterImg;
@TableField("USERNAME")
private String username;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1、4、5、6、9、13、14：PPT标题为“2.4.4 MapStruct对象转换”，子标题为“2.4.4.1 数据传输对象”。内容包括：
- 数据传输对象（DTO）的三种类型：MerchantRegisterVO、MerchantDTO、entity。
- 一个流程图：Application → DTO → Service (Dubbo) → Entity → Mapper。
- 本项目数据传输对象的规范：
  1. 应用层：如没有接口参数的特殊要求，应用层使用DTO结尾的对象传输，否则单独定义VO结尾的对象传输。
  2. 服务层：统一使用DTO结尾的对象传输。
  3. 持久层：统一使用Entity对象传输。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
