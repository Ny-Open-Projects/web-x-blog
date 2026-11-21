# 画面线理解：21_爬虫文章审核_审核成功更新状态

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day11-黑马头条-爬虫系统完善&文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day11-黑马头条-爬虫系统完善&文章审核\21_爬虫文章审核_审核成功更新状态【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:16, 00:42, 00:49, 00:56, 00:59, 01:05, 01:15, 01:28, 01:31, 01:39, 01:43, 01:51, 02:06
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:29:12

1) 这一组画面整体在讲如何在新闻文章审核服务中，通过代码实现文章状态更新、审核日志记录和内容索引功能。

2) 按时间顺序列出每张画面的要点：
画面1：在 ReviewCrawlerArticleServiceImpl.java 文件中，编写 updateNewsSuccess 方法，用于更新文章状态为审核成功（状态码9），并调用 cNewsMapper.updateStatus 方法。
画面2：在 updateNewsSuccess 方法中，添加日志记录语句，记录审核流程结束和耗时。
画面3：在 updateNewsSuccess 方法中，使用 cNewsMapper.updateStatus 方法更新文章状态。
画面4：在 updateNewsSuccess 方法中，使用 cNewsMapper.updateStatus 方法更新文章状态。
画面5：在 updateNewsSuccess 方法中，使用 cNewsMapper.updateStatus 方法更新文章状态。
画面6：在 updateNewsSuccess 方法中，使用 cNewsMapper.updateStatus 方法更新文章状态。
画面7：在 updateNewsSuccess 方法中，使用 cNewsMapper.updateStatus 方法更新文章状态。
画面8：在 updateNewsSuccess 方法中，使用 cNewsMapper.updateStatus 方法更新文章状态。
画面9：在 updateNewsSuccess 方法中，使用 cNewsMapper.updateStatus 方法更新文章状态。
画面10：在 updateNewsSuccess 方法中，使用 cNewsMapper.updateStatus 方法更新文章状态。
画面11：在 ReviewCrawlerArticleServiceImpl.java 文件中，编写 createEsIndex 方法，用于创建文章在 Elasticsearch 中的索引。
画面12：在 ReviewCrawlerArticleServiceImpl.java 文件中，编写 handlerTextAndImages 方法，用于处理文章中的文本和图片。
画面13：展示新闻文章审核流程图，包括：爬取文章 -> 审核文本 -> 审核图片 -> 保存文章 -> 创建索引。
画面14：展示新闻文章审核流程图，包括：爬取文章 -> 审核文本 -> 审核图片 -> 保存文章 -> 创建索引。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
//更改状态 为 9
updateNewsSuccess(cNews);
```
画面2：
```java
Log.info("审核流程结束，耗时：{}",
```
画面3：
```java
private void updateNewsSuccess(CNews cNews) {
    cNews.setStatus((byte) 9);
    cNewsMapper.updateStatus(cNews);
}
```
画面4：
```java
private void updateNewsSuccess(CNews cNews) {
    cNews.setStatus((byte) 9);
    cNewsMapper.updateStatus(cNews);
}
```
画面5：
```java
private void updateNewsSuccess(CNews cNews) {
    cNews.setStatus((byte) 9);
    cNewsMapper.updateStatus(cNews);
}
```
画面6：
```java
private void updateNewsSuccess(CNews cNews) {
    cNews.setStatus((byte) 9);
    cNewsMapper.updateStatus(cNews);
}
```
画面7：
```java
private void updateNewsSuccess(CNews cNews) {
    cNews.setStatus((byte) 9);
    cNewsMapper.updateStatus(cNews);
}
```
画面8：
```java
private void updateNewsSuccess(CNews cNews) {
    cNews.setStatus((byte) 9);
    cNewsMapper.updateStatus(cNews);
}
```
画面9：
```java
private void updateNewsSuccess(CNews cNews) {
    cNews.setStatus((byte) 9);
    cNewsMapper.updateStatus(cNews);
}
```
画面10：
```java
private void updateNewsSuccess(CNews cNews) {
    cNews.setStatus((byte) 9);
    cNewsMapper.updateStatus(cNews);
}
```
画面11：
```java
private void createEsIndex(ApArticle apArticle, CNews cNews) throws IOException {
    EsIndexEntity esIndexEntity = saveEsIndexEntity(apArticle, cNews);
    Index.Builder builder = new Index.Builder(esIndexEntity);
    builder.id(apArticle.getGid()).toString();
    builder.refresh(true);
    Index index = Index.index(ESIndexConstants.ARTICLE_INDEX, type(ESIndexConstants.DEFAULT_DOC).build());
}
```
画面12：
```java
private void handlerTextAndImages(List<String> images, StringBuilder sb, JSONArray jsonArray) {
    if (null != jsonArray) {
        for (Object obj : jsonArray) {
            JSONObject jsonObject = (JSONObject) obj;
            String type = (String) jsonObject.get("type");
            if ("image".equals(type)) {
                String value = (String) jsonObject.get("value");
                images.add(value);
            }
            if ("text".equals(type)) {
                String value = (String) jsonObject.get("value");
                sb.append(value);
            }
        }
    }
}
```
画面13：
```mermaid
flowchart TD
    A[爬取文章] --> B{审核文本}
    B -->|通过| C{审核图片}
    C -->|通过| D[保存文章]
    D --> E[创建索引]
    B -->|不通过| F[拒绝]
    C -->|不通过| F
```
画面14：
```mermaid
flowchart TD
    A[爬取文章] --> B{审核文本}
    B -->|通过| C{审核图片}
    C -->|通过| D[保存文章]
    D --> E[创建索引]
    B -->|不通过| F[拒绝]
    C -->|不通过| F
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面13：流程图结构：
- 起始节点：爬取文章
- 决策节点1：审核文本
  - 如果通过，指向决策节点2：审核图片
  - 如果不通过，指向结束节点：拒绝
- 决策节点2：审核图片
  - 如果通过，指向操作节点：保存文章
  - 如果不通过，指向结束节点：拒绝
- 操作节点：保存文章
- 操作节点：创建索引

画面14：流程图结构：
- 起始节点：爬取文章
- 决策节点1：审核文本
  - 如果通过，指向决策节点2：审核图片
  - 如果不通过，指向结束节点：拒绝
- 决策节点2：审核图片
  - 如果通过，指向操作节点：保存文章
  - 如果不通过，指向结束节点：拒绝
- 操作节点：保存文章
- 操作节点：创建索引

5) 不要评价画面美观，不要输出与课程无关的内容。
