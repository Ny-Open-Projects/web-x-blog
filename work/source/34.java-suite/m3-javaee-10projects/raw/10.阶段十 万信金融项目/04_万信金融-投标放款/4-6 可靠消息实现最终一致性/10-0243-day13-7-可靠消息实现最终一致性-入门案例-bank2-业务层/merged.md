# day13-7-可靠消息实现最终一致性-入门案例-bank2-业务层

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-6 可靠消息实现最终一致性
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-6 可靠消息实现最终一致性\day13-7-可靠消息实现最终一致性-入门案例-bank2-业务层_【海量资源尽在 666java.com】.mp4
- 时长 12分12秒（音频 732s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 前面呢我们把发送方也就是Bank1这边的代码呢就全部编写完了那接下来我们该编写接收方也就是Bank2这边的代码大家看一下就是哪个呀对Bank2这个地方的代码那这边呢我们仍然是从这个数据房层开始的因为大家知道不管是Bank1还是Bank2它都要操作什么呀
[00:30] 对数据库啊那么Bank2这边的这个数据房子呢它其实跟Bank1的代码是一模一样我们直接拿过来用就行了啊咱先拿过来咱从这个Bank1那边啊直接把那个类先说一个接口是吧咱直接拿过来用就是这个我们Ctrl C然后呢找到这边的包粘过来为什么一模一样你看这个代码呗你就知道它肯定是一模一样的啊
[01:02] 这里边你看对于Bank2来说你看这边数据库它是不是也是要操作这两张表是不是这边要加钱对不对这儿是不是还是要保存或者说查询记录所以你会发现这些功能跟当时操作Bank1的功能是一模一样的所以说我们就直接拿过来用那杨腾说老师那还有一点不一样那李四这边就Bank2这边应该是加钱对不对加钱不更容易吗你这儿只要是正数
[01:34] 那自然就是加钱嘛对不对那个半个一那边咱当时不是乘一负一个的变成负数了说这些东西你都不用改啊通通不用改直接拿用的够你看包括下面这俩是不是咱前面也说过吗对于这个半颗二这边这个表是不是用来实现那个什么密等性了啊一会咱写代码时候再说所以说呢这个DAO这块代码咱就直接拿过来用了啊这样的是没有导过来吗我们导一下试试
[02:11] 这有点卡稍等一下啊好我们看看这里边好像哪有错这里边是不是多引了一些东西啊这引的是半颗一的这个要干掉对不对你看这是我们半咖这边啊数据访问层的代码就搞定了咱是直接就从半颗一那拿过来用了啊因为它本身就是呃数据护操就是一模一样那这个数据防抗层咱搞定之后呢接下来呢咱就开始编写什么样要从来吧咱先来一个什么样接口咱先拗一个接口
[02:48] 那这个名字呢我们跟讲义保持一致啊他还是叫什么呀account infoservice对吧我们先把这个接口给定义出来大家看这里边是不是就一个方法因为我们说了半咖这边作为接收方呢他其实这个要做的事情呢比半咖一那边少得多啊他就是接收消息然后等着收钱对不对就是更新账户什么余额啊那就等着收钱就行说他这里边只需要定义这一个方法就够了啊
[03:22] 这右层的接口然后呢紧接着呢就开始写他的实现类account info Service m p l对吧然后呢让他去实现刚才我们这个接口然后上面基本的注解我们要加一下Service呀这个日志你看你用不用啊用的话你就加不用不加也可以啊这已经报错了然后呢咱们把刚才咱在接口里边的定义的那个方法对吧我们给他生成一下
[04:03] 这是方法99那咱接下来就要编写这个方法里边的代码我们前面说过这个半壳二这边都干啥半壳二这边呢主要是做两个表的操作是不是两个表操我们这呢是暂时不实现的那个接收咱这相当于是实现接收到消息之后的这个本地事物的一个操作就是我们刚才说的嘛操作这两张表对不对那这个表是不是应该是更新就是收钱嘛对不对要加钱这个呢
[04:35] 这个我们要进行查询还有什么呀保存来实现这个什么呀密等性的控制啊所以说咱接下来呢其实在要层主要是操作这两张表那咱就一个一个来吧那既然你要操作这个数据库我们是不是应该把do给注进来先对吧好咱先注入这个doad错了atprivateaccaccountinfo什么呀
[05:11] DAO对就是他那我们要凑这两张表其实很简单呀你看我们首先是不是这个收钱呗对吧收钱的话稍等啊我们直接就调用的就是这个accountinfo DAO它里边是不是有一个方法叫什么呀对updateaccountbalance对吧这里边有两个字第一个字应该这应该就是李斯的账号吧这个这个账号李斯这个账号是不是等着收钱吗
[05:41] 第二个参数就是收多少钱吗应该是100块钱是不是那我们把这两个值给他就行这两个值应该从哪来啊这两个值大家看一下啊我们应该是在这对不对这个地方你看他这两个参数值是不是都是从这个参数里边拿就这个参数那我们从这里边取一下啊和康的亲戚点点给他康的number然后再取一个这个什么呀对
[06:14] 变动的金额那这个仓从哪来大家觉得呢这个仓从来这个仓将来应该是他接受方收到消息之后是不是会然后呢是不是会调用这个方法然后往这传数据对不对这个代码咱一会再写你知道这里边的是我们可以取出来这个什么样账号啊还有这个什么呀变动余额那你看这是我们就完成了一件事第一件事对不对就是收钱呗说白了那然后呢
[06:44] 一段时间说老师这这不就完事了吗我们这个李斯这边就半咖这边就是收钱然后呢接收消息接收到消息之后哎收钱就完事了没啥活要做了对吧没有别的工作要做那这里边呢我们要提醒大家注意一点就还是那个密等性那个事就咱前面的一起分析过就是这个地方咱再回顾一下嗯我们说一说这个密等性的这个问题就是这
[07:17] 应该不是这啊是当时提的这个地方啊呃因为我说了消费方呢他很有可能在生产环境当中是一个什么呀集群对不对那这个集群的话可能集群当中的某个节点他其实消费这个消息已经成功就是他已经接收到这个消息但是这个时候比如说这个网络出问题了对不对引起超时啊对吧呃各种意外啊都会造成这个集群当中的另外一个节点又干什么呀重复消费这个消息
[07:48] 所以说这个地方呢我们要实现这个什么呀密等性那这个密等性怎么实现呢咱们前面也提过一次啊就是说我要通过哪个表对接收方通过这个表主要是用来解决什么问题呢密等性的问题那通过这个表咱解决这个密等性的问题其实跟当时班克一那边这个道理啊应该是差不多的应该差不多什么意思呢大家看一下啊他这边也会这么设计就是说
[08:17] 这样的将来会加一个本地事我一会回家本地事务当中有两个操作一个操作就是什么收钱对不对就是增加余额还有一个操作就是往往这个就调这个方法这个大家应该有印象调这个方法干啥往这个表里边在里面保存一条数据这里边是不是应该有一个值这个值也是从参数里边取出来大家看上这跟半个一非常相似的对不对
[08:52] 半个一当时是不是也是一个更新余额然后往这个表里边是保存一个什么呀事务执行的一个日志嘛对不对那这两个操作应该是是一个本地事务对不对那跟半个一一样我们这要加上这个什么呀translation这个注解同时我们给它设置一个比较高的一个什么呀隔离级别啊这呢我就从讲义里面直接拿过来了我们应该是在在哪应该是在这个地方
[09:22] 你看我们讲义里边是不是加了就有这个注解那既然这两个操作我们当成一个本地事物了也就是说呢他俩要么都成功要么都失败是这意思吧那也意味着如果这个他收到钱了那这个表里边一定会干什么呀添加一条数据对吧那如果他没有收到钱那么这个表里边一定不会干什么呀添加一条记录是这意思吧那我将来能不能这么判断啊我
[09:55] 看一看啊或者查一查这个表就这个表如果有数据了能查出来数据了就证明这个操作是成功的对吗没问题吧因为我们说了嘛他俩是一个本地事物嘛要么都成功要么都失败嘛那这个时候呢我就可以利用这一点来解决什么呀对密等性的问题啊打解决啊我为了避免重复操作嘛我可以先干什么呀对先做一次查询然后进行判断
[10:26] 点我调哪个方法去查询这个方法还有印象吧是不是对然后呢我们得到这个number我先查一次得到这个值这个值不就是说这个有没有查出来这个数据吗我们接收一下我先查查完之后呢我做判断那大家想一下你看我准备把这两行代码放到这你觉得这个if条件应该怎么写那应该是什么时候才执行这两个操作
[11:02] 那肯定是等于零嘛等于零是啥意思等于零就是说这个记录没查出来我们刚才说了嘛如果这个表里边没数据就证明是不是这个收钱这个动作没完成嘛如果这里边有数据就证明这个动作已经完成那为了避免这个集群当中各个节点重复操作也就是说为了控制或者实现这个密等性你看我们是不是应该先查一下对吧你集群当中任何一个节点走这个代码的时候都先查一下对不对我先看看
[11:33] 这表里边有明数据一旦有数据了查出来了那你说这个代码还走不走有数据就证明之前肯定某个节点已经把这个钱已经收了那这个代码自然就不再走不再充公证明那一旦一查发现它的值是零证明这表里边有数据没有对证明本次没有查出来数据没有查出来数据就证明这个收钱这个动作是不是还没有完成那接下来不正好这个条件也满足然后接下来是不是执行这两个代码就行应该是什么意思吧所以说在半咖二这边呢
[12:02] 我们主要是通过这个表来实现什么呀对实现密等性的啊这是需要大家注意的

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 RocketMQ 消息系统中实现消息的可靠消费，通过本地事务控制确保消息消费成功后，本地业务操作一定执行成功，防止消息重复消费。

