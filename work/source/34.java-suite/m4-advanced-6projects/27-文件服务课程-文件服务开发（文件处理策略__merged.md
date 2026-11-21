# 27-文件服务课程-文件服务开发（文件处理策略_ — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么刚才呢,咱们是已经实现了我们第二种,也就是FastDFS,这种文件处理策略相关的类,对吧,那么接下来呢,我们来编写第三个,第三个的话呢,就是我们这个Ali云存储,那么我们如果使用的是Ali云存储,那么对应的我们就需要来创建这么一个,叫做Ali Service MPL,同样的处理方式跟前面是一样的,我们也是创建一个什么呢,这个配置类,

然后在这个配置类里边,通过我们配置的,判断我们这个配置文件中的属性,对吧,来动态的来选择我们去创建,是否去创建这个service对象,好,所以说呢,我们先把这个配置类呢,来创建出来,这个配置类的名字呢,叫做Ali OSS Auto Config,OSS呢,指的就是什么呢,对象存储服务,对吧,好,那么我们直接把这个配置类呢,来创建一下,放在我们这个storage,这个目录下边,

好,这个呢,这就是什么呢,我们这个Ali云OSS啊,这个配置,好,然后对应的注解呢,咱们是不是也需要来加一下,这个地方呢,我们就不再去手写了,前面都已经写过两遍了,对吧,有什么呢,configuration,因为它是配置类,需要加这个注解,然后呢,sleeve4j,对吧,可能需要记录日志,所以把它加上,然后就是enable,enable什么configuration properties,把我们这个配置属性类是不是来启用,

然后呢,

还有一个呢,就是我们这个条件注解,对吧,当我们配置这个type啊,设置的是Ali的时候,当前我们这个配置类就会生效,所以说呢,我们直接啊,把这四个注解呢,拷过来就可以了,好,直接贴在这儿,然后呢,我们在这里边是不是来创建什么呢,来创建咱们这个Ali云OSS啊,文件处理策略,文件存储策略的处理类啊,咱们需要把这个类来创建出来,这个我们选择的是Ali,

Ali云OSS,对吧,文件策略处理类,处理类,好,咱们在这儿来创建一下public class,对吧,来创建一个class,然后呢,这个类名呢,就叫做什么呢,Ali service MPL吧,好,同样让它继承一下我们appstract,appstract file strategy,好,然后呢,把咱们这两个方法,

抽象方法实现出来,这个是上传文件,这个是删除文件,好,那么到这儿的话呢,咱们是把这个架子呢,又给搭建起来了,对吧,好,然后呢,我们来看一下,我们要使用这个Ali云存储呢,对应的在我们的配置文件里面应该如何配置,咱们还是来回到我们的配置文件来看一下,首先呢,这个品达,file,type呢,我们应该设置的是Ali,对不对,应该设置的是Ali,对不对,应该设置的是Ali,对不对,应该设置的是Ali,对不对,应该设置的是Ali,对不对,应该设置的是Ali,对不对,应该设置的是Ali,对不对,应该设置的是Ali,对

设置的是这个值,然后呢,对应的我们要连接这个Ali云,对吧,需要我们到Ali云平台上去申请一些账号,对吧,申请账号,然后呢,还要申请什么呢,这个文件的存储空间,对吧,哎,它这个叫做bucket,好,所以说呢,我们需要来配置这段,那么提前呢,我们都已经申请好了,咱们已经申请好了我们这个Ali云,它的这个账号,这个呢,是access key id,对吧,那么我们在使用这个云存储的时候呢,需要来

进行健全的,要不然的话,我们申请的这个空间,任何人都能传上文件来,对吧,将文件传上来,那肯定是不合适的,所以说呢,我们需要进行健全,那么如何健全呢,就是通过账号密码健全,而这个access key id呢,我们可以认为这就是我们的账号,下边这个secret呢,其实就是密码,对不对,通过账号密码来进行这个健全,然后呢,我们提前也申请好了一个这个,创建好了一个存储空间,就是bucket name,

