# 33-声明式缓存（声明式缓存代码实现_编写抽象 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来咱们继续来看我们抽象的缓存注解处理器,刚才我们是编写了generate key这个方法,就是解析我们注解信息动态来生成key,那么这块可能大家对于我们生成的key它的规则,或者是它最终生成什么样的key,可能并不是特别了解,所以说我们可以把我们讲一上这几个测试的方法,你看我们提供了一个J2CatchControl,

那么这是一些测试方法,我们把它复制过来作为我们测试方法来用,然后我们在这儿重点就是来解释一下,假设我们现在是这么使用的注解,最终它生成的key是一个什么样的效果,

然后我们在这儿提供了这么几个方法,然后我把它直接复制,这些方法我们可以直接作为测试方法来用一下,并且它都没有进行什么,都没有进行数据库操作,

这样的话我们测试起来比较方便,把它放大一点,咱们来看,这个地方的报错,来看一下为什么报错,这个map没有导入,

然后我们可以一个一个来看一下,比如说就拿这个来说,咱们这个方法名不用管它了,然后你看这个方法上面我们加了这么一个catch注解,

然后它的region是inx,key是user,parameters等于id,

然后我们这儿传过来的也是一个catch注解,

就是一个简单的字符串,

那这个时候呢,我们最终拼成的那个key呢,其实就是什么呢,就是这个user,加上我们真正传过来的这个id的值,

最终这个key呢,它就等于什么呢,就是原始的这个key,就是user,然后再加上我们具体这个值,id的值,比如说这个id的值是123,

那么最终呢,它拼成的就是这么一个值,

然后再来看下一个,下一个呢,你看这个,这个就比较特殊了,

你看这个region,

它的region还是2x,key呢是user,而这个parameters呢变成了0.name,注意,这个地方必须写0嘛,是必须要写0的,

哎,那上面你这个为什么没有写0啊,就是因为我们这个地方传过来的这个参数,它是一个普通的字符串,而现在这个呢,它是不是一个对象,它是一个map对象,哎,它是一个map对象,这就表示什么呢,我们这个时候要拼成的这个key啊,

哎,它这个要求这个map里边必须得有一个name,

这个name这么一个字段,

啊,所以它最终拼成的呢,就是我们这个key呢,就等于什么呢,就等于原始的这个key,我是不是写的user,对吧,然后呢,再加上一个冒号,再加上这个name的值,比如说它这个name传过来的是小明,啊,那么最终呢,这个key就是这个值,

哎,这就要求,再来强调一遍,要求什么呢,我们传过来的这个map里边必须有一个字段,叫做name,哎,而这个0其实代表的是什么呢,代表的就是第一个参数,

因为我们当前啊,当前这个方法可能不止一个参数,对吧,我可能有多个参数,哎,那这个时候呢,我这个0代表的就是第一个参数,哎,代表的就是第一个参数,那0.name是不是就是第一个参数里边的name,哎,这儿呢,我们是使用了一个map,实际上我们使用实体类也可以,都是一回事,比如说我们实体类有很多,像我们这个address book,对吧,哎,address book里边如果有name,它也可以把name拿出来,然后最终拼成这么一个串,好,

而上面这个呢,因为它是一个简单字符串,对吧,所以就不用写了,好,这个0代表的就是第一个参数,好,然后接下来呢,我们来看下一个,这个的话呢,哎,又是加了cache注解,对吧,radar等于rx,key等于user,parameters呢,等于也是0.name,好,这个呢,其实跟刚才那个效果是一样的,啊,只不过就是什么呢,它这个加的是这个注解,什么request body,对吧,这就说明我们前端传,调这个方法的时候是不是应该,哎,传的是json格式的数据,

这个呢,就是普通的表单提交,好,那么最终呢,都是取这个map里边的name字段,好,然后再往下呢,你看这个,哎,这个又也比较特殊,有region,有key,是不是没有parameters,没有parameters呢,那这样的话,它最终拼成的那个key就是什么呢,那个key是不是就是我们原始的这个users,然后后边呢,就没有,好,所以说呢,相当于这个parameters呢,没有的话呢,那相当于这个呢,就是一个原始的一份数据,

