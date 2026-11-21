# day13-11-解决满标放款业务中的事务问题-交易中心-发送消息

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-7 解决满标放款业务中的事务问题
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-7 解决满标放款业务中的事务问题\day13-11-解决满标放款业务中的事务问题-交易中心-发送消息_【海量资源尽在 666java.com】.mp4
- 时长 12分11秒（音频 732s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们一起分析了一下满标放款业务当中所涉及到的分布式事务问题那咱接下来呢就参考这个图这个解决方案这个图呢把这个分布式事务问题呢编码给它解决了那咱首先从哪开始呢咱们要从先从哪交易中心开始因为在这个案例当中呢交易中心是消息的发送方对吧而还款服务呢是消息的接收方
[00:29] 所以咱先搞定消息的发送方就是交易中心那咱参考讲义啊首先我们是不是要做一些依赖的检查其实接下来这个过程呢跟前面我们实现转账那个流程基本上是一样的只不过是要不一样了对吧他那是转账咱这是什么呀满标放款是不是啊这个依赖的检查大家下去自己检查了啊就是碰我念里边你看看有没有引入这个依赖啊没有引入的话你就自己加一下就行了
[00:58] 那第二步呢我们要检查这个Apollo上面对不对咱交易中心这个项目当中关于RocketMQ的相关的一些什么样配置你比如说这个IP地址啊端口号对吧group啊对吧等等等等这个的话我们一起看一看吧这个应该是咱之前应该是配过的啊交易中心对不对咱找一找那个RocketMQ那个名称空间在最下面你可以看一下
[01:28] 咱这是不是已经配置过了嘛咱那说Key.MQ比如在本机上嘛对不对手机号7.0.0.1端口号默认9876这个名字你可以自己随便给自己自定义就行这块你要检查一下这是相关的一些配置嘛那第三步咱就要编写加代码开始实验功能首先呢我们要实验功能就是发消息是不是你看这个图交易中心要先发消息发消息的话怎么发大家想想我们以前转账的一个例子当中
[01:59] 是不是单独定义了一个类定义一个方法然后呢在那里边实现了这是什么呀对发消息咱看看那讲义是不是也是如此你看他说也是单独新建一个类对不对然后呢在这个类当中呢实现什么呀交易中心这边去发消息所以咱接下来呢去找到交易中心这个微服务啊找到哪个包呢咱是不是也可以单独建一个message这么一个包对不对
[02:29] 先新建一个包反正这个呢你可以自定义包包在这儿我们写一个什么呀MESSAGE吧然后呢在这里边呢我们就新建一个类跟讲义保持一致然后呢在这个类当中呢我们是不是需要单独定义一个方法然后在这个发里边呢去具体实现对发消息这个功能就发定义部分呢我们跟讲义保持一致了
[03:08] 接下来的话我们先补充一些必要的一些注解component对不对然后呢我们看这个方法这个方案名字比较长吧但是见名之义你看这是不是就是干什么呀修改标底的状态然后呢启动还款是不是当然我们说了嘛我们在这个方案里边主要就是发消息这个有两个参数大家注意一下一个是project一个是
[03:36] project with tenders DTO那我们为什么需要这两个参数呢大家看是不是一个是标底对象对吧一个呢这个呢这个对象呢是我不知道你有没有印象啊咱们在前面实现满标放款功能的时候呢这个东西是准备咱们打开一个东西这个东西是准备往满准备往这个什么还款服务这边发的就是22这一笔发到这之后呢它才可以生成什么还款计划应用明信
[04:06] 所以这两个信息这两块信息都是哪边需要用的呀对都是这个呃什么呀还款服务这边他需要用到这需要大家注意的呃这个代码你要是先常忘了的话你可以打开这个什么呀要藏你看看是不是他当时写的这个代码吗对不对你看你看写到这咱当时写到这是不是给他跳过去了吗对不对咱一会就要补充这个代码你看咱在这个
[04:37] 代码上面你看是不是准备了有什么呀准备数据准备的就是这个谁啊project with tender DTO当然上面肯定还有什么对象project对象嘛对不对这些东西我们一会都要都要发送啊都要发送所以你看这个方法里边呢我们就设计了这两个参数啊这需要大家注意的那在这个方法里边我们怎么实现这个发送消息这个功能呢这个大家应该有印象是不是有两个步骤吗第一步是构造消息第二步呢就是什么呀对发送
[05:08] 消息啊一步一步来吧先说构造消息吧这个怎么搞的这个代码你还有印象吗是不是我们得先把这两个参数对不对就这两个对象先给他放到jasonobject里边对不对啊我先把jasonobject呢这个对象给他创建出来等于6直接6了然后呢调他的什么方法呀往里边放东西对put方法我们要put两对东西
[05:41] 因为有两个参数啊嘛这两个数据我们都要翻过去啊那就是这个project吧一个是这个project然后啊再来一对儿点还是put这对呢就是这个谁啊对第二个参数一个见一个值吗然后呢我们再把这个jason啊把jack的对象给他干啥呀
[06:13] 对给他转按成jason串然后再封装成RocketMQ里边哪个对象message对象这个代码咱以前写过啊啊在转账那个案例当中对我们先to哪个方法jason stream是不是然后呢我们再调用一个类叫message builder等一下吧这就是他啊他呢有一个方法叫
[06:44] 叫哪个叫vizpayload是不是然后呢我们这个其实这个接线串就是消息的内容嘛就是负载嘛放到这里边啊然后调用这个build方法哎就构造出来一个什么对象message对象message啊message对就是他这里边有个范型就是字符串嘛咱扔给他的不就是接线串吗是不是一个字符串
[07:14] 然后呢咱就起个变量名叫叫send就这样就行了大家看一下这是不是消息我们就构造完毕了就是他呗对不对那我们接下来就干什么呀对开始发送消息发送消息怎么发的还有印象吗你是不是得注入那个什么模板对象对吧private叫啥名啊还有印象吗叫叫啥什么呀RocketMQ
[07:48] template是不是rocketmqtemplate就是它了那然后呢我们就干嘛呀调用它的一个方法很简单是不是封装好的叫send message intranslation我们前面在介绍这个可靠消息实现最终一致性这个解决方案的时候我们提到我们
[08:21] 这个Rookie的MQ里边是不是有一种消息叫事务消息对不对那这个方法呢就是发送事务消息它这里边是不是有几个参数第一个参数是不是那个group对吧第二个参数是那个目的地第三个参数就是我们要发的这个消息最后一个参数咱暂时用不到给个闹值就行了那这些东西呢我们要跟讲义保持一致吧就是这一块当然了前两个参数这些值呢你是可以自定义的但是你特别要注意第二个参数这个这个值将来
[08:53] 那个消费者那边他在接收消息的时候是必要跟这保持一致对不对这个咱之前在讲这个转账案例的时候都给大家强调过这是咱目前把哪块代码搞定了对就是发送消息我们单独定义了一个类定义了一个方法在这里边呢最终呢实现了这个什么呀发送消息的这个功能这儿呢你要注意一下这可不叫MSG对不对这应该是换成这个是吧换成这个
[09:22] 那这块代码咱想完之后在哪调用呢是不是在哪调用呢大家想要在哪调用在哪调用的话其实就是刚才我们说的嘛前面呢我们是不是已经实现过这个右层的代码右层的代码咱当时你看是不是就是走到这了嘛对不对走到这我们说了这涉及到分布式的事物的问题要通过RocketMQ要发送数据嘛那咱刚才在这不就是实现了发送数据发送消息的这个功能吗
[09:52] 所以接下来呢这个方法我们是不是应该是在这儿进行什么呀对要在这儿进行调用了吗你看我们前面这一堆数据该准备的都准备好了吗这些东西我们刚才说了是不是都是要往这个什么呀对环环微服这边发了但是我们是不是先先发给谁呀Rocket的MQ嘛对不对按照咱这个解决方案所以说呢我们这个发送消息这个代码应该在这儿要进行什么呀对要进行调用
[10:21] 那调用的话我们首先是不是要把这个类给他这个类的对象我们得给他注进来就是他嘛是不是得注进来然后调用这个方法就在这吧注进来之后呢咱接下来就是在什么地方找一找啊就在这就在这个地方对不对
[11:02] 我们就可以调用咱刚才定义的这个方法叫啥名叫比较长对吧update projectstatus and start什么呀repayment他要啥你给啥吧那两个参数一个是什么呀project咱上面代码都已经准备好这两个数据了一个是projectwithtenders什么呀抵消对不对你看看这不是不是就是调用刚才咱写的这个代码干什么呀发消息
[11:31] 那其实就是咱讲义当中的哪一块是不是就这一块对吧一二对吧一二这一块然后呢这个代码写完之后呢你就可以干什么呀这个连上下面代码这个什么呀审核成功当然呢这个不一定你这样写审核成功它就一定成功是不是如果整个过程下来都没有出问题的话没有出异常的最终就审核成功但这个代码这个顺序的确是这么写的啊所以这是咱目前吧
[12:03] 消息的发送方就是交易中心这边发送什么呀对发送消息整个这一块代码我们全部搞定了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
实现一个基于 RocketMQ 的分布式事务消息发送功能，具体是通过创建 P2PTransactionProducer 类来发送“项目状态变更并启动还款”消息。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PPT 内容“5.4.2 功能实现”下的“5.4.2.1 消息发送方：交易中心微服务”，并列出“1. 检查pom.xml的依赖”，其中包含 RocketMQ 的 Maven 依赖配置。
画面2：PPT 内容继续，列出“2. 检查Apollo中交易中心项目的micro_service.RocketMQ命名空间配置”，显示了 RocketMQ.producer.group 和 RocketMQ.name-server 的配置值。
画面3：在 IntelliJ IDEA 中，右键点击 pom.xml 文件，弹出菜单，显示了正在编辑的依赖项，包括 org.apache.RocketMQ 和 org.springframework.boot 的依赖。
画面4：在 IntelliJ IDEA 中，显示了 P2PTransactionProducer.java 文件的代码，方法签名是 public void updateProjectStatusAndStartRepayment(Project project, ProjectWithTendersDTO projectWithTendersDTO)。
画面5：在 IntelliJ IDEA 中，代码编辑器中选中了方法签名中的 ProjectWithTendersDTO 参数。
画面6：在 IntelliJ IDEA 中，代码编辑器中选中了方法体中的 JSON 对象构造部分。
画面7：在 IntelliJ IDEA 中，代码编辑器中选中了 MessageBuilder 的 sendResult 方法。
画面8：在 IntelliJ IDEA 中，代码编辑器中显示了完整的消息构造和发送代码，包括创建 JSONObject、设置字段、构建 MessageBuilder 并发送。
画面9：PPT 内容继续，列出“3. 新建P2pTransactionProducer类，实现交易中心发送消息”，并显示了 P2PTransactionProducer 类的代码，包括 @Component 注解和 rocketMQTemplate 字段。
画面10：在 IntelliJ IDEA 中，显示了 ProjectServiceImpl.java 文件的代码，其中包含审核成功后的业务逻辑和异常处理。
画面11：显示了电脑桌面，多个窗口并排显示，包括 Apollo 配置中心、SQL 管理工具、项目代码编辑器等，用于展示系统架构和数据操作。
画面12：在 IntelliJ IDEA 中，显示了 ProjectServiceImpl.java 文件的代码，其中包含分页查询的逻辑。
画面13：在 IntelliJ IDEA 中，显示了 ProjectServiceImpl.java 文件的代码，其中包含调用 P2PTransactionProducer 的方法。
画面14：在 IntelliJ IDEA 中，显示了 ProjectServiceImpl.java 文件的代码，其中包含调用 P2PTransactionProducer 的方法，并在 else 分支中抛出异常。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```xml
<dependency>
    <groupId>org.apache.RocketMQ</groupId>
    <artifactId>RocketMQ-spring-boot-starter</artifactId>
    <version>2.0.2</version>
</dependency>
```
画面2：
```properties
RocketMQ.producer.group = producer_start_repayment
RocketMQ.name-server = 127.0.0.1:9876
```
画面3：
```xml
<dependency>
    <groupId>org.apache.RocketMQ</groupId>
    <artifactId>RocketMQ-spring-boot-starter</artifactId>
    <version>2.0.2</version>
</dependency>
```
画面4：
```java
package cn.itcast.wanxingzp.transaction.message;

import cn.itcast.wanxingzp.api.repayment.model.ProjectWithTendersDTO;
import cn.itcast.wanxingzp.transaction.entity.Project;
import org.springframework.stereotype.Component;

@Component
public class P2pTransactionProducer {
    public void updateProjectStatusAndStartRepayment(Project project, ProjectWithTendersDTO projectWithTendersDTO) {
    }
}
```
画面5：
```java
public void updateProjectStatusAndStartRepayment(Project project, ProjectWithTendersDTO projectWithTendersDTO) {
```
画面6：
```java
//构造消息
JSONObject object = new JSONObject();
object.put("project", project);
object.put("projectWithTendersDTO", projectWithTendersDTO);
```
画面7：
```java
Message<String> msg = MessageBuilder
        .withPayload(object.toJSONString())
        .build();
```
画面8：
```java
//构造消息
JSONObject object = new JSONObject();
object.put("project", project);
object.put("projectWithTendersDTO", projectWithTendersDTO);
Message<String> msg = MessageBuilder
        .withPayload(object.toJSONString())
        .build();
```
画面9：
```java
@Component
public class P2pTransactionProducer {
    @Resource
    private RocketMQTemplate rocketMQTemplate;

    public void updateProjectStatusAndStartRepayment(Project project, ProjectWithTendersDTO projectWithTendersDTO) {
        // 1.构造消息
        JSONObject object = new JSONObject();
        object.put("project", project);
        object.put("projectWithTendersDTO", projectWithTendersDTO);
        Message<String> msg = MessageBuilder
                .withPayload(object.toJSONString())
                .build();
        // 2.发送消息
        SendResult sendResult = rocketMQTemplate
                .send(msg);
    }
}
```
画面10：
```java
//审核成功
return "审核成功";
} else {
    throw new BusinessException(TransactionErrorCode.E_150113);
}
```
画面11：
无代码或配置。
画面12：
```java
if (StringUtils.isNotBlank(order) && StringUtils.isNotBlank(sort)) {
    if (order.toLowerCase().equals("asc")) {
        queryWrapper.orderByAsc(sort);
    } else if (order.toLowerCase().equals("desc")) {
        queryWrapper.orderByDesc(sort);
    }
} else {
    queryWrapper.orderByDesc(Project::getCreateDate);
}
```
画面13：
```java
p2pTransactionProducer.updateProjectStatusAndStartRepayment(project, projectWithTendersDTO);
```
画面14：
```java
p2pTransactionProducer.updateProjectStatusAndStartRepayment(project, projectWithTendersDTO);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT 标题为“5.4.2 功能实现”，子标题为“5.4.2.1 消息发送方：交易中心微服务”，并列出“1. 检查pom.xml的依赖”。
画面2：PPT 标题为“5.4.2 功能实现”，子标题为“5.4.2.1 消息发送方：交易中心微服务”，并列出“2. 检查Apollo中交易中心项目的micro_service.RocketMQ命名空间配置”，并显示了配置项。
画面9：PPT 标题为“5.4.2 功能实现”，子标题为“5.4.2.1 消息发送方：交易中心微服务”，并列出“3. 新建P2pTransactionProducer类，实现交易中心发送消息”，并显示了类的代码。
画面11：无 PPT 标题或架构图。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已满足）

