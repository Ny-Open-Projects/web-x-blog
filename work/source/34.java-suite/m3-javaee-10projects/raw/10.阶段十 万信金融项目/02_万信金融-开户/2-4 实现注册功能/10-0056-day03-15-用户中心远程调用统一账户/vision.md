# 画面线理解：day03-15-用户中心远程调用统一账户

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day03-15-用户中心远程调用统一账户_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:51, 03:05, 05:25, 05:47, 06:17, 08:56, 10:15, 10:33, 11:20, 12:08, 13:27, 15:39, 16:02, 17:21
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:38:04

1) 这一组画面整体在讲如何使用 Spring Cloud Feign 实现消费者服务对账户服务的远程调用，并完成用户注册功能。

2) 按时间顺序列出每张画面的要点：
画面1: 展示消费者服务的 Controller 层代码，定义了测试接口和用户注册接口，其中用户注册接口使用了 @PostMapping 注解和 @Validated 注解。
画面2: 展示了消费者服务的 Maven 依赖配置，包括 Spring Cloud Starter、Druid、MySQL Connector、Feign Client 等依赖。
画面3: 展示了消费者服务中定义的 Feign 客户端接口 AccountApiAgent，用于调用账户服务。
画面4: 展示了账户服务的 AccountAPI 接口定义，包含校验手机号和验证码、注册保存信息等方法。
画面5: 展示了 AccountApiAgent 接口的完整代码，使用 @FeignClient 注解指定服务名 "account-service"。
画面6: 展示了 AccountApiAgent 接口中定义的注册方法，使用 @PostMapping 注解和 @RequestBody 注解。
画面7: 展示了消费者服务的 ConsumerServiceImpl 类，其中包含 checkMobile 方法用于校验手机号。
画面8: 展示了 ConsumerServiceImpl 类中 checkMobile 方法的完整实现，包含查询数据库和返回结果。
画面9: 展示了 ConsumerServiceImpl 类中 register 方法的实现，包含校验手机号、创建 Consumer 实体、设置属性和调用 AccountApiAgent.register 方法。
画面10: 展示了 register 方法中创建 AccountRegisterDTO 对象并调用 accountApiAgent.register 方法。
画面11: 展示了 register 方法中设置 Consumer 实体属性，包括用户名、手机号、密码、银行卡号等。
画面12: 展示了 register 方法中抛出 BusinessException 异常，使用 ConsumerErrorCode 枚举类。
画面13: 展示了 ConsumerErrorCode 枚举类，包含多个错误码和对应的错误信息。
画面14: 展示了用户注册流程图，包含前端、用户中心服务、认证服务、统一账户、验证服务等模块的交互流程。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面1:
```java
@GetMapping(path = "/hi")
@ApiOperation("测试")
public String hi(String name) {
    return "hi," + name;
}

@PostMapping(value = "/consumers")
@ApiOperation("用户注册")
@Validated
public RestResponse register(@RequestBody ConsumerRegisterDTO consumerRegisterDTO) {
    consumerService.register(consumerRegisterDTO);
    return RestResponse.success();
}
```

画面2:
```xml
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>druid-spring-boot-starter</artifactId>
    <version>1.1.10</version>
</dependency>
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>8.0.28</version>
</dependency>
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-openfeign</artifactId>
</dependency>
<dependency>
    <groupId>com.netflix.feign</groupId>
    <artifactId>feign-http</artifactId>
</dependency>
```

画面3:
```java
@FeignClient(value = "account-service")
public interface AccountApiAgent {
}
```

画面4:
```java
// 校验手机号和验证码
@Param("mobile") String mobile;
@Param("key") String key;
@Param("code") String code;

// 注册 保存信息
@Param("accountRegisterDTO") AccountRegisterDTO accountRegisterDTO;
```

画面5:
```java
@FeignClient(value = "account-service")
public interface AccountApiAgent {
}
```

画面6:
```java
@PostMapping(value = "/account/1/accounts")
RestResponse<AccountDTO> register(@RequestBody AccountRegisterDTO accountRegisterDTO);
```

画面7:
```java
@Service
public class ConsumerServiceImpl extends ServiceImpl<ConsumerMapper, Consumer> implements ConsumerService {

    @Override
    public Integer checkMobile(String mobile) {
        return getMobile(mobile) != null ? 1 : 0;
    }

    private ConsumerDTO getConsumerDTO(String mobile) {
        Consumer consumer = new QueryWrapper<Consumer>().lambda().eq(Consumer::getMobile, mobile).last("LIMIT 1").one();
        return convertConsumerEntityToDTO(consumer);
    }
}
```

