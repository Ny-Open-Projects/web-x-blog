# 37-智能调度服务（实现过程_订单分类_6） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那么刚才呢咱们是编写完成了这个receiver full address

对吧

这个呢就是获取我们这个完整的收件人地址信息

当然了我们这个地方呢

获取之后呢还是需要来判断一下

看看它是否为空对吧

如果是空的话呢

后边这个代码就没法执行了

那么我们就应该往外抛一长了

所以我们在这儿呢处理完之后呢

咱们需要来stream utils来处理一下

点ase

如果ase black

如果是空对吧

然后呢我们把这个address放进去

那这个时候啊

如果地址是空的话

那后边就没有必要再处理了

是不是直接往外抛一长就可以了

包括我们后边在做处理的时候呢

有好多地方呢

那么都需要各种教验各种判断

那么出现异常呢

咱们是不是都需要往外抛

所以说我们在这个地方呢

既然很多地方都需要抛异常

那么我们干脆就封装一个方法出来

封装一个方法出来

然后直接

只要需要抛异常的地方呢

咱们都调这个方法

这就是进行一个代码的一个抽取

那么我们在这儿呢

还是来个private

然后呢void

咱们就叫什么呢

exception

happened

发生对吧

发生

然后呢这个异常信息呢

你给我传进来就可以了

message

然后呢我们在这儿呢

来进行一个抛出

但是抛出的时候呢

最好也try一下

然后呢try catch

这简单封装一下就可以了

这个呢就是抛出异常

抛出异常

咱们在这儿呢直接throw

new一个exception就可以了

exception

然后呢把这个message呢放过来

ok

然后如果是进catch的话呢

直接再打印一下就可以

print the trace

然后这是exception

exception

happened

封装好了之后呢

这个就是一个

我们在这个地方呢

就可以直接啊

如果说它为空的话对吧

是空的话呢

那我们就可以直接调这个exception

happened的这个方法

然后把message传过去对吧

message传过去

这个message呢就是什么呢

这个收件人地址不能为空

收件人地址不能为空

好

这样咱们往外抛一抛一场的话

后边是不是就不执行了

ok

如果说不抛一场的话呢

那程序继续往下走对吧

那接下来呢

我们是不是就需要来调用我们这个百度地图工具类

根据什么呢

根据我们这个地址来获取对应的静伪度坐标

这个就比较简单了

咱们这个地方呢有一个工具类

叫做antcoordinate这个job

当然也可以使用我们自己在课上

前面咱们是不是也封装了一个百度地图工具类

哎都是类似的

都可以用

这个的话呢是在哪呢

这个是在我们

这个comment pdcomment

哎

在这里边给我们提供的

好

然后呢我们直接调用它的一个方法

嗯

来看一下叫做get coordinate

这个方法

然后呢你看我们是不是传进来address

好

传进来address

ok

然后呢它就会给我们返回一个什么呢

呃地址

咱们就叫location吧

好

location

那而这个location的话呢

它对应的是什么呢

对应的就是我们这个静伪度坐标

好

咱们在这呢可以

快速的来测一下

呃用不了起环境了

我们直接写根本方法来简单测一下就可以了

好

测试一下它这个方法

然后呢这个address的话呢

我们可以来写一下

那么比如说我就写咱们刚才举的这个例子

好

这是北京市昌平区建材城西路

对吧

金燕龙办公楼

好

这个地址

然后呢我们在这呢来输出一下这个location

它应该是一个静伪度坐标值

好

好

好

好

,然后呢来执行一下

稍等一下我们看一下这个控制台的输出

好

你看它其实已经给我们输出了

对吧

这就是我们这个静伪度

呃

然后呢我们刚才也提到啊

在这边的时候呢

刚才我们也提到

呃

如果说我们这个

append

咱们在这是不是在拼接我们这个完整的地址

对吧

假设它是重复了

也就是说人家这个详细的地址里边呢

已经包含了什么省市区

对吧

哎

那这个时候呢,有没有问题,那比如说我这个北京市唱名区,我再来复制一遍,那这就假设什么呢,前面这个北京市唱名区呢,是通过我们前面这个append是不是追加进去的,然后后边这一段呢,这就相当于是我们真正的那个地址那个字段,对吧,所对应的值,那这样的话呢,它是不是重复了两遍,北京市唱名区,这边又来个北京市唱名区,好,那这个有没有问题呢,咱们可以来再来测一下。

好,其实这个呢,是没有问题的,因为这个百度地图呢,它会给我们去除,也就是说,只要你留下的这个地址是一个真实的地址,对吧,即使你这个省市区这块写重复了,最终它也能够去正常解析出来,所以说这块呢,大家不用担心,好,这是我们简单验证一下就可以啊。

好,那么到这儿的话呢,咱们是不是就已经啊,把我们这个什么呢,把我们这个坐标值给获取到了。

那么我们可以在这儿来记录一下日日啊,log.info,对吧,log.info,然后呢,这是根据什么,根据这个地址获取对应的坐标值。

那么什么地址呢,我们可以在这儿呢,来写一下。

然后对应的这个坐标值呢,我们也可以写一下,第一个参数对应的是不是地址,地址的话就是address,是吧,然后第二个呢,是不是就是我们这个location,好。

在这儿简单记录一下就可以啊,方便我们后期再进行调试,对吧,后期调试。

