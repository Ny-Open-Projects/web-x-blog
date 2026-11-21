# day13-5-可靠消息实现最终一致性-入门案例-bank1-回查事务

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-6 可靠消息实现最终一致性
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-6 可靠消息实现最终一致性\day13-5-可靠消息实现最终一致性-入门案例-bank1-回查事务_【海量资源尽在 666java.com】.mp4
- 时长 9分7秒（音频 547s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好刚才呢我们把监听器这个类当中的第一个方法给实现了这个方法主要是用来执行本地事务那对应的就是图当中的234这三个步骤我们相当于是不是把它给打通了就是连起来了对不对那咱接下来呢实现这个类当中的另外一个方法就这个方法这个方法主要是干嘛的呀对这个方法呢主要是实现事务回查的咱把这个注释先给他拿过来实现事务回查
[00:34] 那这个事物回查呢我们是不是在一开始的时候给大家讲过吧你还有印象吗这个我们为什么要进行事物回查来咱接下来大概回顾一下啊回顾一下这个事物回查我们当时给大家举了一个很具体的一个例子什么例子呢就是说咱看看讲义吧先讲义里边当时给大家举了一个很具体的一个例子在哪呢在那两个问题是不是就这这个地方
[01:14] 就是我们当时取得一个超时的这个异常这种情况吧是不是车是异常数据库回滚但是这个时候消息已经什么呀正常发送然后同样会导致这个什么呀不一致所以我们要进行事务回查了你看在这在哪在这个地方第五步他说了吗如果发送方在本地在执行本地事务的过程当中出现服务挂掉了或者网络闪断或者超时嘛车是异常对吧那broker这边就无法得到这个什么呀commuter road bike就是啥结果他都得不到
[01:48] 那他这时候就比较着急啊对不对你到底刚才这个本地事务执行成功还是没成功啊对我都等超时了对不对也也不知道咋回事那干脆我也不等了我也我要主动的去干什么最近有挥查事务状态其实说白了就是Rookie的M票会自动的调用咱这个方法来进行事务的一个挥查对不对我要确定啊你这个到底刚才执行成功没有是不是你执行成功给我个commute你执行失败给我个rollback对不对所以这是这个为什么我们要进行这个事务挥查
[02:17] 那这个咱清晨之后呢咱接下来就要想想我怎么去实现这个收回啥呢对吧对应这个图里边对吧我这个broker我这个服务端我咋知道你刚才这个本地收到的执行成功还是没执行成功呢是不是那这个时候呢我们就要用到这个表就这个表这个表就派上用场了啊到现在才派上用场对吧这个表有啥用呢哎大家看这我们之前在业务层的这个地方这个方案里边大家看一下
[02:50] 我们在这个方案里边是不是做了两个数据库操作吗一个是更新这个什么样余额对不对一个就是网什么呀这个表里边是不是有保存的一条数据吗这个大家有印象吗而且我们说了这两个操作是不是一个本地事务而且我们还采用了最高的这个隔离级是不是那大家想一下啊你看我这么说对不对这个操作成功了它里边就一定会保存一条数据对吗那如果它失败了
[03:23] 它里边也不会保存数据因为它是本地事物说白了就是这两个操作要么都成功要么都失败那因此大家注意听你看我这样子做一个判断对不对那我可以从这个表里边做一次查询如果查出来数据了就证明这个操作成功了哎你看我这么说你能理解吗你看我们刚才说了吗它成功了它就会往里边保存数据了那我将来查一下能查出来数据不就反过来证明
[03:53] 这一步操作已经执行了什么呀成功了哎这就是事务会查就是这么查你明白什么意思吗所以其实很简单啊我就是根据一个事务号就这个值我从这个表里边查一下查到数据了证明他这一步执行成功了因为如果没查到数据嘛如果没查到数据证明这一步也没执行成功啊你们要注意他俩是一个本质数就要么都成功要么都什么呀都失败那这个方法呢前面咱们在这个
[04:24] DU里边也让大家看到了你看这是不是做了一个查询吗我们查的是这个counter嘛我当时说了其实就是判断这个记录存在不存在如果存在它肯定是带0的嘛是不是如果不存在那就是0嘛所以怎么进行事务啥就这么回答很简单啊那咱接下来呢就把这个代码呢给编写一下我们回到这个监听器类当中找到这个位置我们把这个代码编写一下那首先的话我们也是要
[04:55] 要接收这个消息就是这一步呢跟这儿是一样我直接就拿过来了就你要先接收并解析消息拿到是不是这个account的亲戚移问的这个对象为什么要拿这个对象因为这个对象里边是不是保存了哪个值对这个TX number我们是要拿着这个值去这个表里边进行什么呀查询的对不对没这个值你怎么查是不是没法查所以我们这样的也是先接收并解析消息然后呢一会儿呢就可以从这边
[05:26] 去到那个tx number然后进行这个事务会查了那拿到这个值之后呢我们接下来直接就是就是什么呀对查询哪个表呢我们就是查询这个表咋查呢是不是这个已经封装好了对不对那我们直接就是哎我们得注意一下因为我们要调那个dao吗这个接口private他是叫啥名啊他是叫account
[06:06] info DAO 对吧好 诸如进来之后呢这个查询很简单就是account info DAO哎 我们调一下那个查询那个方法应该是这个是不是exactx那这个值呢是不是从这里边来去点应该是get tx number这就完成查询了呀
[06:37] 那他反过来是不是一个应他类型的一个数据对不对我们接收一下呗啊1x ist tx然后呢对这是第二第三步这都很自然的事吗第三步就是根据查询结果干什么呀返回之就想那你就判断呗这个多简单哎你就判断一下
[07:11] 这个值是不是带零嘛对不对咱刚才说了嘛如果他能查到数据他一定带零嘛那否则的话就证明没有查到数据带零就表示那个本金是不是已经执行成功了所以说我们应该返回什么呀commute还是这一块我就直接拿过来跟这是一样对不对那这一块啊这个代码等我写完了那这个方案这一块是实现啥功能的呀其实就是这里边的567就是当
[07:47] 发送方在执行本地事务的时候呢由于主动原因对不对这个服务器端呢他不能收到这个什么呀Commuter呀Roebuck呀对吧这个结果那么他们就会去就是Rocky的MQ啊他就会主动调用这个方法来进行事务会查然后具体来说第一步就是先接收并这个什么解析消息最终是主要拿这个值呢对不对然后呢是不是就走到第六个了然后是不是就开始查这个数据库吗我们说的话就是查这个表对不对
[08:17] 查查这个数据能不能查到能查到就证明其实呢这个什么呀这个本金数已经执行成功了但是由于种种原因呢他反而的这个commit还要换roback这个结果我们是不是这边没收到是不是啊那那接下来就是判断结果吧大零那就是成功了我就反而commute那否则就是刚才执行失败了我就反回什么呀roback所以说呢这个售回啥呢其实你其实就是这个什么呀broker他主动做了一个什么呀
[08:47] 结果的一个确认我等不到结果了嘛我就主动的去查一查怎么查刚才说了就是查这个表这个表只要有数据就证明本地事务成功否则就证明本地事务执行失败了这是咱们把这个什么呀监听器类当中事务回答这一块功能也搞定

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示 RocketMQ 事务消息的实现原理与代码结构，包括本地事务执行、消息确认、以及事务状态回查的逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 代码文件：`TransferTransactionListenerImpl.java`
- 方法：`executeLocalTransaction(Message msg, Object arg)`
- 代码逻辑：解析消息体中的 JSON，创建 `AccountChangeEvent` 对象，调用 `accountInfoService` 的 `doUpdateAccountBalance` 方法执行本地事务。
- 代码片段：
```java
@Override
public RocketMQLocalTransactionState executeLocalTransaction(Message msg, Object arg) {
    //1.解析并解析消息
    final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
    AccountChangeEvent accountChangeEvent =
            jsonObject.parseObject(jsonObject.getString("key": "accountChange"), AccountChangeEvent.class);
    //2.执行本地事务
    boolean inCommit = true;
    try {
        accountInfoService.doUpdateAccountBalance(accountChangeEvent);
    } catch (Exception e) {
        inCommit = false;
    }
    //3.返回执行结果
    if(inCommit) {
        return RocketMQLocalTransactionState.COMMIT;
    } else {
        return RocketMQLocalTransactionState.ROLLBACK;
    }
}
```

