# 13-第三方行情源-第三方行情源接口封装实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来接着的话呢

咱们就来实现第三方行情员的对接

我们呢

将它放置在source保木下面

这个呢

是专门用于第三方行情员的接入

如果将来要去扩展

其他的第三方行情员呢

都可以在这下面做对应的实现

那我们呢

要去创建聚合数据的API实现内

咱们回到代码当中

在source木下面

创建一个class

这个呢

是聚合API

第三方的

咱们呢就叫聚合式的API

OK

接着咱们就来做具体的实现

首先给内上面

加上对应的注解

作为一个主件

加上longbook

日志的注解

然后我们要去

编写它的属性

这个呢

是第三方行情员的

APP的密钥信息

这个呢

是它的URL

接口信息

这个就是接口的具体地址

就是包括它的一个完整的后缀路径

这些属性呢

是放在配置文件当中

我们呢

要将它注入进来

通过Value注解

属性的名称

APP Key

这里面也是Value注解

同样也是Code开头

URL

上面呢

也是Value注解

这里注意一下

咱们就采用拼接的方式来做实现

怎么拼接呢

将这里面URL的属性呢

做一个拼接

后面呢

就跟着具体的接口路径

拼接方式

外层的话呢

是以警告开头

避免引号产生冲突

在这里我们采用单引号

然后读取

code.URL

在这里做一个拼接

Connect

拼接的接口路径

因为聚合行情员呢

它有多个行情接口

有互生股市的

也有美股港股的

在这里呢

咱们只对接互生股市的

所以呢

我们要给它一个具体的接口信息

加上说明

互生股市的

行情接口地址

这样如果将来IP发生了变化呢

只需要调整code.URL就可以了

上面呢是

第三方

行情员的地址

这个呢是第三方

行情员的

密钥信息

接下来咱们就来

实现了

它的接口的调用

首先我们要去组装它对应的参数信息

也就是说要传递的股票编号

这个股票编号呢之前咱们做演示的时候呢

也做了讲解

它需要加上了不同的市场名称

所以呢咱们在这里要做一个拼接处理

这里要做一个围攻判断

如果是tog呢

不围攻

接着才可以进行一个拼接

那么如何进行拼接呢?

在这里面Tradestock

也有自身的

股票市场

但这个股票市场呢

跟咱们聚合API文档里面的股票市场是不一样的

咱们知道之前做测试的时候呢

它是以拼音的简写

去作为股票市场

咱们在这里呢是通过数字来定义

所以呢咱们要做一个转换

如何去进行转换呢?

咱们就来通过Mage来做实现

通过Stock Market Animal

做这样一个Mage

这样呢就实现了我们内部的

市场

跟

第三方聚合数据源市场的一个转换

那咱们呢

先将这个Stock Market的Mage创建下

将它创建到咱们的

Common Utils下面

放在Consistency目录下

New Java Class

创建之后呢

咱们就将代码呢

拷贝进来

我们来看一下

它是如何去定义的

在这里面它定义了三个属性

第一个属性是Market Number

这个是市场的编号

也就是咱们内部系统当中的市场编号

接着的话呢就是市场标识

这个市场标识呢

是用于远程的聚合数据源

接口的调用

最后呢就是市场的名称

咱们做了一个名称的描述说明

因为这一期呢咱们主要是实现上交所

升交所股票行情的处理

所以呢我们只需要配置两个标识就可以

其他方面暂时没有实现

咱们呢可以不用做具体配置

为了便于整个的转换呢

下面还写了一个进代方法

也就是根据你的

市场编号来获取具体的

枚举对象

在这里报错咱们要加上

GET的图解

通过Long Book

它会自动生成GET方法

好在这里就没有报错

咱们再回到刚才的代码当中

接着咱们就对

枚举对象做一个转换

Stock

Market

Animal

Stock

再用它的静态转换方法

将Market Number

转入进去

然后呢我们可以将它的对象呢

返回

在这里做一个拼接处理

最后呢

要返回

股票的编号

正常的话呢

这个Stock

应该不为空

那咱们呢就能够正常

