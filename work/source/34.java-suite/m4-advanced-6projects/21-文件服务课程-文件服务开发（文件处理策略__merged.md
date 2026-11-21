# 21-文件服务课程-文件服务开发（文件处理策略_ — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来呢,咱们继续来编写我们这个local service impr

刚才呢,我们是把这个upload file,也就是文件上传这个方法呢,已经写了一部分了

那么主要做的是什么呢

首先呢,我们是不是需要来获得这个properties对象

而这个properties这个对象呢,是通过我们这个file properties来get local是不是来获得

当然需要注意的是什么呢

咱们需要来调用一下这个方法

否则的话,我们这个properties是不是并没有给它复职

所以说呢,我们这个地方呢,需要先来调用一下它

那这样的话呢,我们properties是不是就有值了

具体呢,就是通过get local方法,把它是不是给我们返回

然后呢,拿到它之后呢,我们就可以来get它这里边的东西,对吧

endpoint, bucket name,还有ui, prefix

好,接下来呢,就是什么呢

为我们这个上传上来的这个文件呢,产生一个新的文件名

为了防止重复呢,那么我们可以使用uid来给它产生一个随机的文件名

然后接下来就是什么呢

接下来我们需要把这个日期的目录啊

就是年月这两层目录,是不是给它这个先动态获取一下

因为一会儿呢,需要把它创建出来,对吧

就是生成这种啊,这种年月,这种目录

然后接下来呢,我们是不是还要构造一下什么呢

我们这个文件存储的这个绝对路径,对吧

绝对路径其实就是什么呢

我们的endpoint,其实就是前面这段

然后加上什么呢,bucket name

bucket name呢,其实就是这段

然后再加上我们这个相对路径

日期目录相对路径,就类似于这么一段

好,然后呢,我们通过pass这个get的方法呢

它就可以把我们这三段呢

通过相应的目录分割符给它分割开

那么为什么叫相应的目录分割符呢

因为就是不同的操作系统呢

它这个目录分割符不一样,对吧

这个前面咱们也都已经强调过了

所以说呢,我们把这三部分拼到一块

然后呢,中间用相应的目录分割符

然后呢,最终呢,就得到了

如果是类似于这样的这么一个路径

例如,对吧

例如,就是这么一个路径

好,这段就拿到了

然后拿到这段之后呢

我们接下来呢,就可以怎么做呢

来构造一下我们这个目录的输出文件了

因为呢,一会儿呢,我们就需要

把我们上传上来的这个文件

multiply the file,对吧

把它读过来,并且呢

把它保存在哪呢

保存在我们这个目录下边

然后用哪个文件

我们就得到这个目录分割符

文件名呢

文件名咱们刚才是不是已经给它这个生成好了

就是这个filename

所以说呢,这个呢,我们构造的是什么呢

是我们这个目标的这个输出文件,对吧

输出文件

最终呢,就是把这个文件输出在这个位置

好,然后呢

这个输出文件呢

我们就需要来构造一下

这个地方呢,应该是如何构造呢

咱们是不是在这来一个file对象

注意,这个file的话不要弄错了

应该是我们java.io.file,对吧

好,我们就需要来构造一下这个地方呢

好,这个呢就是我们的autofile

输出的文件吧

等于什么呢

new一个java.io.file

然后呢,这个路径咱们是不是需要给它来拼接一下

好,那么这个路径拼接的话呢

我们希望给它拼成一个什么样的呀

是不是应该就是前面这一段

然后再加上我们这个随机的产生的这个filename

假设啊,假设叫xxx.doc,对吧

好,那么

是不是应该把这个路径给它放到这里面来

好,所以这块呢我们是不是还需要来拼一下

而前面这段这个absolute

是不是相当于就已经有了前面这一段了

那么我们再把中间这最后这一段

是不是给它拼接上就可以了

所以这个拼接的话

这种路径的拼接呢

我们还是使用pass

加s啊,注意

还是这个java.io.file

这个包下边给我们提供的这个pass

点什么呢

get,对吧

get的方法

然后呢,第一个参数是什么呢

第一个参数就是我们前面这一堆

然后第二个参数呢

就是我们这个filename,对吧

filename

然后不要忘了给它toString一下啊

转成这个字符串

好

那这样的话呢

我们就把这个file

outfile,对吧

这个目标的这个输出文件呢

就已经搞定了

然后接下来就是什么呢

接下来我们是不是就是

从我们传上来的这个文件

也就是multiplyfile这个文件来读

然后呢

把这个字节数据呢给它写出来呢

然后呢把这个字节数据呢给它写出来呢

写到我们这个目标的输出文件,对吧

就是outfile

就是从那边读,然后呢

像这个文件写

大概就是这么一个过程

但这个细节问题呢

我们可以通过我们这个工具类呢

来进行一个封装就可以

咱们呢

在这个commonIO里边呢

给我们提供了这么一个fileutils,对吧

fileutils

大家应该都用过

fileutils.什么呢

它这里边是不是有一个方法叫做什么呢

