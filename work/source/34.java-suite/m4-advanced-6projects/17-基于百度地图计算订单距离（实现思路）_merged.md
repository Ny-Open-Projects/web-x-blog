# 17-基于百度地图计算订单距离（实现思路） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来咱们继续来看我们品达物流项目第四章的内容

前面咱们是通过七个案例来学习了一下我们百度地图的用法

接下来我们来看下一个小节,就是基于百度地图来计算订单的距离

这个地方我们需要来说明一下,我们为什么要计算订单距离呢?

实际上我们最终的目的是需要来计算出来订单的价格

那么用户其实在下单的时候,我们会给他预估一下他这个订单大概是多少钱

具体这个价格是怎么算出来的呢?

其中有一个维度就是订单的距离

前面咱们其实也说过了,一个是他所计的货物的重量

还有一个维度就是订单的距离

所以说我们下边要做的这个事,要计算订单距离

是为我们最终要计算订单距离

这个订单距离的价格来服务的

相当于是他的一个前提条件

这是我们先来说明一下

那接下来我们就来看一下

我们要计算这个订单距离

他的实现思路是什么样子的

那么他的实现思路其实是这样的

首先第一步呢

我们可以调用这个百度地图提供的地理编码这个接口

前面我们是不是也已经写过了

可以根据什么呢?

根据订单中他这个寄件人的地址还有收件人的地址呢?

分别来获取经纬度

你看咱们前面呢

我们是不是写了这么两个测试对吧

第一个这个接口

这个接口呢对应的就是我们地理编码

对吧,地理编码这个接口

然后呢,我可以根据什么呢?

客户他所留下的寄件人地址还有收件人地址

然后呢我调用这个接口

他是不是可以给我返回相应的这个什么呢?

坐标信息对吧,坐标信息

那么坐标信息呢就是由这个

径度还有纬度来构成的

这是第一步

这个接口呢我们前面都已经测过了

肯定是能够得到的对吧

然后接下来呢有了经纬度之后呢

我们就可以调用什么呢?

咱们这个驾车路线规划

也就是我们这第二个这个接口

然后呢调用这个接口的话呢

他就可以给我们返回很多数据

其中有一个就是什么呢?

有一个就是这个distance对吧

就这么一项

他代表的就是什么呢?

就是由我们这个起点位置到终点位置对吧?

他所经过的这个距离

所以说呢调用这第二个接口呢

就可以来计算出来

这是咱们实现的思路

你看我们前面设计的这两个案例对吧?

其实呢也都可以用到啊

就是为我们这个地方来服务的

这是这两个接口的调用

通过这两次接口调用呢

就可以把我们订单的距离呢给算出来

这是咱们这个实现思路呢

我们先来明确一下

一会儿呢我们来封装一个工具类

这个工具类呢其实就是来完成这个事儿

因为我们前面呢

虽然这个工作也做完了

但是呢这个是通过一个MIM方法这种方式对吧?

那么为了后边呢能够复用啊

用起来更方便

那么我们一会儿呢来封装一个工具类

把咱们要做的这些事儿呢

全都封装到这个工具类当中

后边呢我们如果想这个计算订单距离

直接调用工具类的某个方法

就可以完成

好这是咱们先把这个思路明确一下

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段是关于一个“品达物流TMS项目”中“订单中心服务开发”模块的实战教学。讲师通过演示一个名为 `BaiduMapTest2` 的 Java 类，详细讲解了如何调用百度地图的 HTTP API 来计算订单距离。核心内容包括：
- **地理编码**：将中文地址（如“北京市育新花园小区”）转换为经纬度坐标。
- **驾车路线规划**：使用获取到的经纬度，调用百度地图的驾车路线规划接口，计算两点间的距离。
- **HTTP 请求与响应处理**：使用 `URL`、`URLConnection`、`BufferedReader` 等类进行 HTTP 请求，并用 `StringBuilder` 汇总响应内容。
- **JSON 数据解析**：使用 FastJSON 库将服务器返回的 JSON 字符串解析为 Java `Map` 对象，并从中提取距离信息。
- **异常处理**：对 API 返回的错误状态码进行判断，确保程序健壮性。

整个过程旨在为后续的订单服务开发（如计算运费）提供基础的地理信息支持。

---

### 2) 按时间顺序的章节（带时间点）

由于提供的画面没有明确的时间戳，以下时间点是根据画面内容和逻辑顺序推断的：

