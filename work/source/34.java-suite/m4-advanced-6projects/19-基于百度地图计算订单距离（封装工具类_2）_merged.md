# 19-基于百度地图计算订单距离（封装工具类_2） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那么接下来呢

咱们继续来看咱们这个百度地图啊

这个工具类对吧

刚才呢我们是分析了一下对吧

然后这个工具类里面大概都有哪些方法

我们是把这些方法的创建出来了

但是方法里边的内容呢还没有完善

所以接下来呢

我们就需要来完善一下咱们这些方法

咱们先来做这个看这个

这个是load json对吧

这个方法它的作用就是什么呢

调用我们这个百度地图服务接口

接口地址是不是通过参数传过来对吧

然后呢调用完之后呢

把这个结果给返回就可以了

好

其实这段代码呢

我们前面都已经写过了

咱们前面这两个案例里边

是不是都已经写过了

你看大概就是哪一段代码呢

其实应该就是我们

这段代码

大概就是这段代码对吧

然后你看这是只不过呢

我们就需要把这个地方呢

它是通过参数传给我们的对吧

然后其他地方大概都是类似的

所以说我们就不再手敲了

咱们直接呢

来把这段复制过来

然后呢直接修改一下就可以

你看

然后呢这个命名上

这个咱们给它把这改造一下

好

这个地方呢最好是处理一下对吧

需要try catch啊

我们这边这个好像是处理了

所以说我们直接复制这边这个吧

好Ctrl C

然后呢我们复制这边这个

好重新覆盖一下

你看

这是

这是

这个输出的话呢

为了便于测试呢

我们可以暂时先留着它

好

所以你看啊

这个方法呢就已经搞定了

哎

其实就是把我们原先的这个

哎

这个命方法里面

这一段代码呢

把它复制过来对吧

然后呢

封装成这么一个load json

这么一个方法就可以好

然后接下来呢

我们再到上面来看

这个呢

对应的就是我们地理编码

这个服务接口对吧

现在呢

我们是不是只需要把那个接口地址拼一下

然后呢

这个

调用这个load json这个方法啊

那么具体发请求对吧

由他来发就可以了

好

所以接下来呢

我们来看一下这个get coordination

这个应该怎么写

好

那咱们是不是应该先拼一下我们这个服务的地址

对吧

服务请求地址啊

因为你要调这个方法

需要把这个http url是不是给我传过来

所以我们先在这儿来

拼接一下咱们这个串

好

String

http url

然后这个接口地址的话呢

咱们前面是不是已经拼过了

就是这个地址对吧

那干脆我就直接把这段拿过来了

好

Ctrl c直接拿过来

好

咱们来看

这里边呢

是不是拼进去的有什么呢

有我们这个address

address通过参数给我传过来

还有一个是ak对吧

这个ak的话呢

应该就是我们上面这个大写的ak

那这样的话呢

我们这个接口地址呢

就已经拼好了

拼好了之后啊

咱们是不是就可以来调用

我们这个load json这个方法对吧

直接调用我们下面load json这个方法

然后呢把这个

接口地址传过去

然后呢它会给我们返回相应的json数据

对吧

相应的json数据

然后接下来呢

是不是就是解析这个json数据

但是解析的这个代码呢

我们前面其实也已经写过了对吧

所以说我们也是啊

从前面这个代码直接抄过来就可以了

就是解析这块

解析这块的话应该就在这儿

好

嗯

咱们是不是先是要从这儿对吧

只不过这块呢

我们需要改一下啊

解析的代码

Ctrl C复制过来

然后呢拿到这边来

好

同样还是通过我们这个fastjson对吧

然后呢通过json.pathobject啊

这个fastjson给我们提供的这个类

然后呢来解析

但是这块它为什么报错呢

因为我们这个变量命名不一样了

这是不是应该就是这一块了

好

解析返回的这个json串

然后呢把它解析成map这种类型对吧

所以返回值就是map啊

然后这个输出语句呢我们就不要了啊

然后呢我们先来判断一下getStatus

如果它等于0是不是表示解析成功了

哎结果成功

然后呢再进一步解析

从我们这个location里面再获得什么

