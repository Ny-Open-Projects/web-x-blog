# day14-9-用户还款-第三阶段-发送消息

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-2 用户还款功能实现
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-2 用户还款功能实现\day14-9-用户还款-第三阶段-发送消息_【海量资源尽在 666java.com】.mp4
- 时长 7分42秒（音频 463s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才咱们把用户还款里边第三阶段和第四阶段以及这里边涉及到的分析事务问题我们通过这个图是不是分析了一下那接下来的话按照顺序先开发第三阶段的功能第三阶段大家看是不是首先发送这个消息是不是这个图里边也是一样2.1你看是不是先发送消息发送消息的话这个代码咱们前面在满标放款当中是不是写过我们是不是需要单独定一个类
[00:29] 在这个类当中呢我们去通过Rocket Template你想吧那个模板对象去发送消息就行了那咱就去哪儿啊这是谁发消息啊谁发消息啊还款服务吗是不是还款服务所以咱需要去还款服务里边找到message包啊找到这个包之后呢我们需要新定义一个类
[00:58] 这个名字呢我们要跟讲义保持一致它叫repayment producer我们站过来这个类就是专门用来干什么呀发消息的好我先把这个注解给它加上那在这里边我是不是需要定一个方法来实现这个发消息的这个功能方法这一块的话我们也要跟讲义保持一致这一块好咱整体了解一下这个方法发明了叫conform什么呀repayment那我们重点关注一下这个参数
[01:45] 这两个参数大家结合以往的经验这两个参数应该是要放到消息里边然后进行什么呀发送对不对一个是这个什么呀还款计划一个是咱们这个还款的一个一个请求这里边也会将来我们传的时候会传进来一些数据那这里边都有啥呢咱得进去看看那你看咱现在是不是还还缺这个类呢是不是咱把这个类呢要给他加进来那咱接下来呢去客架里边找一下这个类啊在这
[02:15] 我们看他应该放到什么地方应该放到APID post我们Ctrl CAPI是吧APID post放到这里边我们粘贴过来我们看这里边他其实就是封装还款信息的我们看这里边都有啥信息咱一起瞅一瞅流水号对吧还有预处理的流水号标题的编码平台的佣金
[02:48] 放款明细对吧业务来历还款总额吧其实这些数据的话主要都是因为这个谁呀将来主要是因为这个什么呀银行存款系统这边他要这些数据啊他要啥呢咱就封装啥给他嘛那这里边是不是还缺一个类吗叫什么放款明细对吧他叫repayment detail request是不是那咱接下来把这个类呢也给他加进来来咱还是去课件里边啊
[03:19] 找到他对吧然后我们瞅一瞅这里边是还款明细的请求数据啊还款明细的请求数据这里边有什么呀投资人的编号对不对佣金派系对吧本金利息等等等等啊这都是银行那边需要的那咱看他应该是考到什么地方还是刚才那个地方啊API DepositoryCtrl C然后呢我们还是给他站到这然后你看这边应该他就不报错了对不对
[03:53] 这是这一块吧它里边涉及到的一些什么呀实体类我们简单过一遍啊回头我们是不是要用它往里边封装数据吗封装的时候再说啊这边也不报错了对不对那这个方法有了之后呢咱接下来是不是开始实现这个什么呀发送消息这个功能那大家知道发送消息是不是要通过那个模板对象我们需要把它注进来啊AdRevit叫啥名啊叫RocketMQTemplate是不是
[04:32] 通过他发消息这里边代码大家应该还有印象咱们前面都写过了分成两步第一步就是什么构造消息第二步就是什么发送消息没错构造消息打构造大家还有印象我们需要把这两个参数给他先存到jason这个对象里面然后再转化成jason串最后封装成message对象这不就搞定了对不对咱一起把代码快速的编写一下
[05:04] 接三什么呀object哎是哪个呀应该是这个对不对别打我错包了啊接上object的等于neiljsonobject先你有一个对象然后呢调用他的这个什么方法里边存数据铺的方法一个键一个值对不对嗯首先我们先把这个repayment plan放进去
[05:35] 然后我们再调用他的put方法把第二个参数也给他存进去是吧说句存进去之后呢我们接下来是不是应该要把它转换成json串哪个方法应该是叫tojson string转成json串之后还不行我们是不是要把它封装成这个message对象这个不知道大家还有没有印象了messagemessage哪个message是这个message啊
[06:08] 这个范型的话我们这个消息最终都是字符串MSG吧那这个对象怎么构造不是直接NEO出来的是通过有一个叫什么Message Builder吧是不是对就是他Message Builder呢他有一个方法叫叫什么叫VizViz Pillow是不是我们把这个阶层串不就是消息内容吗给他放进去由他进行封装
[06:38] 当然最终呢我们是需要调用他的这个什么呀bill的方法完成封装哎这就搞定了这个消息咱就勾到好勾到好之后咱就进行发送发送就是通过这个template嘛对吧rocket template调用他的什么方法呀叫叫叫叫什么呀叫send message intranslation咱发的是一个售消息嘛大家有印象吧这里边四个参数啊四个参数的话咱要跟讲义保持一致因为这个值呢咱不能随便乱写
[07:12] 是这一块的然后来第一个不就是咱这边的组名吗这个非常重要是目的地将来那个消息的接收方是不是要根据这个值来进行消息的一个接收那这样子的话咱就把哪一步的代码给搞定了对就是这个2.1对吧对应我们这个图里边的是不是就是一个1对吧发送这个确认缓缓的事物消息这块呢咱就搞定了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 RocketMQ 的还款服务消息处理流程，包括消息生产者、消费者、数据库操作及系统间交互。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示还款服务与存管代理服务、存管系统的交互流程图，包含多个步骤如“1.1.查询到期的还款计划”、“1.7.冻结还款金额”等。
画面2：IDE中显示 `RepaymentService.java` 文件，其中 `preRepayment` 方法内有 `System.out.println("还款预处理成功");` 语句。
画面3：IDE中显示 `RepaymentProducer.java` 文件，准备编写消息生产者。
画面4：文件资源管理器中显示 `day14` 文件夹，包含 `Elasticsearch-7.4` 等文件夹。
画面5：IDE中显示 `RepaymentRequest.java` 文件，其中 `@ApiModelProperty("请求流水号")` 注解的字段 `private String requestNo;` 被高亮。
画面6：展示还款服务与存管代理服务、存管系统的交互流程图，与画面1类似，但步骤编号和部分描述略有不同。
画面7：IDE中显示 `RepaymentRequest.java` 文件，其中 `@ApiModelProperty("业务id")` 注解的字段 `private Long id;` 被高亮。
画面8：显示 `RepaymentDetailRequest.java` 文件，包含多个 `@ApiModelProperty` 注解的字段，如 `@ApiModelProperty("投资人用户编码") private String userNo;`。
画面9：IDE中显示 `RepaymentProducer.java` 文件，正在编写 `@Component` 注解和 `RocketMQTemplate` 字段。
画面10：IDE中显示 `RepaymentProducer.java` 文件，正在编写 `confirmRepayment` 方法，其中 `//1.构造消息` 和 `//2.发送消息` 语句被高亮。
画面11：IDE中显示 `RepaymentProducer.java` 文件，正在使用 `JsonObject` 类的 `put` 方法构造消息体。
画面12：IDE中显示 `RepaymentProducer.java` 文件，正在使用 `Message` 类的构造方法 `Message(String topic, Object payload)`。
画面13：IDE中显示 `RepaymentProducer.java` 文件，正在使用 `rocketMQTemplate` 对象的 `send` 方法发送消息。
画面14：展示一个包含“还款服务”、“RocketMQ”、“存管服务”等节点的流程图，描述消息发送、接收、处理和状态更新的流程。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
Boolean preRepaymentResult = preRepayment(repaymentPlan, repaymentDetail.getPreRequestNo());
if (preRepaymentResult) {
    System.out.println("还款预处理成功");
}
```

画面5：
```java
@ApiModel(value = "还款请求信息")
public class RepaymentRequest {
    @ApiModelProperty("请求流水号")
    private String requestNo;
    @ApiModelProperty("预处理业务流水号")
    private String preRequestNo;
    @ApiModelProperty("标的编码")
    private String projectNo;
    @ApiModelProperty("平台佣金 -- 具体金额")
    private BigDecimal commission;
    @ApiModelProperty("放款明细")
    private List<RepaymentDetailRequest> details;
    @ApiModelProperty("业务id")
    private Long id;
    @ApiModelProperty("还款金额")
    private BigDecimal amount;
}
```

画面8：
```java
/**
 * @author wuzhao@itcast.cn
 * @since 2019/5/26
 */