画面2：
- 代码文件：`TransferTransactionListenerImpl.java`
- 方法：`checkLocalTransaction(Message msg)`
- 代码逻辑：解析消息体中的 JSON，创建 `AccountChangeEvent` 对象，调用 `accountInfoDao` 的 `isExistTx` 方法检查事务是否存在。
- 代码片段：
```java
@Override
public RocketMQLocalTransactionState checkLocalTransaction(Message msg) {
    //1.接收并解析消息
    final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
    AccountChangeEvent accountChangeEvent =
            jsonObject.parseObject(jsonObject.getString("key": "accountChange"), AccountChangeEvent.class);
    //2.查询事务
    accountInfoDao.isExistTx(accountChangeEvent);
}
```

画面3：
- PPT 标题：5.3.2.4 Maven 工程
- 内容：在 IDEA 中导入 Maven 工程 `wanxin-ensure-message-demo`，其中 `ensure-message-demo-bank1` 负责操作张三账户，连接数据库 bank1；`ensure-message-demo-bank2` 负责操作李四账户，连接数据库 bank2。
- 项目结构图：显示了 `pom.xml` 文件和两个子模块 `ensure-message-demo-bank1`、`ensure-message-demo-bank2`。

画面4：
- PPT 标题：5.2 RocketMQ 可靠消息
- 内容：
  1. 数据库操作
  2. 发送消息
  3. 消息接收方与本地事务的原子性问题
  4. 消息重试机制
  5. 事务消息的必要性