进度 纬度

然后呢是不是又进行了一个格式化对吧

进行了一个格式化

这个前面我们都已经测过了啊

所以说呢我们呃最终呢只要返回什么呢

返回这个是不是就可以了

嗯

嗯

这个输出呢也不要了

所以我们这个地方直接return

啊

就可以了

它的结果呢就是进度

然后加上逗号

然后后边加上维度啊

这么一个格式

但这个呢是我们这个呃Status

状态等于0的时候是不是返回这个

哎如果不等于0呢就返回空就可以了

这就说明什么呢

说明这个地址呢它没有解析成功对吧

它肯定是留的留下的这个地址有问题啊

然后呢导致没有这个解析成功

好

所以这个方法呢我们也就已经写完了

其实就是把我们原先这个代码呢

哎给它重新又又封装了一下对吧

封装成了这么一个方法

好

那这个呢也就搞定了啊

那下面呢我们来看下一个就是这个get instance对吧

这个是计算订单距离

那同样呢我们还是需要先来把这个什么呢

哎把咱们这个接口地址是不是先来封装一下

直接从这边来考就可以了啊

嗯

就是

嗯

这块啊

当然需要相应的改造啊

放在这儿

咱们来看一下

这个origin origin的话其实就是这个对吧

然后呢还有destination那这两个就不要了

然后直接拼进去

然后这个ak的话呢肯定需要改一下啊

ak好

这样的话我们这个接口地址是不是就已经拼好了

呃但是这个地方呢有一个细节问题我们需要来说一下

就是什么呢

哎大家还记得吧我们这个origin呢

它它其实它的格式是什么呢

是纬度然后逗号

进度对吧

而我们刚才这个地方呢

哎

这个方法呢

它其实返回的啊返回的这个呃坐标值呢

其实是什么呢

是进度在前面纬度在后边

哎

所以说呢我们这个地方呢就需要来调整一下

来调整一下就是什么呢

我们把这个地方来调一下

哎

一种方式就是什么呢

调整这个哎

哎

它传过来的是这个

这个颈尾度相当于是跟我们这个给它的数据呢

是正好相反的对吧

哎

所以说呢我们需要手动来调一下

然后还有一种方式是什么呢

就是干脆我们这个地方呢

哎

直接就返回什么呢

纬度然后逗号进度

那这样的话呢

我们是不是就不用调整了

直接呢拿过来就可以用

所以这两种方式都可以啊

呃

但是这种如果我们给它调整过来呢

这是比较简单的

也就是把这个纬度放到前面去

然后呢

把这个进度呢

放到后边啊

放到后边

那这样的话呢

就是纬度哎

逗逗号哎

进度

那么正好呢

符合它这边这个格式要求对吧

哎

那这样的话我们这边就不用做任何处理了啊

所以这两种方式都可以

大家只要明白什么意思就行啊

哎

其实就是一些数据格式的处理

哎

谁先谁后的问题

只要那个能给它这个搞对了就可以了

然后后边的话其实就比较简单了对吧

哎

咱们还是从这边来抄一下啊

嗯

也就是说我们先来调一下啊

咱们先调这个load啊

load json这个方法对吧

先把结果呢

获取到

好

这个也是json

然后呢

我们再把解析json的这段代码呢

直接拷过来

我们就不再手敲了

解析json的代码

也是类似的

就是这块

嗯

在哪呢

这个地方对吧

然后呢

我们把这段代码直接复制一下

在这呢

看一下

相应的修改一下就可以了

呃

然后pass object的这个地方呢

是不是应该改成我们上面这个json啊

解析的就是它

然后呢

还是解析成map这种形式对吧

然后呢

判断如果它等于0说明这个又解析成功了

然后呢

我们就把这个

呃

distance是不是给它返回就可以了啊

所以这个地方呢

别忘了把这个return

distance啊

把它返回一下

哎

如果不是不是0

那是不是说明这个计算有问题对吧

咱们还是返回一个空就可以

好

这是我们第二个这个方法呢

也就已经写完了

那么再往下呢

就是get time对吧

这个get time的话

其实跟刚才这个是非常类似的

