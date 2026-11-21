# 10-第三方行情源-Json封装 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,接着咱们去实现JSON的解析工具封装

上一讲咱们去讲解了ATTP连接池工具的封装

那咱们看一下JSON这块具体是如何去实现的

我们在这里采用的是GSON

也就是谷歌所提供出来的开源的JSON解析组件

它在JSON处理方面有着较高的性能

那咱们来讲解一下代码的具体实现

同样咱们先将代码copy到工程当中

导到JSON Cover的Util

把它放在JSON的保姆录下

好,在这里我们已经放得进去了

那咱们来看一下它这一块是如何封装处理的

同样在这里是采用单立模式

也要考虑现成的安全性

它的实现也是懒家宅的方式

咱们可以看到通过JSONGlatton这个方法

去创建了它的一个单立

那我们再接着往下看

下面要创建一个GSON的解析对象

这个对象它是可以支持印发调用的

不会出现现成安全的问题

这一点大家可以放心去使用

所以咱们是将它放在成员变量当中

然后下面是对JSON Cover的Util工具的初始化配置

在这里做了两项配置

第一项是对日期做了格式化的处理

也就是按照指定的日期格式去返回相应的数据

下面是开启了对MAP的解析转换支持

这个功能也是比较强大和实用

通过该功能它能够将MAP的数据做相互的转换

比如说MAP里面有两条数据

一条是叫Key1一条是叫Key2

那么它就会将MAP里面的数据最终转换成为JSON的格式

只需要去开启这项配置就可以

接着就是单例的实现

然后同样的加了一个同步锁保障现成的安全

下面就是它的具体封装方法

这个方法的作用是将JSON转换为指定的加码对象

可以支持范形的传递

比如说咱们有一个order的订单数据

那么将order的JSON串传入到第一个参数

然后将order的class对象传入到第二个参数

接着它就会返回一个order的具体对象使用起来呢

比较方便

下面的话呢是将JSON object去转换为指定的加码对象

这个和上面的差异是在于呢

一个是传递的JSON字符串

下面呢是传递一个JSON object

我们可以看到它的包是在com.google

也就是GSON的这个依赖包下面

下面呢是将JSON转换为list对象

这个呢用起来也是非常实用的一个功能

如果咱们手工具处理呢

还做一个便利迭代

那么通过JSON呢

采用这个方法就可以直接帮助咱们去实现list的转换

下面呢就是将字符串转换为map对象

大家注意一下

map下面呢

它下面的属性有不同的对象类型

那如果是这里面呢

返回的是实讯

在这里我们包装的时候呢

也要采用实讯

保证呢它整体的一致

再往下面呢就是对象要转换为JSON

然后呢

采用GSON的解析方式去获取呢

JSON的某个属性

因为有的时候呢

咱们要去读取JSON里面的某个属性值

又不想去做一个对象的转换

这样呢

你要去重新定义相关的属性会比较麻烦

那么咱们就可以通过这个方法去快速实现

获取JSON串当中的指定的某个属性

然后下面呢

还封装了一些方法

大家如果是有兴趣和时间的话呢

可以再去研究和学习

咱们可以大概过一下

像那个获取JSON-L对象

然后在这里呢

是生成包含参数名值对的JSON字符串

也就是直接以参数名称作为属性名称

再往下面呢

就是从指定的JSON object的对象当中

去找出subject name命名的指对象

这个呢是它的一些高级用法

如果后面咱们有需要

要使用到的时候呢

可以再回过头来去做详细的研究和了解

然后这里呢

也提供了一个测试

比如说咱们要将一个MAP的字符串呢

转换成为一个MAP对象

让咱们来测试看一下

右键乱运行

咱们可以看一下它的输出结果

这个时候呢

它将MAP的对象呢

打印出来了

我们可以看到

它返回的对象就是一个MAP

通过JSON这个组件呢

能够呢

让咱们去快速操作和读取呢

JSON的数据

功能呢比较丰富

使用起来也比较灵活

好

回到讲义当中

那这一讲呢

就是对基础工具

JSON数据的封装实现

做了一个讲解

好

