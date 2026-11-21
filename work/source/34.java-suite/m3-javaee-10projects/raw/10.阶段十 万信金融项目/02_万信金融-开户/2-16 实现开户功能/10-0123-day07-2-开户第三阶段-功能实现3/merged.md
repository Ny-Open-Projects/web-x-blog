# day07-2-开户第三阶段-功能实现3

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-16 实现开户功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-16 实现开户功能\day07-2-开户第三阶段-功能实现3_【海量资源尽在 666java.com】.mp4
- 时长 5分18秒（音频 319s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好我们刚才是不是把第一步更新数据这个功能实现了对吧实现完之后我们在这先不进行调用我们接下来把第二步这个功能实现完之后最后一起完善这块代码就是control代码那咱接下来就实现第二步第二步是不是要发送消息给谁给用户中心这个功能其实简单我们前面是不是学过Spring Boot整合RocketMQ整合完之后要想发个消息简单吗是不是非常简单不知道你还有没有印象大家看一下
[00:31] 我们是不是直接注入一个RocketMQTemplate某版对象是不是调用他的ConvertAndSend的方法这个消息就发出去了非常非常简单所以说呢我们接下来把这块单元编写一下我们去这个还是哪个工程还是这个呃乘管代理服务我们找到message这个包如果没有这个包你单独新建一个啊然后呢我们在这边新建一个类跟这边保持一致吧
[01:04] 然后加上一个注解交给Spring进行管理component然后我们说了发消息主要通过谁去发是不是模板对象就是RocketMQTemplate我们把它直接注进来就可以用了然后就是private叫rocrocketmqtemplate是吧这个注进来之后我们既然就可以通过它干什么
[01:45] 对来发消息发消息主要是调用convert and send的方当然我们这个代码是一定要写到每一个方法里边的我们这样的定义一个方法名字呢我们这个要跟讲义保持一致然后这就是个人开户嘛然后这里边是不是传过来一个一个参数这个参数干嘛将来啊我们存管代理服务给用户追音发消息的时候这个消息我们会封装成这种类型封装一下然后再
[02:18] 发给谁发给这个用户中心那么这个类不存在的话你去这找一找去这里面叫啥名Depository Consumer Response就他我们看一下他是放到哪个包里面的API Depository我们Ctrl C然后是哪儿API Depository存款代理他这里边还要建一个什么跟这一样建一个model包子包
[02:54] 我们建一个叫MOBEL然后呢把它粘到这里就可以了这边还继承了一个对吧depository base response我们再接着找吧这些都不需要大家编写啊反正封装好的这些东西就这那他是在哪放着呢啊也是在这那咱就Ctrl C然后呢还是这啊Ctrl V粘过来
[03:29] 他是分两块了对不对我们看这里边他发过去的消息有什么返回码就比较成功不成功的描述信息交易状态流水号是不是你看这里边都有然后这边还增加了银行代码银行名称他反他发过去的这个消息里边的内容不见得咱都能用但是该发还只管发这边也不报错了对不对然后这里边我们怎么发消息那就是通过RocketMQTemplate的Convert按到什么
[04:02] Send对我们应该是用哪个呀几个参数的呀我们应该用两个参数的啊两个参数大家看我们的讲义两个参数ConferenceSend第一个参数大家知道是不是那个那个那个叫什么呀叫topic主题嘛对不对而且他这个地方还加了什么呀Tag就是标签其实标签是不是对主题的更更详细的一个细分吧是不是这是那个topic这是那个什么呀Tag就是标签
[04:33] 将来我们可能会呃往这发好多这个消息但是呢我们可以通过这个标签进行细分嘛给他再分分类所以说呢这一块代码呢这个名字你就照着咱们这个讲义里边去写就行了尽量不要改因为将来我们在consumer那边收消息的时候是不是也得照着这去写是不是他俩是有对应关系的第二个参数response不就是咱发过去的那个消息吗咱前面说了是要封装成这种类型
[05:03] 给他发过去所以说呢这就是第几步的代码对这就是第二步就是这第二步就是给用户中心发送消息很简单通过模板对象就搞定

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 RocketMQ 实现消息发送，并展示相关代码结构和类定义。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 `DepositoryNotifyController` 中的 `@RequestMapping` 注解，用于接收用户中心的请求，参数包括 `serviceName`、`platformno`、`signature` 和 `reqData`，并返回 "OK"。
画面2：在 IDE 中右键点击 `wanningzp-depository-agent-Service` 模块，选择“Rebuild Module 'wanningzp-depository-agent-Service'”。
画面3：打开 `GatewayMessageProducer.java` 文件，准备编写消息生产者类。
画面4：在 `GatewayMessageProducer` 类中添加 `@Component` 注解，使其成为 Spring Bean。
画面5：在 `GatewayMessageProducer` 类中添加 `@Resource` 注解，准备注入依赖。
画面6：在 `GatewayMessageProducer` 类中导入 `org.apache.RocketMQ.spring.core.RocketMQTemplate`，并声明其私有属性。
画面7：在文件资源管理器中浏览项目文件，选中 `DepositoryConsumerResponse.java`。
画面8：在 IDE 中右键点击 `wanningzp-depository-agent-Service` 模块，选择“Delete”。
画面9：在文件资源管理器中浏览项目文件，选中 `DepositoryBaseResponse.java`。
画面10：在 `DepositoryBaseResponse.java` 中查看 `@Data` 注解的类定义，包含 `respCode`、`respMsg`、`status` 和 `requestNo` 等字段。
画面11：在 `DepositoryConsumerResponse.java` 中查看其继承自 `DepositoryBaseResponse`，并包含 `bankCode` 和 `bankName` 字段。
画面12：在 `GatewayMessageProducer` 类中调用 `rocketMQTemplate` 的 `convertAndSend` 方法发送消息。
画面13：在文件资源管理器中浏览项目文件，选中 `DepositoryBaseResponse.java`。
画面14：在 PPT 中展示需要在 `DepositoryRecordService` 接口中新增 `modifyRequestStatus` 方法，并在 `DepositoryRecordServiceImpl` 中实现该方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@RequestMapping(value = "gateway", method = RequestMethod.GET, params = "serviceName=PERSONAL_REGISTER")
public String receiveDepositoryCreateConsumerResult(@RequestParam("serviceName") String servicename,
        @RequestParam("platformno") String platformno,
        @RequestParam("signature") String signature,
        @RequestParam("reqData") String reqdata) {
    //1. 更新数据
    //2. 发送消息给用户中心
    //3. 给银行存管系统返回结果
    return "OK";
}
```

画面3：
```java
package cn.itcast.wanningzp.depository.message;
```

画面4：
```java
import org.springframework.stereotype.Component;

