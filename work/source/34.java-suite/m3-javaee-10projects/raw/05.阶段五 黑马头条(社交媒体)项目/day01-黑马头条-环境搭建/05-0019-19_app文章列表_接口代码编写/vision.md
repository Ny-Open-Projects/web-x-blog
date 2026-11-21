# 画面线理解：19_app文章列表_接口代码编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\19_app文章列表_接口代码编写【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:35, 01:16, 01:49, 03:00, 04:36, 05:16, 06:08, 06:35, 07:07, 08:59, 10:09, 11:32, 12:11
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 12:37:26

1) 这一组画面整体在讲什么（一句话）：
演示一个 Spring Boot 项目中，如何定义文章首页 DTO、Controller 接口、Service 接口及其实现类，构建文章加载功能的分页和加载更多逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示项目结构，选中 `heima-leadnews-article` 模块，准备进行开发。
画面 2：打开 `MysqlConfig.java`，展示 Spring Boot 的配置类，使用 `@Configuration` 和 `@ComponentScan` 注解。
画面 3：切换到 PPT 页面，标题为“7.3 article服务功能开发”，并展示 `ArticleHomeDto` 的定义。
画面 4：在 `ArticleHomeDto.java` 中，展示 DTO 类的字段定义，包括 `provinceId`、`cityId`、`countyId`、`maxBehotTime`、`minBehotTime`、`size`、`tag` 等。
画面 5：右键点击 `ArticleHomeDto.java`，弹出菜单，选择“Run All Features in java”等选项。
画面 6：在 `ArticleHomeControllerApi.java` 中，定义了三个方法：`load`、`loadMore`、`loadNew`，并标注了注释。
画面 7：在 `ArticleHomeControllerApi.java` 中，对 `load` 方法的参数和返回值进行注释说明。
画面 8：在 `ArticleHomeController.java` 中，实现 `ArticleHomeControllerApi` 接口，三个方法均返回 `null`。
画面 9：在 `ArticleHomeController.java` 中，为 `load` 方法添加 `@RequestMapping("/api/v1/article")` 注解。
画面 10：在 `ArticleHomeController.java` 中，为 `load` 方法添加 `@Autowired` 注解，注入 `AppArticleService`。
画面 11：在 `ArticleHomeController.java` 中，为 `load` 方法添加 `@RequestMapping("/load")` 注解。
画面 12：在 `ArticleHomeController.java` 中，为 `loadMore` 和 `loadNew` 方法添加 `@RequestMapping("/loadmore")` 和 `@RequestMapping("/loadnew")` 注解。
画面 13：在 `AppArticleService.java` 中，定义了 `load` 方法，参数为 `ArticleHomeDto` 和 `Short type`。
画面 14：在 `AppArticleServiceImpl.java` 中，实现 `load` 方法，返回 `null`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2：
```java
package com.heima.article.config;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration
@ComponentScan("com.heima.common.mysql.core")
public class MysqlConfig {
}
```

画面 3：
```java
mysql初始化扫描配置类com.heima.article.config.MysqlConfig

@Configuration
@ComponentScan("con.heima.common.mysql.core")
public class MysqlConfig {
}
```

画面 3：
```java
public class ArticleHomeDto {
    // 省市
    Integer provinceId;
    // 市区
    Integer cityId;
    // 区县
    Integer countyId;
    // 最大时间
    Date maxBehotTime;
    // 最小时间
    Date minBehotTime;
    // 分页大小
    Integer size;
    // 搜索范围，比如频道
    String tag;
}
```

画面 6：
```java
public interface ArticleHomeApi {
    // 加载首页文章
    @Param dto
    @Return
    public ResponseResult load(ArticleHomeDto dto);

    // 加载更多
    @Param dto
    @Return
    public ResponseResult loadMore(ArticleHomeDto dto);

    // 加载最新的文章信息
    @Param dto
    @Return
    public ResponseResult loadNew(ArticleHomeDto dto);
}
```

画面 8：
```java
public class ArticleHomeController implements ArticleHomeControllerApi {
    @Override
    public ResponseResult load(ArticleHomeDto dto) {
        return null;
    }

    @Override
    public ResponseResult loadMore(ArticleHomeDto dto) {
        return null;
    }

    @Override
    public ResponseResult loadNew(ArticleHomeDto dto) {
        return null;
    }
}
```

画面 9：
```java
@RequestMapping("/api/v1/article")
public class ArticleHomeController implements ArticleHomeControllerApi {
    @Override
    public ResponseResult load(ArticleHomeDto dto) {
        return null;
    }
}
```

画面 10：
```java
@Autowired
private AppArticleService appArticleService;
```

画面 11：
```java
@RequestMapping("/load")
@Override
public ResponseResult load(ArticleHomeDto dto) {
    return appArticleService.load(dto, "1");
}
```

画面 12：
```java
@RequestMapping("/loadmore")
@Override
public ResponseResult loadMore(ArticleHomeDto dto) {
    return appArticleService.load(dto, "1");
}

@RequestMapping("/loadnew")
@Override
public ResponseResult loadNew(ArticleHomeDto dto) {
    return appArticleService.load(dto, "2");
}
```

画面 13：
```java
public interface AppArticleService {
    /**
     * type 1 加载更多 2 加载最新
     * @param dto
     * @param type
     * @return
     */
    ResponseResult load(ArticleHomeDto dto, Short type);
}
```

画面 14：
```java
public class AppArticleServiceImpl implements AppArticleService {
    @Override
    public ResponseResult load(ArticleHomeDto dto, Short type) {
        return null;
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 3：
PPT 标题：“7.3 article服务功能开发”
子标题：“(1) 定义dto”
内容：
- (1) load接口
- (2) load_more接口 & load_new接口
- (4) 行为接口
- (7.3.1) 在Konn文件中的校验注解
- (7.3.2) Article服务功能开发
- (7.3.3) 行为接口功能开发

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
