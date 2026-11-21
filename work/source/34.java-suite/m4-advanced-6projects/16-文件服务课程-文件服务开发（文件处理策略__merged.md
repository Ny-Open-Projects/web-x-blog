# 16-文件服务课程-文件服务开发（文件处理策略_ — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那么接下来呢

继续来编写咱们这个抽象的文件策略处理类

刚才呢我们是把这个upload的方法呢

整体这个结构呢是已经编写出来了

对吧

已经编写出来了

然后还差最后一小点呢

就是什么呢

就是对我们这个file对象呢

来封装它相关的一些属性

而这些属性呢

最终呢都是需要保存到我们的数据库里面去的

好

封装的过程呢

咱们这个地方

是不是使用的是这种构建器这种模式

对吧

所以说我们就在中间来写就可以了

来一个点

什么呢

第一个就是isDelete

表示我们当前这个文件呢

是否被删除了

对吧

是否已经被删除

这个地方呢

我们刚刚上传的文件肯定是false

这个就表示没有被删除

这个设置的是什么呢

是文件是否被删除

好

然后呢

我们再来一个

比如说我来一个size

这个表示文件的大小

对吧

文件的大小呢

我们可以通过这个

这个multiply的file来获取

这是文件的大小

multiply.getsize

好

这个设置的是我们的文件大小

好

然后继续

还有什么呢

还有这个context type

对吧

就是文件的类型

文件的类型呢

我们同样也可以使用这个multiply.getcontent type来获得

这是我们这个文件类型

好

然后呢继续

还有什么能够设置呢

比如说我们这个文件它的这个datatype

这个datatype呢

其实是数据类型啊

这个叫做数据类型

数据类型

那么我们定义了这么几种啊

咱们来看一下这个datatype

进来

你看有什么呢

有这个dir

表示我们上传的这个是一个什么目录

对吧

然后呢

image呢

代表的它是一个图片

然后呢

还有什么视频的音频的文档啊

等等还有其他

这个呢叫做数据类型

其实用来区分我们上传的这个文件到底是一个什么类型的文件

对吧

到底是图片还是音频啊

所以这个呢叫做数据类型

而这个数据类型呢

我们如何来获取呢

咱们在这呢

其实是定义了这么一个叫做file datatype

util

看见没有

定义了这么一个工具类啊

这个工具类呢

就前面咱们已经导入进来了

就是在这个youtube里面对吧

然后在这个youtube里边呢

你看我们其实就是图片类型呢

我们其实就是图片类型呢

我们其实就是图片类型呢

我们其实就是图片类型呢

通过这个工具类的这个get datatype方法

然后呢你传进来一个mime类型

这个mime呢

其实就是对应的是我们的context type

然后呢在这里面来来这个进行这个判断对吧

来进行比对

最终呢来这个返回我们这个真正的datatype

它的类型是docker啦

还是video啊

对吧

还是dir啊

等等这些

那么这些呢

你看到的这些对应的就是我们的context type

也就是i

对吧

mime类型

所以说这个地方呢

具体这个文件它是什么类型

是不是应该跟我们这个context type有关系

那么我们直接调用这个静态方法呢

get datatype

你看它传进来的是不是就是mime

其实对应的就是我们的context type

而这个context type

刚才我们说是不是通过这种方式就可以获取

所以说呢

把这个context type传进来

传进来之后呢

然后呢

最终传给我们这个静态方法

对吧

工具类里面

这个静态方法

好

然后在这里面来进行比对

最终呢

给我们返回这么一种类型

好

其中的一种类型就可以了

好

这个呢

是我们的数据类型

对吧

然后接下来继续啊

注意这是一个链式调用

你看我这是整个一句话

整个一句话

好

然后呢

还有什么呢

咱们来找一下

有一个叫做submit

fail name

这个其实就是我们文件上传的这个原始文件名

上传的文件名

就是我们文件的原始文件名

原始文件名称

好

原始文件名称

这就比较简单了

是不是就是通过我们这个multiplefile.getoriginal

file name

好

这个是原始文件名称

然后接下来再有呢

就是我们这个文件的后缀啊

文件的后缀

好

叫做ext

对吧

ext

咱们可以来看一下

这是我们这个file里边的一个方法