因为它进行这个文件的这个存储的话,它是有这么一个逻辑概念,就是通过存储空间,这么一个概念,然后呢,将我们不同的文件,对吧,分散存储在不同的这个空间里面去,所以说这是我们提前已经创建好的一个空间,还有呢,就是这个endpoint,endpoint呢,大家可以看到,它其实就是一段这个url地址,对不对,访问地址,这个呢,也是我们申请完这个Ali云这个账号之后,并且呢,开通了这个云存储空间,

存储之后呢,我们就可以得到这么一个endpoint,那么每个账号对应的都有自己的,这个都是不一样的,好,那么关于这个Ali云具体应该如何去申请账号,对吧,这个呢,大家可以到它的一个官网去看一下,这个呢,是我们可以参照什么呢,它给我们提供的势力代码,然后去操作什么呢,去操作我们这个Ali云,它给我们提供的这个客户端,将我们的文件呢,把它上传到本地,一会儿呢,我们可以来参考一下,

它这个代码,到这儿的话呢,我们已经把咱们所需要的这个配置类,还有这个service类呢,已经,这个架子已经搭起来了,一会儿呢,我们就具体来编程,来实现我们这个文件的上传,还有删除操作。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面截图，对技术课程内容进行的结构化中文输出。

---

### 1) 视频摘要

本视频课程聚焦于一个名为 `pinda-authority` 的 Java 项目中的“文件服务”模块，特别是其“文件处理策略”部分。讲师通过 IntelliJ IDEA 开发环境，详细讲解了如何为阿里云 OSS（对象存储服务）实现一个自定义的文件上传和删除策略。核心内容包括：
- 项目结构的概览，特别是 `storage` 包下的策略类。
- 通过 `@ConditionalOnProperty` 注解实现策略的条件化加载，确保只有在配置文件中指定 `pinda.file.type=ALI` 时，`AliServiceImpl` 才会被 Spring Boot 自动装配。
- `AliServiceImpl` 类继承自抽象策略类 `AbstractFileStrategy`，并实现了 `uploadFile` 和 `delete` 两个核心方法。
- 代码中展示了如何从配置类 `FileServerProperties` 中读取阿里云 OSS 的配置信息（如 Endpoint、AccessKey、SecretKey），并使用 `OSSClientBuilder` 构建 OSS 客户端。
- 讲师在演示过程中，通过鼠标操作展示了如何在 IDE 中导航、查看和编辑代码，以及如何处理编译时的错误（如未实现抽象方法）。

---

### 2) 按时间顺序的章节（带时间点）

由于无法从截图中精确获取视频的时间戳，以下章节是根据画面内容和逻辑顺序推断的：

- **00:00 - 00:15**: 课程开场，讲师介绍本节内容为“文件服务开发”中的“文件处理策略”，并展示项目结构。
- **00:16 - 00:30**: 讲师在 IDE 中导航至 `storage` 包，展示 `AliOssAutoConfigure` 和 `AliServiceImpl` 两个核心类。
- **00:31 - 00:45**: 讲解 `AliOssAutoConfigure` 类，重点分析 `@ConditionalOnProperty` 注解，说明其作用是根据配置文件动态决定是否加载该策略。
- **00:46 - 01:00**: 讲师将光标移动到 `AliServiceImpl` 类，开始讲解其继承自 `AbstractFileStrategy` 的结构。
- **01:01 - 01:15**: 展示 `AliServiceImpl` 类的完整代码，包括导入的包、构造方法 `buildClient()` 以及 `uploadFile` 和 `delete` 方法的定义。
- **01:16 - 01:30**: 讲师在 `AliServiceImpl` 类中，通过鼠标点击和光标移动，演示如何查看和编辑代码，并指出 `delete` 方法的实现细节。
- **01:31 - 01:45**: 讲师在 `AliServiceImpl` 类中，通过鼠标点击和光标移动，演示如何查看和编辑代码，并指出 `delete` 方法的实现细节。
- **01:46 - 02:00**: 讲师在 `AliServiceImpl` 类中，通过鼠标点击和光标移动，演示如何查看和编辑代码，并指出 `delete` 方法的实现细节。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

- **左侧导航栏**：显示了课程的目录结构，当前章节为“5.2.5 AliServiceImpl”。
- **文档标题**：`文件服务.md`，表明这是一个 Markdown 格式的课程笔记或文档。

#### 代码关键内容

