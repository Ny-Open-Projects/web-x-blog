# day06-7-开户第一阶段-功能实现3

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-16 实现开户功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-16 实现开户功能\day06-7-开户第一阶段-功能实现3_【海量资源尽在 666java.com】.mp4
- 时长 7分58秒（音频 479s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们针对银行卡操作呢把它的业务层面实现了其实银行卡相用的这块东西呢都是一会儿在开户的过程当中要去使用的那咱接下来呢就去实现开户第一阶段的功能就是生成这个什么呀生成开户数据那我们现在就要回到回到哪对回到我们用户中心了回到这边找谁呢找这个consumer Service找consumer的Service
[00:29] 这个才是咱们的什么主业务层刚才银行卡业务层其实将来是要在这被调用被使用的consumer Service才是咱的主业务层那咱回到consumer Service我们是不是要也是要干什么现在接口里边定义方法然后在实现类当中实现第一阶段生成开入数据的功能那这个Service对应的接口和类前面是不是都已经存在了咱前面是不是实现过什么
[01:00] 注册登录当时这些啊这个接口和这个实验类都已经存在了咱无非是往里边增加方法就行因为这不是咱以前开发的注册吗这呢再增加这个哪个方法增加这个CREATE CONSUMER这是咱前面说过了我们直接给它粘过来稍微改一下啊那关于这个方法的参照反正之后我就不再过多解释了咱在需要分析的时候前面都已经跟大家说过
[01:37] 这是右层的接口我们定好定好之后呢我们就需要在实现类当中去实现这个方法来具体啊这就是具体实现我们开户第一阶段的这个功能我们把这个方法生成一下在哪在这那这个代码写起来会有些复杂大家看看讲义是不是复杂了啊看到代码挺多的倒是功能上也不是很复杂啊就是代码的确有点多
[02:08] 呃那这个地方大家需要注意我们在实现这个方法的时候呢这上面要注意加上这个事物的这个注解啊因为这里边咱本地呢数据库的操作进行了好几个我们要搞一个本地事物这个不要忘了一下那接下来这个功能具体怎么实现呢对吧这里边这这这么多代码我们前面说过再复杂咱也不用担心化整为零一步一步来对吧这个慢慢慢慢这个代码我们就能给他写出来
[02:40] 所以说咱既然是这样咱先把这个步骤或者说咱先分析分析这里边我们都需要实现啥功能都是什么样的这个什么样步骤咱先把这个分析好那我们这是不是在做开户而且我们现在做的这个事情是不是开户的第一阶段对不对就最早发生的事情那你想我们这个P2P呢在开户的时候是你首先要是不是要做一些判断要做一些判断吗做什么判断那你比如说这个人万一已经开过户了
[03:11] 他还来凑账呢对吧我就想试试看你这个你这个功能有问题没有对吧我都开个户了万一你你还可以让我开户那你那你这个功能做的不行对不对总我们第一步要判断的就是判断什么呀判断当前用户是否已经什么呀对开户我要判断一下你要是已经开过户了你就别来凑账了是不是那接下来呢现在还有什么需要判断吗
[03:40] 还有我要判断什么呀判断提交过来的什么呀银行卡是否已被什么呀绑定这个不好说啊这是什么意思呢你看大家应该有这方面的经验你在某些网站上注册用户名的时候他会提示你这个用户名已经被使用了让你改了对不对那咱这也是一样那我们要判断我们要做交易你的银行卡是不是
[04:16] 曾经被使用过在我们的这个平台上对不对被绑定过被使用过那就不行了我们这是新开户啊我们这是新开户你这个银行卡必须是在我们P2P平台从来没有出现过没有被使用过所以我们要我们要做这个银行卡是否绑定的一个判断那这些都判断过了我们接下来具体要上要还要做什么事呢那你要看这个时序图了呀看这个地方这个地方我们都要做什么事
[04:46] 你看这个实际图里边目前显示的是不是要准备一些数据然后还要最终发到什么呀从外代理服务那边对不对那其实除了做这些事之外呢我们还有一些本地的本地数据库的表里边的一些数据我们要进行什么更新呀或者说什么呀保存呢对不对要做这么一些事情这些东西可能这个实际图里边没有给大家怎么展示那我们在实现的时候要说一下
[05:16] 那我们要做哪些事情呢哪些这个数据库操作呢我们要首先要要更新什么呀更新用户的信息就consumer那这个有啥好更新呢需要更新啥呢咱看这个表哪个表用户表呢就是哪个表用户表应该就是consumer对不对咱找找consumer这里边有啥需要更新的呀这个表里边数据按说是我们以前应该有是不是咱注册的时候应该就有吧是不是
[05:46] 这些手机号你还有印象吗那这边还有啥需要更新的呢咱进来瞅一瞅都有哪些需要更新那这里边你比如说我们这次开货的时候他就应该会提供什么手机身份证号注册的时候是不是只有一个手机号嘛那开货的时候他其实前端会传过来身份证号我身份证号是不是就往这里边补充了吗还有什么还有一些什么东西对还有他的真实性命是不是这次要提供真实性命等等相关的一些信息里边有些我们就需要干什么
[06:17] 包括这些存款授权那边这些有的我们都要进行补充了所以说呢在这个时候呢我们就要做一件事就是更新啊用户的信息那还要做什么事呢除了更新用户信息之外呢我们还要做的事就是一个保存保存保存银行卡信息银行卡信息因为前段传过来的这里边其实还有银行卡的一些信息比如银行卡号等等那这个信息呢是要往哪保存呢往这个地方
[06:48] 大家注意看这你看我们考虑这个数据库里边是不是还有个银行卡这个表这个咱以前从来没用过对不对你看这里边只有银行什么银行卡号对不对这些信息啊也是前端就可以传过来我们在这需要进行什么呀保存的我这我们还要做一个事就是保保存银行卡信息这什么都是属于数据库操作对吧然后这些操作操作完呢对操作完之后呢我们要做的事就是
[07:21] 那基本上就是最后一步了准备数据怎么说呢发起远程调用把数据发到哪边了发到存管代理服务对没错啊这就是我们怎么说呢开户第一阶段最终我们要实现的功能以及共我们是拆分成了几个步骤对五个步骤那咱一会就
[07:53] 一步一步的把这些代码呢给它实现了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
- 展示IDEA项目结构，当前选中“wanningzp-consumer-Service”工程。
- 项目结构中可见“Service”包下的“ConsumerService”接口文件。

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
- 服务模块包括：adminService、ApolloPortal、configService、wanningzp-consumer-Service、wanningzp-depository-agent-Service。
- 服务间关系：adminService指向ApolloPortal，configService指向wanningzp-consumer-Service。

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

