# 16-百度地图开放平台（入门案例_案例七_2） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来咱们继续来看我们百度地图开放平台的入门案例

刚才我们是讲到这个案例7

我们是在这个浏览器当中访问它这个http接口

并且能够返回出来这个数据

接下来我们就需要在咱们的Java程序当中来调用这个http接口

并且来解析返回的数据

整个这个过程其实跟我们刚才这个地方调用它这个接口实现这个什么地理编码

整个思路是完全一样的

所以我们这个地方就不再去再手敲了

咱们直接把我们这个程序把它复制到我们这个项目当中来运行一下就可以了

整个套路都是一样的

咱们先大概读一下这个代码就行了

你看ak origin destination把这些值是不是都给拼好

拼好了之后把这个URL地址是不是也拼对

然后接下来我们是不是还是使用的这个URL

然后open connection对吧

然后还是得到这个input stream

得到输入流

然后一个一个来读

读完之后呢

把它放到这个stream builder里面去

对吧

然后在这输出一下

这就返回结果

接下来呢

是不是这段呢

就是进行解析

那么我们这块呢

主要解析的是什么呢

想要的是它这个distance

也就是说我们这个路线规划完之后啊

它这个实际的距离是多少

因为在我们后边的项目当中会用到

就是实现我们这个距离的计算

前面呢

我们其实也提到了

对吧

你看在我们这块的话

我们是不是需要来计算我们订单的距离

只不过这个

订单的距离呢

就是寄件人地址到收件人地址

对吧

所以到时候呢

我们需要干什么呢

先根据这个寄件人地址

还有收件人地址啊

然后呢

先是调用第一个这个接口来实现地理编码

也就是把我们这个地址信息给它转成坐标

然后有了坐标之后呢

再调用这第二个接口

根据这个坐标来实现这么一个路线规划

最终呢

我们想拿到的是它的这个什么呢

这个距离也就是distance这个字段的值

那

接下来呢

咱们就来把这个代码呢

我就不写了

直接抄到这边来

咱们这个呢

我就不覆盖了

重新创建一个就可以了

好

然后呢

这里边这个代码就不要了

咱们呢

直接从我们这个讲义上把这个代码拷过来

就直接只拷这个Main方法里边的这个代码就行啊

复制

这是需要导入一下

FastDacent的

好

这个也需要来导一下

好

那接下来呢

我们就来运行一下

这个呢

是从这个坐标点对吧

到这个坐标点

从其实位置这个坐标

纬度精度啊

这个也是

这是这个终点对吧

它的纬度精度啊

然后呢

调用这个接口把数据返回来

返回来之后呢

我们在这儿来进行解析

最终呢

我们是把这个什么distance啊

也就是它这个订单的距离对吧

哎

那么给它解析出来

好

咱们直接来执行这个Main方法

好

你看这个距离其实就已经解析出来了

对吧

是18709

啊

但是这个单位是什么呢

单位应该是米对吧

单位是米

好

所以这个程序呢

跟我们前面这个程序

其实整个套路是完全一样的

无非就是调用的这个接口对吧

这个接口地址不一样

其他的都是一样的

好

这是关于我们这第七个入门案例

咱们先说到这儿

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段是关于一个 Java 项目中如何使用百度地图开放平台的 HTTP API 来计算两点之间的距离。讲师通过一个名为 `BaiduMapTest` 的测试类，演示了如何构造请求 URL、发送 HTTP 请求、读取返回的 JSON 数据，并解析其中的“距离”字段。整个过程旨在为后续的订单系统开发（如计算订单距离、价格等）提供技术基础。视频中同时展示了项目结构、代码编写、以及如何使用 FastJSON 库进行 JSON 解析。

---

### 2) 按时间顺序的章节（带时间点）

