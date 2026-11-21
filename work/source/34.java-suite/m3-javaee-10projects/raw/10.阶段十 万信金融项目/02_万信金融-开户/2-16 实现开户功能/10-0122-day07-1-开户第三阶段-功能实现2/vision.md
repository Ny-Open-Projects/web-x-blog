# 画面线理解：day07-1-开户第三阶段-功能实现2

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-16 实现开户功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-16 实现开户功能\day07-1-开户第三阶段-功能实现2_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:39, 02:54, 05:06, 05:54, 07:14, 07:28, 07:59, 09:08, 10:05, 11:10, 12:23, 12:57, 13:47
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:27:40

1) 这一组画面整体在讲什么（一句话）：
演示一个存款通知服务的代码实现，包括控制器接收请求、服务层修改状态、更新用户信息及银行卡信息等核心逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 `DepositoryNotifyController` 中的 `@RequestMapping` 和 `@RequestParam` 注解，用于接收请求参数并映射到方法。
画面2：聚焦于 `return "OK";` 语句，表示请求处理成功。
画面3：展示 PPT 内容，讲解 `DepositoryRecordService` 接口中的 `modifyRequestStatus` 方法及其实现。
画面4：展示数据库表 `depository_record` 的数据，包含请求ID、类型、项目ID、创建日期等字段。
画面5：展示 `DepositoryRecordServiceImpl` 中的 `modifyRequestStatus` 方法，包含 `update` 方法调用。
画面6：展示 `DepositoryRecordServiceImpl` 中的 `saveDepositoryRecord` 方法，用于创建新的存款记录。
画面7：展示 `ConsumerServiceImpl` 中的 `update` 方法，用于更新用户信息。
画面8：展示 `ConsumerServiceImpl` 中的 `update` 方法，设置用户手机号、姓名、证件号等。
画面9：再次展示 PPT 内容，讲解 `DepositoryRecordService` 接口中的 `modifyRequestStatus` 方法及其实现。
画面10：展示 `ConsumerServiceImpl` 中的 `update` 方法，设置用户证件号。
画面11：展示 `DepositoryRecordServiceImpl` 中的 `modifyRequestStatus` 方法，包含 `update` 方法调用。
画面12：再次展示数据库表 `depository_record` 的数据。
画面13：展示 `DepositoryNotifyController` 中的 `return "OK";` 语句。
画面14：再次展示 `DepositoryNotifyController` 中的 `return "OK";` 语句。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@ApiOperation(value = "需求的存管接口名",
        notes = "平台编号，平台与存管系统签约时获取。",
        required = true, dataType = "String", paramType = "query"),
@ApiOperation(value = "对reqData参数的签名",
        required = true, dataType = "String", paramType = "query"),
@ApiOperation(value = "业务数据报文，json格式",
        required = true, dataType = "String", paramType = "query"),
)
@RequestMapping(value = "/gateway", method = RequestMethod.GET, params = "serviceName=PERSONAL_REGISTER")
public String receivedepositoryCreateConsumerResult(@RequestParam("serviceName") String serviceName,
        @RequestParam("platformNo") String platformNo,
        @RequestParam("signature") String signature,
        @RequestParam("reqData") String reqData) {
    //1.更易读
    //2.发送消息给用户中心
    //3.返回结果
    return "OK";
}
```

画面3：
```java
2. 在DepositoryRecordService接口中新增modifyRequestStatus方法：
/**
 * 根据请求流水号更新请求状态
 * @param requestNo
 * @param requestStatus
 * @return
 */
Boolean modifyRequestStatus(String requestNo, Integer requestStatus);

在DepositoryRecordServiceImpl类中实现modifyRequestStatus方法：
@Override
public Boolean modifyRequestStatus(String requestNo, Integer requestStatus) {
    return update(Wrappers.<DepositoryRecord>lambdaUpdate()
            .eq(DepositoryRecord::getRequestNo, requestNo)
            .set(DepositoryRecord::getRequestStatus, requestStatus)
            .set(DepositoryRecord::getConfirmDate, LocalDateTime.now()));
}

3. 新建message包，在该包中定义消息生产者：
```

画面5：
```java
package cn.icta.warning2p.depository.service;
import cn.icta.warning2p.depository.entity.DepositoryRecord;
import cn.icta.warning2p.depository.mapper.DepositoryRecordMapper;
import cn.icta.warning2p.depository.service.DepositoryRecordService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import java.util.List;
@Service
@Transactional
public class DepositoryRecordServiceImpl implements DepositoryRecordService {
    @Autowired
    private ConfigService configService;
    @Autowired
    private DepositoryRecordMapper depositoryRecordMapper;
    @Override
    public GatewayRequest receivedepositoryCreateConsumerRequest(CommonRequest consumerRequest) {
        //1.修改请求状态
        String reqData = consumerRequest.getReqData();
        String sign = consumerRequest.getSignature();
        String platformNo = consumerRequest.getPlatformNo();
        String serviceNo = consumerRequest.getServiceNo();
        GatewayRequest gatewayRequest = new GatewayRequest();
        gatewayRequest.setReqData(reqData);
        gatewayRequest.setSignature(sign);
        gatewayRequest.setPlatformNo(platformNo);
        gatewayRequest.setServiceNo(serviceNo);
        gatewayRequest.setDepositUrl(configService.getDepositUrl() + "/gateway");
        return gatewayRequest;
    }
}
```

画面6：
```java
@Override
public Boolean modifyRequestStatus(String requestNo, Integer requestStatus) {
    update(Wrappers.<DepositoryRecord>lambdaUpdate()
            .eq(DepositoryRecord::getRequestNo, requestNo)
            .set(DepositoryRecord::getRequestStatus, requestStatus)
            .set(DepositoryRecord::getConfirmDate, LocalDateTime.now()));
}

