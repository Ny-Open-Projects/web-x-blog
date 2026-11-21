# 24-文件服务课程-文件服务开发（文件处理策略_F — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么刚才呢,咱们是已经完成了我们这个本地文件策略处理类,对吧,也就是这个local service MPL这个类的编写。

那么需要注意的一点是什么呢?

我们在进行文件上传还有下载的时候呢,会使用到我们配置文件中的一些配置项。

其实呢,刚才我们在进行这个代码开发的时候呢,也是反复的去查看我们的配置文件,对吧。

也就是说我们的代码呢,跟这个配置项呢,它是息息相关的,是一一对应的。

那么关于本地文件策略处理,对吧,那么我们需要进行这么一个配置啊,在品达下面有个file,对吧,然后type指定成local,这就表示我们使用的是本地策略。

那么为什么这么一配置我们这个本地策略就会出发呢?

就是因为我们在这儿使用的是这么一个什么呢,在我们这个配置类上加了这么一个注解,对吧,叫做conditional on property。

也就是说当我们这个属性啊,按照我们指定的这个值来复职的时候,那么当前这个配置类呢,是不是才会生效。

所以它其实是基于属性的一个这么一个条件注解。

那么什么呢,就是当我们这个品达.file.type给的值呢是local的时候,那么当前这个配置类是不是就会生效。

那么它一生效的话呢,就会把我们这个service对象是不是给我们实力化出来。

但是对应的这里边呢,还有一些这个。

配置文件的加载,对吧,那么这些配置文件的加载。

对应的都是加载我们这块的这个配置,这是local。

好,那么接下来呢,我们继续往下看啊,下一个呢,是关于我们这个fast.dfs的。

也就是说当我们这个文件处理策略呢,选择的是fast.dfs,那么这个时候呢,我们对应的就需要使用这个策略处理类。

那么来进行这个处理。

同样的,这个的玩法呢,跟我们这个local。

是一个大致的思路是一样的。

全都是什么呢,通过一个配置类,对吧。

然后在配置类里面去判断我们设置的配置的这个属性,对吧。

这个type,如果是fast.dfs,那么我们就需要来创建实力化这个fast.dfs service.impl。

好,所以整个这个套路是一样的。

只不过区别是在于哪呢?

我们当前这个呢,要使用它的话,那就是将我们的文件呢,不是上传到我们本地磁盘了。

而是可能是远程的一个什么呢,分布式文件系统,对吧。

也就是fast.dfs。

好,那么咱们先把这个配置类呢,来创建一下。

这个配置类呢,叫做fast.dfs auto-config。

咱们在这个storage,对吧,这个下面,再来创建一个。

好,就这个。

然后呢,这个处理的是什么呢?

就是我们这个,如果说文件处理策略,选择的是fast.dfs,对吧。

这种配置啊。

好,那么,既然它是一个配置类的话呢,我们是不是也需要把这些属性呢,全都加一下啊。

首先一个是configuration,对吧。

configuration,这个需要加一下。

然后呢,再来一个日志的。

然后呢,还要加什么呢?

再来一个enable configuration properties。

同样呢,我们还是要加载配置文件,对吧。

所以说呢,把咱们这个配置属性类呢,给我们加进来。

叫做fileserver properties,对吧。

好。

然后呢,还有一个啊,就是我们这个条件注解,对吧。

conditional,conditional,conditional on property,对吧。

然后呢,在这儿我们来指定啊,这个属性名。

注意这个属性名呢,还是什么呢?

品达.file.type,对吧。

只不过呢,这回呢,我们需要取的值,heaven value,是什么呢?

应该叫做fast.dfs。

好。

那么如果说我们这个地方,咱们这儿,

这个type,对吧。

如果写的是fast.dfs,你看咱们现在其实配置的就是这个,对吧。

fast.dfs。

那么这个时候呢,我们当前这个配置类,是不是就会生效。

那这样的话呢,我们是不是也需要在这里边来创建一个类。

这个类呢,就是负责处理什么呢?

处理我们这个文件策略啊,是fast.dfs啊。

这种时候会使用它。

也就是它是fast.dfs的一个什么呢?

呃,文件,文件策略处理类。

处理类。

好。

那接下来呢,我们需要把它来创建一下。

好。

咱们在这儿来,public class,对吧。

这个类名呢,就叫做什么呢?

fast.dfs service,service,好,impl,对吧。

别忘了,让它去继承什么呢?

咱们那个抽象的,对吧。

abstract file strategy。

