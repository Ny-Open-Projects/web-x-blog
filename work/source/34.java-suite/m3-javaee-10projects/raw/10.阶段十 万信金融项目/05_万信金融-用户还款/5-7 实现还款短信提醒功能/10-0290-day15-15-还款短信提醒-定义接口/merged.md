# day15-15-还款短信提醒-定义接口

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-7 实现还款短信提醒功能
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-7 实现还款短信提醒功能\day15-15-还款短信提醒-定义接口_【海量资源尽在 666java.com】.mp4
- 时长 6分2秒（音频 362s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 刚才我们一起了解了一下腾讯云并做了一些准备工作对吧那咱接下来就开始编码实现这个还款短信提醒功能首先还是先定义什么呀接口那么这个地方呢我们一共要定义两个接口大家看一下我们起来有名字一个叫还款服务发送短信接口
[00:25] 一个是叫还款服务还款提醒接口这只是名字啊那这两个接口分别起什么作用呢咱一个一个给大家说一说啊第一个接口啊这个接口功能很纯粹就是通过腾讯云去干什么呀对发送短信了就是发送短信那我们通过腾讯云发送短信为什么还要设置成一个接口那我将来我要考虑这个事我将来很有可能这个发送短信我不用这个什么腾讯云了
[00:56] 我可能会用什么呀阿里运是不是这都是有可能的啊所以说我们这要设计成一个接口将来方便切换那第二个接口就是还款提醒接口这个接口他主要是为了查询到一些数据比如说大家想一下啊我们在发送短信的时候你是不是得知道借款员的手机号我得知道给谁发呀你是不是得知道他的还款日期是多少你是不是得知道他还款的金额是多少是不是你有了这些数据是不是才能发短信
[01:25] 所以说呢第二个接口我们叫还款提醒接口其实它主要的功能就是为了查询什么呀查询到这些信息你首先要查询到所有到期的还款计划对不对然后查查这个借款它的手机号对不对它的什么呀这个什么呀还款日对不对还有这个什么呀还款金额这些信息都查了查了之后呢由这个接口去调用上面这个接口然后发送这个什么呀短信明天是咋回事吧
[01:54] 所以说呢我们一共是设计成了这两个接口这是功能吧咱大概了解一下接下来的话咱就开始把这两个接口呢给他编写一下那咱首先需要新建一个sms包啊把跟这个发送短信相关的这个接口啊我们全部放到这个包里边啊咱回到这个谁啊这个repayment Service这个微服务里边啊在这儿我们再新建一个包叫
[02:25] sms然后呢在这里边呢我们先建第一个接口发送短信的接口名字呢我们跟讲义保持一致叫smsservice好咱们先来看看讲义我们在这个接口里边呢需要定义一个方法就是发送短信的一个方法名字叫seed repayment notify对吧然后重点我们要看的就是这个方法有三个参数第一个参数就是借款人的什么呀
[03:02] 对还款人的手机号我得知道我这个短信发给谁是不是然后呢日期对不对还有就是什么呀还款金额这些数据是不是应该是要往那个短信的那个模板里面往里边填值呢对不对说他需要这几个参数啊那咱接下来的话把这个方法给他加进来那这个方法都不需要返回值了啊我们就是发个短信嘛不需要有什么返回值啊发名呢刚才说了叫sendrepayment然后no
[03:34] tify对吧然后呢一共有这三个参数第一个参数呢是手机号这第二个参数是什么呀是日期也是字符串类型的啊最后一个参数呢是英环金额这个呢我们得用big decimal对吧你看到这个类型我们就会想到这哥们得还多少钱是吧得用这种类型好这是我们把方法就定义好了然后把这块注释呢我就直接拿过来了
[04:13] 站到这这是咱把第一个接口是不是就定义好了第一个接口定义好之后呢咱接下来开始定义第二个接口那我们说这个第二个接口它是干嘛的呀主要是用来查询一些数据的比如说刚才第一个接口里边要的这些数据是不是我们接下来都要在第二个接口里边把它给查询出来那咱接下来这个是要在什么呀repayment Service接口里边新增一个方法
[04:44] 那我们找到这个谁啊repayment Service也有层面接口对不对然后呢在这里边我们再定一个方法这个方法呢它比较简单啊我们只需要呢是一个参数就够了然后呢没有返回值方法名呢我们得跟讲义保持一致它也叫sendrepaymentnotify是不是然后这里边呢我们只需要传进来一个数据就是方法日期哎就是说呢
[05:15] 我需要把到期的啊就是某个日期到期的这个还款计划全部查出来然后再从还款计划里边把还款人的什么手机号啊这个还款金额等我想要的信息给查出来就行了啊所以说第二个接口其实主要就是来查询数据那这呢我就加一个注释吧呃那就是什么呀对查询借款人相关信息吧就这样
[05:49] 这是咱们把第二个接口也定完那目前的话跟这个什么呀还款短信提醒这个功能相关的两个接口呢我就全部定义好了一会咱们就实现功能

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在还款服务中定义短信通知接口，并在IDE中创建和编写该接口的Java代码。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示PPT内容，标题为“8.2.2 还款服务还款提醒接口”，其中“2. 接口定义”部分显示了接口定义的Java代码，包含注释和方法签名。
画面2：与画面1内容相同，PPT页面未变化。
画面3：与画面1内容相同，PPT页面未变化。
画面4：PPT页面切换，显示“8.2.2 还款服务还款提醒接口”下的“1. 接口描述”，列出三个步骤：1) 查询所有到期的还款计划；2) 根据还款计划查询用户手机号；3) 调用发送短信接口进行还款提醒。
画面5：IDE界面，显示项目结构和pom.xml文件内容，其中包含Spring Boot Starter和qcloudsms的依赖。
画面6：在IDE中右键点击“sms”包，弹出上下文菜单。
画面7：在IDE中右键点击“sms”包，弹出上下文菜单。
画面8：IDE中打开SmsService.java文件，准备创建接口。
画面9：在SmsService.java中输入接口方法签名，IDE提示导入类型。
画面10：在SmsService.java中输入方法参数类型，IDE提示导入类型。
画面11：在SmsService.java中完成接口定义，导入了java.math.BigDecimal。
画面12：PPT页面切换，显示“8.2.2 还款服务还款提醒接口”的“1. 接口描述”和“2. 接口定义”部分。
画面13：IDE中打开RepaymentService.java文件，显示其中的confirmRepayment和invoiceConfirmRepayment方法。
画面14：在RepaymentService.java中，IDE提示导入类型，准备调用sendRepaymentNotify方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
public interface SmsService {
    /*
     * 发送还款短信通知
     * @param mobile 法人手机号
     * @param date 日期
     * @param amount 应还金额
     */
    void sendRepaymentNotify(String mobile, String date, BigDecimal amount);
}
```

画面5：
```xml
<dependency>
    <groupId>org.apache.RocketMQ</groupId>
    <artifactId>RocketMQ-spring-boot-starter</artifactId>
