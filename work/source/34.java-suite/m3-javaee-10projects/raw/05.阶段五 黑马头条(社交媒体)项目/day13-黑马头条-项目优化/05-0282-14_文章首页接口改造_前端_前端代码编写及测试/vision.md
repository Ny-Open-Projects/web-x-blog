# 画面线理解：14_文章首页接口改造_前端_前端代码编写及测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day13-黑马头条-项目优化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day13-黑马头条-项目优化\14_文章首页接口改造_前端_前端代码编写及测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:19, 01:18, 01:57, 02:55, 04:05, 04:49, 05:43, 06:40, 07:47, 09:20, 10:37, 11:50, 14:10, 15:00
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:55:14

1) 这一组画面整体在讲一个基于 Spring Boot 的文章列表服务的开发与调试过程，包括控制器、服务层、数据映射层的代码实现，以及前端页面的预览。

2) 按时间顺序列出每张画面的要点：

画面 1:
- IDE: WebStorm，项目路径为 heima-leadnews-app。
- 项目结构：显示了 src/main/java、src/main/resources、static、web 等目录。
- 控制台输出：应用已成功编译，正在运行于 http://127.0.0.1:8081。

画面 2:
- IDE: IntelliJ IDEA，项目为 heima-leadnews-login。
- 代码文件：ArticleHomeV2Controller.java，显示了 @RequestMapping("/api/v2/article") 的控制器方法。
- 代码内容：public class ArticleHomeV2Controller implements ArticleHomeControllerApi { ... }，包含 private AppArticleService appArticleService; 和 @Override public ResponseResult loadV2(ArticleHomeDto dto) { ... } 方法。

画面 3:
- IDE: IntelliJ IDEA，项目为 heima-leadnews-login。
- 控制台输出：显示了多个消费者（consumer）的分区分配日志，如 consumer-0~7 分配了不同 group 的分区。

画面 4:
- 浏览器：Weex Preview，显示了移动端文章列表页面。
- 页面内容：包含文章标题、缩略图，右侧有二维码提示“Use Weex playground app to scan it.”。

画面 5:
- IDE: IntelliJ IDEA，项目为 heima-leadnews-article。
- 代码文件：ArticleHomeV2Controller.java。
- 代码内容：@Override public ResponseResult loadV2(ArticleHomeDto dto) { ... } 方法，其中包含 return appArticleService.loadV2(ArticleConstants.LOADTYPE_LOAD_MORE, dto, firstPage: false);。

画面 6:
- IDE: IntelliJ IDEA，项目为 heima-leadnews-article。
- 代码文件：AppArticleServiceImpl.java。
- 代码内容：public ResponseResult loadV2(Short type, ArticleHomeDto dto, boolean firstPage) { ... } 方法，包含 if(dto == null) { dto = new ArticleHomeDto(); } 和 if(dto.getMaxBehotTime() == null) { dto.setMaxBehotTime(new Date()); }。

画面 7:
- IDE: IntelliJ IDEA，项目为 heima-leadnews-article。
- 代码文件：AppArticleServiceImpl.java。
- 代码内容：if(user == null) { List<Article> userArticleList = getUserArticleList(user, dto, type); return ResponseResult.okResult(userArticleList); } else { List<Article> defaultArticleList = getDefaultArticleList(dto, type); return ResponseResult.okResult(defaultArticleList); }。

画面 8:
- IDE: IntelliJ IDEA，项目为 heima-leadnews-article。
- 代码文件：AppArticleServiceImpl.java。
- 代码内容：private List<Article> getDefaultArticleList(ArticleHomeDto dto, Short type) { ... } 方法，包含 List<Article> articleList = Lists.newArrayList(); 和 for (ApArticle apArticle : apArticleMapper.selectByIds(Lists.newArrayList())) { articleList.add(apArticle); }。

画面 9:
- IDE: IntelliJ IDEA，项目为 heima-leadnews-article。
- 代码文件：AppArticleMapper.xml。
- 代码内容：if test != null and dto.count != null and a.count_id = dto.count.id ... if test.type = null and type == 1 ... if test.type != null and type == 2 ... if test.dto.tag == '_all' ...。

画面 10:
- IDE: IntelliJ IDEA，项目为 heima-leadnews-article。
- 代码文件：AppArticleServiceImpl.java。
- 代码内容：private List<Article> getDefaultArticleList(ArticleHomeDto dto, Short type) { ... } 方法，包含 List<Article> articleList = Lists.newArrayList(); 和 for (ApArticle apArticle : apArticleMapper.selectByIds(Lists.newArrayList())) { articleList.add(apArticle); }。