好。

这里边呢,它肯定要报错了。

因为在这个抽象类里边,我们是不是有两个抽象方法,需要这个子类呢,来实现啊。

就是这两个方法,文件上传还有删除。

这个呢,是文件上传。

咱们就叫上传文件吧。

好。

这个呢,是删除文件。

OK。

咱们现在呢,就已经按照我们前面跟这个local处理方式是一样的。

只不过是创建出来的是一个fast.dfs这种文件处理策略。

那么对应的呢,有这么一个配置类。

然后呢,这个地方呢,是我们这个service类。

当然了,这个地方不要忘记了。

不要忘了啊。

需要给这个类呢,加一个service注解。

否则的话呢,那么我们这个,你不加这个注解的话呢,这个类呢,是不会被实力化的。

因为我们全都是基于Spring这套平台,对吧。

所以说呢,需要加上这个service注解。

那么如果说我们配置的这个type呢,设置的是fast.dfs,当前配置类生效。

那这样的话呢,实力化出来的就是这个service。

这样的话呢,我们就需要去实现什么呢?

如果是文件处理策略选择的这个tab。

那么这个是fast.dfs,它的文件上传还有删除应该是如何处理。

很显然应该是跟我们本地处理方式是完全不一样的。

好,咱们先把这个大体的这个类的结构架子搭起来。

一会儿呢,我们再去实现具体的这个文件上传,还有这个删除的具体细节。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面截图，对技术课程内容进行的结构化中文输出。

---

### 1) 视频摘要

本视频课程聚焦于一个名为“pinda”的Java项目中的文件服务模块，特别是其基于FastDFS的存储策略实现。讲师通过IDE（IntelliJ IDEA）和配置中心（Nacos）的界面，详细讲解了如何通过Spring Boot的自动配置机制，动态选择并实现不同的文件存储策略。核心内容包括：
- **项目结构与配置**：展示了项目的目录结构和关键配置文件（如 `application.yml`）。
- **FastDFS策略实现**：重点讲解了 `FastDfsServiceImpl` 类，它继承自抽象策略类 `AbstractFileStrategy`，负责处理FastDFS存储的文件上传与删除。
- **自动配置类**：创建了 `FastDfsAutoConfigure` 类，通过 `@Configuration`、`@EnableConfigurationProperties` 和 `@ConditionalOnProperty` 注解，实现根据配置属性 `pinda.file.type` 的值（如 `FAST_DFS`）来自动装配 `FastDfsServiceImpl`。
- **代码演示**：在IDE中逐步编写和展示 `FastDfsAutoConfigure` 和 `FastDfsServiceImpl` 的代码，并在Nacos中配置了FastDFS的连接参数。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取视频的实际时间戳，以下章节结构是根据画面内容和逻辑顺序推断的：

- **00:00 - 00:30**：课程开场，展示项目整体结构和文件服务模块的PPT大纲，引出本节主题：FastDFS存储策略的实现。
- **00:30 - 01:00**：讲解 `FastDfsServiceImpl` 类的作用和代码结构，展示其在IDE中的代码片段。
- **01:00 - 01:30**：演示如何在Nacos配置中心为FastDFS设置连接参数，如 `urlPrefix`、`bucket-name` 和 `endpoint`。
- **01:30 - 02:00**：讲解如何创建自动配置类 `FastDfsAutoConfigure`，并使用 `@Configuration`、`@EnableConfigurationProperties` 和 `@ConditionalOnProperty` 注解。
- **02:00 - 02:30**：在 `FastDfsAutoConfigure` 类中编写代码，通过 `@ConditionalOnProperty` 注解，使 `FastDfsServiceImpl` 在配置属性 `pinda.file.type` 的值为 `FAST_DFS` 时被自动装配。
- **02:30 - 03:00**：展示 `FastDfsServiceImpl` 的完整代码，包括 `uploadFile` 和 `deleteFile` 方法的实现逻辑。
- **03:00 - 03:30**：总结本节内容，强调通过配置驱动实现策略切换的灵活性。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 图表内容

- **PPT大纲**：
  - 5.1 环境搭建
  - 5.2 文件处理策略
    - 5.2.1 FileStrategy
    - 5.2.2 AbstractFileStrategy
    - 5.2.3 LocalServiceImpl
    - 5.2.4 FastDfsServiceImpl
  - 5.3 AliServiceImpl
  - 5.4 接口开发：上传附件
  - 5.5 接口开发：根据业务类型/业务id删除附件
  - 5.6 接口开发：根据业务类型/业务id打包下载