画面5：
- 代码文件：`TransferTransactionListenerImpl.java`
- 方法：`checkLocalTransaction(Message msg)`
- 代码逻辑：解析消息体中的 JSON，创建 `AccountChangeEvent` 对象，调用 `accountInfoDao` 的 `isExistTx` 方法检查事务是否存在。
- 代码片段：
```java
@Override
public RocketMQLocalTransactionState checkLocalTransaction(Message msg) {
    //1.接收并解析消息
    final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
    AccountChangeEvent accountChangeEvent =
            jsonObject.parseObject(jsonObject.getString("key": "accountChange"), AccountChangeEvent.class);
    //2.查询事务
    accountInfoDao.isExistTx(accountChangeEvent);
}
```

画面6：
- 代码文件：`AccountInfoServiceImpl.java`
- 方法：`doUpdateAccountBalance(AccountChangeEvent accountChange)`
- 代码逻辑：调用 `accountInfoDao` 的 `updateAccountBalance` 方法更新账户余额。
- 代码片段：
```java
@Override
@Transactional(isolation = Isolation.SERIALIZABLE)
public void doUpdateAccountBalance(AccountChangeEvent accountChange) {
    accountInfoDao.updateAccountBalance(accountChange.getAccountNo(), accountChange.getAmount());
    accountInfoDao.addTx(accountChange.getAccountNo(), accountChange.getAmount());
}
```

画面7：
- 代码文件：`AccountInfoServiceImpl.java`
- 方法：`doUpdateAccountBalance(AccountChangeEvent accountChange)`
- 代码逻辑：调用 `accountInfoDao` 的 `updateAccountBalance` 方法更新账户余额。
- 代码片段：
```java
@Override
@Transactional(isolation = Isolation.SERIALIZABLE)
public void doUpdateAccountBalance(AccountChangeEvent accountChange) {
    accountInfoDao.updateAccountBalance(accountChange.getAccountNo(), accountChange.getAmount());
    accountInfoDao.addTx(accountChange.getAccountNo(), accountChange.getAmount());
}
```

