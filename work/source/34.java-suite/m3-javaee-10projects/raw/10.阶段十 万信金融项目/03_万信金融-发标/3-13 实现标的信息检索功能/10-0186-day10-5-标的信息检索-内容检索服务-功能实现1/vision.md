# 画面线理解：day10-5-标的信息检索-内容检索服务-功能实现1

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-13 实现标的信息检索功能
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-13 实现标的信息检索功能\day10-5-标的信息检索-内容检索服务-功能实现1_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:13, 00:42, 01:33, 02:09, 05:38, 07:57, 09:47, 11:19, 13:05, 14:32, 15:08, 15:44, 16:51, 17:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:18:22

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 Elasticsearch 的 RestHighLevelClient 构建项目搜索功能，包括配置、构建查询条件、分页和结果封装。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 IDE 中的项目结构，当前选中的是 `ProjectIndexServiceImpl.java` 文件。
- 代码内容：`@Autowired private RestHighLevelClient restHighLevelClient; @Value("${wanxingzp.es.index}") private String projectIndex; public PageVO<ProjectDTO> queryProjectIndex(ProjectQueryParamsDTO projectQueryParamsDTO, Integer pageNo, Integer pageSize, String sortby, String order) { //1.创建搜索请求对象 SearchRequest searchRequest = new SearchRequest(projectIndex); //2.1.搜索条件 BoolQueryBuilder queryBuilder = QueryBuilders.boolQuery(); //2.2.非空判断并设置条件 if (StringUtils.isNotBlank(projectQueryParamsDTO.getname())) { queryBuilder.must(QueryBuilders.termQuery("name", projectQueryParamsDTO.getname())); } if (projectQueryParamsDTO.getStartPeriod() != null) { queryBuilder.must(QueryBuilders.rangeQuery("period").gte(projectQueryParamsDTO.getStartPeriod())); } if (projectQueryParamsDTO.getPeriod() != null) { queryBuilder.must(QueryBuilders.rangeQuery("period").lte(projectQueryParamsDTO.getPeriod())); } }`

画面 2：
- 展示了 IDE 中的项目结构，当前选中的是 `ProjectIndexServiceImpl.java` 文件。
- 代码内容：`public class ProjectIndexServiceImpl implements ProjectIndexService { }`

画面 3：
- 展示了 IDE 中的项目结构，当前选中的是 `ProjectIndexServiceImpl.java` 文件。
- 代码内容：`import cn.itcast.wanxingzp.api.search.model.ProjectQueryParamsDTO; import cn.itcast.wanxingzp.api.transaction.model.ProjectDTO; import org.springframework.stereotype.Service; @Service public class ProjectIndexServiceImpl implements ProjectIndexService { }`

画面 4：
- 展示了 Apollo 配置中心的界面。
- 配置项：`micro_service.spring-boot-es` 的 `wanxingzp.es.host` 值为 `127.0.0.1:9200`，`wanxingzp.es.index` 值为 `wanxingzp_project`。

画面 5：
- 展示了 IDE 中的项目结构，当前选中的是 `ProjectIndexServiceImpl.java` 文件。
- 代码内容：`@Autowired private RestHighLevelClient restHighLevelClient; @Value("${wanxingzp.es.index}") private String projectIndex; public PageVO<ProjectDTO> queryProjectIndex(ProjectQueryParamsDTO projectQueryParamsDTO, Integer pageNo, Integer pageSize, String sortby, String order) { //1.创建搜索请求对象 SearchRequest searchRequest = new SearchRequest(projectIndex); //2.1.搜索条件 BoolQueryBuilder queryBuilder = QueryBuilders.boolQuery(); //2.2.非空判断并设置条件 if (StringUtils.isNotBlank(projectQueryParamsDTO.getname())) { queryBuilder.must(QueryBuilders.termQuery("name", projectQueryParamsDTO.getname())); } if (projectQueryParamsDTO.getStartPeriod() != null) { queryBuilder.must(QueryBuilders.rangeQuery("period").gte(projectQueryParamsDTO.getStartPeriod())); } if (projectQueryParamsDTO.getPeriod() != null) { queryBuilder.must(QueryBuilders.rangeQuery("period").lte(projectQueryParamsDTO.getPeriod())); } }`

画面 6：
- 展示了 IDE 中的项目结构，当前选中的是 `ProjectIndexServiceImpl.java` 文件。
- 代码内容：`//1.创建搜索请求对象 SearchRequest searchRequest = new SearchRequest(projectIndex); //2.1.搜索条件 BoolQueryBuilder queryBuilder = QueryBuilders.boolQuery(); //2.2.非空判断并设置条件 if (StringUtils.isNotBlank(projectQueryParamsDTO.getname())) { queryBuilder.must(QueryBuilders.termQuery("name", projectQueryParamsDTO.getname())); } if (projectQueryParamsDTO.getStartPeriod() != null) { queryBuilder.must(QueryBuilders.rangeQuery("period").gte(projectQueryParamsDTO.getStartPeriod())); } if (projectQueryParamsDTO.getPeriod() != null) { queryBuilder.must(QueryBuilders.rangeQuery("period").lte(projectQueryParamsDTO.getPeriod())); } }`

