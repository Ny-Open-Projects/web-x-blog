# 20-用户上传与下载功能-上传功能的使用验证 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来呢

咱们对上传功能做个使用和验证

首先呢

咱们要确保相关服务呢

都启动成功

首先要检查呢

Safe集群呢

是否启动正常

通过Safe-S命令呢

确认状态呢

是否OK的

那咱们呢

在虚拟机上面

执行了-S命令

一定要确保呢

它是HealthOK

就是属于正常运行的状态

接着的话呢

要启动认证服务

以及呢

用户服务

在启动服务之前呢

我们要先将

Ladies

和Nacos服务呢

启动成功

好

接着呢

我们再启动认证服务

和用户服务

这个呢

是认证服务

右键

Run运行

然后呢

我们还有将刚才呢

编写和实现的用户服务呢

启动起来

注意观察启动日志

不要出现错误

用户服务呢

我们也做个启动

在这里呢

用户服务出现了错误

这个咱们可以看到

它是呢

Shared User File Map里面呢

保存了一场

好

我们看一下该怎么去处理呢

我们在用户服务的功能下面

找到对应的文件

它这提示什么呢

它是说

我们在这里面呢

已经存在了一个

Get By User ID

对不对

好

那么我们来搜索一下

Get By User ID

可以看到

存在了两个

对不对

那么我们要把一个呢

去除

好

其他的话呢

我们也检查一下

像映射的呢

还有没有重复呢

这些话呢

没有重复

映射的话呢

我们就不需要

把它呢

去除

好

接着的话呢

我们再重启用户服务

在整个实现的过程当中呢

我们不要去盲目的去copy

copy的时候呢

要去检查好

对应的这些代码呢

是否是完善

没有问题的

那如果是出现问题的话呢

我们要注意去排查

好

整个用户服务呢

就已经启动成功

认证服务呢

咱们也看一下

它整个运行的话呢

也是OK的

好

接着的话呢

咱们就来做一个

上传的功能测试和验证

咱们呢

首先通过

获胜们工具呢

去申请一个token

这个认证服务的话呢

是9999

我们找到了之前的一个访问测试记录

那么我们去申请个token

它说这个用户对象呢

转换的时候出现错误了

这个呢

之前咱们是

有用户的一些缓存记录

大家在进行测试的时候

如果碰到这种情况呢

怎么去处理呢

首先我们要通过Ladies连接工具

在这里呢

我们要将它的缓存清除掉

我们看一下

它的缓存对应是什么呢

这个话呢

我们要把它的key先找到

查询缓存的时候呢

它用的是这个key

对不对

stock user details

它的key的具体值呢

就是os开头

stock user details

那么我们就按照这种路径呢

去查找

os

stock

user details

我们把它呢

清除

清除完成之后呢

咱们再去请求

这个时候呢

就可以看到

能够呢

正常获取到token了

对不对

好

拿到token之后呢

接着咱们就去实现了

文件的上传功能

我们要注意

上传文件的时候呢

采用的是

form data

表单的形式进行了提交

然后在这里呢

它的类型是采用file

咱们呢

就来通过poster门工具

做个测试和验证

新建一个

标明窗口

在这里呢

采用post方式进行上传

咱们来看一下

之前所编写的接口

它只支持呢

post方式进行提交

对不对

那么我们拿到它的接口名称

VTDP

17.0.0.1

它端口是什么

10691

咱们确认一下

它的端口呢

是10681

那么我们将刚才接口的拷贝进来

好

注意

它的玻璃参数呢

采用form data表单的形式

然后这个类型呢

要采用file

名称呢

叫做file

这里面呢

我们选中一个文件

对不对

选择一个图片文件

我们就随便拿张图片

接着话呢

我们不要忘记加上它的token信息

这个token呢

拿我们之前刚才所申请的token

在这里呢

它的认证方式是采用value token

这次的话呢

改用我们刚才所申请的

那么呢

我们就来发送上传的接口请求

看一下呢结果是否合适呢

OK

点击send

好

可以看到了

它的结果呢

是返回成功的

并且呢

