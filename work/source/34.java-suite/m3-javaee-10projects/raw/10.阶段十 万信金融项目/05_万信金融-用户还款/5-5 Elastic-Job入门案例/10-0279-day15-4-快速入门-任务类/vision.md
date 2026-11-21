# 画面线理解：day15-4-快速入门-任务类

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-5 Elastic-Job入门案例
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-5 Elastic-Job入门案例\day15-4-快速入门-任务类_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:02, 01:59, 02:36, 03:26, 04:25, 05:06, 06:00, 06:31, 07:13, 07:45, 08:19, 09:55, 10:18, 10:54
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:31:15

1) 这一组画面整体在讲如何在 Spring Boot 项目中使用 Elastic-Job 实现分片任务，通过注解和 ShardingContext 获取分片参数并调用数据访问层查询数据。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了数据访问层的 UserMapper 接口定义，其中包含一个通过 MOD 分片的 SQL 查询方法。
画面2: 展示了 Elastic-job 任务类 MyJob 的定义，包含 @Component 注解和 @Autowired 注解的 userMapper 字段。
画面3: 展示了 IntelliJ IDEA 中项目结构，当前选中 MyJob.java 文件。
画面4: 展示了 MyJob.java 文件的顶部导入语句，包括 ShardingContext 和 SimpleJob 等 Elastic-Job 相关类。
画面5: 展示了 MyJob.java 文件中 @Component 和 @Autowired 注解的使用。
画面6: 展示了 MyJob.java 文件中 userMapper 字段的定义。
画面7: 展示了 ShardingContext 类的成员方法列表，光标位于 getShardingTotalCount() 方法上。
画面8: 展示了 ShardingContext 类的成员方法列表，光标位于 getShardingTotalCount() 方法上。
画面9: 展示了 MyJob.java 文件中获取分片总数和分片项的代码。
画面10: 展示了 MyJob.java 文件中调用 userMapper.queryUserById 方法的代码。
画面11: 展示了 MyJob.java 文件中调用 userMapper.queryUserById 方法的代码。
画面12: 展示了 MyJob.java 文件中使用 forEach 遍历查询结果并打印输出的代码。
画面13: 展示了 MyJob.java 文件中使用 forEach 遍历查询结果并打印输出的代码。
画面14: 展示了 MyJob.java 文件中使用 forEach 遍历查询结果并打印输出的代码。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1:
```java
private String password;
@TableField("NAME")
private String name;
@TableField("AGE")
private Integer age;
```

画面1:
```java
public interface UserMapper extends BaseMapper<User> {
    //对id通过mod取模来进行分片
    @Select("SELECT * FROM `tb_user` WHERE MOD(id,#{shardingTotalCount})=#{shardingItem}")
    List<User> queryUserById(@Param("shardingTotalCount") int count,
                             @Param("shardingItem") int item);
}
```

画面2:
```java
/**
 * 数据查询任务
 */
@Component
public class MyJob implements SimpleJob {
    @Autowired
    private UserMapper userMapper;
    //执行定时任务
    @Override
    public void execute(ShardingContext shardingContext) {
    }
}
```

画面4:
```java
import com.dangdang.ddframe.job.api.ShardingContext;
import com.dangdang.ddframe.job.api.simple.SimpleJob;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
```

画面6:
```java
@Autowired
private UserMapper userMapper;
```

画面9:
```java
int count = shardingContext.getShardingTotalCount();
int item = shardingContext.getShardingItem();
```

画面10:
```java
List<User> userList = userMapper.queryUserById(count, item);
```

画面12:
```java
userList.forEach(user -> {
    System.out.println("作业分片：" + item + "-->" + user);
});
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无

5) 不要评价画面美观，不要输出与课程无关的内容。
无