对吧

对应的

当然也有一个数据啊

就是ext

咱们来找一下

这不是文件的后缀

对吧

文件名后缀

好

这个呢

最终呢

是需要保存到我们的这个ext

这个字段里面去的

好

那么这个后缀呢

我们如何来获取呢

那它肯定是跟我们这个原始文件名

是不是有关系

比如说我这个原始文件名叫做什么呢

叫做test.doc

对吧

那么它的后缀呢

很显然

就是从我们这个原始文件名里面

把最后这一点

是不是给它截出来的呢

但是我们不需要

不要这个点

直接把这个doc给截出来

如果它是一个什么呢

这个img的吧

或者是一个这个gopro.pt

好

那么最终

这是不是就是它的这个后缀

也就是说啊

我们这个后缀名呢

肯定是需要从这个原始文件名称里面

是不是去获取

也就是说需要从这个原始文件名称里面去获取

好

然后呢

咱们这个地方呢

其实是封装了这么一个

叫做filename

filename

utils

好

你看我们

其实有这么多的工具类啊

点

然后呢

还有一些属性呢

还是需要

来设置的

但是呢

就不能通过这种链式调用

这种方式来设置了

好

比如说什么呢

我要设置这个

设置我们这个文件的图标

图标

这个

你看在我们这个file里边呢

有一个属性呢

叫做icon

咱们来找一下

这里边属性比较多啊

不太好找

就是这个

你看这是文件的图标

那么用于云盘展示的

对吧

主要是给前端展示的

那么比如说我们当前这个文件呢

它是一个文件夹

对吧

那么我可能就要展示一个文件夹的类型

如果是一个图片呢

我可能展示的就是一个图片的图标

所以说呢

我们这个地方呢

需要来设置一下

这个icon

然后呢

这个是设置文件的图标

也就是我们在这呢

可以继续啊

调用这个file

然后呢

点set

什么呢

icon

好

这个图标

然后呢

我们呢

具体这个图标应该是什么样子的呢

是不是应该跟我们这个文件的后缀有关系

对吧

比如我这个后缀呢

是一个gopg的

对吧

那么我就知道了

它肯定是一个图片

对吧

那么如果是一个doc的

那我就知道它肯定是一个word文档

好

等等啊

也就是说我们可以通过这个文件的后缀

然后来确定它的图标

所以说呢

我们在这呢

就可以通过一个叫做icon type

这个是个什么呢

是我们导进来的一个

一个文件的图标

好

咱们来看一下

在我们这个直接点过来吧

直接点过来看

你看这是在我们pd file entity里边

我们当时导进来的

这个是图标对吧

很多很多图标

然后呢

这是对应的我们前端的一个

其实是一个样式对不对

现在那个样式

方便我们在页面进行展示图标

你比如说是这种dir的目录的对吧

然后呢

txt的

但是还有一些其他的我们是注视起来了

如果有其他的呢

我们也可以去看看

好

我们可以在这后边追加

你看这些都是图片啊

是bmp的是吧

然后groupg的png的gif的等等啊

非常多

好

那么对应的这些呢

都是我们前端的一些样式

用于这个前端展示的

好

在这呢

简单了解一下就可以

所以我们在这呢

就可以使直接使用这个icon type

点什么呢

get icon

然后呢

我们需要给它传进来一个什么呢

后缀对吧

这个后缀

咱们前面在这个file创建完成之后

是不是就已经设置好它的后缀了

所以我们在这呢

直接通过这个file.getextension

对吧

然后呢

再geticon

就可以获得这个图标了

OK

那么这是设置了这几个

这是设置文件的图标

然后还有几个

这个属性需要设置

咱们来看一下

呃

一个叫什么呢

嗯

咱们来找一下

这里面东西比较多

这个

一个叫的curate month

对吧

还有一个叫做curate week

还有一个叫做curate day

那么这三个属性呢

我们也来设置一下

这个curate month代表的是什么呢

表示我们上传的这个文件啊

它创建的这个

哎

创建时的这个年月

创建时的年月

呃

用于统计的

这个都是我们后边

在需要统计一些这个文件的数量

对吧

什么时候创建的

那么每天创建了多少

每个月创建了多少等等

用于数据统计

