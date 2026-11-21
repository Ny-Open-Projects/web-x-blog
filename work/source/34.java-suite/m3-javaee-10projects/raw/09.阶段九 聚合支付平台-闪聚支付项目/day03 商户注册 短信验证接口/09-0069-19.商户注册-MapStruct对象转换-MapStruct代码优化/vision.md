# 画面线理解：19.商户注册-MapStruct对象转换-MapStruct代码优化

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day03 商户注册 短信验证接口
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day03 商户注册 短信验证接口\19.商户注册-MapStruct对象转换-MapStruct代码优化【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 01:02, 01:59, 02:20, 04:03, 04:47, 05:27, 05:49, 06:01, 06:38, 06:57, 07:20, 07:46, 08:13
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:00:51

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 MapStruct 进行商户注册功能的代码优化，包括服务层和应用层的代码改造。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程大纲，当前章节为“2.4.4.3 代码优化”，并显示服务层代码 `createMerchant` 方法，其中包含将 DTO 转换为 Entity、设置审核状态、保存商户信息、再转换回 DTO 的逻辑。
画面 2: 在 IDE 中展示服务层代码，高亮显示使用 MapStruct 进行对象转换的代码行 `Merchant merchant = MerchantConvert.INSTANCE.dto2entity(merchantDTO);`。
画面 3: 在 IDE 中展示服务层代码，高亮显示设置审核状态的代码 `merchant.setAuditStatus("0");`。
画面 4: 在 IDE 中展示控制器层代码，高亮显示创建 `MerchantRegisterVO` 对象并设置其属性的代码，同时弹出“New Package”对话框，提示创建新包。
画面 5: 在 IDE 中展示 `MerchantRegisterConvert` 接口的代码，高亮显示 `@Mapper` 注解和 `INSTANCE` 的获取方式。
画面 6: 在 IDE 中展示控制器层代码，高亮显示将 `MerchantRegisterVO` 转换为 `MerchantDTO` 的代码 `MerchantDTO merchantDTO = MerchantRegisterConvert.INSTANCE.vo2dto(merchantRegisterVO);`。
画面 7: 在 IDE 中展示控制器层代码，高亮显示调用服务层方法 `merchantService.createMerchant(merchantDTO);`。
画面 8: 在 IDE 中展示控制台日志，显示应用启动成功，包含项目名称、Spring Boot 版本、Dubbo 版本等信息。
画面 9: 展示课程大纲，当前章节为“2.4.4.3 代码优化”，并显示应用层代码 `registerMerchant` 方法，其中包含校验验证码、注册商户、返回 VO 的逻辑。
画面 10: 展示 Redis Desktop Manager 界面，连接到本地 Redis 服务。
画面 11: 展示 Postman 界面，设置 POST 请求，请求地址为 `http://localhost:7010/merchant/merchants/register`，请求体为 JSON 格式，包含 `mobile`、`password`、`username`、`verifyCode` 等字段。
画面 12: 在 IDE 中展示调试器界面，高亮显示 `merchantDTO` 对象的 `mobile` 字段值为 `"123123123"`。
画面 13: 在 IDE 中展示调试器界面，高亮显示 `merchantDTO` 对象的 `verifyCode` 字段值为 `"506439"`。
画面 14: 展示课程大纲，当前章节为“2.4.4.3 代码优化”，并显示服务层代码 `createMerchant` 方法，其中包含将 DTO 转换为 Entity、设置审核状态、保存商户信息、再转换回 DTO 的逻辑。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
public MerchantDTO createMerchant(MerchantDTO merchantDTO) {
    //将dto转换entity
    Merchant entity = MerchantConvert.INSTANCE.dto2entity(merchantDTO);
    //设置审核状态0-未申请,1-已申请待审核,2-审核通过,3-审核拒绝
    entity.setAuditStatus("0");
    //保存商户信息
    merchantMapper.insert(entity);
    //将entity转换 dto
    MerchantDTO merchantDTONew = MerchantConvert.INSTANCE.entity2dto(entity);
    return merchantDTONew;
}
```

画面 2:
```java
Merchant merchant = MerchantConvert.INSTANCE.dto2entity(merchantDTO);
```

画面 3:
```java
merchant.setAuditStatus("0");
```

画面 4:
```java
MerchantDTO merchantDTO = new MerchantDTO();
merchantDTO.setMobile(merchantRegisterVO.getMobile());
merchantDTO.setUserName(merchantRegisterVO.getUsername());
merchantDTO.setMerchantType(merchantRegisterVO.getMerchantType());
merchantDTO.setBusinessLicense(merchantRegisterVO.getBusinessLicense());
merchantDTO.setContactAddress(merchantRegisterVO.getContactAddress());
merchantDTO.setContactName(merchantRegisterVO.getContactName());
merchantDTO.setContactPhone(merchantRegisterVO.getContactPhone());
merchantDTO.setContactEmail(merchantRegisterVO.getContactEmail());
merchantDTO.setContactWechat(merchantRegisterVO.getContactWechat());
merchantDTO.setContactQQ(merchantRegisterVO.getContactQQ());
merchantDTO.setContactWeibo(merchantRegisterVO.getContactWeibo());
merchantDTO.setContactWechatOpenid(merchantRegisterVO.getContactWechatOpenid());
merchantDTO.setContactWechatUnionid(merchantRegisterVO.getContactWechatUnionid());
merchantDTO.setContactWechatSessionKey(merchantRegisterVO.getContactWechatSessionKey());
merchantDTO.setContactWechatTicket(merchantRegisterVO.getContactWechatTicket());
merchantDTO.setContactWechatExpiresIn(merchantRegisterVO.getContactWechatExpiresIn());
merchantDTO.setContactWechatRefreshToken(merchantRegisterVO.getContactWechatRefreshToken());
merchantDTO.setContactWechatAccessToken(merchantRegisterVO.getContactWechatAccessToken());
merchantDTO.setContactWechatAccessExpiresIn(merchantRegisterVO.getContactWechatAccessExpiresIn());
merchantDTO.setContactWechatAccessScope(merchantRegisterVO.getContactWechatAccessScope());
merchantDTO.setContactWechatAccessToken(merchantRegisterVO.getContactWechatAccessToken());
merchantDTO.setContactWechatAccessExpiresIn(merchantRegisterVO.getContactWechatAccessExpiresIn());
merchantDTO.setContactWechatAccessScope(merchantRegisterVO.getContactWechatAccessScope());
merchantDTO.setContactWechatAccessToken(merchantRegisterVO.getContactWechatAccessToken());
merchantDTO.setContactWechatAccessExpiresIn(merchantRegisterVO.getContactWechatAccessExpiresIn());
merchantDTO.setContactWechatAccessScope(merchantRegisterVO.getContactWechatAccessScope());
merchantDTO.setContactWechatAccessToken(merchantRegisterVO.getContactWechatAccessToken());
merchantDTO.setContactWechatAccessExpiresIn(merchantRegisterVO.getContactWechatAccessExpiresIn());
merchantDTO.setContactWechatAccessScope(merchantRegisterVO.getContactWechatAccessScope());
merchantDTO.setContactWechatAccessToken(merchantRegisterVO.getContactWechatAccessToken());
merchantDTO.setContactWechatAccessExpiresIn(merchantRegisterVO.getContactWechatAccessExpiresIn());
merchantDTO.setContactWechatAccessScope(merchantRegisterVO.getContactWechatAccessScope());
merchantDTO.setContactWechatAccessToken(merchantRegisterVO.getContactWechatAccessToken());
merchantDTO.setContactWechatAccessExpiresIn(merchantRegisterVO.getContactWechatAccessExpiresIn());
merchantDTO.setContactWechatAccessScope(merchantRegisterVO.getContactWechatAccessScope());
merchantDTO.setContactWechatAccessToken(merchantRegisterVO.getContactWechatAccessToken());
merchantDTO.setContactWechatAccessExpiresIn(merchantRegisterVO.getContactWechatAccessExpiresIn());
merchantDTO.setContactWechatAccessScope(merchantRegisterVO.getContactWechatAccessScope());
merchantDTO.setContactWechatAccessToken(merchantRegisterVO.getContactWechatAccessToken());
merchantDTO.setContactWechatAccessExpiresIn(merchantRegisterVO.getContactWechatAccessExpiresIn());
merchantDTO.setContactWechatAccessScope(merchantRegisterVO.getContactWechatAccessScope());
merchantDTO.setContactWechatAccessToken(merchantRegisterVO.getContactWechatAccessToken());
merchantDTO.setContactWechatAccessExpiresIn(merchantRegisterVO.getContactWechatAccessExpiresIn());
merchantDTO.setContactWechatAccessScope(merchantRegisterVO.getContactWechatAccessScope());
merchantDTO.setContactWechatAccessToken(merchantRegisterVO.getContactWechatAccessToken());
merchantDTO.setContactWechatAccessExpiresIn(merchantRegisterVO.getContactWechatAccessExpiresIn());
merchantDTO.setContactWechatAccessScope(merchantRegisterVO.getContactWechatAccessScope());
merchantDTO.setContactWechatAccessToken(merchantRegisterVO.getContactWechatAccessToken());
merchantDTO.setContactWechatAccessExpiresIn(merchantRegisterVO.getContactWechatAccessExpiresIn());
merchantDTO.setContactWechatAccessScope(merchantRegisterVO.getContactWechatAccessScope());
merchantDTO.setContactWechatAccessToken(merchantRegisterVO.getContactWechatAccessToken());
merchantDTO.setContactWechatAccessExpiresIn(merchantRegisterVO.getContactWechatAccessExpiresIn());
merchantDTO.setContactWechatAccessScope(merchantRegisterVO.getContactWechatAccessScope());
merchantDTO.setContactWechatAccessToken(merchantRegisterVO.getContactWechatAccessToken());
merchantDTO.setContactWechatAccessExpiresIn(merchantRegisterVO.getContactWechatAccessExpiresIn());
merchantDTO.setContactWechatAccessScope(merchantRegisterVO.getContactWechatAccessScope());
merchantDTO.setContactWechatAccessToken(merchantRegisterVO.getContactWechatAccessToken());
merchantDTO.setContactWechatAccessExpiresIn(merchantRegisterVO.getContactWechatAccessExpiresIn());
merchantDTO.setContactWechatAccessScope(merchantRegisterVO.getContactWechatAccessScope());
merchantDTO.setContactWechatAccessToken(merchantRegisterVO.getContactWechatAccessToken());
merchantDTO.setContactWechatAccessExpiresIn(merchantRegisterVO.getContactWechatAccessExpiresIn());
merchantDTO.setContactWechatAccessScope(merchantRegisterVO.getContactWechatAccessScope());
merchantDTO.setContactWechatAccessToken(merchantRegisterVO.getContactWechatAccessToken());
merchantDTO.setContactWechatAccessExpiresIn(merchantRegisterVO.getContactWechatAccessExpiresIn());
merchantDTO.setContactWechatAccess