可能各个用户呢,用的都是一份原始的数据,好,所以说它这个key的话呢,就是使用这个,好,然后再往下呢,哎,这个就是catch evict,这是不是要清理,对吧,这是要清理,清理的话呢,它清理哪个缓存呢,你看我们这是不是有catch,然后呢,region是不是rx,这是user,然后这是id,这个又跟原先的一样了,所以这个呢,最终拼完这个key之后啊,这个key就等于什么呢,就等于user,这个id的值假设还是123,

这个呢,这个key的话,因为没有写parameter,对吧,所以那个key呢,最终还是等于我们原始的这个users,好,这个呢,我们就通过咱们这几个例子来看一下,对吧,来看一下,所以你可以发现啊,这个key的话呢,既可以使用我们原始的这个,也可以加上parameter动态的把后边这个串,把这个参数值给它拼进去,好,这就是根据我们实际的需要了,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

那么这个菜单数据的话呢,

可能所有的用户用的是同一份菜单,

对吧,

假设用的是同一份菜单,

那这个时候呢,

就没有必要每一个用户对应的都缓存一份菜单数据,

相当于它就是,

我们系统当中有这么一份就可以了,

那这个时候呢,

我这个key就是,

大家都使用这个,

而对于我们这种情况呢

那是不是就是每个用户可能有自己的一份缓存数据

比如说我缓存的是我这个address book

我自己每个用户所对应的这个什么的地址部信息

对吧

那这个时候它的ID都是唯一的

那么这个时候呢

它相当于就是某个用户特有的自己的一份缓存数据

所以说呢

我们在这儿是通过parameters来进行区分

好

这是关于我们把讲义上

把咱们这几个测试方法把它考过来

然后呢

主要就是让大家熟悉一下我们这个注解

对吧

它到底怎么使用

以及它这样用完之后

最终生成的那个key

它的规则

对吧

它到底是什么

怎么用法

好

像我们这种写法的话呢

最终呢

它其实就反映到哪去了呢

其实就是我们调用这个工具类

对吧

调用我们这个generator这个工具类

然后继续再往一步一步往下调

最终呢

去分析我们

传进来的这个参数名

以及这个参数值

然后呢

我传过来的是内幕字段

它就会取map里边的内幕字段的值

好

这是关于我们这块

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频是关于 Java 项目中使用 `j2cache` 缓存框架的实战教学。讲师通过 IntelliJ IDEA 开发环境，演示了如何在 Spring Boot 项目中，通过自定义注解处理器（`@Cache`）来实现缓存的读取、写入和清除功能。视频重点讲解了 `@Cache` 注解的使用方式，包括如何通过 `@Cache` 注解指定缓存区域（region）和键（key），以及如何通过 `@CacheEvict` 注解实现缓存的清除。讲师通过在 `J2cacheController` 中编写多个示例方法，展示了不同参数（如 `@PathVariable`, `@RequestBody`, `@RequestParam`）如何影响缓存键的生成，并演示了缓存失效的逻辑。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开头，讲师展示项目结构，定位到“第3章 用户服务开发”下的“6. 声明式缓存”部分。
*   **00:05 - 00:15**: 讲师介绍本节内容，即“原生 j2cache 问题分析”和“声明式缓存代码实现”，并展示 `J2cacheController` 中的 `getCacheData` 方法，用于演示从缓存中获取数据。
*   **00:15 - 00:30**: 讲师演示如何通过 `@Cache` 注解指定缓存区域和键，展示 `@Cache(region = "rx", key = "user", params = "id")` 的用法。
*   **00:30 - 00:45**: 讲师编写 `evict` 方法，演示如何通过 `@CacheEvict` 注解清除指定缓存。
*   **00:45 - 01:00**: 讲师编写 `evictAll` 方法，演示如何清除整个缓存区域。
*   **01:00 - 01:15**: 讲师演示如何通过 `@RequestBody` 注解接收 JSON 数据，并将其作为缓存键的一部分。
*   **01:15 - 01:30**: 讲师演示如何通过 `@RequestParam` 注解接收查询参数，并将其作为缓存键的一部分。
*   **01:30 - 01:45**: 讲师演示如何通过 `@PathVariable` 注解接收路径参数，并将其作为缓存键的一部分。
*   **01:45 - 02:00**: 讲师总结本节内容，强调 `@Cache` 注解的灵活性和 `@CacheEvict` 注解的实用性。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

*   **左侧大纲**：清晰地列出了课程结构，包括“第3章 用户服务开发”、“6. 声明式缓存”、“6.1 原生j2cache问题分析”、“6.2 声明式缓存代码实现”等。
*   **视频标题**：`j2cache 声明式缓存`。

