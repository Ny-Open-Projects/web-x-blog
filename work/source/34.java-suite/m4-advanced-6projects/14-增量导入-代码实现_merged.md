# 14-增量导入-代码实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接着我们来做一下增量导入

增量导入是什么意思呢

刚才我说过批量导入

在以后项目启动之后

有可能只用一次

对吧

也有可能不会用

那这个时候增量导入是什么意思呢

增量导入跟批量导入的区别点在这一块

批量导入是导入所有

一般只用于数据初始化

所以我们用的很少

增量导入呢

就是数据库数据发生变化的时候

我只更新指定的数据就可以了

比如我增加一条商品数据

那么我会往索引库数据里面

导入那一个商品信息

比如我数据库数据对应的某一个商品更新了

那对应的索引库里面

那一个商品的信息跟着更新

如果数据库里面删除了一个商品

索引库里面那一个商品信息删除就可以了

这个就是我们这儿的一个增量更新

好

接着我们来实现一下这个增量更新

增量更新呢

其实也非常的简单

我们只需要去写一个删除方法就可以了

好

我们在这一块来写一下

这里找一个

好

找一个上面一点的地方来写

这个写一个叫增量操作

那么这里有可能会做这么一个事情

删除索引

还有可能会做什么事情呢

修改索引

还有一个就是

添加索引

好

我希望在一个方法里面把这三个都给实现

写个oid modify

那这一块这个方法应该要区分类型才对

删除修改增加对应的类型

比如我给它一个type

那这个type

这个type应该是这个方法的内容

用来做什么事情呢

用来记录当前所做的操作

如果是3

type等于几呢

type等于3

如果是修改

type等于2

好

如果是增加呢

那我就让type等于1

这就可以了

用一个列来标识所操作的类型

另外一个呢

就是你要操作的对象

skuinfo

你直接把它转成skuinfo给我才行

然后呢

就是这个方法

这是我们这个方法

接着我们给它写一个实现

在这一块oid建回车

实现这个方法

行

这个注释呢

我就要考过来就可以了

这是这一块

我们先说说第一个

当它等于增加

等于修改的时候

其实就是把当前这个索引数据

添加到索引库去就可以了

因为它这里修改呢

会先把之前的数据给删掉

然后呢

它会再增加新的数据

所以我们可以做一个判断

如果此时type很等于1

或者是type很等于2的时候

直接做增加

增加和修改

当然其实本质就是增加

skuinfo map点写个save

把这个对象给它就行了

可以了

好

那如果是删除呢

如果是删除呢

这个简单了

剩下的是不是就等于3了呀

等于3就删除嘛

skuinfo.delete

好delete byid

把当前skuinfo

对应的id给传过来就行了

这是我们这个service

这一块的实现

接着我们再去写它的一个控制层了

把这一块打开

添加一个控制的方法

public result modify new result

这一块写个tue

写个status code

点ok

然后这一块写一个叫操作成功

OK了

我们这一块给它一个请求地址

写个叫put map

value这一块写modify

后面是后面咋写呢

所以我需要你给我一个操作的内容

一个操作的内容type

然后还需要你request body

还需要你把要操作的数据给我传过来

行了这是这一块

这一块写了之后

它主要是供我们内部使用

到时候谁要用它

直接调这个接口就行了

调这个接口

我们需要把它写到我们的份里面去

到时候其他的微服用份来进行调用就可以了

好我们把这个设计对应的API打开

在这一块写一个份接口

这里右键新建一个接口

叫skuinfo-fun

上面这里写个叫funclient

写上我们对应的微服务

sql-search

然后把这个接口给写过来

这里把它给去掉

注意前面加一个search

行

于是这一块我们就搞定了

这个增量实现也就已经写完了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面截图，对这段技术课程进行的结构化中文输出。

---

### 1) 视频摘要

