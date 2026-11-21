# 09-第三方行情源-Http连接池封装 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始学习基础工具的封装

在这里呢

我们需要采用ATTP连接池技术

同时呢

采用JSON作为数据载体来进行对接处理

ATTP连接池呢

它能够极大减少ATTP在连接方面的开销

能够去提升交互处理的效率

同时也可以减少调用方面的错误

因为ATTP连接池来讲的话呢

更加稳定一些

对于频繁或者是大量的ATTP请求

咱们最好呢

要加入连接池的处理技术

如果说你的调用频率来讲

或者是调用次数比较少

那么你可以采用ATTP之间的方式

不加入连接池这都没关系

但是对于高并发大数据的应用场景

必须要加入连接池的处理

那接下来咱们就在工程当中

去实现相应的代码

我们将代码呢

放在公用的YouTube手段

在工程下面

使用common utils

在下面呢

要增加ATTP或Util

专门去负责连接池的处理

然后还有一个工具呢

是json-carbot-util

专门去解析呢

节省数据

下面呢

是ATTP或Util工具的主要代码

这一块呢

咱们就不做足以的代码的敲写

节省一些时间

咱们将它呢

直接放到工程代码当中

再做详细的讲解

那咱们找到之前已经实现的代码

首先咱们将ATTP

工装的连接工具呢

拖比进去

这个是在common-utils下面

在下面咱们再创建一个纸包

纸包名称叫做HTTP

让它拖比进来

可以看到包错了

对不对

因为咱们还没把依赖加入进去

接着话呢

咱们先把节省的工具代码呢

也拖比进来

创建一个纸包

节省

在这下面呢

就专门放置

节省处理相关的工具

拖比进来

好

那咱们再将它的依赖呢

加入进去

找到POM文件

一个是ATTP client的组件

另外一个呢

是聚省的组件

将这两个呢

拖比进来

放在咱们的POM文件下面

放在最下面

让它导入生效

好

接着话呢

咱们再看一下

工装的代码

在这里就没包错了

我们首先来

讲解一下HTTP

线人词的连接封装实现

在这里面呢

定义了一个连接管理器

下面呢

是HTTP client的客户端

因为咱们作为调用方呢

就是客户端

咱们要向服务发送请求

下面就是它的连接具体配置

这个是全局的最大并发数

下面呢

是每个主机的最大并发数

这两个是什么意思呢

它们有什么区别呢

咱们来画一下

比如这个是服务A

这个呢是服务B

当然还有很多的一些服务

这里呢就不一一预计

那么从客户端发起的调用

这个呢是客户端

它可以去调用服务A

它也可以呢去调用服务B

它的全局并发数呢

指的就是服务A加上服务B的

整体的并发数

这两个加在一起

那我们来看一下

这个呢

就是每个主机的最大并发数

也就是服务A

它这边所能发起连接的最大并发数

这个呢就是max.post

然后这个呢

max.total

所有的全局最大并发数

这个呢就是包括客户端和服务A建立的连接

包括客户端和服务B所建立的连接

好

再往下面呢

是它的连接超时配置时间

默认的话呢

咱们就设定为20秒

所以这个也不要设的太长了

如果是你设的太长了

你的服务响应就会很慢

因为呢占用了大量的连接

会占据服务内存的开销

所以呢

咱们设置一个合适的时间就可以

然后下面呢就是单立的封装

这里面是加了一个Valetile的修饰服务

避免了并发时产生的原子性资源竞争的问题

当然单立的封装也有很多种方式

在这里咱们是采用懒加载去做的实现

咱们可以看一下

这个通过GETSINGLE这个方法呢

他就会去创建attp for utils

并非初始化的时候呢

就创建该对象

这个呢是懒加载方式去实现的一个单立

咱们再往上面看

下面的是模拟的浏览器代理标识

一些网站呢

他为了防止机器呢

去爬取上面的内容

会有一些那个反爬机制

那么有些爬虫呢

他要去模仿人工的操作

这个时候呢

他就要用到浏览器的代理标识

这个呢

他可以模仿任何浏览器的标识

只需要在上面呢

添加对应的头部信息就可以了

我们可以看到在这里模仿了火狐

苹果的浏览器以及谷歌的浏览器

下面就是attp连接管理工具的初始化

在这里面的去创建connection manager

然后呢

设置他的配置信息最大连接数

每个路由的最大连接数

就是刚才咱们图形当中所画的

有客户端发起每个服务的他的最大连接数

下面呢

是他的一个全局性配置

也就是连接的超时时间

