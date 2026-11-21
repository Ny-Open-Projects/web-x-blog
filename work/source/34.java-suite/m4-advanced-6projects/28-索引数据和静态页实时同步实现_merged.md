# 28-索引数据和静态页实时同步实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

我们接着开始讲数据实时同步这一块

那数据实时同步呢

就包含我们的索引实时同步和静态文件实时同步

那这一块我们先讲解这个索引实时同步

当我们TBSKU里面这个商品发生变化的时候

我们应该让索引同步跟着发生变化

比如增加了商品

那这个时候商品如果是秒杀商品

那我们就应该去增加我们的索引数据

如果是修改了那索引数据要跟着变

如果是删除了这个商品

那秒杀里面的那个索引数据也得跟着删除

好我们来实现一下

在刚才这个案例上面来实现就可以了

在这一块呢

注意我要去调用我们搜索微服了

对不对

所以我要把搜索微服

它的一个

这个份接口给写过来

SKU

叫

search

份

好我们看一下是哪个接口

我们看一下这个搜索这里

叫SKU info份

把它给注入进来

autoride

注入进来之后

开始做一些操作

如果你是增加

那我这个时候要添加索引信息

但有个前提

前提是

你当前商品这一块

它必须是状态必须是二

必须是二

还有一个时间结束时间

你不能结束了

当然这个结束的时间没有结束这个事情

咱就不去做这个判断了

如果你这个时间都结束了

你添加这个商品也没有意义

对不对

所以这个时间我就不去判断了

好我写个判断

一幅

当前SKU.getStatus

横等于二的时候

这个时候就要去添加我们的索引数据

点有一个叫Modify

这一块我们简单看一下Modify

这好像有问题对吧

我们看看Modify状态

是设起Modify

要把这个参数一起传过来

那么一起传过来的话

我那边还要接这个数据

那咱们刚才说的这个参数一起传过来的话我那边还要接这个数据

那咱们刚才这个接数据是不是没有接啊

这里应该要有个PathVariable

Value.type

Integral type

这样才对

那把这个同步增加到我们刚才写的搜索那一块

在搜索这里也要有这个参数才行

这个咱没有测试

所以当时这块就没有写上去

好我们找到这个方法

在这里

把它给加上来

就可以了

好我们这个时候

如果是

如果是秒杀商品

我们就要去调这个Modify

类型呢

其实你做增加就写1就行了

对吧

好后面是什么呢

是当前这个SKU数据

但是你要把它转成SKU info

所以这个时候我们就把它给转一下哈

json.tool.std

然后把它转成Modify.tool.std

然后把它转成Modify.tool.std

然后把它转成我们的SKU info

json.pathobject

把它转成SKU info.class

好了

这是这一块

下面这个呢

注意下面这个是修改了

那修改这一块也有一些问题点哈

第一个问题点是什么呢

就是它这一块状态

如果之前是没有参与过的问题的话呢

如果之前是没有参与过的问题的话呢

如果之前是没有参与过的问题的话呢

如果之前是没有参与过的问题的话呢

如果之前是没有参与过的问题的话呢

如果现在参与秒杀

那现在参与秒杀

那肯定是要增加索引数据的

对吧

我们做一个判断

如果此时叫

after.getStatues.ecourse

只要它等于二

只要它等于二

就是秒杀数据了

那么关于这个活动结束时间

我仍然不做判断了

它这里只要当前这一块这个状态是二

那就是一定参与秒杀的

对吧

就这一块

好

但是还有这么一种可能性存在

之前是参与秒杀

现在把它换了

不参与秒杀了

有没有可能呢

也有可能

好了

这个时候我们再来做另外一个判断

else if

else if

如果说此时

此时before里面

如果此时before里面

.getStatues.ecourse

几呢

如果之前是二

那么现在是几呢

现在是一

.getStatues.ecourse

现在是一

那就说明这一块发生了转变

对吧

好

像上面这一块

无论你怎么操作

那它的类型都是增加或者是修改

对不对

我们写个类型

type等于一

那到这一块来的话

