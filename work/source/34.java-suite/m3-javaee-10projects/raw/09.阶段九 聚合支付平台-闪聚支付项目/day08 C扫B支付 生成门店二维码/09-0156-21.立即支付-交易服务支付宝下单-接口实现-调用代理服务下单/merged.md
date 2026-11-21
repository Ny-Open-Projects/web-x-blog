# 21.立即支付-交易服务支付宝下单-接口实现-调用代理服务下单

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day08 C扫B支付 生成门店二维码
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day08 C扫B支付 生成门店二维码\21.立即支付-交易服务支付宝下单-接口实现-调用代理服务下单【海量资源尽在 666java.com】.mp4
- 时长 17分27秒（音频 1047s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们再继续来实现交易服务的支付宝下单接口刚才我们完成了保存订单那么接下来呢我们就准备调用支付渠道代理服务来通过代理服务呢来向支付宝呢下单其实也就是第二步在这里对吧那么在这里我们要调用的话我们还是要去准备一些调用的参数对吧所以这里边呢我准备这么做我写一个私有的方法
[00:29] 对我写一个私有方法然后在这个私有的方法当中我们去调用然后呢他呢然后在这看好啊这个私有方法就是咱们说的调用支付渠道代理服务调用他的服务的一个什么呀支付宝下单接口是吧好那么要传什么参数呢各位你调用
[01:00] 支付渠道代理服务的下单接口首先你要调的话你需要在这个POM文件当中把它的依赖加进去这没错吧你看这依赖我们检查一下啊这个依赖当初我们在API这儿是不是已经加过了吧加过了之后呢这儿就自动它就可以拿到了拿到了之后呢我们还需要在这儿呢把它给注入进去
[01:25] 注入我们说的这个就是这个叫PayChannelAgentService就把它注进去这个一定是远程的调用所以我们要用reference好那也就是说我们准备调用它好那调用的话也就是在这调用对吧在这调用的话这你看是不是就是CreatePayOrderByAliWaf是吧那么它需要两个参数对吧两个参数一个参数指的是
[01:54] 我们系统中所配置的支付渠道就是在这张表对吧一个参数呢是前端请求的业务参数好那么下面各位你想想我们思考一下这个sale方法最终我们会在这掉对吧那你在这掉你参数这个方法给这个阿里配H5穿啥呢分析一下吧这个参数是刚才我们说的是支付渠道参数表当中的数据
[02:24] 那这个我觉得是可以这么做吧你看啊我们首先从这是两部分参数嘛两部分参数嘛一部分呢是在我们说的这个支付渠道配置参数这是一部分吧另外一部分呢就是前端提交的提交的那些什么呀叫订单信息前端提交的订单信息那其实是应该说在control了
[02:53] 对吧ControllerController最初你注意啊这个方法我们写了很多但是你千万流程不要忘记最终用户一扫码确认支付它会请求到这个接口中这个接口呢是不是会调用SubmitOrderByAli这个方法而这个方法是不是会调我们马上说的这个Ali配H5这个方法你说调这么多方法你的目的其实只有一个
[03:23] 就是第一保存订单到我们的数据库第二通过支付渠道代理服务调支付宝的下单接口那我们之所以在这单独写一个方法就是为啥就是大家看起来这个方法是更干净是吧这是第一步这是第二步是吧好所以各位我们分析出了我们说的整个业务流程这里面我们就先要搞清楚这个方法它的参数一个是订单信息一个是支付渠道
[03:53] 配置参数这个订单信息是不是在这这是支付渠道配置参数支付渠道配置参数我们将来从数据库查就行了那订单信息呢订单信息你可以看一下它其实所需要的订单信息它其实需要我们散去平台的订单信息所以啊你既然需要散去平台的订单信息那么很显然我们是需要从哪里啊
[04:21] 也从数据库来查询懂我的意思吧也就是说你发现他要的订单信息就是你散去平台的这个订单号嘛订单信息包括订单金额那你肯定要从你的这个散去平台数据库去查询嘛所以既然这么说的话那我就知道了那这里边其实你需要一个什么一个订单号就搞定那其实这个方法要调阿里配H5这方法当中它一定是有订单号的为啥
[04:52] 你看这里边是不是就有一个trade number吗对不对所以那那我就知道了也就是说哎从这儿我们让它掉拿到你看这是不是就OK了注意这里边你拿的时候不要乱拿啊原来传进来的这个数据你看这一步是不是保存我们说的订单信息对吧这是保存订单吗
[05:20] 那保存订单了之后这个订单号是不是才会生成啊你告诉我是不是所以你要从save当中来取这个订单号这绝对是很保险的一定是有对吧那你拿到了他的你看这个方法他就反回了嘛这个方法咱们是不是就补齐了那下面我们就把这个方法阿里配H5写完了你说我们是不是既保存了订单又干嘛又掉了支付宝的接口下单好
[05:47] 根据刚才我们的思路我们是不是要根据订单号查询因为要查数据库订单信息查数据库订单信息的话这里边我们你不要在这写我建议你单独还是要去抽一个方法去写因为你要知道很多情况下咱们都可能需要查订单信息对不对并且还是需要根据订单号去查是吧所以我其实建议你
[06:15] 就是根据订单号去查询订单信息这个接口我建议你不要写成私有的你呢最好在这个交易服务当中我们去报一个这样的一个根据订单号去查询订单信息的这么一个接口大家理解我的用意了吧好那么我们很显然我们现在
[06:42] 是不是就需要先把这个根据订单号去查询订单信息的这个逻辑给写出来那他呢肯定是要注入我们说的这个pay order Mapper对吧把它注进去那注进去了之后呢这儿呢我们就可以因为订单号它是一个唯一的嘛所以就slack的onenew一个lambda是吧然后呢这儿要查的是pay怎么样pay order对吧然后这里边呢eco
[07:09] 那pay order我们是要根据订单号你不要选错啊应该选trade number对吧这样我们是不是就拿到了这个订单信息拿到这个新订单信息由于他要的是DTO所以你是不是要把它给转一下这样的话我们最终是不是就拿到了订单信息啊这是跑到哪了拿到订单信息在这啊
[07:38] 拿到订单信息之后呢我在这儿是不是就可以来查询呢那查询的时候很简单你就调用我的这个本地的一个方法我就查到了看到了吗这个信息是不是就拿到了拿到这个信息你的目的是干嘛从数据库查询订单然后呢你要干嘛你最终组装啊你组装这个支付渠道代理服务所需要的这个信息嘛什么你要组装呀你组装的话很显然那你就
[08:07] 定义这么一个什么一个对象我开始组装组装的话你组装完了之后你往里一放是不是就行了一会我们再组装那你说支付渠道参数配置这个你是不是也要去从数据库查询啊那这个从数据库查询的话怎么查你支付渠道参数配置你得知道回忆一下当初我们是专门有一个模块做配置嘛在交易服务当中你看这里边是不是有一个叫渠道
[08:35] 这个配置这么一个Service你看你找找里面有没有一个查询那根据应用服务类型这是不是就是查支付渠道参数配置的对不对所以我们就找到了嘛找到了之后呢各位再回到刚才的这个交易服务这里那我就可以去pay channel不是啊pay channel然后哪个呢这个这还得注入一下了但现在还没有对吧
[09:08] 你这个注入的话因为是都是交易服务嘛所以你就不用reference了就是out of where就行了pay channel Service对吧好多呀看花眼了然后呢你在这是不是就可以去用它了你现在做的事是不是要查支付渠道参数了对然后呢你去查询你这里边需要哪些参数呀它好多呀可能这个有些同学都淡忘了
[09:35] 这个是我们一个一个拿出来看看你就知道了一个是应用ID应用ID在哪你这查订单订单当中就有所属的应用ID所以你这里边直接就拿到了对不对拿到了一个APP ID这个是吧还有这个是服务类型吧这个是支付渠道那这个你你是当前是支付宝支付吗对不对所以我们是C扫币
[10:05] 支付宝支付那我们的服务类型编码是C扫B那你就可以去填进去对吧然后你是支付宝支付那你的支付渠道是这个阿里配WAP所以各位你告诉我咱们这几个参数是不是就搞定搞定了你是不是就可以把支付渠道参数我们都拿到了
[10:31] 拿到了之后你还记不记得当初我们这个渠道参数前端传进去的是一个json对不对所以你拿到了这个param这个参数它其实是一个啥是个json串啊有人不相信啊你不相信你可以看一下嘛你看你告诉我这是不是一个json串对不对那你json串我们拿到这个json串那你要最终要干嘛你是不是就可以把这个json串给它转成一个对象
[11:00] 对吧转层的这个对象恰恰就是这个支付渠道代理服务他定义的这个什么参数的这个类型就是这个AliConfigureParam就是他你看当初我们设计接口的时候就是为了今天对吧好那各位我们再看
[11:22] 你呢现在呢你拿到健身串那拿到健身串你可以瞧瞧里边有APP ID呀有私钥对吧那正好是和刚才我们说的这个类型里边都通通字段属性名都对上了所以你就可以转一下哎这就穿进去了对不对这不就是我们说的支付渠道参数但是还报了个异常报了异常这是当初哪个了
[11:52] 这个应该让他抛这个一层这是我们自定义一层不要抛那个好然后我们继续来接着写还抱一层好然后现在我们要做的事一会咱们说然后他就可以得到一个结果这结果我们就让他返回就行了对不对我们把这个给他稍微的处理一下
[12:34] 它会自动有时候你知道吗我们的快捷键用的多了它会自动的把这个异常类都给我改了那可不行对吧那改了之后呢可能我们这个代码就有问题了对吧然后呢继续我们回到这儿你现在应该就不保错了对吧好这个基本的接口这个框框布局就是这样的那现在我们就是组装参数了对吧这个支付渠道参数配置的这些东西我觉得就OK了主要是这个业务参数业务参数有哪些呢
[13:03] 业务参数有哪些你也得还得看看这个支付区的代理服务他需要哪些你整哪些你看他需要哪些你看吧你看他是不是需要这些需要这些的话各位你把它贴到这你先暂时贴到这然后你就知道了他是需要这些数据那你下边你是不是就该往里边帮他塞这些数据了你看有一个是订单号订单号你这是不是从数据库查出来的订单那你就可以拿对吧
[13:32] 这是订单好对吧还有下面一个是订单的金额那订单的金额这一块你需要注意了因为我们数据库存的是分那支付宝是元对不对那怎么办那得转一下了那得转一下用我们的工具类去转一下由这个分转成元对吧由分转成元你数据库的我们数据库存的是分所以你得转一下那转完了之后你看他还报了个异常
[14:03] 这应该是他这个工具类的异常工具类的异常你不要往外抛你呢去单独把它补一下单独补一下如果说存在这个转换失败的情况那就证明数据有问题数据有问题的话那你只能是往外抛出这个异常对吧抛出的这个异常应该是我们看一下这里边有没有相关的异常比如说有这个竞单金额转换异常看一下对我们就让他往外抛对这样弄还有啥呢你看还需要啥
[14:33] 是不是一个subject对吧这些的话我们就好弄了也就是它subject标题是吧然后还有一个是bodybody然后这是订单的描述然后下边还有一个这个不用了你看这是不是我们说的这个支部渠道代理服务人家写死了你不用管还有一个就是过期的时间过期时间的话这个
[15:01] 他是从这里面取过期时间你得看看文档了啊这个不要乱弄因为呃这个文档当中应该写的有过期时间我们瞧一下这个过期时间到底支付宝过期时间你看是他吧订单最晚的付款时间最晚的付款时间取之范围你看比如说90分钟他就是90M对吧我们呢是30分钟30分钟的话那你这就写一个什么呃30M就行了对吧将来这个你也可以给他配起来啊好那你看他需要的这些数据
[15:30] 我问你咱们是不是就整好了整好了之后那你说这个准备的参数都有了调它是不是就OK了对就这么简单啊这就是我们说的你呢先保存订单保存完订单了之后呢就开始调这个代理服务让他去帮我们调支付宝下单刚才的整个代码的逻辑我们是不是就写完了吧好那么写完这个代码的逻辑了之后呢我们就可以去怎么弄啊就可以去
[16:00] 得到最终支付宝订单的响应这个就应该是他的响应了对吧这就是他响应这响应你看他是不是就拿到了最终这个方法是不是就返回给了肯错了最后肯错了是不是就拿到了支付宝下单的一个响应了对一会我们再完善刚才那个肯错了先不要着急这里边他应该我看我的讲义你看这他是不是还设了一个字符编码应该是这个
[16:28] 这个这个字符编码的话嗯是我们支付渠道参数这一块参数这一块的话你我们也设上去吧为啥呢就是这个如果你配的话你就不用设了因为你配什么在里边是不是都拿到了如果你不配就可以设上去我们先上去吧回头我们测试的时候再说到这为止哎我们的啊支付宝下单在交易服务当中所写的一个sale方法就是阿里配H5最终它是不是要掉
[16:57] 这个支付渠道代理服务来完成支付宝的下单这个是不是就写完了其实我们现在还剩什么工作你先搞清楚你就知道我们做的这些事其实一步一步在接近目标我们还剩一个control了维护control了这个方法我们把它维护一下然后呢把它干干嘛把它完善一下这是不是就行了好那到这呢我们先打一个节点就是交易服务支付宝下单调代理服务我们就完成了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中实现一个支付下单服务，通过查询订单、组装支付宝请求参数并调用支付渠道代理服务完成支付。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示桌面环境，任务栏中可见 IntelliJ IDEA 图标，表明即将进入开发环境。
画面 2: 在数据库管理工具中，展示 `shanyipay_transaction` 数据库下的 `pay_channel` 表，其中包含渠道名称和渠道编码（如 ALIPAY_WAP）。
画面 3: 在 IntelliJ IDEA 中，展示 `TransactionServiceImpl.java` 文件，代码中设置支付渠道为 ALIPAY_WAP，并调用 `alipayHS()` 方法。
画面 4: 同画面 3，但光标位于 `payOrderDTO.setChannel("ALIPAY_WAP");` 行，强调设置支付渠道。
画面 5: 在 `TransactionService.java` 文件中，展示 `createStoreCode` 和 `submitOrderById` 方法的定义。
画面 6: 在 `TransactionServiceImpl.java` 文件中，展示 `queryPayOrder` 方法的实现，用于根据订单号查询订单。
画面 7: 在项目结构视图中，展示 `TransactionService` 相关的包和类，包括 `PayController`、`PayChannelAgentService` 等。
画面 8: 在 `TransactionServiceImpl.java` 文件中，展示 `queryPayOrder` 方法的实现，光标位于 `payChannelAgentService.createPayOrderByIdWAP(...)` 行。
画面 9: 在 `TransactionServiceImpl.java` 文件中，展示 `queryPayOrder` 方法的实现，光标位于 `payOrderDTO.getTradeNo()` 行。
画面 10: 在 `PayChannelAgentService.java` 文件中，展示 `createPayOrderByIdWAP` 方法的接口定义，包含 `allConfigParam`、`alipayBean` 参数。
画面 11: 在 `TransactionServiceImpl.java` 文件中，展示 `alipayBean` 对象的初始化和设置方法，如 `setOutTradeNo`、`setTotalAmount`。
画面 12: 在 `TransactionServiceImpl.java` 文件中，展示 `alipayBean` 对象的设置方法，如 `setSubject`、`setBody`、`setProductCode`。
画面 13: 在 `TransactionServiceImpl.java` 文件中，展示 `alipayBean` 对象的设置方法，如 `setTotalAmount`、`setSubject`、`setBody`、`setProductCode`、`setExpireTime`。
画面 14: 在 Word 文档中，展示支付下单流程的技术方案，包括接口定义、参数设置、调用代理服务等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```java
@Override
public PaymentResponseDTO submitOrderById(PayOrderDTO payOrderDTO) throws BusinessException {
    // 订单已分配多个支付渠道
    payOrderDTO.setChannel("ALIPAY_WAP");//支付渠道
    PayOrderDTO save = save(payOrderDTO);
    //调用支付渠道代理服务的支付下单接口
    private PaymentResponseDTO alipayHS() {
        //订单信息，从数据库查询订单
        //支付渠道配置参数，从数据库查询
        //AllConfigParam allConfigParam, AlipayBean alipayBean
        payChannelAgentService.createPayOrderByIdWAP();
        return null;
    }
```

