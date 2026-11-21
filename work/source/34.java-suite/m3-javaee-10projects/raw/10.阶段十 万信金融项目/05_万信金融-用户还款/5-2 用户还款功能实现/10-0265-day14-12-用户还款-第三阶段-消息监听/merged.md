# day14-12-用户还款-第三阶段-消息监听

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-2 用户还款功能实现
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-2 用户还款功能实现\day14-12-用户还款-第三阶段-消息监听_【海量资源尽在 666java.com】.mp4
- 时长 15分56秒（音频 956s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好咱们刚才呢是不是把这个本地数啊这几个数据不操作搞定了那接下来呢接下来该干嘛接下来是不是我们要说一说谁去调用这块代码对不对咱只是把功能实现了还没去调用啊谁去调用呢那这里边呢咱就要回顾一下啊我们说这个呃环环服务是不是首先发消息给Rocket MQM Rocket MQ会是不是会进行回复吗对不对那环环服务这边是不是呃他要接收消息
[00:30] 对不对要接收消息接收到消息之后比如说这儿接收到些接收到消息之后呢他是不是就开始进行这个什么本地事务的一个调用或者说一个执行执行完之后呢是不是还要发送结果给什么呀
[00:45] 那如果这个中间出现了问题了那ROCKET MQ是跑进行这个什么事务回查所以我们接下来是需要编写一个事务消息的一个什么样监听器去接收消息接收到消息之后呢去调用这块代码然后产生结果并发送给ROCKET MQ然后如果没收到结果ROCKET MQ会进行事务回查那这些代码呢我们都需要放到那个Listener那个监听器里边那这块代码的话咱之前是不是也编写过了啊
[01:14] 咱看看讲一讲他说了在message包当中是要新建这么一个类啊看一看你先把这个类给他创建出来message在这儿好类创建好之后呢咱接下来看看呃这里边他是不是需要实现一个接口啊就是这个rocky的mq本地事务的这个监听这个接口啊然后他会自动倒包对不对然后上面呢我们要加一些必要的注解一个是component
[01:55] 还有一个是不是那个事务监听的这个助理那我们要跟这个谁啊跟讲义保持一致这个地方值是不是不能随便乱写吧他应该跟哪保持一致你看他这叫pid conform repayment是不是那咱找找这应该是找哪一块代码发送吧发送发送是跟这保持一致对不对这你不能乱写这个狗肉
[02:27] 然后呢你看这个类爆错了是因为这里边是有两个方法需要我们进行什么呀重新我们先把这两个方法给它生成这两个方法呢大家应该都是有印象的啊第一个方法它就是用来接收到消息之后啊接收到消息后执行什么呀对本地事务那第二个方法就是用来进行什么呀对事务
[02:58] 状态回查的两个方法咱一个一个来吧先说第一个方法执行什么呀本地事务啊这个代码相来说会比较简单一些我们是不是调用业务层咱刚才是不是在业务层写了这个本地事务的这个代码了就这块吧这不是有几个更新一个保存吗是不是调他就行所以说呢我们接下来需要在这里边是要把那个业务层先住进来做一个准备工作
[03:32] private要层应该是repayment Service对吧好先把它注进来那这里边的代码的话我们跟之前一样我们是分成几个步骤呢分成三个步骤第一个步骤呢就是解析消息大家看消息你不用接收了嘛他在这监听器这个监听器会自动接收接收完的消息是不是放到这你需要从这里边去解析数据啊第二步呢就是干什么呀
[04:08] 对执行本地秀第三步干嘛对返回结果嘛是吧那一个一个来吧先说这个解析消息这个代码咱应该写了不止一遍了啊怎么写呢是不是我们还要靠那个jsonobject是不是json我们先调用他的一个方法第二应该是哪个叫passobjectpassobject啊然后呢怎么办
[04:51] 他要是字符串我们这是一个什么呀message对象所以说呢这个呢我们要从message里边取到那个消息给他payload对不对然后呢把它给转换成什么呀对转换成字符串咋转呢这个代码是这么子来写的我再给大家写一遍啊byt先转换成字节数组然后再new成一个什么呀字符串电路构造方法大家看是不是
[05:21] 就这么写了然后他就会得到一个什么jsonobject你接收一下去个分号然后然后接下来我们是不是要从这里边取数据呢咱看咱当时存的时候或者发消息的时候这个都往里边存了什么数据是不是这两个repayment plan和repayment request那你需要谁取谁呗你都需要就都取呗是不是那接下来就是jsonobject
[05:57] 取数据咋取啊是不是掉get方法对不对get stream方法get stream嘛我们先根据这个键啊等到这个值然后呢我们再给它转换成相应的对象啊get stream啊这个值是不是就不能随便乱写呢我们得给这儿保持一致伸过来然后呢我们还需要把它转换成对象这个转换成对象的话应该就是
[06:32] 呃json 调用json object的一个方法叫pass object的吧pass object对然后呢把后边整个这一串呢全给他就行然后他转换的对象是不是就是这个repayment plan我们用他来接收一下啊这个呢要改成大型对吧然后呢接下来这一块我们还需要再取一个数据这个数据跟上面这个代码差不多只是里边的这个值要改改应该就是他了repayment什么呀
[07:15] repayment request是不是改一改呗这也得改这改成大型那大家看一下我们目前是不是应该是把这个消息给解决完了我看这个代码缺不缺东西你看这两行都报错报错是因为这缺参数你要把它转移成什么类型对不对你需要把这个类型告诉他要不然他不知道转移成谁我们这少给个参数点class对这应该是
[07:48] repayment request.us搞定所以这是第一步我们把这个解析消息给搞定那该拿到的这个数据拿到之后我们既然是不是就可以执行本地事务执行本地事务我们说了是不是就调用这个右层的方法就行了就我们刚才编写的叫confirm什么呀repayment所以你看我们在调用这个
[08:12] 发的时候他是不是要两个东西这两个东西是不是咱刚才在第一步取出来的对不对一个就是repaymentplan对吧咱是正好设计好了啊一个是repaymentrequest对这就是执行本地售那执行完之后呢我们说这个发展是不是有一个布尔类型的反应值我们是不是应该要接收一下接收完之后是不是要在这根据这个结果去返回数据呢对不对那我们这就做一个接收吧不玩了一下i s u l t对吧
[08:44] 这是第二步咱要搞定搞定完之后怎么返回结果呢那这个大家应该都知道了啊一副这个什么呀瑞兹奥特就处嘛我就返回出就比较执行成功了吗本金是5那我就要返回那个commute这个值应该怎么写呢应该是肉应该是rocky啊rocky哎大家看到应该就是这个值对不对知道吧
[09:11] 那else不用说了那就是本地事务执行失败了那我就要返回这个什么呀rollback好大家看一看这个第三个步骤返回结果我们是不是也搞定了那这是目前吧咱们把这个什么呀监听器当中的第一个方法啊就是接收到消息后执行本地事务这个代码咱就搞定
[09:37] 那咱们接下来把第二个方法就是进行事物状态的回查这块代码呢咱们也搞定一下这个事物状态回查这块这个大家还有印象没有我们是不是需要回顾一下呢那这个你要回顾的话我们是不是得找到以前的我看看啊以前的我们是在买一张分布式数对不对在这呢我们当时有一个图我们需要回顾一下就这为什么要进行事物回查
[10:08] 因为当发送方执行完本地事务之后产生的结果比如说可名的我就back就第四步他是不要往broker进行发送那么这个过程当中有可能出现各种问题造成了broker呢接收不到这个commuter或者什么呀那他等待一段时间之后就会进行主动的一个什么呀查询对吧我通过查什么数据来判断你前面这个本地事务到底执行成功还是没有成功那判断完之后呢如果成功我就这个干什么呀发送可名的失败我就发送什么呀
[10:38] 说咱既然要做的就是这个事那在咱们这个业务当中咱们是不是在进行这个什么呀还款是不是那在这个业务当中我怎么判断他这个本地事务执行成功还是失败呢那这个其实好办了大家看一下这是不是咱的本地事务他是不是做了三个更新和一个保存嘛那我是不是随便从这几个表里边
[11:06] 查一查某个表的这个状态有没有改比如说还款明信有没有改成已同步对不对这个什么还款计划有没有改成已收或者说这个还款计划对不对有没有改成这个什么已还款我随便挑一个表的状态查一查有没有改成比如说1那我就能判断出来这个本地事务有没有执行成功因为这一堆操作是一个本地事务要么他们都成功要么都什么呀失败所以说呢我们就挑这个吧
[11:33] 我们查查缓缓计划这个表里边这个状态有没有改成什么呀一一旦改成一我们就认为刚才这个本地事务它是什么呀执行成功了负责就是什么呀执行什么那我们这个代码怎么写呢这里边也大概分三个步骤吧第一步仍然是对解析消息第二步呢就是呃什么呀回查状态回查事物状态
[12:06] 那第三步呢就是返回结果呗那第一步解析消息是不是跟这个方案里边代码是一样的我就直接拿过来但是我们这里边呢只需要这个这个值啊缓缓计划因为我们刚才说了我们就判断缓缓计划那个表里边的那个那个什么状态有没有改就行了说这个代码我就直接拿过来然后接下来执行数会查怎么会查我们刚才说呢就是查一查这个
[12:34] repayment plan这个表里边的这个什么呀状态呢这个状态有没有从0改成什么呀1就是它值这个值是不是1那大家看我这儿是不是就是一个很简单的一个查询对不对我们可以根据什么呀对我们可以根据ID因为我们手上是不是拿到了这个这个什么呀一个repayment plan对象嘛它里边肯定有ID我们根据ID查一下查一下这个什么呀这个值看它是不是1就OK了所以接下来呢我们回查事务状态其实说白了就是一个什么呀
[13:03] 数据库查询非常简单啊那我们这里边是不是得住一个住一个Mapper借口啊我们要做数据库查询嘛呃住一下啊应该是Repayment Plan是吧PlanMapper它不叫Repayment Plan咱当时起的名字是叫PlanPlanMapper把它住进来然后呢通过它做一个查询
[13:38] 我们调哪个方法呢查询根据主件应该是slack的白地吧对不对白地根据主件那这个主件的值不就是从这个对象里边我们取一下就行大家看对吗这是不要查出来一个什么呀对还款计划啊我们接下来接收一下我看看我们换一个名字这应该是新查出来的是不是
[14:07] 那我这呢就给他加一个6吧那我接下来要干什么呀这就查完了呀查完之后我接下来是不是要根据什么呀他里边那个状态的值是不是1对不对来返回结果所以说呢我这呢就要进行判断了严谨起见的话我这应该先判断他不等于什么呀然后就是判断他的这个什么呀
[14:40] 状态我们取到它的状态应该是哪个状态呢在哪里我们找找就这个状态那我要判断它的值是不是等于什么呀1对我们当时给它改成1了大家看一下你看这对不对所以我们就判断它是不是1那如果这两个条件都成立了就证明什么呀对这个本金数值成功了我们就应该返回什么呀commute这块代码我就拿过来了
[15:13] 那L字表是本地事务执行失败我就返回什么呀对rollback说这是咱们把执行这个什么呀事务状态回查这块代码写了那目前是这样啊我们目前呢就是把这个什么呀呃事务监听啊整个这个对象呢全部搞定这里边实现两个功能一个是执行本地事务一个是什么呀进行事务状态回查这块代码写完之后呢你看啊咱这里边的啊应该是
[15:42] 咱看哪个图呢看这个图吧相当于是这里边的1234567整个这块代码就全部干什么呀对全部搞定了啊全部打通了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在 RocketMQ 中实现确认还款事务消息监听器，通过本地事务确保消息与数据库操作的最终一致性。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了课程文档“5.3 确认还款事务消息监听类”，并显示了 `ConfirmRepaymentTransactionListener.java` 文件的代码，其中包含 `@Component` 注解和 `executeLocalTransaction` 方法的实现。
画面 2: 展示了 `ConfirmRepaymentTransactionListener.java` 文件的开头部分，包含包声明和导入语句。
画面 3: 展示了 `executeLocalTransaction` 方法的实现，其中包含注释“//收到消息后执行本地事务”和“//进行事务状态回查”。
画面 4: 展示了 `executeLocalTransaction` 方法中解析消息体的代码，使用 `JSON.parseObject` 解析 JSON 字符串。
画面 5: 展示了 `confirmRepayment` 方法的实现，用于发送确认消息。
画面 6: 展示了 `executeLocalTransaction` 方法中解析消息体的代码，使用 `JSON.parseObject` 解析 JSON 字符串。
画面 7: 展示了 `executeLocalTransaction` 方法中调用 `repaymentService.confirmRepayment` 执行本地事务。
画面 8: 展示了 `checkLocalTransaction` 方法中返回 `RocketMQLocalTransactionState.COMMIT` 的代码。
画面 9: 与画面 1 相同，再次展示课程文档“5.3 确认还款事务消息监听类”。
画面 10: 展示了 `RepaymentServiceImpl.java` 文件中 `confirmRepayment` 方法的实现，包含数据库操作。
画面 11: 展示了 `executeLocalTransaction` 方法中解析消息体的代码，使用 `JSON.parseObject` 解析 JSON 字符串。
画面 12: 展示了 `checkLocalTransaction` 方法中调用 `newRepaymentPlanMapper.selectById` 查询数据库。
画面 13: 展示了 `checkLocalTransaction` 方法中判断 `newRepaymentPlan` 是否为 null 并检查状态。
画面 14: 展示了 RocketMQ 事务消息的架构图，说明 Broker 与发送方、接收方的通信机制。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
@Component
@RocketMQTransactionListener(txProducerGroup = "PID_CONFIRM_REPAYMENT")
public class ConfirmRepaymentTransactionListener implements RocketMQLocalTransactionListener {
    @Autowired
    private RepaymentService repaymentService;