write

write

什么呢

write

write

write

array

to file

你看

这字面翻译过来是不是就是写字节

这个数组

到文件,对吧,到文件

那么

我们呢就可以直接啊

来调用这个方法

然后注意第一个参数是什么呢,第一个参数是不是应该就是我们

目标文件,对吧

目标文件是不是就是咱们这个outfile

然后第二个呢就是我们的字节数组

字节数组从那来读呢,是不是就是从我们传上来的这个multi

pdf来读

所以说呢我们直接通过它点什么呢

getbytes

就可以了

把它的这个字节数组

读取到

当然了这个地方的是因为它这个有异常对吧

异常的话呢

咱们不用在这儿来处理啊

不用在service里面来处理,直接往外抛就可以

直接往外抛就可以

那么咱们呢可以在这儿来

source

exception

往外抛异常

这个地方它为什么报错呢?

就是因为跟我们

这边呢它

这应该是找到它的

附类对吧

附类里边

这个地方是不是也需要往外抛

这样的话呢前后就统一了

这边是不是没有问题

所以我们这个地方的不用自己try catch

直接往外抛一下就可以

这个呢其实就是

我们向这个目标文件写入数据对吧

向我们这个目标文件写入

写入数据

好

那么到这儿的话呢咱们这个文件呢其实就已经写好了

就是从我们上传上来这个文件对吧

从这儿来读把这个字节数据读过来

然后呢向这个目标文件去写

好

那么这个呢就已经写完了

写完之后呢再往下我们要做的处理是什么呢

要再做的处理其实就是来封装什么呢

封装我们

这个因为我们这个保存完了对吧这个上传完了上传完之后呢需要补充这个文件的数据

这个上传完了上传完了之后呢需要补充这个文件的数据

把这个上传的文件信息啊把它保存到数据库里面去

而我们已经上传完了之后呢

就有一些什么呢

有一些这个

文件的属性能够确定下来了

比如说什么呢

比如我们这个

文件的这个URL地址

其实应该就能确定下来了

就是这个URL

对吧

然后还有什么呢

还有就是我们这个文件名

File Name

注意这个File Name啊

咱们来看一下

File Name在哪儿呢

File Name在哪儿呢

这里边比较多啊

这里边比较多啊

这个File Name

这个File Name指的就是我们

动态产生的那个UID

随机的

这是唯一的那个文件名

原始文件名呢咱们是

也没有扔啊

也是给它保留下来

只不过它对应的是什么呢

对应的是这个叫做Submitted

File Name

这个是原始文件名

最终的也是需要保存到数据库的

所以说呢我们

还需要

在文件上传完之后呢

还需要来设置我们文件的这个什么呢

唯一的文件名对吧

还有刚才提到的这URL

还有就是什么呢

还有就是它保存的绝对的磁盘路径

绝对的磁盘路径

比如说

类似于这样的

需要把这个路径也给它保存起来

所以说呢下面呢

我们这个文件上传

完成后

还需要来干什么呢

设置我们这个File对象

File对象的

这个

属性

哪些属性呢

刚才我们提到了

主要有URL对吧

然后还有什么呢

这个File Name对吧

File Name

然后还有一个是

这个绝对路径对吧

Relative Path

这个就是绝对的这个磁盘路径

需要把这个

属性来设置一下

设置一下

用于什么呢

用于这个保存到数据库

但是我们上传完了之后呢

还需要把这些

属性来设置一下

然后呢

我们就把这个

这个文件呢

这个文件呢

我们就把这个文件呢

就把这个文件呢

在这个文件中呢

需要保存到数据库里面去

那么关于这个属性设置呢

我们一会再来说

那么

到这儿的话呢

咱们其实这个文件呢

就已经写到我们这个本地磁盘