本视频课程主要讲解如何在“秒杀”项目中，通过 Spring Boot 和 Spring Cloud 的 Feign 客户端，实现对商品 SKU（库存单位）信息的增删改操作。讲师首先在 Elasticsearch 中展示了商品数据的索引结构，随后在代码层面，从服务接口 `SkuInfoService` 开始，逐步实现并演示了 `modify` 方法的逻辑。该方法根据传入的类型（type）参数，决定是调用 `SkuInfoMapper` 的 `save` 方法（新增或修改）还是 `deleteById` 方法（删除）。最后，讲师展示了如何在 `SearchController` 中定义对应的 REST API 接口，并通过 Feign 客户端 `SkuInfoFeign` 将服务调用暴露给外部。整个过程旨在构建一个可维护、可扩展的搜索服务架构。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开头，展示 Elasticsearch 的数据界面，列出商品索引 `goods_sku` 的部分数据，包括 `id`, `name`, `price`, `seckillId` 等字段，为后续操作提供数据背景。
*   **00:05 - 00:15**: 讲师切换到 IntelliJ IDEA，展示项目结构，定位到 `search-service` 模块下的 `SkuInfoService` 接口文件。
*   **00:15 - 00:25**: 在 `SkuInfoService` 接口中，讲师定义了 `modify` 方法，该方法接收一个整型 `type` 和一个 `SkuInfo` 对象作为参数，用于区分不同的操作类型。
*   **00:25 - 00:40**: 讲师进入 `SkuInfoServiceImpl` 实现类，开始编写 `modify` 方法的具体逻辑。他首先定义了 `@Autowired` 注入的 `SkuInfoMapper` 和 `SkuFeign` 两个依赖。
*   **00:40 - 00:55**: 在 `modify` 方法中，讲师编写了核心逻辑：如果 `type` 为 1（新增或修改），则调用 `skuInfoMapper.save(skuInfo)`；否则，调用 `skuInfoMapper.deleteById(skuInfo.getId())` 进行删除。
*   **00:55 - 01:10**: 讲师切换到 `SearchController`，定义了 `@PutMapping` 的 `modify` 接口，用于接收前端的修改请求。
*   **01:10 - 01:25**: 讲师在 `SearchController` 中定义了 `@GetMapping` 的 `addAll` 接口，用于批量导入数据。
*   **01:25 - 01:40**: 讲师切换到 `SkuInfoFeign` 接口文件，使用 `@FeignClient` 注解将其命名为 `seckill-search`，并定义了与 `SkuInfoService` 对应的 `modify` 方法。
*   **01:40 - 01:55**: 讲师在 `SkuInfoFeign` 接口中，为 `modify` 方法添加了 `@PutMapping` 注解，并指定了请求路径 `/search/modify/{type}`。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段**:
    *   **`SkuInfoService` 接口**:
        ```java
        public interface SkuInfoService {
            // 增量操作 ->删除索引 type=3
            // ->修改索引 type=2
            // ->添加索引 type=1
            void modify(Integer type, SkuInfo skuInfo);
        }
        ```
    *   **`SkuInfoServiceImpl` 实现类**:
        ```java
        @Service
        public class SkuInfoServiceImpl implements SkuInfoService {
            @Autowired
            private SkuInfoMapper skuInfoMapper;
            @Autowired
            private SkuFeign skuFeign;
            @Override
            public void modify(Integer type, SkuInfo skuInfo) {
                if(type==1 || type==2) {
                    skuInfoMapper.save(skuInfo);
                } else {
                    skuInfoMapper.deleteById(skuInfo.getId());
                }
            }
        }
        ```
    *   **`SearchController` 控制器**:
        ```java
        @RestController
        @RequestMapping("/search")
        public class SearchController {
            @Autowired
            private SkuInfoService skuInfoService;
            @PutMapping(value = "/modify/{type}")
            public Result modify(@PathVariable Integer type, @RequestBody SkuInfo skuInfo) {
                skuInfoService.modify(type, skuInfo);
                return new Result(true, HttpStatus.OK, "操作成功！");
            }
            @GetMapping(value = "/add/all")
            public Result addAll() {
                // 分页数据
                int page=1,size=500;
                // ... 其他逻辑
            }
        }
        ```
    *   **`SkuInfoFeign` 接口**:
        ```java
        @FeignClient(name = "seckill-search")
        public interface SkuInfoFeign {
            @PutMapping(value = "/search/modify/{type}")
            Result modify(@RequestBody SkuInfo skuInfo);
        }
        ```

*   **关键注解**:
    *   `@FeignClient`: 用于定义 Feign 客户端，指定服务名称。
    *   `@PutMapping`: 用于定义 HTTP PUT 请求的接口。
    *   `@GetMapping`: 用于定义 HTTP GET 请求的接口。
    *   `@RequestBody`: 用于将 HTTP 请求体中的 JSON 数据绑定到方法参数。
    *   `@PathVariable`: 用于从 URL 路径中提取参数。

---

### 4) 关键场景与演示描述

*   **场景一：数据展示与接口定义** (00:00-00:15)
    *   讲师首先在浏览器中打开 Elasticsearch 的 Kibana 界面，展示了 `goods_sku` 索引中的商品数据，包括 `name`, `price`, `seckillId` 等字段，为后续的增删改操作提供数据基础。
    *   接着，讲师在 IntelliJ IDEA 中打开 `SkuInfoService` 接口，定义了 `modify` 方法，明确了服务层的契约。

*   **场景二：服务实现逻辑编写** (00:15-00:55)
    *   讲师进入 `SkuInfoServiceImpl` 类，开始实现 `modify` 方法。
    *   他首先通过 `@Autowired` 注入了 `SkuInfoMapper` 和 `SkuFeign` 两个依赖。
    *   在方法内部，他使用 `if(type==1 || type==2)` 判断条件，决定是调用 `save` 方法（用于新增或修改）还是 `deleteById` 方法（用于删除）。
    *   他通过 `skuInfoMapper.save(skuInfo)` 和 `skuInfoMapper.deleteById(skuInfo.getId())` 来执行具体的数据库操作。

*   **场景三：控制器接口与 Feign 客户端配置** (00:55-01:40)
    *   讲师在 `SearchController` 中定义了 `@PutMapping` 的 `modify` 接口，用于接收前端的修改请求，并调用服务层的 `modify` 方法。
    *   他同时定义了 `@GetMapping` 的 `addAll` 接口，用于批量导入数据。
    *   讲师切换到 `SkuInfoFeign` 接口，使用 `@FeignClient` 注解将其命名为 `seckill-search`，并定义了与服务层对应的 `modify` 方法。
    *   他为 `modify` 方法添加了 `@PutMapping` 注解，并指定了请求路径 `/search/modify/{type}`，以便外部服务可以通过 Feign 客户端调用此接口。

整个演示过程清晰地展示了如何在微服务架构中，通过定义接口、实现逻辑、配置 Feign 客户端，来完成对商品 SKU 数据的增删改操作。