2) 按时间顺序列出每张画面的要点：
画面1：展示 TransferTransactionListenerImpl 类中的 checkLocalTransaction 方法，用于检查本地事务状态，根据是否存在事务记录返回 COMMIT 或 ROLLBACK。
画面2：展示 AccountInfoDao 接口中的 SQL 语句，用于查询账户信息和更新账户余额。
画面3：展示 AccountInfoDao 接口中的 SQL 语句，用于查询事务记录是否存在，并插入事务记录。
画面4：展示 AccountInfoDao 接口中的 SQL 语句，用于查询账户信息。
画面5：展示 AccountInfoService 类中 updateAccountBalance 方法的实现，用于更新账户余额。
画面6：展示 AccountInfoServiceImpl 类中的 updateAccountBalance 方法，包含事务注解和业务逻辑。
画面7：展示 AccountInfoServiceImpl 类中的 updateAccountBalance 方法，包含事务注解和业务逻辑。
画面8：展示 AccountInfoService 接口和 AccountInfoServiceImpl 类的定义。
画面9：展示 PPT 页面，内容为 RocketMQ 可靠消息的介绍，包括消息发送方执行本地事务与发送消息的原子性问题。
画面10：展示 AccountInfoServiceImpl 类中的 updateAccountBalance 方法，包含事务注解和业务逻辑。
画面11：展示 PPT 页面，内容为实现转发消息的步骤。
画面12：展示 AccountInfoServiceImpl 类中的 updateAccountBalance 方法，包含事务注解和业务逻辑。
画面13：展示 SQLyog 数据库管理工具界面，显示数据库连接和表结构。
画面14：展示 SQLyog 数据库管理工具界面，显示数据库连接和表结构。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Override
public RocketMQLocalTransactionState checkLocalTransaction(Message msg) {
    final JSONObject jsonObject = JSON.parseObject(new String((byte[]) msg.getPayload()));
    AccountChangeEvent accountChangeEvent =
            jsonObject.parseObject(jsonObject.getString(key: "accountChange"), AccountChangeEvent.class);
    int isExistTx = accountInfoDao.isExistTx(accountChangeEvent.getTxNo());
    // 根据查询结果返回
    if(isExistTx != 0) {
        return RocketMQLocalTransactionState.COMMIT;
    } else {
        return RocketMQLocalTransactionState.ROLLBACK;
    }
}
```

画面2：
```java
// 修改其账号的余额
@Update("update account_info set account_balance=account_balance+#{amount} where account_no=#{accountNo}")
int updatedAccountBalance(@Param("accountNo") String accountNo, @Param("amount") Double amount);

