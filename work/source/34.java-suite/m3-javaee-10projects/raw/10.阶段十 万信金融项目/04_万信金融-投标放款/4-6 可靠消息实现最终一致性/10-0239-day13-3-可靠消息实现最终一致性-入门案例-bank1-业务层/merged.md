# day13-3-可靠消息实现最终一致性-入门案例-bank1-业务层

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-6 可靠消息实现最终一致性
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-6 可靠消息实现最终一致性\day13-3-可靠消息实现最终一致性-入门案例-bank1-业务层_【海量资源尽在 666java.com】.mp4
- 时长 7分53秒（音频 473s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢咱是不是把数据访问层的代码以及发送转账消息的代码全部编下来那咱接下来呢就开发这个业务层业务层呢无非就是调用这个类实现这个什么呀发送消息然后再调用什么呀数据访问层实现数据库操作对吧把这些功能呢集中体现在这个业务层那咱还是先定一个接口吧这个接口呢我就不再编写这个代码我们直接拿过来用
[00:31] 那我应该是在Service这个包里边我们新建一个右层的一个接口名字呢我们跟简易保证一致拿过来然后呢里边呢你看就两个方法因为我们说了嘛这个张三这边就是半可一这边其实主要的事情就两个一个就是发消息一个就是什么呀对更新账户的一个那具体来说就是应该是减少对吧账户的一个就这点事
[01:05] 所以说我们右层的接口里边就定义了两个方法哎这个方案就是什么呀发送消息的这个方案就干什么呀对扣减这个什么呀余额的啊只不过呢这两个方都需要这个什么呀account 亲戚基本的这个参数因为我们在完成这两个工作的时候是不是都要用到他里边的一些数据这接口咱就定义好然后呢咱们把实现类也定义出来呃实现类的名字呢咱也跟讲义保持一致
[01:39] 然后呢让他去实现我们刚才定义的这个接口然后呢上面的这些注解我们需要加一下什么意思呀那如果你要用日志的话对吧SLF4G没有吗大写SLF4G然后这已经报错了报错是因为我们是不是必须得实现他里边的那两个方法我们把这两个方法呢先给他生成一下
[02:23] 这边代码其实写起来还是比较简单的首先我们先看第一个功能吧第一个功能我们说了就是用来发送消息放消息咋发咱是不是这个功能已经放到这个这个谁呀呃bank message什么呀produs这个类当中我们是把它注进来就可以用了对不对那你要想注入它你这可是少加注解来对不对component这个注解来加上然后呢我们在这边就可以进行注入了private
[02:59] 叫啥名叫bank message producer好他注进来之后呢这个发消息就简单多了我们是不是直接调用他的方法就行了点是不是就是这个方法对吧然后呢把这个参数呢给他扔进去哎大家看一下我们就把什么功能搞定了对发送这个转账消息这个功能就搞定了然后接下来还有一个方案要实现这个方案是不是就是更新这个什么呀账户
[03:31] 余额的那这个功能是不是就调用数据防护层就行了那我们是不是应该把那个DAO也给他注入进来private叫啥名啊我们是叫account我们那个DAODAO在这啊account info DAO对吧那应该是accaccount这个我们所有操作数据库的方案是不是都在这里边对吧
[04:06] 你把它注入进来之后我们也是直接调方法就行了第二我们要调的方法就是这个update account balance对不对那这里边你看是不是要几个参数呀两个参数一个是account number一个是这个什么呀变动的余额这两个星都在哪放着了呀这都在这个参数里边我们从这里边取就行了然后首先我们要取的就是这个账号然后呢再需要取的就是那个
[04:40] 金额是不是就这个金额但这个金额呢你一定要注意啊你不能直接这么一写就放到这儿为什么因为我们说了嘛张三就是半个一这边是比较扣钱对不对扣钱的话你这要给他变成什么呀负数这个大家还有印象吗我们前面在写这个数据访问层的时候你看这儿当时提过嘛你这儿如果传进来的是正数它就是增加余额嘛如果是负数它就减少余额嘛对不对所以我们这儿呢它这个值一定是正数嘛所以说我们乘以负一嘛
[05:12] 成于负极就给它变成负数这是这个什么呀扣减余额就搞定了然后还有一个操作数据操作大家不要忘了我们前面说过嘛我们是不是应该要往这个表里边是要保存一行数据就是当我们这个执行这个什么呀对执行本地事务就是扣减余额的时候呢我们也同步的需要往这里边呢保存一条数据那这个数据将来我们可以用来进行这个事务的回查
[05:41] 那这个也很简单我们是不是也放到这个什么呀啊 deal 里边直接调用方法应该是叫 add 对吧 add text啊然后他的值就是那个那个 number 吗也是从这里边取出来就行了其实就是当前时间的那个那个什么呀时间穿对不对就是他哎就可以了啊所以说其实一共是三个操作对吧一个是发消息一个是更新账户的余额一个是网那个什么呀
[06:11] 事务日志那个记录表里边保存一条数据对吧然后这个方法呢这有一个细节你看这是不是两个操作吗一个是更新那个余额的一个是保存那个事务执行的日志的对不对那这两个操作其实是一个本因事务就是他俩要么都成功要么都失败没错吧所以这块我们要加什么要加受控制怎么加呢咱看咱们讲一
[06:39] 咱们的讲义里边我们加一个注解就行就这个注解这个你一定要注意啊我们是需要给他加上这么一个东西这个注解大家应该都知道是咋回事是不是就是sprint的这个事物的一个控制对不对那里边这个东西呢这个属性呢这个属性咱之前用的不多是不是这是设置这个事物隔离级别的隔离级别咱应该以前学过吧隔离级别那这个值是隔离级别当中应该是要求最简的一种
[07:11] 最严格的这个事务隔离级别那他要求呢这里边操作呢必须严格按照顺序一个一个的去执行啊这个理论来讲呢隔离级别越高他越能保证数据的完整性和一致性但是他对这个并发的性能并发性的影响会比较大但是这一块呢我们不用考虑这个并发啊我们要考虑的就是这个什么呀对数据的完整性和一致性所以说我们这儿呢设置了一个比较高的啊
[07:39] 或者说你可以认为是最高的吧最严格的一个事务隔离基这个大家知道是咋回事就行这是我们把哪一块代码搞定了说把这个右层代码就搞定了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在银行转账场景中，通过消息队列（RocketMQ）实现分布式事务，确保本地事务与消息发送的最终一致性。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了项目结构，当前选中文件为 `BankMessageProducer.java`。
- 代码内容：定义了 `@Component` 注解的 `BankMessageProducer` 类，其中包含 `sendAccountChangeEvent` 方法，用于发送账户变更事件消息。
- 代码片段：
  ```java
  @Component
  @Slf4j
  public class BankMessageProducer {
      @Resource
      private RocketMQTemplate rocketMQTemplate;
  
      public void sendAccountChangeEvent(AccountChangeEvent accountChangeEvent) {
          // 构造消息
          JSONObject object = new JSONObject();
          object.put("accountChange", accountChangeEvent);
          MessageString msg = MessageBuilder
                  .withPayload(object.toJSONString())
                  .build();
          // 发送消息
          SendResult sendResult = rocketMQTemplate
                  .sendMessageInTransaction("producer_ensure_transfer",
                          "topic_ensure_transfer",
                          msg, null);
      }
  }
  ```

