# 画面线理解：15_自媒体文章管理_发布文章业务代码编写2

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\15_自媒体文章管理_发布文章业务代码编写2【海量资源尽在 666java.com】.mp4
- 抽帧：13 帧 @ 00:28, 01:10, 02:10, 03:31, 05:00, 05:44, 06:39, 07:19, 07:51, 09:12, 10:20, 11:26, 12:18
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:51:44

1) 这一组画面整体在讲什么（一句话）：
实现新闻内容与媒体素材（图片）的关联保存功能，包括前端数据处理、后端服务逻辑、数据库表结构及SQL操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：在IDE中编辑NewsServiceImpl.java，展示保存图片到文件系统并关联文章的代码逻辑，包含判断文件类型并调用saveFiles方法。
画面2：继续编辑NewsServiceImpl.java，展示将图片与文章关联的代码，调用saveRelationInfoForContent方法，并处理异常。
画面3：展示NewsServiceImpl.java中saveRelationInfoForContent方法的完整结构，包含参数和返回值声明。
画面4：在Navicat中查看wm_news_material表的数据，展示新闻与素材的关联记录。
画面5：在Navicat中展示wm_news_material表的SQL创建语句，包含字段定义和索引。
画面6：在IDE中编辑NewsServiceImpl.java，展示调用WmMaterialMapper的findMaterialByIdAndUserId方法查询素材。
画面7：在IDE中编辑NewsServiceImpl.java，展示调用findMaterialByIdAndUserId方法并传入参数。
画面8：在IDE中编辑NewsServiceImpl.java，展示使用Stream API对查询到的素材进行处理。
画面9：在IDE中编辑NewsServiceImpl.java，展示使用Collectors.toMap方法对素材进行分组映射。
画面10：在IDE中编辑NewsServiceImpl.java，展示使用Stream API对素材进行处理。
画面11：在Navicat中查看wm_material表的数据，展示用户上传的图片记录。
画面12：在IDE中编辑NewsServiceImpl.java，展示使用Stream API对素材进行处理。
画面13：在IDE中编辑NewsServiceImpl.java，展示使用Stream API对素材进行处理。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
//保存或修改文章的图片
WmFiles wmFiles = new WmFiles();
ResultUtils.copyProperties(dto, wmFiles);
if (dto.getType().equals(WmMediaConstants.WM_NEWS_TYPE_AUTO)) {
    saveFiles(wmFiles, dto.getType());
} else {
    saveFiles(wmFiles, dto.getType());
}
//保存内容内的图片和当前文章的关系
```

画面2：
```java
//保存内容内的图片和当前文章的关系
if (materials.containsKey(dto)) {
    saveRelationInfoForContent(materials, wmFiles);
}
```

画面3：
```java
private ResponseResult saveRelationInfoForContent(Map<String, Object> materials, Integer id) {
    //保存文章
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews = new WmNews();
    WmNews wmNews