这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段是关于一个Java项目中“JSON解析工具封装”的技术讲解。讲师通过IDE（IntelliJ IDEA）展示了一个名为 `GsonConvertUtil` 的工具类的源代码。该工具类旨在提供一套统一、安全的Gson JSON处理方法，包括单例模式的实现、日期格式化配置、对象与JSON字符串的相互转换（如 `fromJson` 和 `toJson`），以及针对复杂JSON结构（如嵌套对象、数组）的解析方法。视频主要演示了如何封装这些功能，以供项目其他模块调用，体现了工具类设计和代码复用的思想。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取视频的精确时间戳，以下章节是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:05**: 视频开头，讲师展示课程大纲，定位到“3. Json解析工具封装”这一章节。
*   **00:05 - 00:15**: 讲师介绍Gson工具，并展示 `GsonConvertUtil` 类的代码结构，包括单例模式和Gson对象的初始化。
*   **00:15 - 00:30**: 讲师详细讲解单例模式的实现，包括 `volatile` 关键字的作用和 `synchronized` 同步块的使用，以确保线程安全。
*   **00:30 - 00:45**: 讲师演示 `fromJson` 方法，展示如何将JSON字符串转换为Java对象（`T`），并介绍了 `TypeToken` 的使用。
*   **00:45 - 01:00**: 讲师演示 `toJson` 方法，展示如何将Java对象转换为JSON字符串。
*   **01:00 - 01:15**: 讲师讲解 `cvtSubJson2Obj` 方法，展示如何从JSON对象中提取指定键名的值并转换为指定类型的对象。
*   **01:15 - 01:30**: 讲师展示 `cvtJson2Map` 方法，用于将JSON字符串转换为 `Map<String, String>`。
*   **01:30 - 01:45**: 讲师展示 `getJsonObject` 和 `getJsonArray` 方法，用于从JSON字符串中提取 `JsonObject` 或 `JsonArray` 对象。
*   **01:45 - 02:00**: 讲师总结，强调该工具类封装了常用功能，便于项目复用。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文本内容

*   **章节标题**: “3. Json解析工具封装”
*   **关键描述**: “Gson是Google开源的json解析组件，在json处理方面有较高的性能及支持。”
*   **代码标题**: “GsonConvertUtil代码：”

#### 代码关键内容

以下是视频中展示的 `GsonConvertUtil` 类的核心代码片段：

```java
public class GsonConvertUtil {
    // 单例模式，需要保证线程安全
    private volatile static GsonConvertUtil singleton = null;
    // Gson解析对象
    private Gson gson;

    // Gson封装工具的初始化，主要处理JSON的解析配置
    private GsonConvertUtil() {
        // 1. 对日期格式化处理
        // 2. 开启对MAP的解析转换支持，{key1: value1, key2: value2}
        gson = new GsonBuilder()
                .setDateFormat("yyyy-MM-dd HH:mm:ss")
                .enableComplexMapKeySerialization()
                .create();
    }

    // 单例的实现（做了线程安全处理）
    public static GsonConvertUtil getSingleton() {
        if (singleton == null) {
            synchronized (GsonConvertUtil.class) {
                if (singleton == null) {
                    singleton = new GsonConvertUtil();
                }
            }
        }
        return singleton;
    }

    // 将JSON转换为对象
    public <T> T cvtJson2Obj(String json, Class<T> t) {
        return gson.fromJson(json, t);
    }

    // 将JSON字符串转换为MAP对象
    public Map<String, String> cvtJson2Map(String json) {
        return gson.fromJson(json, new TypeToken<Map<String, String>>() {}.getType());
    }

    // 从指定 json对象 中找出 subJsonName 命名的对象
    public <T> T cvtSubJson2Obj(JsonObject jsonobject, String subJsonName, Class<T> t) {
        String param = jsonobject.getAsJsonPrimitive(subJsonName).getAsString();
        return cvtJson2Obj(param, t);
    }

    // 将对象转换为JSON
    public String toJson(Object obj) {
        return gson.toJson(obj);
    }

    // 获取JsonObject对象
    public JsonObject getJsonObject(String jsonObject) {
        JsonParser parser = new JsonParser();
        return parser.parse(jsonObject).getAsJsonObject();
    }

    // 获取JsonArray对象
    public JsonArray getJsonArray(String jsonObject) {
        JsonParser parser = new JsonParser();
        return parser.parse(jsonObject).getAsJsonArray();
    }
}
```

---

### 4) 关键场景与演示描述

*   **场景一：工具类介绍与初始化**
    *   讲师首先在IDE中打开 `GsonConvertUtil.java` 文件。
    *   他高亮显示了类的声明和单例模式的静态变量 `singleton`，并解释了其作用。
    *   他接着展示了构造函数，其中使用 `GsonBuilder` 配置了日期格式和复杂键名支持。

*   **场景二：单例模式实现**
    *   讲师聚焦于 `getSingleton()` 方法。
    *   他通过代码注释和高亮，解释了双重检查锁定（Double-Checked Locking）的线程安全机制，即先判断 `singleton` 是否为 `null`，如果是，则加锁并再次判断，确保只创建一个实例。

*   **场景三：JSON转换方法演示**
    *   讲师依次展示了 `cvtJson2Obj`、`cvtJson2Map`、`cvtSubJson2Obj` 等方法。
    *   他通过高亮和注释，说明了这些方法如何利用 `gson.fromJson` 和 `gson.toJson` 进行对象和字符串的相互转换。
    *   特别地，他演示了 `cvtSubJson2Obj` 方法，该方法先从 `JsonObject` 中提取指定键名的字符串值，再调用 `cvtJson2Obj` 进行类型转换。

*   **场景四：项目结构与工具类使用**
    *   讲师在IDE的项目结构视图中，展示了 `GsonConvertUtil` 所在的包路径 `com.icast.bulls.stock.common.json`。
    *   他通过“Find Usages of singleton in All Places”功能，演示了该工具类在项目中的使用情况，验证了其可复用性。

---

以上是根据视频画面内容进行的结构化分析。