无非就是这个地方是不是拿的不一样

所以说呢

我们把这段呢

来

复制过来

Ctrl c

复制过来

然后呢

把它贴到这来

那么唯一不同的就是这个地方对吧

然后呢

我们直接把这改成什么呢

get time就可以啊

好

然后呢

它的这个返回值呢

它的这个返回值应该是什么呢

呃

对这个类型啊

需要处理一下对吧

咱们这个是不是要返回的是integer啊

好

所以我们这呢

需要改成什么integer.pathint对吧

integer.pathint

好

这边也错了

呃

然后呢

注意啊

这这这项呢应该不是time

它叫什么呢

我记得叫做duration啊

啊

一会呢

我们可以到那个

它的这个文档上去看一下

好

然后呢

我们把这个time呢

是不是来返回一下就可以了

这个地方呢

得改成int对吧

好

那么整个这个方法呢

我们也就已经写完了

一会呢

咱们来测试一下这个工具类啊

来验证一下我们这些方法是否

都是能够使用的对吧

有没有问题

好

那么关于咱们这个工具类呢

我们先写到这

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频是一个关于如何在 Java 项目中集成百度地图 API 的技术教程。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何编写工具类 `BaiduMapUtils`，以实现三个核心功能：
- **地理编码**：将中文地址（如“北京市朝阳区”）转换为经纬度坐标。
- **距离计算**：根据两个地址的经纬度，计算两点之间的驾车距离。
- **JSON 数据获取**：封装一个通用的 `loadJSON` 方法，用于向百度地图 API 发送 HTTP 请求并解析返回的 JSON 数据。

整个过程强调了如何利用百度地图的开放接口（Geocoding 和 Direction API），并通过 Java 代码进行网络请求、JSON 解析和数据处理，为后续的业务逻辑（如订单距离计算）提供基础支持。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**：开场，展示项目结构和 `BaiduMapTest.java` 文件，介绍本节将实现的功能。
*   **00:05 - 00:15**：讲解 `loadJSON` 方法的必要性，演示其在 `BaiduMapUtils` 类中的位置。
*   **00:15 - 00:30**：编写 `loadJSON` 方法的代码，使用 `URL` 和 `BufferedReader` 读取 HTTP 响应流，并将结果拼接成字符串。
*   **00:30 - 00:45**：讲解 `getCoordinate` 方法，用于地理编码，展示其方法签名和注释。
*   **00:45 - 01:00**：编写 `getCoordinate` 方法的核心逻辑，构造百度地图地理编码 API 的 URL，调用 `loadJSON` 获取响应，解析 JSON 中的 `location` 字段，提取经纬度并格式化返回。
*   **01:00 - 01:15**：讲解 `getDistance` 方法，用于计算两点间距离，展示其方法签名和注释。
*   **01:15 - 01:30**：编写 `getDistance` 方法的核心逻辑，构造百度地图驾车路线规划 API 的 URL，调用 `loadJSON` 获取响应，解析 JSON 中的 `routes` 数组，提取第一个路线对象的 `distance` 字段并返回。
*   **01:30 - 01:45**：补充 `getDistance` 方法，解析 `duration` 字段（行程时间），并展示如何返回。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段**：

    *   **`loadJSON` 方法**：
        ```java
        public static String loadJSON(String httpUrl) {
            StringBuilder json = new StringBuilder();
            try {
                URL url = new URL(httpUrl);
                URLConnection urlConnection = url.openConnection();
                BufferedReader in = new BufferedReader(new InputStreamReader(urlConnection.getInputStream(), "UTF-8"));
                String inputLine = null;
                while ((inputLine = in.readLine()) != null) {
                    json.append(inputLine);
                }
                in.close();
            } catch (MalformedURLException e) {
                e.printStackTrace();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return json.toString();
        }
        ```

    *   **`getCoordinate` 方法**：
        ```java
        public static String getCoordinate(String address) {
            String httpUrl = "http://api.map.baidu.com/geocoding/v3/address" + "&address=" + address + "&output=json&ak=" + AK;
            String json = loadJSON(httpUrl);
            Map map = JSON.parseObject(json, Map.class);
            String status = map.get("status").toString();
            if (status.equals("0")) {
                // 返回结果成功，能够正常解析地址信息
                Map result = (Map) map.get("result");
                Map location = (Map) result.get("location");
                String lng = location.get("lng").toString();
                String lat = location.get("lat").toString();
                DecimalFormat df = new DecimalFormat(pattern: "#.######");
                String lngStr = df.format(Double.parseDouble(lng));
                String latStr = df.format(Double.parseDouble(lat));
                String r = latStr + "," + lngStr;
                return r;
            }
            return null;
        }
        ```

    *   **`getDistance` 方法**：
        ```java
        public static Double getDistance(String origin, String destination) {
            String httpUrl = "http://api.map.baidu.com/directionlite/v1/driving?origin=" + origin + "&destination=" + destination + "&ak=" + AK;
            String json = loadJSON(httpUrl);
            Map map = JSON.parseObject(json, Map.class);
            if ("0".equals(map.getOrDefault("status", "500").toString())) {
                Map childMap = (Map) map.get("result");
                JSONArray jsonArray = (JSONArray) childMap.get("routes");
                JSONObject jsonObject = (JSONObject) jsonArray.get(0);
                double distance = Double.parseDouble(jsonObject.get("distance").toString()) == null ? "0" : jsonObject.get("distance").toString();
                System.out.println(distance);
                return distance;
            }
            return null;
        }
        ```

