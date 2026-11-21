# 32-常见组件与中台化-常用组件服务介绍（分布 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么刚才呢,我们是对着蒋易呢,来给大家说明了一下,就是我们这个分布式ID服务,部署完了之后呢,具体如何来使用,对吧,也就是它的使用说明,那接下来呢,我们可以来带着大家来操作一下,首先呢,我们需要来创建一个第三方系统,对吧,那么我在这呢,是创建了这么一个叫做distributed ID-demo,这个比较简单,

然后呢,需要在这个系统里边来引入什么呢,引入咱们这个client,但是前提是什么呢,需要你提前安装,对吧,你看我在这边呢,其实已经提前安装了,就是把我们这个client模块,把它装到你Maven的这个本地仓库,前面我也提到了,如果说你们公司有私服,对吧,你也可以把它安装到私服,这样的话呢,整个公司的这个开发团队呢,就都可以使用了,

好,现在呢,我是把它安装到我本地的Maven,

然后呢,在我这个POM文件当中,把它引进来,好,这是第一步,对吧,引进来之后呢,我们还需要来编写它的一个配置文件,注意这个配置文件的名字呢,不能改,必须叫这个名字,而且这个位置呢,也必须是在resource下边,在resource直接的这个根目录下边,叫做distributed ID-client.properties,为什么必须叫这个名字呢,是因为咱们引入的这个架包,我们引入的这个client包呢,

它就会去读取这个文件来获取这个配置信息,所以说呢,我们这个地方呢,一定要按照它的要求来写,否则的话呢,它就读不到这个配置了,而这个配置呢,它其实主要配置的是什么呢,就是我们服务器的ID,这个服务器呢,指的是什么呢,指的就是咱们这边这个分布式ID服务,也就是这个server,它所对应的这个IP,还有这个端口号,

而我现在呢,很显然是部署在本地的吧,

所以我写localhost的,然后端口号呢,是18099,这个呢,也是跟它对应的,你看这边,我这边是不是写的,这个端口号是18099,所以按照它的要求,把这个配置文件创建出来,创建出来之后呢,我们其实就可以来编写一个什么测试类,对吧,我在这其实直接写了个面方法,然后呢,通过这种方式,然后呢,我们是不是直接调这个类,而这个类的话呢,它其实来自于哪呢,就来自于咱们引入的这个,你看client包,

distributed client,你可以把它当成就是一个工具类,它这里边封装了一些这个什么呢,静态方法,对吧,而这些静态方法呢,它底层呢,就会干什么呢,就会去通过远程调用,去调到我们真正的这个fin,调用到我们真正的这个什么呢,server,最终呢,在server这边来给我们生成这个ID,所以我们从使用者的这一端来看的话呢,其实就非常简单了,你直接调它这些静态方法,它就可以给我们生成,

各种各样的ID,比如说这个呢,是从服务器端来获得资增型的ID,对吧,然后呢,这个呢,是什么呢,本地生成雪花算法,对吧,继续雪花算法来生成ID,这个呢,是从服务器端获取雪花算法生成的ID,好,但是它还有其他的,比如说我们再来一个distributed ID点什么呢,你看它有这个segment,segment其实就是什么呢,就是我们这个生成某一段,

生成某一段,比如说我在这儿,这个呢,这个Biztype指的是什么呢,是我们的这个业务类型,一般对应的就是我们这个系统类型,比如说我这个来个TMS,因为我们不同的系统,不同的业务呢,是不是都可以去调这些服务,对吧,然后呢,我们通过一个Biztype来区分什么呢,不同的服务,然后呢,它的返回值,你看是不是也是一个浪形的ID,OK,

然后呢,我们可以在这儿来输出一下这个ID的值,对吧,那ID的值呢,咱们都可以来输出一下,好,然后呢,我们就直接来执行一下这个Main方法就可以了,这样的话呢,它底层呢,就会去调到我们这个服务,最终呢,把这个ID呢,给生成出来,你看,把这个ID给生成出来,好,你看这是,这个是一个ID,对吧,这是一个ID,这个是一个ID,然后呢,这个是ID,这个也是ID,好,

最终呢,把不同的ID呢,是不是都能够给获取到,好,这就是我们作为这个使用方,对吧,我们如何来使用咱们这个分布式ID服务,那么整体使用起来呢,还是比较简单的,重点呢,就这么三步,第一步呢,引坐标,第二步呢,写配置文件,第三步呢,是不是就是直接去调它这个静态方法来获得ID就可以了。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程旨在演示一个名为 `distributedid` 的分布式ID生成系统的实际应用。该系统包含一个服务端和一个客户端，用于在分布式环境中生成唯一ID。课程通过 IntelliJ IDEA 开发环境，逐步展示了如何配置项目、编写测试代码，并最终运行程序来验证ID生成功能。核心内容包括：
- **项目结构**：展示了 `distributedid-client` 和 `distributedid-server` 两个模块的 `pom.xml` 文件，说明了依赖关系。
- **配置文件**：重点讲解了 `distributedid_client.properties` 文件，用于配置服务端地址和超时时间。
- **代码实现**：演示了 `DistributedId` 类中提供的三种ID生成方式：自增ID、本地雪花算法ID、以及从服务端获取的雪花算法ID。
- **运行演示**：通过 `DistributedIdTest` 测试类，成功调用并打印了三种不同类型的ID，验证了系统的功能。

---

### 2) 按时间顺序的章节（带时间点）

由于无法从画面中精确获取视频的时间戳，以下章节是根据画面内容和逻辑顺序推断的：

