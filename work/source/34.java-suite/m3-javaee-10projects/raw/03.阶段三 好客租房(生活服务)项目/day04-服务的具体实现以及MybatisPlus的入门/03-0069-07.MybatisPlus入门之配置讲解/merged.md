# 07.MybatisPlus入门之配置讲解

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day04-服务的具体实现以及MybatisPlus的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day04-服务的具体实现以及MybatisPlus的入门\07.MybatisPlus入门之配置讲解【海量资源尽在 ubkz.com】.mp4
- 时长 2分54秒（音频 174s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 那么下面我们来看一下配置这个是什么意思呢那么在前面我们在使用mybattiesplastic插件的时候我们基本上使用的是零配置的方式就是说我没有写任何的配置文件当然了 除了Spring中的DataSource的配置之外它是不是就是零配置 OK但是有些时候我们需要对mybatties注意是对mybatties做一些
[00:26] 这个配置的时候那么我们是不是就要使用它原生的一些配置方式了OK那么就会有几个疑问就是比如说像mybatties的全局的配置文件还有一些我们的map的一些XML文件对吧那么这个又在哪里配置呢我们来看一下那么在我们的applicationapplication文件中我们可以通过两个配置项一个是要做mybatties plus.config location来指定mybatties的一个全局的配置文件
[00:56] 那么还有一个呢是通过这个mybidx-plusmapllocations然后呢指定啊指定我们那个mapl的一个配置文件那么指定这俩那么我相信熟悉mybidx同学应该就并不陌生了对吧这两个呢我就不做演示了大家应该能够懂这个意思能够明白这个意思好那么他们还会有一些其他的配置项那么就需要大家去阅读一下这个官方的一个
[01:23] 这个文档了我们来一起可以看一下那么在官方的这个文档中那么他呢可以告诉我们有很多的配置包括像这个什么config location那么这个是不是就前面我们说说的这个mybidx全局的那个配置文件对吧ok那么在这个位置他给出两种配置方式一种是使用sprintboot这种方式的配置一种是sprint原生的这种sprintmvc这种方式一种配置ok好
[01:51] 下面的这个呢是配置的Mapper的配置文件刚刚呢其实我们也看过了对吧有两种配置还是Spring Boot和spring mvc的啊这种配置那么呢我们来看一下那么像这个type-alerts-package就是我们那个别名的扫描包对吧那么熟悉mybidis的同学这个应该是比较熟悉的一个配置项好然后呢还有一些其他的就不一一去讲了啊有很多的一些配置啊那么它的配置项呢有这么多下面呢还有一些
[02:20] 进阶这个阶段的一些配置这个其实就是我们MyBetis全局配置文件中的一些配置项包括像这种驼分的这种自动映射对吧还有像这个是我们的颜色加载的一些配置项那么它的配置的一些内容都在这那么有需要的一些同学到这个里面去做一些阅读好那么关于MyBetis Plus的一些如何配置原生的一些
[02:48] 这个配置配置项那么我们就讲到这里好那么配置项我们就讲到这里了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 MyBatis-Plus 框架中用于自定义配置的 MyBatis 原生配置文件，包括 configLocation、mapperLocations、typeAliasesPackage 等核心配置项及其在 Spring Boot 和 Spring MVC 中的写法。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 内容：PDF 文档页面，标题为“2.6、配置”，介绍在 MyBatis-Plus 中自定义配置需使用 MyBatis 原生配置文件。
- 代码片段：
  ```
  # 指定全局配置文件
  mybatis-plus.config-location = classpath:mybatis-config.xml
  # 指定Mapper.xml文件
  mybatis plus.Mapper locations = classpath:mybatis/*.xml
  ```

画面 2：
- 内容：网页文档，标题为“基本配置”，展示 MyBatis-Plus 的 configLocation 配置。
- 代码片段：
  ```
  mybatis-plus:
    config-location: classpath:mybatis-config.xml
  ```

画面 3：
- 内容：网页文档，展示 MyBatis-Plus 的 mapperLocations 配置。
- 代码片段：
  ```
  mybatis-plus:
    Mapper-locations: classpath:mybatis/*.xml
  ```

画面 4：
- 内容：网页文档，展示 MyBatis-Plus 的 mapperLocations 配置，与画面 3 内容相同。

画面 5：
- 内容：网页文档，展示 MyBatis-Plus 的 typeAliasesPackage 配置。
- 代码片段：
  ```
  mybatis-plus:
    type-aliases-package: com.baomidou.mybatisplus.samples.quickstart.entity
  ```

画面 6：
- 内容：网页文档，展示 MyBatis-Plus 的 typeAliasesPackage 配置，与画面 5 内容相同。

画面 7：
- 内容：网页文档，展示 MyBatis-Plus 的 typeAliasesPackage 配置，与画面 5 内容相同。

画面 8：
- 内容：网页文档，展示 MyBatis-Plus 的 typeHandlersPackage 配置。
- 代码片段：
  ```
  mybatis-plus:
    type-handlers-package: com.baomidou.mybatisplus.samples.quickstart.handler
  ```

画面 9：
- 内容：网页文档，展示 MyBatis-Plus 的 typeEnumsPackage 配置。
- 代码片段：
  ```
  mybatis-plus:
    type-enums-package: com.baomidou.mybatisplus.samples.quickstart.enums
  ```

画面 10：
- 内容：网页文档，展示 MyBatis-Plus 的 checkConfigLocation 配置。
- 代码片段：
  ```
  mybatis-plus:
    check-config-location: false
  ```

画面 11：
- 内容：网页文档，展示 MyBatis-Plus 的 configurationProperties 配置。
- 代码片段：
  ```
  mybatis-plus:
    configuration-properties: classpath:mybatis/config.properties
  ```

画面 12：
- 内容：网页文档，展示 MyBatis-Plus 的 aggressiveLazyLoading 配置。
- 代码片段：
  ```
  mybatis-plus:
    configuration:
      aggressive-lazy-loading: true
  ```

画面 13：
- 内容：网页文档，展示 MyBatis-Plus 的 autoMappingUnknownColumnBehavior 配置。
- 代码片段：
  ```
  mybatis-plus:
    configuration:
      auto-mapping-unknown-column-behavior: none
  ```

画面 14：
- 内容：PDF 文档页面，与画面 1 内容相同，展示 MyBatis-Plus 的配置相关代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
见上文第 2 点。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

