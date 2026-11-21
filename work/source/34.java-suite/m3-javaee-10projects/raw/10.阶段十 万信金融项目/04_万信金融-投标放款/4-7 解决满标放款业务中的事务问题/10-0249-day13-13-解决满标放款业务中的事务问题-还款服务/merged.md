# day13-13-解决满标放款业务中的事务问题-还款服务

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-7 解决满标放款业务中的事务问题
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-7 解决满标放款业务中的事务问题\day13-13-解决满标放款业务中的事务问题-还款服务_【海量资源尽在 666java.com】.mp4
- 时长 13分9秒（音频 789s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 咱们刚才呢把这个消息的发送方就交易中心整个这块的代码呢全部编写完了那咱接下来呢就该实现哪一块对消息的接收方也就是谁呀对环环服务这边的功能那这边呢其实它就两大块的功能对吧第一大块就接收消息是不是消息接收方法它首先得接收消息接收完消息之后呢就执行本地事务它这边的本地事务就是生成环环计划和
[00:29] 应收明细那其实它这个功能咱之前是不是都已经开发过了咱找找之前的代码先回顾一下之前的代码应该是还款服务我们找到业务层是这个发布是它吧start repayment这里边不就是你看这是生成还款计划的这是生成这个应收明细的对不对这个功能咱其实都已经实现过了那咱接下来主要就是实现这个谁啊对接收消息
[00:58] 那接收消息是不是也得实现一个什么呀对监听器然后收到消息解析消息然后去调用业务层执行什么本地事务那咱是不是也是单独定义一个类啊你找到这个谁还款微服务在这儿对不对找到哪个包啊message有吗没有没有咱自己建一个吧MESSAG对吧
[01:28] message然后呢在这里边新建一个类监听器类消息的消费方嘛那么他是不是需要实现什么呀接口需要实现哪个接口呢大家还有印象吗我们需要实现一个叫rocket mqlistenrocketrocketmqlisten就是他了范形的就是字符串发过来的都是这个字符串
[01:58] 那他肯定要报错因为我们要重写他里边的这个什么呀方法生成一下就这一个方法对吧呃咱先把这个类上面相关的注解啊必要的注解咱先给他补充上一个是component一个是那个监听对不对叫rocket mqmessage这个这里边是不是要设置一个值吗
[02:28] 这个值啊他的属性啥的我就从讲义里边拿过来咱们保持一致两个属性对吧那这里边我们要特别给大家强调一点这个在前面实现这个转账那个案例的时候也给大家强调过哪一点谁和谁的值要要怎么保持一致有印象吗应该是啊这个值不是他啊这是他自己的那个组啊这个值啊tp下降线start对吧repayment
[03:01] 他应该跟我们发消息的时候的第二个参数这是要往事一致咱当时也提过就这个地方呢这个执行不能随便乱写这是注解咱该家都加过了加过之后呢咱在这里边我们刚才说了啊是不是就要接收到消息解析消息然后再执行什么呀本地事务对不对那接收消息咱就不用管了嘛这个监听器本身就是接收消息了他接收到消息之后是不是放到这个什么呀对这个参数里边
[03:32] 所以咱接下来第一步就是干什么呀解析消息然后第二步就是干什么呀对调用业务层然后呢执行本地售也就两个小步骤吧那咱先说这个第一步吧解析消息解析消息的话这个代码咱是不是刚才在那个什么呀发送房是不是刚写过对不对咱也就可以拿过来用一下呗这一块大家看一下啊
[04:10] 呃这个值我们给这改成msg吧保持一致好大家看一下这个代码啊呃咱需要稍微改造一下啊这呢就不需要这了吗不需要这个这样写了他传过来的就是字符串了对不对我们还是先把消息转换成json啊不这个对象然后呢再调用他的get使用方法根据什么呀根据键得到这个我们想要吃这个键可不是project了啊这个键呢应该是咱当时发消息的时候
[04:42] 我们是不是放进去两对东西吗我们现在要的是这个要的是这个东西啊因为这个消息的接收方就是还款服务这边是不是要拿到这个对象然后去生成什么还款计划啊还有什么呀应收明细这个类呢也得改一改没错吧那这儿是不是也都要进行什么修改大家看是不是这么想对吧
[05:14] 那这个消息呢咱就解析完了解析完之后呢第二步呢就是调用业务层去执行本金数那业务层的对象咱还没有注入呀那咱就是out world然后注入这个业务层业务层应该叫啥名应该叫repaymentservice然后呢我们就可以调哪个方法刚才让大家看的叫start什么repayment方法这咱之前写过了你看他要的是不是一个project with tender的dto对象
[05:50] 我们刚从消息里边把它解析出来我这儿一放这就实现了什么功能对执行什么呀本地事务的这个功能然后呢这里边呢这个咱以前代码还要完善一下我们说这是一个本地事务嘛呃他调的这个方法是在一月我从这个地方这个代码是咱之前写过的但是呢这儿呢我们是不是要把它当成一个本地事务去去处理对不对你看这里边有生成缓缓计划有生成了什么呀
[06:22] 这个应收明信对不对他多个操作我们这是一个本地事务所以说呢这个地方你一定要记住跟他加上这个什么呀加什么东西对事务的注解啊要不然这是没有本地事务这里边咱还是加上那个什么呀rollback啊我们抛自己的这个异常吧b u s s iexception对所以最主要是这个注解一定要加啊我们说了这是
[06:54] 呃还款服务就是消息接收方的一个什么样本地事务这个细节一定要注意那这块代码咱补充上之后呢其实呃消息的接收方啊就是还款服务这边代码基本上就搞定了最后呢就剩一个细节什么细节呢呃大家应该有印象的就是我们前面在实现这个转账的时候大家来我们找找啊你看这儿我说啊消息的接收方啊他这边有一个问题是不是要实现密等性有印象吗
[07:25] 要实现密等性嘛因为他这边来我找找找找找咱以前的这个东西第三个对吧我们说了这个在生产环境当中呢消费方很有可能是一个汲取嘛然后由于种种原因他会我们要防止他干什么重复消费重复执行所以说这个地方要去实现什么呀密等性那咱转账业务当中这个密等性怎么实现呢是吧还是通过那个新增的那个表好看一看就是这个是不是通过这个表来实现的
[08:01] 密等性那咱这次也碰到这样的问题啊对吧我们这个呃消息的接收方就是还款服务这边我们同样也要实现什么呀密等性那我们这个地方的密等性怎么实现难道也是跟转转账一样我们再新增这么一个表那就不用了啊那又不用我们准备这么干怎么干呢那这里边其实你实现密等性主要的目的不就是为了防止他这个什么呀
[08:30] 重复的往表里边插数据嘛大家看啊回顾一下咱这个代码咱整个这一块以前写的这个代码你看首先是生成这个还款计划生成完之后是不是要把这个还款计划保存到表里边这个你还有印象吗然后呢是生成应收明细然后应收明细也得保存到什么数据库里边我们这样实现的这个密等性控制其实说白了就是不让它重复的往数据库里边去保存这些什么数据是这意思吧那我们只要做到这一点这个密等性我们是不是
[09:00] 也就实现了那我们想了这么一个方法啊大家看一下行不行这个方法还比较简单啊什么方法呢咱一起看一看我们准备这么干你不就是为了防止这个表里边添加重复的数据吗哎我就往表里边添加一个什么唯一所以但是唯一所以的作用就是防止添加什么重复数据那如果说你这个这个要添加重复的数据那那这个你肯定添加不进去吗因为我这个表里边有什么有唯一所以
[09:31] 那也就是说呢我现在只需要往表里边添加个我一所以那么我们就不用再编写什么加代码也不用像转账一样再单独什么呀造一个表这个方案是比较简单但是能不能搞定呢咱进来看看我这提供好了这个建所有的这个脚本我先拿过来咱先看看大家看一下我准备给这个谁还款计划你看这是还款计划就是这个表
[10:06] 我们刚才说了嘛这个还款服务这边他在执行本地事务的时候是不是要往这个表里边干什么呀对保存数据是不是我们这密等性实现密等性就是为了防止重复的数据往这里面进行什么呀保存那我就给这个表添加唯一索引吧添加唯一索引那你重复添加数据你是添加不进去的那大家看一下这个脚本啊你看alert table对吧修改这个表怎么修改呢我要添加一个唯一索引unique对吧index这是索引的名字这个可以随意命名
[10:36] 关键是后边后边大家看一下我们经常见到的这个唯一索引是不是都是针对某一个字段对不对比如说这个什么什么ID对不对我可以把这个字段呢给它新建成一个什么呀一个所以但是呢我们这个场景当中呢你用一个字段是不能解决这个密等性的这个问题你看我一共挑了几个字段三个字段我挑了三个字段相当于是搞了一个组合所以因为你挑一个字段或者两个字段都不行我挑了三个字段大家看一看
[11:08] 一个consumer ID一个project ID一个什么呀七数这是七数你看七数对不对也就是说一个是发标人的标识一个是标底的标识一个是七数这三个字段组合到一起那么这个唯一索引就能保证这个数据的什么呀唯一性就是某个人对吧某个标底这个某一期你比如说你借钱借了12个月那就是12期对吧就是123456嘛这是七数说这三个字段组合到一起就可以保证数据的什么呀
[11:39] 那如果你在添加数据的时候这三个字段都一样那我就认为是什么重复数据那你就添加不进来那什么意思啊我这么发是最简单的我们只要执行一下思维脚本给这个表添加了这么一个组合的一个什么所以那这个密等性的问题咱就解决了做咱进来执行啊这报了一个错是吧这个点是我刚才
[12:07] 这个从那个什么呀从pdf里边粘的时候可能会有点问题repayment plan是这个点吗啊这行代码我就不要了我这是不是都已经这个干什么呀都已经选进来了是不是我就直接执行了啊啊这呢就可能是这个符号的问题我们再执行啊他说这个什么呀这已经存在了呀是不是刚才执行成功了这个名字也可以随便改了你再改一个名字执行因为这次是不是就执行成功了啊
[12:43] 这个反正这个索引名你可以自定义然后呢就是你从pdf里边粘的时候可能那个点啊或者一些符号可能会报这个语法凑或者说呢这个东西你可以自己手写一下都行这是咱把索引加上它到底起不起作用咱是不是将来要做功能测试到时候再说这是目前吧咱们把这个消息的接收方啊就是缓缓服务这边的代码我们也全部编写完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 RocketMQ 消息队列实现还款服务的异步处理，包括消息消费者监听、业务逻辑处理、数据库事务管理及状态流转。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示还款流程图，重点在“接口⑤”和“接口⑥”，涉及状态变更和交易记录更新。
画面2：展示 RepaymentServiceImpl.java 代码，处理还款逻辑，包括计算月数、获取还款方式、生成还款计划。
画面3：继续展示 RepaymentServiceImpl.java 代码，重点在生成还款计划并保存到数据库。
画面4：展示 StartRepaymentMessageConsumer.java 文件，开始编写消息消费者类。
画面5：展示 StartRepaymentMessageConsumer.java 的 RocketMQ 相关配置注解。
画面6：展示 StartRepaymentMessageConsumer.java 中解析消息体并转换为 ProjectWithTendersDTO 对象。
画面7：展示 StartRepaymentMessageConsumer.java 的代码，准备调用业务服务。
画面8：展示 RepaymentServiceImpl.java 中 startRepayment 方法的业务逻辑。
画面9：展示 RepaymentServiceImpl.java 中 startRepayment 方法的事务注解。
画面10：展示 PPT 内容，讲解消息接收方（还款微服务）的实现，包括 @RocketMQMessageListener 注解和业务调用。
画面11：展示还款流程图，重点在“接口⑥”和“接口⑦”，涉及状态变更和交易记录更新。
画面12：展示 RepaymentServiceImpl.java 中 startRepayment 方法的业务逻辑。
画面13：展示 PPT 内容，讲解功能测试，包括数据库索引创建语句。
画面14：展示还款流程图，重点在“接口⑥”和“接口⑦”，涉及状态变更和交易记录更新。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
//1.2 获取投标信息
List<TenderDTO> tenders = projectWithTendersDTO.getTenders();
//1.3 计算还款的月数
Double cell = Math.ceil(projectDTO.getPeriod() / 30.0);
Integer month = cell.intValue();
//1.4 还款方式，只针对等额本息
String repaymentWay = projectDTO.getRepaymentWay();
if (repaymentWay.equals(RepaymentWayCode.FIXED_REPAYMENT.getCode())) {
    //1.5 生成还款计划
    EqualInterestRepayment fixedRepayment = RepaymentUtil.fixedRepayment(projectDTO.getAmount(), projectDTO.getPeriod(), projectDTO.getTenders());
    //2.1 根据投资人生成明细
    tenders.forEach(tenderDTO -> {
        //2.2 保存应收明细到数据库
        List<RepaymentPlan> planList = saveRepaymentPlan(projectDTO, fixedRepayment);
        planList.forEach(plan -> tenderDTO.receipt(plan));
    });
}
```

画面3：
```java
//2.2 保存应收明细到数据库
List<RepaymentPlan> planList = saveRepaymentPlan(projectDTO, fixedRepayment);
planList.forEach(plan -> tenderDTO.receipt(plan));
```

画面4：
```java
package cn.itcast.wanxing2p.repayment.message;
import org.apache.RocketMQ.spring.core.RocketMQListener;
```

画面5：
```java
@RocketMQMessageListener(topic = "TP_START_REPAYMENT", consumerGroup = "CID_START_REPAYMENT")
```

画面6：
```java
final JSONObject jsonObject = JSON.parseObject(new String(byte[]));
Project project = JSON.parseObject(jsonObject.getString("project"), Project.class);
```

画面7：
```java
@RocketMQMessageListener(topic = "TP_START_REPAYMENT", consumerGroup = "CID_START_REPAYMENT")
public class StartRepaymentMessageConsumer implements RocketMQListener<String> {
```

画面8：
```java
//1.1 获取投标信息
ProjectDTO projectDTO = projectWithTendersDTO.getProject();
//1.2 获取投标信息
List<TenderDTO> tenders = projectWithTendersDTO.getTenders();
//1.3 计算还款的月数
Double cell = Math.ceil(projectDTO.getPeriod() / 30.0);
Integer month = cell.intValue();
//1.4 还款方式，只针对等额本息
String repaymentWay = projectDTO.getRepaymentWay();
if (repaymentWay.equals(RepaymentWayCode.FIXED_REPAYMENT.getCode())) {
    //1.5 生成还款计划
    EqualInterestRepayment fixedRepayment = RepaymentUtil.fixedRepayment(projectDTO.getAmount(), projectDTO.getPeriod(), projectDTO.getTenders());
    //2.1 根据投资人生成明细
    tenders.forEach(tenderDTO -> {
        //2.2 保存应收明细到数据库
        List<RepaymentPlan> planList = saveRepaymentPlan(projectDTO, fixedRepayment);
        planList.forEach(plan -> tenderDTO.receipt(plan));
    });
}
```

画面9：
```java
@Transactional
public String startRepayment(ProjectWithTendersDTO projectWithTendersDTO) {
    //1.1 获取投标信息
    ProjectDTO projectDTO = projectWithTendersDTO.getProject();
    //1.2 获取投标信息
    List<TenderDTO> tenders = projectWithTendersDTO.getTenders();
    //1.3 计算还款的月数
    Double cell = Math.ceil(projectDTO.getPeriod() / 30.0);
    Integer month = cell.intValue();
    //1.4 还款方式，只针对等额本息
    String repaymentWay = projectDTO.getRepaymentWay();
    if (repaymentWay.equals(RepaymentWayCode.FIXED_REPAYMENT.getCode())) {
        //1.5 生成还款计划
        EqualInterestRepayment fixedRepayment = RepaymentUtil.fixedRepayment(projectDTO.getAmount(), projectDTO.getPeriod(), projectDTO.getTenders());
        //2.1 根据投资人生成明细
        tenders.forEach(tenderDTO -> {
            //2.2 保存应收明细到数据库
            List<RepaymentPlan> planList = saveRepaymentPlan(projectDTO, fixedRepayment);
            planList.forEach(plan -> tenderDTO.receipt(plan));
        });
    }
}
```

画面10：
```java
@RocketMQMessageListener(topic = "TP_START_REPAYMENT", consumerGroup = "CID_START_REPAYMENT")
public class StartRepaymentMessageConsumer implements RocketMQListener<String> {
    @Autowired
    private RepaymentService repaymentService;
    @Override
    public void onMessage(String projectStr) {
        System.out.println("消费消息：" + projectStr);
        JSONObject jsonObject = JSON.parseObject(projectStr);
        ProjectWithTendersDTO projectWithTendersDTO = JSON.parseObject(jsonObject.getString("projectWithTendersDTO"), ProjectWithTendersDTO.class);
        //2. 调用业务层执行本地事务
        repaymentService.startRepayment(projectWithTendersDTO);
    }
}
```

画面13：
```sql
use p2p_repayment . repayment_plan ;
ALTER TABLE .repayment_plan
ADD UNIQUE INDEX plan_unique ( CONSUMER_ID , PROJECT_ID ,
NUMBER_OF_PERIODS );
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面10：
标题：5.4.2 消息接收方：还款微服务
内容：
- 实现 RocketMQ 事务消息监听器，收到消息后，解析消息、调用业务层进行处理。
- 代码示例：
```java
@RocketMQMessageListener(topic = "TP_START_REPAYMENT", consumerGroup = "CID_START_REPAYMENT")
public class StartRepaymentMessageConsumer implements RocketMQListener<String> {
    @Autowired
    private RepaymentService repaymentService;
    @Override
    public void onMessage(String projectStr) {
        System.out.println("消费消息：" + projectStr);
        JSONObject jsonObject = JSON.parseObject(projectStr);
        ProjectWithTendersDTO projectWithTendersDTO = JSON.parseObject(jsonObject.getString("projectWithTendersDTO"), ProjectWithTendersDTO.class);
        //2. 调用业务层执行本地事务
        repaymentService.startRepayment(projectWithTendersDTO);
    }
}
```

画面13：
标题：5.4.3 功能测试
内容：
- 交易中心和还款服务都成功。
- 交易中心执行本地事务失败，则还款服务接收不到消息。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