@Component
public class GatewayMessageProducer {
}
```

画面5：
```java
@Resource
private String xxx;
```

画面6：
```java
import org.apache.RocketMQ.spring.core.RocketMQTemplate;
import org.springframework.stereotype.Component;
import java.lang.annotation.Resource;

@Component
public class GatewayMessageProducer {
    @Resource
    private RocketMQTemplate rocketMQTemplate;
}
```

画面10：
```java
@Data
public class DepositoryBaseResponse implements Serializable {
    @MyModelProperty("返回码")
    private String respCode;
    @MyModelProperty("描述信息")
    private String respMsg;
    @MyModelProperty("交易状态")
    private Integer status;
    @MyModelProperty("请求流水号")
    private String requestNo;
}
```

画面11：
```java
package cn.itcast.wanningzp.api.depository.model;

@Data
public class DepositoryConsumerResponse extends DepositoryBaseResponse {
    @MyModelProperty("银行代码")
    private String bankCode;
    @MyModelProperty("银行名称")
    private String bankName;
}
```

画面12：
```java
rocketMQTemplate.convertAndSend("xxx", xxx);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14：
标题：2. 在DepositoryRecordService接口中新增modifyRequestStatus方法；
内容：根据请求流水号更新请求状态
```java
/**
 * 根据请求流水号更新请求状态
 * @param requestNo
 * @param requestsStatus
 * @return
 */
Boolean modifyRequestStatus(String requestNo, Integer requestsStatus);
```
在DepositoryRecordServiceImpl类中实现modifyRequestStatus方法：

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

