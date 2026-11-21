# 画面线理解：day10-7-标的信息检索-功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-13 实现标的信息检索功能
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-13 实现标的信息检索功能\day10-7-标的信息检索-功能测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:26, 01:03, 01:31, 02:21, 03:26, 04:10, 04:50, 05:38, 06:53, 07:39, 08:26, 09:56, 10:24, 10:58
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:20:05

1) 这一组画面整体在讲如何在 P2P 项目中通过创建内容搜索服务，结合 Elasticsearch 和 Logstash 技术栈，实现对交易数据的全文检索功能。

2) 按时间顺序列出每张画面的要点：
画面 1:
要点：展示 ContentSearchController 中的 queryProjects 方法，其中调用 contentSearchAgent 查询索引，并在响应不成功时抛出业务异常。
代码：
```java
@Override
public PageVO<ProjectDTO> queryProjects(ProjectQueryDTO projectQueryDTO) {
    RestResponse<PageVO<ProjectDTO>> response = contentSearchAgent.queryProjectIndex(projectQueryDTO, 
        projectQueryDTO.getOrder(), projectQueryDTO.getPageNo(), projectQueryDTO.getPageSize(), projectQueryDTO.getSortBy());
    if (!response.isSuccess()) {
        throw new BusinessException(CommonErrorCode.UNKNOW);
    }
    return response.getResult();
}
```

画面 2:
要点：展示 ContentSearchController 中的 queryProjectIndex 方法，其方法体中调用 projectIndexService 的 queryProjectIndex 方法。
代码：
```java
public RestResponse<PageVO<ProjectDTO>> queryProjectIndex(ProjectQueryParamsDTO projectQueryParamsDTO, Integer pageNo, Integer pageSize, String sortBy) {
    return projectIndexService.queryProjectIndex(projectQueryParamsDTO, pageNo, pageSize, sortBy);
}
```

画面 3:
要点：展示 ContentSearchController 中的 queryProjectIndex 方法，其方法体中调用 projectIndexService 的 queryProjectIndex 方法，代码自动补全。
代码：
```java
public RestResponse<PageVO<ProjectDTO>> queryProjectIndex(ProjectQueryParamsDTO projectQueryParamsDTO, Integer pageNo, Integer pageSize, String sortBy) {
    return projectIndexService.queryProjectIndex(projectQueryParamsDTO, pageNo, pageSize, sortBy);
}
```

画面 4:
要点：展示 PPT 中的代码片段，说明 ContentSearchController 中的 queryProjectIndex 方法如何调用 projectIndexService。
代码：
```java
@PostMapping(value = "/l/projects/indexes/q")
public RestResponse<PageVO<ProjectDTO>> queryProjectIndex(
    @RequestBody ProjectQueryParamsDTO projectQueryParamsDTO,
    @RequestParam Integer pageNo,
    @RequestParam Integer pageSize,
    @RequestParam(required = false) String sortBy) {
    PageVO<ProjectDTO> projects = projectIndexService.queryProjectIndex(projectQueryParamsDTO, pageNo, pageSize, sortBy);
    return RestResponse.success(projects);
}
```

画面 5:
要点：展示 PPT 中的“4.1 需求分析”章节，说明为提高数据查询性能，需要创建内容搜索服务，采用 Elasticsearch 和 Logstash 技术栈。
架构图：
- 潘发APP → 交易中心 → 内容搜索服务 → ES索引
- 交易中心 → 内容搜索服务 → ES索引
- 内容搜索服务 → ES索引

画面 6:
要点：展示 ProjectIndexServiceImpl 中的 queryProjectIndex 方法，其中将 PageVO 的内容设置为 list，设置分页信息。
代码：
```java
// 将为 PageVO 设置分页信息
pageVO.setContent(list);
pageVO.setPageSize(pageSize);
pageVO.setTotalCount(totalCount);
return pageVO;
```

画面 7:
要点：展示 Elasticsearch 的 head 插件界面，显示 wanxing2p_project 索引中的数据，其中一条记录的 status 字段值为 "FULLY"。
数据：
```json
{
  "_index": "wanxing2p_project",
  "_type": "doc",
  "_id": "2135463643093290627",
  "_score": 1.0,
  "_source": {
    "amount": 22320,
    "period": 360,
    "version": 1,
    "consumerId": 25,
    "name": "个人生活贷款",
    "description": "个人生活贷款",
    "projectStatus": "FULLY",
    "createdate": "2019-06-30T02:20:20.252Z",
    "status": "FULLY"
  }
}
```

画面 8:
要点：展示万信金融网站的首页，以及浏览器开发者工具中的 Network 面板，显示了多个请求的响应时间。
数据：
- 请求 1: 30 ms
- 请求 2: 100 ms
- 请求 3: 150 ms
- 请求 4: 230 ms

画面 9:
要点：展示万信金融网站的“金融投资”页面，以及浏览器开发者工具中的 Network 面板，显示了多个请求的响应时间。
数据：
- 请求 1: 1000 ms
- 请求 2: 2000 ms
- 请求 3: 3000 ms
- 请求 4: 4000 ms

画面 10:
要点：展示 ProjectIndexServiceImpl 中的 queryProjectIndex 方法，其中将搜索结果转换为 ProjectDTO 对象并添加到 list 中。
代码：
```java
for (SearchHit hit : searchHits) {
    ProjectDTO projectDTO = new ProjectDTO();
    Map<String, Object> sourceMap = hit.getSourceAsMap();
    Double amount = (Double) sourceMap.get("amount");
    String projectStatus = (String) sourceMap.get("projectStatus");
    Integer period = Integer.parseInt(sourceMap.get("period").toString());
    String name = (String) sourceMap.get("name");
    String description = (String) sourceMap.get("description");
    projectDTO.setAmount(new BigDecimal(amount));
    projectDTO.setProjectStatus(projectStatus);
    projectDTO.setPeriod(period);
    projectDTO.setName(name);
    projectDTO.setDescription(description);
    list.add(projectDTO);
}
```

画面 11:
要点：展示 ProjectIndexServiceImpl 中的 queryProjectIndex 方法，其中将搜索结果转换为 ProjectDTO 对象并添加到 list 中，代码高亮显示了 name 字段的赋值。
代码：
```java
String name = (String) sourceMap.get("name");
```

画面 12:
要点：展示 ProjectIndexServiceImpl 中的 queryProjectIndex 方法，其中将搜索结果转换为 ProjectDTO 对象并添加到 list 中，代码高亮显示了 pageSize 字段。
代码：
```java
Integer pageSize = Integer.valueOf(projectQueryParamsDTO.getPageSize());
```

画面 13:
要点：展示 Elasticsearch 的 head 插件界面，显示 wanxing2p_project 索引中的数据，其中一条记录的 status 字段值为 "MISCARRY"。
数据：
```json
{
  "_index": "wanxing2p_project",
  "_type": "doc",
  "_id": "21455063275464705",
  "_score": 1.0,
  "_source": {
    "amount": 2000,
    "period": 360,
    "version": 1,
    "consumerId": 19,
    "name": "个人生活贷款",
    "description": "个人生活贷款",
    "projectStatus": "MISCARRY",
    "createdate": "2019-06-30T02:20:20.252Z",
    "status": "MISCARRY"
  }
}
```

画面 14:
要点：展示万信金融网站的“金融投资”页面，以及浏览器开发者工具中的 Network 面板，显示了多个请求的响应时间。
数据：
- 请求 1: 2000 ms
- 请求 2: 4000 ms
- 请求 3: 6000 ms
- 请求 4: 8000 ms
