# 画面线理解：17.课程总结

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day06-开发GraphQL服务以及前台系统搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day06-开发GraphQL服务以及前台系统搭建\17.课程总结【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:24, 00:43, 01:07, 01:31, 01:47, 02:03, 02:38, 02:51, 03:05, 03:27, 03:58, 04:08, 04:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:17:26

1) 这一组画面整体在讲什么（一句话）：
本课程讲解如何使用 GraphQL 开发房源接口、实现广告系统，并整合前端系统，涉及 SpringBoot、Dubbo、Apollo Client 等技术。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 课程介绍，列出核心内容：使用 GraphQL 开发房源接口、实现房源列表查询接口、搭建前后端系统、实现首页轮播广告功能、改造广播广告接口方式为 GraphQL、学习使用 Apollo Client 的使用。
画面 2: 展示 HouseResourcesService 接口定义，包含 import 语句和 @Transactional 注解。
画面 3: 展示 GraphQLController 的 import 语句，包括 graphql.GraphQL、@Autowired、@Controller 等。
画面 4: 讲解优化 GraphQLProvider 逻辑的问题，指出当前方法难以维护，并提出改进思路：编写接口、所有实现查询的逻辑都实现该接口、在 GraphQLProvider 中使用该接口进行处理、以后新增查询只需增加实现类即可。
画面 5: 展示 GraphQL 查询类型定义，包括 HouseResources 对象的字段，如 id、title、estateId、buildingQuint、rent、rentMethod、paymentMethod、houseType、coveredArea、useArea、floor、orientation、decoration、pic、houseDesc 等。
画面 6: 讲解搭建工程，第一步是将资料中的 haoke-web.zip 解压到项目目录。
画面 7: 展示 GraphQL 查询返回的数据结构，包含 data.list 和 meta.status、msg。
画面 8: 讲解实现查询接口（dubbo服务），分析首页轮播广告功能需要独立的 dubbo 服务，并创建 common 工程。
画面 9: 讲解整合前端系统，修改 home.js 文件中请求地址，使用 axios.post 发送请求。
画面 10: 展示成功获取到 GraphQL 接口的数据。
画面 11: 展示 haoke.graphqls 文件内容，定义 schema 和 query: HaokeQuery。
画面 12: 讲解 GraphQL 客户端，介绍 Apollo Client、graphql-request、Lokka、nogql、AWS Amplify 等。
画面 13: 发现两个问题：GraphQL 服务不支持 cross、Apollo Client 发起的请求为 POST，而当前 GraphQL 仅支持 GET。并展示相关代码。
画面 14: 展示成功获取到数据，页面效果实现。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
import cn.itcast.haoke.dubbo.server.pojo.HouseResources;
import cn.itcast.haoke.dubbo.server.service.HouseResourcesService;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import org.apache.commons.lang3.StringUtils;
@Transactional
@Service
public class HouseResourcesServiceImpl extends BaseServiceImpl<HouseResources> implements HouseResourcesService {
    @param houseResources
```

画面 3:
```java
package cn.itcast.haoke.dubbo.api.controller;
import graphql.GraphQL;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import java.io.IOException;
import java.util.Map;
import java.util.Map;
```

画面 4:
```java
private RuntimeWiring buildWiring() {
    return RuntimeWiring.newRuntimeWiring()
        .type("HouseResources", builder -> builder.dataFetcher(fieldname -> {
            long id = environment.getArgument(name: "id");
            return this.houseResourcesService.queryById(id);
        }))
        .build();
}
```

画面 5:
```graphql
type HaokeQuery {
    HouseResources(id:Long):HouseResources
    HouseResourcesList(page:Int, pageSize:Int):TableResult
}
type HouseResources {
    id:Long
    title:String
    estateId:Long
    buildingQuint:String
    buildingFloorNum:String
    rent:Int
    rentMethod:Int
    paymentMethod:Int
    houseType:String
    coveredArea:String
    useArea:String
    floor:String
    orientation:String
    decoration:String
    pic:String
    houseDesc:String
}
```

画面 6:
```text
第一步，将资料中的haoke-web.zip解压到项目目录，我的是：F:\code\itcast-haoke\itcast-haoke-web
```

画面 7:
```json
{
  "data": {
    "list": [
      {
        "original": "http://127.0.0.1:8086/public/1.png"
      },
      {
        "original": "http://127.0.0.1:8086/public/2.png"
      },
      {
        "original": "http://127.0.0.1:8086/public/3.png"
      }
    ]
  },
  "meta": {
    "Status": 200,
    "msg": "测试数据"
  }
}
```

画面 8:
```text
3.3.2、创建common工程
创建itcast-haoke-manage-dubbo-server-common工程，将BasePojo、BaseServiceImpl移动至该工程。
```

画面 9:
```javascript
let swipe = new Promise((resolve, reject) => {
    axios.post('/homes/swipe').then((data) => {
        axios.get('http://127.0.0.1:18080/ad').then((data) => {
            resolve(data.data.list);
        });
    });
});
```

画面 10:
```text
可以看到，成功的获取到数据。
```

画面 11:
```graphql
schema {
    query: HaokeQuery
}
```

画面 12:
```text
Apollo Client (github)：一个强大的 JavaScript GraphQL 客户端，设计用于与 React、React Native、Angular 2 或者原生 JavaScript 一同工作。
```

画面 13:
```java
package cn.itcast.haoke.dubbo.api.controller;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import graphql.GraphQL;
```

画面 14:
```json
{
  "data": {
    "IndexAdList": [
      {
        "list": [...],
        "__typename": "IndexAdResult"
      }
    ]
  },
  "meta": {
    "msg": "成功",
    "status": 200
  }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: 标题为“课程介绍”，列出课程内容要点。
画面 2: 标题为“1.1.1、定义接口方法”，展示接口定义代码。
画面 3: 标题为“1.4、编写GraphQLController”，展示控制器代码。
画面 4: 标题为“1.7、优化改进GraphQLProvider逻辑”，展示问题和改进思路。
画面 5: 标题为“1.1.1、定义接口方法”，展示 GraphQL 查询类型定义。
画面 6: 标题为“2.1、搭建工程”，展示工程搭建步骤。
画面 7: 标题为“1.7、优化改进GraphQLProvider逻辑”，展示 GraphQL 查询返回数据。
画面 8: 标题为“3.3、实现查询接口（dubbo服务）”，展示分析和创建 common 工程。
画面 9: 标题为“4.5、整合前端系统”，展示修改 home.js 文件。
画面 10: 标题为“4、广告服务的GraphQL接口”，展示成功获取数据。
画面 11: 标题为“4.2、编写haoke.graphqls”，展示 GraphQL 文件内容。
画面 12: 标题为“4.6、GraphQL客户端”，展示客户端工具列表。
画面 13: 标题为“4.6、GraphQL客户端”，展示问题和解决方案。
画面 14: 标题为“4.6、GraphQL客户端”，展示成功获取数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