组装到它的完整的编号信息

我们加上对应的注释说明

这里呢是组装

完整的

股票编号

要附带呢

市场的

标识

具体格式呢

它要符合

聚合

数据

平台的

规范要求

也就是说市场标识

这个的话呢是拼音简写

再拼接

它的股票编号

接下来咱们就看一下如何去调用实现

public

它调用完成之后呢

要返回一个

实时的

行情数据

Bedstock

Rule

环境呢

股票产品信息

Stock

首先咱们设置它的请求参数

这个呢是一个Map结构

名称就叫Pyramids

Rule

Rachemap

然后将参数呢

设置进去

一个参数呢是GID

这个呢就是股票的完整编号信息

通过咱们刚才所封装的方法

将股票产品呢传递进去

接着换了是它的

Key密钥信息

AppKey

这个就是读取属性配置

然后要定义一个

行情数据对象

这个是实时行情对象

外层要一个Check-catch

因为整个处理过程当中呢可能会爆出

未知的异常

咱们将日志呢把一下

最后呢就要返回Core的实时行情对象

那咱们看一下具体该如何去调用实现了

通过

Pull Util

里面的ATDP去照上

那么我们就可以通过连接式工具呢

做一个调用

ATDP

Pull Util

通过单例去访问Post

可以传递它的头部信息

UIL

这个是接口地址

然后是参数信息

那咱们拿到Result呢就要做一个判断

如果是请求正常的

它就会返回200的

状态了

Result

Get the respond code

等于200

为了便于排查呢我们可以先将日志打一下

Result

获取了它的包体数据

然后我们要去组装为JSON

JSON

通过封装的JSON Cover的Util工具

也是单例的形式

进行一个JSON的转换

Result.GetBody

这个就是获取

JSON

数据中的

Data

信息节点

怎么去获取呢

JSON

Object

Data

JSON

.Get

这个就作为一个JSON的

JSON的数据

拿到Result

之前咱们也看过它的返回数据结构对不对

Result呢是一个数据

然后呢

获取它的第一个索引数据

Get as JSON Object

转换为JSON Object对象

然后再拿到它的Data节点信息

最后再将它转换为JSON Object对象

拿到JSON对象之后呢

就要

将JSON数据

JSON数据

转换为

股票

分时

行情

报价对象

也就是最新行情报价

Port

Last

咱们通过一个方法做对应的封锁实现

Page

Drom

JSON

传递了Data

还有股票产品信息

如果

图是200

那么咱们要将它的

异常信息打印出来

JSON

这个就是

聚合社的API

JSON

这个方法呢

我们加上注释

他是将JSON

并不复杂 咱们呢 就从讲义当中扣币进来

好 咱们可以看到呢 首先是设置他的基础信息 然后呢 要设置他的卖方的五档的盘口信息

接着换的就是买方的五档盘口信息 在这里呢 咱们做了一个封装 也就是说将这里面的所有价格信息呢 都转换为一个长整形

咱们已经相关代码了 后面进来 一个是转换为日期 一个是转换为长整形

他默认了会保留两位金注 在这里呢 咱们就将他的辅助方法引入进来

那整个的聚合数据API的交易逻辑呢 就已经实现完成

咱们回到讲义当中 整个流程呢 咱们再回顾一下 在这里呢 咱们要注意一下

getstock留有方法呢 他是获取行情源报价的具体实现

该方法接受的是一个股票产品对象 实际呢 还有处理多个产品的行情报价

由上层呢

去便利调用控制 在该方法内部呢 不做便利处理 由外部的调用呢 去做上层的便利控制

这样就实现多个产品的行情报价处理 内部的要先判断状态码是否正常 如果错误呢 这里是忽略处理

实际当中呢 要加入预警或者是上保机制更为稳妥

因为行情来讲呢 是比较重要的信息 行情源传递过来的呢 他是带精度的价格 这里就需要做一层转换

通过呢

这个方法呢 转换成为长整性

同时 每一口行情报价呢 必须带有时间 这里接受的时间呢 是精确到秒 而且他是与日期分离开来

