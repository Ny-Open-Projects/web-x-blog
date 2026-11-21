# 20.获取支付结果-支付结果更新

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day09 支付结果获取 RocketMQ
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day09 支付结果获取 RocketMQ\20.获取支付结果-支付结果更新【海量资源尽在 666java.com】.mp4
- 时长 17分58秒（音频 1079s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们来讲支付结果更新那根据整个获取支付结果的技术方案我们知道支付渠道代理服务呢调用支付宝的订单查询接口查到订单的支付状态然后呢将订单支付状态发送到MQ然后这时候的交易服务是不是要监清MQ然后呢拿到订单的状态然后开始更新订单表当中的状态字段
[00:28] 这是后边我们要做的第三步和第四步这两个功能那么各位我们说支付结果要更新肯定是首先需要支付渠道这个代理服务将查询到的支付结果把它发送到哪里啊MQ那你也知道支付渠道代理服务呢它是不是就查询的这个代码呢是刚才我们写的你看
[00:56] 是不是调用阿里的支付查询接口查到了结果吗查到了结果之后我觉得应该是在这看见吗对要把它把它发到MQ上对不对然后这里边是支付协调代理服务向MQ发然后呢交易服务呢还要监听所以下面我们来做这个工作首先发送的话还是照常规我们需要写一个发送的producer的方法原来我们发的是啥
[01:27] 要求去查询订单状态的一个消息现在你发送消息发的啥你发的可就是直接是发你查询到的这个什么支付结果了对不对所以各位这个发送的方法我们先写一下这个发送方法参数呢我们还用这个参数吧行吧好那现在问题来了原来我们发一个查询
[01:53] 消息它是延迟消息对吧那现在我们要发一个消息的话它还需要延迟吗不需要了吧为啥因为你已经拿到结果了嘛对不对你现在就是迫不及待赶紧发给MQ让交易服务去获取消息更新状态嘛所以这里边呢我们就直接不要延迟了那么我就发一个同步方法就行可以吧然后呢我们就用这个哎topic我们不能用同一个topic吧这个是订单查询的这个消息
[02:22] 我觉得应该还要建一个topic这个topic应该是专门是干嘛拿订单结果的topic就这两个topic大家理解吗这个是什么叫订单结果查询的topic懂吧而下边这个是什么是查询到结果了把结果发到MQ里那这就是订单结果的topic懂吧
[02:53] 所以这里面呢我们要让它发到这里头然后呢你就发谁啊发这个对象就行了在这个方法我就想好了这个方法写好了之后呢接下来我们是不是就可以去调这方法再哪调再哪调再回到这个图上因为这个发来发去可能就把大家发懵了你不要着急你捋思路现在刚才我写的方法是不是第三步向MQ发的消息那我问你什么时候
[03:24] 支付区的代理服务要向MQ发这个支付结果的消息是不是当他拿到支付结果之后就要发呀拿支付结果的代码在哪是不是也是支付区的代理服务他消费嘛当初他是不是消费了一个订单查询的消息然后是不是开始查询订单了然后查询完订单的结果之后各位在这我们是不是要调用刚才我们写的那个方法那调用刚才写的方法我们是不是就需要对在这吧
[03:53] 配producer注进去然后在这掉一下这个是不是就是要发送一个结果通知的这个消息吗结果通知这消息他需要传什么呀你看一下他是不是需要传一个对象吗传一个对象的话他就是把从支付宝查询到的这个结果就这个response DTO你把它传进去这就行了对吧有时候老师这DTO是个空啊对不对你传进去吗
[04:23] 这个空你看它如果是支付宝这是不是就查询到结果了对微信是不是就查询到结果了你这个代码如果想写的严谨的话可以这么写如果说它等于空或者说拿到结果是no或者说拿到结果是支付中我们都让它抛一层让它再次查就证明这个结果不合法就是没有查到这样就行了
[04:48] 好了那这样的话我们是不是就实现了支付区的代理服务向MQ发消息那么支付区的代理服务向MQ发完消息接下来呢是不是就是开交易服务去接消息了对吧那交易服务接消息接收到消息怎么办他是不是要更新订单所以我们先把更新订单的这个接口呢给他写了懂吧好我们思路跟得上啊现在又跑到交易服务了交易服务要干嘛是吧接到消息要更新订单
[05:18] 那接到消息更新订单我们就要写一个更新订单的接口懂了吧好这个更新订单的接口的话那你需要拿什么参数啊一个肯定是订单号嘛另外还有一点你再看我们的这个订单表就是你根据订单号去更新我们的这个订单状态是没有问题的另外你别忘了支付宝给你
[05:45] 返回结果的时候他把支付宝自己的这个订单啊也给你了你看这里面有一个字段叫啥叫原始渠道订单号看见了吗就是我们我们自己的订单号你看叫tradenumber嘛就是散去平台订单号根据散去平台订单号从支付宝查到了这个订单他的支付状态同时支付宝呢也把他系统的订单号也给我们了就我们呢在我们数据库呢也保存一下懂了吧所以这里边呢我们就需要传至少两个参数
[06:15] 两个参数一个参数是我们散聚的订单号一个参数是支付给我们的他系统的订单号同时还有一个最重要的一个参数是什么呢就是状态因为你现在更新的就是订单状态你肯定是少不了这个什么状态的这样我们这个参数就搞定了对吧然后我们也可以让他去抛一个自定义一长如果有问题那么这个接口其实很简单就是更新什么更新状态
[06:43] 那么更新状态我们需要传几个参数啊一个是三聚平台订单号一个是支付宝或微信的交易流水号其实这个就是交易流水号就叫啥就指第三方支付系统的订单号就是他们系统订单号然后呢并别把订单状态也给咱好那接下来我们是不是就可以怎么弄去实现一下这个结果这就是更新嘛好那更新的话那就paypay ordermapupdate
[07:14] 对吧那更新的话这里边怎么更新呢更新看好我们需要Nu一个Lambda update你更新这张表那我就是它各位这这个Lambda的这个这个写错了啊不要写太快一快就错看Lambda看update wrapper看见了吗对我们要用这个wrapper那现在这个wrapper怎么用呢你根据什么来更新呢你根据什么来更新你得EQ写条件
[07:45] 对不对你根据我们说的这个散区平台的订单号来更新那你就得找到订单号是不是就是这个tree number那这个tree number现在你看是不是也传进来了大家看懂了吗你根据它来更新更新谁呢对更新谁你得写set对更新谁那你这都我刚才说了嘛要更新订单状态这肯定是必须的没错往下翻你看是不是有一个订单状态然后呢你把
[08:13] 订单状态放进去对吧还要更新谁啊刚才也说了还要更新的就是支付宝微信给我们返回他自己系统的订单他自己系统的订单是不是就是这个pay channel trade number对吧这样的话我们就把我们该更新的就更新完了然后你把这个对象放进去前面第一个是我们写的no你看他是什么
[08:42] 什么第一个实体的实体类型我们就不需要直接让他执行这个rapper就行了好这样的话各位update就写完了吧update写完了之后我们再回到这来接下来要做什么接下来要做啥看我抱错了看一下我们就需要接下来让他去消费消费这个什么消息了是不是啊
[09:09] 好我们把这儿补一下啊这儿报错好那接下来我们说交易服务要去消费消息那我们肯定是要让交易服务仍然要连上RocketMQ的对不对所以我们要在交易服务的碰文件当中把RocketMQ的依赖加进去然后呢还要让交易服务的主配置文件也要加载RocketMQ的配置这样他是不是就可以读到name server的地址
[09:36] 那接下来我们就可以来写这个什么写这个消费的这个类型好那这个消费的这个类型我们需要在我们统一一般来说MQ的东西我们都在message当中写懂吗然后在这里边呢我们就写好开始了啊又开始MQ了这里边开始监听监听这里边各位俩东西一个是topic一个是消费组对吧topic
[10:07] 是谁消费主是谁你告诉我消费主我们自定义一个名称就行了关键是topic对吧谁给交易服务发的消息是不是叫支付渠道代理服务发的对吧那支付渠道代理服务发的消息在这儿吗你看他的topic是不是他找到了吧所以你topic千万别弄错你弄错了你可以接不到消息对然后呢就可以接着
[10:37] 在这这个消费者的这个组吧你弄一个字幕串对不一样和原来的组不一样就行了OK了好然后呢让他实现RocketMQ listener对吧好然后这里边呢仍然是怎么弄仍然是写message这个这个ext对吧好然后让他把这个方法报出来这是不是就齐了
[11:09] 然后接下来我们就开始来解析吧这里头仍然跟以前一样是不是就拿到body它是一个直接数组new一个string然后body这是不是就我们拿到了我们说的Jason Chuan了因为他发送的时候是不是转Jason发送了那么Jason Chuan我们拿到了之后呢你是不是要转成对象了呀转对象怎么转呀转对象好转关键是你转成啥对象对不对你转成什么对象你原来发是谁发的你得看你看谁发的
[11:41] 是不是这里发的这里发的他的对象类型是不是他所以你转的时候呢你得这么来转打开这你转的时候你要写这个类型对吧好这样的话我们是不是就是把这个消息呢就拿到了消息拿到之后呢注意别着急现在这个就是我们接收到的消息那这个消息内容里边包括了什么你要知道包括了我们说的订单的状态对不对
[12:14] 好那下面我们要做什么事呢那就开始解析它了那我们就拿出来它的订单结果吧你看订单状态是不是它对吧拿出来之后呢我们说这就是我们说的订单状态那订单状态拿出来之后我们说那更新数据库吧是不是要更新数据库的订单表啊对吧那更新那我们刚才也我们刚才也写完了它是一个我们是不是写了一个更新方法对不对那我们就把它注进去吧注进去Transaction Service把它注进去
[12:44] 好这我们都搞定了那接下来就调更新吧调更新那调更新各位问题来了就是你调更新没错但是你更新你看更新需要三个参数你怎么给他传对不对这不是问题吗更新是要根据我们说的什么订单号来更新订单号呢订单号呢订单号在这啊拿到啊这是不是就订单号我把它都取出来这是我们的订单号
[13:15] 没错吧对不对这里头还有这里头还有这是谁的这是支付宝的订单号就是支付宝微信的订单号懂吧然后还有什么呢还有就是状态状态你是不是也取出来了那你说这我都取出来有人说老师那就更新嘛对不对更新但是你点进去你看人家的状态是个四幅串呀
[13:46] 对不对你的数据库要求是啥你要求是订单成功是二交易处理完成是三四是关闭对不对所以现在你需要做一件事更新数据库的时候呀你需要去根据这个订单状态的类型就是这个美酒类型对我们要来看如果说是成功你更新成什么
[14:16] 大家理解了吧如果是成功的话那么你就把这个东西往里边填注意停一下我们说这里边我们再看一下这里边的状态应该是我们解析的有问题原来我们放进去的这个你看一下我们现在放进去的是它吧这个是不是我们说支付宝给我们返回的呀你往后翻看好最终你看这里边拿到
[14:50] 你看你看啊注意看啊很关键的啊你看看散剧平台的订单号是谁啊你看我们返将来原来我们返回去的参数是out trade number这个支付宝的订单号是trade number看见了吧所以我刚才忽然间发现一个问题就是这里边我们刚才你看你不能这么对了你看trade number这个trade number啊它是支付宝微信的订单号
[15:17] 你根据刚才我们看到的这个才是我们说的散剧平台的订单号对吧你得看谁给你发的消息你得看谁你看这个是支部渠道代理服务发的你看最终他是咋发的你看这就是发的这几个参数对吧so other to the number是我们散剧平台的订单号所以咱们不要弄反了为什么我关注这个事呢因为你现在要更新了
[15:46] 是不是啊你更新了你是根据散去平台的更新这个订单号吗更新支出宝的订单然后呢再更新什么再更新订单状态当这个结果是成功我们就要把订单的状态更新成二看见了吗所以这写二对吧然后呢这个返回然后如果case它是no那就算了no肯定不能如果是什么呀嗯那你得看
[16:18] 如果是rework那这个呢应该就是订单就关闭了关闭的结果值我们看一下它是4对吧4这是订单关闭所以这几个我们都需要去更新这是我们说的成功了这是什么呀关闭了那最后一个呢还得有呀你说你如果失败了呢对不对你失败了呢说失败它这个里头也有
[16:49] 你看看意思你看这里头有没有一个是不是failed是吧失败了失败了我们单独再给它单独定一个叫5这叫失败数据库在这个注释这没有写那这呢我们说4是5那4关闭5就是失败懂了吧那如果说这些都不是呢都不是的话那你就不能更新了都不是你得跑一层了你得让它继续消费了就是无法解析这个支付结果
[17:20] 大家看懂了吗对这就是我们说的什么交易服务来更新订单的状态先要把这个消息解析出来解析出这个状态然后呢通过switch然后开始一个一个的去判断更新就这么一种方式那到这为止我们的支付结果更新这个功能就开发完了就是支付渠道呢它在消费到这个订单查询
[17:46] 然后呢查询到订单的结果之后然后呢向MQ发了一个订单结果消息这时候呢交易服务就拿到了这个消息然后解析然后更新到订单当中好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解支付结果更新的交互流程，包括通过MQ发送消息、消费消息并更新订单状态的代码实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示文档大纲，当前章节为6.6.1 交互流程，描述支付渠道代理服务查询支付结果后，通过MQ发送“支付结果更新”消息，交易服务监听并更新订单状态。
画面2：展示6.6.2 发送消息部分，代码中定义了发送“支付结果更新”消息的方法，使用rocketMQTemplate.convertAndSend发送。
画面3：展示PayConsumer类中，当查询到支付结果后，调用payProducer.payResultNotice方法发送消息。
画面4：展示PayConsumer类中，当支付状态未知时抛出异常，等待重试。
画面5：展示数据库表结构，包含TRADE_NO、MERCHANT_ID、STORE_ID等字段。
画面6：展示TransactionService类中，使用LambdaUpdateWrapper更新订单状态。
画面7：展示TransactionService类中，使用LambdaUpdateWrapper设置更新条件。
画面8：展示dubbo配置文件，定义了服务分组、端口、注册中心等信息。
画面9：展示PayProducer类中，定义了发送“支付结果更新”消息的常量TOPIC_RESULT。
画面10：展示PayProducer类中，根据支付渠道判断使用哪个接口查询订单状态。
画面11：展示TransactionConsumer类中，接收MQ消息并解析为PaymentResponseDTO。
画面12：展示AlipayClient类中，调用execute方法查询支付结果。
画面13：展示TransactionConsumer类中，根据支付状态更新订单状态。
画面14：展示TransactionConsumer类中，根据支付状态更新订单状态。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
6.6.1 交互流程
支付渠道代理服务查询到支付结果，将支付结果更新消息发送给交易服务，实现订单状态更新，流程如下：
1、支付渠道代理服务查询到支付结果
2、向MQ发送“支付结果更新”消息
3、交易服务监听“支付结果更新”消息队列
4、交易服务接收到“支付结果更新”消息，更新订单状态

