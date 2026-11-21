# 画面线理解：day15-20-定时还款短信提醒

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-7 实现还款短信提醒功能
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-7 实现还款短信提醒功能\day15-20-定时还款短信提醒_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:39, 02:56, 03:37, 06:19, 09:44, 10:36, 11:53, 12:23, 12:39, 12:58, 13:19, 13:45, 14:03, 14:39
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:42:49

1) 这一组画面整体在讲如何使用 Elastic-job 实现分布式定时还款任务，包括依赖引入、分片逻辑、业务执行和短信通知等环节。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程目录结构，当前章节为“7.2 功能实现”，并显示了 Elastic-job 的 Maven 依赖配置。
画面2：展示还款计划 Mapper 接口，其中包含两个 SQL 查询语句，用于根据日期和状态分片查询还款计划。
画面3：展示 RepaymentJob 类的 execute 方法，开始执行还款业务。
画面4：在 execute 方法中添加注释“//用业务层执行还款任务”，并调用 repaymentService.executeRepayment 方法。
画面5：在 execute 方法中添加注释“//用业务层执行还款短信通知”，并调用 repaymentService.sendRepaymentNotify 方法。
画面6：展示数据库中还款计划表的数据，包含项目ID、期数、金额、应还日期等字段。
画面7：展示 RepaymentJob 类的 execute 方法，其中调用 sendRepaymentNotify 方法。
画面8：展示服务启动日志，包括 Spring Boot 启动、Tomcat 初始化等信息。
画面9：展示服务启动日志，包括 Quartz Scheduler 初始化、JobStore 配置等信息。
画面10：展示服务启动日志，包括服务端点暴露、线程池配置等信息。
画面11：展示服务启动日志，包括短信通知发送成功的信息。
画面12：展示服务启动日志，包括短信通知发送成功的信息。
画面13：展示服务启动日志，包括 SQL 执行和短信通知发送成功的信息。
画面14：展示 sendRepaymentNotify 方法的实现，其中调用 SmsSingleSender 发送短信。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```xml
<dependency>
    <groupId>com.dangdang</groupId>
    <artifactId>elastic-job-lite-spring</artifactId>
    <version>2.1.5</version>
</dependency>
```

画面2：
```java
@Select("SELECT * FROM repayment_plan WHERE DATE_FORMAT(SHOULD_REPAYMENT_DATE, '%Y-%m-%d') = #{date} AND repayment_status = 0")
List<RepaymentPlan> selectRepaymentPlanByDate(String date);

@Select("SELECT * FROM repayment_plan WHERE DATE_FORMAT(SHOULD_REPAYMENT_DATE, '%Y-%m-%d') = #{date} AND repayment_status = 0")
List<RepaymentPlan> selectRepaymentPlanList(String date, @Param("shardingCount") int count, @Param("shardingIndex") int shardingIndex);
```

画面3：
```java
import java.time.format.DateTimeFormatter;

@Component
public class RepaymentJob implements SimpleJob {

    @Autowired
    private RepaymentService repaymentService;

    @Override
    public void execute(ShardingContext shardingContext) {
        //用业务层执行还款任务
        repaymentService.executeRepayment(LocalDate.now().format(DateTimeFormatter.ISO_LOCAL_DATE), shardingContext.getShardingTotalCount());
    }
}
```

画面4：
```java
//用业务层执行还款任务
repaymentService.executeRepayment(LocalDate.now().format(DateTimeFormatter.ISO_LOCAL_DATE), shardingContext.getShardingTotalCount());
```

画面5：
```java
//用业务层执行还款短信通知
repaymentService.sendRepaymentNotify(LocalDate.now().plusDays(1).format(DateTimeFormatter.ISO_LOCAL_DATE));
```

画面6：
无代码或配置，仅展示数据库表数据。

画面7：
```java
//用业务层执行还款短信通知
repaymentService.sendRepaymentNotify(LocalDate.now().plusDays(1).format(DateTimeFormatter.ISO_LOCAL_DATE));
```

画面8：
无代码或配置，仅展示服务启动日志。

画面9：
无代码或配置，仅展示服务启动日志。

画面10：
无代码或配置，仅展示服务启动日志。

画面11：
无代码或配置，仅展示服务启动日志。

画面12：
无代码或配置，仅展示服务启动日志。

画面13：
无代码或配置，仅展示服务启动日志。

画面14：
```java
@Value("${sms.qcloud.sign}")
private String sign;

@Override
public void sendRepaymentNotify(String mobile, String date, BigDecimal amount) {
    log.info("给手机号{}，发送还款提醒，0.金额：{}，日期：{}，金额：{}", mobile, amount, date, amount);
    SmsSingleSender sender = new SmsSingleSender(appId, appKey);
    try {
        sender.sendWithParam(nationCode, "86", mobile, templateId, new String[]{date, amount.toString()}, sign, extend, "");
    } catch (Exception ex) {
        log.error("发送失败：{}，{}", ex.getMessage());
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无 PPT 标题、架构图/流程图或表格数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