将文件的ID呢

也返回出来了

我们可以拿到这个ID呢

去数据库查验一下数据

我们进入chatstock

我们找到tchatuserfile这个表

可以看到的这里面有一条记录了

对不对

这个ID的话呢

跟这个ID是不是一致呢

我们可以看到这两个ID的话呢

都是一致的

对不对

就是什么呢

刚才所上传的这个文件

那在这里呢

咱们是通过postman

对整个文件上传功能呢

做了一个测试和验证

那整个验证下来的话呢

也是符合咱们的预期

接下来呢

我们要去实现文件的下载功能

去验证呢

咱们刚才所上传的这个文件呢

能否去通过save成功获取和下载

这一讲呢

就是对save功能的测试

那这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频片段是关于一个基于 Spring Boot 的文件上传与下载系统的开发与验证过程。核心内容围绕如何在用户上传文件时，通过 OAuth2 服务获取用户身份信息，并将文件元数据（如文件名、类型、路径）存储到数据库中，同时将实际文件存储到 Ceph 分布式存储系统。视频演示了从启动服务、申请访问令牌、编写并调试数据库映射文件（MyBatis），到最终在前端界面查看上传数据的完整流程。整个过程强调了服务间的协作（如 `trade-auth` 和 `stock-user` 服务）以及后端代码与数据库的联动。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，展示课程大纲，定位到“3.6 上传功能使用验证”章节。
*   **00:00:05 - 00:00:15**: 展示 Postman 工具，准备向 `http://127.0.0.1:9999/oauth/token` 发起请求以获取访问令牌。
*   **00:00:15 - 00:00:25**: 在 IntelliJ IDEA 中，展示 `TradeAuthApplication` 的启动类，准备启动 `trade-auth` 服务。
*   **00:00:25 - 00:00:35**: 启动 `stock-user` 服务，展示其 `StockUserApplication` 的主类。
*   **00:00:35 - 00:00:45**: 在 `TradeUserFileMapper.xml` 中，编写用于插入文件记录的 SQL 映射语句。
*   **00:00:45 - 00:00:55**: 在 `TradeUserFileMapper.xml` 中，编写用于根据用户 ID 查询文件记录的 SQL 映射语句。
*   **00:00:55 - 00:01:05**: 在 `StockUserController` 中，编写 `@PostMapping("/uploadCard")` 接口，用于处理文件上传请求。
*   **00:01:05 - 00:01:15**: 在 Navicat 数据库管理工具中，查看 `t_trade_user_file` 表，确认文件记录已成功插入。
*   **00:01:15 - 00:01:25**: 在 Typora 文档中，展示“3.7 文件下载功能”的章节标题，预示下一阶段的开发。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **章节标题**: “3.6 上传功能使用验证” 和 “3.7 文件下载功能”。
    *   **服务启动步骤**: 1. 启动 ceph 集群 (`ceph -s`)；2. 启动 `trade-auth` 服务；3. 启动 `stock-user` 服务。
    *   **令牌申请接口**: `GET http://127.0.0.1:9999/oauth/token`，请求参数包括 `grant_type`, `username`, `password`。
    *   **文件上传接口**: `@PostMapping("/uploadCard")`，接收 `@RequestParam("file") MultipartFile file`。
    *   **文件下载功能**: “新增一个接口，根据文件ID标识下载文件”。