// 查询账户信息
@Select("select * from account_info where where account_no=#{accountNo}")
AccountInfo findByIdAccountNo(@Param("accountNo") String accountNo);
```

画面3：
```java
// 查询事务记录是否存在
@Select("select count(1) from de_duplication where tx_no = #{txNo}")
int isExistTx(long txNo);

// 保存事务执行记录
@Insert("insert into de_duplication values(#{txNo},now());")
int addTx(long txNo);
```

画面6：
```java
@Service
@Slf4j
public class AccountInfoServiceImpl implements AccountInfoService {

    @Autowired
    private AccountInfoDao accountInfoDao;

    @Override
    @Transactional(isolation = Isolation.SERIALIZABLE)
    public void updateAccountBalance(AccountChangeEvent accountChange) {
        int isExistTx = accountInfoDao.isExistTx(accountChange.getTxNo());
        if(isExistTx == 0) {
            accountInfoDao.updateAccountBalance(accountChange.getAccountNo(), accountChange.getAmount());
            accountInfoDao.addTx(accountChange.getTxNo());
        }
    }
}
```

画面7：
```java
import cn.itcast.wanxin.ensure.demo.bank2.model.AccountChangeEvent;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.transaction.annotation.Isolation;
import org.springframework.stereotype.Service;
@Service
@Slf4j
public class AccountInfoServiceImpl implements AccountInfoService {

