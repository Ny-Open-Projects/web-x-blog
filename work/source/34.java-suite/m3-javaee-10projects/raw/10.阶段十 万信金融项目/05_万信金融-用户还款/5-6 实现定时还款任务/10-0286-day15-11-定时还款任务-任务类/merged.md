# day15-11-定时还款任务-任务类

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-6 实现定时还款任务
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-6 实现定时还款任务\day15-11-定时还款任务-任务类_【海量资源尽在 666java.com】.mp4
- 时长 6分22秒（音频 382s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们把定时还款任务当中的数据访问层以及要层这些代码呢该修改的都已经修改过了那修改过之后呢那这就有个问题呢这块代码谁去触发它运行呢我们之前是怎么做我们之前是不是去访问control了control了去调用要层要层去调用什么呀数据访问层然后这个功能就执行了对不对那现在呢
[00:28] 现在肯定不是这么走现在我们是不是应该把它做成一个什么定时任务对不对由系统到了指定时间自动就干什么运行所以说接下来我们要编写一个任务类ElasticJob的什么任务类不知道大家还有没有印象在入门案例当中我们也编写过这么一个任务类就是自定义一个类让它实现哪个接口
[00:54] simple job这个接口并重写里边的is cute方法然后在这个方法里边呢去调用什么呀药草然后就触发这个呃代码的这个运行对不对所以咱接下来的话看看咱有没有这个job包啊咱们找一找这个repayment这个微服是不是这里边应该没有这个job包咱新建一个吧点右键啊新建一个包叫go
[01:25] 然后呢我们找一找这个包包嘞在这对吧我们新建一个任务类名字叫repayment叫吧稍等一下然后呢他一定要实现啊elastic job的一个接口叫什么呀对叫simple jobs a m p l esimple jobs i m
[02:13] 然后呢我们看应该是这个对不对然后他报错是因为我们是不是要重写他里边的什么呀对一个叫eat cute的一个什么呀的一个方法我们把这个方法呢给他生成是q的然后呢在这个类的上面呢我们要加上component这个助理那接下来我们主要的任务就是编写eat cute的这个方法我们刚才说了在这个方法里边是不是要去调用什么呀业务层然后由业务层去调用数据房子
[02:48] 所以在这里边呢我们需要把右层给它注进来privaterepaymentservice好然后呢我们在这儿是不是就可以进行调用了对不对怎么调用啊那就直接点呗我们要调哪个方法我们要调用这个iscuterepayment这个方法这个方法咱原来不是一个参数吗就这个日期吗咱刚刚不是都给它改成几个参数呀对三个参数所以说我们要调用这个iscuterepayment
[03:28] 这个方法然后传进去三个参数那第一个日期一定是当前日期对不对是不是当前日期啊那后边这两个参数怎么来这个分片总数啊以及一个分片项这两只从哪这两只是不是从这个参数里边就是上下玩对象有印象吧对所以说咱接下来把这个代码写一下Qt呃第一个值当前时间我们怎么得到啊当前时间我们用这个Local啊Local date
[03:59] 第二什么呀闹这个方法就得到那些时间但是呢我们需要对它进行格式化我们来一个格式化怎么格式化呢这里边呢有一个静态的一个值叫data哎呀我们看看啊就第一个取之吧iso local data就用它就行这个iso local data其实指的是一种格式就是年月日啊中间用什么呀用杠来分割的那种格式也是咱最常用的啊
[04:35] 咱之前是不是呃很早的时候是不是要自己拗一个什么simple data format然后里边是不是什么四个y两个mm然后一个d两个dd是不是啊我们现在呢呃不用那么麻烦了我们可以用这些类啊或者这些常见的一些值这这块一片呢是gdk8啊gdk8新增的一些一片这是需要大家注意的这是第一个参数对吧第二个参数呢我们要给的就是这个谁呀
[05:05] 我看这个大果号小果号配对这应该没错吧这是第一个参数然后第二个参数是不是从这个sharding context这个上下文里边取出来这个什么呀对这个分片总数然后再来一个这次我们要取的应该是谁呀是不是那个分片项对吧应该调到哪个方法叫get a sharding item搞定了是不是
[05:40] 这就搞定了啊其实在XQ的方案里边就这么简单我们只需要把业务层注进来然后调用他的XQ的repayment的方法他要三个参数我就传给他什么呀三个参数就行了那将来的话啊这个业务层的代码其实就是在这进行出发然后呢他再去调用数据扫案子那这个任务类啊我们就编写到
[06:03] 这里了后边的话我们是不是还要增加一些配置类组k帕的elastic job的对不对这两块配置我们加上之后呢这个方案是不是就会自动被被谁啊自动被elastic job去调用然后就触发这个功能的自动运行

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
import cn.itcast.wanxingzp.repayment.Service.RepaymentService;
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