需要做一层转换和封装 转换为浪形的时间戳

具体的可以参考他问的data time这个方法 在这里呢 咱们也做了相应的实现 可以看到

他的一个调用处理 他会将data以及的time两个时间信息呢 转换成为一个

长整性的时间戳 这个呢 是精确到秒

好 这一讲呢 就是对第三方行情源对接他整体逻辑的实现

这一讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个股票行情数据聚合平台的开发教程，具体聚焦于“第三方行情源对接”的实现。讲师通过 IntelliJ IDEA 开发环境，演示了如何创建一个名为 `JuheThirdApi` 的 Spring Boot 组件类，用于调用第三方（如“聚合数据”）的股票行情接口。实现过程包括：配置接口参数、定义市场枚举、构建请求参数、发送 HTTP 请求、解析 JSON 响应并转换为平台内部的 `TradeStockQuoteLast` 对象。整个过程强调了代码的健壮性，例如对 HTTP 状态码的检查和异常捕获。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开始，展示课程大纲，定位到“3.4 第三方行情源对接实现”章节。
*   **00:00:05 - 00:00:15**：讲师在 IDE 中创建 `sources` 包，并在其中新建 `JuheThirdApi` 类。
*   **00:00:15 - 00:00:30**：在 `JuheThirdApi` 类中，定义了用于注入第三方 API 配置的私有字段 `APPKEY`、`url` 和 `url_hs`。
*   **00:00:30 - 00:00:45**：讲师在 `common` 模块中创建 `StockMarketEnum` 枚举类，用于定义不同市场的编号和标识。
*   **00:00:45 - 00:01:00**：在 `JuheThirdApi` 类中，实现 `getStockCodeByMarket` 方法，根据 `TradeStock` 对象的市场编号获取对应的市场标识符。
*   **00:01:00 - 00:01:15**：实现 `getStockReal` 方法，构建请求参数 `params`，并使用 `HttpPoolUtil` 发送 POST 请求。
*   **00:01:15 - 00:01:30**：讲师演示如何解析 HTTP 响应，使用 `GsonConvertUtil` 将 JSON 字符串转换为 `JSONObject`。
*   **00:01:30 - 00:01:45**：在 `getStockReal` 方法中，调用 `parseFromJson` 方法将解析后的数据填充到 `TradeStockQuoteLast` 对象中。
*   **00:01:45 - 00:02:00**：讲师在 `parseFromJson` 方法中，逐个设置 `TradeStockQuoteLast` 对象的属性，如价格、成交量、买卖五档等。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**：
    *   **章节标题**：`3.4 第三方行情源对接实现`。
    *   **关键说明**：`getStockReal` 方法用于获取行情报价的具体实现，需处理多个产品行情，内部需检查 HTTP 状态码并加入预警机制。
    *   **注意事项**：使用 JSON 工具转换数据时，需参考接口文档，避免数据错位。

