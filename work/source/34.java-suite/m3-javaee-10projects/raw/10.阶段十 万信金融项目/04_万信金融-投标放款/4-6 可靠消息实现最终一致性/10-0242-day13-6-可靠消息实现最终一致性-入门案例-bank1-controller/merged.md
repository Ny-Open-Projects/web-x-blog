# day13-6-可靠消息实现最终一致性-入门案例-bank1-controller

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-6 可靠消息实现最终一致性
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-6 可靠消息实现最终一致性\day13-6-可靠消息实现最终一致性-入门案例-bank1-controller_【海量资源尽在 666java.com】.mp4
- 时长 6分20秒（音频 381s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好前面呢咱们把Bank1这个微服务当中1到7这7个步骤当中这个所涉及到代码的全部变现完毕了最后呢我们需要把Controller这里边的代码给补充完善一下因为呢我们这个转账这个业务呢就是从访问这个Controller开始了对不对它相当于是一个入口咱找一找这个Bank1这个微服务里边的Controller咱当时应该是
[00:31] 对给了一个Controller但是这里边是空时限了对不对然后我们将来是不是要往这里边发请求对不对那这个Controller里边代码完善很简单我们是不是把业务层给他注进来就行了private account info Service哎把它注进来注进来之后干什么呀调用他的方法就行了咱可以大概参考一下这个讲义你看这是不是注入业务层然后调用这个方法然后这里边呢你一会要注意这个
[01:03] 参数在这呢我们就是account info Service点那我们要调用的方法呢就是哪个方法应该是这个方法注意是这个方法update不是这个度开头的是update这个方法然后这个方法大家看到了他是不是要一个参数就是那个我们说的封装那个消息的那个account 庆祭 even 对不对我们在这直接 new
[01:36] 这边大家还有印象吗它是不是有三个参数来我一再找一找这个类一个是这个账号这个账号我们这次应该给的是不是张三的那个账号对不对张三应该是一吧我记得是不是就是这个一然后呢第二个参数呢第二个的这个值就是这个转账金比如我们转账100块钱然后第三个参数呢就是这个什么15号就是当前的时间戳我们在这直接给一下这个一我就暂时给它写死了
[02:06] 因为咱这就是一个demo啊这是张三的这个账号我要从这个账号转钱转多少钱呢转转多少钱转100吧行不行张三没钱是不是我就先转100先试试然后第三个参数呢就是当前时间的这个时间戳当前时间我们通过C term类的这个什么呀convert time millions来得了这个大家应该有印象吧就当前时间这个时间戳嘛就是距离1970年1月1号以来的这个和面值嘛大家有印象吗
[02:38] 然后呢我们这个反应值反复给前面页面的吧我们就就就反复一个转账成功吧这就完事了啊所以说这个control这个代码呢还是比较简单的那这个代码想完之后呢咱先不着急着测试因为咱Bank2那边这个代码是不是还没有开始编写那咱先把Bank1这边这个流程咱结合这个图给它串一下把这个代码结合这个流程串一下那起点呢是不是就
[03:09] 往这发请求对不对你不管是通过浏览器还是通过铺子办反正我们是要往这发请求没错吧然后一发请求是不是该走这块那样吧就是掉右层然后我们是不是传给他一个什么呀这种类型的一个对象这里边告诉他要从账号1余额里边转什么呀100块钱啊然后呢这儿呢是一个时间戳当前是一个时间戳那根据这个这个流程我们是不是该到这儿他调了是不是这个方法对吧你看进来之后他先干什么呀
[03:39] 先发消息了你看这儿是不是咱刚才写的发消息那个代码你看这个流程一样吗是不是先发消息对不对发消息之后呢broker是不是会返回对吧返回的话我们发送方是不是要接收这个消息那这儿接下来这个流程该跳到哪该跳到哪往下走吗可不是啊可不是啊它应该跳到这个监听器这一块这个监听器不就是这个接收broker这个返回的这个消息了就是走第二步嘛是不是
[04:08] 走到这边一旦有消息了他这边就会进行接收那接收的时候接下来该走走啥来该走这个执行本地事务就该调这个了这个方案是由Rocky的MQ自动调的咱们有关那一进来之后呢他是不是接收起解析消息对不对从这里边是不是要拿到咱刚才这个这个参数码然后呢接下来是不是该走这个第三步了执行本地事务你看这是不是这是调要从的这个方法这里边是不是我们说的一个是更新余额吗一个是往那个什么呀
[04:40] 对吧这个表里边是不是开始保存数据我们说了他要么都成功要么都失败如果这个更新语言成功了这个表里边是不是一定会添加一条数据这需要注意他就该执行这个本地是我就这个那然后呢根据结果根据这个执行的结果返回commute或者说什么呀rollback是不是该走到这儿是不是走第四步对不对就返回给这个broke所以你看这个1234我通过这个代码已经给你
[05:08] 这个流程串下来了啊然后这个时候我们要考虑这个特殊情况对不对什么特殊情况这个前面说比如超时那个异常对不对就服务器端他怎么着都等不回来这个什么呀这个这个结果说他就要进行什么呀数回查啊这个时候服务器端呢他会自动啊或者主动去调用这个方法这个方法也不需要咱们去调用啊啊是说k的mq自动去调用哎然后进来之后也是先这个什么呀导到这个消息从这里边是不是取到那个什么呀
[05:38] 那个就是那个时间窗嘛然后呢调用这个数据访问层去从这里边做一次什么呀查询那一旦查出来数据了就证明他那个那个什么呀本地事务其实已经执行成功然后就反而有可能有的那是不是就是走到哪一块啊是不是走到六和什么呀七对不对就反而孔明塔会是什么呀对不对主要这块走的就是五六七这个步骤所以你看目前我们把一到七这七个步骤通过这个代码是不是全给大家串了一下
[06:08] 这是目前吧咱们把这个什么呀Bank1啊就是张三这边了整个就是发送方整个这一块功能呢全部编写完了咱一会呢编写Bank2那边的这个代码

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 RocketMQ 中实现消息的本地事务保障，通过自定义事务监听器来确保消息消费与数据库操作的最终一致性。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 `TransferTransactionListenerImpl` 类中 `checkLocalTransaction` 方法的代码，用于解析消息并根据数据库操作结果返回事务状态（COMMIT 或 ROLLBACK）。
画面2：展示 `TransferTransactionListenerImpl` 类中 `checkLocalTransaction` 方法的代码，注释说明了事务状态的初始设置和业务逻辑。
画面3：展示 `AccountInfoController` 类中 `transfer` 方法的代码，调用 `accountInfoService.updateAccountBalance` 方法进行转账操作。
画面4：展示 `AccountChangeEvent` 类的定义，包含 `accountNo`、`amount` 和 `txId` 三个私有属性。
画面5：展示 `AccountInfoController` 类中 `transfer` 方法的代码，调用 `accountInfoService.updateAccountBalance` 方法并传入 `AccountChangeEvent` 对象。
画面6：展示 `AccountInfoController` 类中 `transfer` 方法的代码，返回字符串“转账成功”。
画面7：展示 `AccountInfoServiceImpl` 类中 `updateAccountBalance` 方法的代码，调用 `bankMessageProducer.sendAccountChangeEvent` 发送消息，并定义 `doUpdateAccountBalance` 方法进行数据库操作。
画面8：展示 `TransferTransactionListenerImpl` 类中 `checkLocalTransaction` 方法的代码，注释说明了事务状态的初始设置和业务逻辑。
画面9：展示 `TransferTransactionListenerImpl` 类中 `executeLocalTransaction` 方法的代码，用于执行本地事务，通过 try-catch 块控制事务提交或回滚。
画面10：展示一个 PPT 页面，包含多个窗口截图，其中一个窗口显示了 `AccountChangeEvent` 类的定义，另一个窗口显示了 `TransferTransactionListenerImpl` 类的代码，还有一个窗口显示了 `SQLyog` 数据库管理工具的界面。
画面11：展示 `TransferTransactionListenerImpl` 类中 `executeLocalTransaction` 方法的代码，根据 `isCommit` 的值返回 `COMMIT` 或 `ROLLBACK`。
画面12：展示 `TransferTransactionListenerImpl` 类中 `checkLocalTransaction` 方法的代码，注释说明了事务状态的初始设置和业务逻辑。
画面13：展示 `SQLyog` 数据库管理工具中 `bank1` 数据库的 `tx_id` 表，显示了 `tx_id` 为 1 的记录。
画面14：展示 `TransferTransactionListenerImpl` 类中 `checkLocalTransaction` 方法的代码，注释说明了事务状态的初始设置和业务逻辑。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Override
public RocketMQLocalTransactionState checkLocalTransaction(Message msg) {
    //接收并解析消息
    final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
    AccountChangeEvent accountChangeEvent =
            jsonObject.parseObject(jsonObject.getString("accountChange"), AccountChangeEvent.class);
    //查询de_duplication表
    int isExistTx = accountInfoDao.isExistTx(accountChangeEvent.getTxId());
    //根据查询结果返回
    if (isExistTx > 0) {
        return RocketMQLocalTransactionState.COMMIT;
    } else {
        return RocketMQLocalTransactionState.ROLLBACK;
    }
}
```

画面2：
```java
@Override
public RocketMQLocalTransactionState checkLocalTransaction(Message msg) {
    //初始化事务状态
    RocketMQLocalTransactionState state;
    //解析消息中的业务数据
    final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
    AccountChangeEvent accountChangeEvent =
            jsonObject.parseObject(jsonObject.getString("accountChange"), AccountChangeEvent.class);
    //查询已执行事务
    int isExistTx = accountInfoDao.isExistTx(accountChangeEvent.getTxNo());
    if (isExistTx > 0) {
        state = RocketMQLocalTransactionState.COMMIT;
    } else {
        state = RocketMQLocalTransactionState.ROLLBACK;
    }
    return state;
}
```

画面3：
```java
@RestController
@S1f4
public class AccountInfoController {
    private AccountInfoService accountInfoService;
    @GetMapping(value = "/transfer")
    public String transfer() {
        accountInfoService.updateAccountBalance();
    }
}
```

画面4：
```java
package cn.itcast.wanxintz.ensuredemo.bank1.model;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class AccountChangeEvent implements Serializable {
    private String accountNo;
    private double amount;
    private long txId;
}
```

画面5：
```java
@RestController
@S1f4
public class AccountInfoController {
    private AccountInfoService accountInfoService;
    @GetMapping(value = "/transfer")
    public String transfer() {
        accountInfoService.updateAccountBalance(new AccountChangeEvent("1", amount: 100, System.currentTimeMillis()));
    }
}
```

画面6：
```java
@RestController
@S1f4
public class AccountInfoController {
    private AccountInfoService accountInfoService;
    @GetMapping(value = "/transfer")
    public String transfer() {
        accountInfoService.updateAccountBalance(new AccountChangeEvent("1", amount: 100, System.currentTimeMillis()));
        return "转账成功";
    }
}
```

画面7：
```java
@Autowired
private BankMessageProducer bankMessageProducer;
@Autowired
private AccountInfoDao accountInfoDao;
@Override
public void updateAccountBalance(AccountChangeEvent accountChange) {
    bankMessageProducer.sendAccountChangeEvent(accountChange);
}
@Override
@Transactional(isolation = Isolation.SERIALIZABLE)
public void doUpdateAccountBalance(AccountChangeEvent accountChange) {
    accountInfoDao.updateAccountBalance(accountChange.getAccountNo(), accountChange.getAmount(), accountChange.getTxId());
    accountInfoDao.addTx(accountChange.getTxId());
}
```

画面8：
```java
@Override
public RocketMQLocalTransactionState checkLocalTransaction(Message msg) {
    //接收并解析消息
    final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
    AccountChangeEvent accountChangeEvent =
            jsonObject.parseObject(jsonObject.getString("accountChange"), AccountChangeEvent.class);
    //查询de_duplication表
    int isExistTx = accountInfoDao.isExistTx(accountChangeEvent.getTxId());
    //根据查询结果返回
    if (isExistTx > 0) {
        return RocketMQLocalTransactionState.COMMIT;
    } else {
        return RocketMQLocalTransactionState.ROLLBACK;
    }
}
```

画面9：
```java
@Override
public RocketMQLocalTransactionState executeLocalTransaction(Message msg, Object arg) {
    //接收并解析消息
    final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
    AccountChangeEvent accountChangeEvent =
            jsonObject.parseObject(jsonObject.getString("accountChange"), AccountChangeEvent.class);
    //执行本地事务
    Boolean isCommit = true;
    try {
        accountInfoService.doUpdateAccountBalance(accountChangeEvent);
    } catch (Exception e) {
        isCommit = false;
    }
    //返回执行结果
    if (isCommit) {
        return RocketMQLocalTransactionState.COMMIT;
    } else {
        return RocketMQLocalTransactionState.ROLLBACK;
    }
}
```

画面10：无代码或配置内容。

画面11：
```java
@Override
public RocketMQLocalTransactionState executeLocalTransaction(Message msg, Object arg) {
    //接收并解析消息
    final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
    AccountChangeEvent accountChangeEvent =
            jsonObject.parseObject(jsonObject.getString("accountChange"), AccountChangeEvent.class);
    //执行本地事务
    Boolean isCommit = true;
    try {
        accountInfoService.doUpdateAccountBalance(accountChangeEvent);
    } catch (Exception e) {
        isCommit = false;
    }
    //返回执行结果
    if (isCommit) {
        return RocketMQLocalTransactionState.COMMIT;
    } else {
        return RocketMQLocalTransactionState.ROLLBACK;
    }
}
```

画面12：
```java
@Override
public RocketMQLocalTransactionState checkLocalTransaction(Message msg) {
    //接收并解析消息
    final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
    AccountChangeEvent accountChangeEvent =
            jsonObject.parseObject(jsonObject.getString("accountChange"), AccountChangeEvent.class);
    //查询de_duplication表
    int isExistTx = accountInfoDao.isExistTx(accountChangeEvent.getTxId());
    //根据查询结果返回
    if (isExistTx > 0) {
        return RocketMQLocalTransactionState.COMMIT;
    } else {
        return RocketMQLocalTransactionState.ROLLBACK;
    }
}
```

画面13：
```sql
SELECT tx_id, account_no, amount, create_time FROM tx_id WHERE tx_id = 1;
```

画面14：
```java
@Override
public RocketMQLocalTransactionState checkLocalTransaction(Message msg) {
    //接收并解析消息
    final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
    AccountChangeEvent accountChangeEvent =
            jsonObject.parseObject(jsonObject.getString("accountChange"), AccountChangeEvent.class);
    //查询de_duplication表
    int isExistTx = accountInfoDao.isExistTx(accountChangeEvent.getTxId());
    //根据查询结果返回
    if (isExistTx > 0) {
        return RocketMQLocalTransactionState