由于无法从画面中精确获取视频时间戳，以下章节是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:15**: **项目与环境介绍**。讲师展示了 IntelliJ IDEA 中的项目结构，包括 `pd-oms`、`pd-base` 等模块，并定位到 `test` 包下的 `BaiduMapTest.java` 文件。
*   **00:15 - 00:30**: **代码编写与API调用**。讲师开始编写 `BaiduMapTest` 类，定义了百度地图的 AK（密钥）和两个测试地址（起点和终点），并构造了用于计算驾车距离的 HTTP 请求 URL。
*   **00:30 - 00:45**: **发送请求与读取响应**。讲师编写了 `try-catch` 块，使用 `URL`、`URLConnection` 和 `BufferedReader` 来发送请求并读取服务器返回的 JSON 字符串。
*   **00:45 - 01:00**: **JSON数据解析**。讲师展示了如何将读取到的字符串转换为 `Map` 对象，并通过 `get` 方法提取 `status` 和 `result` 字段。
*   **01:00 - 01:15**: **提取距离信息**。讲师演示了如何从 `result` 中获取 `routes` 数组，再从中提取第一个元素的 `distance` 字段，并将其转换为 `double` 类型。
*   **01:15 - 01:30**: **输出结果**。讲师将解析出的距离值打印到控制台，完成整个流程。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**：
    *   左侧导航栏显示了当前文档的目录结构，包括“第4章 订单中心服务开发”、“4.3 人门案例”、“5. 基于百度地图计算订单距离”等。
    *   第5章标题为“**5. 基于百度地图计算订单距离**”，子标题“**5.1 实现思路**”。
    *   PPT 文本描述了实现思路：“前面我们通过入门案例已经对百度地图的使用有所了解，本节我们就调用百度地图提供的HTTP接口服务来实现订单距离的计算”。

*   **代码关键内容**：

    ```java
    // 1. 导入必要的包
    import com.alibaba.fastjson.JSON;
    import java.io.BufferedReader;
    import java.io.IOException;
    import java.net.URL;
    import java.net.URLConnection;
    import java.util.Map;

    // 2. 定义测试类和主方法
    public class BaiduMapTest {
        public static void main(String[] args) throws Exception {
            // 3. 设置百度地图AK（密钥）
            String ak = "UEBQm9c3KZ5LrsO2C2qsOAsleSdlvZm"; // 注意，ak类型必须为服务端类型
            // 4. 设置起点和终点坐标
            String origin = "40.01116,116.339303"; // 起点经纬度，格式为：纬度,经度；小数点后不超过6位
            String destination = "39.936404,116.452562"; // 终点经纬度，格式为：纬度,经度；小数点后不超过6位
            // 5. 构造HTTP请求URL
            String httpUrl = "http://api.map.baidu.com/directionlite/v1/driving?origin=" + origin + "&destination=" + destination + "&ak=" + ak;

            // 6. 发送请求并读取响应
            URL url = new URL(httpUrl);
            URLConnection urlConnection = url.openConnection();
            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(urlConnection.getInputStream(), "UTF-8"));
            StringBuilder json = new StringBuilder();
            String inputLine = null;
            while ((inputLine = bufferedReader.readLine()) != null) {
                json.append(inputLine);
            }
            bufferedReader.close();

            // 7. 解析JSON数据
            String data = json.toString();
            if (data != null && !"".equals(data)) {
                Map map = JSON.parseObject(data, Map.class);
                if ("0".equals(map.getOrDefault("status", "500").toString())) {
                    Map childMap = (Map) map.get("result");
                    JSONArray jsonArray = (JSONArray) childMap.get("routes");
                    JSONObject jsonObject = (JSONObject) jsonArray.get(0);
                    double distance = Double.parseDouble(jsonObject.get("distance").toString());
                    System.out.println(distance);
                }
            }
        }
    }
    ```

*   **公式与图表**：
    *   无明确的数学公式。
    *   无图表。

---

### 4) 关键场景与演示描述

*   **场景一：项目结构展示** (00:00-00:15)
    *   讲师在 IntelliJ IDEA 中展示了项目的整体结构，鼠标选中了 `test` 包下的 `BaiduMapTest.java` 文件，为后续代码演示做准备。

*   **场景二：构造请求URL** (00:15-00:30)
    *   讲师在代码中定义了百度地图的 AK，并设置了两个测试地址（起点和终点）。
    *   他将这些参数拼接成一个完整的 HTTP 请求 URL，用于调用百度地图的驾车距离计算接口。

*   **场景三：发送请求与读取响应** (00:30-01:00)
    *   讲师使用 `URL` 和 `URLConnection` 对象创建了网络连接。
    *   他使用 `BufferedReader` 逐行读取服务器返回的 JSON 数据，并将其拼接成一个 `StringBuilder` 对象。

*   **场景四：JSON数据解析** (01:00-01:15)
    *   讲师将读取到的 JSON 字符串使用 `JSON.parseObject` 方法解析为一个 `Map` 对象。
    *   他检查了 `status` 字段，确保请求成功（值为 "0"）。
    *   他从 `result` 中获取 `routes` 数组，并取第一个元素。

*   **场景五：提取并输出距离** (01:15-01:30)
    *   讲师从 `routes` 数组的第一个元素中提取 `distance` 字段。
    *   他使用 `Double.parseDouble` 将字符串距离转换为 `double` 类型。
    *   最后，他通过 `System.out.println` 将计算出的距离值打印到控制台，完成演示。
