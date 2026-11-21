# 画面线理解：day06-8-开户第一阶段-功能实现4

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-16 实现开户功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-16 实现开户功能\day06-8-开户第一阶段-功能实现4_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 01:33, 02:31, 04:04, 04:40, 06:06, 07:32, 10:30, 11:24, 12:09, 14:03, 15:37, 16:21, 17:05
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:17:57

1) 这一组画面整体在讲什么（一句话）：
演示如何在用户注册服务中，通过调用银行服务查询用户银行卡信息，并根据查询结果更新用户信息和银行卡信息，最终通过代理服务完成注册。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示ConsumerServiceImpl.java文件中createConsumer方法的代码，注释说明“判断当前用户是否已经开户”，并调用getByIdCard方法。
画面2：展示ConsumerRequest.java文件，定义了请求参数，包括手机号、角色、请求流水号、用户编号、是否有回调URL等。
画面3：在createConsumer方法中，调用getByIdCard方法获取银行卡信息，弹出提示框说明“Inserts 'if null' statement”。
画面4：展示ConsumerService接口的实现类ConsumerServiceImpl，其中包含checkMobile方法和confirmRegister方法。
画面5：在createConsumer方法中，调用bankCardService.getByCardNumber方法获取银行卡信息。
画面6：在createConsumer方法中，判断银行卡对象是否为空或状态是否为STATUS_IN，如果是则抛出BusinessException。
画面7：展示数据库表consumer的结构，包含ID、USERNAME、USER_NO、USER_TYPE、BANK_CARD、LOGIN_ACCOUNT、REQUEST_NO等字段。
画面8：在createConsumer方法中，设置用户信息，包括用户名、请求流水号、用户编号等，并使用UpdateWrapper更新数据库。
画面9：展示PPT内容，说明如何保存银行卡信息，包括设置卡号、手机号、状态等，并调用bankCardService.saveOrUpdate方法。
画面10：展示系统架构图，包括SQLyog、Apollo、adminservice、configservice等服务。
画面11：在createConsumer方法中，创建BankCard对象，设置用户ID、卡号、手机号、状态等，并调用bankCardService.saveOrUpdate方法。
画面12：展示PPT内容，说明如何完善ConsumerController的代码，包括设置用户名、调用ConsumerService.createConsumer方法。
画面13：在createConsumer方法中，调用depositoryAgentApiAgent.createConsumer方法。
画面14：在createConsumer方法中，如果银行卡对象为空，则抛出BusinessException。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Override
@Transactional
public RestResponse<GatewayRequest> createConsumer(ConsumerRequest consumerRequest) {
    //1.判断当前用户是否已经开户
    ConsumerDTO consumerDTO = getBankCardService().getByIdCard(consumerRequest.getMobile());
    if (consumerDTO != null) {
        //2.判断传过来的银行卡是否已被绑定
        BankCardDTO bankCardDTO = bankCardService.getByCardNumber(consumerRequest.getCardNumber());
        if (bankCardDTO != null && bankCardDTO.getStatus() == StatusCode.STATUS_IN) {
            throw new BusinessException(ConsumerErrorCode.E_14015);
        }
    }
    //3.更新用户的信息
    consumerRequest.setId(consumerDTO.getId());
    //产生请求流水号
    consumerRequest.setRequestNo(CodeUtil.getNoCodePrefixCode(CodePrefixCode.CODE_CONSUMER_PREFIX));
    consumerRequest.setUserNo(CodeUtil.getNoCodePrefixCode(CodePrefixCode.CODE_REQUEST_PREFIX));
    //设置查询条件和需要更新的数据
    UpdateWrapper<Consumer> updateWrapper = new UpdateWrapper<>();
    updateWrapper.lambda().eq(Consumer::getUsername, consumerRequest.getUsername());
    updateWrapper.lambda().eq(Consumer::getRequestNo, consumerRequest.getRequestNo());
    updateWrapper.lambda().eq(Consumer::getUserNo, consumerRequest.getUserNo());
    updateWrapper.lambda().eq(Consumer::getFullName, consumerRequest.getFullName());
    updateWrapper.lambda().eq(Consumer::getAuthList, "ALL");
    updateWrapper.lambda().set(Consumer::getAuthList, "ALL");
    //4.保存银行卡信息
    BankCard bankCard = new BankCard();
    bankCard.setConsumerId(consumerDTO.getId());
    bankCard.setCardNumber(consumerRequest.getCardNumber());
    bankCard.setMobile(consumerRequest.getMobile());
    bankCard.setStatus(StatusCode.STATUS_OUT.getCode());
    BankCardDTO existBankCard = bankCardService.getByConsumerId(bankCard.getConsumerId());
    if (existBankCard != null) {
        bankCard.setId(existBankCard.getId());
    }
    bankCardService.saveOrUpdate(bankCard);
    return depositoryAgentApiAgent.createConsumer(consumerRequest);
}
```

画面2：
```java
private String cardNumber;
@ApiModelProperty("手机号")
private String mobile;
@ApiModelProperty("角色")
private String role;
@ApiModelProperty("请求流水号")
private String requestNo;
@ApiModelProperty("用户编号")
private String userNo;
@ApiModelProperty("是否有回调URL")
private String callbackUrl
```

画面3：
```java
ConsumerDTO consumerDTO = getBankCardService().getByIdCard(consumerRequest.getMobile());
if (consumerDTO != null) {
    //2.判断传过来的银行卡是否已被绑定
    BankCardDTO bankCardDTO = bankCardService.getByCardNumber(consumerRequest.getCardNumber());
    if (bankCardDTO != null && bankCardDTO.getStatus() == StatusCode.STATUS_IN) {
        throw new BusinessException(ConsumerErrorCode.E_14015);
    }
}
```

画面4：
```java
@Service
public class ConsumerServiceImpl extends ServiceImpl<ConsumerMapper, Consumer> implements ConsumerService {
    @Autowired
    private AccountApiAgent accountApiAgent;

