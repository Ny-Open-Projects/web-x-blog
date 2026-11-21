# 18.获取支付结果-支付结果查询-生产消息

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day09 支付结果获取 RocketMQ
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day09 支付结果获取 RocketMQ\18.获取支付结果-支付结果查询-生产消息【海量资源尽在 666java.com】.mp4
- 时长 11分32秒（音频 692s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们继续来实现交易结果的查询那么我们整个流程各位当前我们已经完成了支付渠道代理服务调用支付宝来查询订单状态的这个接口咱们做完了那做完了之后呢接下来这个就开始第一步了开始向MQ来发消息然后呢支付渠道代理服务呢他自己接消息开始调用刚才我们写的查询支付宝
[00:28] 交易状态这个接口来查询交易状态好那这个6.5章节呢就是支付结果的查询那支付结果查询我们是需要做哪些事呢其实主要就是发消息第一步支付渠道代理服务要在调用支付宝下单接口之后呢向MQ来发一个消息这个消息是一个延迟消息这个消息的内容呢就是要求查询
[00:57] 支付的结果那么消费方呢还是他本人支付渠道代理服务呢他自己去消费消费接收到这个消息他要调用这个第三方的这个支付结果查询接口来查询那好我们找到代码吧看这个文字呢看着不是非常直接我们找到代码当初我们写支付渠道代理服务我们写了很多的方法其中有一个方法是调用支付宝的下单接口
[01:27] 各位是不是在这儿呀那么我们知道这一步是不是就是请求下单呀对那我们想是不是要下单过了之后我们要做什么事啊我们是不是准备让他去向MQ发消息发一条延迟消息这个延迟消息是干啥的呀对这条消息的内容就是要进行什么
[01:58] 结果的查询嗯就是支付结果查询就发这个消息哎那么这个是支付渠道代理服务他调支付宝下单完了之后我们是不是要延迟一段时间开始查结果了那么他这呢要发一条消息那各位我们不是说了吗他自己还要消费这条消息对不对所以我们还需要待会在这再写一个类然后呢我们要定义一个监听
[02:28] 对吧监听这个队列然后呢拿到消息然后呢他才可以调用刚才我们写的调用支付宝他的接口来查订单状态看懂这个流程了吧好那么我们按照顺序来写首先呢我们在这呢准备发消息那么你发消息你得先把这个消息给他构建出来对不对那么构建出这个消息的话那这里边呢我们就需要怎么做呀
[02:58] 主要是这个准备一些环境吧你最终发消息你肯定是要和这个Rocket MQ通信啊所以我们在支付渠道代理服务当中咱们把Rocket MQ的包咱们把它加进来好然后把Rocket MQ包加进来之后呢接下来还有啊你是不是得连接Name Server所以我们就需要在我们的Necros里面专门配一个Rocket MQ的配置文件方便其他
[03:27] 服务呢去使用好那这里面呢它就叫rocket mcode然后呢然后把它配成一般这种不是主配置文件了我们都是把它统一为common group然后呢这rocket mcode的配置文件也比较简单其实就是连一个name server那它就可以了这就是我们说的rocket mcode的配置就搞定了吧好然后呢你这个配完了之后呢那你是不是需要在我们说
[03:57] 支付渠道代理服务是不是要连RockMQ那你就需要去在你的组配置文件当中去把它加上大家的眼睛不要长仔细看因为这个工程切的比较快这是什么支付渠道代理服务吧那在这它是不是要连RockMQ了那你是不是要把它给加上对这样的话它是不是就连上了好准备工作搞定然后接下来再回到代码我们不是按照流程说吗当下单完了之后
[04:27] 是不是准备让他发消息了好那么发消息咱们就发啊怎么发呀先构建一个消息的内容嘛是不是啊那这个消息的内容咱们怎么构建呢那么我们还用咱们之前用到的这个类啊叫payment这个类这个类呢你可别小看这个类它可是一个万能类为啥说它是一个万能类呢
[04:53] 因为它这里头有一个什么content范形你看见了吗那里边可以填很多东西对任意类型都能往里边放方便我们做接口交互那行我们呢继续来写那这里头准备做哪些事呢往里边放哪些东西呢那么我们这里边准备放首先一个订单号肯定得有吧你查订单的状态你肯定得有订单号对不对所以这里边呢我们就要往里边放一个订单号
[05:23] 对吧订单号那么这个订单号在哪呢你前面是不是做了一个下单吗上面是下单代码这是早期写的代码你慢点看啊你慢点看然后我们看一下这是上这是前面写的下单对吧下单那你是不是就你看这看这这是不是就是我们的订单号你把它拿过来对你要查订单吗你肯定要把我们
[05:53] 散具平台的订单号你传到这个支付宝然后其次我们也当初研究过需要干嘛各位除了订单号还需要啥是不是还需要这个支付渠道参数支付渠道参数我们怎么找到支付渠道参数在这个里头你看有它本身它这个行参就是支付渠道参数你看就是为咱量身定做的但是这个支付渠道参数各位
[06:22] 我准备把它放到这个content里头对就是各位你看啊我现在写好这个这个结果这是不是就是我把准备要发的消息就整理好了整理好了之后还差一个啊这个消息呢里头呢我标识一下因为将来还要接微信我标识一下这表示是发的这个是这个消息里头是不是准备调用支付宝的吗哎这标识是对查询支付宝的接口
[06:50] 是吧这是不是支付宝的那个阿里佩Waaf这个接口啊好消息准备好了准备开始发送对吧发送用什么法啊用什么法我们肯定还需要写一个什么对我们需要写一个单独的类让他发消息就跟我们当初研究Rockett MQ一样我们写一个Producer的类让他发消息对吧好那我们现在呢就写一个Producer的类这类呢
[07:17] 现在肯定是还没有但是我先放到这你大概知道就是这么个意思看见了吗懂了吧好你看当下单成功了之后也不是成功反正就是下单完成下单完成之后我们就开始发消息延迟消息是吧延迟消息这个延迟到底是怎么个延迟法我们就需要在producer里面来做文章了那么首先这里面你看创建一个message的包然后在这我们就开始新建一个producer
[07:48] 就叫做Pay Producer那这个是不是就是我们说的专门用来生产消息的那这个他首先要做的一件事是不是就是要这是干嘛呀对发送消息嘛这啥消息啊这个消息就是我们说的叫做查询支付宝订单状态的消息对不对那你这个消息
[08:18] 是查询支付宝的订单状态对吧那你查询支付宝的订单状态你怎么查呢你肯定得有topic呀你发消息对不对那你发一个消息的话你没有topic那你发到哪里啊所以咱们所有凡是你发消息还有你监听消息都得先把topic给他定出来这topic呢我们就叫做TP然后呢payment order我们准备发一个订单查询的消息那发这个订单的查询消息的话
[08:47] 各位我们你也知道刚才我们的消息内容你也看到了叫做payment response DTO对不对所以那我就很清楚这里面这个参数就叫做payment response DTO对不对然后呢各位在这里头我才来发消息懂了吗这个时候你再回到刚才我们的下单这注意
[09:15] 我们说下单完成是不是要发消息对不对好发延迟消息那各位刚才的这个什么那个producer我是不是就已经创建出来了那你创建出来之后我们就可以把它干嘛就把它注进去了对不对好注进去注进去了之后你看这代码就不报错了对吧这个时候我们再进来
[09:41] 开始发那发消息我们之前研究过RocketMQ我们需要用一个什么叫RocketMQ的什么timeplate模板类对不对所以这里面他要发发什么消息呢是发一个什么延迟消息对吧延迟消息那这个延迟消息各位我们之前学习过延迟消息是不是后边需要指定delay level是不是所以这里面呢我们就可以把我们的目标主题
[10:10] 放进去然后呢我们要构建一个消息体原来我们学过RocketMQ对吧构建消息体需要怎么弄啊需要用它的一个builder的这个工具类然后build一下就出来了那出来这个message之后是不是就可以把它放到这对吧然后呢发送的时候一个操作时间随便设一秒然后延迟让它几秒发送呢我们说那延迟三秒吧三哪是三秒呀
[10:40] 33秒不是第三个等级是10秒对吧我们之前学过Rocket MQ是不是总共18个等级所以这里面我们说延迟第三级发送第三级发送的话就相当于我们刚才说的什么延迟10秒如果你要是Rocket MQ有点淡忘了你就回头再复一下我给大家讲的Rocket MQ好各位这是不是就发消息到这咱们说
[11:10] 这个就是当下单通过然后呢我们让他调用我们的producer准备开始发消息这个就是我们的在获取支付结果然后呢下单成功之后然后调用我们说的producer然后呢生产一条消息好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在支付代理服务中集成支付宝接口并使用 RocketMQ 发送支付结果通知消息。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程文档“6.5 支付结果查询”章节，重点在“6.5.2 发送消息”下的“6.5.2.1 配置RocketMQ”，并显示了需要添加的 Maven 依赖。
画面 2: 在 IDE 中展示 `AlipayClient` 的 `pageExecute` 方法，用于发起支付请求并返回响应。
画面 3: 在 IDE 中展示 `queryOrderBySync` 方法，用于查询支付宝订单状态，其中包含获取配置参数的代码。
画面 4: 展示在 Nacos 中为 RocketMQ 配置 `spring-boot-starter-RocketMQ.yaml` 文件，配置了 `nameServer`。
画面 5: 在 Nacos 界面中新建配置，Data ID 为 `spring-boot-starter-RocketMQ.yaml`，Group 为 `COMMON_GROUP`，格式为 YAML。
画面 6: 在 IDE 中展示 `bootstrap.yml` 文件，配置了 RocketMQ 的 `nameServer` 和 `group`。
画面 7: 在 IDE 中展示 `AlipayClient` 的 `pageExecute` 方法，用于发起支付请求并返回响应。
画面 8: 在 IDE 中展示 `createPayOrderByAli` 方法，用于创建支付宝订单，其中包含获取配置参数和初始化 `AlipayClient` 的代码。
画面 9: 在 IDE 中展示 `PaymentResponseDTO` 类的 `setContent` 方法，用于设置响应内容。
画面 10: 在 IDE 中展示 `AlipayClient` 的 `pageExecute` 方法，用于发起支付请求并返回响应。
画面 11: 展示课程文档“6.5.2.2 生产消息类”，并显示了 `PayProducer` 类中用于发送消息的代码。
画面 12: 在 IDE 中展示 `@Configuration` 配置类，用于配置 `AliConfigParam`。
画面 13: 在 IDE 中展示 `PayProducer` 类中用于发送消息的代码，其中包含 `rocketMQTemplate` 的使用。
画面 14: 展示支付确认页面，提示“由于没有数据，订单信息均为空”，并提到“4.3.2 页面完善”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```xml
<dependency>
    <groupId>org.apache.RocketMQ</groupId>
    <artifactId>RocketMQ-spring-boot-starter</artifactId>
    <version>2.0.2</version>
</dependency>
```