相当于就已经保存好了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段展示了一个 Java 项目中文件上传功能的实现过程。核心内容是 `LocalServiceImpl` 类中 `uploadFile` 方法的编写。该方法负责接收一个文件和一个 `MultipartFile` 对象，通过生成唯一的文件名、构建目标存储路径、创建文件对象，并最终将文件内容写入磁盘。视频中还展示了 `delete` 方法的定义，并在最后切换到 `FileDO` 实体类，展示了其用于存储文件元数据的字段定义。整个过程是在 IntelliJ IDEA 开发环境中进行的，代码风格和注释表明这是一个基于 Spring Boot 的项目，可能用于演示或教学目的。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:03**: 展示 `LocalServiceImpl` 类的 `uploadFile` 方法的初始结构，包括方法签名和 `buildClient()` 调用。
*   **00:03 - 00:06**: 代码光标移动到方法体内部，开始编写具体的逻辑。
*   **00:06 - 00:09**: 编写获取配置属性的代码，包括 `endpoint`、`bucketName` 和 `uriPrefix`。
*   **00:09 - 00:12**: 编写生成文件名的逻辑，使用 `UUID.randomUUID().toString()` 和文件扩展名。
*   **00:12 - 00:15**: 编写构建日期目录的代码，使用 `Paths.get(LocalDateTime.now()).format(...)`。
*   **00:15 - 00:18**: 编写构建完整文件路径的代码，使用 `Paths.get(endpoint, bucketName, relativePath).toString()`。
*   **00:18 - 00:21**: 创建目标文件对象 `java.io.File`。
*   **00:21 - 00:24**: 调用 `FileUtils.writeByteArrayToFile` 方法将文件内容写入磁盘。
*   **00:24 - 00:27**: 完成 `uploadFile` 方法，添加注释说明上传完成后需要设置 `FileDO` 对象的属性。
*   **00:27 - 00:30**: 展示 `delete` 方法的定义。
*   **00:30 - 00:33**: 切换到 `FileDO` 实体类，展示其字段定义，包括 `size`、`folderName`、`treePath` 和 `grade`。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **代码片段 1 (uploadFile 方法)**:
    ```java
    @Override
    public File uploadFile(File file, MultipartFile multipartFile) {
        buildClient();
        String endpoint = properties.getEndpoint();
        String bucketName = properties.getBucketName();
        String uriPrefix = properties.getUriPrefix();

        // 使用UUID为文件生成新文件名
        String fileName = UUID.randomUUID().toString() + StrPool.DOT + file.getExt();

        // 日期目录
        String relativePath = Paths.get(LocalDateTime.now()).format(DateTimeFormatter.ofPattern(DateUtils.DEFAULT_MONTH));

        // 上传文件存储的绝对目录
        String absolutePath = Paths.get(endpoint, bucketName, relativePath).toString();

        // 目标输出文件
        java.io.File outFile = new java.io.File(Paths.get(absolutePath, fileName).toString());

        // 向目标文件写入数据
        FileUtils.writeByteArrayToFile(outFile, multipartFile.getBytes());

        return null;
    }
    ```

*   **代码片段 2 (delete 方法)**:
    ```java
    @Override
    public void delete(FileDeleteDO fileDeleteDO) {
        // 代码未完整展示
    }
    ```

*   **代码片段 3 (FileDO 实体类)**:
    ```java
    @ApiModelProperty(value = "文件大小")
    @TableField("size")
    private Long size;

    @ApiModelProperty(value = "父文件夹名称")
    @Length(max = 255, message = "父文件夹名称长度不能超过255")
    @TableField("folder_name")
    private String folderName;

    @ApiModelProperty(value = "FastDFS组")
    @Length(max = 255, message = "FastDFS组长度不能超过255")
    @TableField("group_name")
    private String groupName;

    @ApiModelProperty(value = "父目录层级关系")
    @Length(max = 255, message = "父目录层级关系长度不能超过255")
    @TableField("tree_path")
    private String treePath;

    @ApiModelProperty(value = "层级等级")
    @TableField("grade")
    private Integer grade;
    ```

---

### 4) 关键场景与演示描述

*   **场景 1: 文件上传逻辑构建**
    *   **描述**: 开发者在 `LocalServiceImpl` 类中逐步构建 `uploadFile` 方法。首先调用 `buildClient()` 初始化客户端，然后从配置中读取存储服务的端点、存储桶名称和 URI 前缀。
    *   **关键动作**: 代码光标依次移动到 `endpoint`、`bucketName`、`uriPrefix`、`fileName`、`relativePath` 和 `absolutePath` 的定义处，展示了如何动态生成文件名和存储路径。

*   **场景 2: 文件写入磁盘**
    *   **描述**: 在确定了目标文件路径后，开发者创建了一个 `java.io.File` 对象，并使用 `FileUtils.writeByteArrayToFile` 方法将 `MultipartFile` 的字节内容写入磁盘。
    *   **关键动作**: 代码光标在 `FileUtils.writeByteArrayToFile` 方法的调用处停留，强调了这是文件实际写入的关键步骤。

*   **场景 3: 文件删除方法**
    *   **描述**: 在完成上传逻辑后，开发者展示了 `delete` 方法的定义，该方法接收一个 `FileDeleteDO` 对象作为参数，用于处理文件删除操作。
    *   **关键动作**: 代码光标在 `delete` 方法的定义处，暗示了后续可能需要实现删除逻辑。

*   **场景 4: 文件元数据实体类**
    *   **描述**: 视频最后切换到 `FileDO` 实体类，展示了用于存储文件元数据的字段，包括文件大小、父文件夹名称、FastDFS 组、父目录层级关系和层级等级。
    *   **关键动作**: 代码光标在 `FileDO` 类的字段定义处，强调了这些字段在数据库中存储文件信息的重要性。

---

**注意**: 视频中显示的 `FileUtils.writeByteArrayToFile` 方法调用，其参数是 `multipartFile.getBytes()`，这在实际开发中是可行的，但通常会更倾向于使用 `multipartFile.transferTo(File)` 或 `multipartFile.getInputStream()` 来避免内存溢出问题。视频中的代码逻辑是演示性的，可能为了简化而省略了最佳实践。