画面 11:
- 数据库工具：Navicat for MySQL。
- 数据库连接：heima-news。
- 数据库表：显示了多个表，如 ap_article、ap_article_tag、ap_article_comment、ap_article_like、ap_article_view、ap_article_collect、ap_article_share、ap_article_favorite、ap_article_star、ap_article_bookmark、ap_article_download、ap_article_report、ap_article_feedback、ap_article_comment_reply、ap_article_comment_like、ap_article_comment_star、ap_article_comment_collect、ap_article_comment_share、ap_article_comment_favorite、ap_article_comment_bookmark、ap_article_comment_download、ap_article_comment_report、ap_article_comment_feedback、ap_article_comment_reply_like、ap_article_comment_reply_star、ap_article_comment_reply_collect、ap_article_comment_reply_share、ap_article_comment_reply_favorite、ap_article_comment_reply_bookmark、ap_article_comment_reply_download、ap_article_comment_reply_report、ap_article_comment_reply_feedback、ap_article_comment_reply_reply_like、ap_article_comment_reply_reply_star、ap_article_comment_reply_reply_collect、ap_article_comment_reply_reply_share、ap_article_comment_reply_reply_favorite、ap_article_comment_reply_reply_bookmark、ap_article_comment_reply_reply_download、ap_article_comment_reply_reply_report、ap_article_comment_reply_reply_feedback、ap_article_comment_reply_reply_reply_like、ap_article_comment_reply_reply_reply_star、ap_article_comment_reply_reply_reply_collect、ap_article_comment_reply_reply_reply_share、ap_article_comment_reply_reply_reply_favorite、ap_article_comment_reply_reply_reply_bookmark、ap_article_comment_reply_reply_reply_download、ap_article_comment_reply_reply_reply_report、ap_article_comment_reply_reply_reply_feedback、ap_article_comment_reply_reply_reply_reply_like、ap_article_comment_reply_reply_reply_reply_star、ap_article_comment_reply_reply_reply_reply_collect、ap_article_comment_reply_reply_reply_reply_share、ap_article_comment_reply_reply_reply_reply_favorite、ap_article_comment_reply_reply_reply_reply_bookmark、ap_article_comment_reply_reply_reply_reply_download、ap_article_comment_reply_reply_reply_reply_report、ap_article_comment_reply_reply_reply_reply_feedback、ap_article_comment_reply_reply_reply_reply_reply_like、ap_article_comment_reply_reply_reply_reply_reply_star、ap_article_comment_reply_reply_reply_reply_reply_collect、ap_article_comment_reply_reply_reply_reply_reply_share、ap_article_comment_reply_reply_reply_reply_reply_favorite、ap_article_comment_reply_reply_reply_reply_reply_bookmark、ap_article_comment_reply_reply_reply_reply_reply_download、ap_article_comment_reply_reply_reply_reply_reply_report、ap_article_comment_reply_reply_reply_reply_reply_feedback、ap_article_comment_reply_reply_reply_reply_reply_reply_like、ap_article_comment_reply_reply_reply_reply_reply_reply_star、ap_article_comment_reply_reply_reply_reply_reply_reply_collect、ap_article_comment_reply_reply_reply_reply_reply_reply_share、ap_article_comment_reply_reply_reply_reply_reply_reply_favorite、ap_article_comment_reply_reply_reply_reply_reply_reply_bookmark、ap_article_comment_reply_reply_reply_reply_reply_reply_download、ap_article_comment_reply_reply_reply_reply_reply_reply_report、ap_article_comment_reply_reply_reply_reply_reply_reply_feedback、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_like、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_star、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_collect、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_share、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_favorite、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_bookmark、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_download、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_report、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_feedback、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_reply_like、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_reply_star、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_reply_collect、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_reply_share、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_reply_favorite、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_reply_bookmark、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_reply_download、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_reply_report、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_reply_feedback、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_reply_reply_like、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_reply_reply_star、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_reply_reply_collect、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_reply_reply_share、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_reply_reply_favorite、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_reply_reply_bookmark、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_reply_reply_download、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_reply_reply_report、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_reply_reply_feedback、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_reply_reply_reply_like、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_reply_reply_reply_star、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_reply_reply_reply_collect、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_reply_reply_reply_share、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_reply_reply_reply_favorite、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_reply_reply_reply_bookmark、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_reply_reply_reply_download、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_reply_reply_reply_report、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_reply_reply_reply_feedback、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_reply_reply_reply_reply_like、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_reply_reply_reply_reply_star、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_reply_reply_reply_reply_collect、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_reply_reply_reply_reply_share、ap_article_comment_reply_reply_reply_reply_reply_reply_reply_reply_reply_reply_reply_favorite、ap_article_comment_reply_reply_reply_reply_reply
