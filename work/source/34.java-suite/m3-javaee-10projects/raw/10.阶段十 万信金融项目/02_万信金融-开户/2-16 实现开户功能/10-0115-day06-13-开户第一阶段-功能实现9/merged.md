# day06-13-开户第一阶段-功能实现9

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-16 实现开户功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-16 实现开户功能\day06-13-开户第一阶段-功能实现9_【海量资源尽在 666java.com】.mp4
- 时长 3分44秒（音频 225s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们把要藏代码里边写了一下这里边就俩功能一个是保存这个交易记录一个是签名数据然后把数据返回是吧那最后呢我们还是要回到Controller里面把Controller那个代码就完善一下就搞完了啊Controller我们找一下Controller当时在定义接口的时候Controller这边是一个空时线吧是吧我们把这完善一下就行了这怎么完善呢首先是不是注入Service吧这个大家都清车熟路了at all to work
[00:32] private然后就是depositoryservice的depositoryrecord Service比较长然后呢我们就是调用他的方法就是开户的那个方法叫create consumer然后把它传进去传进去之后呢他要的是不是这个rest response这个方式那跟以前的做法一样直接点什么呀success吧
[01:02] 他的这个反应他反而是什么那个gitway request吗对不对直接扔进来就OK了这扛车了这个代码呢就晚上完了啊晚上了之后呢大家注意看一下我们目前开户的第一阶段整个所有的代码就全部编下来了编完之后呢咱大概串一下啊这个串呢我就不再看这个图串了这个大家都很熟悉了我我看上代码大概串一下他是这样的啊嗯我们按照顺序吧他这样前端发请求先到哪是先到用户中心是吧
[01:33] 他这样啊来我们找一找consumer前端发请求先到这是这吧然后前端发过来数据里边是不是就有一堆数据了就是有什么影响卡号身份证号之类信息我们是用consumer request来接收了对不对接完之后呢我们又往这里边存了一个当前动用用户的什么呀手机号啊又补充了一个值然后就扔给什么层了业务层好那个业务层之后业务层干什么事呢业务层是不是判断当前用户是否已经开会已经开会你就别挫热闹了
[02:08] 然后还要判断你这个银行卡你调过来一看有没有被绑定能用不能用然后都通过的话就开始什么样更新用户的信息因为卡丝用户在注册的时候这边是不是只保存了像手机号一些基本的信息现在呢这些什么身份证号啊银行卡号这些都要进行这个存储我们要进行更新然后还要再单独保存一个什么样银行卡的信息然后这边保存完之后呢就把这个数据远程发到哪对
[02:37] 这个存款代理服务这边然后这个按照流程就应该跳到哪了呀对跳到咱刚才写的这个代码就存款代理服务这边的Controller就到这儿了就刚才在刚完善的这个代码对吧就到这儿还是一个consumer request嘛到这之后呢他毫不犹豫直接扔给什么呀业务层那刚才写的这个代码然后先进行输这个交易记录的一个什么呀保存保存完之后呢这儿进行签名签名完之后呢把这个数据封装成什么类型啊
[03:05] 对给他位request的进行返回返回谁了呀那肯定是返回到这儿的嘛因为我这儿发起的远程调用嘛对不对返回到这儿这样呢又作为返回值进行了什么呀返回返回到哪返回到什么呀Controller这儿吧Controller直接就返回返回到就返回到对前端了前端呢接下来是不是该走第几端了对该走第二阶段了呀第二阶段在这儿是不是该携带这个数据直接往银行那边发请求来进行开户就行所以说这是咱开户
[03:35] 第一阶段这个所有的代码就编写完了编完之后呢咱接下来是不是得进行一个测试吧对吧测试通过之后咱就开始搞第二阶段

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲一个开户代理服务的实现，包括控制器接收请求、服务层处理业务逻辑、生成并签名网关请求，以及最终调用网关完成开户流程。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 `DepositoryRecordServiceImpl.java` 中的 `createConsumer` 方法，用于生成并签名网关请求。代码中包含对 `ConfigService` 的调用和 RSA 签名逻辑。
画面2: 展示了 `DepositoryRecordServiceImpl.java` 中的 `saveDepositoryRecord` 方法，用于保存交易记录。
画面3: 展示了 `DepositoryAgentController.java` 中的 `createConsumer` 方法，用于接收前端请求并调用服务层。
画面4: 展示了 `DepositoryAgentController.java` 中的 `@Autowired` 注解，用于注入 `DepositoryRecordService`。
画面5: 展示了 `DepositoryAgentController.java` 中的 `createConsumer` 方法，将请求委托给服务层。
画面6: 展示了 `GatewayController.java` 中的 `create` 方法，用于处理网关请求，包括解密、解析和调用银行服务。
画面7: 展示了 IDEA 的项目结构，选中了 `wanningzp-depository-agent-Service` 模块。
画面8: 展示了 `ConsumerController.java` 中的 `createConsumer` 方法，用于接收客户端请求并调用服务层。
画面9: 展示了 `ConsumerServiceImpl.java` 中的 `createConsumer` 方法，用于处理用户信息和银行卡信息。
画面10: 展示了 `ConsumerServiceImpl.java` 中的 `updateWrapper` 方法，用于更新用户信息。
画面11: 展示了 `ConsumerServiceImpl.java` 中的 `bankCardService.saveOrUpdateData` 方法，用于保存银行卡信息。
画面12: 展示了 `DepositoryRecordServiceImpl.java` 中的 `createConsumer` 方法，用于生成并签名网关请求。
画面13: 展示了 `DepositoryRecordServiceImpl.java` 中的 `createConsumer` 方法，用于生成并签名网关请求。
画面14: 展示了开户业务流程图，描述了从客户端到银行的开户流程。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1:
```java
import org.springframework.stereotype.Service;
import java.time.LocalDateTime;

@Service
public class DepositoryRecordServiceImpl extends ServiceImp<DepositoryRecordMapper, DepositoryRecord> implements DepositoryRecordService {

    @Autowired
    private ConfigService configService;

    @Override
    public GatewayRequest createConsumer(ConsumerRequest consumerRequest) {
        // 保存交易记录
        saveDepositoryRecord(consumerRequest);

        // 签名数据并返回
        String reqData = JSON.toJSONString(consumerRequest);
        String sign = RSAUtil.sign(reqData, configService.getPrivateKey(), input_charset: "utf-8");
        GatewayRequest gatewayRequest = new GatewayRequest();
        gatewayRequest.setServiceName("PERSONAL_REGISTER");
        gatewayRequest.setPlatformId(configService.getPlatformId());
        gatewayRequest.setRequestData(EncryptUtil.encodeURL(EncryptUtil.encodeUTF8StringBased64(reqData)));
        gatewayRequest.setSignature(EncryptUtil.encodeURL(EncryptUtil.encodeUTF8StringBased64(sign)));
        gatewayRequest.setDepositUrl(configService.getDepositUrl() + "/gateway");
        return gatewayRequest;
    }
```

