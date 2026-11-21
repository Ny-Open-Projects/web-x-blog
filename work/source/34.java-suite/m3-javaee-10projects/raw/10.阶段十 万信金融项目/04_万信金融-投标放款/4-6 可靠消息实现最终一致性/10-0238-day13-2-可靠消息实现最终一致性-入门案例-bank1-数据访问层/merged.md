# day13-2-可靠消息实现最终一致性-入门案例-bank1-数据访问层

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-6 可靠消息实现最终一致性
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-6 可靠消息实现最终一致性\day13-2-可靠消息实现最终一致性-入门案例-bank1-数据访问层_【海量资源尽在 666java.com】.mp4
- 时长 16分24秒（音频 985s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好前面呢我们已经把开发环境呢全部打好接下来呢咱就实现功能那一共呢是不是有两个微服务嘛对不对一个Bank1一个什么呀Bank2那咱按照顺序一个一个来吧先搞定Bank1那么Bank1呢在咱们这个案例当中呢它是属于消息的发送方对不对也就是张三这边他是要干什么呀对发消息然后他还要干什么呀对扣件
[00:28] 因为它是给给利斯转账嘛对不对所以我们先搞定这个半个一那咱看一下讲义那我们在实现半个一这边的功能的时候呢我们首先要定义一个类来封装这个转账消息这块呢大家要注意看这个图吧看这个图也行或者看咱上面这个图也行我们说了这个发送方是不是首先要发送这个消息对不对这里边会有一些数据这个数据呢我们会定义一个类来进行封装
[00:57] 那么这个类呢实际上我们在刚才导入这个工程的时候里边已经有了但是咱需要熟悉熟悉因为一会要用它这个类的名字呢叫account-changed-even大家看一下这是不是都是Lambook的一些什么呀注解对不对我就不再说了那这边主要有三个属性大家看一下第一个就是账号对吧你要修改哪个账号对不对那第二个属性就是余额
[01:24] 你是要增加钱还是减少钱对吧这个增加多少减少多少这是这个变动的金额第三个属性呢是一个事物号啊这个事物号呢我们是用当前的这个时间的这个时间穿作为纸来使用那这个东西有啥用呢先简单说一下啊这个数字数号呢一个他可以将来实现这个这个帮助实现这个事物的回查还有一个呢就是可以帮助我们去控制这个密等线
[01:55] 大概的这是它的作用吧咱一会儿用到的时候再说那这呢就是大家首先得知道我们一会儿发送消息的时候啊这些数据会封装到这个类当中你看咱这个工程当中呢其实已经有了这是直接提供给大家这是需要大家注意的然后咱接下来呢编码呢具体就是从数据访问层开始这我觉得我就不用说了吧大家知道我们这个转账吧一定涉及到数据库操作是不是所以说我们要先编写
[02:24] 数据访问层的代码那这一块呢咱主要使用的是mybattis没有使用mybattis plus这个一定要注意所以我们需要自己定义一个接口叫accountinfo.dao然后在这里边呢你一定要注意一共要实现四个功能四个功能都哪四个功能呢咱一块说一说首先呢咱看看啊四个功能大家看
[02:54] 那我们目前需要操作是不是就这俩表看一下啊一个account info这里边是不是就有账号以及账号这里边什么账号密码还有什么余额吧对不对啊还有一个表是不是就这个表这个表我们前面是不是也介绍过了吗他可以利用他来进行事务盔查来控制这个什么呀密等性那这四个功能分别是啥呢第一个功能是往这个表里边干什么呀这个来更新数据的就更新这个余额这个大家应该理解是咋个事
[03:25] 他有可能是增加有可能是什么呀减少对不对当然张三这边应该是减少李四那边应该是什么增加对不对但是这肯定是有个更新这是第一功能第二功能就是查询啊比如我根据这个账号对不对进行这个信息的一个查询这是已经两个功能了对不对然后接下来就是这个表那么这个表呢我们也要实现两个功能第一功能就是往这里边保存数据啊保存数据第二功能就是查询数据比如说根据这个逐渐这个number
[03:55] 进行查询所以一共加起来是两张表四个功能啊两张表四个功能那咱们接下来看这个奖励吧因为这个my belly pass这块代码大家都非常熟啊所以说这个东西我就不再从头给大家编写了我直接拿过来用了嗯我应该是不是在这对不对新建一个dao接口名字呢跟奖励保持一致有点卡然后呢我们把这块代码拿过来用一下
[04:38] 我们看一下从这开始还没有整完还有这部分好咱具体的一起过一遍就行了咱看一看过的同时呢把这个格式也稍微调整一下咱看第一个功能第一个功能呢就是这一块这一块这还没有调整好就是修改某账号的什么呀余额嘛刚才说了张三要干什么呀减少李四要干什么呀对李四要
[05:20] 增加嘛不管怎么着就是修改操作那修改操作是不是应该是有一个什么语句啊啊不对的一句对吧你看啊不对的一句然后是不是修改的是这个表吗刚才让大家看到这个啊康特什么呀音负这个表对不对修改他当然修改了字段是不是就是这个这个余额这个字段是不是你看我们的这个伺服局set这边那个余额吗然后呢呃这个变动的金额是不是通过将来我们会通过一个参数传进来就是变动的这个余额
[05:51] 然后条件呢就是根据这个什么账号就是这个number对吧说这只是一个很简单的一个修改操作啊这个语句大家一看就明白是咋的事然后呢对应这条搜狗语句的话是不是有两个参数吧我先倒一下包哎这个为什么倒不进来呢倒一下啊好咱看看两个参数第一个参数就是这条件这里面是不是要用的这个看到number对吧第二个参数就是这这个变动的这个金额是多少啊哎有的老师这
[06:29] 是不是只能增加你看你这写的加号对吧是不是只能增加余额那李斯那边是要干什么要减少这其实就看你这个值进来传的是正数还是负数明白吗你传正数这就是增加你要传负数这不就变成什么减少了对不对所以你看我这说的是变动进度不是说增加进度或者说什么减少进度所以这是咱这里边第几个功能对第一个功能OK第二个功能第二个功能就是
[06:57] 从这个表里边做一个什么呀查询也很简单Src from是不是还是这个表对吧根据这个什么Akana number做一次查询然后这个参数就一个嘛就是这个Akana number所以这个我就不再说了非常简单这是第二个功能第三个功能就是操作另外一个表就是咱这个表这个用来保存什么事物日志的那首先第一个功能呢就是针对这个表第一个功能就是做查询很简单就是根据这个什么呀
[07:28] number这个主件来做一个查询当然我这只是查询这个什么个数为什么只查询个数呢到用的时候大家就知道了其实我这呢就相当你看我这个名字我这个发名字应该能猜出来is exact这啥意思其实就判断这个事物日志存在还是什么呀不存在的所以我这呢其实不是要它的具体信息的是要它的这个个数就是用来判断它存在不存在那这里边只有一个参数就是这个number对不对这是
[07:59] 这个功能然后最后一个功能最后一个功能呢就是往这里边保存数据的往这个表里边保存数据insider语句对不对然后呢一个值就是这个主键对吧还有呢就是这个什么呀时间窗码就当前的这个时间这个时间窗啊这是搜索语句里边的no函数其实得到就是当前的这个日期时间这是一个保存功能吧也比较简单这是咱们把什么呀DAO层的这个代码咱就连接完了
[08:29] 那这个代表咱写完之后呢接下来咱该干啥呢该噎我层了吧先不着急咱要先搞定这个什么呀这个什么呀发送转账消息为啥要搞定这个呢大家看这个图你看这个图来想你看咱前面介绍过这个解决方案对吧我说了他在实际运行的时候会先发消息对吧发完消息之后呢然后再执行什么呀本地事务进行什么呀账户的余额的一个什么扣减的一个操作对吧
[08:59] 从顺序来讲他应该是先发消息啊所以说咱先不急着实现右层的功能咱先把这个发这个发送什么呀转账消息的这个功能先搞定那这块是不是纯粹就是通过什么呀对RocketMQ的API我们就可以搞定了这些代码呢大家应该以前也比较熟悉啊是不是主要靠这个谁啊RocketMQTemplate这个模板对象来实现的啊所以这样呢我们需要单独定一个类在这个类当中呢实现
[09:28] 发送这个什么转账消息这个功能把这个类呢给他定义一下我们把这个类呢给他放到message这个包里边啊我们先新建一下那这里边我们说了主要是通过这个什么叫RocketMQ template这个对象来实现这个消息的发送了咱需要先把它给注进来与sauce然后privaterocktrocketmqtemplate对吧那我们这边呢还需要定义一个方法那么我们跟讲义保持一致
[10:16] 好大家看一下这个方法这个方法呢这个发明叫啥无所谓对吧主要是这个参数大家看这个参数咱前面是不是刚给大家介绍过阿康的一亲戚一问他对不对我们一开始就给他说这个类码这个类是干嘛的呀是封装转账消息吗我们说了我们现在是不是要要要通过那个模板对象来发消息那么这个相关的数据就这三个数据吧我们会封装到这个什么呀阿康的亲戚经文的对象里边来进行发送所以我们现在其实编写的就是这个代码大家注意一下
[10:46] 就是这个参数啊大家一定要注意他会这个调到这个发的时候会传进来啊传进来之后怎么办呢那这个对象呢我们没法直接发送他是加对象吧所以说你看我们接下来要做什么事对是要给他转换成jason对不对然后呢再封装成对message类型的这个对象然后呢再调用他的这个send messageintranslation我们发的是一个事物消息啊事物消息这个大家一定要注意然后就可以把这个消息给
[11:16] 发送过去那咱接下来呢把这个代码给编写一下首先呢就是我们要构造消息先溜这个jsonobject是吧jsonobject然后等于溜jsonobject然后溜好之后呢溜好之后呢我们就开始往里边放东西啊第二什么方法啊还有印象吗对铺的方法一个键一个值嘛
[11:56] 键的话那咱就跟讲义保持一致啊叫account什么呀chinch进去对吧值是不是就是咱这个参数啊嘛就是accountchinch even先给它存进去然后呢然后呢我们就需要把它转换成什么呀对转换成字符串调哪个方法to对to to哪个to json string调上这个方法把它转换成什么呀
[12:25] 走上走上自顾上直接就发吗不是啊按照这个什么样rocky的mq的这个要求呢我们需要把它封装成message类型的所以说呢我们接下来是这样mesag注意看我们导播应该是导哪个包啊导导哪个包啊哎导哪个包嘞导导spring啊因为他是这个这个整合的吗应该是这个带有饭型的这个
[12:54] 这里边是不是就需要设置一个范形这个范形其实就是字符串白走上msg这个对象怎么构造出来我们需要通过一个叫me ssage builder message builder就是他通过他的一个方法叫对就是哪个方法viz payroll是这个方法
[13:23] 通过他来构造怎么构造呢这里边呢我们就需要把这个字符串JSON串对不对放进然后呢再调用Builder方法就构造出来这个Message对象这是第一步构造消息啊咱整理看一下首先呢我们要Nu一个JSON Object然后呢把这个这个相当于就是这个对象吧加上对象给它存到这里边然后呢把它转换成JSON串然后通过Message Builder对象的方法就是最终是Builder方法
[13:54] 把它再构造成什么呀message对象那只有message对象呢将来才可以通过RocketMQ template来进行什么呀发送所以咱接下来就该干什么呀对发送消息那我们直接就是调这个模板对象的方法叫send messageintranslation注意了我们现在发的是事物消息
[14:22] 这个一开始我们给大家说了嘛这个RocketMQ从4.3之后是不是正式支持这个事务消息它这RocketMQ的消息是分好几种的啊分有分类的我们这儿呢是事务消息你看我们调用的方法什么叫Send a message in Translation那后边怎么写呢后边呢是有好几个参数需要这个往里边扔的啊我们先一个一个来吧第一个参数是啥呢
[14:51] 这第一个参数啊就是一个组名吧这个我们跟嗯讲义要保持一致吧这个名字啊我们看一看讲义里边它是叫啥名呢讲义里边是在这儿啊我把这几个都拿过来啊好第一个参数就是这这个发送方这个一个组的组名对不对那第二个参数非常重要第二个参数是目的地
[15:26] 目的地的这个这个这个topic的名字那这个名字呢将来呢我们在bank2就是消息的接收方那边就要用要跟这保持一致第三个字大家看出来是不是就是这个这个message对象对吧最后一个字表示额外的其他一些参数我们这不需要给成一个闹市就行这就我们就实现了是这个什么呀对发送消息说这块代码其实编译起来不是特别的复杂
[15:55] 那这目前是这个转账啊发送这个转账消息这一块我们已经实验实验完之后呢咱既然是该实现业务层了那么业务层这一块呢是咱们这个案例当中的核心对不对他因为他这边就要调用刚才这个地方要要干什么呀发送事务消息还要进行本地事务扣减金额这个核心的业务都要在这进行什么呀体现了那这一块代码的话咱一会单独再编写

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Cloud 项目中，通过 RocketMQ 实现消息发送方（bank1）与消息接收方（bank2）之间的账户变更消息的可靠传输，包含事件定义、DAO层、消息生产者、事务消息等核心代码。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT标题页，内容为“5.3.3 功能实现”和“5.3.3.1 消息发送方bank1”，并提示“工程中提供的初始文件，由大家自行查看”。
画面2：展示PPT内容“5.3.2 环境搭建”，其中包含环境要求（数据库MySQL 5.7+、JDK 64位 JDK 8+、微服务spring-boot 2.1.3、RocketMQ服务端4.5.0、RocketMQ客户端2.0.2-RELEASE）和“5.3.2.2 创建数据库”的说明，下方显示SQL语句：DROP TABLE IF EXISTS `de_duplication`;。
画面3：展示IDE中“AccountChangeEvent.java”文件，定义了账户变更事件类，包含字段accountNo、amount、txNo。
画面4：展示PPT内容“5.3.3.1 消息发送方bank1”，下方显示SQL语句：
UPDATE account_info SET account_balance=account_balance+#(amount)
WHERE account_no=#(accountNo);
SELECT * FROM account_info WHERE account_no=#(accountNo);
SELECT COUNT(1) FROM de_duplication WHERE tx_no = #{txNo};
画面5：展示IDE中“AccountInfoDao.java”文件，定义了接口方法，包含更新余额、查询账户信息、检查事务是否已执行的SQL语句。
画面6：展示IDE中“AccountInfoDao.java”文件，高亮显示更新余额的SQL语句。
画面7：展示PPT内容“3. 实现发送转账消息”，下方显示代码片段：
@Component
@RabbitListener
public class BankMessageProducer {
    @Resource
    private RocketMQTemplate rocketMQTemplate;
    ...
画面8：展示IDE中“message”包下右键新建文件的菜单，选项包括“Java Class”、“Kotlin File”、“XML Configuration File”等。
画面9：展示PPT内容“5.3.3.1 消息发送方bank1”，下方显示SQL语句：
SELECT * FROM account_info WHERE account_no=#(accountNo);
SELECT COUNT(1) FROM de_duplication WHERE tx_no = #{txNo};
画面10：展示IDE中“BankMessageProducer.java”文件，定义了消息生产者类，包含发送消息的方法。
画面11：展示IDE中“BankMessageProducer.java”文件，高亮显示导入的MessageBuilder类和Message类。
画面12：展示IDE中“BankMessageProducer.java”文件，高亮显示发送消息的代码：
Message<String> msg = MessageBuilder.withPayload(jsonObject.toJSONString()).build();
rocketMQTemplate.sendMessageInTransaction(msg, jsonObject.toJSONString());
画面13：展示IDE中“BankMessageProducer.java”文件，高亮显示事务消息状态处理方法：
public RocketMQLocalTransactionState executeLocalTransaction(Message msg, Object arg) {
    RocketMQLocalTransactionState state = RocketMQLocalTransactionState.COMMIT;
    final JSONObject jsonObject = JSON.parseObject(new String(msg.getPayload()));
    ...
画面14：展示IDE中“AccountInfoServiceImpl.java”文件，定义了服务类，包含注入BankMessageProducer和AccountInfoDao的代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
package cn.itcast.wanxinz.ensure.demo.bank1.model;
import ...
public class AccountChangeEvent implements Serializable {
    private String accountNo;
    // 变动金额
    private double amount;
    // 事务号、时间戳
    private long txNo;
}

画面4：
UPDATE account_info SET account_balance=account_balance+#(amount)
WHERE account_no=#(accountNo);
SELECT * FROM account_info WHERE account_no=#(accountNo);
SELECT COUNT(1) FROM de_duplication WHERE tx_no = #{txNo};

画面5：
import org.springframework.stereotype.Component;
public interface AccountInfoDao {
    // 修改某账号的余额
    @Param("accountNo") 账号
    @Param("amount") 变动金额
    @Return
    // Update "update account_info set account_balance=account_balance+#(amount) where account_no=#(accountNo)"
    int updateAccountBalance(@Param("accountNo") String accountNo, @Param("amount") Double amount);
    // 查询某账号信息
    @Param("accountNo") 账号
    @Return
    // Select "select * from account_info where account_no=#(accountNo)"
    AccountInfo findbyAccountId(@Param("accountNo") String accountNo);
    // 查询某事务是否已执行
    @Param("txNo") 事务号
    @Return
    // Select "select count(1) from de_duplication where tx_no = #{txNo}"
    int isExistTx(long txNo);
}

画面7：
@Component
@RabbitListener
public class BankMessageProducer {
    @Resource
    private RocketMQTemplate rocketMQTemplate;
    ...

画面10：
import cn.itcast.wanxinz.ensure.demo.bank1.model.AccountChangeEvent;
import com.alibaba.fastjson.JSONObject;
import org.apache.RocketMQ.spring.core.RocketMQTemplate;
import java.util.Map;
public class BankMessageProducer {
    @Resource
    private RocketMQTemplate rocketMQTemplate;
    public void sendAccountChangeEvent(AccountChangeEvent accountChangeEvent) {
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("accountChange", accountChangeEvent);
        Message<String> msg = MessageBuilder.withPayload(jsonObject.toJSONString()).build();
        rocketMQTemplate.sendMessageInTransaction(msg, jsonObject.toJSONString());
    }
}

画面11：
import cn.itcast.wanxinz.ensure.demo.bank1.model.AccountChangeEvent;
import com.alibaba.fastjson.JSONObject;
import org.apache.RocketMQ.spring.core.RocketMQTemplate;
import org.springframework.messaging.Message;
import org.springframework.messaging.support.MessageBuilder;
import org.springframework.stereotype.Component;
import org.springframework.util.Assert;

画面12：
Message<String> msg = MessageBuilder.withPayload(jsonObject.toJSONString()).build();
rocketMQTemplate.sendMessageInTransaction(msg, jsonObject.toJSONString());

画面13：
public RocketMQLocalTransactionState executeLocalTransaction(Message msg, Object arg) {
    // 初始化事务状态
    RocketMQLocalTransactionState state = RocketMQLocalTransactionState.COMMIT;
    final JSONObject jsonObject = JSON.parseObject(new String(msg.getPayload()));
    AccountChangeEvent accountChangeEvent = (AccountChangeEvent) jsonObject.get("accountChange");
    // 根据业务逻辑决定事务状态
    if (accountChangeEvent != null) {
        // 业务逻辑处理
        // 如果成功则提交事务
        state = RocketMQLocalTransactionState.COMMIT;
    } else {
        // 如果失败则回滚事务
        state = RocketMQLocalTransactionState.ROLLBACK;
    }
    return state;
}

画面14：
@Service
public class AccountInfoServiceImpl implements AccountInfoService {
    @Autowired
    private BankMessageProducer bankMessageProducer;
    @Autowired
    private AccountInfoDao accountInfoDao;
    @Override
    public void updateAccountBalance(AccountChangeEvent accountChange) {
        // 1. 查询账户信息
        AccountInfo accountInfo = accountInfoDao.findbyAccountId(accountChange.getAccountNo());
        // 2. 检查事务是否已执行
        if (accountInfoDao.isExistTx(accountChange.getTxNo())) {
            // 3. 事务已执行，直接返回
            return;
        }
        // 4. 更新账户余额
        accountInfoDao.updateAccountBalance(accountChange.getAccountNo(), accountChange.getAmount());
        // 5. 发送消息
        bankMessageProducer.sendAccountChangeEvent(accountChange);
    }
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“5.3.3 功能实现”，副标题为“5.3.3.1 消息发送方bank1”。
画面2：PPT标题为“5.3.2 环境搭建”，包含子标题“5.3.2.1 环境要求”和“5.3.2.2 创建数据库”。
画面4：PPT标题为“5.3.3.1 消息发送方bank1”，下方列出SQL语句。
画面7：PPT标题为“3. 实现发送转账消息”，下方列出代码片段。
画面9：PPT标题为“5.3.3.1 消息发送方bank1”，下方列出SQL语句。
画面14：PPT标题为“5.3.3.1 消息发送方bank1”，下方列出代码片段。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）