下面是读取的超时时间

也就是说

服务端这边接收到你客户端的请求之后

服务端要做业务逻辑处理

对不对

然后呢

他再把数据返回给客户端

这个

过程当中呢

就是指的读取的超时时间

下面的是connection request timeout

这个就是从连接词当中获取一个有效连接的超时时间

如果是在高频发的场景上面

资源进振了比较频繁连接的再频繁的去申请频繁的去使用

这个呢

也会存在一定时间的开销

所以呢

我们也给他一个超时等待时间

这个是在内存CPU

当中的一个超时等待时间

当中去做的计算处理处理速度是非常快的

所以呢

一般配置500毫秒就足够了

然后下面是连接存活的配置策略

这个配置策略呢

他的意思呢

就是客户端发连接

他这个连接有效的存活时间

这个连接的并非在交互过程当中就开始去计时

而是在你连接他的数据处理完成之后

比如说这个连接他数据交互完成之后

跟服务器A还产生连接时间之后呢

这个连接他数据交互完成之后呢

跟服务器A还产生连接时间之后呢

跟服务器A还产生连接时间之后呢

那么这个连接的话呢

就是一个空闲的对不对

这个呢就是他的一个空闲有效时间

下面呢

就是对ATTP Client的连接的一个创建

上面呢

是对整个连接的一些配置

然后呢

就要将这些配置信息注入进去

像Connection Manage

还有请求的配置

从事策略

连接词的存活策略等等

然后咱们再往下面看

这个呢

是请求的从事策略

也是这上面的一个配置

从事策略有什么作用呢

因为在实际运行过程当中呢

经常会出现各种各样的一些问题

比如说一些网络问题

超时等不同情况

那么客户端发送过去的连接呢

服务器A有可能没有收到

这个时候就需要有个从事策略

客户端呢

可以再次发送一个请求

到达指定次数之后呢

就不再进行从事

那咱们可以看一下代码的具体实现

这里呢

它会有一个方法的重写

Return Request

这里面该怎么去配置呢

首先是要配置你想从事的次数

这个次数呢

一般配置三次就可以了

下面呢

就是针对哪些异常

然后呢

让它加入到从事策略当中

那这个Timeout的

还有Unlocked,False的

以及Connection Refused的

这些异常的话呢

都是Return Force的

这些话呢

就不会进入从事的策略

当然这些也可以根据咱们的需要

去重新设定

去做不同的配置

你想让这个Unlocked Force的

加入从事策略呢

直接将它凯为Cue就可以了

然后下面针对哪些情况

会进行从事呢

它会针对于No HTTP Response

也就是说没有收到服务端的响应

那么就会发送这样一个从事

下面呢

是针对于请求类型的配置

这个配置是什么意思呢

如果是请求类型

它不是HTTP in Entity Enclosing Request

那么它就被认为

是Midden了

它就会进入从事策略

如果是属于HTTP in Entity Enclosing Request

它就不能保证Midden性

就不会进入从事策略

为什么这么说呢

因为咱们常用的

比如说Cat请求

它是没有什么请求体的

对不对

Post跟Put都是有请求体的

它要附带一些参数

要提交表单等信息

那么Post的Put

它的请求类型呢

一般都是HTTP in Entity Enclosing Request

如果你让Post还有Put的请求类型

可以从事的话呢

结果可能会造成重复的数据

它不能保证接口的一等性

那么对于Cat的请求呢

它只是进行数据的查询

对不对

无论说你查第一次

还是查第二次

获取到的数据呢

往往都是一致的

当然排除这个时间段之内

或产生的数据

它实质上呢

是不会对服务器的

数据呢

造成任何的影响

所以呢

它能够保证它的一个密等性

这个时候的Cat的请求呢

就能够让它加入从事的机制

这里的这个配置呢

主要就是起这个作用

那咱们呢

要理解清楚

并非所有的场景都适合从事

从事你要去保证

接口的密等性

否则呢

你从事之后

会产生一些垃圾

或者是冗余的数据

再往下面

咱们来看一下

这个呢

就是单例的实现

在这里

它采用了一个同步锁

就是保障呢

并发时候不产生多个死例

下面呢

就是POST的调用请求方式

POST的N体

于是N局的呢

会附带头部信息

也就咱们在上面所定义的

浏览器代理标识

再往下面呢

就是普通的POST的N体

在下面就不附带N局的头部信息

下面是POST的N体方法的具体实现

咱们可以看到

如果头部信息呢

不为空

它就会将它呢

放到头部里面

它的标识呢

