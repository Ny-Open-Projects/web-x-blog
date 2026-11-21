# 04-详情页-页面倒计时讲解 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

我们紧接着就要测试静态业生成

在刚才这里我们用到了份接口

所以我们要把份接口这一块给配置过来

在这一块我们写一下

叫做EnableFundClientBasePackage

这里把包的路径给写过来就OK了

接下来我们就启动进行测试

看一下效果如何

能否实现我们静态业的一个生成操作

如果可以那这一块就没啥问题

咱们再去把故事微服务给启动一下

在这一块这个故事微服务是需要启动的

OK 右键启动一次

启动之后咱们看看这个结果如何

好 等它启动

启动了

启动了咱们就开始进行一个相关的访问操作

行 都没有问题

咱们开始访问一下相关的页面

访问一下相关的一个商品

然后给它生成静态业

配解HTML加上对应的一个ID

这个用get吧

咱们为了方便点用get

等它启动

行 目前已经启动了

启动了之后我们现在来进行一次测试

直接把浏览器打开

在这一块输入一下localhost

咱们这个端口是18087

对吧

配解

加上HTML加上商品的ID

那么商品的ID咱们就随意找一个商品就行了

我们就不用去关注太多了

就这个冰箱来给它生成一个详情页回车一次

那这一块生成了

很显然生成成功了

生成成功了

我们看一下这个静态业它在哪里

静态业在地盘配解HTML

我们看一下这个页面生成没有

回车一次

生成了

再把它删掉再来生成一次

再来刷新一次

又生成了

打开看看页面

页面这一块就显示出来了

虽然说不是特别的美观

但是显示出来了

因为咱这个数据没有那么的漂亮

对不对

还有一个问题

这一块还有些图片没有显示

图片没关系

在这一块我们把它给弄过来

后面还会用到我们axls

vue.js

我们都把它弄过来

行再刷新一次

它的效果就会好一些了

图片都有了

当然目前这些数据还都是一些假数据

我们一会要把这个变得动起来

让它能够进行一个倒计时操作

那么倒计时操作在这一块

其实已经给咱们提供了相关的代码

我们就直接去拷贝了

我们就不去写了

因为这一块主要是涉及前端相关的一些知识点

咱没必要去把它给响了一下

我们就直接来详细写一遍了

我们来拷贝之后给大伙讲解一下

从这一块一直到后面全部拷贝

Ctrl A,Ctrl C

全部拷过来

拷过来之后

一会儿我再给大家介绍一次就OK了

行把它给放到这里

放这里就可以了

那么放到这里之后

我们来简单介绍一下

简单说一下这一块

我们绑定的节点是

井号app

那这一块呢

大家说一下

没有这个

标签

咱写个标签

divid.app

到后面去

把这一块给

扩起来

扩起来之后

我们这一块vue标签就能识别了

行,走到这里

整体就搞定

那么整体搞定之后呢

我们开始做这么一个事

把上面这一块给优化一下

怎么优化呢

这里不是有一个

大家看哈

这里不是有一个

距离还剩多少天吗

这样写

叫做

小时

还有一个是咱们看一下啊

这个是

写个message

为什么这么写

咱们等会儿再说

小时

我们看另外一个

第二个是什么呢

是分钟

这个换成分钟

还有一个是咱们的一个

秒

seconds

把他给放到这里来

好我们这个时候来生成这个静态页

看有什么不同

刷新一次

来开始生成

这是生成之后的

大家可以看到在倒计时

600多天之后结束

对吧

这个时间是准确的啊

因为咱这块时间是

测试了非常久的时间

时间准确

那么下面这一块也都是正确的

倒计时就搞定了

那么倒计时这一块是怎么做的呢

我给大家介绍一下就行了

我们不详细去讲解他

他的一个代码

因为主要是前端JS代码

刚才我为什么要在最外层包一个DLV呢

因为这一块没有

节点没有标签

他的一个

ID是App

是不存在的

所以我加了一个

另外这里有个message

message是什么呢

是这一块上面的一个

显示

就活动一旦结束

这上面会写

活动结束

是这一块

还有一个别的就是小时

分钟

秒了

这就是倒计时这一块了

小时分钟秒

就这一块

行咱们后面这里有一个时间的运算

这个就是时间运算

每次只需要把我们当前这一块

商品

秒杀活动开始时间

秒杀活动结束时间

传过来就可以了

传过来之后

他这里会进行倒计时的一个操作

那么倒计时操作在这一块是怎么做的呢

在下面这里

会把

这一块

剩余多久的时间

比如说是10天之后结束

