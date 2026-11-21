# 28-车辆轨迹服务（pd-druid开发） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好前面呢我们关于PD-90这个微服务的开放呢都已经完成了

下边呢就是这个PD-J的

因为我们前面也提到了咱们车辆轨迹服务呢

主要涉及到的就是这么两个工厂对吧

一个是PD-90还有一个是PD-J的

然后呢PD-J的呢这里边的代码呢我们都已经写完了

咱们直接使用就可以

因为这块呢其实相对来说还是比较简单的

就是什么呢我们这个PD-J的呢

它其实主要的作用就是什么呢

跟我们的这个J的服务来进行对接

从这里边是不是来查询数据

而这块的话呢我们前面在这个Java客户端操作J的这儿

是不是已经写过一个小的案例了对不对

而这块的话呢其实就是使用我们最早讲的GDPC这种方式呢

来操作我们的J的

你看这儿写的其实也就是普通的sql对吧

那么这儿呢指定连接的我们这个J的它服务的这个地址对吧

所以说呢我们这个PDJ的呢

跟我们前面这个Java客户端操作J的呢

其实是一回事

无非呢就是操作的数据源

不一样对吧

那么我们这个地方呢要查的就是这个TMS order location

所以说呢在我们这个PDJ的当中呢

我们提前呢都已经把这个代码写好了

因为都是GDPC这种代码

所以我们这块呢就不再刻上去开发了

咱们大概呢把这个代码读一下就可以了

你看在我们这个controller当中啊提供了这么三个方法

其实全都是查询什么呢

我们这个车辆位置信息的对吧

只不过就是传的参数呢不一样啊

这个是查询什么

这个是传的参数呢

全部车辆最后位置信息

然后呢这个是指定车辆

这个是select one对吧

然后呢这个是根据动态参数

那么它是传过来一个list的

里边呢封装的是一个一个的map

然后也就是根据各种各样的不同的参数

来这个进行查询

最终呢你看它都是调用一个service对吧

调用service

然后呢来查咱们往里面跟一下

你看这边调用这个service的这个方法

然后在这儿呢

是不是把我们这个什么

这个车辆的位置信息

把这些参数是不是来设置一下

然后呢把这个circle来拼一下

注意看它是from我们这个

填码s other location

其实对应的就是咱们追的上面的这个数据源

对吧

然后呢这是动态

前面这是动态去拼一些这个参数

最后呢把这个参数拼到我们这个circle语句里面去

然后呢调用这个map的这个方法

而在这个地方呢我们来看一下

你看它是不是就会使用我们这个jdbc

这不是jdbc的connection吗

对吧

然后呢

哎

在这儿注入我们这个配置的数据源对象

然后呢

这段代码呢

看着就比较眼熟了

就跟我们前面这个案例是一样的

Java code端来操作对的

就是这道代码

无非就是封装到这个map里面去了

最终的把我们这个circle执行一下

对吧

把返回结果封装一下

所以说呢

我们这块代码呢

因为是从技术上来说没有什么新的基础点啊

所以我们这个的话呢

就直接提供好

大家能够直接使用这个代码

就可以了

好

这是关于咱们这个pd3的呢

我们来说一下

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是关于“品达物流TMS项目”第7章“车辆轨迹服务”的开发教程，主要聚焦于使用 `pd-netty` 和 `pd-druid` 两个模块来实现车辆轨迹数据的获取与处理。课程内容分为两大部分：
- **第一部分（5.1）**：介绍基于 `pd-netty` 的 TCP 通信方式，用于建立客户端与服务端的连接，并处理网络通信的生命周期（如连接建立、关闭）。
- **第二部分（5.2）**：讲解如何使用 `pd-druid` 模块连接并操作 Apache Druid 数据库，实现对车辆轨迹数据的查询。这部分代码已预先写好，开发者只需直接调用即可。

整个课程通过 IntelliJ IDEA 开发环境进行演示，展示了从项目结构、控制器层、服务层到数据访问层的完整代码实现，并辅以 Typora 文档和数据库操作的说明。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取视频的实际时间戳，以下章节结构是根据画面内容推断的逻辑顺序：

- **00:00 - 00:30**：课程导览与项目背景介绍。讲师在 Typora 文档中展示项目大纲，重点指向“5. 车辆轨迹服务”下的“5.2 pd-druid开发”章节，说明本节将讲解如何使用 pd-druid 连接数据库。
- **00:30 - 01:00**：演示 `pd-netty` 的 TCP 通信客户端。在 IDEA 中展示 `NettyClientTest` 类，演示如何异步连接服务器、等待连接完成、关闭连接并优雅地释放资源。
- **01:00 - 01:30**：讲解 `pd-druid` 的数据库连接与查询。展示 `DruidController` 中的 `select`、`selectOne`、`selectByList` 等接口，说明这些接口用于调用底层服务查询数据。
- **01:30 - 02:00**：深入 `DruidServiceImpl` 服务层代码。展示 `listFirst` 方法的实现，该方法负责执行 SQL 查询、处理结果集，并将数据封装成 `Map` 对象返回。
- **02:00 - 02:30**：展示 `BaseMapper` 中的 `listFirst` 方法，该方法是 `DruidServiceImpl` 中 `listFirst` 方法的底层实现，负责与数据库进行实际交互。
- **02:30 - 03:00**：演示 SQL 查询语句的构建。在 `DruidServiceImpl` 中，展示如何根据传入的参数动态拼接 SQL 语句，例如查询车辆的经纬度和时间。
- **03:00 - 03:30**：总结与收尾。讲师在 Typora 文档中再次强调“5.2 pd-druid开发”章节，说明该部分代码已写好，开发者可直接使用。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

