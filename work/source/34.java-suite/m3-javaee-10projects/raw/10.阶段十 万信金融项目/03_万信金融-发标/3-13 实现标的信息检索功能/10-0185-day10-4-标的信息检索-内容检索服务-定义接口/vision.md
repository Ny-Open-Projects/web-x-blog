# 画面线理解：day10-4-标的信息检索-内容检索服务-定义接口

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-13 实现标的信息检索功能
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-13 实现标的信息检索功能\day10-4-标的信息检索-内容检索服务-定义接口_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:13, 01:15, 02:00, 02:01, 02:27, 02:36, 02:37, 02:40, 02:43, 02:50, 02:52, 03:23, 03:25, 03:27
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:17:24

1) 这一组画面整体在讲什么（一句话）：
在P2P项目中，为了解决数据库性能瓶颈，创建一个独立的“内容检索服务”微服务，使用ElasticSearch和Logstash技术实现全文检索功能，并演示了如何定义业务接口。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示PPT内容，说明为提高数据库性能，创建内容检索服务，采用ElasticSearch+Logstash技术，附带交互流程图。
画面2：展示PPT内容，交互流程图中，前端请求交易中心，交易中心请求内容检索服务，内容检索服务请求ES索引库，最后返回结果。
画面3：展示PPT内容，标题为“4.6.2.2 检索服务标的查询功能”，说明需新建业务接口ProjectIndexService。
画面4：展示PPT内容，与画面3相同，强调新建业务接口。
画面5：展示IDEA界面，项目结构中选中“wanningzp-content-search-service”模块。
画面6：在IDEA中右键“wanningzp-content-search-service”模块，弹出菜单。
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
