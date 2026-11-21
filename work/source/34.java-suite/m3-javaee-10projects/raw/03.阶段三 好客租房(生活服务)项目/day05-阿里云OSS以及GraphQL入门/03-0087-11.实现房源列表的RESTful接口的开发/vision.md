# 画面线理解：11.实现房源列表的RESTful接口的开发

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day05-阿里云OSS以及GraphQL入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day05-阿里云OSS以及GraphQL入门\11.实现房源列表的RESTful接口的开发【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:42, 01:33, 02:33, 03:19, 03:48, 04:50, 05:46, 06:20, 07:00, 07:35, 08:10, 08:41, 09:06
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:55:50

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中实现 RESTful 接口，包括控制器编写、服务层实现、分页结果封装及接口测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程讲义 PDF 中“5.4. 实现 RESTful 接口”章节，内容为在 itcast-haoke-manage-api-server 工程中导入依赖（joda-time）和编写 Controller。
画面 2: 展示 HouseResourcesController.java 文件，其中定义了 @GetMapping 注解的 list 方法，用于查询房源列表，参数包括 houseResources、currentPage 和 pageSize。
画面 3: 展示课程讲义 PDF 中“5.4. 实现 RESTful 接口”章节，内容为编写 TableResult。
画面 4: 展示项目结构，选中了 TableResult.java 文件，其内容为一个泛型类，包含 List<T> list 和 Pagination pagination 两个私有属性。
画面 5: 展示 HouseResourcesController.java 文件，高亮显示了 @GetMapping 注解的 list 方法。
画面 6: 展示 HouseResourcesController.java 文件，高亮显示了 @GetMapping 注解的 list 方法。
画面 7: 展示 HouseResourcesService.java 文件，高亮显示了 queryList 方法，该方法调用 apiHouseResourcesService 的 queryHouseResourcesList 方法。
画面 8: 展示 HouseResourcesService.java 文件，高亮显示了 queryList 方法，该方法调用 apiHouseResourcesService 的 queryHouseResourcesList 方法。
画面 9: 展示 HouseResourcesService.java 文件，高亮显示了 queryList 方法，该方法调用 apiHouseResourcesService 的 queryHouseResourcesList 方法，并返回 new TableResult<>(pageInfo.getRecords(), new Pagination())。
画面 10: 展示项目运行日志，显示 DubboApplication 启动成功，以及 Tomcat 服务启动。
画面 11: 展示 Advanced REST Client 浏览器插件界面，准备发送 HTTP 请求。
画面 12: 展示 Advanced REST Client 浏览器插件界面，显示了返回的 JSON 数据，包含房源信息。
画面 13: 展示课程讲义 PDF 中“5.4. 实现 RESTful 接口”章节，内容为 Service 实现部分，展示 queryList 方法的实现。
画面 14: 展示课程讲义 PDF 中“5.4. 实现 RESTful 接口”章节，内容为测试部分，展示返回的 JSON 数据，包含房源信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```xml
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.18.4</version>
</dependency>
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.9.9</version>
</dependency>
```

画面 2:
```java
return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();

/**
 * 查询房源列表
 * @param houseResources
 * @param currentPage
 * @param pageSize
 * @return
 */
@GetMapping
@ResponseBody
public ResponseEntity<TableResult> list(HouseResources houseResources,
        @RequestParam(name = "currentPage",
        defaultValue = "1") Integer currentPage,
        @RequestParam(name = "pageSize",
        defaultValue = "10") Integer pageSize) {
    return ResponseEntity.ok(this.houseResourcesService.queryList(houseResources, currentPage, pageSize));
}
```

画面 4:
```java
package cn.itcast.haoke.dubbo.api.vo;
import ...
@AllArgsConstructor
public class TableResult<T> {
    private List<T> list;
    private Pagination pagination;
}
```

画面 5:
```java
@GetMapping
@ResponseBody
public ResponseEntity<TableResult> list(HouseResources houseResources,
        @RequestParam(name = "currentPage",
        defaultValue = "1") Integer currentPage,
        @RequestParam(name = "pageSize",
        defaultValue = "10") Integer pageSize) {
    return ResponseEntity.ok(this.houseResourcesService.queryList(houseResources, currentPage, pageSize));
}
```

画面 6:
```java
@GetMapping
@ResponseBody
public ResponseEntity<TableResult> list(HouseResources houseResources,
        @RequestParam(name = "currentPage",
        defaultValue = "1") Integer currentPage,
        @RequestParam(name = "pageSize",
        defaultValue = "10") Integer pageSize) {
    return ResponseEntity.ok(this.houseResourcesService.queryList(houseResources, currentPage, pageSize));
}
```

画面 7:
```java
@Service
public class HouseResourcesService {
    @Reference(version = "1.0.0")
    private ApiHouseResourcesService apiHouseResourcesService;

    public boolean save(HouseResources houseResources) {
        int result = this.apiHouseResourcesService.saveHouseResources(houseResources);
        return result == 1;
    }

    public TableResult<HouseResources> queryList(HouseResources houseResources, Integer currentPage, Integer pageSize) {
        this.apiHouseResourcesService.queryHouseResourcesList(currentPage, pageSize, houseResources);
        return null;
    }
}
```

画面 8:
```java
@Service
public class HouseResourcesService {
    @Reference(version = "1.0.0")
    private ApiHouseResourcesService apiHouseResourcesService;

    public boolean save(HouseResources houseResources) {
        int result = this.apiHouseResourcesService.saveHouseResources(houseResources);
        return result == 1;
    }

    public TableResult<HouseResources> queryList(HouseResources houseResources, Integer currentPage, Integer pageSize) {
        PageInfo<HouseResources> pageInfo = this.apiHouseResourcesService.queryHouseResourcesList(currentPage, pageSize, houseResources);
        return null;
    }
}
```

画面 9:
```java
@Service
public class HouseResourcesService {
    @Reference(version = "1.0.0")
    private ApiHouseResourcesService apiHouseResourcesService;

    public boolean save(HouseResources houseResources) {
        int result = this.apiHouseResourcesService.saveHouseResources(houseResources);
        return result == 1;
    }

    public TableResult<HouseResources> queryList(HouseResources houseResources, Integer currentPage, Integer pageSize) {
        PageInfo<HouseResources> pageInfo = this.apiHouseResourcesService.queryHouseResourcesList(currentPage, pageSize, houseResources);
        return new TableResult<>(pageInfo.getRecords(), new Pagination());
    }
}
```

画面 13:
```java
public TableResult queryList(HouseResources houseResources, Integer currentPage, Integer pageSize) {
    PageInfo<HouseResources> pageInfo = this.apiHouseResourcesService.queryHouseResourcesList(currentPage, pageSize, houseResources);
    return new TableResult(pageInfo.getRecords(), new Pagination(currentPage, pageSize, pageInfo.getTotal()));
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 3: PPT 标题为“5.4. 实现 RESTful 接口”，内容为“编写 TableResult”。
画面 13: PPT 标题为“Service 实现”，内容为“public TableResult queryList(HouseResources houseResources, Integer currentPage, Integer pageSize) { ... }”。
画面 14: PPT 标题为“测试”，内容为“返回的 JSON 数据”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