- **00:00 - 00:05**: 课程开场，展示 IntelliJ IDEA 的初始界面，项目名为 `distributedid_demo`。
- **00:05 - 00:15**: 展示 `distributedid-client` 模块的 `pom.xml` 文件，重点讲解了 `dependencies` 部分，包括 `distributedid-core` 和 `junit` 依赖。
- **00:15 - 00:25**: 展示 `distributedid_client.properties` 配置文件，讲解了 `distributedid.server`、`readTimeout` 和 `connectTimeout` 等关键配置项。
- **00:25 - 00:35**: 展示 `DistributedId` 类的源码，讲解了 `IdGenClientFactory`、`Snowflake` 和 `userMap` 等核心成员变量及方法。
- **00:35 - 00:45**: 展示 `DistributedIdTest` 测试类的源码，演示了如何调用 `autoincrementId`、`snowflake` 和 `snowflakeFromServer` 方法。
- **00:45 - 00:55**: 运行测试程序，终端输出了三种ID的生成结果，验证了功能。
- **00:55 - 01:05**: 展示了课程配套的 PPT，其中包含了 `pom.xml` 和 `distributedid_client.properties` 的配置说明，以及ID获取的三种方式。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT 内容

- **标题**：分布式ID生成系统使用说明。
- **章节**：2.3.4 使用说明。
- **内容**：
  1. 引入 `distributedid-client` 依赖。
  2. 配置 `distributedid_client.properties` 文件。
  3. 获取ID的三种方式：
     - `DistributedId.autoincrementId("your service name")`
     - `DistributedId.snowflake()`
     - `DistributedId.snowflakeFromServer()`

#### 代码关键内容

- **`pom.xml` (客户端)**：
  ```xml
  <dependencies>
      <dependency>
          <groupId>com.ithema.distributedid</groupId>
          <artifactId>distributedid-client</artifactId>
          <version>1.0-SNAPSHOT</version>
      </dependency>
      <dependency>
          <groupId>junit</groupId>
          <artifactId>junit</artifactId>
          <version>4.12</version>
          <scope>test</scope>
      </dependency>
  </dependencies>
  ```

- **`distributedid_client.properties`**：
  ```properties
  #服务器地址
  distributedid.server=localhost:18099
  #部署多个的话，可自行添加
  #distributedid.server=211.103.136.244:7315,ip2:port,...
  #超时时间
  distributedid.readTimeout=5000
  distributedid.connectTimeout=5000
  ```

- **`DistributedId.java`**：
  ```java
  public class DistributedId {
      private static IdGenClientFactory clientFactory = IdGenClientFactory.getInstance(String.valueOf(System.currentTimeMillis()));
      private static Snowflake snowflake = new Snowflake();
      private static Map<String, Snowflake> userMap = new HashMap<>();

      public static Long autoincrementId(String bizType) {
          return clientFactory.getAutoincrementId(bizType);
      }

      public static Long snowflake() {
          return snowflake.nextId();
      }

      public static Long snowflake(long dataCenterId, long machineId) {
          Snowflake snowflake = userMap.get(dataCenterId + "_" + machineId);
          if (snowflake != null) {
              return snowflake.nextId();
          } else {
              // ... (省略初始化逻辑)
          }
      }
  }
  ```

- **`DistributedIdTest.java`**：
  ```java
  public class DistributedIdTest {
      public static void main(String[] args) {
          Long id = 0L;
          // 从服务端获取自增型ID
          id = DistributedId.autoincrementId("sms");
          System.out.println(id);

          // 本地生成雪花算法ID
          id = DistributedId.snowflake();
          System.out.println(id);

          // 从服务端获取雪花算法ID
          id = DistributedId.snowflakeFromServer();
          System.out.println(id);

          // 段模式ID
          id = DistributedId.segment(bizType: "tms");
          System.out.println(id);
      }
  }
  ```

---

### 4) 关键场景与演示描述

- **场景一：项目结构与依赖配置**
  - **描述**：讲师在IDE中打开 `distributedid-client` 模块，展示其 `pom.xml` 文件。通过高亮和滚动，重点讲解了 `distributedid-client` 和 `junit` 依赖的配置，说明了项目构建所需的外部库。

- **场景二：配置文件详解**
  - **描述**：讲师切换到 `distributedid_client.properties` 文件，通过鼠标悬停和高亮，解释了 `distributedid.server` 用于指定服务端地址，`readTimeout` 和 `connectTimeout` 用于设置网络超时时间，这些配置对客户端与服务端的通信至关重要。

- **场景三：核心代码实现**
  - **描述**：讲师在 `DistributedId.java` 文件中，通过滚动和高亮，解释了 `IdGenClientFactory` 用于管理客户端工厂，`Snowflake` 用于生成本地雪花算法ID，以及 `userMap` 用于存储不同数据中心和机器的雪花算法实例。

- **场景四：测试代码与运行结果**
  - **描述**：讲师在 `DistributedIdTest.java` 文件中，编写了测试代码，分别调用 `autoincrementId`、`snowflake` 和 `snowflakeFromServer` 方法。随后，点击运行按钮，终端输出了三种ID的值，成功验证了系统的功能。输出结果包括：
    - 自增ID：`62`
    - 本地雪花ID：`51520929715567616`
    - 服务端雪花ID：`51520929712365312`
  - **演示效果**：通过终端输出，直观地展示了三种ID生成方式的差异和正确性，增强了课程的说服力。

- **场景五：PPT辅助说明**
  - **描述**：在演示代码的同时，讲师切换到PPT，用以辅助说明。PPT清晰地列出了三种ID获取方式的代码示例，与代码演示内容完全一致，帮助观众更好地理解和记忆。

---

以上是根据视频画面进行的结构化分析，旨在提供一个清晰、准确的技术课程概览。