画面2：
private static final String TOPIC_RESULT = "TP_PAYMENT_RESULT";
/**
 * 发送支付结果消息
 * @param result
 */
public void payResultNotice(PaymentResponseDTO result){
 rocketMQTemplate.convertAndSend(TOPIC_RESULT,result);
}

画面3：
//如果查询到订单状态为未知，抛出异常，等待重试
if(responseDTO == null || TradeStatus.UNKNOWN.equals(responseDTO.getTradeState()) || TradeStatus.USERPAYING.equals(responseDTO.getTradeState())){
 throw new RuntimeException("支付状态未知，等待重试");
}
//如果重试的次数达到一次数量，不要重试查询，将消息记录到数据库，由单独的程序人工进行处理
//将订单状态，再次发到mq
payProducer.payResultNotice(responseDTO);

画面4：
//如果查询到订单状态为未知，抛出异常，等待重试
if(responseDTO == null || TradeStatus.UNKNOWN.equals(responseDTO.getTradeState()) || TradeStatus.USERPAYING.equals(responseDTO.getTradeState())){
 throw new RuntimeException("支付状态未知，等待重试");
}
//如果重试的次数达到一次数量，不要重试查询，将消息记录到数据库，由单独的程序人工进行处理
//将订单状态，再次发到mq
payProducer.payResultNotice(responseDTO);

