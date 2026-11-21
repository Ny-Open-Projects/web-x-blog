# 7.22 项目实战 - 查询Druid列表

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.22 项目实战 - 查询Druid列表_【海量资源尽在 666java.com】.mp4
- 时长 13分21秒（音频 802s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面我们来开发我们这个DroidService的一个开发然后呢这个DroidService会用到我们的DroidHelper也就是说我们Droid的这个连接环连接数据库连接来开发我们这个Service那首先我们建一个package这个package实际上就是Service那么这个Service里边我们会建一个这种这种我们的这个叫Droid
[00:35] 这个jade Service其实是个interface而这个jade Service的interface我们需要给它添加什么样的一个方法呢第一个来讲的话我们需要查询jade数据列表第二个是我们需要查询数据列表那第二个来讲的话我们需要查询我们的这个查询
[01:08] 查询最近的10条温湿度数据温度或者是湿度的一个数据最近的10条的那么第一个方法来讲的话我们可以把它写成我们的叫返回一个R这个R的话就是一个返回的一个格式那么我们query
[01:41] GridListGridList 其实就是atRequestPyramidMap这个map是个stream和object也把前台传过来的参数传进去这是一个那另外一块的话我们也是直接查询我们的温湿度这个实际上是我们查询我们Grid
[02:35] 温度和湿度的一个那我们做好了我们的这个叫Service那下一个的话我们再添加一个package这个package那这个package我们需要创建我们的这个class而这个class呢我们需要就是dread Service rmpr而这个dread Service rmpr我们需要把它
[03:04] 继承我们的实现我们的一个implement我们的JIT Service实现JIT Service就需要把这两个方法给它实现出来override具体实现的方法下一步的话我们就来看看我们如何用GDPC来实现我们的方法第一个我们要查询我们的温湿度查询我们JIT的一个列表整个的列表整个列表来讲的话我们
[03:42] 我们可以看到我们的这个我们的这个数据对吧就数据的话我们是select啊行from all device message然后limit 10啊我们假设把它作为我们的一个string那下一步的话其实就是要执行这个查询然后呢查询这个circle一句对吧我们dread我们刚才就开发了我们的dread的help对吧help我们等于newdread help
[04:28] 那我们要定义一个connection,connection,然后是Java Circle的这个connection,它等于什么呢?
[04:53] 等于成功,然后呢,statement,statement,然后st,我们Circle里边的,Java Circle里边的statement,那第三个来讲的话是result set,那么我们下边就开发我们的查询,那第一个来讲的话,
[05:38] 我们查询的结果是一个什么呢我们查询结果其实大家可以看到我们这个查询查询是一个我们根据我们的message entity它的一个实体的一个列表所以说它第一个来讲的话我们返回的其实是一个list而这个list是一个message entitymessage entity result那么我们想要
[06:20] 把connection,想要得到connection,connected等于什么呢?
[06:27] harper.getconnection,对吧?
[06:30] 我们此时就得到了我们GDPC的connection,那么st呢?
[06:35] 我们这个st实际上就是statement,statement等于我们这个connection,它创建一个statement,对吧?
[06:45] 这个能创建得了,然后我们的这个rs呢,就是result set,等于什么呢?
[06:51] 等于我们的这个叫st.执行queryserve, 也就是serve都可以此时我们就拿到了我们的这个执行了一个查询和我们GTPC数据库查询是类似的对吧那么我们要再循环我们的next循环next循环next等于什么呢什么我们要创建一个message entity
[07:33] 这个intity是message-intity等于我们要把IS转换成IS to intitit这个时候其实是IS也就是说我们因为我们查询到的实际上是一行一行的记录对吧这一行一行的记录我要把一行一行的记录要转换成我们这个message-intity那么我们message-intit就是result-list里边我们要
[08:07] 我们先把整体的结构给它写好这个时候我们就可以设置我们的这个返回值了map.trim.object然后我们那个map呢等于new rcmap然后此时我们map就put这个呢是取决于我们返回的我们前台要求的一个返回值
[08:57] OK这个时候我们就可以return rd ok然后把map放进去到最后的时候我们finally我们要把helper.closeconnection.it.rs那现在的话我们把我们的整体结构开发完了但是这中间有一个转化那个过程
[09:37] 这个转换的过程就是RS to Entity这个我们还没开发我们需要来开发一个RS to EntityRS to Entity的话它这个转换其实也比较简单一点那其实就是我们的这个RS to Entity那么它的一个结果其实是一个叫MessageMessage Entity对吧然后RS to Entity然后这个说是一个ResultSet此时
[10:11] 我把result set 我 return 一个那我 return 什么呢我其实是一个 message.inti new message.inti那我最终的事是返回 message.inti那只不过是我返回这个 message.inti 的时候我要对我的数值进行转换message.inti 里边它有很多嘛对不对我set metacode metaname那么等于什么呢等于 rs.get string
[10:48] 这里面其实就是meta name那么这个时候我看看要serve我们的一个exception那么也就是说我在这个过程中我们把我们的rs把我们的一条返回结果的一个返回结果那么返回结果的时候包含了各个字段我把各个字段设置我们的message entity
[11:20] 同样道理我们也可以设置message.entity的一个setMeterID等于is.getString然后这里边是一个meta同样道理我们把所有的我们的message.entity这个实体对象我们找到这个实体对象就可以在实体对象里边实体对象的所有的这些我们都可以拿过来用了
[11:59] 这个时候我们就能够后边的我不写了那么在这个过程中我们就能够开发完了我们这个Service而这个Service其实是我们要查询我们的这个叫查询我们的执行这个sales水据这个sales水据就是select我们的all device message那么它得到了一个我们想要的一个结果而这个结果其实我们可以看一下我们最终的一个实现的一个效果
[12:31] 就是我们要拿到的item对吧因为我刚才说是返回的是一个啊RDR返回的是IDLOK对吧IDLOK那是在默认的时候IDLOK就只值得包含的就是message等于successcode等于0然后呢因为我们要加的是一个item而这个item它里边是包含了我们的每一条记录一条记录里边的所有字段
[13:10] 这个时候我们就把我们的这个数据啊把我们的querydreadlist也就是查询查询我们的这个列表啊给开发完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中编写一个 Druid 数据库连接池的工具类和对应的 Service 层代码，实现对数据库的查询操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 DruidHelper 类的源码，其中定义了数据库连接字符串 URL 和 Properties 对象。
- 代码片段：
  ```java
  public class DruidHelper {
      private String url = "jdbc:mysql://172.17.0.133:3306/druid/vz/sql/avticea";
      private Properties conf = new Properties();
      private Connection connection;
  ```