画面2：
- 展示了 `AccountInfoDao` 接口定义。
- 代码内容：定义了 `@Mapper` 注解的接口，包含 `updateAccountBalance` 方法用于修改账户余额，以及 `select` 方法用于查询账户信息。
- 代码片段：
  ```java
  @Mapper
  public interface AccountInfoDao {
      /*
       * 修改某账号的余额
       * @param accountNo 账号
       * @param amount 变动金额
       * @return
       */
      @Update("update account_info set account_balance=account_balance+#{amount} where account_no=#{accountNo}")
      int updateAccountBalance(@Param("accountNo") String accountNo, @Param("amount") Double amount);
  
      /*
       * 查询某账号信息
       * @param accountNo 账号
       * @return
       */
      @Select("select * from account_info where account_no=#{accountNo}")
      AccountInfo selectAccountInfo(@Param("accountNo") String accountNo);
  }
  ```

画面3：
- 展示了 `AccountInfoService` 接口定义。
- 代码内容：定义了 `AccountInfoService` 接口，用于声明业务方法。

画面4：
- 展示了在 `AccountInfoService` 接口中，通过右键菜单选择“Generate” -> “Setter” 为 `AccountChange` 类生成 setter 方法。

画面5：
- 展示了 `AccountInfoServiceImpl` 类的创建过程。
- 代码内容：创建了 `AccountInfoServiceImpl` 类，实现了 `AccountInfoService` 接口。

画面6：
- 展示了 `AccountInfoServiceImpl` 类的代码编辑界面。
- 代码内容：导入了必要的包，包括 `@Service` 注解和 `@Slf4j` 注解。

画面7：
- 展示了 `AccountInfoServiceImpl` 类中定义了 `private` 字段。
- 代码内容：定义了 `private` 字段，用于存储 `BankMessageProducer` 和 `AccountInfoDao` 的实例。

画面8：
- 展示了 `AccountInfoServiceImpl` 类中定义了 `@Autowired` 注解的字段。
- 代码内容：定义了 `@Autowired` 注解的 `bankMessageProducer` 和 `accountInfoDao` 字段。

画面9：
- 展示了 `AccountInfoServiceImpl` 类中定义了 `updateAccountBalance` 方法。
- 代码内容：定义了 `updateAccountBalance` 方法，用于更新账户余额。

画面10：
- 展示了 `AccountInfoDao` 接口的代码编辑界面。
- 代码内容：定义了 `updateAccountBalance` 方法，用于更新账户余额。

画面11：
- 展示了 `AccountInfoServiceImpl` 类中定义了 `doupdateAccountBalance` 方法。
- 代码内容：定义了 `doupdateAccountBalance` 方法，用于更新账户余额。

画面12：
- 展示了 `AccountInfoServiceImpl` 类中定义了 `doupdateAccountBalance` 方法。
- 代码内容：定义了 `doupdateAccountBalance` 方法，用于更新账户余额。

画面13：
- 展示了 `AccountInfoServiceImpl` 类中定义了 `doupdateAccountBalance` 方法。
- 代码内容：定义了 `doupdateAccountBalance` 方法，用于更新账户余额。

画面14：
- 展示了 `AccountInfoService` 接口的代码编辑界面。
- 代码内容：定义了 `updateAccountBalance` 和 `doupdateAccountBalance` 方法，用于更新账户余额。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
（已在上述各画面要点中完整抄录）

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
（无 PPT 标题、架构图/流程图或表格数据）

5) 不要评价画面美观，不要输出与课程无关的内容。
（已遵守）

