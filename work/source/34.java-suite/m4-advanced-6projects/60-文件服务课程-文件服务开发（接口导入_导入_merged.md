# 60-文件服务课程-文件服务开发（接口导入_导入 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来咱们继续来看我们文件服务的开发

这个小节我们要导入的是我们网盘服务的接口

前面咱们已经完成了文件服务中附件服务相关接口的开发

那么附件服务最终是将上传的文件信息保存到了我们这个附件表

也就是PD,Touchman的这张表中

那么我们这个小节要完成的是文件服务中的网盘服务功能

这个功能其实最终是将我们上传的文件信息

把它保存到我们PD File

也就是下面这一张表里面去

而整个这个网盘服务和附件服务其实是非常类似的

它只是多了一个什么呢,文件夹的概念

也就是说我们可以在这个网盘当中去创建文件夹

然后在文件夹当中去上传附件,去上传文件

所以整个这个过程跟我们前面这个附件服务是非常类似的

所以对于这一块的代码呢

咱们直接来导入就可以了

我们就不再去手敲了

那么我们对应的需要来创建新的一个Controller

叫做File Controller

咱们前面全都是在我们这个Attachment Controller

也就是在我们这个附件这个控制器里面来完成的

那么接下来我们要做的就是咱们这个File Controller

咱们来创建一个新的Controller

直接把这些代码导过来就可以了

因为功能都是类似的

所以对于这种非常类似的功能呢

咱们就不再去重复去开发了

这是File Controller

然后呢我们直接把这个代码呢拷过来就可以了

这里面呢也是提供的一些什么呢

文件的上传呢

还有下载呀

还有数据库的一些增伸改查操作

只不过呢它是针对我们这个文件表

对吧

文件表来进行的操作

也就是我们那个PD File那张表

好

当然了

这里边呢肯定有一些是报错的

因为它所依赖的一些Service

对吧

我们还都没有去创建啊

这是咱们这个文件服务

也就是我们的网盘服务

然后呢它也是继承了Base Controller

你看它这个地方呢需要使用到一个叫做File Service

对吧

还有一个叫做File REST Manager

这么两个接口

然后这里边提供的一些方法

你看这个呢是一个查询文件

对吧

如果这个参数人能够知道

他应该是根据ID是不是来查

这其实是一个纯数据库操作

然后这个是分页查询

然后呢这个是文件的上传对吧

文件的上传upload

而这个上传的过程啊

跟我们前面已经实现的附件上传呢

是非常类似的

好

只不过呢它是封装到了这个File Service

接口里边

然后这个呢Save Folder

你看这个是新增一个文件夹对吧

其实呢就是像我们这个表里边

也就是PD File这个表里边来查询的过程里面

其实呢就是像我们这个表里边也就是PD File这个表里边来查询的过程里面

这个表里边来查询的过程里面

来查入一个文件夹这么一条数据

然后呢这个是什么呢

修改文件文件夹的信息

比如说我改一个文件名对吧

然后呢这个是删除

文件的删除

然后这个是什么呢下载

打包下载

这是我们当前把这个File Controller呢

已经导进来了

它这里边呢肯定是报错的

所以接下来呢我们还需要继续来导入

接下来呢还有一个

就是导入了另外一个Controller

这个Controller呢是做

这个File Controller的

这个File Controller呢是做

这个数据统计的

比如说什么呢

你看这是文件统计的接口

比如说我们来统计一下我们整个这个云盘

它的数据的概览

它这里边呢是统计了各种维度的

全都是封装到了这个

叫做File Overview DTO

咱们呢可以来看一下

就这个叫做

File Overview DTO

这里边你看比如说所有文件的数量

所有文件大小

然后呢文件夹的数量

然后图片文件的数量

文档

嗯

文件的数量对吧

就是各种类型的文件

哎都有多少个

哎他是从这这么多的维度啊去统计

呃其实呢最终呢都是

呃都是去查询数据库对吧

因为我们数据库里面都保存着这些信息

所以它其实本质上是一个数据库的这个查询操作

好

所以接下来呢我们就把这个统计的

这个Controller先创建出来

好

把这个Controller创建出来

然后呢我们直接把代码拷过来就可以了

好

直接在这来覆盖一下

你看这里边对吧

这是文件统计的这么一个接口

好

但是它这呢也会去调用咱们的Service啊

来实现真正的统计

呃最终呢都是一些数据库的查询操作

好

然后接下来呢我们就需要来导入什么呢

导入咱们这个接口

呃首先导入的是这么一个叫做FileRestManager

哎

这是什么呢

文件公共代码管理类

它这里边呢给我们提供了这么一个分页的方法

哎

咱们这个地方啊

网盘服务这个分页查询呢

是封装到这个地方了

然后还有一个是什么呢

呃下载的方法

好

然后呢我们直接啊

把这个类呢拷过来

放在哪呢

呃

咱们创建这么一个新的包吧

跟我们的讲义保持一致

在这个File下边来创建这么一个包

叫做Manager

对吧

然后呢把咱们这个类呢