画面 7：
- 展示了 IDE 中的项目结构，当前选中的是 `ProjectIndexServiceImpl.java` 文件。
- 代码内容：`private RestHighLevelClient restHighLevelClient; @Value("${wanxingzp.es.index}") private String projectIndex; public PageVO<ProjectDTO> queryProjectIndex(ProjectQueryParamsDTO projectQueryParamsDTO, Integer pageNo, Integer pageSize, String sortby, String order) { //1.创建搜索请求对象 SearchRequest searchRequest = new SearchRequest(projectIndex); //2.1.搜索条件 BoolQueryBuilder queryBuilder = QueryBuilders.boolQuery(); //2.2.非空判断并设置条件 if (StringUtils.isNotBlank(projectQueryParamsDTO.getname())) { queryBuilder.must(QueryBuilders.termQuery("name", projectQueryParamsDTO.getname())); } if (projectQueryParamsDTO.getStartPeriod() != null) { queryBuilder.must(QueryBuilders.rangeQuery("period").gte(projectQueryParamsDTO.getStartPeriod())); } if (projectQueryParamsDTO.getPeriod() != null) { queryBuilder.must(QueryBuilders.rangeQuery("period").lte(projectQueryParamsDTO.getPeriod())); } }`

画面 8：
- 展示了 IDE 中的项目结构，当前选中的是 `ProjectIndexServiceImpl.java` 文件。
- 代码内容：`private RestHighLevelClient restHighLevelClient; @Value("${wanxingzp.es.index}") private String projectIndex; public PageVO<ProjectDTO> queryProjectIndex(ProjectQueryParamsDTO projectQueryParamsDTO, Integer pageNo, Integer pageSize, String sortby, String order) { //1.创建搜索请求对象 SearchRequest searchRequest = new SearchRequest(projectIndex); //2.1.搜索条件 BoolQueryBuilder queryBuilder = QueryBuilders.boolQuery(); //2.2.非空判断并设置条件 if (StringUtils.isNotBlank(projectQueryParamsDTO.getname())) { queryBuilder.must(QueryBuilders.termQuery("name", projectQueryParamsDTO.getname())); } if (projectQueryParamsDTO.getStartPeriod() != null) { queryBuilder.must(QueryBuilders.rangeQuery("period").gte(projectQueryParamsDTO.getStartPeriod())); } if (projectQueryParamsDTO.getPeriod() != null) { queryBuilder.must(QueryBuilders.rangeQuery("period").lte(projectQueryParamsDTO.getPeriod())); } }`

画面 9：
- 展示了 Elasticsearch 的 Head 界面。
- 显示了索引 `wanxingzp_project`，状态为 `green`，文档数量为 418。

画面 10：
- 展示了 IDE 中的项目结构，当前选中的是 `ProjectQueryParamsDTO.java` 文件。
- 代码内容：`@ApiModelProperty("标的名称(分词匹配)") private String name; @ApiModelProperty("标的描述(分词匹配)") private String description; @ApiModelProperty("起止标的期限(单位:天)") private Integer startPeriod; @ApiModelProperty("起止标的期限(单位:天)") private Integer endPeriod; @ApiModelProperty("起止年化利率(投资人视图)") private BigDecimal startAnnualRate; @ApiModelProperty("起止年化利率(投资人视图)") private BigDecimal endAnnualRate; @ApiModelProperty("标的的状态") private String status;`

画面 11：
- 展示了 IDE 中的项目结构，当前选中的是 `ProjectIndexServiceImpl.java` 文件。
- 代码内容：`//1.创建搜索请求对象 SearchRequest searchRequest = new SearchRequest(projectIndex); //2.1.搜索条件 BoolQueryBuilder queryBuilder = QueryBuilders.boolQuery(); //2.2.非空判断并设置条件 if (StringUtils.isNotBlank(projectQueryParamsDTO.getname())) { queryBuilder.must(QueryBuilders.termQuery("name", projectQueryParamsDTO.getname())); } if (projectQueryParamsDTO.getStartPeriod() != null) { queryBuilder.must(QueryBuilders.rangeQuery("period").gte(projectQueryParamsDTO.getStartPeriod())); } if (projectQueryParamsDTO.getPeriod() != null) { queryBuilder.must(QueryBuilders.rangeQuery("period").lte(projectQueryParamsDTO.getPeriod())); } }`

画面 12：
- 展示了 IDE 中的项目结构，当前选中的是 `ProjectIndexServiceImpl.java` 文件。
- 代码内容：`//1.创建搜索请求对象 SearchRequest searchRequest = new SearchRequest(projectIndex); //2.1.搜索条件 BoolQueryBuilder queryBuilder = QueryBuilders.boolQuery(); //2.2.非空判断并设置条件 if (StringUtils.isNotBlank(projectQueryParamsDTO.getname())) { queryBuilder.must(QueryBuilders.termQuery("name", projectQueryParamsDTO.getname())); } if (projectQueryParamsDTO.getStartPeriod() != null) { queryBuilder.must(QueryBuilders.rangeQuery("period").gte(projectQueryParamsDTO.getStartPeriod())); } if (projectQueryParamsDTO.getPeriod() != null) { queryBuilder.must(QueryBuilders.rangeQuery("period").lte(projectQueryParamsDTO.getPeriod())); } }`

画面 13：
- 展示了 IDE 中的项目结构，当前选中的是 `ProjectIndexServiceImpl.java` 文件。
- 代码内容：`if (projectQueryParamsDTO.getPeriod() != null) { queryBuilder.must(QueryBuilders.rangeQuery("period").lte(projectQueryParamsDTO.getPeriod())); } //3.创建SearchSourceBuilder对象——封装对象 SearchSourceBuilder searchSourceBuilder = new SearchSourceBuilder(); //3.1.设置查询条件 searchSourceBuilder.query(queryBuilder); //3.2.设置分页参数 searchSourceBuilder.from(pageNo).size(pageSize); //3.3.