    @Override
    public RocketMQLocalTransactionState executeLocalTransaction(Message msg, Object arg) {
        //1.解析消息
        final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
        RepaymentPlan repaymentPlan = JSON.parseObject(jsonObject.getString("repaymentPlan"), RepaymentPlan.class);
        RepaymentRequest repaymentRequest = JSON.parseObject(jsonObject.getString("repaymentRequest"), RepaymentRequest.class);
    }
```

画面 2:
```java
package cn.itcast.wanxingzp.repayment.message;
import org.apache.RocketMQ.spring.core.RocketMQTransactionListener;
import org.springframework.stereotype.Component;
public class ConfirmRepaymentTransactionListener implements RocketMQLocalTransactionListener {
```

画面 3:
```java
@Component
@RocketMQTransactionListener(txProducerGroup = "PID_CONFIRM_REPAYMENT")
public class ConfirmRepaymentTransactionListener implements RocketMQLocalTransactionListener {
    @Override
    //收到消息后执行本地事务
    public RocketMQLocalTransactionState executeLocalTransaction(Message msg, Object arg) {
        //1.解析消息
        //2.执行本地事务
        //3.返回结果
    }
    @Override
    //进行事务状态回查
    public RocketMQLocalTransactionState checkLocalTransaction(Message msg) {
        return null;
    }
```

画面 4:
```java
@Component
@RocketMQTransactionListener(txProducerGroup = "PID_CONFIRM_REPAYMENT")
public class ConfirmRepaymentTransactionListener implements RocketMQLocalTransactionListener {
    @Autowired
    private RepaymentService repaymentService;