放在这里边

好

叫做FileRestManager

然后呢我们直接把这个代码拷过来就可以了

大概来读一下这个代码

呃

当然了

它这边肯定也是报错的

因为它要叫service对吧

FileService

呃所以说呢我们接下来呢

需要把这个FileService接口

创建出来

FileService接口

呃那么很显然应该是放在我们service这个包下边

所以我们来导入这个FileService

它呢是一个interface啊

一个接口

放在我们service这个包下边

来一个interface

对吧

FileService

然后呢把这个接口整个代码拷过来

这里边呢声明的方法也是比较多的啊

好

咱们来看一下

你看这边

呃这都是什么方法呢

咱们大概来过一下

一个是save folder

保存文件夹对吧

保存文件夹

然后呢download

这是文件下载

文件下载

然后还有什么呢

remove list

哎

这是不是移除

就是删除啊

然后还有什么呢

根据文件夹ID

是不是查询呢

哎查询

然后这个是上传的对吧

然后这个也是上传的

这么两个方法

然后呢

这个是做统计的对吧

FileOverview

哎

首页概览啊

因为它是个网盘服务啊

所以说呢

它要有一个整体的这么一个概念对吧

数据统计啊

对吧

数据统计啊

这些FindTop20对吧

哎

查询什么下载排行前20的文件等等

这些啊

都是一些统计的

这是咱们这个接口

然后接下来呢

就是导入咱们这个实现类对吧

叫做FileServiceIMPR实现类

对吧

对吧

呃来看一下

在这个下边

创建出来我们这个实现类

然后呢

我们直接把这个实现类呢

代码拷过来

这个代码量呢

也是比较多的

这对应的是我们网盘服务

这个Service实现

好

整个这个代码呢

还是非常多的

直接一直到这个地方

他就把我们这个接口里边所有的方法是不是都实现了

所有的方法都实现了

啊

然后呢

这个地方呢

你看他会报错

对吧

哎

就是因为我们这个baseMapper里面目前还没有这些方法

所以下一个呢

我们就需要把咱们Mapper里边缺少的这些方法了

给他导过来啊

这是实现类啊

在这里边呢

也会使用到我们这个FileBIZ

对吧

这个是我们前面在做复建的时候复建这个服务的时候呢

使用到的

那么这个地方呢

他也会用到

好

他现在就已经复用了

然后呢

接下来我们把最后这一点就是我们这个FileMapper对吧

FileMapper

然后呢

扩展出来这几个方法

FileMapper来看一下

应该是在DAO下边对吧

FileMapper这个地方

然后呢

把我们这几个方法扩展出来

你看现在他这边就已经不报错了啊

这是我们这个FileMapper

但是对应的呢

我们的这个circle语句呢

其实都已经导入过了啊

咱们的circle语句对应的是不是应该就是在我们

这个resources下边对吧

然后呢

应该是在ext

FileMapper这里边所对应的

你看我们这些统计的circle呢

其实都已经写完了

都已经写完了

大家可以来看一下

你看

这些统计的circle其实都已经写完了啊

所以说整个呢

我们这个代码呢

就都已经导入完了

导入完之后呢

咱们重新来启动一下就可以了

重新来启动一下

然后一会儿呢

我们可以来简单测试一下

我们导入的这些代码

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程是关于一个名为“pinda-authority”的Java项目中“文件服务”模块的开发讲解。讲师通过IDEA（IntelliJ IDEA）和Navicat Lite等工具，系统性地演示了文件上传、下载、统计以及分片合并等核心功能的实现。课程内容聚焦于Spring Boot框架下的Controller层、Service层和Mapper层的代码编写，以及数据库表结构的设计。讲师通过代码逐行讲解、接口调用演示和数据库操作展示，旨在帮助学习者掌握文件服务的完整开发流程。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取精确的时间戳，以下章节结构是根据画面内容和逻辑顺序推断的：

*   **5.9 导入网盘接口** (约 00:00:00 - 00:00:05)
    *   5.9.1 导入FileController
    *   5.9.2 导入StatisticsController
    *   5.9.3 导入FileRestManager
    *   5.9.4 导入FileService
    *   5.9.5 导入FileServiceImpl
    *   5.9.6 扩展FileMapper接口方法
*   **5.10 接口开发-分片上传** (约 00:00:05 - 00:00:10)
    *   讲解`FileController`中的`@PostMapping("/upload")`方法，用于处理文件上传。
*   **5.11 接口开发-分片合并** (约 00:00:10 - 00:00:15)
    *   讲解`FileRestManager`中的`download`方法，用于处理文件下载。
*   **5.9.2 StatisticsController** (约 00:00:15 - 00:00:20)
    *   讲解`StatisticsController`中的`overview`和`findAlByDataType`方法，用于统计文件数据。
*   **5.9.5 FileServiceImpl** (约 00:00:20 - 00:00:25)
    *   讲解`FileServiceImpl`中的`findSizeByDate`方法，用于按日期范围统计文件大小。
