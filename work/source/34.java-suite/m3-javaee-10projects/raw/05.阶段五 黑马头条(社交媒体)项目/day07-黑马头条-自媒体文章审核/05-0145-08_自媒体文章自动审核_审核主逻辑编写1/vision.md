# 画面线理解：08_自媒体文章自动审核_审核主逻辑编写1

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day07-黑马头条-自媒体文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day07-黑马头条-自媒体文章审核\08_自媒体文章自动审核_审核主逻辑编写1【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:13, 00:31, 01:29, 02:26, 03:05, 03:33, 04:35, 05:21, 06:04, 06:30, 07:02, 07:49, 08:38, 09:54
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:20:34

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中为一个媒体文章审核服务编写 Java 代码，包括定义接口、实现类、使用 MyBatis Mapper 和条件判断逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示一个流程图，包含“标题与内容是否匹配”、“审核文本”、“审核图片”、“发布时间是否大于当前时间”等判断节点，以及“人工审核拒绝”和“通过”等分支。
画面 2: 展示 IntelliJ IDEA 项目结构，选中了 `heima-leadnews-media` 模块。
画面 3: 展示 `ReviewMediaArticleService` 接口定义，包含 `autoReviewArticleByMedia(Integer newsId)` 方法。
画面 4: 展示 `ReviewMediaArticleServiceImpl` 类的开始部分，包含 `@Service` 注解和 `@Autowired` 注解。
画面 5: 展示 `ReviewMediaArticleServiceImpl` 类中定义 `private WalleMapper walleMapper;` 字段。
画面 6: 展示 `ReviewMediaArticleServiceImpl` 类中 `public void autoReviewArticleByMedia(Integer newsId)` 方法的开始部分。
画面 7: 展示 `ReviewMediaArticleServiceImpl` 类中 `if (walle != null) { ... }` 条件判断语句。
画面 8: 展示 `ReviewMediaArticleServiceImpl` 类中 `if (walle != null) { ... }` 条件判断语句，其中包含 `if (walle.getStatus() == 1) { reviewSuccessSaveAll(walle); }`。
画面 9: 展示 `ReviewMediaArticleServiceImpl` 类中 `private void reviewSuccessSaveAll(Walle walle) { ... }` 方法的开始部分。
画面 10: 展示 `ReviewMediaArticleServiceImpl` 类中 `private void reviewSuccessSaveAll(Walle walle) { ... }` 方法的注释部分。
画面 11: 展示 `ReviewMediaArticleServiceImpl` 类中 `if (walle.getStatus() == 8 && walle.getPublishtime() != null && walle.getPublishtime().getTime() > new Date().getTime()) { ... }` 条件判断语句。
画面 12: 展示 `ReviewMediaArticleServiceImpl` 类中 `reviewSuccessSaveAll(Walle walle)` 方法的调用。
画面 13: 展示 `ReviewMediaArticleServiceImpl` 类中 `if (walle.getStatus() == 8) { ... }` 条件判断语句。
画面 14: 展示 `ReviewMediaArticleServiceImpl` 类中 `if (walle.getStatus() == 8) { ... }` 条件判断语句，其中包含 `//审核文章的标题与内容的匹配度` 和 `//审核文章内容的图片信息，然后接口` 注释。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```java
package com.heima.admin.service;
public interface ReviewMediaArticleService {
    public void autoReviewArticleByMedia(Integer newsId);
}
```

画面 4:
```java
@Service
public class ReviewMediaArticleServiceImpl implements ReviewMediaArticleService {
```

画面 5:
```java
private WalleMapper walleMapper;
```

画面 6:
```java
public void autoReviewArticleByMedia(Integer newsId) {
```

画面 7:
```java
if (walle != null) {
```

画面 8:
```java
if (walle.getStatus() == 1) {
    reviewSuccessSaveAll(walle);
}
```

画面 9:
```java
private void reviewSuccessSaveAll(Walle walle) {
```

画面 11:
```java
if (walle.getStatus() == 8 && walle.getPublishtime() != null && walle.getPublishtime().getTime() > new Date().getTime()) {
```

画面 12:
```java
reviewSuccessSaveAll(Walle walle);
```

画面 13:
```java
if (walle.getStatus() == 8) {
```

画面 14:
```java
if (walle.getStatus() == 8) {
    //审核文章的标题与内容的匹配度
    //审核文章内容的图片信息，然后接口
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: 流程图结构：
- 起始节点 → “标题与内容是否匹配” → “是” → “审核文本” → “通过” → “审核图片” → “通过” → “发布时间是否大于当前时间” → “是” → 结束节点。
- “标题与内容是否匹配” → “否” → “人工审核拒绝” → 结束节点。
- “审核文本” → “不通过” → 结束节点。
- “审核图片” → “不通过” → 结束节点。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