- **00:00 - 00:05**：开场，展示项目结构和 `BaiduMapTest2.java` 文件，介绍本节目标是调用百度地图 API 计算订单距离。
- **00:05 - 00:15**：讲解 `BaiduMapTest2` 类的代码结构，重点是 `main` 方法中定义的 `ak`（密钥）、`origin`（起点经纬度）、`destination`（终点经纬度）和 `httpUrl`（请求地址）。
- **00:15 - 00:30**：演示如何构建 HTTP 请求，使用 `URL` 和 `URLConnection`，并创建 `BufferedReader` 读取响应流。
- **00:30 - 00:45**：展示如何将响应内容逐行读取并拼接成字符串，使用 `StringBuilder`。
- **00:45 - 01:00**：讲解如何使用 FastJSON 库解析 JSON 数据，将字符串转换为 `Map` 对象，并提取 `status` 和 `distance` 字段。
- **01:00 - 01:15**：演示如何处理 API 返回的错误状态码，确保程序在异常情况下也能正常运行。
- **01:15 - 01:30**：总结本节内容，强调地理编码和路线规划在订单系统中的重要性。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

- **文档标题**：`TMS项目源码_第4章_订单中心服务开发(pd-oms)`
- **章节标题**：`5. 基于百度地图计算订单距离`
- **子章节**：
  - `5.1 实现思路`：详细描述了两步实现过程：
    1.  调用百度地图的地理编码接口，获取地址的经纬度。
    2.  调用百度地图的驾车路线规划接口，根据经纬度获取距离。
  - `5.2 封装工具类`：介绍了封装操作百度地图接口的工具类，其包路径为 `com.itehima.pinda.common.utils;`，并列出了需要导入的依赖库，如 `com.alibaba.fastjson.JSON`、`java.io.BufferedReader`、`java.math.BigDecimal` 等。

#### 代码关键内容

- **类定义**：
  ```java
  package com.itehima.test;
  public class BaiduMapTest2 {
  ```

- **HTTP 请求构建**：
  ```java
  String httpUrl = "http://api.map.baidu.com/geocoding/v3/?address=" + address + "&output=json&ak=" + ak;
  URL url = new URL(httpUrl);
  URLConnection urlConnection = url.openConnection();
  ```

- **响应读取**：
  ```java
  StringBuilder stringBuilder = new StringBuilder();
  InputStream inputStream = urlConnection.getInputStream();
  BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(inputStream, "UTF-8"));
  String inputLine = null;
  while ((inputLine = bufferedReader.readLine()) != null) {
      stringBuilder.append(inputLine);
  }
  bufferedReader.close();
  ```

- **JSON 解析与距离提取**：
  ```java
  String data = stringBuilder.toString();
  Map map = JSON.parseObject(data, Map.class);
  if ("0".equals(map.getOrDefault("status", "500").toString())) {
      Map childMap = (Map) map.get("result");
      JSONArray jsonArray = (JSONArray) childMap.get("routes");
      JSONObject jsonObject = (JSONObject) jsonArray.get(0);
      double distance = Double.parseDouble(jsonObject.get("distance").toString());
      System.out.println(distance);
  }
  ```

---

### 4) 关键场景与演示描述

- **场景一：地理编码接口调用**
  - 讲师在 `BaiduMapTest2.java` 中定义了 `address` 为“北京市育新花园小区”，并构造了地理编码的 URL。
  - 通过 `URL` 和 `URLConnection` 发起 HTTP 请求，模拟了向百度地图服务器发送地址查询的全过程。

- **场景二：驾车路线规划接口调用**
  - 讲师切换到另一个示例，展示了如何使用 `origin` 和 `destination` 两个经纬度坐标，构造驾车路线规划的 URL。
  - 通过 `BufferedReader` 读取服务器返回的 JSON 数据流，并将其存储在 `StringBuilder` 中。

- **场景三：JSON 数据解析**
  - 讲师将 `StringBuilder` 中的字符串转换为 `Map` 对象。
  - 通过 `map.get("status")` 检查 API 返回的状态码，如果为 `"0"`，则表示请求成功。
  - 从 `result` 字段中提取 `routes` 数组，再从第一个元素中获取 `distance` 字段，最终输出距离值。

- **场景四：异常处理与健壮性**
  - 讲师强调了 `if ("0".equals(...))` 这个判断语句的重要性，它确保了只有在请求成功时才进行后续的数据解析。
  - 这体现了在实际开发中，对 API 响应进行错误处理和容错设计的必要性。

- **场景五：工具类设计**
  - 讲师在 PPT 中展示了 `5.2 封装工具类` 的内容，强调了将重复的 HTTP 请求和 JSON 解析逻辑封装到一个工具类中，可以提高代码的复用性和可维护性。

---

以上是根据视频画面进行的详细结构化分析。
