# 画面线理解：16_自媒体文章管理_发布文章业务代码编写3

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\16_自媒体文章管理_发布文章业务代码编写3【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 01:31, 03:12, 05:14, 06:52, 07:42, 08:53, 09:58, 11:36, 12:32, 14:29, 15:33, 16:53, 17:52
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:52:46

1) 这一组画面整体在讲什么（一句话）：
在 IntelliJ IDEA 中编写 Java 代码，实现新闻内容与封面图片、文章内容与图片的关联保存逻辑，并在 Navicat 中查看数据库表结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 编辑 `NewsServiceImpl.java` 文件，正在处理 `saveRelationInfoForContent` 方法的调用。
- 代码片段：`materials, wallows.getid();`
- 代码片段：`saveRelationInfoForContent(Map<String> materials, Wallows wallows, int countingNum);`
- 代码片段：`notify()`、`notifyAll()`、`VerifyError` 等方法名被高亮显示。

画面 2：
- 编辑 `NewsServiceImpl.java` 文件，显示 `coveragesRelation` 方法的参数和注释。
- 代码片段：`private ResponseResult coveragesRelation(WallowsDto dto, Map<String, Object> materials, Wallows wallows, int countingNum) {`
- 注释：`//保存图片与文档的关系`、`//保存处理完成返回结果`

画面 3：
- 编辑 `NewsServiceImpl.java` 文件，正在编写 `coveragesRelation` 方法的逻辑。
- 代码片段：`List<String> images = dto.getImages();`
- 代码片段：`if (!WmMediaConstants.WM_NEWS_TYPE_AUTO.equals(dto.getType()) && dto.getType() != images.size()) {`
- 代码片段：`return ResponseResult.errorResult(ApitypCodeEnum.PARAM_INVALID, errorMessage: "图文模式不匹配");`

画面 4：
- 编辑 `NewsServiceImpl.java` 文件，继续编写 `coveragesRelation` 方法。
- 代码片段：`if (!WmMediaConstants.WM_NEWS_TYPE_AUTO.equals(dto.getType())) {`
- 注释：`//如果是自动匹配封面`

画面 5：
- 编辑 `NewsServiceImpl.java` 文件，继续编写 `coveragesRelation` 方法。
- 代码片段：`if (WmMediaConstants.WM_NEWS_TYPE_AUTO.equals(dto.getType())) {`
- 代码片段：`images = new ArrayList<>();`
- 代码片段：`if (countImageNum == WmMediaConstants.WM_NEWS_SINGLE_IMAGE) {`
- 代码片段：`for (Object value : materials.values()) {`
- 代码片段：`images.add(String.valueOf(value));`
- 代码片段：`break;`

画面 6：
- 编辑 `NewsServiceImpl.java` 文件，继续编写 `coveragesRelation` 方法。
- 代码片段：`if (countImageNum == WmMediaConstants.WM_NEWS_SINGLE_IMAGE) {`
- 代码片段：`for (Object value : materials.values()) {`
- 代码片段：`images.add(String.valueOf(value));`
- 代码片段：`break;`

画面 7：
- 编辑 `NewsServiceImpl.java` 文件，继续编写 `coveragesRelation` 方法。
- 代码片段：`if (countImageNum == WmMediaConstants.WM_NEWS_MAIN_IMAGE) {`
- 代码片段：`for (int i = 0; i < images.size(); i++) {`
- 代码片段：`images.add(String.valueOf(images.get(i)));`

画面 8：
- 编辑 `NewsServiceImpl.java` 文件，继续编写 `coveragesRelation` 方法。
- 代码片段：`if (images.size() != 0) {`
- 代码片段：`ResponseResult responseResult = saveRelationInfoForCover(images, wallows.getid());`
- 代码片段：`if (responseResult != null) {`
- 代码片段：`return responseResult;`

画面 9：
- 编辑 `NewsServiceImpl.java` 文件，继续编写 `coveragesRelation` 方法。
- 代码片段：`if (images.size() != 0) {`
- 代码片段：`ResponseResult responseResult = saveRelationInfoForCover(images, wallows.getid());`
- 代码片段：`if (responseResult != null) {`
- 代码片段：`return responseResult;`