画面5：
Field Type Comment
ID bigint(20) NOT NULL 主键
TRADE_NO varchar(50) NOT NULL 订单号
MERCHANT_ID bigint(20) NOT NULL 商户ID
STORE_ID bigint(20) NOT NULL 店铺ID
APP_ID varchar(50) NOT NULL 应用ID
PAY_CHANNEL varchar(50) NOT NULL 支付渠道
PAY_CHANNEL_MCH_ID varchar(50) NULL 支付渠道商户ID
PAY_CHANNEL_MCH_APP_ID varchar(50) NULL 支付渠道商户应用ID
CHANNEL varchar(50) NULL 渠道
OUT_TRADE_NO varchar(50) NULL 交易流水号
GOODS_ID varchar(50) NULL 商品ID
GOODS_NAME varchar(255) NULL 商品名称
GOODS_PRICE decimal(10,2) NULL 商品价格
GOODS_NUM int(11) NULL 商品数量
GOODS_TOTAL decimal(10,2) NULL 商品总价
GOODS_TYPE varchar(50) NULL 商品类型
GOODS_ATTR varchar(255) NULL 商品属性
GOODS_DESC varchar(255) NULL 商品描述
GOODS_IMAGE varchar(255) NULL 商品图片
GOODS_URL varchar(255) NULL 商品链接
GOODS_URL_TYPE varchar(50) NULL 商品链接类型
GOODS_URL_NAME varchar(255) NULL 商品链接名称
GOODS_URL_DESC varchar(255) NULL 商品链接描述
GOODS_URL_IMAGE varchar(255) NULL 商品链接图片
GOODS_URL_PRICE decimal(10,2) NULL 商品链接价格
GOODS_URL_NUM int(11) NULL 商品链接数量
GOODS_URL_TOTAL decimal(10,2) NULL 商品链接总价
GOODS_URL_TYPE_NAME varchar(50) NULL 商品链接类型名称
GOODS_URL_TYPE_DESC varchar(255) NULL 商品链接类型描述
GOODS_URL_TYPE_IMAGE varchar(255) NULL 商品链接类型图片
GOODS_URL_TYPE_PRICE decimal(10,2) NULL 商品链接类型价格
GOODS_URL_TYPE_NUM int(11) NULL 商品链接类型数量
GOODS_URL_TYPE_TOTAL decimal(10,2) NULL 商品链接类型总价
GOODS_URL_TYPE_NAME_DESC varchar(255) NULL 商品链接类型名称描述
GOODS_URL_TYPE_NAME_IMAGE varchar(255) NULL 商品链接类型名称图片
GOODS_URL_TYPE_NAME_PRICE decimal(10,2) NULL 商品链接类型名称价格
GOODS_URL_TYPE_NAME_NUM int(11) NULL 商品链接类型名称数量
GOODS_URL_TYPE_NAME_TOTAL decimal(10,2) NULL 商品链接类型名称总价
GOODS_URL_TYPE_NAME_DESC_IMAGE varchar(255) NULL 商品链接类型名称描述图片
GOODS_URL_TYPE_NAME_DESC_PRICE decimal(10,2) NULL 商品链接类型名称描述价格
GOODS_URL_TYPE_NAME_DESC_NUM int(11) NULL 商品链接类型名称描述数量
GOODS_URL_TYPE_NAME_DESC_TOTAL decimal(10,2) NULL 商品链接类型名称描述总价
GOODS_URL_TYPE_NAME_DESC_IMAGE_PRICE decimal(10,2) NULL 商品链接类型名称描述图片价格
GOODS_URL_TYPE_NAME_DESC_IMAGE_NUM int(11) NULL 商品链接类型名称描述图片数量
GOODS_URL_TYPE_NAME_DESC_IMAGE_TOTAL decimal(10,2) NULL 商品链接类型名称描述图片总价
GOODS_URL_TYPE_NAME_DESC_IMAGE_PRICE_NUM int(11) NULL 商品链接类型名称描述图片价格数量
GOODS_URL_TYPE_NAME_DESC_IMAGE_PRICE_TOTAL decimal(10,2) NULL 商品链接类型名称描述图片价格总价
GOODS_URL_TYPE_NAME_DESC_IMAGE_PRICE_NUM_TOTAL decimal(10,2) NULL 商品链接类型名称描述图片价格数量总价
GOODS_URL_TYPE_NAME_DESC_IMAGE_PRICE_NUM_TOTAL_DESC varchar(255) NULL 商品链接类型名称描述图片价格数量总价描述
GOODS_URL_TYPE_NAME_DESC_IMAGE_PRICE_NUM_TOTAL_DESC_IMAGE varchar(255) NULL 商品链接类型名称描述图片价格数量总价描述图片
GOODS_URL_TYPE_NAME_DESC_IMAGE_PRICE_NUM_TOTAL_DESC_IMAGE_PRICE decimal(10,2) NULL 商品链接类型名称描述图片价格数量总价描述图片价格
GOODS_URL_TYPE_NAME_DESC_IMAGE_PRICE_NUM_TOTAL_DESC_IMAGE_PRICE_NUM int(11) NULL 商品链接类型名称描述图片价格数量总价描述图片价格数量
GOODS_URL_TYPE_NAME_DESC_IMAGE_PRICE_NUM_TOTAL_DESC_IMAGE_PRICE_NUM_TOTAL decimal(10,2) NULL 商品链接类型名称描述图片价格数量总价描述图片价格数量总价
GOODS_URL_TYPE_NAME_DESC_IMAGE_PRICE_NUM_TOTAL_DESC_IMAGE_PRICE_NUM_TOTAL_DESC varchar(255) NULL 商品链接类型名称描述图片价格数量总价描述图片价格数量总价描述
GOODS_URL_TYPE_NAME_DESC_IMAGE_PRICE_NUM_TOTAL_DESC_IMAGE_PRICE_NUM_TOTAL_DESC_IMAGE varchar(255) NULL 商品链接类型名称描述图片价格数量总价描述图片价格数量总价描述图片
GOODS_URL_TYPE_NAME_DESC_IMAGE_PRICE_NUM_TOTAL_DESC_IMAGE_PRICE_NUM_TOTAL_DESC_IMAGE_PRICE decimal(10,2) NULL 商品链接类型名称描述图片价格数量总价描述图片价格数量总价描述图片价格
GOODS_URL_TYPE_NAME_DESC_IMAGE_PRICE_NUM_TOTAL_DESC_IMAGE_PRICE_NUM_TOTAL_DESC_IMAGE_PRICE_NUM int(11) NULL 商品链接类型名称描述图片价格数量总价描述图片价格数量总价描述图片价格数量
GOODS_URL_TYPE_NAME_DESC_IMAGE_PRICE_NUM_TOTAL_DESC_IMAGE_PRICE_NUM_TOTAL_DESC_IMAGE_PRICE_NUM_TOTAL decimal(10,2) NULL 商品链接类型名称描述图片价格数量总价描述图片价格数量总价描述图片价格数量总价
GOODS_URL_TYPE_NAME_DESC_IMAGE_PRICE_NUM_TOTAL_DESC_IMAGE_PRICE_NUM_TOTAL_DESC_IMAGE_PRICE_NUM_TOTAL_DESC varchar(255) NULL 商品链接类型名称描述图片价格数量总价描述图片价格数量总价描述图片价格数量总价描述
GOODS_URL_TYPE