是U者N群的

然后是它的参数组装

还有发送方式

通过呢

此群N体去做了包装

然后将它呢

附带在N体里面

采用POST的方式进行发送

然后通过CLANT进行执行

处理完成之后呢

会拿到它的响应码

然后再做一层包装

这样呢

便于接口调用时呢

对结果的处理

它的包装信息呢

其实也是很简单

首先呢

是包装它的响应码

接着呢

就是包装它的数据体

数据体呢

它将它的响应结果包装为一个

ToStreetStreet

也就是一个StreetStreet字符串类型的对象

最后呢

它会做一个日志的打印记录

这里呢

是一个远程调用的耗时时间

便于咱们出现问题时的一个排查

最后不要忘记了

要将相关的资源呢

做个释放

好

然后下面呢

就是其他封装实现方式

这个呢

是get的请求

下面呢

就是post的请求

这个post呢

跟刚才是有些不一样

刚才的话呢

是通过一个screen entity的方式进行发送

在这里面的post呢

我们可以看到

它是通过一个什么

URL encoder的form entity进行的提交

这两种方式呢

有些区别

具体的话呢

就是看服务端所能够接收数据的方式

咱们呢

就采用不同方式进行下载

相应的提交

这一讲呢

就是对attp连接词工具的封装讲解

那这一讲

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析：

---

### 1) 视频摘要

本视频片段是关于一个股票行情数据处理项目的开发教程，重点讲解如何构建一个基础的工具包（`bulls-stock-common-utils`）来处理 HTTP 请求。讲师通过 IntelliJ IDEA 开发环境，演示了如何创建一个名为 `HttpPoolUtil` 的工具类，该类封装了 HTTP 连接池、请求重试策略和请求体处理等功能，旨在提高 HTTP 请求的效率和稳定性。视频内容主要集中在代码实现和配置上，旨在为后续的行情数据对接打下基础。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，讲师在 Typora 文档中展示课程大纲，明确当前章节为“3.2 基础工具封装”。
*   **00:00:05 - 00:00:15**: 讲师在文档中解释了本节目标：采用 HTTP 连接池技术与 JSON 来对接第三方行情数据源，并强调了连接池在处理大量 HTTP 请求时的重要性。
*   **00:00:15 - 00:00:30**: 讲师切换到文件资源管理器，演示了如何解压 `bulls-stock-ori.zip` 文件，定位到 `bulls-stock-common-utils` 模块的 `src/main/java` 目录。
*   **00:00:30 - 00:00:45**: 讲师在 IntelliJ IDEA 中打开项目，展示 `bulls-stock-common-utils` 模块的目录结构，并在 `com.ictast.stock.common.http` 包下创建 `HttpPoolUtil` 类。
*   **00:00:45 - 00:01:00**: 讲师在 `HttpPoolUtil` 类中开始编写代码，导入了 `org.apache.http.client` 和 `org.apache.http.entity` 等核心包。
*   **00:01:00 - 00:01:15**: 讲师编写了 `HttpPoolUtil` 类的构造函数，初始化 `PoolingHttpClientConnectionManager` 连接管理器，并设置了最大连接数和每个路由的最大连接数。
*   **00:01:15 - 00:01:30**: 讲师编写了 `getDefaultRequestRetryHandler()` 方法，定义了请求重试策略：超过 3 次失败或遇到 `InterruptedException` 时停止重试。
*   **00:01:30 - 00:01:45**: 讲师继续编写 `HttpPoolUtil` 类，添加了对 `HttpEntity` 的判断逻辑，区分 GET 和 POST 请求。
*   **00:01:45 - 00:02:00**: 讲师编写了 `get` 方法的主体逻辑，创建 `HttpGet` 对象，设置请求头和参数，并执行请求。
*   **00:02:00 - 00:02:15**: 讲师在 `HttpPoolUtil` 类中添加了 `defaultUserAgent` 静态变量，用于设置默认的 User-Agent 请求头。
*   **00:02:15 - 00:02:30**: 讲师在 `HttpPoolUtil` 类中添加了 `setConnectionTimeout` 和 `setSocketTimeout` 方法，用于设置连接和读取超时时间。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **章节标题**: “3.2 基础工具封装”
    *   **核心概念**: “采用 HTTP 连接池技术与 JSON 来对接处理，HTTP 连接池能极大减少 HTTP 的连接开销，提升处理效率，减少调用错误。对于频繁或大量的 HTTP 请求最好要加入连接池处理技术。”
    *   **任务目标**: “先建立相关工具：增加 `HttpPoolUtil` 连接池工具与 `GsonConvertUtil` 解析工具。”