*   **代码关键内容**：

    *   **`JuheThirdApi.java` 类定义**：
        ```java
        @Component
        @Log4j2
        public class JuheThirdApi {
            @Value("${quote.appkey}")
            private String APPKEY;
            @Value("${quote.url}")
            private String url;
            @Value("${quote.url}.concat('/hs')")
            private String url_hs;
        }
        ```

    *   **`StockMarketEnum.java` 枚举类**：
        ```java
        public static StockMarketEnum parseByMarketNo(int marketNo) {
            for (StockMarketEnum marketEnum : values()) {
                if (marketNo == marketEnum.getMarketNo()) {
                    return marketEnum;
                }
            }
            return null;
        }
        ```

    *   **`getStockCodeByMarket` 方法**：
        ```java
        private String getStockCodeByMarket(TradeStock stock) {
            if (null != stock) {
                StockMarketEnum marketEnum = StockMarketEnum.parseByMarketNo(stock.getMarketNo());
                return marketEnum.getMarketFlag().toLowerCase() + stock.getCode();
            }
            return stock.getCode();
        }
        ```

    *   **`getStockReal` 方法**：
        ```java
        public TradeStockQuoteLast getStockReal(TradeStock stock) {
            Map<String, String> params = new HashMap<>();
            params.put("gid", getStockCodeByMarket(stock));
            params.put("key", APPKEY);
            TradeStockQuoteLast quoteLast = null;
            try {
                HttpPoolUtil.HttpResult result = HttpPoolUtil.getSingleton().postWithAgent(url_hs, params);
                if (result.getResponseCode() == 200) {
                    JSONObject json = GsonConvertUtil.getSingleton().getJsonObject(result.getBody());
                    JSONObject data = json.getJSONArray("result").getJSONObject(0);
                    quoteLast = parseFromJson(data, stock);
                }
            } catch (Exception e) {
                log.error(e.getMessage(), e);
            }
            return quoteLast;
        }
        ```

    *   **`parseFromJson` 方法**：
        ```java
        private TradeStockQuoteLast parseFromJson(JSONObject data, TradeStock stock) {
            TradeStockQuoteLast quoteLast = new TradeStockQuoteLast();
            quoteLast.setAmount(cvtLong(data, "traAmount"));
            quoteLast.setVolume(cvtLong(data, "traNumber"));
            quoteLast.setUpdateTime(cvtDateTime(data, "date").getAsString(), data.get("time").getAsString());
            quoteLast.setPriceAsk1(cvtLong(data, "sellOnePri"));
            quoteLast.setPriceAsk2(cvtLong(data, "sellTwoPri"));
            quoteLast.setPriceAsk3(cvtLong(data, "sellThreePri"));
            quoteLast.setPriceAsk4(cvtLong(data, "sellFourPri"));
            quoteLast.setPriceAsk5(cvtLong(data, "sellFivePri"));
            quoteLast.setPriceBid1(cvtLong(data, "buyOnePri"));
            quoteLast.setPriceBid2(cvtLong(data, "buyTwoPri"));
            quoteLast.setPriceBid3(cvtLong(data, "buyThreePri"));
            quoteLast.setPriceBid4(cvtLong(data, "buyFourPri"));
            quoteLast.setPriceBid5(cvtLong(data, "buyFivePri"));
            return quoteLast;
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：创建 API 类**（00:00:05 - 00:00:15）
    *   讲师在项目结构中导航到 `sources` 包，右键点击并选择“新建” -> “Java 类”。
    *   输入类名 `JuheThirdApi`，并选择 `public class`。
    *   通过 `@Component` 注解将其标记为 Spring Bean，通过 `@Log4j2` 注解引入日志功能。

*   **场景二：配置参数注入**（00:00:15 - 00:00:30）
    *   讲师在 `JuheThirdApi` 类中定义了三个私有字段：`APPKEY`、`url` 和 `url_hs`。
    *   使用 `@Value("${...}")` 注解，从配置文件中注入第三方 API 的 AppKey、基础 URL 和沪深市场专用 URL。

*   **场景三：定义市场枚举**（00:00:30 - 00:00:45）
    *   讲师在 `common` 模块中创建 `StockMarketEnum` 枚举类。
    *   通过 `parseByMarketNo` 静态方法，根据市场编号查找对应的枚举实例，并返回其市场标识符（如 `sh` 或 `sz`）。

*   **场景四：构建请求参数**（00:00:45 - 00:01:00）
    *   在 `getStockCodeByMarket` 方法中，讲师演示了如何将 `TradeStock` 对象的市场编号转换为标准的市场标识符（如 `sh`）。
    *   通过字符串拼接，将市场标识符与股票代码组合成最终的股票代码。

*   **场景五：发送 HTTP 请求**（00:01:00 - 00:01:15）
    *   讲师在 `getStockReal` 方法中，创建了一个 `HashMap` 用于存储请求参数。
    *   使用 `HttpPoolUtil.getSingleton().postWithAgent(url_hs, params)` 方法，向第三方 API 发送 POST 请求。

*   **场景六：解析 JSON 响应**（00:01:15 - 00:01:30）
    *   讲师演示了如何通过 `GsonConvertUtil` 将 HTTP 响应体（`
