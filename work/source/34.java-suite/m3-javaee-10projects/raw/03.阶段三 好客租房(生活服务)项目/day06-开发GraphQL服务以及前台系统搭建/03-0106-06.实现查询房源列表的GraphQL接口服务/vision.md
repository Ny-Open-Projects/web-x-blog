# 画面线理解：06.实现查询房源列表的GraphQL接口服务

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day06-开发GraphQL服务以及前台系统搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day06-开发GraphQL服务以及前台系统搭建\06.实现查询房源列表的GraphQL接口服务【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:40, 01:48, 02:33, 03:36, 04:28, 05:07, 05:28, 06:28, 07:01, 08:25, 08:52, 09:16, 09:56
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:09:15

1) 这一组画面整体在讲什么（一句话）：
实现一个基于 GraphQL 的房屋资源列表查询接口，包括修改 GraphQL Schema 文件、编写数据获取器（DataFetcher）以及测试接口。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了课程 PDF 文档的目录结构，当前章节为“1.8.1、修改haoke.graphqls文件”，并显示了部分 GraphQL Schema 代码。
画面 2: 在 IntelliJ IDEA 中，展示了 `HouseResourcesService` 服务类中的 `queryList` 方法，用于分页查询房屋资源。
画面 3: 在 `haoke.graphqls` 文件中，定义了 `HouseResources` 类型的字段，包括 `buildingFloorNum`、`rent`、`paymentMethod` 等。
画面 4: 在 `haoke.graphqls` 文件中，定义了 `TableResult` 和 `Pagination` 类型，其中 `TableResult` 包含 `list` 和 `pagination` 字段。
画面 5: 在 `HouseResourcesListDataFetcher` 类中，定义了 `dataFetcher` 方法，用于根据 ID 查询房屋资源。
画面 6: 在 `haoke.graphqls` 文件中，定义了 `HaokeQuery` 类型，包含 `HouseResources` 和 `HouseResourcesList` 两个查询字段。
画面 7: 在 `HouseResourcesListDataFetcher` 类中，定义了 `fieldNames` 方法和 `dataFetcher` 方法的参数类型。
画面 8: 在 `GraphQlController` 类中，定义了 `query` 方法，用于接收 GraphQL 查询并执行。
画面 9: 在 `haoke.graphqls` 文件中，定义了 `HouseResources` 类型的字段，包括 `orientation`、`decoration`、`facilities` 等。
画面 10: 在 Altair GraphQL Client 中，编写了查询 `HouseResourcesList` 的 GraphQL 查询语句。
画面 11: 在 PDF 文档中，展示了 `haoke.graphqls` 文件的 Schema 定义，包括 `HaokeQuery` 和 `HouseResources` 类型。
画面 12: 在 `HouseResourcesListDataFetcher` 类中，编写了 `dataFetcher` 方法的逻辑，用于处理分页参数。
画面 13: 在 `haoke.graphqls` 文件中，定义了 `Pagination` 类型，包含 `current`、`pageSize` 和 `total` 字段。
画面 14: 在 PDF 文档中，展示了 `haoke.graphqls` 文件的 Schema 定义，包括 `HaokeQuery` 和 `HouseResources` 类型。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```graphql
schema {
  query: HaokeQuery
}

type HaokeQuery {
  HouseResources(id:Long): HouseResources
  HouseResourcesList(page:Int, pageSize:Int): TableResult
}
```

画面 2:
```java
public TableResult<HouseResources> queryList(HouseResources houseRese
queryHouseResourcesList(currentPage, pageSize, houseRese
return new TableResult<>(pageInfo.getRecords(), new Pagination(
```

画面 3:
```graphql
buildingFloorNum:String
rent:Int
rentMethod:Int
paymentMethod:Int
houseType:String
coveredArea:String
useArea:String
floor:String
orientation:String
decoration:Int
facilities:String
pic:String
houseDesc:String
contact:String
mobile:String
time:Int
propertyCost:String
```

画面 4:
```graphql
type TableResult{
  list:[HouseResources]
  pagination:Pagination
}

type Pagination{
  current:Int
  pageSize:Int
  total:int
}
```

