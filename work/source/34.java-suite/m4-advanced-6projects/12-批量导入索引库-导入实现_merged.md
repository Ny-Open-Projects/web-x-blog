# 12-批量导入索引库-导入实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

我们接着基于刚才所写好的一个应用设置对象开始实现将秒杀商品批量查出来,然后导入到我们EleticSearch的一个索引库中。

那这一块呢,我们要集成SpendDataEleticSearch来实现。

那要集成SpendDataEleticSearch呢,首先第一个要配置一下我们EleticSearch的一个地址信息,然后编写我们的DL接口。

DL接口需要集成EleticSearchRepository,紧接着我们需要在Service中去调用我们的查询,然后将秒杀商品批量导入到我们的索引库中。

好,在这一块我们看一下我们EleticSearch的一个地址信息。

这一块呢是我们当前要操作的ES索引库的一个配置信息,它的名称叫EleticSearch,IP是这个。

行,我们开始配置一下。

来,在这一块呢,我们先配置这个ES的连接信息,把我们的Botch.yaml打开,添加这一段配置。

在Spring节点下添加。

好了,就这一个。

节点的名称叫EleticSearchLim,下面是它的一个IP和端口号。

接着我们开始去实现整体的操作了。

在这一块我们把包给写传了。

Controller。

还有一个是Service。

还有一个是DAO。

好,这一块写传了。

紧接着我们就开始去写一下我们的DAO。

DAO写完之后再写Service,因为Service要调用DAO。

好,我们来写一下。

写一个叫SKU Info Map。

它需要继承。

ElecticSearchRepository。

这里注意这个范形写SKU Info,表示你用当前这个DAO去操作索引库的时候,它其实是操作这个对象所对应的索引库。

后面写当前这个对象它的唯一标识,它对应的类型。

这个ID是唯一标识,对应的类型是字符串类型,所以我这里写个String。

可以了。

好,在这一块写完了。

接着我们就开始去写我们的业务层。

右键新建一个叫SKU Info Service,IMPL。

好,把它给载进去。

然后这里实现一个接口SKU Info Service。

这个接口没有,我们就创建一个。

接口也创建了。

这个内不要忘了把它交给容器去管理。

好,我们现在就来看我们的设计。

我们现在就来看我们的设计。

我们现在就来看我们的设计。

我们现在就来看我们的设计。

我们现在就来看我们的设计。

我们现在就来看我们的设计。

我们现在就来看我们的设计。

好,我们现在开始写这一块批量导入的一个方法。

写个OID,ADD,OR,这是批量导入。

这个实现呢,我们也来写一下批量导入。

那这一块该怎么做呢?

这一块很简单,我们分析一下整个流程。

第一个步骤,我要先去查询总记录数。

因为我要分页查询呀,先查询总记录数。

然后做这么一个事,根据总记录数查询,计算总页数。

总页数有了,然后去查询每页就可以了。

循环总页数,查询每页的数据。

每页的数据查出来了,接着将数据转换成SKUINFO。

为什么?

为什么要转成SKUINFO呢?

因为我们从我们商品微服务查出来的对象是SKU。

而我要把它转成SKUINFO,才能添加到我们索引库去。

这是这个流程。

接着我们按这个流程来实现一下。

那这个时候需要导入我们的份接口对象,SKU份。

SKU份。

还需要导入我们的DAO,Privacy。

SKUINFOMAP。

好,开始实现这个过程。

第一个步骤,先去查询总数据,点Count。

于是总的数量就有了,Total。

总数量有了,那一会儿我希望每页显示多少条呢?

我写一个配置,int配置定1。

从第一页查询,每页显示500条。

这个是分页数据。

好,我们开始。

开始去查询。

但查询得先计算这一块总共有多少页。

写个int,totals,total配置。

等于当前这个总记录数除以每页显示的条数。

如果能整除,那么就是它俩相除。

如果不能整除呢,它俩相除,记得加1。

好,总页数算出来了。

接着就是循环总页数,查询每页的数据。

那每页的数据这个查询呢也容易了。

我们看一下这一块,从它里面去查询即可。

点有一个list,当前页配置,size给它。

那么于是这个集合就拿到了,skus。

查询到了之后,需要将它转成skuinfo对不对?

所以我们要转一下list,skuinfo。

好,我们来看看。

好,我们来看看。

好,转一下。

好,转一下。

好,转一下。

好,转一下。

这一块转换搞定了。

接着我们就开始进行批量保存。

用我们的do接口去批量保存。

save all,把当前这个集合给它,就可以了。

这个是批量保存。

这一块写完了,但是还有一个小问题。

什么问题呢?

就是我们这一块给了它一个新的属性,叫bgtime。

bgtime呢,是开始时间。

bgtime呢,是开始时间。

