# 07-订单状态响应-页面长连接处理 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

那么排队以后咱们这个时候

这边就开始进行消费了

对不对

消费我们看他这一块是怎么消费的

大家看一下

我们之前这一块是用卡夫卡去给他下单

下单的话在这里

注意下单成功之后会做这么一个事情

开始向谁发消息了

开始向咱们当前这一块

你看message分是不是向咱们消息微服发消息

会向咱们消息微服发消息

叫skew message

我们看一下skew message在哪个地方

在这里

skew message是不是向他发消息

向他发消息

那么这个时候他就会去接收处理这个消息

在这一块发消息

发消息就会给咱们当前对应的客户端了

是不是

给当前客户端了

那客户端这个时候

是不是要跟咱们服务端建立连接才行

所以这一块

首先我们要在

客户端跟服务端之间建立一个websocket的连接

那么跟客户端跟服务端之间建立websocket连接

这一块该怎么做呢

其实非常容易

就把我们之前写的代码给挪过来

其实就可以了

好咱们找找

这个页面先找到

咱们再找找之前写的代码

把之前写的代码给找到

这是之前写的

随意打开

打开了我们简单看一下

第一个

步骤这里首先要创建一个websocket连接

对不对

创建websocket连接

我们来把这个过程搬过来就行了

怎么搬过来呢

非常容易

在这一块我们来写一个websocket对象

到上面这里websocket

先让它等于none

等于none之后

等会一进来咱们就对它进行初始化就行了

好

我们把方法写到这里来

初始化

创建websocket连接

那么怎么做呢

这样子

itwebsocket

行在这里面写这个初始化的连接操作

怎么做呢

也非常容易

这些代码直接给拷过来就可以了

直接拷过来就可以了

这写个叫类似点websocket

写个类似点对吧

这个是你打开未打开对不对

那这个呢

我们可以写到这里

也可以写到

外面去都行

这是连接连接打开了

还有另外一个除了连接打开是不是还有连接关闭等等

这有连接关闭

我们可以来写一下

把它给写到这里写个类似点

你也可以把这个写到外面去都行

好

我们接着继续看这里

还有一个是不是发生异常

我们仍然可以给写过来写个类似点就行了

行

这是我们这一块

这一块搞定了

接着我们再来看这还有关闭链接对不对

关闭链接这个自己可以写这个方法还有发消息对吧

好我们把这两个方法也给写过来

咋写呢

这是初始化连接

初始化连接写了接着我们开始写发消息

还有一个是关闭连接对吧

好发消息非常简单

直接写一个方法

剩的就行了

那么每次发什么消息你要把消息给我msg给我就行了

那发怎么发呢

直接写类似点websocket的点

剩的当前msg给他就行了

这就是发消息

关闭连接了也很简单

closews

来我们来写一下这一块

关闭连接了也非常简单

直接close就行了

类似点

类似点websocket

注意这不是socket是websocket

或者我们直接把它换成socket的得了

就不用说每个地方都跟着改了对吧

行那这个我们就搞定了

这个搞定了之后呢

我们来看一下我们这要做的一些相关的操作

现在是怎么回事呢

现在是后头那边跟我这儿

后头那边跟我这儿做了个什么事情呢

就是下单操作对不对

后头那只要响应我的是202

响应了202

这个时候我就需要跟我们后端建立连接了是不是

只要响应的是202

我就要建立连接

这一块

咱们这里的发消息的可能不存在什么发消息

对吧

好我们把这一块打开

这是建立连接

什么是建立连接

当后端响应我的时候

说我在排队

我就建立连接

如果在排队就建立连接

怎么做呢

直接这样写

app.iitwebsocket

就可以了

这个就建立连接了

那么建立连接了

这个时候这是打开

这个时候这是关闭

对不对

还有另外一个就是有消息过来了

怎么办呢

你们看这是不是有socket的onmessage

这是不是有消息啊

行

我们这里也写一下

就是接收到了消息

这是这一块

行我写这里

我写到外面去写到外面

在外面写一个方法

在外面写个方法

就不写到里面去了

这是发消息

咱们发消息都不要了吧

行留着吧

在这写

写个叫load message

行这有个叫做

console.log1就好了

这个是后端消息接收

后端给我发消息了

我就能接到这个消息了

对不对

在这一块

那么接到这个消息

我该怎么处理呢

这是另外一个事情了

行我们来看一下这个消息接收

我得写到这儿

接收消息

写个类似的消息

类似点

sort的点

叫onmessage

等于

等于它

那点外部的方法

对不对

行这是咱们这一块

这是咱们这一块

类似点

这一块写了之后

接着我们还要做这么一个事

是不是要测试这一块相关的一个操作

其实上面这个我们可以展示

不用写它

把它给干掉

就不用写这么多了

对吧

只要这里有个1打开

我们能看到就OK了

行下面这里还有关闭什么的都有

关闭链接咱们都不要了

发消息我们也不要了

我们只要我们当前这一块主要的方法就行了

就是后端给我响应的时候