画面 4:
```yaml
RocketMQ:
  nameServer: 127.0.0.1:9876
```

画面 5:
Data ID: spring-boot-starter-RocketMQ.yaml
Group: COMMON_GROUP
配置格式: YAML

画面 6:
```yaml
RocketMQ:
  nameServer: 127.0.0.1:9876
  group: PID_PAY_PRODUCER
```

画面 11:
```java
import javax.annotation.Resource;

@SLF4J
public class PayProducer {

    @Resource
    private RocketMQTemplate rocketMQTemplate;

    public void payOrderNotice(PaymentResponseDTO result) {
        log.info("支付通知发送延迟消息:{}", result);
        try {
            //处理消息存储格式
            Message<PaymentResponseDTO> message = MessageBuilder.withPayload(result).build();
            SendResult sendResult = rocketMQTemplate.syncSend(TOPTC_ORDER, message, 1000, 3);
        } catch (Exception e) {
            log.warn(e.getMessage(), e);
        }
    }
}
```

画面 12:
```java
@Configuration
public class AliConfigParamConfig {

    @Bean
    public AliConfigParam aliConfigParam() {
        return new AliConfigParam();
    }
}
```

画面 13:
```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class PayProducer {

    @Autowired
    private RocketMQTemplate rocketMQTemplate;

    //发送消息
    public void payOrderNotice(PaymentResponseDTO result) {
        log.info("支付通知发送延迟消息:{}", result);
        try {
            //处理消息存储格式
            Message<PaymentResponseDTO> message = MessageBuilder.withPayload(result).build();
            SendResult sendResult = rocketMQTemplate.syncSend(TOPTC_ORDER, message, 1000, 3);
        } catch (Exception e) {
            log.warn(e.getMessage(), e);
        }
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: 标题为“6.5 支付结果查询”，子标题“6.5.2 发送消息”。
画面 4: 标题为“6.5.2.1 配置RocketMQ”，内容为在 Nacos 中添加配置。
画面 5: 标题为“新建配置”，内容为 Data ID、Group、配置格式。
画面 6: 标题为“bootstrap.yml”，内容为配置项。
画面 11: 标题为“6.5.2.2 生产消息类”，内容为 `PayProducer` 类。
画面 14: 标题为“4.3.2 页面完善”，内容为支付确认页面的说明。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

