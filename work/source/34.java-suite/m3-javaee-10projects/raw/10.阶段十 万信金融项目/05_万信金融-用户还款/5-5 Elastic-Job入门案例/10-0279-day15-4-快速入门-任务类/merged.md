# day15-4-快速入门-任务类

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-5 Elastic-Job入门案例
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-5 Elastic-Job入门案例\day15-4-快速入门-任务类_【海量资源尽在 666java.com】.mp4
- 时长 10分59秒（音频 659s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们把快速入门案例当中的数据访问层给编写完了大家注意一下这里边其实就是一个什么呀就是一个查询但是呢这里边我们设置了一个什么呀分片的一个规则了对不对就是根据ID的余数啊来进行了一个平均分配那么这里边大家一定要注意我们用到一个函数叫MOD那么这个小五号你一定要注意这个小五号呢我刚才是放到这了啊
[00:29] 放到最后可不对啊小果号应该是在等号前这个细节呢是你要注意一下的那咱数据访问层写完之后是不是就意味着我们就可以查询数据了对吧那谁去调用数据访问层去查询这个数据呢我们以前是不是都是业务层对吧业务层调用数据访问层那我们现在也可以去干什么呀由业务层去调用数据访问层但是咱这个业务太简单了
[00:54] 就是一个查询所以说呢咱就把业务层给省掉省掉之后呢我们谁去调这个数据访问层呢我们要编写一个elastic-job的什么类啊叫任务类注意了任务类啊我们现在这个是不是要实现一个定时任务吗对吧每隔多少时间去查一下表里边的数据所以我们需要一个任务类啊这是elastic-job这个框架吧它的一个要求而且呢我们在定义这个任务类的时候你看一下
[01:25] 他要求必须实现一个接口叫simple什么叫然后重写他里边的一个方法叫execute那将来你注意了将来我们需要把什么调用Mapper接口查询数据的这个代码要放到哪个方案里边对execute方案里边这就是我们要执行的这个什么呀定时任务那么你实现了这个接口重写了这个方法之后将来将来
[01:53] 由elastic杠叫吧这个框架会去自动调用这个什么呀is cute方法然后通过map接口进行数据的一个查询所以我们这就是说就是按照人家要求你就实现哪个接口啊重新哪个方法把我们要完成的这个任务对吧给他扔到这个方案里上就OK了所以咱接下来呢一起把这个任务类呢给他编写一下
[02:19] 好咱们回到i地里边我们找到一个包叫叫不包啊我们准备把这个任何类呢放到这个叫包里面我们新建一个类这个类的名字呢我们要跟讲义保持一致叫my叫吧啊然后咱加个注尸吧我们说这是干嘛的呀这个类是不是数据查询任务吗对不对数据数据查询
[02:48] 任务啊要在这个类里边完成这个类呢不能你想怎么着就怎么着我们刚才说了必须实现这个谁啊对elastic杠叫报的一个接口叫simple jobs i m p l e g o bsimple job大家看好啊这个包别引错了然后呢实现了这个接口之后他就报错了因为我们是不是要重写他里边的一个方法是不是刚才大家看到叫什么呀
[03:16] 对exclude的方法我们把它给生成一下是不是exclude对吧生成了然后它就不报错了然后这个类的上面呢我们还要加上一个注解那咱接下来就重点看一下这个exclude方法那这个方法大家看没有返回值但是有一个什么呀参数叫sharding context是不是一个上下文对象上下文对象结合咱以往的经验上下文对象一般是不是通过它来取一些什么呀
[03:49] 一些数据的是这意思吧那我们通过这个shouting context我们能拿到什么数据呢那能拿到什么数据呢咱一会儿再说啊编写纳门的时候再说那我把这个方法呢先加一个注释吧我们这个方法就是具体来干什么呀执行定时任务我们的定时任务就是要查询某个表里边的数据当然你要查询数据是不是得通过这个什么呀Mapper接口对不对那因此呢我们一定是要在
[04:20] 我们的任务类当中把这个MapperJetro给他干什么对注入进来先把这个准备工作搞定了是吧这个注进来注进来之后我们是不是就应该需要在Excel的方案里边干什么Down UserMapper然后点咱是不是就那一个方法对吧Query UserByID然后大家看看这个方案是不是要两个参数一个是分片总数一个是什么分片项对不对就是哪来服务器这两个值我从哪去是不是哪值从哪来
[04:54] 你比如这个分片总数分片总数在哪放下来分片总数是不是在那个什么配置文件里是他不是我现在就就想要这个值怎么样有同学老师你用at value啥的把它注进来对吧你在这能用可以你说的也可以但是呢我们这呢不准备用这种方法为啥呢因为一会儿呢我们的elastic-job会有一个配置类会有个配置类专门搞配置了我们会把配置文件里边这些值给它放到那个配置类里边
[05:27] 那你放到配置类里边之后呢我这想要怎么办呢哎你就通过这个参数sharding context那么elastic-job呢他会把跟这个配置相关的一些数据呢放到这个sharding-context这个参数里边你想要什么数据从这里边取就可以了你比如说我们写一下我们就可以从这里边取出来什么呀对取出来分片总数他提供的有方法啊你看sharding
[05:56] text. 你觉得是哪个应该看名字是这个吧sharding total content对不对我给它存到一个变量里那我们还可以得到什么呀分片项得到分片分片是吧然后呢这个也是有现成的方法大家看你觉得应该是谁呢分片项应该叫get a sharding item
[06:34] 好然后我也给他存起来ititm大家看一下啊我们需要的分片总数以及分片项的全是从这里边来的那这里边的数据从哪来这里边的数据是由对elastic job啊这个框架存进去了那他存的这些数据从哪来呢我们将来啊这个代码还没写到我们将来呢会把配用件里边这些值注入给他的这个什么呀配置类明白吧注到配置类里面所以他就导荡这些数据
[07:05] 得到这些数据之后呢它会存到这个山下文环境里边那我们就可以从山下文里边是不是取到这些数据它们之间内部啊是大概这么一个关系那么大家看一下我现在有了分片总数有了分片项之后我接下来是就可以调用这个什么呀Mapper接口的这个Query方法然后呢第一个参数是不是就是Count第二个参数就是这个什么呀对分片项你注意分片项指的就是哪一台服务器
[07:32] 那这儿得到的是不是就是当前的这个这台服务器就是当前哪台服务器正在执行这个定时任务这个atom就是谁啊就是谁这个一定要注意然后呢查询的时候它返回来是不是一个集合对吧然后呢我们起一个名字就叫user list那这儿呢其实就是在干什么呀查询数据而且你一定要注意我们这个查询是分片查询啊你看我们是不是把这个分片总数啊以分片项
[08:09] 是作为参数传进来传进来之后你看这个总数这个值是不是就放到这儿了那个分片项当前那个服务器的编号是不是就放到这儿了对不对我们是做了这个分工分片的这是我们最终想要的一个效果那到底有没有分工分片我是不是得看一下这个效果呀对不对所以我们就是接下来就是要输出结果到空气台我让你瞅一眼嘛对不对看这个效果是是不是我们想要的那个效果那这个呢我是不是得便利这个集合呀
[08:41] 便利这个集合对便利这个集合那我们输出点啥呢为了让大家能看到这个分片的效果呀我需要把这个分片项给你打印出来分片项你就写个什么呀作业分片冒号然后把谁给打印出来呀item这个值
[09:09] 因为我说了item这个值是不是相当于是这个服务器的编号吗对不对我得能让你看出来每台服务器都查了哪些数据对不对我们看这个编号就能区分这些服务器那我怎么看出来每台服务器它查的是哪些数据呢数据不就是这个集合里边这个一个user对象了对不对我们把它呢也打印一下不就完了吗我中间用这个箭头分割一下你打印这个谁呀user不就完了大家看是不是对不对将来呢我一观察控制台就能看出来
[09:42] 作业分片0他查了哪些数据对吧分片1查了哪些数据分片2又查了哪些数据这是不是我们一观察控制台是不是就一幕亮了对不对所以说这就是我们把什么给编写好了对elastic-job的什么类对这是一个任务类任务类就是我们具体要完成的定时任务你这个代码应该写到is cute这个方法里
[10:11] 当然呢我们不同的业务这里边写的代码应该肯定是什么呀不一样的那有的同学会说那老师你这个写完之后我感觉是不是就完事了吗你看这都已经开始进行查询了吗那这个例子是不是就写完了没有啊没有了这个方案刚才说谁去调用啊是不是没人调用的话你这个代码写到这儿那不是还是白搭吗所以说我们接下来还有两个配置类要搞一个是zookeeperzookeeper你可不敢把它忘了我们说ZooKeeper是不是这个什么呀
[10:40] 对微服务的注册中心嘛这个组k帕还有配置我们没搞然后就是elastic job资深也有配置还没没搞啊这两块配置咱搞定之后呢他将来会自动去调用这个方法来触发这个什么样任务的执行啊这是目前吧任务类咱就搞到这儿

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