它的type你可以写个一

没有关系的

你写个二也行

因为一是整个的

一是增加二是修改

对吧

就这一块

这个就不用去管它了

好

接着往后面继续看

但如果是这种类型的

这种操作了

那它就是三要做删除了

对吧

那还有没有别的情况呢

别的情况我们就暂时不考虑了

我们现在只考虑这两种现象

那这一块一整之后

紧接着我们就实现一下索引的管理

SKU info.modifier

索引的管理

这儿写type

紧接着里面仍然是对象进行转换就行了

但是这个转换应该是after之后的

好

这是这一块

那么删除这一块

我们删除就不做讲解了

因为我们这一块数据一般不会真实删除的

所以这个删除我们就不做讲解了

好

这是我们索引数据实时同步

接着我们再来看这个

再往后面看还有一个叫静态页的一个同步

那静态页的同步呢比较简单哈

我们把静态页的

静态页的份接口导入进来

SKU配给

把它给注入进来

然后开始去调用对应的方法

这不是增加吗

那么增加这一块

这个就要同步

静态页了

那上面也是

同步索引

同步静态页写一下点静态页

现在肯定是生成对不对

SKU给他就搞定了

我们看一下这一块

SKU要把它转成我们的节省数据

对吧

我们看一下这一块哈

这里要抛出一个异常就行了

行

这是这个

紧接着我们再看下面这里也是一样的哈啊

大家看等于二的时候表示增加

等于三的时候表示删除

所以我们可以在这里做一下

那在上面做这个是增加在这里做了

这里是不是做删除啊

删除的话

after.getid给他就可以了

如果是这一块做增加了

把after给他

好

我们看这一块应该也是一个异常

对吧好

这一块就搞定了

行

我们总体来进行一次测试

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个电商系统中“库存同步”功能的开发演示。核心内容是利用 **Canal**（一个 MySQL 数据库的增量数据订阅工具）来监听数据库中 `tb_sku` 表的数据变更（如新增、修改、删除），并根据变更类型，通过 **Feign** 客户端异步调用远程服务（如搜索服务、商品详情页服务）来同步更新索引或静态数据。演示重点在于如何在 `SkuHandler` 监听器中编写逻辑，根据 SKU 的状态（如“秒杀商品”状态为 2）来触发不同的同步操作。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取精确的时间戳，以下时间点是根据画面内容和逻辑顺序推断的：

*   **0:00 - 0:15**: 视频开头，展示项目结构和 `CanalApplication` 启动类，说明程序启动后会监听数据库变更。
*   **0:16 - 0:30**: 进入 `SkuHandler.java` 文件，开始编写数据监听器。演示如何使用 `@Component` 和 `@CanalTable` 注解，并定义 `insert` 方法。
*   **0:31 - 0:45**: 在 `insert` 方法中，编写逻辑判断 SKU 状态是否为“秒杀商品”（状态码为 2），如果是，则调用 `SkuInfoFeign` 的 `modify` 方法进行索引同步。
*   **0:46 - 1:00**: 演示如何为 `SkuInfoFeign` 客户端添加 `@FeignClient` 注解，并定义 `modify` 方法的接口。
*   **1:01 - 1:15**: 在 `SearchController.java` 中，演示如何定义 `modify` 的 HTTP 接口，用于接收前端的修改请求。
*   **1:16 - 1:30**: 回到 `SkuHandler.java`，编写 `update` 方法。演示如何根据 SKU 状态的变化（如从“秒杀”变为“正常”）来判断是“修改索引”（type=2）还是“删除索引”（type=3）。
*   **1:31 - 1:45**: 演示如何为 `SkuPageFeign` 客户端添加 `@FeignClient` 注解，并定义 `delHtml` 方法用于删除商品详情页的静态数据。
*   **1:46 - 2:00**: 在 `update` 方法中，根据状态变化调用 `skuPageFeign.delHtml` 方法进行静态数据同步。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   项目结构图：展示了 `seckill-parent` 项目下的多个子模块，如 `seckill-api`, `seckill-service`, `seckill-search` 等。
    *   课程大纲：包含“6 同步数据”、“6.1 索引库同步”、“6.2 静态同步”等章节标题。
    *   文档注释：在代码中多次出现 `// 修改数据监听`、`// 增量操作 -> 删除索引 type=3`、`// 增量操作 -> 修改索引 type=2` 等注释。

