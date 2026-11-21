# 画面线理解：day06-7-开户第一阶段-功能实现3

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-16 实现开户功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-16 实现开户功能\day06-7-开户第一阶段-功能实现3_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:18, 00:27, 00:57, 01:08, 01:11, 01:26, 01:40, 01:58, 02:03, 02:20, 02:28, 05:13, 05:47, 07:02
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:16:59

1) 这一组画面整体在讲什么（一句话）：
在“万方企业级”项目中，演示如何在用户中心服务中新增“生成开户数据”的接口定义与实现，包括在接口层和实现层添加方法、处理用户注册逻辑、银行卡绑定校验及数据库操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示课程PPT页面“3.3 第一阶段: 生成开户数据”，其中3.3.1节要求参考“开户业务流程图”和“个人银行卡开户接口说明”。
- 3.3.2节“接口定义”下，3.3.2.1小节“用户中心生成开户数据接口”要求在“warxinp2p-api”工程的ConsumerAPI接口中新增createConsumer方法。
- 代码片段：`RestResponse<GatewayRequest> createConsumer(ConsumerRequest consumerRequest);`

画面2：
- PPT页面继续展示“3.3.2.1 用户中心生成开户数据接口”。
- 代码片段：`RestResponse<GatewayRequest> createConsumer(ConsumerRequest consumerRequest);`

画面3：
- 展示IDEA项目结构，当前选中“wanningzp-consumer-service”工程。
- 项目结构中可见“service”包下的“ConsumerService”接口文件。

画面4：
- 展示“ConsumerService.java”接口文件内容。
- 代码片段：
```java
public interface ConsumerService extends IService<Consumer> {
    // 检测用户是否存在
    @Param mobile
    @Return
    Integer checkMobile(String mobile);

    // 用户注册
    @Param consumerRegisterDTO
    @Return
    void register(ConsumerRegisterDTO consumerRegisterDTO);
}
```

画面5：
- PPT页面展示“在ConsumerService接口中新增createConsumer方法”和“在ConsumerServiceImpl类中实现该方法”。
- 代码片段：
```java
@override
@Transactional
public RestResponse<GatewayRequest> createConsumer(ConsumerRequest consumerRequest) {
    ConsumerDTO consumerDTO = getUserName(consumerRequest.getUsername(), true);
    if (consumerDTO.getIsBindCard() == 1) {
        throw new BusinessException(ConsumerErrorCode.E_140105);
    }
    // 判断银行卡是否已绑定
    BankCardDTO bankCardDTO = bankCardService
            .getByConsumerId(consumerDTO.getConsumerId());
    if (existBankCard != null) {
        bankCardDTO.setBindCard(consumerRequest.getBindCard());
    }
    bankCardService.saveOrUpdate(bankCard);
    return depositoryAgentApiAgent.createConsumer(consumerRequest);
}
```

画面6：
- 展示“ConsumerService.java”接口文件，光标位于新增的`createConsumer`方法定义处。

画面7：
- 展示“ConsumerServiceImpl.java”文件内容。
- 代码片段：
```java
@Override
@Transactional
public RestResponse<GatewayRequest> createConsumer(ConsumerRequest consumerRequest) {
    Consumer consumer = new Consumer();
    BeanUtils.copyProperties(consumerRegisterDTO, consumer);
    consumer.setUsername(CodecUtil.getOCodePrefix().CODE_NO_PREFIX);
    consumerRegisterDTO.setUsername(consumer.getUsername());
    consumer.setMobile(CodecUtil.getOCodePrefix().CODE_REQUEST_PREX);
    consumer.setBindCard(consumerRegisterDTO.getBindCard());
    consumer.save(consumer);
    // 调用账户服务
    AccountRegisterDTO accountRegisterDTO = new AccountRegisterDTO();
    BeanUtils.copyProperties(consumerRegisterDTO, accountRegisterDTO);
    RestResponse<GatewayRequest> restResponse = accountApiAgent.register(accountRegisterDTO);
    if (restResponse.getErrorCode() != CommonErrorCode.SUCCESS.getCode()) {
        throw new BusinessException(ConsumerErrorCode.E_140106);
    }
    return restResponse;
}
```

画面8：
- PPT页面展示“在ConsumerService接口中新增createConsumer方法”和“在ConsumerServiceImpl类中实现该方法”。
- 代码片段：
```java
@override
@Transactional
public RestResponse<GatewayRequest> createConsumer(ConsumerRequest consumerRequest) {
    ConsumerDTO consumerDTO = getUserName(consumerRequest.getUsername(), true);
    if (consumerDTO.getIsBindCard() == 1) {
        throw new BusinessException(ConsumerErrorCode.E_140105);
    }
    // 判断银行卡是否已绑定
    BankCardDTO bankCardDTO = bankCardService
            .getByConsumerId(consumerDTO.getConsumerId());
    if (existBankCard != null) {
        bankCardDTO.setBindCard(consumerRequest.getBindCard());
    }
    bankCardService.saveOrUpdate(bankCard);
    return depositoryAgentApiAgent.createConsumer(consumerRequest);
}
```