好,那么这一块呢,这是我们根据百度地图工具类,对吧,然后获取对应的坐标值,我们就先写到这儿。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段展示了一个 Java 项目中订单派送服务的核心逻辑。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何根据订单的收件人地址，调用百度地图 API 获取经纬度坐标，并最终返回一个网点 ID。核心代码位于 `TaskOrderClassifyServiceImpl.java` 文件中，主要包含 `getEndAgencyId` 方法。讲师重点讲解了如何处理空地址的异常情况，并演示了如何通过 `EntCoordSyncJob` 工具类调用百度地图服务。整个过程体现了典型的后端服务开发流程，包括业务逻辑、异常处理和第三方服务集成。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 展示 `TaskOrderClassifyServiceImpl.java` 文件的代码结构，定位到 `getEndAgencyId` 方法。
*   **00:00:05 - 00:00:15**: 讲师将光标移动到 `String address = receiverFullAddress(order);` 这一行，解释其作用是获取收件人的完整地址。
*   **00:00:15 - 00:00:30**: 讲师将光标移动到 `if (StringUtils.isBlank(address))` 这一行，讲解空地址的判断逻辑。
*   **00:00:30 - 00:00:45**: 讲师将光标移动到 `exceptionHappend(msg);` 这一行，演示如何抛出异常。
*   **00:00:45 - 00:01:00**: 讲师将光标移动到 `String location = EntCoordSyncJob.getCoordinate(address);` 这一行，演示如何调用百度地图工具获取坐标。
*   **00:01:00 - 00:01:15**: 讲师将光标移动到 `Log.info("根据地址[{}]对应的坐标值[{}]", address, location);` 这一行，演示如何记录日志。
*   **00:01:15 - 00:01:30**: 讲师将光标移动到 `return null;` 这一行，讲解方法的返回值。
*   **00:01:30 - 00:01:45**: 讲师将光标移动到 `public static void main(String[] args)` 方法，演示如何在测试环境中调用 `getCoordinate` 方法。
*   **00:01:45 - 00:02:00**: 讲师将光标移动到 `String address = "北京市昌平区建材城西路金燕龙办公楼";` 这一行，演示如何传入一个具体的地址。
*   **00:02:00 - 00:02:15**: 讲师将光标移动到 `String location = EntCoordSyncJob.getCoordinate(address);` 这一行，演示如何调用百度地图工具获取坐标。
*   **00:02:15 - 00:02:30**: 讲师将光标移动到 `System.out.println(location);` 这一行，演示如何打印坐标值。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段**:
    *   **`getEndAgencyId` 方法**:
        ```java
        private String getEndAgencyId(Order order) {
            // 根据当前订单获取收件人地址详细信息，包含省市区，例如：北京市昌平区建材城西路金燕龙办公楼
            String address = receiverFullAddress(order);
            if (StringUtils.isBlank(address)) {
                exceptionHappend(msg); // 抛出异常
            }
            // 调用百度地图工具，根据地址获取对应的经纬度坐标
            String location = EntCoordSyncJob.getCoordinate(address);
            // 根据经纬度坐标获取对应的区县检查通过百度地图获取的区域是否和下单时选择的区域一致
            // 查询当前区县下的所有网点
            // 计算当前区域下所有网点距离收件人地址最近的网点
            return null;
        }
        ```
    *   **`receiverFullAddress` 方法**:
        ```java
        private String receiverFullAddress(Order order) {
            Long provinceId = Long.valueOf(order.getReceiverProvinceId()); // 省份ID
            Long cityId = Long.valueOf(order.getReceiverCityId()); // 城市ID
            // ... 其他逻辑
        }
        ```
    *   **`exceptionHappend` 方法**:
        ```java
        private void exceptionHappend(String msg) {
            try {
                throw new RuntimeException(msg);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        ```
    *   **`main` 方法中的测试代码**:
        ```java
        public static void main(String[] args) {
            String address = "北京市昌平区建材城西路金燕龙办公楼";
            String location = EntCoordSyncJob.getCoordinate(address);
            System.out.println(location);
        }
        ```

*   **关键工具类**:
    *   `EntCoordSyncJob`: 一个工具类，用于调用百度地图 API 获取经纬度坐标。
    *   `StringUtils`: Apache Commons Lang 库中的工具类，用于字符串操作。

---

### 4) 关键场景与演示描述

*   **场景一：异常处理演示**
    *   讲师在 `getEndAgencyId` 方法中，通过 `StringUtils.isBlank(address)` 判断地址是否为空。
    *   如果地址为空，调用 `exceptionHappend(msg)` 方法抛出异常，并在控制台打印异常信息。
    *   这个场景演示了如何在代码中处理异常情况，确保程序的健壮性。

*   **场景二：百度地图坐标获取演示**
    *   讲师在 `getEndAgencyId` 方法中，调用 `EntCoordSyncJob.getCoordinate(address)` 方法获取经纬度坐标。
    *   讲师在 `main` 方法中，传入一个具体的地址 "北京市昌平区建材城西路金燕龙办公楼"，并调用 `getCoordinate` 方法获取坐标。
    *   讲师在控制台打印出获取到的坐标值，演示了如何通过百度地图 API 获取地理坐标。

*   **场景三：代码结构与注释演示**
    *   讲师在 `getEndAgencyId` 方法中，通过注释解释了每个步骤的作用，包括获取地址、检查地址、获取坐标、查询网点等。
    *   讲师在 `main` 方法中，通过注释解释了代码的作用，包括传入地址、获取坐标、打印坐标等。
    *   这个场景演示了如何通过注释来提高代码的可读性和可维护性。

*   **场景四：IDEA 开发环境演示**
    *   讲师在 IntelliJ IDEA 开发环境中，通过光标移动和代码高亮，演示了如何查看和编辑代码。
    *   讲师在 IDEA 中，通过 `Ctrl + 点击` 或 `Alt + Enter` 等快捷键，查看方法的定义和调用。
    *   这个场景演示了如何使用现代 IDE 进行高效的开发工作。