#### 代码关键内容

*   **`J2cacheController.java` 中的 `getCacheData` 方法**：
    ```java
    @GetMapping("/getCacheData/{id}")
    @Cache(region = "rx", key = "user", params = "id")
    public List<String> getCacheData(@PathVariable(name = "id") String id) {
        // 没有获取到缓存数据，需要从数据库中查询数据
        List<String> data = new ArrayList<>();
        data.add("beijing");
        data.add("nanjing");
        data.add("shanghai");
        System.out.println("查询数据库");
        return data;
    }
    ```

*   **`J2cacheController.java` 中的 `evict` 方法**：
    ```java
    @CacheEvict(@Cache(region = "rx", key = "user", params = "id"))
    @GetMapping("/evict/{id}")
    public String evict(@PathVariable(name = "id") String id) {
        System.out.println("删除数据库");
        return "evict success";
    }
    ```

*   **`J2cacheController.java` 中的 `evictAll` 方法**：
    ```java
    @CacheEvict(@Cache(region = "rx", key = "users"))
    @GetMapping("/evict")
    public String evictAll() {
        System.out.println("删除数据库");
        return "evict success";
    }
    ```

*   **`J2cacheController.java` 中的 `getCacheDataBody` 方法**：
    ```java
    @GetMapping("/getCacheDataBody")
    @Cache(region = "rx", key = "user", params = "0.name")
    public List<Map> getCacheDataBody(@RequestBody Map body) {
        // 没有获取到缓存数据，需要从数据库中查询数据
        List<Map> data = new ArrayList<>();
        data.add(body);
        System.out.println("查询数据库");
        return data;
    }
    ```

*   **`J2cacheController.java` 中的 `getCacheDataParams` 方法**：
    ```java
    @GetMapping("/getCacheDataParams")
    @Cache(region = "rx", key = "user", params = "0.name")
    public List<Map> getCacheDataParams(@RequestParam Map params) {
        // 没有获取到缓存数据，需要从数据库中查询数据
        List<Map> data = new ArrayList<>();
        data.add(params);
        System.out.println("查询数据库");
        return data;
    }
    ```

*   **`J2cacheController.java` 中的 `getAllData` 方法**：
    ```java
    @GetMapping("/getAllData")
    @Cache(region = "rx", key = "users")
    public List<String> getAllData() {
        // 没有获取到缓存数据，需要从数据库中查询数据
        List<String> data = new ArrayList<>();
        data.add("beijing");
        return data;
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：缓存读取演示**
    *   **描述**：讲师在 `J2cacheController` 中编写了 `getCacheData` 方法，该方法通过 `@Cache` 注解指定了缓存区域为 `"rx"`，键为 `"user"`，参数为路径变量 `id`。当访问 `/getCacheData/123` 时，系统会先尝试从缓存中获取数据，如果缓存中没有，则会打印“查询数据库”并返回模拟数据。
    *   **技术点**：演示了 `@Cache` 注解的使用，以及缓存的读取逻辑。

*   **场景二：缓存清除演示**
    *   **描述**：讲师编写了 `evict` 和 `evictAll` 方法，分别用于清除指定缓存和整个缓存区域。`evict` 方法通过 `@CacheEvict` 注解指定清除的缓存键，`evictAll` 方法则清除整个缓存区域。
    *   **技术点**：演示了 `@CacheEvict` 注解的使用，以及缓存的清除逻辑。

*   **场景三：不同参数类型缓存键生成演示**
    *   **描述**：讲师编写了 `getCacheDataBody`、`getCacheDataParams` 和 `getAllData` 方法，分别通过 `@RequestBody`、`@RequestParam` 和 `@PathVariable` 注解接收不同的参数，并将这些参数作为缓存键的一部分。
    *   **技术点**：演示了如何通过不同的注解来生成不同的缓存键，以及缓存的灵活性。

*   **场景四：缓存失效逻辑演示**
    *   **描述**：讲师在 `evict` 方法中添加了 `System.out.println("删除数据库")`，并在方法中返回 `"evict success"`。当调用该方法时，系统会打印“删除数据库”，并返回成功信息。
    *   **技术点**：演示了缓存失效的逻辑，以及如何通过 `@CacheEvict` 注解来实现缓存的清除。

---

以上是根据视频画面进行的结构化分析，希望能帮助您更好地理解视频内容。
