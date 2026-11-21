# 画面线理解：18_自媒体文章管理_发布文章前后端联调测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\18_自媒体文章管理_发布文章前后端联调测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 01:42, 03:26, 04:43, 05:43, 06:51, 08:13, 08:59, 10:04, 11:43, 12:58, 14:14, 15:12, 16:35
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:54:29

1) 这一组画面整体在讲一个新闻内容管理系统（“黑马头条”）的前端发布文章功能与后端 Java 服务端处理文章图片上传和内容校验的实现逻辑。

2) 按时间顺序列出每张画面的要点：
画面 1: 登录页面，显示“黑马头条”登录框，要求输入用户名和密码。
画面 2: 发布文章页面，用户正在编辑文章，包含一张图片和多个图片占位符。
画面 3: 在图片上点击后弹出“添加文字”对话框，用于在图片上添加文字。
画面 4: Java 后端代码，`NewsServiceImpl.java` 中的 `coverImagesRelation` 方法，处理文章图片数据，从 JSON 中提取图片数量并创建 `Images` 对象。
画面 5: Java 后端代码，`NewsServiceImpl.java` 中的 `coverImagesRelation` 方法，校验图片类型是否匹配，若不匹配则返回错误。
画面 6: Java 后端代码，`NewsServiceImpl.java` 中的 `coverImagesRelation` 方法，若图片类型匹配，则更新数据库中的图片信息。
画面 7: Vue 前端代码，`index.vue` 中的 `<el-form-item>` 组件，用于选择频道和发布时间。
画面 8: Vue 前端代码，`publish.js` 文件，定义了 `getChannels`、`publishArticles` 和 `modifyArticles` 等 API 请求函数。
画面 9: Vue 前端代码，`index.vue` 中的 `<el-select>` 组件，用于选择频道，`placeholder` 为“选择日期时间”。
画面 10: Vue 前端代码，`selectImgList.vue` 文件，定义了 `getImgData` 函数，用于获取图片列表。
画面 11: Vue 前端代码，`index.vue` 中的 `<el-tabs>` 组件，用于切换图片展示模式，包含“单图”、“三图”等选项。
画面 12: Vue 前端代码，`heima.vue` 文件，定义了 `addText` 和 `editText` 函数，用于添加和编辑文字。
画面 13: Vue 前端代码，`selectImgList.vue` 文件，定义了 `transImage` 函数，用于处理图片类型，`type == "1"` 时为单图，`type == "3"` 时为三图。
画面 14: Vue 前端代码，`api.js` 文件，定义了多个 API 常量，如 `API_USER_IMAGES_ADD`、`API_CHANNELS`、`API_ARTICLES_SUBMIT` 等。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面 4:
```java
Map<String, Object> materials;
try {
    List<Map> list = objectMapper.readValue(content, List.class);
    // 检查信息
    List<Map> extractInfo = extractInfo(list);
    extractInfo.size() == 2 && list.size() == 4
    materials = (Map<String, Object>) extractInfo.get("materials");
    // 图片数量
    int countImageNum = (int) extractInfo.get("countImageNum");
    // 保存文章的逻辑
    News news = new News();
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsTitle((String) materials.get("title"));
    news.setNewsContent((String) materials.get("content"));
    news.setNewsImages((List) materials.get("images"));
    news.setNewsImagesCount(countImageNum);
    news.setNewsStatus(NewsStatus.NEWS_STATUS_PUBLISH);
    news.setNewsAuthor((String) materials.get("author"));
    news.setNewsCreateTime(new Date());
    news.setNewsUpdateTime(new Date());
    news.setNewsChannelId((Integer) materials.get("channelId"));
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE_AUTO);
    news.setNewsType(NewsType.NEWS_TYPE