10天距离当前时间

有多久

那么有多久呢

会把它传过来

传过来之后会进行一个计算

计算会先做这么一个事

先计算有多少小时

有多少小时

这个是总时间

除以每小时有多少

毫秒

然后这个时候

注意

把它的整数

取出来就行了

整数取出来

就是我们当前这一块

有多少小时了

那下面这个是什么呢

是这么回事

是

总时间

除以

每小时

它的余数

看到没

其实说把整除

整除的就是多少小时吧

把整除的除去余数是不是剩下的时间呢

剩下的时间

除以每分钟有多少毫秒

每分钟有多少毫秒取什么呢

取整数

这个是取整数的意思啊

取整数并不是四舍五入

是只取整数部分

而不会取什么四舍五入这一块

不存在

那这个时候

小时

它的一个

剩余的余数是不是就是剩下时间呢

剩下时间再除以

每小时有多少毫秒

每分钟有多少毫秒

那这个时候得到就是分钟了

下面这一块也是一样

把

这一块总的时间有多少分钟

除掉

除掉之后剩下的余数就是剩下的时间

剩下时间除以

每秒有多少毫秒

那就是我们这剩下多少秒了

行这是我们这个倒计时这一块

倒计时有了之后紧接着我们就要调用

这一块这个时间计算了

这一块调用的是调用上面这个load time

调用这个

看一下

在这一块呢

调用上面这个

调用它

它会调谁呢

会往后面走往后面走

在这里

就会调刚才下面这一个

这个

倒计时计算

倒计时在这进行倒计时的

这进行倒计时的

这是清除倒计时

这里是

进行倒计时

这就是咱们接受的简单倒计时

好下面这一块就是我们秒杀开始时间和秒杀结束时间

直接把秒杀开始时间取出来

秒杀结束时间取出来

然后放进去就OK了

行这是这一块

下面这里是下单操作

我们等会来讲解下单操作

这个是初始化调用它

OK

这就是咱们倒计时实现的一个流程讲解

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段主要演示了一个基于 Spring Boot 和 Vue.js 的电商商品详情页的前后端交互实现。讲师通过 IntelliJ IDEA 开发环境，逐步讲解了如何在后端 Java 控制器中通过 `@PostMapping` 接收商品 ID，调用 `skuFeign` 服务获取商品数据（包括 SKU 信息、图片、规格等），并将数据封装成一个 `Map<String, Object>` 用于前端渲染。前端部分则使用 Vue.js 框架，通过 `axios` 发起 HTTP 请求，接收后端返回的数据，并在页面上动态展示商品详情、图片、规格参数和“立即购买”按钮。同时，视频也展示了如何在前端实现一个倒计时功能，并处理用户登录状态，以实现“立即购买”按钮的权限控制。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**：展示项目结构，定位到 `SkuPageController` 类。
*   **00:05 - 00:15**：讲解后端控制器方法 `@PostMapping` 的作用，以及如何通过 `skuFeign.findbyId(id)` 获取商品数据。
*   **00:15 - 00:30**：演示如何将商品数据（如图片、规格）封装到 `Map<String, Object>` 中，准备传递给前端。
*   **00:30 - 00:45**：切换到前端 Vue.js 代码，展示如何通过 `axios` 请求后端接口。
*   **00:45 - 01:00**：讲解前端 Vue 实例的 `data` 和 `methods` 部分，以及如何将后端返回的数据绑定到页面元素上。
*   **01:00 - 01:15**：演示如何在前端页面中使用 `v-for` 循环渲染商品规格参数。
*   **01:15 - 01:30**：讲解如何在前端实现一个倒计时功能，使用 `timeCalculate` 方法计算剩余时间。
*   **01:30 - 01:45**：演示如何在前端处理用户登录状态，通过 `localStorage` 获取 token，并根据状态决定“立即购买”按钮的跳转逻辑。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   展示了课程大纲，包含“商品详情页生成”、“Sentinel限流”、“Nginx限流”、“秒杀”等章节。
    *   在前端代码中，展示了 Vue.js 的 `data` 和 `methods` 结构。