所以说呢

我们这个文件呢

在上传之后呢

需要把这个

哎

月份对吧

然后呢

以及这个周

还有日

对吧

年月日

那么它是这种形式的

把它一个一个保存进来

啊

这个是周

然后呢

这个是月啊

所以说呢

我们需要来设置这三个属性

分别是curate month

curate week

还有curate day

这三个

回到这边来

那么咱们来设置一下

在这儿啊

咱们统一就叫什么呢

设置我们这个文件创建这个时间吧

对吧

好

好

这个咱们就不要了

好

那么我们在这儿来设置一下

file.setcurate什么curate month吧

curate month

那么这个月份怎么获得呢

怎么获得呢

哎

首先我们需要知道当前的这个系统时间

对吧

所以说呢

我们获得当前系统时间

咱们就使用这个localdatetime

好

然后点什么呢

now

获得当前系统时间

好

然后呢

这个地方呢

这个时间

我是不是就知道了这个年月呀

所以我们在这儿呢

直接使用这个工具类啊

data utils

好

我们提供了这么一个工具类

然后呢

这里边有一个叫做format格式化对吧

把我们当前这个时间呢

给它来格式化成这种什么呢

as year month

就是年月这种形式

好

把我们这个日期传进去

当前系统时间传进去

好

好

你看把这个now是不是传进去了

这样呢

就设置了这个month了

然后呢

同理啊

我们还有一个file.set create week

好

同样的也是调用这个data utils

点什么呢

format as什么呢

week in

对吧

这个呢

格式化成我们这个什么呢

是什么类型呢

刚才大家已经看到了

应该是week那个是这个

应该是年周

对吧

年周

只不过y y y

这是四位表示年份

这个代表的是周

第几周

好

那我们再来看看这个

前面的这个file.set什么呢

create date

同样的还是通过date

youtube.什么呢

format as

data

好

然后呢

把当前时间传进去

那么到这儿的话呢

我们就已经都封装好了

大家来看啊

我们这一块呢

一共是不是封装了6个属性

然后呢

在这个地方

图标是不是又封装了一个

七个属性

然后再加上这三个

一共是封装了10个属性

但是仅仅是这10个属性呢

还是不够,

还是不够,

所以说呢,

我们还需要把这个file对象呢,

继续传到这个upload file里边,

在这个方法里边,

还需要去设置它其余的一些属性,

对吧,

其他的一些属性,

也就是那些属性呢,

只有在真正完成文件上传之后,

才能确定下来,

所以说需要在这个方法里边去实现,

去封装,

而这个方法呢,

咱们是在这儿是不是,

在我们当前这个抽象类里边呢,

是声明了这么一个抽象的方法,

那么具体呢,

我们一会儿还要去提供,

当前这个类的子类,

对吧,

在子类里边去实现这个upload file,

真正这个文件上传的那个具体的处理过程,

好,

那么到这儿的话呢,

咱们就把这个抽象类里边,

这个upload的方法呢,

整个都已经写完了,

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频是一个关于 Java 文件上传服务的实战开发教程，重点讲解了如何使用 `File.builder()` 构建一个 `File` 实体对象，并为其设置各种属性。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何处理上传文件的原始名称、文件类型、大小、MD5 值、图标、创建时间等信息，并将其封装到数据库实体中。整个过程体现了面向对象设计和策略模式的应用，旨在构建一个功能完整、可扩展的文件服务。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 开场，展示项目结构和 `FileServerApplication.java` 文件，介绍本节将讲解文件上传服务的实现。
*   **00:05 - 00:15**: 讲解 `File.builder()` 的使用，演示如何通过链式调用设置文件的基本属性，如是否删除、大小和内容类型。
*   **00:15 - 00:25**: 介绍 `FileDataTypeUtil` 工具类，演示如何根据 MIME 类型判断文件类型，并返回对应的 `DataType` 枚举值。
*   **00:25 - 00:35**: 讲解 `File` 实体类的属性，包括文件名、文件类型、父目录层级关系和层级等级。
*   **00:35 - 00:45**: 演示如何根据文件扩展名获取对应的图标，使用 `IconType` 枚举类。
*   **00:45 - 00:55**: 讲解如何设置文件的创建时间，使用 `LocalDateTime` 和 `Date` 类进行格式化。
*   **00:55 - 01:05**: 总结并回顾整个 `upload` 方法的实现，强调了文件信息的完整封装过程。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **核心代码：`File.builder()` 链式调用**
    ```java
    File file = File.builder()
        .isDelete(false) // 文件是否被删除
        .size(multipartFile.getSize()) // 文件大小
        .contextType(multipartFile.getContentType()) // 文件类型
        .build();
    ```