如果响应的时候

202我就开始发消息

也不是什么时候都发

是202的时候

如果此时像普通的咱们就不去管它了

response.data.code

横等于202的时候

证明是不是要去

是不是这个时候要去获取后端响应的一个抢单排队的一个状态

对吧

好这是咱们这一块页面就搞定了

因为搞定了之后

紧接着我们就跟服务端进行对接

那么跟服务端对接这一块

我们就开始去做相关的一个处理了

就这一块要去获取订单

或者订单之后

这个时候就要开始处理了

这个时候就要开始处理了

订单处理了

就要开始给当前消息服务发消息了

消息服务发消息这一块有一个点大家要注意一下

就是每次发消息

它都是根据当前用户的名字ws

加上用户的名字来的对不对

既然是ws加上用户名字

当前这个方法这里满足得了咱们当前的需求吗

这个是满足不了的

为什么说满足不了的呢

因为咱们这里这个地址李氏是不是写死了呀

最好是把它给传过来

最好是把它给传过来

ulm给传过来

这才是我们需要的一个正确操作

加到这来

这就正确了

这就正确了

行在这一块

既然要把ulm加到这来

每次我这里去下单的时候

如果用户已登录

我是不是要把用户的名字也给你返回过来

你才知道怎么去创建当前web说的连接吧

我们这个时候就要改改当前这的一个操作了

我们这个时候就要改改当前这的一个操作了

我们这个时候就要改改当前这的一个操作了

好我们这个时候就要改改当前这的一个操作了

行大家来看一下

我们来改一下

怎么改呢

在这一块

若脚本里面

kill

我们看一下

其实用户名我们这里早就已经有了

这个用户名其实早就已经有了

我们只需要做这么一个事情

我们只是需要做这么一个事情

就是无论你这一块抢单

怎么抢

我都把这个用户名响应给你

怎么抢

那在这

把它给加上去

就可以了

做这么一个事情

做这么一个事情

response

写个叫做user name

等于

user name

这就可以了

这样子的话

每次响应就会把用户名

给我携带过来了

n进的是刚

s reload

大家看一下

现在是不是跟刚才就不一样了

我们这里仍然去进行抢购

看它返回的是不是就不一样了

这个时候就会多一个什么呢

多一个user name

对不对

那么多一个user name的话

那这个时候

我每次到后端去进行一个

webhook连接

我就知道是谁了

对吧

这里就写个response.data.user name

这样子就OK了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段展示了一个名为“秒杀系统”的前端 JavaScript 代码实现过程。核心内容是处理用户下单（`addOrder`）和建立 WebSocket 连接以监听排队状态的逻辑。视频通过 IntelliJ IDEA 开发环境，逐步演示了如何在用户成功下单后，根据服务器返回的响应码（`data.code`）来决定是跳转到个人中心（表示成功排队）还是跳转到登录页（表示未登录或下单失败）。同时，视频也展示了如何初始化一个 WebSocket 连接，并处理其连接、关闭和错误事件。整个过程体现了前后端协作、状态管理以及实时通信的实现。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 展示项目结构和 `addOrder` 函数的初始代码，包含从本地存储获取 token 并发送 POST 请求。
*   **00:05 - 00:10**: 代码编辑器中显示 `MessageController.java` 文件，用于演示后端 WebSocket 服务的实现。
*   **00:10 - 00:15**: 回到前端代码，展示 `addOrder` 函数中 `else` 分支，用于处理未登录或下单失败的情况。
*   **00:15 - 00:20**: 代码中出现 `initWebSocket` 函数的初始化部分，用于建立 WebSocket 连接。
*   **00:20 - 00:25**: 展示 `initWebSocket` 函数中定义的 `onopen`、`onclose` 和 `onerror` 事件处理函数。
*   **00:25 - 00:30**: 代码中添加了 `onerror` 事件处理函数，用于在发生错误时弹出警告。
*   **00:30 - 00:35**: 展示 `send` 方法，用于通过 WebSocket 发送消息。
*   **00:35 - 00:40**: 代码中添加了 `onmessage` 事件处理函数，用于接收后端消息并调用 `loadMessage` 方法。
*   **00:40 - 00:45**: 在 `addOrder` 函数中，根据 `response.data.code` 的值，决定是否调用 `initWebSocket`。
*   **00:45 - 00:50**: 代码中将 `initWebSocket` 的调用参数从 `null` 修改为 `response.data`，以传递用户信息。
*   **00:50 - 00:55**: 展示 `initWebSocket` 函数的最终版本，其中 `this.socket` 被初始化为 `new WebSocket("ws://localhost:28082/ws/" + username)`。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段**:
    *   **`addOrder` 函数**:
        ```javascript
        addOrder: function () {
            localStorage.setItem("token", "eyJ..."); // 设置 token
            var token = localStorage.getItem("token");
            if (token != null && token != "") {
                var instance = axios.create({});
                instance.defaults.headers.common['Authorization'] = 'Bearer ' + token;
                instance.post("http://data-seckill-java.itheima.net/lua/order/add?id=${sku.id}", ...).then(function (response) {
                    console.log(response);
                    // 跳转到个人中心
                    location.href = "http://data-seckill-java.itheima.net/#/user";
                    // 如果在排队，就建立链接
                    app.initWebSocket();
                }) else {
                    // 跳转登录
                    location.href = "http://data-seckill-java.itheima.net/#/login";
                    console.log("未登录！");
                }
            }
        }
        ```
    *   **`initWebSocket` 函数**:
        ```javascript
        initWebSocket: function () {
            this.socket = new WebSocket("ws://localhost:28082/ws/ls");
            this.socket.onopen = function () {
                console.log("Socket 已打开");
            };
            this.socket.onclose = function () {
                console.log("Socket已关闭");
            };
            this.socket.onerror = function () {
                alert("Socket发生了错误");
            };
            this.socket.onmessage = function (event) {
                loadMessage(event.data);
            };
        }
        ```
    *   **`loadTime` 函数**:
        ```javascript
        loadTime: function () {
            let tm1 = new Date(`${sku.seckillBegin}`.replace(/-/g, '-').replace(/:/g, '-'));
            let tm2 = new Date(`${sku.seckillEnd}`.replace(/-/g, '-').replace(/:/g, '-'));
            this.timeCalculate(tm1, tm2);
        }
        ```
    *   **`timeCalculate` 函数**:
        ```javascript
        timeCalculate: function (tm1, tm2) {
            var oneMinute = oneSecond * 60;
            var oneHour = oneMinute * 60;
            var oneDay = oneHour * 24;
            this.days = Math.floor((tm2.getTime() - tm1.getTime()) / oneDay);
            this.hours = Math.floor((tm2.getTime() - tm1.getTime()) / oneHour);
            this.minutes = Math.floor((tm2.getTime() - tm1.getTime()) / oneMinute);
            this.seconds = Math.floor((tm2.getTime() - tm1.getTime()) / oneSecond);
            var str = `${this.days}天${this.hours}时${this.minutes}分${this.seconds}秒`;
            return str;
        }
        ```

