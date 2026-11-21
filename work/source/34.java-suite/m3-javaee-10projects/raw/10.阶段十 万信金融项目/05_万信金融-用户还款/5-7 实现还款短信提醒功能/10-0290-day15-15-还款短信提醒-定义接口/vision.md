# 画面线理解：day15-15-还款短信提醒-定义接口

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-7 实现还款短信提醒功能
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-7 实现还款短信提醒功能\day15-15-还款短信提醒-定义接口_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:25, 01:04, 01:26, 01:52, 02:15, 02:21, 02:31, 02:43, 03:40, 03:56, 04:11, 04:35, 04:49, 05:11
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:39:23

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
    <groupId>org.apache.rocketmq</groupId>
    <artifactId>rocketmq-spring-boot-starter</artifactId>
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
