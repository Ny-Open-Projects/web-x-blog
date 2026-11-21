# 画面线理解：day15-18-还款短信提醒-发送还款短信-功能实现

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-7 实现还款短信提醒功能
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-7 实现还款短信提醒功能\day15-18-还款短信提醒-发送还款短信-功能实现_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:56, 01:28, 02:13, 03:08, 03:53, 04:26, 04:55, 05:59, 08:10, 09:19, 10:10, 10:52, 11:45
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:41:31

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
