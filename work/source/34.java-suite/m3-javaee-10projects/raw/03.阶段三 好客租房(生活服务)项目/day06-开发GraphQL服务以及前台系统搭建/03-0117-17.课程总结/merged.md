# 17.课程总结

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day06-开发GraphQL服务以及前台系统搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day06-开发GraphQL服务以及前台系统搭建\17.课程总结【海量资源尽在 ubkz.com】.mp4
- 时长 5分29秒（音频 329s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们对今天的课程内容呢做一个总结今天呢我们做了哪些内容呢我们来看一下那我们使用GrabQL来开发了我们房源的接口那开发了有两个接口那么第一个呢就是我们根据ID去查找房源第二个呢就是我们查询房源的一个列表OK那么前面呢我们先实现的是一个double的一个服务对吧在实现完成之后呢我们就开始去编写
[00:30] GrabQR这样的一个服务那么我们去在编写我们GrabQR服务的时候呢我们需要注意的是我们需要把GrabQR的客户端需要跟我们的Spring是不是做一个整合对吧做一个整合那么整合之后呢才能够去做这样的一个服务的一个查询那么我们关键的一个逻辑是不是在这个provider这个里面啊provider这个里面哎OK这个里面的代码逻辑大家一定要
[00:58] 能够看懂啊并且也能够把它写出来OK然后呢我们后面是不是去讲了一些他的一个改进啊改进那么为什么要改进包括他的一些改进的思路啊这个点希望大家能够学会啊能够学到手然后呢我们是不是安装了一个他的一个插件啊他这个插件这个呢需要大家去解决一下那个翻墙的一个问题啊OK
[01:23] 好然后我们往下面走去查询这个房源这个呢其实就相对比较简单了那么只是按照我们的一个结构去做一个定义就可以了然后呢我们后面的去实现我们的一个这个接口对吧这个叫mydatafetcher这样的一个接口实现这个接口就OK了好然后呢我们去搭建我们的前台系统那么搭建前台系统呢大家按照这个步骤的一步一步去做一个搭建相信是没有问题的啊OK
[01:53] 好那么我们在分析我们的这个首页这个轮播广告这个功能的时候呢我们去看到他的一些这个数据结构数据结构并且呢针对数据结构呢去做出我们后台数据库的一个设计那么我们知道的一点是我们做的这个后台这个结构呢他并不是真并不简单的为首页的这个轮播广告做一个实践而是为我们整站的一个广告
[02:20] 去做这样的一个实现大家这个定位的一定要清楚OK那么下面的就做了一些这个实现当然了我们抽取了一个common工程为什么要抽取这个就不做重复了我们在前面的讲解中的也做了一些详细的一些讲解OK好那么下面我们就去实现了他具体的一些逻辑这个我们就不做重复了OK那么在实现完成之后我们当然我们实现这个是RESTful的接口
[02:49] 最后我们跟前端是不是做了一个整合那么整合之后呢会发现有个跨域的问题最终我们也解决了对吧然后呢最后是不是可以跟我们前端是不是整合起来但是呢我们只是通过rest4这种方式做整合那么如果我们后端改成grabqr这种方式那么又该如何去做一个整合那我们是不是就去把我们的广告的服务是不是改造成了grabqr这种接口的这种方式OK
[03:17] 那我们对他的一个数据结构呢做了一些这个优化啊做了一些这个优化那么原来这个优化呢原来这个数据结构呢不是特别的理想所以做了一些这样一个优化那么我们就去实现了这样的一个GrabQ的一个服务那么在我们实现之后啊那么我们就去去整合我们的前端做开发但是我们前端的有如何去调用我们的GrabQ这就成了一个技术问题所以呢我们会发现
[03:45] 官网呢其实有列出啊一些这个关于JS啊的一些相关的一些这个第三方的一些实现那我们采用的第二个这个实现就是Apollo Client啊它呢是一个比较好用的这样的一个客户端工具那么具体用法呢我们刚刚也都用到了啊然后呢最后呢它也会遇到一个我们的一个跨域的问题然后呢我们把它解决掉了
[04:08] 当然我们也做了一个POST这样的一个处理那么也就是说现在我们这个GrabQ这个服务它其实相对还是比较完整的一个服务它既支持get请求也支持这个POST请求对不对OK那么最后那么我们把这个问题解决了那么也就最后呢我们成功的在客户端是不是调用了GrabQ所定义的服务那么现在呢我们是不是我们这个系统所定义了两套服务一个呢是我们的RESTful
[04:37] 另外一个是WebQL这两套服务是不是都能够成功的现在调用通了对吧OK好那么这样的话我们去设计的这样的一个效果也就达到了OK好那么这个就是我们今天的内容当然我们今天的内容主要就是围绕着我们的一个WebQL的一个接口那么后端怎么样去定义如何跟我们的Spring做整合前端又该如何去定义
[05:04] 然后呢我们使用了前台系统的一个轮播广告的这样的一个功能把这样的一个这个技术点把它串起来去做了一个展现OK也希望大家呢从中呢能够去学到一些技术包括我们在编码时候的一些技巧OK好那么今天的内容呢我们就讲这么多OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
本课程讲解如何使用 GraphQL 开发房源接口、实现广告系统，并整合前端系统，涉及 Spring Boot、Dubbo、Apollo Client 等技术。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 课程介绍，列出核心内容：使用 GraphQL 开发房源接口、实现房源列表查询接口、搭建前后端系统、实现首页轮播广告功能、改造广播广告接口方式为 GraphQL、学习使用 Apollo Client 的使用。
画面 2: 展示 HouseResourcesService 接口定义，包含 import 语句和 @Transactional 注解。
画面 3: 展示 GraphQLController 的 import 语句，包括 GraphQL.GraphQL、@Autowired、@Controller 等。
画面 4: 讲解优化 GraphQLProvider 逻辑的问题，指出当前方法难以维护，并提出改进思路：编写接口、所有实现查询的逻辑都实现该接口、在 GraphQLProvider 中使用该接口进行处理、以后新增查询只需增加实现类即可。
画面 5: 展示 GraphQL 查询类型定义，包括 HouseResources 对象的字段，如 id、title、estateId、buildingQuint、rent、rentMethod、paymentMethod、houseType、coveredArea、useArea、floor、orientation、decoration、pic、houseDesc 等。
画面 6: 讲解搭建工程，第一步是将资料中的 haoke-web.zip 解压到项目目录。
画面 7: 展示 GraphQL 查询返回的数据结构，包含 data.list 和 meta.status、msg。
画面 8: 讲解实现查询接口（dubbo服务），分析首页轮播广告功能需要独立的 dubbo 服务，并创建 common 工程。
画面 9: 讲解整合前端系统，修改 home.js 文件中请求地址，使用 axios.post 发送请求。
画面 10: 展示成功获取到 GraphQL 接口的数据。
画面 11: 展示 haoke.graphqls 文件内容，定义 schema 和 query: HaokeQuery。
画面 12: 讲解 GraphQL 客户端，介绍 Apollo Client、GraphQL-request、Lokka、nogql、AWS Amplify 等。
画面 13: 发现两个问题：GraphQL 服务不支持 cross、Apollo Client 发起的请求为 POST，而当前 GraphQL 仅支持 GET。并展示相关代码。
画面 14: 展示成功获取到数据，页面效果实现。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
import cn.itcast.haoke.dubbo.server.pojo.HouseResources;
import cn.itcast.haoke.dubbo.server.Service.HouseResourcesService;
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
package cn.itcast.haoke.dubbo.api.Controller;
import GraphQL.GraphQL;
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
```GraphQL
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
```GraphQL
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
package cn.itcast.haoke.dubbo.api.Controller;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import GraphQL.GraphQL;
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

