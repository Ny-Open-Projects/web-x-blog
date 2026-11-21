# 画面线理解：day05-4-注册功能存在的事务问题

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-10 理解事务和分布式事务
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-10 理解事务和分布式事务\day05-4-注册功能存在的事务问题_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:05, 04:50, 05:17, 06:05, 06:29, 06:45, 07:01, 07:28, 08:01, 08:24, 08:46, 09:22, 09:49, 11:22
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:59:24

1) 这一组画面整体在讲一个用户注册流程的系统架构与代码实现，包括时序图、服务启动、代码调试和数据库操作。

2) 按时间顺序列出每张画面的要点：
画面1：展示用户注册流程的时序图，包含前端、用户中心服务、短信服务、账户服务和鉴权服务等组件及其交互步骤。
画面2：与画面1相同，为时序图的重复展示。
画面3：在SQLyog中打开p2p_account数据库，显示表结构，当前选中表为p2p_account。
画面4：在IntelliJ IDEA中，显示wanningzp-apollo项目结构，控制台输出GatewayServer和NamingService启动日志。
画面5：在IntelliJ IDEA中，控制台输出NamingService初始化完成日志。
画面6：在IntelliJ IDEA中，选中wanningzp-consumer-service模块，准备进行调试。
画面7：在IntelliJ IDEA中，显示ConsumerServiceImpl.java代码，包含checkMobile和getMobile方法。
画面8：在IntelliJ IDEA中，调试器断点位于AccountRegisterDTO构造方法处，准备执行注册逻辑。
画面9：在浏览器中打开登录页面，网络面板显示请求15376791900成功返回。
画面10：在浏览器中，登录页面显示“请输入手机号”和“请输入验证码”输入框，网络面板显示请求548173和548173。
画面11：在IntelliJ IDEA中，调试器断点位于AccountRegisterDTO构造方法处，准备执行注册逻辑。
画面12：在SQLyog中打开p2p_consumer数据库，当前选中表为空。
画面13：在SQLyog中打开p2p_account数据库，当前选中表为空。
画面14：在SQLyog中打开p2p_consumer数据库，显示用户表数据，包含ID、USERNAME、MOBILE、USER_TYPE、ROLE等字段。

3) 画面中出现的代码、配置、命令、目录结构、SQL、XML/YAML配置：
画面7代码：
```java
package cn.itcast.wanningzp.consumer.service;

import ...

@Service
public class ConsumerServiceImpl extends ServiceImpl<ConsumerMapper, Consumer> implements ConsumerService {

    @Autowired
    private AccountApiAgent accountApiAgent;

    @Override
    public Integer checkMobile(String mobile) { return getMobile(mobile); }

    private ConsumerECO getMobile(String mobile) {
        Consumer consumer = getOne(new QueryWrapper<Consumer>().lambda().eq(Consumer::getMobile, mobile));
        return consumer;
    }
}
```

画面8代码：
```java
consumer.setUserId(CodeUtil111.getFb(CodePrefixCode.CODE_REQUEST_PREFIX));
consumer.setBindCard(0);
save(consumer);

// 注册应用 account
AccountRegisterDTO accountRegisterDTO = new AccountRegisterDTO();
BeanUtils.copyProperties(consumer, accountRegisterDTO, accountApiAgent.register(accountRegisterDTO);
RestResponse<AccountDTO> restResponse = accountApiAgent.register(accountRegisterDTO);
if (restResponse.getCode() != CommonErrorCode.SUCCESS.getCode()) {
    throw new BusinessException(ConsumerErrorCode.E_140106);
}
```

画面14 SQL：
```sql
ID USERNAME MOBILE USER_TYPE ROLE
100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