*   **关键代码**：

    *   **后端 Java 控制器代码 (`SkuPageController.java`)**：
        ```java
        @PostMapping(value = "/html/{id}")
        public Result html(@PathVariable(value = "id") String id) throws Exception {
            Result<Sku> skuResult = skuFeign.findbyId(id);
            // 数据模型
            Map<String, Object> dataMap = new HashMap<>();
            dataMap.put("path", "htmlPath");
            dataMap.put("templateName", "items.ftl");
            dataMap.put("name", id + ".html");
            dataMap.put("address", "北京");
            dataMap.put("sku", skuResult.getData().getSku());
            dataMap.put("images", skuResult.getData().getImages().split(regex: ","));
            // 获取spec
            String spec = skuResult.getData().getSpec();
            Map<String, String> specMap = JSON.parseObject(spec, Map.class);
            String specList = "";
            for (Map.Entry<String, String> entry : specMap.entrySet()) {
                specList += entry.getValue();
            }
            dataMap.put("spec", specList);
            return Result.success(dataMap);
        }
        ```

    *   **前端 Vue.js 代码 (`items.ftl` 或 `index.html`)**：
        ```javascript
        var app = new Vue({
            el: '#app',
            data: {
                message: '',
                hours: '',
                minutes: '',
                seconds: ''
            },
            methods: {
                timeCalculate: function (starttimes, endtimes) {
                    let nowtimes = new Date().getTime();
                    if (nowtimes > endtimes) {
                        this.message = '活动已结束！';
                        return;
                    }
                    // 时间差
                    let nums = 0;
                    let prefix = '距离结束：';
                    if (starttimes < nowtimes) {
                        // 距离开始
                        nums = nowtimes - starttimes;
                    } else {
                        // 距离结束
                        nums = endtimes - nowtimes;
                    }
                    // 计算小时、分钟、秒
                    let hours = Math.floor(nums / (1000 * 60 * 60));
                    let minutes = Math.floor((nums - hours * 1000 * 60 * 60) / (1000 * 60));
                    let seconds = Math.floor((nums - hours * 1000 * 60 * 60 - minutes * 1000 * 60) / 1000);
                    this.hours = hours;
                    this.minutes = minutes;
                    this.seconds = seconds;
                    this.message = prefix + hours + '小时' + minutes + '分钟' + seconds + '秒';
                }
            }
        });
        ```

    *   **前端请求与登录处理代码**：
        ```javascript
        var token = localStorage.getItem("token");
        if (token != null && token != '') {
            var instance = axios.create({
                baseURL: 'http://data-seckill-java.itheima.net/api/order/add',
                headers: {
                    'Authorization': 'Bearer ' + token
                }
            });
            instance.post('http://data-seckill-java.itheima.net/api/order/add', {skuId: skuId}).then(function (response) {
                location.href = 'http://data-seckill-java.itheima.net/#/user';
            }).catch(function (error) {
                console.log(error);
            });
        } else {
            location.href = 'http://data-seckill-java.itheima.net/#/login';
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：后端数据获取与封装**
    *   讲师在 IntelliJ IDEA 中打开 `SkuPageController.java` 文件。
    *   通过 `@PostMapping` 注解定义了一个处理商品详情页请求的接口。
    *   通过 `skuFeign.findbyId(id)` 调用远程服务获取商品数据。
    *   将商品的图片、规格等信息封装到一个 `Map<String, Object>` 中，准备返回给前端。

*   **场景二：前端页面渲染与数据绑定**
    *   讲师切换到前端页面，展示 Vue.js 实例。
    *   通过 `axios` 发起请求，获取后端返回的 `dataMap`。
    *   将 `dataMap` 中的数据（如 `name`, `sku`, `images`, `spec`）绑定到 Vue 实例的 `data` 对象中。
    *   使用 `v-for` 循环渲染商品规格参数列表。

*   **场景三：倒计时功能实现**
    *   讲师在前端代码中定义了一个 `timeCalculate` 方法。
    *   该方法接收开始时间和结束时间（以秒为单位）。
    *   通过 `new Date().getTime()` 获取当前时间戳。
    *   计算当前时间与开始时间、结束时间的差值，动态更新 `hours`, `minutes`, `seconds` 字段。
    *   将计算结果绑定到页面元素上，实现倒计时效果。

*   **场景四：用户登录状态处理**
    *   讲师在前端代码中添加了 `localStorage` 用于存储用户 token。
    *   在 `created` 生命周期钩子中，通过 `localStorage.getItem("token")` 获取用户登录状态。
    *   如果用户已登录，调用 `axios` 发起购买请求，并跳转到个人中心页面。
    *   如果用户未登录，跳转到登录页面。

*   **场景五：页面调试与效果展示**
    *   讲师在浏览器中打开商品详情页，展示页面效果。
    *   使用浏览器开发者工具（F12）查看页面元素和样式。
    *   通过 `console.log` 输出调试信息，验证数据绑定和功能逻辑。

---

以上是根据视频画面进行的结构化技术课程分析，希望能帮助您更好地理解课程内容。