private void saveDepositoryRecord(CommonRequest consumerRequest) {
    DepositoryRecord depositoryRecord = new DepositoryRecord();
    depositoryRecord.setRequestNo(consumerRequest.getRequestNo());
    depositoryRecord.setRequestType(DepositoryRecordTypeCode.CONSUMER_CREATE.getCode());
    depositoryRecord.setObjectType(DepositoryRecordObjectTypeCode.CONSUMER.getCode());
    depositoryRecord.setObjectId(consumerRequest.getConsumerId());
    depositoryRecord.setCreateDatetime(LocalDateTime.now());
    depositoryRecord.setRequestStatus(DepositoryRecordStatusCode.STATUS_OUT.getCode());
    depositoryRecord.setConfirmDate(LocalDateTime.now());
    depositoryRecord.setConfirmDatetime(LocalDateTime.now());
    depositoryRecord.setConfirmUser(consumerRequest.getConfirmUser());
    depositoryRecord.setConfirmIp(consumerRequest.getConfirmIp());
    depositoryRecord.setConfirmTime(consumerRequest.getConfirmTime());
    depositoryRecord.setConfirmStatus(DepositoryRecordConfirmStatusCode.CONFIRMED.getCode());
    depositoryRecord.setConfirmRemark(consumerRequest.getConfirmRemark());
    depositoryRecord.setConfirmType(DepositoryRecordConfirmTypeCode.CONFIRM_TYPE.getCode());
    depositoryRecord.setConfirmCode(consumerRequest.getConfirmCode());
    depositoryRecord.setConfirmData(consumerRequest.getConfirmData());
    depositoryRecord.setConfirmStatus(DepositoryRecordConfirmStatusCode.CONFIRMED.getCode());
    depositoryRecord.setConfirmType(DepositoryRecordConfirmTypeCode.CONFIRM_TYPE.getCode());
    depositoryRecord.setConfirmCode(consumerRequest.getConfirmCode());
    depositoryRecord.setConfirmData(consumerRequest.getConfirmData());
    depositoryRecord.setConfirmStatus(DepositoryRecordConfirmStatusCode.CONFIRMED.getCode());
    depositoryRecord.setConfirmType(DepositoryRecordConfirmTypeCode.CONFIRM_TYPE.getCode());
    depositoryRecord.setConfirmCode(consumerRequest.getConfirmCode());
    depositoryRecord.setConfirmData(consumerRequest.getConfirmData());
    depositoryRecord.setConfirmStatus(DepositoryRecordConfirmStatusCode.CONFIRMED.getCode());
    depositoryRecord.setConfirmType(DepositoryRecordConfirmTypeCode.CONFIRM_TYPE.getCode());
    depositoryRecord.setConfirmCode(consumerRequest.getConfirmCode());
    depositoryRecord.setConfirmData(consumerRequest.getConfirmData());
    depositoryRecord.setConfirmStatus(DepositoryRecordConfirmStatusCode.CONFIRMED.getCode());
    depositoryRecord.setConfirmType(DepositoryRecordConfirmTypeCode.CONFIRM_TYPE.getCode());
    depositoryRecord.setConfirmCode(consumerRequest.getConfirmCode());
    depositoryRecord.setConfirmData(consumerRequest.getConfirmData());
    depositoryRecord.setConfirmStatus(DepositoryRecordConfirmStatusCode.CONFIRMED.getCode());
    depositoryRecord.setConfirmType(DepositoryRecordConfirmTypeCode.CONFIRM_TYPE.getCode());
    depositoryRecord.setConfirmCode(consumerRequest.getConfirmCode());
    depositoryRecord.setConfirmData(consumerRequest.getConfirmData());
    depositoryRecord.setConfirmStatus(DepositoryRecordConfirmStatusCode.CONFIRMED.getCode());
    depositoryRecord.setConfirmType(DepositoryRecordConfirmTypeCode.CONFIRM_TYPE.getCode());
    depositoryRecord.setConfirmCode(consumerRequest.getConfirmCode());
    depositoryRecord.setConfirmData(consumerRequest.getConfirmData());
    depositoryRecord.setConfirmStatus(DepositoryRecordConfirmStatusCode.CONFIRMED.getCode());
    depositoryRecord.setConfirmType(DepositoryRecordConfirmTypeCode.CONFIRM_TYPE.getCode());
    depositoryRecord.setConfirmCode(consumerRequest.getConfirmCode());
    depositoryRecord.setConfirmData(consumerRequest.getConfirmData());
    depositoryRecord.setConfirmStatus(DepositoryRecordConfirmStatusCode.CONFIRMED.getCode());
    depositoryRecord.setConfirmType(DepositoryRecordConfirmTypeCode.CONFIRM_TYPE.getCode());
    depositoryRecord.setConfirmCode(consumerRequest.getConfirmCode());
    depositoryRecord.setConfirmData(consumerRequest.getConfirmData());
    depositoryRecord.setConfirmStatus(DepositoryRecordConfirmStatusCode