    @Override
    //收到消息后执行本地事务
    public RocketMQLocalTransactionState executeLocalTransaction(Message msg, Object arg) {
        //1.解析消息
        final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
        //2.执行本地事务
        //3.返回结果
    }
```

画面 5:
```java
@Resource
private RocketMQTemplate rocketMQTemplate;

public void confirmRepayment(RepaymentPlan repaymentPlan, RepaymentRequest repaymentRequest) {
    JSONObject jsonObject = new JSONObject();
    jsonObject.put("repaymentPlan", repaymentPlan);
    jsonObject.put("repaymentRequest", repaymentRequest);
    Message<String> msg = MessageBuilder.withPayload(jsonObject.toJSONString()).build();
    rocketMQTemplate.sendMessageInTransaction("PID_CONFIRM_REPAYMENT", destination: "TP_CONFIRM_REPAYMENT", msg, null);
}
```

画面 6:
```java
@Component
@RocketMQTransactionListener(txProducerGroup = "PID_CONFIRM_REPAYMENT")
public class ConfirmRepaymentTransactionListener implements RocketMQLocalTransactionListener {
    @Autowired
    private RepaymentService repaymentService;

    @Override
    //收到消息后执行本地事务
    public RocketMQLocalTransactionState executeLocalTransaction(Message msg, Object arg) {
        //1.解析消息
        final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
        RepaymentPlan repaymentPlan = JSON.parseObject(jsonObject.getString("repaymentPlan"), RepaymentPlan.class);
        RepaymentRequest repaymentRequest = JSON.parseObject(jsonObject.getString("repaymentRequest"), RepaymentRequest.class);
        //2.执行本地事务
        //3.返回结果
    }
```

画面 7:
```java
@Component
@RocketMQTransactionListener(txProducerGroup = "PID_CONFIRM_REPAYMENT")
public class ConfirmRepaymentTransactionListener implements RocketMQLocalTransactionListener {
    @Autowired
    private RepaymentService repaymentService;