画面9：
- PPT页面展示“保存用户银行卡信息”的代码逻辑。
- 代码片段：
```java
BankCard bankCard = new BankCard();
bankCard.setConsumerId(consumerDTO.getConsumerId());
bankCard.setBankCode(consumerRequest.getBankCode());
bankCard.setCardNumber(consumerRequest.getCardNumber());
bankCard.setMobile(consumerRequest.getMobile());
bankCard.setStatus(StatusCode.STATUS_OUT.getCode());
BankCardDTO existBankCard = bankCardService.getByConsumerId(bankCard.getConsumerId());
if (existBankCard != null) {
    bankCard.setBindCard(existBankCard.getBindCard());
}
bankCardService.saveOrUpdate(bankCard);
return depositoryAgentApiAgent.createConsumer(consumerRequest);
```

画面10：
- 展示“ConsumerServiceImpl.java”文件内容。
- 代码片段：
```java
if (restResponse.getErrorCode() != CommonErrorCode.SUCCESS.getCode()) {
    throw new BusinessException(ConsumerErrorCode.E_140106);
}
@Override
public RestResponse<GatewayRequest> createConsumer(ConsumerRequest consumerRequest) {
    // 判断当前用户是否已经开户
    // 重新用户的信息
    // ...
}
public void confirmRegister(ConsumerRegisterDTO consumerRegisterDTO) {
    log.info("execute confirmRegister");
    remote(Wrappers.<Consumer>lambdaQuery().eq(Consumer::getMobile, consumerRegisterDTO.getMobile()));
}
public void cancelRegister(ConsumerRegisterDTO consumerRegisterDTO) {
    log.info("execute cancelRegister");
    remote(Wrappers.<Consumer>lambdaQuery().eq(Consumer::getMobile, consumerRegisterDTO.getMobile()));
}
```

画面11：
- 展示系统架构图，包含多个服务模块。
- 服务模块包括：adminService、ApolloPortal、configService、wanningzp-consumer-service、wanningzp-depository-agent-service。
- 服务间关系：adminService指向ApolloPortal，configService指向wanningzp-consumer-service。

画面12：
- 展示“ConsumerServiceImpl.java”文件内容。
- 代码片段：
```java
if (restResponse.getErrorCode() != CommonErrorCode.SUCCESS.getCode()) {
    throw new BusinessException(ConsumerErrorCode.E_140106);
}
@Override
public RestResponse<GatewayRequest> createConsumer(ConsumerRequest consumerRequest) {
    // 判断当前用户是否已经开户
    // 重新用户的信息
    // ...
}
public void confirmRegister(ConsumerRegisterDTO consumerRegisterDTO) {
    log.info("execute confirmRegister");
    remote(Wrappers.<Consumer>lambdaQuery().eq(Consumer::getMobile, consumerRegisterDTO.getMobile()));
}
public void cancelRegister(ConsumerRegisterDTO consumerRegisterDTO) {
    log.info("execute cancelRegister");
    remote(Wrappers.<Consumer>lambdaQuery().eq(Consumer::getMobile, consumerRegisterDTO.getMobile()));
}
```

画面13：
- 展示数据库表“consumer”的结构。
- 表结构：
```sql
CREATE TABLE `consumer` (
  `ID` bigint(20) NOT NULL,
  `USERNAME` varchar(50) NOT NULL,
  `FULLNAME` varchar(50) NOT NULL,
  `MOBILE` varchar(50) NOT NULL,
  `USER_TYPE` varchar(50) NOT NULL,
  `HTML_LIST` varchar(50) NOT NULL,
  `IS_BIND_CARD` tinyint(1) NOT NULL,
  `LOGIN_ACCOUNT` decimal(10,0) NOT NULL,
  `STATUS` tinyint(1) NOT NULL,
  `REQUEST_NO` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

画面14：
- 展示“ConsumerServiceImpl.java”文件内容。
- 代码片段：
```java
if (restResponse.getErrorCode() != CommonErrorCode.SUCCESS.getCode()) {
    throw new BusinessException(ConsumerErrorCode.E_140106);
}
@Override
public RestResponse<GatewayRequest> createConsumer(ConsumerRequest consumerRequest) {
    // 判断当前用户是否已经开户
    // 重新用户的信息
    // ...
}
public void confirmRegister(ConsumerRegisterDTO consumerRegisterDTO) {
    log.info("execute confirmRegister");
    remote(Wrappers.<Consumer>lambdaQuery().eq(Consumer::getMobile, consumerRegisterDTO.getMobile()));
}
public void cancelRegister(ConsumerRegisterDTO consumerRegisterDTO) {
    log.info("execute cancelRegister");
    remote(Wrappers.<Consumer>lambdaQuery().eq(Consumer::getMobile, consumerRegisterDTO.getMobile()));
}
```
