# 画面线理解：day09-11-幂等性-测试准备

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-11 幂等性问题分析及实现
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-11 幂等性问题分析及实现\day09-11-幂等性-测试准备_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:36, 01:50, 03:20, 05:47, 07:38, 08:57, 10:27, 11:58, 13:36, 16:10, 17:12, 18:05, 19:22, 20:30
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:09:00

1) 这一组画面整体在讲P2P平台中标的存管流程，包括前端发起、交易中心审批、存管代理服务处理、标的存管服务同步及银行存管系统交互等环节。

2) 按时间顺序列出每张画面的要点：
画面1：展示P2P平台标的存管流程的时序图，包含“浏览器/APP”、“交易中心”、“存管代理服务”、“标的存管服务”、“银行存管系统”五个参与者，以及从1.1到2.14的流程步骤。
画面2：展示`DepositoryRecordServiceImpl.java`中处理标的存管请求的代码，包含创建`DepositoryRecord`对象、转换`ProjectDTO`、生成JSON字符串、加密等逻辑。
画面3：展示`ProjectServiceImpl.java`中`projectApprovalStatus`方法，通过`depositoryAgentApiAgent.createProject`调用存管代理服务，根据返回结果更新项目状态。
画面4：展示`DepositoryRecordServiceImpl.java`中`handleDepositent`方法，根据请求No查询记录，若不存在则保存，若存在则根据状态码判断是否重复点击。
画面5：展示数据库设计文档，包含“1.2.1.2 标的存管”、“2. 在Project类中新增对应的属性”、“3. 在ProjectDTO类中新增对应的属性”等章节。
画面6：展示`ProjectDTO.java`中定义的属性，包括`remainingAmount`、`risk`、`tenderCount`等。
画面7：展示`ProjectServiceImpl.java`中`projectApprovalStatus`方法，通过IDE的代码提示功能选择`getConsumerId`方法。
画面8：重复画面1的内容，展示P2P平台标的存管流程的时序图。
画面9：展示数据库设计文档，包含“另外，针对幂等性问题中的第3种情况，我们也要做一些修改”、“1. 在depository_record表中新增一个字段RESPONSE_DATA”等说明。
画面10：展示数据库管理工具中`p2p_depository_agent`数据库的表结构，显示`depository_record`表的字段信息。
画面11：展示`DepositoryRecord.java`中新增的`@TableField("RESPONSE_DATA") private String responseData;`属性。
画面12：展示`DepositoryRecordServiceImpl.java`中`handleDepositent`方法的`else`分支，处理失败情况，设置状态码、确认时间、更新数据库并抛出异常。
画面13：展示`DepositoryRecordServiceImpl.java`中`handleDepositent`方法的`else`分支，处理失败情况，设置状态码、确认时间、更新数据库并抛出异常。
画面14：展示数据库设计文档，包含“4. 在DepositoryRecordServiceImpl类的sendHttpGet方法中新增一行代码”等说明。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面2：
```java
DepositoryResponseDTO DepositoryBaseResponse responseDTO = handleDepotent(depositoryRecord);
if (responseDTO != null) {
    return responseDTO;
}
depositoryRecord = getInitByRequestNo(projectDTO.getRequestNo());
```
画面3：
```java
projectDTO.setRequestNoCodePrefix(projectDTO.getCodePrefix() + projectDTO.getRequestNo());
```
画面4：
```java
if (null == depositoryRecordDTO) {
    saveDepositoryRecord(depositoryRecord);
    return null;
}
if (StatusCode.STATUS_OUT.getCode() ==
    depositoryRecordDTO.getRequestStatus()) {
```
画面5：
```sql
ALTER TABLE `p2p_transaction`.`project_0`
    ADD COLUMN `REQUEST_NO` varchar(50) NULL COMMENT '发标请求流水号' AFTER `IS_ASSIGNMENT`;
ALTER TABLE `p2p_transaction`.`project_1`
    ADD COLUMN `REQUEST_NO` varchar(50) NULL COMMENT '发标请求流水号' AFTER `IS_ASSIGNMENT`;
```
画面6：
```java
private BigDecimal remainingAmount;
private String risk = "B";
private Integer tenderCount;
```
画面7：
```java
if (project.getConsumerId() != null) {
```
画面9：
```sql
ALTER TABLE `p2p_depository_agent`.`depository_record`
    ADD COLUMN `RESPONSE_DATA` text NULL COMMENT '处理结果' AFTER `CONFIRM_DATE`;
```
画面10：
```sql
Field Type Comment
ID bigint(20) NOT 主键
REQUEST_NO varchar(50) NULL 请求流水号
REQUEST_TYPE varchar(50) NULL 业务类型
DEPOSIT_ID bigint(20) 关联业务实体标识
```
画面11：
```java
@TableField("RESPONSE_DATA")
private String responseData;
```
画面12：
```java
depositoryRecord.setRequestStatus(StatusCode.STATUS_FAIL.getCode());
depositoryRecord.setConfirmDate(LocalDateTime.now());
updateById(depositoryRecord);
throw new BusinessException(DeponentErrorCode.E_16010);
```
画面13：
```java
depositoryRecord.setRequestStatus(StatusCode.STATUS_FAIL.getCode());
depositoryRecord.setConfirmDate(LocalDateTime.now());
updateById(depositoryRecord);
throw new BusinessException(DeponentErrorCode.E_16010);
```
画面14：
```sql
ALTER TABLE `p2p_depository_agent`.`depository_record`
    ADD COLUMN `RESPONSE_DATA` text NULL COMMENT '处理结果' AFTER `CONFIRM_DATE`;
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1：时序图，参与者包括“浏览器/APP”、“交易中心”、“存管代理服务”、“标的存管服务”、“银行存管系统”，流程步骤从1.1到2.14。
画面5：文档标题“万向金融P2P平台-标的存管”、“1.2.1.2 标的存管”、“2. 在Project类中新增对应的属性”、“3. 在ProjectDTO类中新增对应的属性”。
画面9：文档标题“万向金融P2P平台-标的存管”、“另外，针对幂等性问题中的第3种情况，我们也要做一些修改”、“1. 在depository_record表中新增一个字段RESPONSE_DATA”。
画面14：文档标题“万向金融P2P平台-标的存管”、“4. 在DepositoryRecordServiceImpl类的sendHttpGet方法中新增一行代码”。

5) 无。