画面 4:
```java
@Override
public PaymentResponseDTO submitOrderById(PayOrderDTO payOrderDTO) throws BusinessException {
    payOrderDTO.setChannel("ALIPAY_WAP");//支付渠道
    PayOrderDTO save = save(payOrderDTO);
    PaymentResponseDTO paymentResponseDTO = alipayHS(save.getTradeNo());
    return paymentResponseDTO;
```

画面 5:
```java
// 有支付平台订单，1、保存到订单平台，2、调用支付渠道代理服务调用支付宝的接口
String createStoreCode(QrCodeDto qrCodeDto) throws BusinessException;
// 支付入口（url），需要将参数（传入的参数转换成json，用base64编码）
@Return
BusinessException
// 有支付平台订单，1、保存到订单平台，2、调用支付渠道代理服务调用支付宝的接口
public PaymentResponseDTO submitOrderById(PayOrderDTO payOrderDTO) throws BusinessException;
```

画面 6:
```java
// 根据订单号查询订单详情
public PayOrderDTO queryPayOrder(String tradeNo) {
    PayOrder payOrder = payOrderConvert.selectOne(new LambdaQueryWrapper<PayOrder>().eq(PayOrder::getTradeNo, tradeNo));
    return payOrderConvert.INSTANCE.entity2Dto(payOrder);
}
```