@ApiModel(value = "RepaymentDetailRequest", description = "还款明细请求信息")
public class RepaymentDetailRequest {
    @ApiModelProperty("投资人用户编码")
    private String userNo;
    @ApiModelProperty("向投资人收取的佣金")
    private BigDecimal commission;
    @ApiModelProperty("利息")
    private BigDecimal dividend;
    @ApiModelProperty("投资人应得本金")
    private BigDecimal amount;
    @ApiModelProperty("投资人应得利息")
    private BigDecimal interest;
}
```

画面9：
```java
import cn.itcast.wanxingzp.api.depository.model.RepaymentRequest;
import cn.itcast.wanxingzp.repayment.entity.RepaymentPlan;
import org.springframework.stereotype.Component;

@Component
public class RepaymentProducer {
```

画面10：
```java
@Resource
private RocketMQTemplate rocketMQTemplate;

public void confirmRepayment(RepaymentPlan repaymentPlan, RepaymentRequest repaymentRequest) {
    //1.构造消息
    //2.发送消息
}
```

画面11：
```java
//1.构造消息
JsonObject jsonObject = new JsonObject();
jsonObject.put("requestNo", repaymentRequest.getRequestNo());
jsonObject.put("preRequestNo", repaymentRequest.getPreRequestNo());
jsonObject.put("projectNo", repaymentRequest.getProjectNo());
jsonObject.put("commission", repaymentRequest.getCommission());
jsonObject.put("details", repaymentRequest.getDetails());
jsonObject.put("id", repaymentRequest.getId());
jsonObject.put("amount", repaymentRequest.getAmount());
```

画面12：
```java
Message<String> message = new Message("repayment-topic", jsonObject.toString());
```

画面13：
```java
rocketMQTemplate.send("repayment-topic", message);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：
- 标题：用户还款业务流程图
- 流程图结构：
  - “还款服务”指向“存管代理服务”（步骤1.1、1.2、1.3、1.4、1.5、1.6、1.7、1.8、1.9、1.10）
  - “存管代理服务”指向“存管系统”（步骤1.4、1.5、1.6、1.7、1.8、1.9）
  - “存管系统”指向“还款服务”（步骤1.7、1.8、1.9）

画面6：
- 标题：还款服务与存管代理服务、存管系统的交互流程图
- 流程图结构：
  - “还款服务”指向“存管代理服务”（步骤1.1、1.2、1.3、1.4、1.5、1.6、1.7、1.8、1.9、1.10）
  - “存管代理服务”指向“存管系统”（步骤1.4、1.5、1.6、1.7、1.8、1.9）
  - “存管系统”指向“还款服务”（步骤1.7、1.8、1.9）

画面14：
- 标题：还款服务与RocketMQ、存管服务的交互流程图
- 流程图结构：
  - “还款服务”指向“RocketMQ”（步骤1.发送确认还款事务消息）
  - “RocketMQ”指向“还款服务”（步骤2.消息接收成功，不可消费）
  - “还款服务”指向“存管服务”（步骤3.接收回调、4.执行本地事务、5.发送执行结果、6.修改消息状态为可消费、7.接收消息（重试）、8.通过Feign向存管）
  - “存管服务”指向“还款服务”（步骤8.通过Feign向存管）

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

