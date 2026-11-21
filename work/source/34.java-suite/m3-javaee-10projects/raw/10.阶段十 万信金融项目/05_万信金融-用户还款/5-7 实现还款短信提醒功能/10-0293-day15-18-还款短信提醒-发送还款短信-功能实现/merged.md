# day15-18-还款短信提醒-发送还款短信-功能实现

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-7 实现还款短信提醒功能
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-7 实现还款短信提醒功能\day15-18-还款短信提醒-发送还款短信-功能实现_【海量资源尽在 666java.com】.mp4
- 时长 11分49秒（音频 709s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们把哪个功能给实现了呀我们把还款提醒功能给实现了那其实具体来说的话就是先把到期的还款计划都查出来然后呢从还款计划里边呢得到借款人借款人其实还款人吧得到他的信息最终我们要的是不是手机号然后接下来就可以给他在那发短信了但是发短信这个功能是不是还没实现
[00:27] 这个功能是不是咱当时应该是定义的是不是第一个接口嘛你还有印象吗就是这个SMS Service那咱接下来就该实现通过腾讯云去干什么呀发送短信的这个功能那咱接下来是不是要把这个接口的实现类先创建出来然后呢在这个方案里边具体实现功能那应该就我们写到哪了那我们放到这个SMS这个包里边
[00:58] 充电一个类名字呢就叫就叫啥名呢我们要跟讲义保持一致啊讲义里边我们看看他起的名字是叫QCloud这个QCloud为啥叫这名呢用QCloud指的就是腾讯云然后呢让他去实现谁呀对SMS这个什么呀接口然后呢重写里边发送短信的这个什么呀方法就行
[01:31] 然后我们先加一些注解啊addservice对吧还有就是add日志吧这根据你的需求啊你要加一些注解呃这些注解加完之后呢咱接下来开始实现这个什么呀发送短信的功能我们前面提过咱这个发送短信要通过谁啊腾讯云去实现对吧那我们自然就要用到腾讯云提供的什么呀一些API对吧就一些类啊一些方法
[02:05] 那这块的话大家其实可以参考腾讯云的这个什么呀官方文档就是这个开发文档啊他这里边其实都有例子你比如说你看这儿是吧根据指定的模板id去发送什么呀短信你看这里边其实我们主要用到的是不是就是这个类对吧叫smssingle什么呀sender这个类然后他有一个方法叫sendv是什么呀
[02:32] PARM其实就这两行代码核心的核心的就这两行代码但是你仔细观察一下我们在编写这块代码的时候你需要提前获取一些数据什么数据呢这是咱们前面提到过的你看他说了你要准备一些必要的参数就是APP IDAPP Key手机号这不用说了就是模板的ID包括这个什么签名对吧这些信息我们一开始在介绍这个什么
[03:02] 腾讯云那时候是不是就已经给人家说过了对不对那你可以登录腾讯云的后台是不是在这进行什么呀申请或者说进行什么呀设置而且呢我们把设置好的这些数据是不是给它配置到什么地方对配置到了我们的这个地方对Apollo上其实现在我们要的就是这四个值我们需要把这个四个值呢给它注入到咱们的
[03:32] 实现类当中然后编码的时候就可以用来咱看一下这个讲义啊你看讲义里边你看是不是首先就是通过at value注解把那四个值呢全部都注入进来了啊这块我就直接拿过来用了因为这个东西大家都比较熟at value注解那你一定要注意啊你一定要注意的就是这四个值啊你一定是提前在Apollo当中已经干什么呀配置过
[04:04] 而且呢还有一个事一个细节你千万不要忘了哪个细节呢就是你在这个Apollo上是不是应该是当时应该是我们说了嘛是新建了一个名称空间吧然后呢你一定要记住在这个什么呀application.yml当中要把这个名称空间给它干什么呀加进来否则那个配置那些值就这些值你是取不到的啊这些细节一定要注意
[04:30] 那这些值我们注入进来之后呢我们接下来在这个方法里边就可以干什么呀对你就可以参考它的这个官方的这个文档吧其实就是我们刚才说的就是这两个代码然后呢就可以实现这个发送短信的这个功能它这个API还是使用起来比较简单的那咱回到这开始编码实现这个功能呃首先的话咱为了便于大家将来能看到这个什么呀效果啊我打印一句话吧呃
[05:01] 那就是给手机号多少对吧发送还款提醒呃我这个提醒的内容不就是一个是什么呀日期一个是什么呀金额嘛对不对这个你大概能把这些信息给他展示出来就行了啊然后后边的话就是对应嘛第一个大股号里边就是手机号第二个大股号里边就是这个什么呀日期
[05:38] 第三个大拐号里边应该就是这个什么呀还款金额我们打下这样的一句话将来我们测试的时候便于观察那咱接下来就实现这个发送短线的功能我们说要用哪个类呀你看这个地方就行了你完全就可以把这一块给他拿过来用一用就行了直接扔过来自动倒包了对不对然后你看这里边我们首先是不是要new一个对象叫sm
[06:10] s single cinder对不对那么在new它的时候呢需要传过来两个数据一个是app id一个是什么呀app key这都是从配置里边我们注入进来然后有了这个对象之后呢我们就可以调用它的一个方法叫send v字什么呀perm这个方法具体就是发送暖信的然后第一个参数是国家代码大家应该知道我们国家的手机号这个国家代码是不是就是86吧对不对
[06:41] 那第二个参数其实就是什么呀手机号手机号不就是目标吗我们通过参数传进来然后呢第三个参数就是这个什么呀模板ID这个咱前面提过嘛你需要设置这个模板信息嘛设置成功之后呢会有一个ID模板ID你放到这儿那就表示我将来发送短信的时候呢就是根据这个ID对应的那个模板内容来进行什么呀对进行发送然后再接下来还有什么信息
[07:13] 这第三个参数啊非常关键你看perms是不是参数的意思这一块的数据啊就是第三个数据第三个参数它是这么子用的啊它是给这个什么呀给这个模板里边的这个站位符提供值的这个大家还有印象吗我们前面在介绍腾讯云那时候我们说过我们是不是要创建一个模板对不对这个模板里边其实就是你发送短信的内容那么这个内容里边呢总有一些数据是不是在变比如说这个还款日对吧
[07:43] 好这个还款金额是不一样的我们是不是通过类似这种语法作为占位服先放到这那么你将来就要在这个地方就第三个参数里边给这些数据给干什么呀提供值你看我这里边是不是应该需要提供几个值两个值需要提供两个值的话那这一块的代码应该怎么写呢那你需要这么的来写大家看啊newstream
[08:11] 你有一个字符串类型的一个数组我们要给几个值我们刚才说了嘛两个值嘛第一个值就是这个什么呀日期第二个值就是那个谁啊对就是那个还款金额就是他咧当然字符串类型的话你需要给他转一下啊转成字符串大家看一下一个日期一个还款金额那么这两个值呢就会被填充到这两个位置大家一定要注意了啊第三个参数呢是起
[08:42] 这个作用然后第四个参数呢大家看看什么就是这个签名后边这两个参数呢咱暂时用不着啊我们看一下这报错是什么错呀啊他要求你必须进行什么呀异常处理那我们就加个try开机就行了呗反正就是一个发送短信对不对这个返回值呢咱要不要都行啊因为我们要加这个什么呀异常处理嘛那我们就给他包起来然后呢就是
[09:17] 对不对我就脱个脸写个exception那如果在这个过程当中抛异常了那我就也打印一句话吧打印到这个控制台上我们也可以便于观察对不对那这个时候我就调用这个什么呀error方法呃这里边我们就写个什么呀就发送失败是不是这肯定是发送失败了呃然后呢这个原因我们要给他
[09:50] 打印出来这个异常信息吧就是ex第二get什么message对就这个样子因为出问题我们也想看看是什么原因造成的大家看一下目前呢我们就把这个什么呀对通过腾讯云发送短信的这一块代码就全部搞定了大家注意一下啊这一块API非常简单其实就是用人家的一个类对吧创建成对象然后调用人家的一个方法这个短信
[10:24] 就发出去啊但是呢在调这个方法的时候呢我们是不是需要啊这些数据对吧这些数据呢你正常情况下应该是给他对配置到这个什么呀阿卜罗上在这呢通过at value注解给他注进来就行了啊所以这是这一块功能但是呢这样呢我要给大家说一说前面咱也提到过了我们说这个腾讯云呢你在进行这个以个人的身份进行申请的时候比如说你想拿到这些数据对不对
[10:52] 然后你在这才可以自己实现这个什么呀发送短线的功能但是以个人申请的时候呢这个很难啊我也测试过了你用个人的身份去去进行这个相关的一些申请的话一般都通不过啊因为他要要求你提交这个提交那个资账我们个人的话一般没有所以说呢这块功能的话啊就是大家该听要听该学习要学习但是你自己在编码实现的时候这个是
[11:22] 搞不定的啊就是说你没有这些数据但是呢我这边是以公司的名义申请的这些数据这些数据大家知道我是不能给大家去用的啊给大家用所以说呢这块你听听就行了然后将来你在测试这个功能的时候我建议你整个这块代码就换成一个控制台输出就是Ctm.Auto.Print就模拟一下就行了啊所以关于这一点呢我在这要给大家强调一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中集成腾讯云短信服务，实现还款通知的发送功能。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了还款通知服务的业务逻辑代码，通过调用 consumerApiAgent 获取借款人手机号，然后调用 smsService 发送短信。
画面 2: 在 IDE 中右键点击项目，准备新建一个 Java 类，用于实现短信服务。
画面 3: 展示了 QCloudSmsServiceImpl 类的骨架，该类实现了 SmsService 接口，用于发送短信。
画面 4: 在腾讯云短信 SDK 文档中查看 Java SDK 的示例代码，用于了解如何使用 SDK 发送短信。
画面 5: 在腾讯云短信控制台中查看申请签名和模板的步骤。
画面 6: 在 QCloudSmsServiceImpl 类中，使用 @Value 注解注入短信服务所需的配置参数（appId, appKey, templateId, sign）。
画面 7: 在 application.yml 配置文件中，配置了短信服务的参数（appId, appKey, templateId, sign）。
画面 8: 在 QCloudSmsServiceImpl 类中，为 sendRepaymentNotify 方法添加了日志记录。
画面 9: 在 QCloudSmsServiceImpl 类中，为 sendRepaymentNotify 方法添加了日志记录，内容为“给手机号 0，发送还款提醒：0 金额：0”。
画面 10: 在 QCloudSmsServiceImpl 类中，为 sendRepaymentNotify 方法添加了短信发送的代码，使用 SmsSingleSender 类。
画面 11: 在 QCloudSmsServiceImpl 类中，为 sendRepaymentNotify 方法添加了 try-catch 块，用于捕获异常。
画面 12: 在 QCloudSmsServiceImpl 类中，为 sendRepaymentNotify 方法添加了异常处理，记录错误日志。
画面 13: 在 QCloudSmsServiceImpl 类中，为 sendRepaymentNotify 方法添加了异常处理，记录错误日志。
画面 14: 在 QCloudSmsServiceImpl 类中，为 sendRepaymentNotify 方法添加了异常处理，记录错误日志。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面 1:
```java
@Autowired
private SmsService smsService;

@Override
public void sendRepaymentNotify(String date) {
    //查询到期还款计划
    List<RepaymentPlan> repaymentPlanList = selectDueRepayment(date);
    //遍历还款计划
    repaymentPlanList.forEach(repaymentPlan -> {
        RestResponse<BorrowerDTO> consumerResponse = consumerApiAgent
                .getBorrowerMobile(repaymentPlan.getContractId());
        if (consumerResponse.isSuccessful()) {
            //用到借款人手机号
            String mobile = consumerResponse.getResult().getMobile();
            //发送还款提醒
            smsService.sendRepaymentNotify(mobile, date,
                    repaymentPlan.getAmount());
        }
    });
}
```