画面 7:
```java
// 交易下单
private PaymentResponseDTO alipayHS(String tradeNo) {
    //订单信息，从数据库查询订单
    PayOrderDTO payOrderDTO = queryPayOrder(tradeNo);
    //组装alipayBean
    AlipayBean alipayBean = new AlipayBean();
    //支付渠道配置参数，从数据库查询
    //AllConfigParam allConfigParam, AlipayBean alipayBean
    payChannelAgentService.createPayOrderByIdWAP(alipayBean);
    return null;
}
```

画面 8:
```java
// 根据订单号查询订单详情
private PaymentResponseDTO alipayHS(String tradeNo) {
    //订单信息，从数据库查询订单
    PayOrderDTO payOrderDTO = queryPayOrder(tradeNo);
    //组装alipayBean
    AlipayBean alipayBean = new AlipayBean();
    //支付渠道配置参数，从数据库查询
    //AllConfigParam allConfigParam, AlipayBean alipayBean
    payChannelAgentService.createPayOrderByIdWAP(alipayBean);
    return null;
}
```

画面 9:
```java
// 根据订单号查询订单详情
private PaymentResponseDTO alipayHS(String tradeNo) {
    //订单信息，从数据库查询订单
    PayOrderDTO payOrderDTO = queryPayOrder(tradeNo);
    //组装alipayBean
    AlipayBean alipayBean = new AlipayBean();
    //支付渠道配置参数，从数据库查询
    //AllConfigParam allConfigParam, AlipayBean alipayBean
    payChannelAgentService.createPayOrderByIdWAP(alipayBean);
    return null;
}
```