所以需要把上面这个开始时间转一下。

把下面这个开始时间给转成我们的一个,这个是我们对应的一个字母串类型时间,把它转一下。

好,这个转换呢,我先简单写一下,非常的简单哈。

在这里写个for循环就可以了。

skuinfo.for循环。

skus.

行,咱这一块它这个就循环不了哈。

好,这个转换呢,我先简单写一下,非常的简单哈。

在这里写个for循环就可以了。

skuinfo.for循环。

skus.

行,咱这一块它这个就循环不了哈。

好,咱这一块它这个就循环不了哈。

我看一下哈,可以了,刚才可能有点小问题。

这个是循环,循环做什么事情呢?

将开始时间转换成字符串类型。

来,那你这里得有开始时间才行,是不是?

得有开始时间才行哈。

我得写个,如果此时当前skuinfo.getbegin不等于long,我才进行转换。

是不是?

那进行转换怎么转换呢?

simple,simple data format。

6 simple data format。

转成什么类型呢?

年月日。

好,转成这个类型就可以了。

我们来转换一下哈。

那这个时候转换一下就可以了。

把当前这个skuinfo.getskubegin给它就行了。

把当前这个skuinfo.getskubegin给它就行了。

再把它复制给当前这个skuinfo.getskubegin。

再把它复制给当前这个skuinfo.getskubegin。

再把它复制给当前这个skuinfo.getskubegin。

再把它复制给当前这个skuinfo.getskubegin。

再把它复制给当前这个skuinfo.getskubegin。

就可以了,就这么实现。

行,那这一块我们就搞定了。

接着就是我们的控制层要去调它,所以我们再写一个控制层。

我们就写个search,control,在这里写个reset control,request mapping。

value 就给个search,不要忘了跨域close origin。

好,写第一个方法,批量导入。

那么批量导入呢,写个public result,叫addall就行了。

这里呢,就给个get mapping。

地址我们就写个addall,

new result,status code.ok。

这个对象我们前面已经讲过了,后面我们就直接用了。

信息是批量导入成功。

好了,接着开始去实现批量导入。

那它是不是要把我们的service接口给注入进来啊?

好,注入进来。

然后开始去调用实现我们的批量导入addall即可。

ok,我们这一块就搞定了。

那一会儿想要测试的话,得启动我们当前程序。

所以我们还要写一个启动类,叫做search。

application。

启动类呢,遵循我们supermboot的原则。

这一块要注意,把数据源给相关的启动给禁止掉。

data,data source。

好,还有一个注意一下啊。

我们这一块还要做什么事情呢?

还要去扫描我们,扫描我们deo接口。

写个叫enableElectricSystem。

我们要设起reportory,base package,写一下我们的deo。

deo的路径在这一块,右键copy一下就行了。

除了这个之外呢,还没有别的地方呢?

注意,还有一个是我们的Fend接口。

这一块要指定一下。

EnableFendClient。

Base package,这一块也要写一下。

这个Fend接口呢,注意在这个API对应的包里。

找到这个。

拷贝一下。

好了,这一块就搞定了。

接着是启动

对应的MEM方法

sperm

application.run

当前这个对象的直接码给他点class

args

搞定了。

我们现在就可以去进行一个测试了。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程是关于一个名为“秒杀系统”（seckill）的 Java 项目中，如何使用 Spring Data Elasticsearch 实现商品搜索功能的实战教学。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何配置 Elasticsearch、创建索引映射、编写服务层代码以批量导入商品数据，并最终通过 REST API 提供搜索服务。整个过程围绕“商品搜索”模块展开，重点在于 Spring Boot 与 Elasticsearch 的集成，以及如何处理分页和数据转换。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：课程开场，展示项目结构和当前学习的模块“商品搜索”。
*   **00:00:05 - 00:00:15**：讲解 Spring Data Elasticsearch 的集成流程，包括配置地址、编写 DAO、在 Service 中调用、分页导入。
*   **00:00:15 - 00:00:30**：在 `SkullInfoServiceImpl.java` 中编写 `addAll1()` 方法，用于批量导入商品数据。
*   **00:00:30 - 00:00:45**：在 `SkullInfo.java` 中定义 Elasticsearch 的索引映射（`@Document` 和 `@Field` 注解），并配置分词器。
*   **00:00:45 - 00:01:00**：在 `SkullInfoServiceImpl.java` 中实现分页查询逻辑，使用 `skuFeign` 获取数据并转换为 `SkullInfo` 对象。
*   **00:01:00 - 00:01:15**：使用 `SimpleDateFormat` 格式化日期，并调用 `SkullInfoMapper.saveAll()` 方法将数据批量写入 Elasticsearch。
*   **00:01:15 - 00:01:30**：编写 `SearchController.java`，定义一个 REST API 接口 `/search`，用于接收前端搜索请求。
*   **00:01:30 - 00:01:45**：在 `SearchApplication.java` 中配置 `@EnableElasticsearchRepositories` 和 `@EnableFeignClients`，并启动应用。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   **集成 Spring Data Elasticsearch 实现索引导入流程**：
        1.  配置 Elasticsearch 地址信息。
        2.  编写 DAO 代码，继承 `ElasticsearchRepository<T, ID>`。
        3.  在 Service 中分页调用查询秒杀商品集合。
        4.  分页导入秒杀商品集合数据到 Elasticsearch 中。
    *   **项目结构**：左侧导航栏展示了项目模块，如 `seckill-canal`, `seckill-goods`, `seckill-search` 等。

