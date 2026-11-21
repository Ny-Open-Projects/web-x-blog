# 16-用户上传与下载功能-文件上传业务层实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们就可以实现了文件上传的功能

那么咱们来看一下

文件上传功能我们该怎么去调整和修改呢

在这里我们要去创建use file的实体

这个是用户的文件对象

那么我们上传和下载的文件

这些信息的话都是存储在这里面

那么我们做个实现

现在use file我们可以看一下

在我们bus.nd下面

已经将它做了生成

那么大家在实现的时候

可以通过mybattis.generalit的这个工程

去快速生成和实现

之前咱们也做了讲解

那我们主要看一下它具备了哪些属性

在这里面有用户的ID

业务类型文件ID

文件ID是要保持全局的唯一性

下面就是文件的名称

文件类型

路径

然后它的状态等等

好

在这里就是要注意的是文件ID的生成

因为接下来的话呢

咱们就可以用用snowflake呢

去生成对应的file ID

保持呢全局的唯一性

每个文件呢

它都有所属的业务类型

可以呢支持它的扩展

也就是说目前的话呢

比如咱们只支持身份证

还有它的银行卡

如果说将来呢

它还要再支持其他的文件类型

比如说护照啊等等的话呢

那么只要

扩展不同类型就可以了

接下来呢

咱们就来对DAO的数据层做个实现

下面呢

有五个接口

一个呢

是新增用户文件

接着呢

是更新用户文件资料

然后呢

要根据用户ID去获取呢

它的所有文件信息

下面呢

就是根据用户ID呢

以及你的文件标识类型去获取对应的文件

然后呢

就是根据文件ID去直接获取对应的文件

然后呢

就是根据文件ID去直接获取对应的文件

然后呢

就是根据文件ID去直接获取对应的文件

然后呢

就是根据文件ID去直接获取对应的文件

这五个数据层操作接口呢

可以支持新增修改查询功能

注意了

如果是存在多个参数

我们需要加上Penome的这个注解

那么单个参数的话呢

你不加上这个呢

也没有关系

它会默认的话呢

就采用了属性名称作为标识

那么多个的话呢

还是要把它加上去

该注解全路径呢

是在iBetis下面

这个呢

不要搞错了

Blainwork下面呢

也会有对应的一个注解

不要引用了其他路径的注解

好

那么

咱们呢

将这个接口就先copy过去

找到iChad的user file

它是在stockuser的DUO下面

咱们呢

将原来的接口呢

先给删除

然后呢

再新增进去

好

Helmy这个参数呢

咱们要引入iBetis下面这个包

那么接着呢

咱们还将MAP文件做个实现

是在Chad user file MAP下面

那么快速起见呢

咱们把MAP当中的

这个接口文件呢

直接copy过来

这里面呢

有五个接口

那么整个实现接口呢

并不复杂

咱们呢

就不做过多的追溯

好

在Insert的方法当中呢

它是采用select key方式去获取主线

插入完成之后呢

会将ID保存到我们参数对象Chad user file ID当中

这个呢

大家可以看到

它呢

会保存在Chad user file ID的属性当中

再往下面呢

咱们就要对service服务层做个代码试试

实现咱们去增加呢

stock user file service

在咱们的service包下面

去新增一个类

stock user file service

in payment

那咱们呢

就先来实现文件的上传功能

将属性呢

先copy进来

咱们呢

加上对应的注释

这个方法我们看一下

还没有添加对应的依赖对不对

我们要把这个依赖呢

加入进来

放到我们的user的公文件下面

这个watch呢

咱们修改一下

就采用了变量

project stock.watch

compile呢

这个不需要

好

加上注释

这个呢

是save

自动化

装配

有间依赖

好

咱们再回到刚才service当中

这个呢

就是

save

save的

API接口

下面这个呢

就是全局序列号生成器

这个呢

就是咱们刚才实现的

用户文件资料的数据层接口

好

那接着的话呢

咱们就来实现它的文件上传的处理逻辑

我们首先呢

定一个方法

public

string

upload

user id card

就是上传用户的身份证

然后呢

传递的参数是user id

这个呢

我们采用multiply

因为这个是从

control的层接口当中呢

传递过来的文件对象

multiply

好

抛出它的异常

加上注释

这呢就是上传

用户的身份证

文件信息

那我们看一下整个的处理实现流程是怎样的

首先我们对文件呢