画面 5:
```java
@Component
public class HouseResourcesListDataFetcher implements MyDataFetcher {
  @Autowired
  private HouseResourcesService houseResourcesService;

  @Override
  public String fieldName() {
    return "HouseResourcesList";
  }

  @Override
  public Object dataFetcher(DataFetchingEnvironment environment) {
    Long id = environment.getArgument("id");
    return this.houseResourcesService.queryHouseResourcesById(id);
  }
}
```

画面 6:
```graphql
schema {
  query: HaokeQuery
}

type HaokeQuery {
  HouseResources(id:Long): HouseResources
  HouseResourcesList(page:Int, pageSize:Int): TableResult
}

type HouseResources {
  id:Long!
  title:String
  estateId:Long
  buildingNum:String
  buildingUnit:String
  buildingFloorNum:String
  rent:Int
  rentMethod:Int
  paymentMethod:Int
  houseType:String
  coveredArea:String
  useArea:String
  floor:String
}
```

画面 7:
```java
@Component
public class HouseResourcesListDataFetcher implements MyDataFetcher {
  @Autowired
  private HouseResourcesService houseResourcesService;

  @Override
  public String fieldName() {
    return "HouseResourcesList";
  }

  @Override
  public Object dataFetcher(DataFetchingEnvironment environment) {
    Integer page = environment.getArgument("page");
    if(page == null){
      page = 1;
    }
    Integer pageSize = environment.getArgument("pageSize");
    if(pageSize == null){
      pageSize = 5;
    }
    return this.houseResourcesService.queryList(null, page, pageSize);
  }
}
```

画面 8:
```java
@GetMapping
@ResponseBody
public Map<String, Object> query(@RequestParam("query") String query) {
  return this.graphQL.execute(query).toSpecification();
}
```

画面 9:
```graphql
orientation:String
decoration:Int
facilities:String
pic:String
houseDesc:String
contact:String
mobile:String
time:Int
propertyCost:String
```

画面 10:
```graphql
{
  HouseResourcesList {
    list {
      id
      title
      estateId
      buildingUnit
      buildingFloorNum
      mobile
      useArea
      pic
    }
    pagination {
      current
      pageSize
    }
  }
}
```

画面 11:
```graphql
schema {
  query: HaokeQuery
}

type HaokeQuery {
  HouseResources(id:Long): HouseResources
  HouseResourcesList(page:Int, pageSize:Int): TableResult
}

type HouseResources {
  id:Long!
  title:String
  estateId:Long
  buildingNum:String
  buildingUnit:String
  buildingFloorNum:String
  rent:Int
  rentMethod:Int
  paymentMethod:Int
  houseType:String
  coveredArea:String
  useArea:String
  floor:String
}
```

画面 12:
```java
@Component
public class HouseResourcesListDataFetcher implements MyDataFetcher {
  @Autowired
  private HouseResourcesService houseResourcesService;

  @Override
  public String fieldName() {
    return "HouseResourcesList";
  }

  @Override
  public Object dataFetcher(DataFetchingEnvironment environment) {
    Integer page = environment.getArgument("page");
    if(page == null){
      page = 1;
    }
    Integer pageSize = environment.getArgument("pageSize");
    if(pageSize == null){
      pageSize = 5;
    }
    return this.houseResourcesService.queryList(null, page, pageSize);
  }
}
```

画面 13:
```graphql
type Pagination{
  current:Int
  pageSize:Int
  total:int
}
```

画面 14:
```graphql
schema {
  query: HaokeQuery
}

type HaokeQuery {
  HouseResources(id:Long): HouseResources
  HouseResourcesList(page:Int, pageSize:Int): TableResult
}

type HouseResources {
  id:Long!
  title:String
  estateId:Long
  buildingNum:String
  buildingUnit:String
  buildingFloorNum:String
  rent:Int
  rentMethod:Int
  paymentMethod:Int
  houseType:String
  coveredArea:String
  useArea:String
  floor:String
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PDF 文档标题为“1.8、实现查询房源列表接口”，子标题为“1.8.1、修改haoke.graphqls文件”。
画面 6: PDF 文档标题为“1.8、实现查询房源列表接口”，子标题为“1.8.1、修改haoke.graphqls文件”。
画面 11: PDF 文档标题为“1.8、实现查询房源列表接口”，子标题为“1.8.1、修改haoke.graphqls文件”。
画面 14: PDF 文档标题为“1.8、实现查询房源列表接口”，子标题为“1.8.1、修改haoke.graphqls文件”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