*   **关键代码**：

    *   **Elasticsearch 索引映射类 `SkullInfo.java`**：
        ```java
        @Document(indexName = "goodsindex", type = "skullinfo")
        public class SkullInfo {
            @Id
            private String id;
            
            @Field(type = FieldType.Text, searchAnalyzer = "ik_smart", analyzer = "ik_smart", store = false)
            private String name;
            
            // ... 其他字段
        }
        ```

    *   **服务层 `SkullInfoServiceImpl.java` 中的 `addAll1()` 方法**：
        ```java
        @Override
        public void addAll1() {
            // 1. 查询总记录数
            Integer total = skuFeign.count();
            
            // 2. 根据总记录数计算总页数
            int totalpages = total % size == 0 ? total / size : total / size + 1;
            
            // 3. 循环分页，查询每页的数据
            for (int i = 0; i < totalpages; i++) {
                List<Sku> skus = skuFeign.list(page, size);
                
                // 4. 将数据转换成 SkullInfo
                List<SkullInfo> skullInfos = JSON.parseArray(JSON.toJSONString(skus), SkullInfo.class);
                
                // 5. 批量保存
                skullInfoMapper.saveAll(skullInfos);
            }
        }
        ```

    *   **控制器 `SearchController.java`**：
        ```java
        @RestController
        @RequestMapping("/search")
        public class SearchController {
            // ... 业务逻辑
        }
        ```

    *   **主启动类 `SearchApplication.java`**：
        ```java
        @SpringBootApplication(exclude = DataSourceAutoConfiguration.class)
        @EnableElasticsearchRepositories(basePackages = "com.seckill.search.dao")
        @EnableFeignClients(basePackages = "com.seckill")
        public class SearchApplication {
            public static void main(String[] args) {
                SpringApplication.run(SearchApplication.class, args);
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构与集成流程**（00:00:05）
    *   讲师在 IDEA 中展示了项目结构，重点讲解了 `seckill-search` 模块。
    *   通过 PPT 展示了 Spring Data Elasticsearch 的四步集成流程，并强调当前项目已集成好，只需实现操作即可。

*   **场景二：编写服务层代码**（00:00:30）
    *   讲师在 `SkullInfoServiceImpl.java` 中编写 `addAll1()` 方法。
    *   通过 IDEA 的代码提示功能，快速引入 `skuFeign` 和 `skullInfoMapper`。
    *   代码中使用 `skuFeign.count()` 获取总记录数，然后通过 `for` 循环分页查询数据。
    *   使用 `JSON.parseArray` 将 JSON 数组转换为 `SkullInfo` 对象列表。
    *   最后调用 `skullInfoMapper.saveAll(skullInfos)` 将数据批量写入 Elasticsearch。

*   **场景三：配置索引映射**（00:00:45）
    *   讲师在 `SkullInfo.java` 中使用 `@Document` 注解指定索引名称和类型。
    *   使用 `@Field` 注解配置字段的类型、分词器等属性。
    *   特别强调了 `searchAnalyzer` 和 `analyzer` 都设置为 `"ik_smart"`，用于中文分词。

*   **场景四：编写控制器与启动应用**（00:01:15）
    *   讲师在 `SearchController.java` 中创建一个 `@RequestMapping("/search")` 的 REST API。
    *   在 `SearchApplication.java` 中添加 `@EnableElasticsearchRepositories` 和 `@EnableFeignClients` 注解，以启用相关功能。
    *   最后点击运行按钮，启动 Spring Boot 应用。

*   **场景五：调试与验证**（00:01:30）
    *   讲师在 `SearchController.java` 中添加了 `@CrossOrigin` 注解，以支持跨域请求。
    *   通过 IDEA 的调试功能，验证了 `addAll1()` 方法的执行流程。
    *   在控制台输出“批量导入成功！”信息，表明数据已成功写入 Elasticsearch。

---

以上是根据视频画面进行的结构化分析，旨在帮助理解课程内容和实现细节。