要做一个教研判断

判断你传递过来的参数呢

是否合法

接着的话呢

咱们就要去

生成

全局的

唯一文件id标识

好

然后呢

我们要去将文件呢

上传至save服务器

然后呢

我们要从数据库当中

去获取文件信息

要判断这个文件呢

是否存在

如果是文件呢

它存在就做更新对不对

如果是不存在呢

我们就做新增

那我们呢

就对某个部

对吧

就对每个步骤呢

做个具体实现

这里呢

做个唯空判断

如果说上传的文件呢

是唯空的

我们先这里呢修正一下

我们就将这一场的跑出来

business exception

给他一个错误吧

错误网呢

我们叫userfile not found

就是用户上传的临时文件呢

没有找到

然后呢

我们就生成唯一的文件标识

remote file id

global id generator

然后呢next

之前呢咱们做了盘装对不对

那我们直接拿过来做调用就可以了

再往下面呢

咱们就通过save接口呢

去实现文件的上传

调用了free object

然后呢

要给他唯一文件的id标识

再将这个数据呢

传递到save当中

getbytes

通过二进制字节呢

将这个数据呢

传递过去

我们定义一个chaduserfile对象

这个呢

是要用于数据库的更新和保存

通过DAU呢

我们先去查询一下

根据呢

用户id

然后呢

是文件的类型

global

consistence

这个话呢

是用户的身份证

idcard

然后呢

咱们要做个判断

如果是等于空的时候呢

咱们就要对他进行什么

进行新增对不对

那么首先呢

我们要去创建一个新的chaduserfile对象

接着的话呢

我们要给他复制

bgtype

然后呢

global

file

最后上是idcard

我们还给他的名称复制

get原始的文件名称

还有很多的一些属性

咱们呢

就直接先copy过来

在讲义当中呢

我们找到对应的代码

将这一段呢

直接copy过来

把必要的属性呢

咱们都加入进去

然后呢

进行一个保存

这个就是

用户文件的保存

下面呢

是判断这个文件的不等于空

那么就说明了

他已经是存在

存在之后呢

咱们就做更新前之前呢

咱们要先将原来的文件呢

做一个删除

对不对

那么通过delete方法

然后将他原来的文件

ID标识呢

拿了

getfile ID

这样呢

我们才能够从save当中去删除原文件

如果文件呢

已存在

先删除

删除

文件服务器的原始文件

然后呢

咱们就来

更新

用户

文件信息

在这里我们更新哪些信息呢

首先的话呢

是他的文件ID

因为这个的话呢

就做了一个修改

那么呢

我们要把最新的文件ID呢

选入进去

接着的话呢

就是他的文件名称

filename

这话呢

获取他原始的文件名称

然后呢

file type

他的文件内容

这话呢

get context type

最后呢

咱们就通过DO的接口了

进行文件资料的更新

好

最后一步呢

叫返回

最新的用户文件ID

这个呢

就是用户身份证

文件上传的

功能接口

咱们呢

对他做了一个整体的实现

好

接着的话呢

咱们再从讲义当中呢

做一个回顾

首先呢

要对

整个的文件信息呢

做交易

也就是做围攻判断

然后呢

要获取全局文件ID标识

采用呢

雪花算法去做

去实现

雪花算法之前呢

咱们给大家做了讲解

他每秒呢

能够采取26万的ID

足够呢

满足高频发的场景要求

咱们放心去使用就可以

接着话呢

咱们要上传文件呢

到save系统当中

通过save

save

operate的接口呢

做对应实现

那么他可以支持呢

文件流也可以支持

字节数组的方式进行传递

如果文件呢

不是很大的情况下面

建议呢

可以直接采用字节数组

进行一个传递

那么如果是文件比较大呢

还采用文件流方式呢

会比较好一些

因为这个流社会呢

他是永远不断的去进行处理

对不对

那如果是你的文件比较大的

你通过字节方式存储呢

他要占据很大的内存

在保存数据库之前呢

先要查找用户之前

是否已经上传过该业务类型文件

如果唯空呢

咱们就新增

那么如果是已经上传了

就要覆盖更新

对不对

在这里呢

每个

业务类型呢

他只会存在一条数据

那在覆盖更新之前呢

要先将原来的物理文件

进行

删除

这样呢

防止SAVE文件服务器当中呢

产生一些垃圾文件

那么大家要注意一下