    @Override
    //收到消息后执行本地事务
    public RocketMQLocalTransactionState executeLocalTransaction(Message msg, Object arg) {
        //1.解析消息
        final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
        RepaymentPlan repaymentPlan = JSON.parseObject(jsonObject.getString("repaymentPlan"), RepaymentPlan.class);
        RepaymentRequest repaymentRequest = JSON.parseObject(jsonObject.getString("repaymentRequest"), RepaymentRequest.class);
        //2.执行本地事务
        repaymentService.confirmRepayment(repaymentPlan, repaymentRequest);
        //3.返回结果
    }
```

画面 8:
```java
@Override
public RocketMQLocalTransactionState checkLocalTransaction(Message msg) {
    //1.解析消息
    JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
    RepaymentPlan repaymentPlan = JSON.parseObject(jsonObject.getString("repaymentPlan"), RepaymentPlan.class);
    //2.查询事务状态
    RepaymentPlan newRepaymentPlan = newRepaymentPlanMapper.selectById(repaymentPlan.getId());
    //3.返回结果
    if (newRepaymentPlan != null && newRepaymentPlan.getRepaymentStatus().equals("1")) {
        return RocketMQLocalTransactionState.COMMIT;
    } else {
        return RocketMQLocalTransactionState.ROLLBACK;
    }
}
```

画面 10:
```java
//1.根据还款计划id查询还款计划
List<ReceivablePlan> receivablePlanList = receivablePlanMapper.selectList(Wrappers.<ReceivablePlan>lambdaQuery().eq(ReceivablePlan::getRepaymentPlanId, repaymentPlan.getId()));
//2.保存数据到receivable_detail表
ReceivableDetail receivableDetail = new ReceivableDetail();
receivableDetail.setReceivableId(receivablePlan.getId());
//应收款标识
receivableDetail.setAmount(receivablePlan.getAmount());
//应收款日期
receivableDetail.setReceivableDate(DateUtil.now());
//保存投资人应收明细
receivableDetailMapper.insert(receivableDetail);
```

画面 11:
```java
@Component
@RocketMQTransactionListener(txProducerGroup = "PID_CONFIRM_REPAYMENT")
public class ConfirmRepaymentTransactionListener implements RocketMQLocalTransactionListener {
    @Autowired
    private RepaymentService repaymentService;

    @Override
    //收到消息后执行本地事务
    public RocketMQLocalTransactionState executeLocalTransaction(Message msg, Object arg) {
        //1.解析消息
        final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
        RepaymentPlan repaymentPlan = JSON.parseObject(jsonObject.getString("repaymentPlan"), RepaymentPlan.class);
        RepaymentRequest repaymentRequest = JSON.parseObject(jsonObject.getString("repaymentRequest"), RepaymentRequest.class);
        //2.执行本地事务
        //3.返回结果
    }
```

画面 12:
```java
//2.查询事务状态
RepaymentPlan newRepaymentPlan = newRepaymentPlanMapper.selectById(repaymentPlan.getId());
//3.返回结果
if (newRepaymentPlan != null && newRepaymentPlan.getRepaymentStatus().equals("1")) {
    return RocketMQLocalTransactionState.COMMIT;
} else {
    return RocketMQLocalTransactionState.ROLLBACK;
}
```

画面