画面8：
- 代码文件：`TransferTransactionListenerImpl.java`
- 方法：`executeLocalTransaction(Message msg, Object arg)`
- 代码逻辑：解析消息体中的 JSON，创建 `AccountChangeEvent` 对象，调用 `accountInfoService` 的 `doUpdateAccountBalance` 方法执行本地事务。
- 代码片段：
```java
@Override
public RocketMQLocalTransactionState executeLocalTransaction(Message msg, Object arg) {
    //1.解析并解析消息
    final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
    AccountChangeEvent accountChangeEvent =
            jsonObject.parseObject(jsonObject.getString("key": "accountChange"), AccountChangeEvent.class);
    //2.执行本地事务
    boolean inCommit = true;
    try {
        accountInfoService.doUpdateAccountBalance(accountChangeEvent);
    } catch (Exception e) {
        inCommit = false;
    }
    //3.返回执行结果
    if(inCommit) {
        return RocketMQLocalTransactionState.COMMIT;
    } else {
        return RocketMQLocalTransactionState.ROLLBACK;
    }
}
```

画面9：
- 代码文件：`TransferTransactionListenerImpl.java`
- 方法：`checkLocalTransaction(Message msg)`
- 代码逻辑：解析消息体中的 JSON，创建 `AccountChangeEvent` 对象，调用 `accountInfoDao` 的 `isExistTx` 方法检查事务是否存在。
- 代码片段：
```java
@Override
public RocketMQLocalTransactionState checkLocalTransaction(Message msg) {
    //1.接收并解析消息
    final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
    AccountChangeEvent accountChangeEvent =
            jsonObject.parseObject(jsonObject.getString("key": "accountChange"), AccountChangeEvent.class);
    //2.查询事务
    accountInfoDao.isExistTx(accountChangeEvent);
}
```

画面10：
- 代码文件：`TransferTransactionListenerImpl.java`
- 方法：`executeLocalTransaction(Message msg, Object arg)`
- 代码逻辑：解析消息体中的 JSON，创建 `AccountChangeEvent` 对象，调用 `accountInfoService` 的 `doUpdateAccountBalance` 方法执行本地事务。
- 代码片段：
```java
@Override
public RocketMQLocalTransactionState executeLocalTransaction(Message msg, Object arg) {
    //1.解析并解析消息
    final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
    AccountChangeEvent accountChangeEvent =
            jsonObject.parseObject(jsonObject.getString("key": "accountChange"), AccountChangeEvent.class);
    //2.执行本地事务
    boolean inCommit = true;
    try {
        accountInfoService.doUpdateAccountBalance(accountChangeEvent);
    } catch (Exception e) {
        inCommit = false;
    }
    //3.返回执行结果
    if(inCommit) {
        return RocketMQLocalTransactionState.COMMIT;
    } else {
        return RocketMQLocalTransactionState.ROLLBACK;
    }
}
```

画面11：
- 代码文件：`TransferTransactionListenerImpl.java`
- 方法：`checkLocalTransaction(Message msg)`
- 代码逻辑：解析消息体中的 JSON，创建 `AccountChangeEvent` 对象，调用 `accountInfoDao` 的 `isExistTx` 方法检查事务是否存在。
- 代码片段：
```java
@Override
public RocketMQLocalTransactionState checkLocalTransaction(Message msg) {
    //1.接收并解析消息
    final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
    AccountChangeEvent accountChangeEvent =
            jsonObject.parseObject(jsonObject.getString("key": "accountChange"), AccountChangeEvent.class);
    //2.查询事务
    accountInfoDao.isExistTx(accountChangeEvent);
}
```

画面12：
- 架构图：RocketMQ 事务消息流程图
- 结构：
  - 本地事务（A服务数据库） → 发送方（A服务） → 服务端（Broker） → 接收方（B服务）
  - 发送方 → 服务端：1. 发送半消息；2. 半消息发送成功
  - 服务端 → 发送方：4. Commit 或者 Rollback
  - 发送方 → 服务端：5. 未收到4的确认时，回查事务状态
  - 服务端 → 发送方：6. 检查本地事务的状态
  - 服务端 → 接收方：7. 根据事务的状态 Commit/Rollback

画面13：
- 数据库界面：`bank1` 数据库
- 表：`t_account`
- 数据：`account_no` 为 `00011`，`account_balance` 为 `10000`。
- 操作：执行 SQL `UPDATE t_account SET account_balance = account