整体的实现顺序

他是有考究的

这里实现了多个功能

为了尽量保证它的一致性呢

我们呢

把容易出问题的文件上传功能呢

就放在前面去执行

这一点呢

大家要注意一下

为什么呢

咱们是按照这种流程去做对应处理

对不对

为什么不是先保存数据库的文件

然后再去上传

因为呢

我们可以看到

这个呢

是依赖于第三方SAVE的服务

对不对

并且呢

文件的这种操作

持续时间会比较长

把收购放在呢

最后面

这样呢

就不会出现现有的数据库记录呢

已经操作完成

但是呢

没有文件存在的情况

咱们想一想

如果说你数据库操作完成之后

那么调用

SAVE的时候出现问题

这样呢

就会存在不一致的情况

当然了

弊端是如果说数据库保存失败了

按现有这种方式

对吧

如果是数据库保存失败了

那么上传的文件呢

他就

成了一个

临时文件

但这种情况上来讲呢

也没环境

为什么呢

是可以接受的

因为业务数据的一致性呢

更为重要

对不对

你多产生几个临时文件呢

大不了就是占用一点空间

不会对我业务逻辑呢

整个稳定性造成影响

对不对

后面呢

也可以通过一些补偿机制

去清理无效的临时文件

所以呢

这个处理流程

整个的实现顺序

大家要明白和理解清楚

好

那么文件上传功能呢

业务层的实现

咱们呢

就先讲到这里

下一节呢

咱们再来讲解

conclude层的实现

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于一个名为“bulls-stock”的Java项目中“用户资料上传功能”的实现讲解。讲师通过在IDEA开发环境中逐步演示代码，详细说明了如何实现一个文件上传服务。核心内容包括：定义数据实体类 `TradeUserFile`，实现服务层 `StockUserFileServiceImpl`，其中包含了文件上传、校验、ID生成、Ceph对象存储上传、数据库持久化以及文件覆盖更新的完整逻辑。讲师特别强调了为保证数据一致性，将数据库操作放在最后执行的策略，并解释了其背后的业务逻辑和风险控制。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:03**: 开场，展示课程大纲，定位到“3.4 文件上传功能”章节。
*   **00:03 - 00:07**: 展示实体类 `TradeUserFile` 的定义，包含 `id` 和 `userId` 字段。
*   **00:07 - 00:11**: 展示实体类的增删改查方法，包括 `insert`, `update`, `getById`, `getByIdAndBizType`。
*   **00:11 - 00:15**: 展示服务层 `StockUserFileServiceImpl` 的类结构，包含 `@Autowired` 注入的 `cephSwiftOperator`、`globalIDGenerator` 和 `tradeUserFileDao`。
*   **00:15 - 00:20**: 进入 `uploadUserIdCard` 方法的实现，开始进行文件校验。
*   **00:20 - 00:25**: 代码中进行文件空值校验 `if (file == null)`。
*   **00:25 - 00:30**: 生成全局唯一ID，使用 `globalIDGenerator.nextStrId()`。
*   **00:30 - 00:35**: 调用 `cephSwiftOperator.createObject(remoteFileId)` 将文件上传至Ceph。
*   **00:35 - 00:40**: 从数据库查询是否存在同用户、同业务类型的文件。
*   **00:40 - 00:45**: 如果文件不存在，则插入新记录；如果存在，则先删除旧文件，再更新新记录。
*   **00:45 - 00:50**: 完成数据库操作后，返回生成的 `remoteFileId`。
*   **00:50 - 00:55**: 讲师总结实现逻辑，强调了“先上传、再查库、最后写库”的顺序，以保证数据一致性。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT内容**:
    *   **实体类定义**: `@Data public class TradeUserFile extends BaseEntity { private Long id; private Long userId; }`
    *   **服务层方法**: `int insert(TradeUserFile record); int update(TradeUserFile record); List<TradeUserFile> getByUserId(Long userId); TradeUserFile getByUserIdAndBizType(@Param("userId") Long userId, @Param("bizType") Integer bizType); TradeUserFile getByFileId(@Param("fileId") Long fileId);`
    *   **服务层实现**: `public class StockUserFileServiceImpl implements IStockUserFileService { @Autowired private CephSwiftOperator cephSwiftOperator; @Autowired private GlobalIDGenerator globalIDGenerator; @Autowired private ITradeUserFileDao tradeUserFileDao; }`
    *   **核心方法**: `public String uploadUserIdCard(Long userId, MultipartFile file) throws Exception { ... }`
    *   **关键逻辑总结**:
        1.  先校验，获取全局文件ID标识，采用雪花算法实现，支持分布式，每秒可以产生26万ID，能够满足高并发场景要求。
        2.  上传文件至Ceph系统，通过封装的`cephSwiftOperator`实现，ceph可以支持文件流和字节数组方式传递，文件不是很大的情况，可以直接采用字节数组方式。
        3.  在保存数据库之前，先要查询用户之前是否已经上传过该业务类型文件，如果为空，则新增；如果之前已经上传，则覆盖更新，每个用户的每个业务类型，只能存在一条数据。在覆盖更新之前，要将原来上传的物理文件删除，再做更新。
        4.  注意整体的实现顺序，是有考究的。这里实现了多个功能，为尽量保证一致性，我们把容易出现问题的文件上传功能放在前面执行，因为依赖第三方ceph服务，且持续时间较长；把SQL操作放在最后。这样就不会出现数据库记录，但没有文件存在的情况。当然，弊端是如果数据库保存失败，上传的文件就成了临时文件，但这种情况不影响业务，因为业务数据的一致性就更重要，后面也可以通过补偿机制，清理无效的临时文件。

