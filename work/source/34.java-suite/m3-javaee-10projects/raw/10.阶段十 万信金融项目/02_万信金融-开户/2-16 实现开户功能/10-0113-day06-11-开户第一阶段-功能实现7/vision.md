# 画面线理解：day06-11-开户第一阶段-功能实现7

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-16 实现开户功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-16 实现开户功能\day06-11-开户第一阶段-功能实现7_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:10, 01:15, 01:41, 02:23, 04:34, 06:40, 07:03, 08:03, 08:41, 09:56, 10:49, 11:45, 12:31, 13:55
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:20:24

1) 这一组画面整体在讲什么（一句话）：
演示如何在开户业务中，通过定义并实现 RepositoryRecordService 接口及其方法，完成交易记录的持久化和状态更新。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 mapper 包中新建 DepositoryRecordMapper 接口，定义其继承自 BaseMapper<DepositoryRecord>；同时在同包中新建 DepositoryRecordMapper.xml 文件，配置其 namespace 为 cn.itcast.wanxing2p.depository.mapper.DepositoryRecordMapper。
画面 2: 展示了多个窗口，包括 PPT、WPS 图片、日志文件等，同时在 IDE 中显示了 DepositoryRecordServiceImpl 类的开头部分，定义了 createConsumer 方法。
画面 3: 展示了开户业务流程图，图中包含“前端/App”、“用户中心”、“容器代理服务”、“存管系统”和“开卡银行”五个模块，以及它们之间的交互流程。
画面 4: 在 IDE 中显示了 DepositoryRecordServiceImpl 类的完整结构，其中 extends ServiceImpl<DepositoryRecordMapper, DepositoryRecord>。
画面 5: 在 IDE 中显示了 DepositoryRecord 类的定义，包含私有字段 requestStatus、confirmDate 和 responseData，以及构造函数。
画面 6: 在 IDE 中显示了 createConsumer 方法的实现，调用 saveDepositoryRecord 方法。
画面 7: 在 IDE 中显示了 saveDepositoryRecord 方法的实现，创建 DepositoryRecord 对象并设置 requestNo 和 requestType。
画面 8: 在 IDE 中显示了 DepositoryRequestTypeCode 类的定义，包含多个常量如 TRADING、PULL_LOAN、MODIFY_STATUS 等。
画面 9: 在 IDE 中显示了 saveDepositoryRecord 方法中，设置 requestType 为 CONSUMER_CREATE。
画面 10: 在 IDE 中显示了 saveDepositoryRecord 方法中，设置 objectType 为 "Consumer"。
画面 11: 在 IDE 中显示了 ConsumerServiceImpl 类中，对银行卡状态进行校验，并设置 consumerRequest 的相关属性。
画面 12: 在 IDE 中显示了 saveDepositoryRecord 方法中，设置 objectTo 为 "Consumer"。
画面 13: 在 IDE 中显示了 saveDepositoryRecord 方法中，设置 requestStatus 为 STATUS_OUT。
画面 14: 在 IDE 中显示了 saveDepositoryRecord 方法中，调用 save 方法保存记录。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
/**
 * 存管交易记录表 Mapper 接口
 */
