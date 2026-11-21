# 画面线理解：20_app文章列表_业务层实现类代码完成

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\20_app文章列表_业务层实现类代码完成【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:08, 02:09, 03:20, 04:55, 05:46, 07:12, 08:33, 09:57, 11:32, 12:43, 14:11, 15:10, 16:09, 17:26
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 12:38:10

1) 这一组画面整体在讲什么（一句话）：
讲解一个文章推荐系统中，根据用户登录状态和请求参数（如时间范围、分页大小）加载不同文章列表的逻辑，涉及控制器、服务层、线程局部变量和数据映射器的实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示一个用户文章加载的流程图，包含“未登录”、“登录”、“用户设置的频道”三种状态，以及“上拉刷新”、“下拉刷新”、“隐藏需求”等交互说明。
画面2：展示IDEA中ArticleHomeDto类的定义，包含provinceId、cityId、countyId、maxBehotTime、minBehotTime、size、tag等字段。
画面3：展示ArticleHomeService类中load方法的参数校验逻辑，包括对dto参数和时间参数的非空判断。
画面4：展示ArticleHomeService类中对分页参数size的校验逻辑，包括设置默认值20。
画面5：展示对type参数的校验逻辑，包括判断是否为0。
画面6：展示AppThreadLocalUtils类中设置当前线程用户信息的代码。
画面7：展示ArticleHomeService类中获取用户信息并根据用户状态决定加载推荐文章或默认文章的逻辑。
画面8：展示ArticleHomeService类中根据用户是否存在决定加载推荐文章或默认文章的逻辑。
画面9：展示ArticleHomeService类中获取默认文章列表的逻辑。
画面10：展示ArticleHomeService类中获取默认文章列表的逻辑，包含返回ResponseResult。
画面11：展示ArticleHomeService类中获取默认文章列表的逻辑，包含使用apArticleMapper。
画面12：展示ArticleHomeService类中获取默认文章列表的逻辑，包含使用apUserArticleListMapper。
画面13：展示ArticleHomeService类中获取用户文章列表的逻辑，包含判断列表是否为空。
画面14：展示ArticleHomeService类中获取用户文章列表的逻辑，包含根据列表是否为空返回不同结果。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
// 省
Integer provinceId;
// 市
Integer cityId;
// 县
Integer countyId;
// 最大时间
Date maxBehotTime;
// 最小时间
Date minBehotTime;
// 分页大小
Integer size;
// 每页范围，比如频道 20
String tag;
```

画面3：
```java
@Override
public ResponseResult load(ArticleHomeDto dto, Short type) {
    // 参数校验
    if(dto == null) {
        dto = new ArticleHomeDto();
    }
    // 时间校验
    if(dto.getMaxBehotTime() == null) {
        dto.setMaxBehotTime(new Date());
    }
    if(dto.getMinBehotTime() == null) {
        dto.setMinBehotTime(new Date());
    }
    // 分页参数的校验
    Integer size = dto.getSize();
    if(size == null || size <= 0) {
        size = 20;
    }
    dto.setSize(size);
    // 获取用户的信息
    // 判断用户是否存在
```

画面4：
```java
// 类型参数校验
if(type.equals(ArticleConstants.LOADTYPE_LOAD_MORE) && type.equals(ArticleConstants.LOADTYPE_LOAD_MORE)) {
    type = ArticleConstants.LOADTYPE_LOAD_MORE;
}
// 获取用户的信息
AppUser user = AppThreadLocalUtils.getUser();
// 判断用户是否存在
if(user == null) {
    // 存在，已登录，加载推荐的文章
} else {
    // 不存在，未登录，加载默认的文章
}
```

画面6：
```java
package com.heima.utils.threadlocal;

import com.heima.modal.user.pojos.ApUser;

public class AppThreadLocalUtils {
    private final static ThreadLocal<ApUser> userThreadLocal = new ThreadLocal<>();

    // 设置当前线程中的用户
    public static void set(User user) {
        userThreadLocal.set(user);
    }

    // 获取线程中的用户
    public static ApUser getUser() {
        return userThreadLocal.get();
    }
}
```

画面7：
```java
// 获取用户的信息
AppUser user = AppThreadLocalUtils.getUser();
// 判断用户是否存在
if(user == null) {
    // 存在，已登录，加载推荐的文章
} else {
    // 不存在，未登录，加载默认的文章
}
```

画面8：
```java
// 获取用户的信息
AppUser user = AppThreadLocalUtils.getUser();
// 判断用户是否存在
if(user == null) {
    // 存在，已登录，加载推荐的文章
} else {
    // 不存在，未登录，加载默认的文章
}
```

画面9：
```java
// 获取默认文章列表
private List<Article> getDefaultArticle(ArticleHomeDto dto, Short type) {
    return apArticleMapper.loadArticleListByLocation(dto, type);
}
```

画面10：
```java
// 获取默认文章列表
private List<Article> getDefaultArticle(ArticleHomeDto dto, Short type) {
    return apArticleMapper.loadArticleListByLocation(dto, type);
}
```

画面11：
```java
// 获取默认文章列表
private List<Article> getDefaultArticle(ArticleHomeDto dto, Short type) {
    apArticleMapper.loadArticleListByLocation(dto, type);
}
```

画面12：
```java
// 获取默认文章列表
private List<Article> getDefaultArticle(ArticleHomeDto dto, Short type) {
    apUserArticleListMapper.loadArticleListByUser(dto, type);
}
```

画面13：
```java
// 获取用户文章列表
private List<Article> getUserArticle(AppUser user, ArticleHomeDto dto, Short type) {
    List<Article> articleList = apUserArticleListMapper.loadArticleListByUser(user, dto, type);
    if(articleList.isEmpty()) {
        return apArticleMapper.loadArticleListByLocation(dto, type);
    } else {
        return getDefaultArticle(dto, type);
    }
}
```

画面14：
```java
// 获取用户文章列表
private List<Article> getUserArticle(AppUser user, ArticleHomeDto dto, Short type) {
    List<Article> articleList = apUserArticleListMapper.loadArticleListByUser(user, dto, type);
    if(articleList.isEmpty()) {
        return apArticleMapper.loadArticleListByLocation(dto, type);
    } else {
        return getDefaultArticle(dto, type);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：流程图结构：
- “用户”指向“未登录，加载默认的文章列表”
- “用户”指向“登录，加载推荐的文章列表”
- “用户”指向“用户设置的频道进行加载”
- “上拉刷新”指向“加载当前时间之前发布文章”
- “下拉刷新”指向“加载当前时间之后发布文章”
- “隐藏需求”指向“记录当前用户的行为”

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
