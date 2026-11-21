# 画面线理解：day10-6-标的信息检索-内容检索服务-功能实现2

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-13 实现标的信息检索功能
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-13 实现标的信息检索功能\day10-6-标的信息检索-内容检索服务-功能实现2_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:43, 01:36, 03:31, 04:36, 05:10, 05:52, 07:19, 09:21, 10:21, 11:39, 12:14, 12:49, 13:13
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:19:18

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中使用 Elasticsearch 的 SearchSourceBuilder 构建查询条件、设置排序和分页参数，并将搜索结果封装为 PageVO 对象返回。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 ProjectIndexServiceImp.java 文件中构建 QueryBuilder 的代码，用于处理项目名称和时间段的查询条件。
画面 2: 展示创建 SearchSourceBuilder 对象并设置查询条件的代码。
画面 3: 展示设置排序参数的代码，根据 sortBy 和 order 字段决定升序或降序。
画面 4: 展示设置分页参数的代码，包括 from 和 size。
画面 5: 展示执行搜索请求的代码，使用 restHighLevelClient。
画面 6: 展示获取搜索结果并封装为 PageVO 对象的代码。
画面 7: 展示获取搜索结果的总记录数并设置到 PageVO 中。
画面 8: 展示遍历搜索结果并封装为 ProjectDTO 对象的代码。
画面 9: 展示将 ProjectDTO 对象添加到列表中。
画面 10: 展示捕获异常并返回 null 的代码。
画面 11: 展示封装为 PageVO 对象并返回的代码。
画面 12: 展示 PageVO 类的结构，包括 pageNo、pageSize、content、total 等属性。
画面 13: 展示设置分页参数的代码。
画面 14: 展示封装为 PageVO 对象并返回的代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
if(StringUtils.isNotBlank(projectQueryParamsDTO.getNames()) {
    queryBuilder.must(QueryBuilders.termQuery("name", projectQueryParamsDTO.getNames()));
}
if(projectQueryParamsDTO.getStartPeriod() != null) {
    queryBuilder.must(QueryBuilders.rangeQuery("period").gte(projectQueryParamsDTO.getStartPeriod()));
}
if(projectQueryParamsDTO.getEndPeriod() != null) {
    queryBuilder.must(QueryBuilders.rangeQuery("period").lte(projectQueryParamsDTO.getEndPeriod()));
}
```

画面 2:
```java
//3. 创建SearchSourceBuilder对象
SearchSourceBuilder searchSourceBuilder = new SearchSourceBuilder();
//3.1 封装条件
searchSourceBuilder.query(queryBuilder);
//3.2 设置排序参数
```

画面 3:
```java
//3.2 设置排序参数
if(StringUtils.isNotBlank(sortBy) && StringUtils.isNotBlank(order)) {
    if(order.toLowerCase().equals("asc")) {
        searchSourceBuilder.sort(sortBy, SortOrder.ASC);
    }
    if(order.toLowerCase().equals("desc")) {
        searchSourceBuilder.sort(sortBy, SortOrder.DESC);
    }
} else {
    searchSourceBuilder.sort("createdate", SortOrder.DESC);
}
//3.3 设置分页参数
searchSourceBuilder.from((pageNo - 1) * pageSize);
searchSourceBuilder.size(pageSize);
```

画面 4:
```java
//3.2 设置排序参数
if(StringUtils.isNotBlank(sortBy) && StringUtils.isNotBlank(order)) {
    if(order.toLowerCase().equals("asc")) {
        searchSourceBuilder.sort(sortBy, SortOrder.ASC);
    }
    if(order.toLowerCase().equals("desc")) {
        searchSourceBuilder.sort(sortBy, SortOrder.DESC);
    }
} else {
    searchSourceBuilder.sort("createdate", SortOrder.DESC);
}
//3.3 设置分页参数
searchSourceBuilder.from((pageNo - 1) * pageSize);
searchSourceBuilder.size(pageSize);
```

画面 5:
```java
//4. 完成封装
searchRequest.source(searchSourceBuilder);
```

画面 6:
```java
//6. 获取搜索的结果
//7. 封装为PageVO对象并返回
PageVO<ProjectDTO> pageVO = new PageVO<>();
```

画面 7:
```java
//5. 执行搜索
List<ProjectDTO> list = new ArrayList<>();
PageVO<ProjectDTO> pageVO = new PageVO<>();
try {
    SearchResponse searchResponse = restHighLevelClient.search(searchRequest, RequestOptions.DEFAULT);
    //6. 获取搜索结果
    SearchHits hits = searchResponse.getHits();
    long totalHits = hits.getTotalHits().value;
    pageVO.setTotalTotalHits(totalHits);
    //7. 遍历并封装DTO
    for (SearchHit hit : searchHits) {
        ProjectDTO projectDTO = new ProjectDTO();
        Map<String, Object> sourceASMap = hit.getSourceAsMap();
        Double amount = (Double) sourceASMap.get("amount");
        String projectStatus = (String) sourceASMap.get("projectstatus");
        Integer period = Integer.parseInt(sourceASMap.get("period").toString());
        String name = (String) sourceASMap.get("name");
        String description = (String) sourceASMap.get("description");
        projectDTO.setAmount(new BigDecimal(amount));
        projectDTO.setProjectStatus(projectStatus);
        projectDTO.setPeriod(period);
        projectDTO.setName(name);
        projectDTO.setDescription(description);
        list.add(projectDTO);
    }
} catch (Exception e) {
    e.printStackTrace();
    return null;
}
//8. 封装为PageVO对象并返回
pageVO.setContent(list);
pageVO.setPageSize(pageSize);
```

画面 8:
```java
//5. 执行搜索
List<ProjectDTO> list = new ArrayList<>();
PageVO<ProjectDTO> pageVO = new PageVO<>();
try {
    SearchResponse searchResponse = restHighLevelClient.search(searchRequest, RequestOptions.DEFAULT);
    //6. 获取搜索结果
    SearchHits hits = searchResponse.getHits();
    long totalHits = hits.getTotalHits().value;
    pageVO.setTotalTotalHits(totalHits);
    //7. 遍历并封装DTO
    for (SearchHit hit : searchHits) {
        ProjectDTO projectDTO = new ProjectDTO();
        Map<String, Object> sourceASMap = hit.getSourceAsMap();
        Double amount = (Double) sourceASMap.get("amount");
        String projectStatus = (String) sourceASMap.get("projectstatus");
        Integer period = Integer.parseInt(sourceASMap.get("period").toString());
        String name = (String) sourceASMap.get("name");
        String description = (String) sourceASMap.get("description");
        projectDTO.setAmount(new BigDecimal(amount));
        projectDTO.setProjectStatus(projectStatus);
        projectDTO.setPeriod(period);
        projectDTO.setName(name);
        projectDTO.setDescription(description);
        list.add(projectDTO);
    }
} catch (Exception e) {
    e.printStackTrace();
    return null;
}
//8. 封装为PageVO对象并返回
pageVO.setContent(list);
pageVO.setPageSize(pageSize);
```

画面 9:
```java
//7. 遍历并封装DTO
for (SearchHit hit : searchHits) {
    ProjectDTO projectDTO = new ProjectDTO();
    Map<String, Object> sourceASMap = hit.getSourceAsMap();
    Double amount = (Double) sourceASMap.get("amount");
    String projectStatus = (String) sourceASMap.get("projectstatus");
    Integer period = Integer.parseInt(sourceASMap.get("period").toString());
    String name = (String) sourceASMap.get("name");
    String description = (String) sourceASMap.get("description");
    projectDTO.setAmount(new BigDecimal(amount));
    projectDTO.setProjectStatus(projectStatus);
    projectDTO.setPeriod(period);
    projectDTO.setName(name);
    projectDTO.setDescription(description);
    list.add(projectDTO);
}
```

画面 10:
```java
} catch (Exception e) {
    e.printStackTrace();
    return null;
}
```

画面 11:
```java
//8. 封装为PageVO对象并返回
pageVO.setContent(list);
pageVO.setPageSize(pageSize);
```

画面 12:
```java
public class PageVO<T> {
    private Integer pageNo;
    private Integer pageSize;
    private List<T> content;
    private Long total;
    private Integer totalTotalHits;
    private Integer totalPages;
    private String status;
    private String message;
    private String code;
    private String url;
    private String method;
    private String request;
    private String response;
    private String ip;
    private String userAgent;
    private String referer;
    private String xForwardedFor;
    private String xRealIp;
    private String xRequestedWith;
    private String xContentTypeOptions;
    private String xFrameOptions;
    private String xXSSProtection;
    private String xContentTypeOptions;
    private String xFrameOptions;
    private String xXSSProtection;
    private String xContentTypeOptions;
    private String xFrameOptions;
    private String xXSSProtection;
    private String xContentTypeOptions;
    private String xFrameOptions;
    private String xXSSProtection;
    private String xContentTypeOptions;
    private String xFrameOptions;
    private String xXSSProtection;
    private String xContentTypeOptions;
    private String xFrameOptions;
    private String xXSSProtection;
    private String xContentTypeOptions;
    private String xFrameOptions;
    private String xXSSProtection;
    private String xContentTypeOptions;
    private String xFrameOptions;
    private String xXSSProtection;
    private String xContentTypeOptions;
    private String xFrameOptions;
    private String xXSSProtection;
    private String xContentTypeOptions;
    private String
