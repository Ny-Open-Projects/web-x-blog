# 画面线理解：07.MybatisPlus入门之配置讲解

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day04-服务的具体实现以及MybatisPlus的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day04-服务的具体实现以及MybatisPlus的入门\07.MybatisPlus入门之配置讲解【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:23, 01:24, 01:51, 01:54, 02:01, 02:03, 02:11, 02:13, 02:14, 02:15, 02:30, 02:33, 02:35, 02:43
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:42:37

1) 这一组画面整体在讲什么（一句话）：
讲解 MyBatis-Plus 框架中用于自定义配置的 MyBatis 原生配置文件，包括 configLocation、mapperLocations、typeAliasesPackage 等核心配置项及其在 Spring Boot 和 Spring MVC 中的写法。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 内容：PDF 文档页面，标题为“2.6、配置”，介绍在 MyBatis-Plus 中自定义配置需使用 MyBatis 原生配置文件。
- 代码片段：
  ```
  # 指定全局配置文件
  mybatis-plus.config-location = classpath:mybatis-config.xml
  # 指定mapper.xml文件
  mybatis plus.mapper locations = classpath:mybatis/*.xml
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
    mapper-locations: classpath:mybatis/*.xml
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