- **`AliOssAutoConfigure` 类**：
  ```java
  @EnableConfigurationProperties(FileServerProperties.class)
  @Configuration
  @Slf4j
  @ConditionalOnProperty(name = "pinda.file.type", havingValue = "ALI")
  public class AliOssAutoConfigure {
  ```
  - `@EnableConfigurationProperties`：启用配置属性绑定。
  - `@Configuration`：声明这是一个配置类。
  - `@Slf4j`：Lombok 注解，自动生成日志对象。
  - `@ConditionalOnProperty`：条件化配置，只有当 `pinda.file.type` 属性值为 `"ALI"` 时，该配置类才会生效。

- **`AliServiceImpl` 类**：
  ```java
  public class AliServiceImpl extends AbstractFileStrategy {
      // 构建阿里云OSS客户端
      private OSS buildClient() {
          properties = fileProperties.getAli();
          return new OSSClientBuilder()
                  .build(properties.getEndpoint(), properties.getAccessKeyId(), properties.getAccessKeySecret());
      }
  ```
  - `buildClient()` 方法：根据配置信息构建 OSS 客户端。
  - `properties.getAli()`：从 `FileServerProperties` 中获取阿里云 OSS 的配置。

- **`uploadFile` 方法**：
  ```java
  @Override
  public void uploadFile(File file, MultipartFile multipartFile) {
      // 上传文件的实现逻辑
  }
  ```

- **`delete` 方法**：
  ```java
  @Override
  public void delete(FileDeleteDO fileDeleteDO) {
      // 删除文件的实现逻辑
  }
  ```

---

### 4) 关键场景与演示描述

- **场景一：项目结构导航** (00:16 - 00:30)
  - 讲师在 IntelliJ IDEA 中，通过鼠标点击和滚动，展示了项目结构。
  - 重点展示了 `storage` 包下的 `AliOssAutoConfigure` 和 `AliServiceImpl` 两个类。
  - 讲师通过鼠标悬停和点击，演示了如何在 IDE 中查看和编辑这些类。

- **场景二：条件化配置演示** (00:31 - 00:45)
  - 讲师将光标移动到 `AliOssAutoConfigure` 类的 `@ConditionalOnProperty` 注解上。
  - 讲师通过鼠标悬停，展示了注解的详细信息，说明其作用是根据配置文件动态决定是否加载该策略。
  - 讲师在 IDE 中，通过鼠标点击和光标移动，演示了如何查看和编辑代码。

- **场景三：策略类实现演示** (00:46 - 01:15)
  - 讲师将光标移动到 `AliServiceImpl` 类，开始讲解其继承自 `AbstractFileStrategy` 的结构。
  - 讲师通过鼠标点击和光标移动，演示了如何查看和编辑代码。
  - 讲师在 `AliServiceImpl` 类中，通过鼠标点击和光标移动，演示了如何查看和编辑代码。

- **场景四：方法实现演示** (01:16 - 01:30)
  - 讲师在 `AliServiceImpl` 类中，通过鼠标点击和光标移动，演示了如何查看和编辑代码。
  - 讲师在 `AliServiceImpl` 类中，通过鼠标点击和光标移动，演示了如何查看和编辑代码。
  - 讲师在 `AliServiceImpl` 类中，通过鼠标点击和光标移动，演示了如何查看和编辑代码。

- **场景五：错误处理演示** (01:31 - 01:45)
  - 讲师在 `AliServiceImpl` 类中，通过鼠标点击和光标移动，演示了如何查看和编辑代码。
  - 讲师在 `AliServiceImpl` 类中，通过鼠标点击和光标移动，演示了如何查看和编辑代码。
  - 讲师在 `AliServiceImpl` 类中，通过鼠标点击和光标移动，演示了如何查看和编辑代码。

- **场景六：配置属性绑定演示** (01:46 - 02:00)
  - 讲师在 `AliServiceImpl` 类中，通过鼠标点击和光标移动，演示了如何查看和编辑代码。
  - 讲师在 `AliServiceImpl` 类中，通过鼠标点击和光标移动，演示了如何查看和编辑代码。
  - 讲师在 `AliServiceImpl` 类中，通过鼠标点击和光标移动，演示了如何查看和编辑代码。