画面 2:
无直接代码，但展示了 IDE 中的菜单选项。

画面 3:
```java
package cn.itcast.wanxing2p.repayment.sms;

import java.math.BigDecimal;

public class QCloudSmsServiceImpl implements SmsService {

    @Override
    public void sendRepaymentNotify(String mobile, String date, BigDecimal amount) {

    }
}
```

画面 4:
```java
import com.github.qcloudsms.SmsSingleSender;
import com.github.qcloudsms.SmsSingleSenderResult;
import com.github.qcloudsms.SmsSingleSenderException;
import org.json.JSONException;
import java.io.IOException;
import java.util.String[] params = {"5678"};
SmsSingleSender sender = new SmsSingleSender(appId, appKey);
SmsSingleSenderResult result = sender.sendWithParam("86", phoneNumber[0], templateId, params, sign, extend, ext);
System.out.println(result, smsSign, "");
```

画面 5:
无直接代码，但展示了腾讯云短信控制台的界面。

画面 6:
```java
@Service
@Qualifier("sms")
public class QCloudSmsServiceImpl implements SmsService {

    @Value("${sms.qcloud.appId}")
    private int appId;

    @Value("${sms.qcloud.appKey}")
    private String appKey;

    @Value("${sms.qcloud.templateId}")
    private int templateId;

    @Value("${sms.qcloud.sign}")
    private String sign;
```