画面 10：
- 编辑 `NewsServiceImpl.java` 文件，继续编写 `coveragesRelation` 方法。
- 代码片段：`if (images != null && images.size() != 0) {`
- 代码片段：`String[] elements = images.stream().map(s -> s.replace(fileServerUrl, "")).toArray(String[]::new);`
- 代码片段：`wallows.setImages(elements);`

画面 11：
- 打开 Navicat for MySQL，查看 `wm_news_material` 数据库表。
- 表结构：`id`, `user_id`, `url`, `type`, `is_collection`, `created_at`
- 数据行示例：`3105`, `1100`, `group(00/00/01)/...`, `0`, `2019-08-22 21:26:20`

画面 12：
- 编辑 `NewsServiceImpl.java` 文件，编写 `saveRelationInfoForCover` 方法。
- 代码片段：`private ResponseResult saveRelationInfoForCover(List<String> images, Integer id) {`
- 代码片段：`Map<String, Object> materials = new HashMap<>();`
- 代码片段：`for (int i = 0; i < images.size(); i++) {`
- 代码片段：`materials.put(images.get(i), i);`

画面 13：
- 编辑 `NewsServiceImpl.java` 文件，编写 `saveRelationInfoForCover` 方法。
- 代码片段：`private ResponseResult saveRelationInfoForCover(List<String> images, Integer id) {`
- 代码片段：`Map<String, Object> materials = new HashMap<>();`
- 代码片段：`for (int i = 0; i < images.size(); i++) {`
- 代码片段：`materials.put(images.get(i), i);`

画面 14：
- 编辑 `NewsServiceImpl.java` 文件，编写 `saveRelationInfoForCover` 方法。
- 代码片段：`private ResponseResult saveRelationInfoForCover(List<String> images, Integer id) {`
- 代码片段：`Map<String, Object> materials = new HashMap<>();`
- 代码片段：`for (int i = 0; i < images.size(); i++) {`
- 代码片段：`materials.put(images.get(i), i);`

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
- 代码片段：`materials, wallows.getid();`
- 代码片段：`saveRelationInfoForContent(Map<String> materials, Wallows wallows, int countingNum);`
- 代码片段：`notify()`、`notifyAll()`、`VerifyError`

画面 2：
- 代码片段：`private ResponseResult coveragesRelation(WallowsDto dto, Map<String, Object> materials, Wallows wallows, int countingNum) {`
- 注释：`//保存图片与文档的关系`、`//保存处理完成返回结果`

画面 3：
- 代码片段：`List<String> images = dto.getImages();`
- 代码片段：`if (!WmMediaConstants.WM_NEWS_TYPE_AUTO.equals(dto.getType()) && dto.getType() != images.size()) {`
- 代码片段：`return ResponseResult.errorResult(ApitypCodeEnum.PARAM_INVALID, errorMessage: "图文模式不匹配");`

画面 4：
- 代码片段：`if (!WmMediaConstants.WM_NEWS_TYPE_AUTO.equals(dto.getType())) {`
- 注释：`//如果是自动匹配封面`

画面 5：
- 代码片段：`if (WmMediaConstants.WM_NEWS_TYPE_AUTO.equals(dto.getType())) {`
- 代码片段：`images = new ArrayList<>();`
- 代码片段：`if (countImageNum == WmMediaConstants.WM_NEWS_SINGLE_IMAGE) {`
- 代码片段：`for (Object value : materials.values()) {`
- 代码片段：`images.add(String.valueOf(value));`
- 代码片段：`break;`

画面 6：
- 代码片段：`if (countImageNum == WmMediaConstants.WM_NEWS_SINGLE_IMAGE) {`
- 代码片段：`for (Object value : materials.values()) {`
- 代码片段：`images.add(String.valueOf(value));`
- 代码片段：`break;`

画面 7：
- 代码片段：`if (countImageNum == WmMediaConstants.WM_NEWS_MAIN_IMAGE) {`
- 代码片段：`for (int i = 0; i < images.size(); i++) {`
- 代码片段：`images.add(String.valueOf(images.get(i)));`

画面 8：
- 代码片段：`if (images.size() != 0) {`
- 代码片段：`ResponseResult responseResult = saveRelationInfoForCover(images, wallows.getid());`
- 代码片段：`if (responseResult != null) {`
- 代码片段：`return responseResult;`

画面 9：
- 代码片段：`if (images.size() != 0) {`
- 代码片段：`ResponseResult responseResult = saveRelationInfoForCover(images, wallows.getid());`