*   **代码关键内容**:

    **1. Canal 启动类 (`CanalApplication.java`)**
    ```java
    @SpringBootApplication
    public class CanalApplication {
        public static void main(String[] args) {
            SpringApplication.run(CanalApplication.class, args);
        }
    }
    ```

    **2. 数据监听器 (`SkuHandler.java`)**
    ```java
    @Component
    @CanalTable(value = "tb_sku")
    public class SkuHandler implements EntryHandler<Sku> {
        @Autowired
        private SkuInfoFeign skuInfoFeign;

        @Override
        public void insert(Sku sku) {
            // status=2 表示秒杀商品
            if (sku.getStatus().equals("2")) {
                // type=1 表示修改索引
                skuInfoFeign.modify(type: 1, JSON.parseObject(JSON.toJSONString(sku), SkuInfo.class));
            }
        }

        @Override
        public void update(Sku before, Sku after) {
            int type = 1;
            if (after.getStatus().equals("2")) {
                type = 2; // 修改索引
            } else if (before.getStatus().equals("2") && after.getStatus().equals("1")) {
                type = 3; // 删除索引
            }
            skuInfoFeign.modify(type, JSON.parseObject(JSON.toJSONString(after), SkuInfo.class));
        }
    }
    ```

    **3. Feign 客户端接口 (`SkuInfoFeign.java`)**
    ```java
    @FeignClient(name = "seckill-search")
    public interface SkuInfoFeign {
        @PostMapping(value = "/search/modify/{type}")
        Result modify(@RequestBody SkuInfo skuInfo);
    }
    ```

    **4. 控制器接口 (`SearchController.java`)**
    ```java
    @PostMapping(value = "/modify/{type}")
    public Result modify(@RequestBody SkuInfo skuInfo) {
        return new Result(flag: true, StatusCode.OK, message: "操作成功");
    }
    ```

    **5. 静态数据同步 Feign 客户端 (`SkuPageFeign.java`)**
    ```java
    @FeignClient(name = "seckill-search")
    public interface SkuPageFeign {
        @PostMapping(value = "/page/delHtml")
        Result delHtml(String skuId);
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构与启动**
    *   **描述**: 视频首先展示了项目在 IntelliJ IDEA 中的完整结构，包括 `seckill-parent` 及其子模块。接着，演示了 `CanalApplication` 启动类，说明程序启动后会开始监听数据库。

*   **场景二：编写数据监听器**
    *   **描述**: 在 `SkuHandler.java` 中，演示了如何使用 `@Component` 和 `@CanalTable` 注解来标记监听器。通过 `@Autowired` 注入 `SkuInfoFeign` 客户端。在 `insert` 方法中，通过 `sku.getStatus().equals("2")` 判断是否为秒杀商品，并调用 `skuInfoFeign.modify` 方法。

*   **场景三：实现更新逻辑**
    *   **描述**: 在 `update` 方法中，演示了如何根据 `before` 和 `after` 对象的状态变化来判断操作类型。例如，当状态从 2 变为 1 时，设置 `type=3` 表示删除索引。

*   **场景四：同步静态数据**
    *   **描述**: 演示了如何为商品详情页服务创建 `SkuPageFeign` 客户端，并在 `update` 方法中调用 `skuPageFeign.delHtml` 方法，用于删除商品详情页的静态数据。

*   **场景五：调试与注释**
    *   **描述**: 在编写代码过程中，多次使用 `// 修改数据监听`、`// 增量操作 -> 删除索引 type=3` 等注释来说明代码逻辑。在 IDE 中，通过 `Ctrl+Shift+Space` 调用智能提示，辅助编写代码。

---

以上是根据视频画面进行的结构化技术分析。