public interface DepositoryRecordMapper extends BaseMapper<DepositoryRecord> {

}
```
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
    "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="cn.itcast.wanxing2p.depository.mapper.DepositoryRecordMapper">
</mapper>
```
画面 4:
```java
package cn.itcast.wanxing2p.depository.service;

import cn.itcast.wanxing2p.depository.entity.DepositoryRecord;
import cn.itcast.wanxing2p.depository.mapper.DepositoryRecordMapper;
import org.springframework.stereotype.Service;

@Service
public class DepositoryRecordServiceImpl extends ServiceImpl<DepositoryRecordMapper, DepositoryRecord> {

}
```
画面 5:
```java
private Integer requestStatus;
// 消息确认时间
@TableField("CONFIRM_DATE")
private LocalDateTime confirmDate;
// 返回数据
@TableField("RESPONSE_DATA")
private String responseData;

public DepositoryRecord() {

}

public DepositoryRecord(String requestNo, String requestType, String objectType, Long objectId) {
    this.requestNo = requestNo;
    this.requestType = requestType;
    this.objectType = objectType;
    this.objectId = objectId;
}
```
画面 6:
```java
@Override
public GatewayRequest createConsumer(ConsumerRequest consumerRequest) {
    //1.保存交易记录
    saveDepositoryRecord(consumerRequest);
    //2.签名（加密）数据并返回
}
```
画面 7:
```java
private DepositoryRecord saveDepositoryRecord(ConsumerRequest consumerRequest) {
    DepositoryRecord depositoryRecord = new DepositoryRecord();
    depositoryRecord.setRequestNo(consumerRequest.getRequestNo());
    depositoryRecord.setRequestType(consumerRequest.getRequestType());
}
```
画面 8:
```java
/**
 * 用户投标
 */
TRADING("TRADING", "用户投标"),
/**
 * 审核标满放款
 */
PULL_LOAN("FULL_LOAN", "审核标满放款"),
/**
 * 修改标的的状态
 */
MODIFY_STATUS("MODIFY_STATUS", "修改标的的状态"),
CONSUMER_CREATE("CONSUMER_CREATE", "开户"),
RECHARGE("RECHARGE", "充值"),
WITHDRAW("WITHDRAW", "提现");

private String code;
private String desc;
```
画面 9:
```java
depositoryRecord.setRequestType(DepositoryRequestTypeCode.CONSUMER_CREATE);
```
画面 10:
```java
depositoryRecord.setObjectType("Consumer");
```
画面 11:
```java
//3.更新用户的信息
consumerRequest.setUserName(bankCardDTO.getCardNo());
consumerRequest.setUserId(bankCardDTO.getCardNo());
consumerRequest.setRequestNo(CodeGenUtil.getCode(ConsumerRequest.CODE_REQUEST_PREFIX));
consumerRequest.setUserName(bankCardDTO.getCardNo());
consumerRequest.setUserId(bankCardDTO.getCardNo());
consumerRequest.setRequestNo(CodeGenUtil.getCode(ConsumerRequest.CODE_REQUEST_PREFIX));
//更新用户信息
UpdateWrapper<Consumer> updateWrapper = new UpdateWrapper<>();
updateWrapper.lambda().set(Consumer::updateUserName, consumerRequest.getUserName());
updateWrapper.lambda().set(Consumer::updateUserId, consumerRequest.getUserId());
updateWrapper.lambda().set(Consumer::updateRequestNo, consumerRequest.getRequestNo());
updateWrapper.lambda().set(Consumer::updateCardNo, consumerRequest.getCardNo());
updateWrapper.lambda().set(Consumer::updateStatus, consumerRequest.getStatus());
updateWrapper.lambda().set(Consumer::updateCreateTime, consumerRequest.getCreateTime());
updateWrapper.lambda().set(Consumer::updateUpdateTime, consumerRequest.getUpdateTime());
updateWrapper.lambda().set(Consumer::updateRemark, consumerRequest.getRemark());
updateWrapper.lambda().set(Consumer::updateVersion, consumerRequest.getVersion());
updateWrapper.lambda().set(Consumer::updateStatus, consumerRequest.getStatus());
updateWrapper.lambda().set(Consumer::updateUpdateTime, consumerRequest.getUpdateTime());
updateWrapper.lambda().set(Consumer::updateRemark, consumerRequest.getRemark());
updateWrapper.lambda().set(Consumer::updateVersion, consumerRequest.getVersion());
```
画面 12:
```java
depositoryRecord.setObjectTo("Consumer");
```
画面 13:
```java
depositoryRecord.setRequestStatus(StatusCode.STATUS_OUT);
```
画面 14:
```java
depositoryRecord.setCreateTime(LocalDateTime.now());
save(depositoryRecord);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 3: PPT 标题为“开户业务流程图”，流程图包含五个模块：“前端/App”、“用户中心”、“容器代理服务”、“存管系统”和“开卡银行”，它们之间的交互流程如下：
- “前端/App”指向“用户中心”，执行“1.1生成开户请求数据”。
- “用户中心”指向“容器代理服务”，执行“1.2准备开户所需基础数据”。
- “容器代理服务”指向“存管系统”，执行“1.4通过短信生成交易及数据”。
- “存管系统”指向“开卡银行”，执行“2.4验证请求”。
- “开卡银行”指向“存管系统”，执行“2.7保存交易记录”。
- “存管系统”指向“用户中心”，执行“2.6返回开户信息”。
- “用户中心”指向“前端/App”，执行“1.7返回开户请求数据”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