*   **代码关键内容**:
    *   **文件校验**: `if (file == null) { throw new BusinessException(ApplicationErrorCodeEnum.USER_FILE_NOT_FOUND); }`
    *   **生成ID**: `String remoteFileId = globalIDGenerator.nextStrId();`
    *   **上传文件**: `cephSwiftOperator.createObject(remoteFileId);`
    *   **查询数据库**: `dbTradeUserFile = tradeUserFileDao.getByUserIdAndBizType(userId, bizType);`
    *   **覆盖更新逻辑**:
        ```java
        if (dbTradeUserFile == null) {
            // 新增
            dbTradeUserFile.insert(dbTradeUserFile);
        } else {
            // 删除旧文件
            cephSwiftOperator.deleteObject(dbTradeUserFile.getFileId());
            // 更新新文件信息
            dbTradeUserFile.setFileId(remoteFileId);
            dbTradeUserFile.setFileName(file.getOriginalFilename());
            dbTradeUserFile.update();
        }
        ```
    *   **返回结果**: `return remoteFileId;`

---

### 4) 关键场景与演示描述

*   **场景一：实体类定义与方法声明 (00:03-00:11)**
    *   讲师在Typora中展示 `TradeUserFile` 类的定义，强调其作为数据实体的作用。
    *   随后，讲师滚动展示该类中定义的增删改查方法，为后续的数据库操作做准备。

*   **场景二：服务层实现与核心方法 (00:15-00:45)**
    *   讲师切换到IDEA，展示 `StockUserFileServiceImpl` 类的结构，重点讲解其依赖的三个组件：`CephSwiftOperator`（用于与Ceph存储交互）、`GlobalIDGenerator`（用于生成唯一ID）和 `ITradeUserFileDao`（用于与数据库交互）。
    *   讲师进入 `uploadUserIdCard` 方法，首先进行文件空值校验，如果文件为空则抛出业务异常。
    *   接着，讲师演示如何使用 `globalIDGenerator` 生成一个全局唯一的文件ID。
    *   然后，讲师调用 `cephSwiftOperator.createObject(...)` 方法，将文件上传到Ceph存储系统。
    *   之后，讲师演示如何通过 `tradeUserFileDao.getByUserIdAndBizType(...)` 方法查询数据库，检查该用户是否已经上传过该业务类型的文件。
    *   讲师演示了“如果不存在则新增，如果存在则先删除旧文件再更新”的覆盖逻辑，代码中包含了对Ceph的 `deleteObject` 方法的调用。

*   **场景三：业务逻辑总结与一致性保障 (00:50-00:55)**
    *   讲师回到Typora，通过PPT总结了整个上传流程。
    *   讲师重点解释了“先上传、再查库、最后写库”的顺序设计，其目的是为了保证业务数据的一致性。
    *   讲师指出，虽然这种设计可能导致上传的文件在数据库写入失败后成为“临时文件”，但业务上可以接受，因为业务数据的一致性更为重要。
    *   讲师最后提到，可以通过补偿机制来清理这些无效的临时文件，从而实现最终的一致性。
