# 画面线理解：day15-11-定时还款任务-任务类

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-6 实现定时还款任务
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-6 实现定时还款任务\day15-11-定时还款任务-任务类_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:22, 00:39, 00:44, 01:16, 01:30, 01:50, 02:13, 02:54, 03:12, 03:55, 04:09, 05:28, 06:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:36:50

1) 这一组画面整体在讲如何修改业务层代码并创建定时任务来处理到期还款计划。

2) 按时间顺序列出每张画面的要点：
画面1: 修改 RepaymentService.java 中的 selectDueRepayment 方法，添加分片参数。
画面2: 继续修改 RepaymentService.java，方法签名保持不变。
画面3: 在 RepaymentService.java 中添加 executeRepayment 方法，用于执行还款逻辑。
画面4: 新建 RepaymentJob 类，实现 SimpleJob 接口，用于定时任务。
画面5: 在 IDEA 中查看项目结构，定位到 RepaymentService.java 文件。
画面6: 在 IDEA 中查看项目结构，定位到 RepaymentService.java 文件。
画面7: 在 IDEA 中创建 RepaymentJob.java 文件，准备编写定时任务代码。
画面8: 在 IDEA 中为 RepaymentJob.java 导入必要的依赖包。
画面9: 在 IDEA 中为 RepaymentJob.java 导入 ShardingContext 和 SimpleJob 包。
画面10: 在 IDEA 中为 RepaymentJob.java 导入 RepaymentService 和 ShardingContext 包。
画面11: 在 IDEA 中为 RepaymentJob.java 添加 @Autowired 注解注入 RepaymentService。
画面12: 在 IDEA 中为 RepaymentJob.java 调用 repaymentService.executeRepayment 方法。
画面13: 在 IDEA 中为 RepaymentJob.java 调用 repaymentService.executeRepayment 方法，传入参数。
画面14: 在 IDEA 中为 RepaymentJob.java 完成 execute 方法，调用 repaymentService.executeRepayment 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```java
@Select("SELECT * FROM repayment_plan WHERE DATE_FORMAT(SHOULD_REPAYMENT_DATE, 'yyyy-mm-dd') = #{date} AND REPAYMENT_STATUS = '0' AND MOD(number_of_periods, #shardingCount) = #shardingItem")
List<RepaymentPlan> selectDueRepayment(@Param("date") String date, @Param("shardingCount") int shardingCount, @Param("shardingItem") int shardingItem);
```

画面3:
```java
void executeRepayment(String date, int shardingCount, int shardingItem)
```

画面4:
```java
@Component
public class RepaymentJob implements SimpleJob {

    @Autowired
    private RepaymentService repaymentService;

    @Override
    public void execute(ShardingContext shardingContext) {
        //调用业务层执行任务
        repaymentService.executeRepayment(LocalDate.now().format(DateTimeFormatter.ISO_LOCAL_DATE), shardingContext.getShardingTotalCount(), shardingContext.getShardingItem());
    }
}
```

画面5:
```java
repaymentDetail.setRepaymentPlanId(repaymentPlan.getId());
repaymentDetail.setAmount(repaymentPlan.getAmount());
repaymentDetail.setRepaymentTime(LocalDateTime.now());
repaymentDetail.setRequestId(CodeUtil.genWeCodePrefixCode.CODE_REQUEST_PREFIX);
repaymentDetail.setStatus(StatusCode.STATUS_OUT.getCode());
repaymentDetailMapper.insert(repaymentDetail);
return repaymentDetail;
```

画面10:
```java
import cn.itcast.wanxingzp.repayment.service.RepaymentService;
import com.dangdang.ddframe.job.api.ShardingContext;
import com.dangdang.ddframe.job.api.simple.SimpleJob;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
```

画面11:
```java
@Autowired
private RepaymentService repaymentService;
```

画面12:
```java
repaymentService.executeRepayment(LocalDate.now().format(DateTimeFormatter.ISO_LOCAL_DATE), shardingContext.getShardingTotalCount(), shardingContext.getShardingItem());
```

画面13:
```java
String date, int shardingCount, int shardingItem
```

画面14:
```java
@Override
public void execute(ShardingContext shardingContext) {
    repaymentService.executeRepayment(LocalDate.now().format(DateTimeFormatter.ISO_LOCAL_DATE), shardingContext.getShardingTotalCount(), shardingContext.getShardingItem());
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无

5) 不要评价画面美观，不要输出与课程无关的内容。
无