画面 7:
```yaml
sms:
  qcloud:
    appId: 1234567890
    appKey: abcdefghijklmnopqrstuvwxyz
    templateId: 123456
    sign: "还款提醒"
```

画面 8:
```java
@Override
public void sendRepaymentNotify(String mobile, String date, BigDecimal amount) {
    log.info("给手机号 0，发送还款提醒：0 金额：0", mobile, date, amount);
}
```

画面 9:
```java
@Override
public void sendRepaymentNotify(String mobile, String date, BigDecimal amount) {
    Log.info("给手机号 0，发送还款提醒：0 金额：0", mobile, date, amount);
}
```

画面 10:
```java
@Override
public void sendRepaymentNotify(String mobile, String date, BigDecimal amount) {
    Log.info("给手机号 0，发送还款提醒：0 金额：0", mobile, date, amount);
    SmsSingleSender sender = new SmsSingleSender(appId, appKey);
```

画面 11:
```java
@Override
public void sendRepaymentNotify(String mobile, String date, BigDecimal amount) {
    Log.info("给手机号 0，发送还款提醒：0 金额：0", mobile, date, amount);
    SmsSingleSender sender = new SmsSingleSender(appId, appKey);
    try {
        SmsSingleSenderResult result = sender.sendWithParam("86", mobile, templateId, new String[]{date, amount.toString()}, sign, extend, ext);
    } catch (Exception e) {
```