    @Autowired
    private AccountInfoDao accountInfoDao;

    @Override
    @Transactional(isolation = Isolation.SERIALIZABLE)
    public void updateAccountBalance(AccountChangeEvent accountChange) {
        accountInfoDao.updateAccountBalance(accountChange.getAccountNo(), accountChange.getAmount());
        accountInfoDao.addTx(accountChange.getTxNo());
    }
}
```

画面8：
```java
public interface AccountInfoService {
    /**
     * 更新账户余额
     * @param accountChange
     */
    void updateAccountBalance(AccountChangeEvent accountChange);
}

@Service
@Slf4j
public class AccountInfoServiceImpl implements AccountInfoService {

    @Autowired
    private AccountInfoDao accountInfoDao;

    @Override
    @Transactional(isolation = Isolation.SERIALIZABLE)
    public void updateAccountBalance(AccountChangeEvent accountChange) {
        int isExistTx = accountInfoDao.isExistTx(accountChange.getTxNo());
        if(isExistTx == 0) {
            accountInfoDao.updateAccountBalance(accountChange.getAccountNo(), accountChange.getAmount());
            accountInfoDao.addTx(accountChange.getTxNo());
        }
    }
}
```

画面9：
```text
5.2 RocketMQ可靠消息

RocketMQ 是一个来自阿里巴巴的分布式消息中间件，于 2012 年开源，并在 2017 年正式成为 Apache 顶级项目。Apache RocketMQ 4.3 之后的版本支持事务消息，为分布式事务实现提供了便利支持。因此，我们通过 RocketMQ 就可以解决前面的问题。

1.消息发送方执行本地事务与发送消息的原子性问题，也就是说如何保证本地事务执行成功，消息一定发送成功
```

画面10：
```java
public void updateAccountBalance(AccountChangeEvent accountChange) {
    accountInfoDao.updateAccountBalance(accountChange.getAccountNo(), accountChange.getAmount());
    accountInfoDao.addTx(accountChange.getTxNo());
}
```

画面11：
```text
3. 实现转发消息
```

画面12：
```java
@Override
@Transactional(isolation = Isolation.SERIALIZABLE)
public void updateAccountBalance(AccountChangeEvent accountChange) {
    accountInfoDao.updateAccountBalance(accountChange.getAccountNo(), accountChange.getAmount());
    accountInfoDao.addTx(accountChange.getTxNo());
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面9：
标题：5.2 RocketMQ可靠消息
内容：
- RocketMQ 是一个来自阿里巴巴的分布式消息中间件，于 2012 年开源，并在 2017 年正式成为 Apache 顶级项目。Apache RocketMQ 4.3 之后的版本支持事务消息，为分布式事务实现提供了便利支持。因此，我们通过 RocketMQ 就可以解决前面的问题。
- 1.消息发送方执行本地事务与发送消息的原子性问题，也就是说如何保证本地事务执行成功，消息一定发送成功

画面11：
标题：3. 实现转发消息

5) 不要评价画面美观，不要输出与课程无关的内容。

