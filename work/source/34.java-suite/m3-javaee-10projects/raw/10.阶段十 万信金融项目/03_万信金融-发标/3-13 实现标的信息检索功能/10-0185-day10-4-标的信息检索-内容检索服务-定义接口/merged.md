# day10-4-标的信息检索-内容检索服务-定义接口

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-13 实现标的信息检索功能
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-13 实现标的信息检索功能\day10-4-标的信息检索-内容检索服务-定义接口_【海量资源尽在 666java.com】.mp4
- 时长 3分47秒（音频 227s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们搞定了交易中心这边的功能对吧接下来咱们就接着要去哪内容检索微服务这边继续编写代码实现功能而且呢咱整个标底信息快速检索它的核心功能啊或者核心代码就在哪边就在内容检索微服务这边你看它这边是不是先是接到什么呀交易中心通过飞发过来这个请求这个请求里边是不是带有那些参数就是
[00:31] 条件呀分页的数据啊还有排序的数据对不对他先接收接收完之后呢然后他就去ES索引库里边进行查询就是带有条件的带有分页的带有排序的一个综合查询查完之后呢就返回结果对吧那这里边是这样啊内容检索服务这边呢我们是实现咱这个功能的一个核心的一个地方那这个地方的话你可以用这个以前我们学过的SpringData
[01:00] Elasticsearch来实现Spring Data还有印象吗是不是通过它实现起来相对来说会简单一些或者轻松一些但是但是这儿我要给大家强调一下咱们现在用的Elasticsearch这个版本是731这个版本这个版本非常新目前Spring Data还没有跟上这个节奏没有跟上这个步伐有时候你现在用Spring Data支持不了这么新的一个版本所以我们这儿要使用
[01:30] Elasticsearch本身的官方的API来实现这个查询功能当然了官方也是推荐使用他自己提供的这个什么API就是我们前面在搭建环境的时候跟大家提到的那个什么高级别的那个扣端通过它来实现从ES索引库进行标底信息的一个查询这一块呢我要跟大家先说一说那咱们接下来具体功能实现的话也是先要定义接口
[02:00] 就要藏我们直接就到要藏因为这里边也不是涉及到数据库没有丢没有数据方案而这个接口报控制了我们前面是不是已经定义过说咱功能开发主要就是在要藏那咱要藏这块要先建一个什么呀接口叫project indexservice这个index就是什么意思对所以那意思好咱接下来去这个哪
[02:28] 对content search就是内容检索微服工程里边找到Service这个包在这个包里边呢新建一个接口这在右层的接口那这个接口的话其实应该跟交易中心那边的接口里边定义的方法应该是差不多的大家可以看看讲义你看看是不是基本上是一样你看这个名字无所谓了第一个层是不是封装那个查询条件呢是不是然后这一段配一number配一size是什么
[03:02] 对分页的数据sort byorder是什么呀对排序的数据然后发言值你看一样吗也是一样配一流嘛对不对某一样的数据嘛里边的范形是project的地球啊所以说呢这块这个接口啊跟前面接入中心一模一样那我就不再敲了直接粘过来用好这是咱在哪对内容检索微服务这边先把业务层的接口给定好那么一会呢咱就开始编写
[03:40] 实现类啊那么这个实现类里边的这个代码会比较多一些

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在P2P项目中，为了解决数据库性能瓶颈，创建一个独立的“内容检索服务”微服务，使用ElasticSearch和Logstash技术实现全文检索功能，并演示了如何定义业务接口。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示PPT内容，说明为提高数据库性能，创建内容检索服务，采用ElasticSearch+Logstash技术，附带交互流程图。
画面2：展示PPT内容，交互流程图中，前端请求交易中心，交易中心请求内容检索服务，内容检索服务请求ES索引库，最后返回结果。
画面3：展示PPT内容，标题为“4.6.2.2 检索服务标的查询功能”，说明需新建业务接口ProjectIndexService。
画面4：展示PPT内容，与画面3相同，强调新建业务接口。
画面5：展示IDEA界面，项目结构中选中“wanningzp-content-search-Service”模块。
画面6：在IDEA中右键“wanningzp-content-search-Service”模块，弹出菜单。
画面7：在弹出菜单中选择“New”。
画面8：弹出“Create New Class”对话框，选择“Class”类型，名称为“ProjectIndexService”。
画面9：在IDEA中打开并编辑“ProjectIndexService.java”文件，准备编写接口。
画面10：展示PPT内容，与画面3相同，强调新建业务接口。
画面11：展示PPT内容，显示接口定义和后续步骤：创建ProjectIndexServiceImpl实现类。
画面12：展示PPT内容，显示“4.6.3 创建测试类”，并展示多个开发工具窗口（如Postman、Elasticsearch-head、终端等）。
画面13：在IDEA中编辑“ProjectIndexService.java”文件，光标在接口定义处。
画面14：在IDEA中编辑“ProjectIndexService.java”文件，光标在接口定义处，准备编写方法签名。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3、4、10、11：
```java
/**
 * 标的检索业务层接口
 */
public interface ProjectIndexService {
    PageVO<ProjectDTO> queryProjectIndex(ProjectQueryParamsDTO projectQueryParamsDTO,
            Integer pageNo, Integer pageSize,
            String sortBy, String order);
}
```
画面11：
```java
@Service
public class ProjectIndexServiceImpl implements ProjectIndexService {
    @Autowired
    private RestHighLevelClient restHighLevelClient;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：
标题：为了提高数据库性能，我们面对交易中心数据库p2p_transaction进行了分库分表、读写分离。但是即便如此，我们仍进行多字段分段过滤，在数据量很大的情况下，类似这样查询仍然会比较耗时。在这种情况下，我们考虑使用全文检索技术来进一步优化性能。
由于P2P项目中会有多处业务数据有这种需求，所以我们单独创建一个微服务工程(下图中的内容检索服务)为整个项目提供全文检索服务，该工程主要采用ElasticSearch+Logstash技术实现。具体交互流程如下：
架构图：
- 调用端/APP → 交易中心 → 内容检索服务 → ES索引库
- 交易中心 → 内容检索服务 → ES索引库
- 内容检索服务 → ES索引库
- ES索引库 → 内容检索服务
- 内容检索服务 → 交易中心
- 交易中心 → 调用端/APP
交互流程：
1. 前端请求交易中心检索服务
2. 交易中心请求内容检索服务
3. 内容检索服务请求ES索引库
4. ES索引库返回结果给内容检索服务
5. 内容检索服务返回结果给交易中心
6. 交易中心返回结果给前端

画面3：
标题：4.6.2.2 检索服务标的查询功能
内容：
1. 新建一个业务接口ProjectIndexService：
   - 标的检索业务层接口
   - public interface ProjectIndexService {
     PageVO<ProjectDTO> queryProjectIndex(ProjectQueryParamsDTO projectQueryParamsDTO,
         Integer pageNo, Integer pageSize,
         String sortBy, String order);
   }
2. 创建ProjectIndexServiceImpl实现类，通过Elasticsearch的API实现标的检索(条件+分页+排序)：

画面11：
标题：4.6.2.2 检索服务标的查询功能
内容：
1. 新建一个业务接口ProjectIndexService：
   - 标的检索业务层接口
   - public interface ProjectIndexService {
     PageVO<ProjectDTO> queryProjectIndex(ProjectQueryParamsDTO projectQueryParamsDTO,
         Integer pageNo, Integer pageSize,
         String sortBy, String order);
   }
2. 创建ProjectIndexServiceImpl实现类，通过Elasticsearch的API实现标的检索(条件+分页+排序)：
   - @Service
   - public class ProjectIndexServiceImpl implements ProjectIndexService {
     - @Autowired
     - private RestHighLevelClient restHighLevelClient;

画面12：
标题：4.6.3 创建测试类
内容：
- 展示多个开发工具窗口：
  - Postman
  - Elasticsearch-head
  - 终端窗口
  - ApolloPortal
  - adminService
  - ConfigService
  - grunt

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