    @Override
    public Integer checkMobile(String mobile) {
        return getMobile(mobile) != null ? 1 : 0;
    }

    private ConsumerDTO getMobile(String mobile) {
        Consumer consumer = new QueryWrapper<Consumer>().lambda().eq(Consumer::getMobile, mobile).one();
        return convertConsumerEntityDTO(consumer);
    }

    @Override
    @Transactional
    public void confirmRegister(ConsumerRegisterDTO consumerRegisterDTO) {
        if (checkMobile(consumerRegisterDTO.getMobile()) == 0) {
            throw new BusinessException(ConsumerErrorCode.E_14017);
        }
    }
}
```

画面5：
```java
BankCardDTO bankCardDTO = bankCardService.getByCardNumber(consumerRequest.getCardNumber());
```

画面6：
```java
if (bankCardDTO != null && bankCardDTO.getStatus() == StatusCode.STATUS_IN) {
    throw new BusinessException(ConsumerErrorCode.E_14015);
}
```

画面7：
```sql
CREATE TABLE `consumer` (
  `ID` bigint(20) NOT NULL COMMENT '主键',
  `USERNAME` varchar(50) NOT NULL COMMENT '用户名',
  `USER_NO` varchar(50) NOT NULL COMMENT '真实姓名',
  `USER_TYPE` varchar(50) NOT NULL COMMENT '用户类型，个人用户，企业用户',
  `BANK_CARD` tinyint(1) NOT NULL COMMENT '是否已绑定银行卡',
  `LOGIN_ACCOUNT` varchar(50) NOT NULL COMMENT '登录账号',
  `REQUEST_NO` varchar(50) NOT NULL COMMENT '请求流水号',
  `STATUS` tinyint(1) NOT NULL COMMENT '状态',
  `CREATE_TIME` datetime NOT NULL COMMENT '创建时间',
  `UPDATE_TIME` datetime NOT NULL COMMENT '更新时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

画面8：
```java
consumerRequest.setId(consumerDTO.getId());
//产生请求流水号
consumerRequest.setRequestNo(CodeUtil.getNoCodePrefixCode(CodePrefixCode.CODE_CONSUMER_PREFIX));
consumerRequest.setUserNo(CodeUtil.getNoCodePrefixCode(CodePrefixCode.CODE_REQUEST_PREFIX));
//设置查询条件和需要更新的数据
UpdateWrapper<Consumer> updateWrapper = new UpdateWrapper<>();
updateWrapper.lambda().eq(Consumer::getUsername, consumerRequest.getUsername());
updateWrapper.lambda().eq(Consumer::getRequestNo, consumerRequest.getRequestNo());
updateWrapper.lambda().eq(Consumer::getUserNo, consumerRequest.getUserNo());
updateWrapper.lambda().eq(Consumer::getFullName, consumerRequest.getFullName());
updateWrapper.lambda().eq(Consumer::getAuthList, "ALL");
updateWrapper.lambda().set(Consumer::getAuthList, "ALL");
```

画面9：
```java
//保存银行卡信息
BankCard bankCard = new BankCard();
bankCard.setConsumerId(consumerDTO.getId());
bankCard.setCardNumber(consumerRequest.getCardNumber());
bankCard.setMobile(consumerRequest.getMobile());
bankCard.setStatus(StatusCode.STATUS_OUT.getCode());
BankCardDTO existBankCard = bankCardService.getByConsumerId(bankCard.getConsumerId());
if (existBankCard != null) {
    bankCard.setId(existBankCard.getId());
}
bankCardService.saveOrUpdate(bankCard);
return depositoryAgentApiAgent.createConsumer(consumerRequest);
```

画面10：
无代码或配置内容。

画面11：
```java
BankCard bankCard = new BankCard();
bankCard.setConsumerId(consumerDTO.getId());
bankCard.setCardNumber(consumerRequest.getCardNumber());
bankCard.setMobile(consumerRequest.getMobile());
bankCard.setStatus(StatusCode.STATUS_OUT.getCode());
BankCardDTO existBankCard = bankCardService.getByConsumerId(bankCard.getConsumerId());
if (existBankCard != null) {
    bankCard.setId(existBankCard.getId());
}
bankCardService.saveOrUpdate(bankCard);
```

画面12：
```java
@PostMapping("/my/consumers")
public RestResponse<GatewayRequest> createConsumer(@RequestBody ConsumerRequest consumerRequest) {
    consumerRequest.setUsername(SecurityUtil.getUser().getUsername());
    return consumerService.create