*   **关键公式/计算**:
    *   时间计算公式：
        ```math
        \text{总秒数} = \text{结束时间} - \text{开始时间}
        ```
        ```math
        \text{天数} = \left\lfloor \frac{\text{总秒数}}{86400} \right\rfloor
        ```
        ```math
        \text{小时} = \left\lfloor \frac{\text{总秒数}}{3600} \right\rfloor
        ```
        ```math
        \text{分钟} = \left\lfloor \frac{\text{总秒数}}{60} \right\rfloor
        ```
        ```math
        \text{秒} = \text{总秒数} \mod 60
        ```

---

### 4) 关键场景与演示描述

*   **场景一：下单成功后的逻辑分支**
    *   **描述**: 视频首先展示 `addOrder` 函数，当用户成功下单后，会收到一个响应。代码中通过 `if (response.data.code == 200)` 判断是否成功。如果成功，会调用 `app.initWebSocket()` 来建立 WebSocket 连接，以便后续监听排队状态。
    *   **演示**: 代码编辑器中高亮显示了 `if (response.data.code == 200)` 条件语句，并在下方添加了 `app.initWebSocket()` 的调用。

*   **场景二：WebSocket 连接初始化与事件处理**
    *   **描述**: 视频演示了如何初始化一个 WebSocket 连接。代码中创建了一个 `WebSocket` 对象，并为其注册了 `onopen`（连接打开）、`onclose`（连接关闭）和 `onerror`（发生错误）事件。
    *   **演示**: 代码编辑器中展示了 `this.socket = new WebSocket("ws://localhost:28082/ws/ls");` 的初始化语句，并依次添加了 `onopen`、`onclose` 和 `onerror` 的事件处理函数。

*   **场景三：处理 WebSocket 消息**
    *   **描述**: 视频展示了如何处理从后端接收到的消息。通过 `onmessage` 事件，可以调用 `loadMessage` 方法来更新前端页面。
    *   **演示**: 代码编辑器中添加了 `this.socket.onmessage = function (event) { loadMessage(event.data); };` 的事件处理函数。

*   **场景四：时间计算与显示**
    *   **描述**: 视频演示了如何计算并显示秒杀活动的剩余时间。通过 `loadTime` 函数，将开始和结束时间转换为毫秒，并计算出天、小时、分钟和秒。
    *   **演示**: 代码编辑器中展示了 `loadTime` 函数的实现，以及 `timeCalculate` 函数中用于计算时间的公式和逻辑。

*   **场景五：错误处理与用户引导**
    *   **描述**: 视频展示了如何处理用户未登录或下单失败的情况。在 `else` 分支中，代码会跳转到登录页，并在控制台输出“未登录！”。
    *   **演示**: 代码编辑器中高亮显示了 `else` 分支，并展示了 `location.href = "http://data-seckill-java.itheima.net/#/login";` 和 `console.log("未登录！");` 的代码。

---

以上是