画面 10:
```java
public interface PayChannelAgentService {
    // 调用支付宝的下单接口
    // @param allConfigParam 支付渠道配置参数（配置的支付宝的必要参数）
    // @param alipayBean 业务参数（商户订单号，订单标题，订单描述，）
    // @return 返回PaymentResponseDTO
    public PaymentResponseDTO createPayOrderByIdWAP(AllConfigParam allConfigParam, AlipayBean alipayBean) throws Exception;
}
```

画面 11:
```java
// 调用支付渠道代理服务的支付下单接口
private PaymentResponseDTO alipayHS(String tradeNo) {
    //订单信息，从数据库查询订单
    PayOrderDTO payOrderDTO = queryPayOrder(tradeNo);
    //组装alipayBean
    AlipayBean alipayBean = new AlipayBean();
    //支付渠道配置参数，从数据库查询
    //AllConfigParam allConfigParam, AlipayBean alipayBean
    payChannelAgentService.createPayOrderByIdWAP(alipayBean);
    return null;
}
```

画面 12:
```java
// 调用支付渠道代理服务的支付下单接口
private PaymentResponseDTO alipayHS(String tradeNo) {
    //订单信息，从数据库查询订单
    PayOrderDTO payOrderDTO = queryPayOrder(tradeNo);
    //组装alipayBean
    AlipayBean alipayBean = new AlipayBean();
    //支付渠道配置参数，从数据库查询
    //AllConfigParam allConfigParam, AlipayBean alipayBean
    payChannelAgentService.createPayOrderByIdWAP(alipayBean);
    return null;
}
```

画面 13:
```java
// 调用支付渠道代理服务的支付下单接口
private PaymentResponseDTO alipayHS(String tradeNo) {
    //订单信息，从数据库查询订单
    PayOrderDTO payOrderDTO = queryPayOrder(tradeNo);
    //组装alipayBean
    AlipayBean alipayBean = new AlipayBean();
    //支付渠道配置参数，从数据库查询
    //AllConfigParam allConfigParam, AlipayBean alipayBean
    payChannelAgentService.createPayOrderByIdWAP(alipayBean);
    return null;
}
```

画面 14:
```java
AlipayBean alipayBean = new AlipayBean();
//根据订单号查询订单详情
PayOrderDTO payOrderDTO = queryPayOrder(tradeNo);
alipayBean.setOutTradeNo(tradeNo);//商户的订单号，即商户平台的订单号
alipayBean.setTotalAmount(payOrderDTO.getTotalAmount());//订单金额（元）
alipayBean.setSubject(payOrderDTO.getSubject());//订单标题
alipayBean.setBody(payOrderDTO.getBody());//订单描述
alipayBean.setProduct