- **Typora 文档**：
  - 项目名称：“品达物流TMS项目”。
  - 当前章节：“5. 车辆轨迹服务”。
  - 子章节：“5.2 pd-druid开发”。
  - 关键说明：“在初始项目中已经编写完成，直接使用即可。”

#### 代码关键内容

- **Netty TCP 客户端 (`NettyClientTest.java`)**
  ```java
  public static void main(String[] args) throws Exception {
      new NettyClientTest(hosts, port).start();
  }
  // 连接服务器
  cf.channel().closeFuture().sync();
  // 关闭完成
  group.shutdownGracefully().sync();
  ```

- **Druid Controller (`DruidController.java`)**
  ```java
  @ApiOperation("查询Druid全部车辆的最后位置列表")
  @RequestMapping(value = "/select")
  public Result select(@RequestParam Map<String, Object> params) { return druidService.select(params); }

  @ApiOperation("查询Druid当前车辆的全部位置")
  @RequestMapping(value = "/selectOne")
  public Result selectOne(@RequestParam Map<String, Object> params) { return druidService.selectOne(params); }

  @ApiOperation("查询Druid当前全部位置")
  @RequestMapping(value = "/selectByList")
  public Result selectByList(@RequestBody List<Map<String, Object>> params) { return druidService.selectByList(params); }
  ```

- **Druid Service (`DruidServiceImpl.java`)**
  ```java
  public Result selectOne(Map<String, Object> params) {
      StringBuffer baseSql = new StringBuffer("select name,phone,licensePlate,businessId,_time from tms_order_location where 1=1");
      baseSql.append(whereSql(params));
      baseSql.append(orderSql(params));
      Map baseMap = messageMapper.listFirst(baseSql.toString());
      if (CollectionUtils.isEmpty(baseMap)) {
          return Result.ok();
      }
      return Result.ok(baseMap);
  }
  ```

- **Base Mapper (`BaseMapper.java`)**
  ```java
  public Map listFirst(String sql) {
      Connection connection = null;
      Statement st = null;
      ResultSet rs = null;
      try {
          connection = dataSource.getConnection();
          st = connection.createStatement();
          rs = st.executeQuery(sql);
          ResultSetMetaData rsmd = rs.getMetaData();
          if (rs.next()) {
              Map map = new HashMap();
              for (int i = 0; i < rsmd.getColumnCount(); i++) {
                  String columnName = rsmd.getColumnName(i + 1);
                  map.put(columnName, rs.getObject(columnName));
              }
              return map;
          }
      } catch (SQLException e) {
          log.error("关闭连接异常：", e);
      } finally {
          try {
              connection.close();
          } catch (SQLException e) {
              log.error("关闭连接异常：", e);
          }
      }
      return null;
  }
  ```

- **Druid 数据库连接代码 (`pd-druid` 模块)**
  ```java
  Class.forName("org.apache.calcite.avatica.remote.Driver");
  Connection connection = DriverManager.getConnection("jdbc:avatica:remote:url=http://68.79.63.42:8888/druid/v2/sql/avatica/");
  ```

---

### 4) 关键场景与演示描述

- **场景一：项目结构与章节导航**
  - 讲师在 Typora 文档中滚动鼠标，高亮显示“5.2 pd-druid开发”章节，强调本节内容。
  - 展示项目结构，包括 `pd-netty` 和 `pd-druid` 两个模块。

- **场景二：Netty TCP 客户端演示**
  - 在 IDEA 中打开 `NettyClientTest.java`。
  - 讲师演示 `main` 方法，创建 `NettyClientTest` 实例并调用 `start()` 方法。
  - 代码中使用 `cf.channel().closeFuture().sync()` 等方法，演示连接建立、等待连接完成、关闭连接和释放资源的完整流程。

- **场景三：Druid Controller 接口演示**
  - 在 IDEA 中打开 `DruidController.java`。
  - 讲师高亮显示 `@ApiOperation` 注解和 `@RequestMapping` 注解，说明这些接口用于查询车辆轨迹数据。
  - 展示 `select`、`selectOne`、`selectByList` 三个方法，说明它们分别用于查询全部车辆、单个车辆和列表数据。

- **场景四：Druid Service 层代码演示**
  - 在 IDEA 中打开 `DruidServiceImpl.java`。
  - 讲师高亮显示 `selectOne` 方法，展示如何构建 SQL 语句并调用 `messageMapper.listFirst` 方法。
  - 展示 `listFirst` 方法的实现，说明其如何处理数据库查询结果。

- **场景五：Base Mapper 层代码演示**
  - 在 IDEA 中打开 `BaseMapper.java`。
  - 讲师高亮显示 `listFirst` 方法，说明其如何执行 SQL 查询、处理结果集并返回 `Map` 对象。
  - 展示 `try-catch-finally` 块，说明如何处理数据库连接异常。

- **场景六：SQL 语句构建演示**
  - 在 `DruidServiceImpl.java` 中，讲师高亮显示 `StringBuffer` 的使用，展示如何动态拼接 SQL 语句。
  - 展示 `whereSql` 和 `orderSql` 方法，说明如何根据参数动态添加查询条件和排序条件。

- **场景七：数据库连接与查询**
  - 在 Typora 文档中，讲师展示 `pd-druid` 的数据库连接代码。
  - 展示 `Class.forName` 和 `DriverManager.getConnection` 方法，说明如何连接 Apache Druid 数据库。
  - 展示 `ResultSetMetaData` 和 `ResultSet` 的使用，说明如何获取查询结果的元数据和数据。

- **场景八：多窗口演示**
  - 讲师在 Typora 文档中打开多个窗口，包括 IDEA、Notepad++ 和 Chrome。
  - 展示 `pd-dr