画面8:
```java
@Override
public Integer checkMobile(String mobile) {
    return getMobile(mobile) != null ? 1 : 0;
}

private ConsumerDTO getConsumerDTO(String mobile) {
    Consumer consumer = new QueryWrapper<Consumer>().lambda().eq(Consumer::getMobile, mobile).last("LIMIT 1").one();
    return convertConsumerEntityToDTO(consumer);
}
```

画面9:
```java
@Override
public void register(ConsumerRegisterDTO consumerRegisterDTO) {
    if (checkMobile(consumerRegisterDTO.getMobile()) == 0) {
        throw new BusinessException(ConsumerErrorCode.E_140107);
    }
    Consumer consumer = new Consumer();
    BeanUtils.copyProperties(consumerRegisterDTO, consumer);
    consumer.setUserName(CodeUtil.getNoCodePrefixCode(CodePrefixCode.CODE_NO_PREFIX));
    consumer.setMobile(CodeUtil.getNoCodePrefixCode(CodePrefixCode.CODE_REQUEST_PREFIX));
    consumer.setIsBindCard(0);
    consumer.setIsBindCard(0);
    // 选择调用 account
    accountApiAgent.register();
}
```

画面10:
```java
@Override
public void register(ConsumerRegisterDTO consumerRegisterDTO) {
    if (checkMobile(consumerRegisterDTO.getMobile()) == 0) {
        throw new BusinessException(ConsumerErrorCode.E_140107);
    }
    Consumer consumer = new Consumer();
    BeanUtils.copyProperties(consumerRegisterDTO, consumer);
    consumer.setUserName(CodeUtil.getNoCodePrefixCode(CodePrefixCode.CODE_NO_PREFIX));
    consumer.setMobile(CodeUtil.getNoCodePrefixCode(CodePrefixCode.CODE_REQUEST_PREFIX));
    consumer.setIsBindCard(0);
    consumer.setIsBindCard(0);
    // 选择调用 account
    AccountRegisterDTO accountRegisterDTO = new AccountRegisterDTO();
    BeanUtils.copyProperties(consumerRegisterDTO, accountRegisterDTO);
    accountApiAgent.register(accountRegisterDTO);
}
```

画面11:
```java
@Override
public void register(ConsumerRegisterDTO consumerRegisterDTO) {
    if (checkMobile(consumerRegisterDTO.getMobile()) == 0) {
        throw new BusinessException(ConsumerErrorCode.E_140107);
    }
    Consumer consumer = new Consumer();
    BeanUtils.copyProperties(consumerRegisterDTO, consumer);
    consumer.setUserName(CodeUtil.getNoCodePrefixCode(CodePrefixCode.CODE_NO_PREFIX));
    consumer.setMobile(CodeUtil.getNoCodePrefixCode(CodePrefixCode.CODE_REQUEST_PREFIX));
    consumer.setIsBindCard(0);
    consumer.setIsBindCard(0);
    // 选择调用 account
    AccountRegisterDTO accountRegisterDTO = new AccountRegisterDTO();
    BeanUtils.copyProperties(consumerRegisterDTO, accountRegisterDTO);
    accountApiAgent.register(accountRegisterDTO);
}
```

画面12:
```java
throw new BusinessException(ConsumerErrorCode.E_140107);
```

画面13:
```java
public enum ConsumerErrorCode {
    E_140107("用户手机号已存在"),
    E_140108("用户手机号格式错误"),
    E_140109("用户密码格式错误"),
    E_140110("用户邮箱格式错误"),
    E_140111("用户昵称格式错误"),
    E_140112("用户头像格式错误"),
    E_140113("用户性别格式错误"),
    E_140114("用户生日格式错误"),
    E_140115("用户地址格式错误"),
    E_140116("用户电话格式错误"),
    E_140117("用户邮箱已存在"),
    E_140118("用户昵称已存在"),
    E_140119("用户头像已存在"),
    E_140120("用户性别已存在"),
    E_140121("用户生日已存在"),
    E_140122("用户地址已存在"),
    E_140123("用户电话已存在"),
    E_140124("用户邮箱已存在"),
    E_140125("用户昵称已存在"),
    E_140126("用户头像已存在"),
    E_140127("用户性别已存在"),
    E_140128("用户生日已存在"),
    E_140129("用户地址已存在"),
    E_140130("用户电话已存在"),
    E_140131("用户邮箱已存在"),
    E_140132("用户昵称已存在"),
    E_140133("用户头像已存在"),
    E_140134("用户性别已存在"),
    E_140135("用户生日已存在"),
    E_14