*   **文件类型判断工具类 `FileDataTypeUtil`**
    ```java
    public static DataType getDataType(String mime) {
        if (mime == null || "".equals(mime)) {
            return DataType.OTHER;
        }
        if (mime.contains("IMAGE")) {
            return DataType.IMAGE;
        } else if (mime.contains("TEXT")) {
            // ... 其他文本类型判断
        } else if (mime.startsWith("application/vnd.ms-excel")) {
            return DataType.EXCEL;
        } // ... 其他文件类型判断
    }
    ```

*   **`File` 实体类关键属性**
    ```java
    @ApiModelProperty(value = "md5值")
    @Length(max = 255, message = "md5值长度不能超过255")
    @TableField("file_md5")
    private String fileMd5;

    @ApiModelProperty(value = "文件类型")
    @Length(max = 255, message = "文件类型长度不能超过255")
    @TableField("context_type")
    private String contextType;

    @ApiModelProperty(value = "原始文件名")
    @Length(max = 255, message = "原始文件名长度不能超过255")
    @TableField("submitted_file_name")
    private String submittedFileName;

    @ApiModelProperty(value = "父目录层级关系")
    @Length(max = 255, message = "父目录层级关系长度不能超过255")
    @TableField("tree_path")
    private String treePath;

    @ApiModelProperty(value = "层级等级")
    @Length(max = 255, message = "层级等级长度不能超过255")
    @TableField("level")
    private Integer level;
    ```

*   **图标映射枚举 `IconType`**
    ```java
    MP3("mp3", "el-icon-microphone"),
    BMP("bmp", "el-icon-picture"),
    JPEG("jpeg", "el-icon-picture"),
    JPG("jpg", "el-icon-picture");
    ```

*   **创建时间设置**
    ```java
    LocalDateTime now = LocalDateTime.now();
    file.setCreateMonth(DateUtils.formatsYearMonthEn(now));
    file.setCreateWeek(DateUtils.formatsAsWeekEn(now));
    file.setCreateDate(DateUtils.formatsAsDayEn(now));
    ```

---

### 4) 关键场景与演示描述

*   **场景一：文件上传校验**
    讲师在 `upload` 方法中，首先获取上传文件的原始文件名，并通过 `contains(FILE_SPLIT)` 判断文件名是否包含后缀。如果未包含，则抛出 `BizException` 异常，提示“上传文件名称缺少后缀”。

*   **场景二：构建 `File` 对象**
    讲师使用 `File.builder()` 开始构建文件对象，并依次调用 `.isDelete(false)`、`.size(multipartFile.getSize())`、`.contextType(multipartFile.getContentType())` 等方法，为对象设置属性。

*   **场景三：文件类型判断**
    讲师切换到 `FileDataTypeUtil` 类，演示如何根据文件的 MIME 类型判断其具体类型，例如判断 `application/vnd.ms-excel` 为 Excel 文件。

*   **场景四：设置文件图标**
    讲师在 `File` 实体类中，通过 `IconType.getIcon().getExt().getIcon()` 获取文件对应的图标，并设置到 `file.setIcon(...)` 中。

*   **场景五：设置文件创建时间**
    讲师演示如何使用 `LocalDateTime.now()` 获取当前时间，并通过 `DateUtils` 工具类将其格式化为月、周、日等不同格式，分别设置到 `file.setCreateMonth(...)`、`file.setCreateWeek(...)` 和 `file.setCreateDate(...)` 中。

*   **场景六：异常处理**
    讲师在 `upload` 方法的 `catch` 块中，对可能出现的异常进行统一处理，记录日志并抛出 `BizException`，确保程序的健壮性。

---

以上是根据视频画面进行的结构化分析，希望能帮助您更好地理解本节内容。