画面2:
```java
private void saveDepositoryRecord(ConsumerRequest consumerRequest) {
    DepositoryRecord depositoryRecord = new DepositoryRecord();
    depositoryRecord.setReqId(consumerRequest.getReqId());
    depositoryRecord.setReqTime(consumerRequest.getReqTime());
    depositoryRecord.setReqData(consumerRequest.getReqData());
    depositoryRecord.setSign(consumerRequest.getSign());
    depositoryRecord.setServiceName(consumerRequest.getServiceName());
    depositoryRecord.setPlatformId(consumerRequest.getPlatformId());
    depositoryRecord.setReqStatus(ReqStatusEnum.PENDING.getCode());
    depositoryRecord.setReqType(consumerRequest.getReqType());
    depositoryRecord.setReqSource(consumerRequest.getReqSource());
    depositoryRecord.setReqChannel(consumerRequest.getReqChannel());
    depositoryRecord.setReqIp(consumerRequest.getReqIp());
    depositoryRecord.setReqUserAgent(consumerRequest.getReqUserAgent());
    depositoryRecord.setReqReferer(consumerRequest.getReqReferer());
    depositoryRecord.setReqUser(consumerRequest.getReqUser());
    depositoryRecord.setReqPassword(consumerRequest.getReqPassword());
    depositoryRecord.setReqMobile(consumerRequest.getReqMobile());
    depositoryRecord.setReqEmail(consumerRequest.getReqEmail());
    depositoryRecord.setReqCardNo(consumerRequest.getReqCardNo());
    depositoryRecord.setReqCardType(consumerRequest.getReqCardType());
    depositoryRecord.setReqCardCode(consumerRequest.getReqCardCode());
    depositoryRecord.setReqCardName(consumerRequest.getReqCardName());
    depositoryRecord.setReqCardStatus(consumerRequest.getReqCardStatus());
    depositoryRecord.setReqCardStatusDesc(consumerRequest.getReqCardStatusDesc());
    depositoryRecord.setReqCardStatusTime(consumerRequest.getReqCardStatusTime());
    depositoryRecord.setReqCardStatusDesc(consumerRequest.getReqCardStatusDesc());
    depositoryRecord.setReqCardStatusTime(consumerRequest.getReqCardStatusTime());
    depositoryRecord.setReqCardStatusDesc(consumerRequest.getReqCardStatusDesc());
    depositoryRecord.setReqCardStatusTime(consumerRequest.getReqCardStatusTime());
    depositoryRecord.setReqCardStatusDesc(consumerRequest.getReqCardStatusDesc());
    depositoryRecord.setReqCardStatusTime(consumerRequest.getReqCardStatusTime());
    depositoryRecord.setReqCardStatusDesc(consumerRequest.getReqCardStatusDesc());
    depositoryRecord.setReqCardStatusTime(consumerRequest.getReqCardStatusTime());
    depositoryRecord.setReqCardStatusDesc(consumerRequest.getReqCardStatusDesc());
    depositoryRecord.setReqCardStatusTime(consumerRequest.getReqCardStatusTime());
    depositoryRecord.setReqCardStatusDesc(consumerRequest.getReqCardStatusDesc());
    depositoryRecord.setReqCardStatusTime(consumerRequest.getReqCardStatusTime());
    depositoryRecord.setReqCardStatusDesc(consumerRequest.getReqCardStatusDesc());
    depositoryRecord.setReqCardStatusTime(consumerRequest.getReqCardStatusTime());
    depositoryRecord.setReqCardStatusDesc(consumerRequest.getReqCardStatusDesc());
    depositoryRecord.setReqCardStatusTime(consumerRequest.getReqCardStatusTime());
    depositoryRecord.setReqCardStatusDesc(consumerRequest.getReqCardStatusDesc());
    depositoryRecord.setReqCardStatusTime(consumerRequest.getReqCardStatusTime());
    depositoryRecord.setReqCardStatusDesc(consumerRequest.getReqCardStatusDesc());
    depositoryRecord.setReqCardStatusTime(consumerRequest.getReqCardStatusTime());
    depositoryRecord.setReqCardStatusDesc(consumerRequest.getReqCardStatusDesc());
    depositoryRecord.setReqCardStatusTime(consumerRequest.getReqCardStatusTime());
    depositoryRecord.setReqCardStatusDesc(consumerRequest.getReqCardStatusDesc());
    depositoryRecord.setReqCardStatusTime(consumerRequest.getReqCardStatusTime());
    depositoryRecord.setReqCardStatusDesc(consumerRequest.getReqCardStatusDesc());
    depositoryRecord.setReqCardStatusTime(consumerRequest.getReqCardStatusTime());
    depositoryRecord.setReqCardStatusDesc(consumerRequest.getReqCardStatusDesc());
    depositoryRecord.setReqCardStatusTime(consumerRequest.getReqCardStatusTime());
    depositoryRecord.setReqCardStatusDesc(consumerRequest.getReqCardStatusDesc());
    depositoryRecord.setReqCardStatusTime(consumerRequest.getReqCardStatusTime());
    depositoryRecord.setReqCardStatusDesc(consumerRequest.getReqCardStatusDesc());
    depositoryRecord.setReqCardStatusTime(consumerRequest.getReqCardStatusTime());
    depositoryRecord.setReqCardStatusDesc(consumerRequest.getReqCardStatusDesc());
    depositoryRecord.setReqCardStatusTime(consumerRequest.getReqCardStatusTime());
    depositoryRecord.setReqCardStatusDesc(consumerRequest.getReqCardStatusDesc());
    depositoryRecord.setReqCardStatusTime(consumerRequest.getReqCardStatusTime());
    depositoryRecord.setReqCardStatusDesc(consumerRequest.getReqCardStatusDesc());
    depositoryRecord.setReqCardStatusTime(consumerRequest.getReqCardStatusTime());
    depositoryRecord.setReqCardStatusDesc(consumerRequest.getReqCardStatusDesc());
    depositoryRecord.setReqCardStatusTime(consumerRequest.getReqCardStatusTime());
    depositoryRecord.setReqCardStatusDesc(consumerRequest.getReqCardStatusDesc());
    depositoryRecord.setReqCardStatusTime(consumerRequest.getReqCardStatusTime());
    depositoryRecord.setReqCardStatusDesc(consumerRequest.getReqCardStatusDesc());
    depositoryRecord.setReqCardStatusTime(consumerRequest.getReqCardStatusTime());
    depositoryRecord.setReqCardStatusDesc(consumerRequest.getReqCardStatusDesc());
    depositoryRecord.setReqCardStatusTime(consumerRequest.getReqCardStatusTime());
    depositoryRecord.setReqCardStatusDesc(consumerRequest.getReqCardStatusDesc());
    depositoryRecord.setReqCardStatusTime(consumerRequest.getReqCardStatusTime());
    depositoryRecord.setReqCardStatusDesc(consumerRequest.getReqCardStatusDesc());
    depositoryRecord.setReqCardStatusTime(consumerRequest