*   **代码关键内容**:
    *   **`HttpPoolUtil` 类构造函数**:
        ```java
        private HttpPoolUtil() {
            connectionManager = new PoolingHttpClientConnectionManager();
            // 最大连接数
            connectionManager.setMaxTotal(maxTotalConn);
            // 默认的每个路由的最大连
            connectionManager.setDefaultMaxPerRoute(maxConnPerHost);
            RequestConfig defaultRequestConfig = RequestConfig.custom();
        }
        ```
    *   **`getDefaultRequestRetryHandler()` 方法**:
        ```java
        @Override
        public boolean retryRequest(IOException exception, int executionCount, HttpContext context) {
            if (executionCount >= 3) {
                return false;
            }
            if (exception instanceof InterruptedIOException) {
                return false;
            }
            if (exception instanceof org.apache.http.NoHttpResponseException) {
                logger.warn("No response from server on " + executionCount + " call");
                return true;
            }
            return false;
        }
        ```
    *   **`get` 方法**:
        ```java
        public HttpResult get(String url, Map<String, String> params) throws Exception {
            HttpResult ret = new HttpResult();
            HttpGet method = new HttpGet(url);
            InputStream is = null;
            CloseableHttpResponse httpResponse = null;
            try {
                if (null != params && params.size() > 0) {
                    List<NameValuePair> listParams = new ArrayList<>();
                    for (Map.Entry<String, String> entry : params.entrySet()) {
                        listParams.add(new BasicNameValuePair(entry.getKey(), entry.getValue()));
                    }
                    method.setEntity(new UrlEncodedFormEntity(listParams, Consts.UTF_8));
                }
                httpResponse = client.execute(method);
                ret.setStatusCode(httpResponse.getStatusLine().getStatusCode());
                if (null != httpResponse.getEntity() && null != httpResponse.getEntity().getContent()) {
                    is = httpResponse.getEntity().getContent();
                    // ... (后续处理)
                }
            } catch (IOException e) {
                throw new RuntimeException(e);
            } finally {
                // ... (资源清理)
            }
            return ret;
        }
        ```
    *   **`defaultUserAgent`**:
        ```java
        private volatile static HttpPoolUtil httpPoolUtil = null;
        public static String defaultUserAgent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36";
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构与工具创建 (00:00:30 - 00:00:45)**:
    *   讲师在 IntelliJ IDEA 中打开项目，展示了 `bulls-stock-common-utils` 模块的目录结构。
    *   讲师在 `com.ictast.stock.common.http` 包下右键，选择“New -> Java Class”，创建了 `HttpPoolUtil` 类。

*   **场景二：连接池配置 (00:01:00 - 00:01:15)**:
    *   讲师在 `HttpPoolUtil` 类中编写了构造函数。
    *   讲师通过 `connectionManager.setMaxTotal(maxTotalConn)` 和 `connectionManager.setDefaultMaxPerRoute(maxConnPerHost)` 设置了连接池的最大连接数和每个路由的最大连接数。

*   **场景三：请求重试策略 (00:01:15 - 00:01:30)**:
    *   讲师编写了 `getDefaultRequestRetryHandler()` 方法。
    *   讲师通过 `if (executionCount >= 3)` 判断重试次数，超过 3 次则返回 `false` 停止重试。
    *   讲师通过 `if (exception instanceof InterruptedIOException)` 判断是否因中断而失败，如果是则返回 `false`。

*   **场景四：请求体与方法处理 (00:01:30 - 00:01:45)**:
    *   讲师编写了 `HttpPoolUtil` 类中对 `HttpEntity` 的判断逻辑。
    *   讲师通过 `if (request instanceof HttpEntityEnclosingRequest)` 判断请求是否包含实体（如 POST 请求）。
    *   讲师通过 `if (idempotent)` 判断请求是否幂等（如 GET 请求）。

*   **场景五：GET 请求实现 (00:01:45 - 00:02:00)**:
    *   讲师编写了 `get` 方法的主体逻辑。
    *   讲师创建了 `HttpGet` 对象，并通过 `method.setEntity(new UrlEncodedFormEntity(listParams, Consts.UTF_8))` 设置请求参数。
    *   讲师通过 `httpResponse = client.execute(method)` 执行请求，并通过 `ret.setStatusCode(httpResponse.getStatusLine().getStatusCode())` 获取响应状态码。

*   **场景六：User-Agent 设置 (00:02:00 -