*   **代码关键内容**:
    *   **`TradeAuthApplication.java`**:
        ```java
        @EnableDiscoveryClient
        @ComponentScan(basePackages = {"com.ictast"})
        @EnableJpaRepositories(basePackages = {"com.ictast"})
        @EnableCaching
        public class TradeAuthApplication {
            public static void main(String[] args) {
                SpringApplication.run(TradeAuthApplication.class, args);
            }
        }
        ```
    *   **`StockUserApplication.java`**:
        ```java
        @EnableDiscoveryClient
        @EnableFeignClients
        @ComponentScan(basePackages = {"com.ictast.trade.bulls.stock.user.dao", "com.ictast.bulls.stock.common.system.dao"})
        @EnableTransactionManagement
        @EnableCaching
        public class StockUserApplication {
            public static void main(String[] args) {
                SpringApplication.run(StockUserApplication.class, args);
            }
        }
        ```
    *   **`TradeUserFileMapper.xml` (插入语句)**:
        ```xml
        <insert id="insert" parameterType="com.ictast.trade.stock.entity.TradeUserFile" useGeneratedKeys="true" keyProperty="id">
            insert into t_trade_user_file (userId, bizType, fileId, filename, fileType, filePath, status, createTime)
            values
            (#userId,jdbcType=INTEGER), #bizType,jdbcType=INTEGER), #fileId,jdbcType=VARCHAR),
            (#filename,jdbcType=VARCHAR), #fileType,jdbcType=VARCHAR), #filePath,jdbcType=VARCHAR),
            (#status,jdbcType=INTEGER), #createTime,jdbcType=TIMESTAMP)
        </insert>
        ```
    *   **`TradeUserFileMapper.xml` (查询语句)**:
        ```xml
        <select id="getById" resultMap="BaseResultMap">
            select id, userId, bizType, fileId, filename, fileType, filePath, status, createTime, updateTime
            from t_trade_user_file
            where userId = #{userId} and bizType = #{bizType}
        </select>
        ```
    *   **`StockUserController.java` (上传接口)**:
        ```java
        @PostMapping("/uploadCard")
        public ApiRespResult uploadCard(@RequestParam("file") MultipartFile file) {
            ApiRespResult result = null;
            try {
                // 1. 获取用户的ID
                Long userId = getUserId();
                // 2. 保存用户上传的文件
                String fileId = stockUserService.uploadCard(file);
                return ApiRespResult.success(fileId);
            } catch (Exception e) {
                e.printStackTrace();
                return ApiRespResult.error("文件上传失败");
            }
        }
        ```

*   **图表/界面**:
    *   **Postman 请求界面**: 用于模拟获取 OAuth2 令牌的 HTTP GET 请求。
    *   **Navicat 数据库界面**: 用于查看 `t_trade_user_file` 表中的数据，确认上传成功。
    *   **IntelliJ IDEA 项目结构**: 展示了 `stock-user` 和 `trade-auth` 服务的项目目录和代码文件。

---

### 4) 关键场景与演示描述

*   **场景一：服务启动与令牌申请**
    *   **描述**: 讲师首先在 Postman 中配置了获取访问令牌的请求，参数包括用户名 `admin` 和密码。随后，他启动了 `trade-auth` 服务（通过 `TradeAuthApplication` 的 `main` 方法），并准备启动 `stock-user` 服务。此场景旨在验证服务间的依赖关系和认证服务的可用性。

*   **场景二：数据库映射文件调试**
    *   **描述**: 讲师在 `TradeUserFileMapper.xml` 中编写了用于插入和查询文件记录的 SQL 映射语句。他通过在 IDEA 中的 Console 窗口查看日志，确认了 MyBatis 映射文件的加载情况。在调试过程中，他遇到了一个 `IllegalArgumentExeption`，提示“Mapped Statements collection already contains value for ...”，这表明他正在处理一个已存在的映射语句，需要进行修改或删除。

*   **场景三：文件上传接口实现**
    *   **描述**: 讲师在 `StockUserController` 中实现了 `@PostMapping("/uploadCard")` 接口。该接口接收一个 `MultipartFile` 对象，首先通过 `getUserId()` 方法获取用户 ID，然后调用 `stockUserService.uploadCard(file)` 方法来处理文件上传。此场景展示了如何将前端上传的文件与后端服务进行交互。

*   **场景四：数据验证与下载功能预告**
    *   **描述**: 讲师使用 Navicat 工具连接到数据库，查询 `t_trade_user_file` 表，成功查看到了上传的文件记录，包括文件 ID、文件名和文件类型。随后，他在 Typora 文档中切换到“3.7 文件下载功能”章节，预示接下来将实现文件下载功能，即根据文件 ID 从 Ceph 存储中获取文件。

---

以上是根据视频画面进行的详细技术分析。