*   **关键注释**：
    *   `getCoordinate` 方法注释：`调用百度地图地理编码服务接口，根据地址获取坐标（经度、纬度）`
    *   `getDistance` 方法注释：`调用百度地图驾车路线规划服务接口，根据寄件人地址和收件人地址坐标计算订单距离`
    *   `loadJSON` 方法注释：`调用服务接口，返回百度地图服务端的结果`

*   **关键常量**：
    *   `AK`：百度地图的密钥，用于验证 API 调用。

---

### 4) 关键场景与演示描述

*   **场景一：项目结构与方法定位**
    *   讲师首先展示了项目的整体结构，包括 `src/main/java` 和 `src/main/resources` 目录。
    *   他将光标移动到 `BaiduMapUtils.java` 文件，并定位到 `getCoordinate`、`getDistance` 和 `loadJSON` 方法，说明这些方法将共同完成地理编码和距离计算功能。

*   **场景二：编写 `loadJSON` 方法**
    *   讲师在 `BaiduMapUtils` 类中创建了 `loadJSON` 方法。
    *   他演示了如何使用 `URL` 类创建网络连接，并通过 `BufferedReader` 逐行读取 HTTP 响应流。
    *   他强调了 `UTF-8` 编码的重要性，并展示了如何将读取到的字符串拼接成一个完整的 JSON 字符串。

*   **场景三：实现 `getCoordinate` 方法**
    *   讲师展示了如何构造百度地图地理编码 API 的 URL，其中包含了地址参数和密钥 `AK`。
    *   他调用 `loadJSON` 方法获取响应，并使用 `JSON.parseObject` 将 JSON 字符串解析为 `Map` 对象。
    *   他演示了如何检查 `status` 字段，如果为 `"0"`，则表示请求成功。
    *   他提取了 `location` 对象中的 `lng` 和 `lat` 字段，并使用 `DecimalFormat` 格式化为字符串，最终拼接成 `lat,lng` 格式返回。

*   **场景四：实现 `getDistance` 方法**
    *   讲师展示了如何构造百度地图驾车路线规划 API 的 URL，其中包含了起点和终点参数。
    *   他调用 `loadJSON` 方法获取响应，并解析 JSON。
    *   他演示了如何检查 `status` 字段，如果为 `"0"`，则表示请求成功。
    *   他提取了 `routes` 数组中的第一个元素，并从中获取 `distance` 字段，将其转换为 `double` 类型并返回。
    *   他还演示了如何同时提取 `duration` 字段（行程时间），并将其转换为 `int` 类型。

整个演示过程清晰、步骤明确，旨在教授观众如何在 Java 应用中集成百度地图 API，以实现地理信息相关的功能。