画面 12:
```java
@Override
public void sendRepaymentNotify(String mobile, String date, BigDecimal amount) {
    Log.info("给手机号 0，发送还款提醒：0 金额：0", mobile, date, amount);
    SmsSingleSender sender = new SmsSingleSender(appId, appKey);
    try {
        SmsSingleSenderResult result = sender.sendWithParam("86", mobile, templateId, new String[]{date, amount.toString()}, sign, extend, ext);
    } catch (Exception e) {
        log.error("发送失败", 0, e.getMessage());
    }
}
```

画面 13:
```java
@Override
public void sendRepaymentNotify(String mobile, String date, BigDecimal amount) {
    Log.info("给手机号 0，发送还款提醒：0 金额：0", mobile, date, amount);
    SmsSingleSender sender = new SmsSingleSender(appId, appKey);
    try {
        SmsSingleSenderResult result = sender.sendWithParam("86", mobile, templateId, new String[]{date, amount.toString()}, sign, extend, ext);
    } catch (Exception e) {
        log.error("发送失败", 0, e.getMessage());
    }
}
```

画面 14:
```java
@Override
public void sendRepaymentNotify(String mobile, String date, BigDecimal amount) {
    Log.info("给手机号 0，发送还款提醒：0 金额：0", mobile, date, amount);
    SmsSingleSender sender = new SmsSingleSender(appId, appKey);
    try {
        SmsSingleSenderResult result = sender.sendWithParam("86", mobile, templateId, new String[]{date, amount.toString()}, sign, extend, ext);
    } catch (Exception e) {
        log.error("发送失败", 0, e.getMessage());
    }
}
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 5: 展示了腾讯云短信控制台的“快速入门”页面，包含两个步骤：
步骤 1: 申请签名与短信正文模板
步骤 2: 等待短信签名与短信正文模板审核

5) 无其他内容。