画面 2：
- 展示了 DruidService 接口的定义，用于声明服务方法。
- 代码片段：
  ```java
  public interface DruidService {
  ```

画面 3：
- 展示了在 DruidService 接口中定义的方法 queryDruidList，用于查询数据库。
- 代码片段：
  ```java
  public interface DruidService {
      R queryDruidList(@RequestParam Map<String, Object> params);
  ```

画面 4：
- 展示了在 DruidService 接口上右键，选择“Implement”来生成实现类。
- 代码片段：
  ```java
  public class DruidServiceImpl implements DruidService {
  ```

画面 5：
- 展示了 DruidServiceImpl 类中定义的两个方法：queryDruidList 和 queryDruidTumum。
- 代码片段：
  ```java
  public class DruidServiceImpl implements DruidService {
      @Override
      public R queryDruidList(Map<String, Object> params) {
          String url = "select * from all_device_message limit 10";
          DruidHelper helper = new DruidHelper();
          return null;
      }
      @Override
      public R queryDruidTumum(Map<String, Object> params) {
          return null;
      }
  ```

画面 6：
- 展示了在 queryDruidList 方法中，为变量声明类型。
- 代码片段：
  ```java
  Connection connection = null;
  Statement st = null;
  ResultSet rs = null;
  ```

画面 7：
- 展示了在 queryDruidList 方法中，声明了 List<MessageEntity> resultList。
- 代码片段：
  ```java
  List<MessageEntity> resultList = new ArrayList<>();
  ```

画面 8：
- 展示了在 queryDruidList 方法中，使用 try-catch-finally 块来处理异常。
- 代码片段：
  ```java
  try {
      // 代码
  } catch (Exception e) {
      e.printStackTrace();
  } finally {
      // 代码
  }
  ```

画面 9：
- 展示了在 queryDruidList 方法中，调用 DruidHelper 的 getConnection 方法获取数据库连接。
- 代码片段：
  ```java
  connection = helper.getConnection();
  ```

画面 10：
- 展示了在 queryDruidList 方法中，使用 rs.next() 循环遍历结果集。
- 代码片段：
  ```java
  while (rs.next()) {
      MessageEntity messageEntity = rs2Entity(rs);
      resultList.add(messageEntity);
  }
  ```

画面 11：
- 展示了在 queryDruidList 方法中，将查询结果封装成 Map 并返回。
- 代码片段：
  ```java
  Map<String, Object> map = new HashMap<>();
  map.put("items", resultList);
  return R.ok(map);
  ```

画面 12：
- 展示了在 queryDruidList 方法中，定义了 rs2Entity 方法用于将 ResultSet 转换为 MessageEntity。
- 代码片段：
  ```java
  private MessageEntity rs2Entity(ResultSet rs) throws Exception {
      MessageEntity messageEntity = new MessageEntity();
      messageEntity.setDeviceName(rs.getString("metaname"));
      messageEntity.setMeterId(rs.getString("meterid"));
      return messageEntity;
  }
  ```

画面 13：
- 展示了在 rs2Entity 方法中，设置 MessageEntity 的属性。
- 代码片段：
  ```java
  messageEntity.setDeviceName(rs.getString("metaname"));
  messageEntity.setMeterId(rs.getString("meterid"));
  ```

画面 14：
- 展示了在 rs2Entity 方法中，返回 MessageEntity 对象。
- 代码片段：
  ```java
  return messageEntity;
  ```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
见上文第 2 点。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

