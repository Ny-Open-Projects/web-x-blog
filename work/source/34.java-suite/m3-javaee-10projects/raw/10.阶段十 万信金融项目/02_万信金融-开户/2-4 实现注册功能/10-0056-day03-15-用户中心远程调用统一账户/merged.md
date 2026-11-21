# day03-15-用户中心远程调用统一账户

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day03-15-用户中心远程调用统一账户_【海量资源尽在 666java.com】.mp4
- 时长 17分47秒（音频 1067s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 咱还是要看一下这张图我们开发到现在呢得稍微停一停对吧打开这个图我们再整体再看一看我们目前都实现了什么功能啊你看我们目前是不是统一账户这边实现了保存注册信息的功能没错吧然后呢用户中心这边是不是也实现了保存注册信息的功能那是不是就实现完了呀我感觉对不对全部搞定了前端又不用咱管这流程打通了吗
[00:33] 这个流程还不通呢还缺什么呀还缺这儿缺这儿呢13缺这儿我们前面说过用户中心服务是比较远程调用什么呀囤移账户服务然后整个这个流程才算打通了就是将来前端发一个请求先到用户中心用户中心保存完数据之后发请求到哪儿囤移账户囤移账户保存完信息之后财算完成然后就返回注册成功这个结果所以目前呢我们还差这么一步就是在用户中心这个微服务里边
[01:02] 去发起远程请求调用统一账户这边因为统一账户呢它跟前端可是没关系的啊前端这个请求不到这儿了所以说我们现在缺一个远程调用这个远程调用是不是两个微幅之间的远程调用啊那我们该怎么实现呢用咱以前学过的东西通过什么呀对通过FINFINFFINFIN我们前面在学E9A看的时候
[01:32] 提过飞通过它可以非常快速的方便的实现这个远程请求或者远程访问那么接下来呢咱就需要在哪个地方用户中心就是consumer这边通过飞发起一个远程请求到统一账户这边那咱这块咱首先要做的事是不是要把飞的环境大概的先提供一下嘛那个代理最主要的那个代理嘛大家回顾一下吧我们是如何通过飞发起远程调用的呀
[02:05] 是不是咱一开始是讲过ribbon是吧后来讲的fame那这块你要是没印象的话你要复习复习前面的东西这样呢我们就直接给大家进行编码了啊这一块其实最主要的是不是我们就是consumer这边consumer这边我们最主要的是不是要写一个接口然后呢由sprint帮我们根据这个接口产生一个什么呀代理啊或者说代理对象然后将来由这个代理对象是不是帮我们发起了一个什么呀
[02:35] 愿成一个请求一个调用这些事其实说白不用咱们管咱只需要定一个代理接口好咱嗯回到这个consumer里边呃咱再建一个包吧啊这个包已经建过了啊而进的agnt就是代理的意思如果你的工程里边没这个包的话你就建一个啊将来我们所有的这个代理相同东西都放在这里边那我们在这个包上点右键新建一个接口
[03:07] 我们起个名字叫叫叫叫啥名我们是要调用谁那边看到那边对吧那就是ACC OUNT吧API然后AGENT可以吧这样子起名的话好处就是你看到这个这个类名是不是你不知道他是调用谁那边的什么服务的对不对我们这是接口不是类NPFAC改一下
[03:38] 那这个接口里边都需要写什么东西大家还有印象吗非印相关的东西啊那这个接口首先咱上面是不是要先写一个注页叫什么呀FinklandFinkland对这个注记也有什么用啊大家还有印象吗我们有了有瑞卡之后所有的微服务是不是都是注册到有瑞卡里边而且注册的时候是不是每个微服都有一个名字吗那个副名
[04:10] 那我们现在是不是要调用哪个服务啊是不是啊可看到那微服务那这个注解的作用就是用来设置你要调用或者访问哪个微服务的你在这把这个微服的名字告诉他就行了那我们啊看他那个微服的名字呢应该就是啊可看他干Service这你自己查一下那我在这呢就直接写了就是ACCOUACCOUNT干什么SERVSE
[04:42] 对你得先告诉他我要访问哪个什么呀微服务嘛我们要加这个注解加注解之后还没完呢我们account微服务里边这个方法是不是有很多呀那我到底调哪个control或者哪个control里边具体哪个方法呢是不是那这个东西呢我们也得告诉他要不然他将来是成代理的时候他就不知道该访问谁了或者请求谁了那这块东西的话其实我们直接可以从account那边找到control或者找到那个那个接口直接粘过来就行了
[05:13] 我们找到快那边不是恐怕应该API里边可靠他里边咱找到这个哪个呀我们是要调谁呀是调这个保存就这个注册注射我就不再考这我就不再考我只要下面这个方法就行这C然后呢我们粘到这里
[05:53] 这就完了吗这没完啊这没完我们得告诉他你具体调呢是哪个方法怎么告诉他呢或者请求路径对不对你要告诉他请问这个请求路径啊你就需要去啊可看他那边找到具体的什么呀Controller我们找一找这个Controller啊看到那边啊看在哪最上面因为你是往这边发请求吗请求最终是不是落到哪个地方
[06:25] 所以说你应该找到就是他我要的就是这个东西可能c好伸过来但是呢这个路应该改这个路径你这么写就不行了因为你这是远程调用是从consumer这边远程调用这个account了你直接这么写他可不知道这个路径这是哪个微服务当中的路径对不对所以你应该把account Service那边那个基本的那个路径给他加上那个基本的路径肯定是叫account
[06:57] 这个当然你可以自己查一下配置啊ACCOUNT你得把这一层或者这一级也给它干什么呀加上这个路径才是对的啊所以这个你一定要注意了那么这是咱把啥给补上来哎这还没完这还没完还缺一个东西呢这得加什么东西啊咱以前讲飞音的时候是不是这点特别强调我有印象吗如果我们在用飞音发起远程调用的时候
[07:29] 你调用的这个Controller这个方法如果有参数这一定要加什么东西对你要把request body这个注解给他补上要不然会出问题的request body对没错就这个一定要加上这个细节千万不要忘了那这样子的话咱这个代理就写好那至于他具体怎么工作咱以前讲过我这呢再给大家说一说那将来呢Spring框架呢会根据咱这个什么呀接口帮我们生成代理类甚至还有什么呀代理对象
[07:58] 当然在代理类当中呢他会自动重写这个方法那重写这个方法的时候他实现的功能无非就是去9A卡里边是不是找到这个什么呀可抗他这个微幅然后呢朝这干什么呀对发请求就行了也就是说具体其实远程调用远程发请求这个功能咱用不用管不用管咱只需要写这个接口就行那这个接口写完之后我在哪去用它呢是不是我总得有个代码去体现我
[08:29] 我干什么呀我比如我调用这个方法了还是怎么着了对不对或者说体现我调用那个代理代理对象的这个方法对不对那也说发起远程调用这个代码应该在哪写应该在哪写那你看这个图啊这个地方大家看这我应该是在用户中心这个服务这边咱保存完数据之后是不是应该发请求到这边是不是而用户中心这边保存数据这个代码是不是咱刚写过了是不是我们关一些东西啊打开东西有点多
[09:03] 这些我们看看对吧这些都给他关掉了我们只留下 Service大家看这这是咱刚才写的代码这块代码是不是咱用户中心这边刚保存完数据保存完数据之后接下来在这就应该干嘛在 save 的下面就应该干嘛是不是就应该发起远程调用到什么地方对到 account 这边所以咱接下来需要找到 Service 代码在下面再补一下补什么代码
[09:35] 对就是远程调用的这个代码我们在这再加一个什么呀注释吧再加一个注释将来大家看这个代码会更清晰一些那这个注释的话那就是什么呀远程调用ACC OUNT那这个代码具体怎么写大家还有印象吗具体怎么写那直接怎么着对你应该把那个接口给注一下
[10:12] 其实你住来的不是接口住进来是不是他框架产生的那个代理类或者代理对象对不对at auto auto world然后呢private他叫什么名account account api agent对吧住进来是那个代理对象然后呢我们怎么远程调用呢那就是调用他的那个方法register方法就发起了这个什么呀远程调用
[10:45] 其实这个代码还是比较简单的那咱就写一下这个代码吧那就是怎么写刚才不是注入进来一个对象ACC OUNT然后它有一个方法叫什么呀REGEST然后呢这个方法是不是有一个参数对吧它要一个什么东西对它要啥你得看这个接口它要的是一个什么呀ACC REGEST DTO诶想一想
[11:16] 我们现在手头上有的DTO是什么DTO是Consumer Register DTO发现问题了吧那怎么办没有别的办法你只能是把它里边的属性值取出来然后给谁啊给一个Account Register DTO这个代码我们前面说过嘛在P2P里边很常见那咱自己先溜一个空的Account什么呀对Register DTO直接溜
[11:48] 没人提供给你吧你就只能自己用了呗自己动手丰衣足食是吧那这里边属性的值怎么从哪来啊那肯定是从哪来consumer register detail里边来那怎么办呢如发袍制呀我们还是用用谁呀用他还是用这号呗这样control ccontrol v那这里边这个值你得换一换了对不对那这里边第一个参议应该写谁呀对应该就是这个
[12:21] 就是他consumer register DTO那第二个值应该写谁啊第二值是不是就应该写这个DTO写他那这行代码的意思是什么对这行代码做的就是把这个DTO对象里边所有属性的值是不是复制给他就OK了那咱这个account register DTO这个对象咱是不是就有了有了之后呢咱接下来是不是就可以发起远程调用然后把它传过去了
[12:53] 那这样呢我就可以写什么呀ACC OUNTregister什么呀底条对那另外呢这个register方案是不是有反而值啊有没有反而值有啊那你还要看这个接口吗因为这个接口是不是咱当时呃是你可以说是照着奥康到那边写其实我是不是直接就复制过来对不对你看它是不是返回有这么一个东西啊那我们得接收一下就反而是得接收一下
[13:28] 那就是rest response接受一下然后接收完之后呢那这里边也有可能成功也有可能什么呀失败所以说我们这里边来判断一下万一远程调用失败了呢对不对是来我们干什么呀跑一场对我们这设计的就是只要失败了我们就干什么呀跑一场那我怎么判断它有没有成功会有没有失败这个代码咱以前也写过是不是判断这个rest response对象里边是不是有个code吗对不对
[13:58] 他可以表示什么呀成功或者说什么呀对失败所以咱接下来啊把这个代码给补一下if这里边呢我们就要判断restrestresponse第二什么呀对get a codeget a code啊然后呢我们是如果他不等于谁啊这个代码我就直接写了啊不等于苦慢咱以前也有那个封装好的那个那个类
[14:33] 供我们大家去使用的啊有一个叫苦漫 error code苦漫common对我们air code 点他有个点点出来谁呀我们是不等于吗不等于success吧s对success就是其实说白就是零啊你要不想那么费劲你这直接写个零就行了然后再点给他什么呀扣的其实这个给的扣的话反而就是什么呀零啊就是呃那
[15:09] 这么写他表达的意思就是什么呀这个春天了失败了那我这就干什么呀手动的抛一个一场那就是怎么写啊那就死肉牛呗还是牛咱那个b字那一次是什么呀一颗人工抛这个一场那就是死肉牛然后一个就是bu si对吧那具体这个一场的内容是啥呢我们从consumer里边来去
[15:42] consumer error codeconsumer error code里边应该有现成的一个值啊好的找一找consumer error code点一下我们看看应该是取哪个呀那就哪个注册失败吧好吧140106这个注册失败我们就抛弃一场就行这是咱们把什么呀远程叼这个代码在Service里边给它补充上补充完之后呢接下来就剩最后一步了
[16:19] 你要发起远程电话还有一个非常关键的一步看有没有同学知道想一想以前我们在用飞应的时候还差哪一步非常关键对就是启动内上我们再检查检查启动内上我们还有一个注解要加启动内上我给咱加了没有这已经加过了就这样这行注解是干嘛的这行注解是干嘛的你看他是不是写的是这个all进的这个包的这个路径对不对干嘛的
[16:49] 对这是让框架去扫描到这个接口扫描到这个接口框架好帮我们干什么呀去自动生成代理类及代理对象啊所以说你的启动内上你一定要检查一下我这儿有不代表你的就有所以这个地方一定要检查一下没有的话自己加上就行那这是目前吧咱们把什么呀在consumer里边啊发起远程调就是通过飞啊发起远程调到哪儿对到可看它这边这个代码呢我们全部补上
[17:20] 那么这个补上之后大家注意了咱们整个注册整个这一套这个代码就全部干什么呀实现完毕了就这三个小功能全部实现完毕那咱后边要做的事就是要进行什么测试了而且我们还要前后端集成到一起进行什么测试

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Spring Cloud Feign 实现消费者服务对账户服务的远程调用，并完成用户注册功能。

2) 按时间顺序列出每张画面的要点：
画面1: 展示消费者服务的 Controller 层代码，定义了测试接口和用户注册接口，其中用户注册接口使用了 @PostMapping 注解和 @Validated 注解。
画面2: 展示了消费者服务的 Maven 依赖配置，包括 Spring Cloud Starter、Druid、MySQL Connector、Feign Client 等依赖。
画面3: 展示了消费者服务中定义的 Feign 客户端接口 AccountApiAgent，用于调用账户服务。
画面4: 展示了账户服务的 AccountAPI 接口定义，包含校验手机号和验证码、注册保存信息等方法。
画面5: 展示了 AccountApiAgent 接口的完整代码，使用 @FeignClient 注解指定服务名 "account-Service"。
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
@FeignClient(value = "account-Service")
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
@FeignClient(value = "account-Service")
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