</dependency>

<dependency>
    <groupId>com.github.qcloudsms</groupId>
    <artifactId>qcloudsms</artifactId>
    <version>1.0.5</version>
</dependency>
```

画面8：
```java
package cn.itcast.wanxingzp.repayment.sms;

public interface SmsService {

}
```

画面9：
```java
package cn.itcast.wanxingzp.repayment.sms;

public interface SmsService {
    void sendRepaymentNotify(String mobile, String date, BigDecimal amount);
}
```

画面10：
```java
package cn.itcast.wanxingzp.repayment.sms;

public interface SmsService {
    void sendRepaymentNotify(String mobile, String date, BigDecimal amount);
}
```

画面11：
```java
package cn.itcast.wanxingzp.repayment.sms;

import java.math.BigDecimal;

public interface SmsService {
    void sendRepaymentNotify(String mobile, String date, BigDecimal amount);
}
```

画面13：
```java
/**
 * 远程网关确认还款接口
 * @param repaymentPlan
 * @param repaymentRequest
 */
void invoiceConfirmRepayment(RepaymentPlan repaymentPlan, RepaymentRequest repaymentRequest);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面4：
标题：8.2.2 还款服务还款提醒接口
子标题1：1. 接口描述
内容：
1) 查询所有到期的还款计划
2) 根据还款计划查询用户手机号
3) 调用发送短信接口进行还款提醒

画面12：
标题：8.2.2 还款服务还款提醒接口
子标题1：1. 接口描述
子标题2：2. 接口定义
内容：
在RepaymentService接口中，定义如下方法：
```java
/*
 * 发送还款提醒
 */
void sendRepaymentNotify(String mobile, String date, BigDecimal amount);
```

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