*   **5.9.6 FileMapper** (约 00:00:25 - 00:00:30)
    *   讲解`FileMapper.xml`中的SQL语句，用于查询文件数据。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   课程大纲：清晰地列出了“文件服务开发”的各个子模块，包括环境搭建、文件处理策略、接口开发（上传、删除、下载、统计、分片上传、分片合并等）。
    *   代码注释：在代码中大量使用了中文注释，如“文件夹不能为空”、“忽略路径字段，只处理文件类型”、“统计当前登录人各种类型的大小和数量”等，便于理解。
*   **关键代码片段**:
    *   **Controller层 - 文件上传** (`FileController.java`):
        ```java
        @PostMapping("/upload")
        public R<File> upload(
            @RequestParam(name = "source", defaultValue = "inner") String source,
            @RequestParam(name = "userId", required = false) Long userId,
            @RequestParam(value = "folderId") Long folderId,
            @RequestParam(value = "file") MultipartFile simpleFile
        ) {
            if (simpleFile.getContentType() == null) {
                return fail(msg: "文件为空");
            }
            File file = fileService.upload(simpleFile, folderId, source, userId);
            return success(file);
        }
        ```
    *   **Controller层 - 文件下载** (`StatisticsController.java`):
        ```java
        @GetMapping("/download")
        public void download(
            @RequestParam(name = "ids", value = "文件id 数组") String[] ids,
            @RequestParam(value = "ids") Long[] ids,
            HttpServletRequest request, HttpServletResponse response
        ) throws Exception {
            fileRestManager.download(request, response, ids, null);
        }
        ```
    *   **Service层 - 文件统计** (`FileServiceImpl.java`):
        ```java
        public InnerQueryDate invoke() {
            if (startTime == null) {
                startTime = LocalDateTime.now().plusDays(-9);
            }
            if (endTime == null) {
                endTime = LocalDateTime.now();
            }
            endTime = LocalDateTime.of(endTime.toLocalDate(), LocalTime.MAX);
            dateList = new ArrayList<>();
            dateType = DateUtils.calculationEn(startTime, endTime, dateList);
            return this;
        }
        ```
    *   **Mapper层 - SQL语句** (`FileMapper.xml`):
        ```xml
        <select id="findAlByDataType" parameterType="map" resultType="FileStatisticsAllDTO">
            SELECT
                f.create_user,
                f.file_name,
                f.file_size,
                f.file_type,
                f.create_time
            FROM
                pd_file f
            WHERE
                f.create_time BETWEEN #{startTime} AND #{endTime}
                AND f.create_user = #{userId}
            GROUP BY
                f.file_type
            HAVING
                SUM(f.file_size) > 0
            ORDER BY
                f.create_time DESC
        </select>
        ```
*   **关键公式/图表**:
    *   无明确的数学公式或复杂图表，主要以代码和数据库结构图为主。

---

### 4) 关键场景与演示描述

*   **场景一：文件上传接口开发** (约 00:00:05)
    *   讲师在IDEA中打开`FileController.java`文件，展示`@PostMapping("/upload")`方法的代码。
    *   代码中使用了`@RequestParam`注解来接收前端传来的参数，如`source`（文件来源）、`userId`（用户ID）、`folderId`（文件夹ID）和`file`（文件本身）。
    *   讲师解释了代码逻辑：首先检查文件内容类型是否为空，如果为空则返回失败信息；然后调用`fileService.upload`方法进行文件存储，并返回成功信息。
*   **场景二：文件下载接口开发** (约 00:00:10)
    *   讲师切换到`StatisticsController.java`文件，展示`@GetMapping("/download")`方法。
    *   代码中使用了`@RequestParam`注解接收`ids`参数，用于指定要下载的文件ID。
    *   讲师解释了该方法调用`fileRestManager.download`方法，将文件流写入HTTP响应，实现文件下载。
*   **场景三：文件统计接口开发** (约 00:00:15)
    *   讲师在IDEA中打开`StatisticsController.java`文件，展示`overview`和`findAlByDataType`方法。
    *   `overview`方法用于获取用户文件的概览信息。
    *   `findAlByDataType`方法用于按文件类型统计文件数量和大小。
    *   讲师解释了这两个方法的业务逻辑和返回值。
*   **场景四：分片上传与合并** (约 00:00:20)
    *   讲师在IDEA中打开`FileServiceImpl.java`文件，展示`findSizeByDate`方法。
    *   该方法用于按日期范围统计文件大小。
    *   讲师解释了`InnerQueryDate`类的`invoke`方法，用于处理日期范围的计算和数据的初始化。
*   **场景五：数据库操作演示** (约 00:00:25)
    *   讲师在Navicat Lite中打开数据库连接，展示`pd_file`表的结构。
    *   讲师在IDEA中打开`FileMapper.xml`文件，展示SQL语句。
    *   讲师解释了SQL语句的含义：查询指定用户在指定日期范围内的文件数据，并按文件类型分组统计。

---

以上是根据视频画面进行的结构化分析，希望能帮助您更好地理解课程内容。