#### 代码关键内容

- **配置文件 `application.yml`**：
  ```yaml
  database: pd_files
  nginx:
    ip: ${spring.cloud.client.ip-address} # 正式环境需要将ip设置成nginx对应的公网ip
    port: 10000
    # 正式环境需要将该ip设置成nginx对应的公网端口
  file:
    type: LOCAL
    local:
      urlPrefix: http://${pinda.nginx.ip}:${pinda.nginx.port}
      bucket-name: oss-file-service
      endpoint: D:\upload\files
  ```

- **`FastDfsServiceImpl` 类（代码片段）**：
  ```java
  package com.iteima.pinda.file.storage;

  import com.github.tobato.fastdfs.domain.fdfs.StorePath;
  import com.github.tobato.fastdfs.service.FastFileStorageClient;
  import com.iteima.pinda.file.domain.FileDeleteDO;
  import com.iteima.pinda.file.entity.File;
  import com.iteima.pinda.file.properties.FileServerProperties;

  // ... 其他代码 ...
  ```

- **`LocalServiceImpl` 类（代码片段）**：
  ```java
  @Service
  public class LocalServiceImpl extends AbstractFileStrategy {
      private void buildClient() {
          properties = fileProperties.getLocal();
      }

      @Override
      public void uploadFile(File file, MultipartFile multipartFile) throws Exception {
          buildClient();
          String endpoint = properties.getEndpoint();
          // ... 上传逻辑 ...
      }
  }
  ```

- **`FastDfsAutoConfigure` 类（代码片段）**：
  ```java
  @Configuration
  @EnableConfigurationProperties(FileServerProperties.class)
  @ConditionalOnProperty(name = "pinda.file.type", havingValue = "FAST_DFS")
  public class FastDfsAutoConfigure {
      // ... 其他代码 ...
  }
  ```

- **`FastDfsServiceImpl` 类（完整结构）**：
  ```java
  @Service
  public class FastDfsServiceImpl extends AbstractFileStrategy {
      // ... 上传文件方法 ...
      @Override
      public void uploadFile(File file, MultipartFile multipartFile) throws Exception {
          // ... 上传逻辑 ...
      }

      // ... 删除文件方法 ...
      @Override
      public void deleteFile(FileDeleteDO fileDeleteDO) {
          // ... 删除逻辑 ...
      }
  }
  ```

---

### 4) 关键场景与演示描述

- **场景一：项目结构与配置展示**
  - **描述**：讲师在IDE中展示了项目的目录结构，重点指向 `storage` 包下的 `strategy` 子包，其中包含 `AbstractFileStrategy`、`LocalServiceImpl` 和 `FastDfsServiceImpl` 等类。同时，展示了 `application.yml` 配置文件，其中定义了FastDFS的连接参数。

- **场景二：Nacos配置中心演示**
  - **描述**：讲师切换到Nacos配置中心，展示了 `pd-file-server.yml` 配置文件的内容，其中包含了FastDFS的配置项，如 `type: FAST_DFS`、`urlPrefix`、`bucket-name` 和 `endpoint`。讲师强调了这些配置项在实际项目中的作用。

- **场景三：自动配置类创建与注解应用**
  - **描述**：讲师在IDE中创建了 `FastDfsAutoConfigure` 类，并逐步添加了 `@Configuration`、`@EnableConfigurationProperties` 和 `@ConditionalOnProperty` 注解。通过 `@ConditionalOnProperty` 注解，讲师演示了如何根据配置属性 `pinda.file.type` 的值来决定是否加载 `FastDfsServiceImpl`。

- **场景四：FastDfsServiceImpl 代码实现**
  - **描述**：讲师在IDE中编写了 `FastDfsServiceImpl` 类的代码，该类继承自 `AbstractFileStrategy`。讲师展示了 `uploadFile` 方法的实现逻辑，包括调用 `buildClient()` 方法获取配置，并使用 `endpoint` 进行文件上传。同时，也展示了 `deleteFile` 方法的实现。

- **场景五：代码调试与错误处理**
  - **描述**：在编写 `FastDfsServiceImpl` 时，讲师遇到了编译错误，IDE提示 `AbstractMethodError`。讲师通过检查代码和注解，最终解决了问题，确保了 `FastDfsServiceImpl` 能够正确继承并实现 `AbstractFileStrategy` 中的方法。

---

以上是根据视频画面截图整理出的技术课程内容结构化输出。
