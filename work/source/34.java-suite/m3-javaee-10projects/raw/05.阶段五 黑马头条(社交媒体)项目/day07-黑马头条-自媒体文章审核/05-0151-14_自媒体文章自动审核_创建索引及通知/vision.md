# 画面线理解：14_自媒体文章自动审核_创建索引及通知

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day07-黑马头条-自媒体文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day07-黑马头条-自媒体文章审核\14_自媒体文章自动审核_创建索引及通知【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 01:01, 01:49, 02:39, 03:19, 04:36, 05:24, 06:15, 07:50, 08:41, 10:33, 11:33, 12:18, 13:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:25:37

1) 这一组画面整体在讲什么（一句话）：
在 ReviewMediaArticleServiceImpl 类中，演示如何处理文章审核通过后的数据操作，包括插入文章配置、构建索引实体、调用搜索引擎创建索引，并更新文章状态。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 ReviewMediaArticleServiceImpl.java 文件中，代码正在设置文章内容并插入 aparticleConfig，同时弹出类名补全提示。
画面 2: 代码继续编写，创建并初始化 esIndexEntity 对象，设置文章内容和频道ID。
画面 3: 继续设置 esIndexEntity 的属性，包括内容、发布时间、状态和标题。
画面 4: 为 esIndexEntity 设置发布者ID，如果用户ID不为空。
画面 5: 设置文章标题为“media”，并创建 Index.Builder 实例。
画面 6: 为 Index.Builder 设置文章ID和索引名称，并调用 refresh 方法。
画面 7: 调用 jestClient 的 execute 方法执行索引创建，并处理异常。
画面 8: 代码回退，显示之前插入 aparticleConfig 的部分。
画面 9: 展示 ReviewMediaArticleServiceImpl.java 文件的顶部，显示导入的包和类定义。
画面 10: 代码中调用 jestClient.execute() 创建索引，并添加异常处理和日志。
画面 11: 设置文章ID，并调用 updateNews 方法更新文章状态。
画面 12: 调用 apiseMessage.set 方法设置消息内容。
画面 13: 弹出类名补全提示，选择 apiseMessage。
画面 14: 展示处理文本和图片的 handlerTextAndImages 方法，用于处理 JSON 数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
aparticleContent.setArticleId(aparticle.getId());
aparticleContent.setContent(ZipUtils.gzip(wNews.getContent()));
aparticleContentMapper.insert(aparticleContent);

ApArticleConfig aparticleConfig = new ApArticleConfig();
aparticleConfig.setArticleId(aparticle.getId());
aparticleConfig.setIsComment(true);
aparticleConfig.setIsDelete(false);
aparticleConfig.setIsDown(false);
aparticleConfig.setIsForward(true);
aparticleConfigMapper.insert(aparticleConfig);
```

画面 2:
```java
//创建索引
esIndexEntity = new EsIndexEntity();
esIndexEntity.setId(aparticle.getId().longValue());
esIndexEntity.setChannelId(new Long(channelId));
esIndexEntity.setContent(wNews.getContent());
```

画面 3:
```java
esIndexEntity.setPublishTime(new Date());
esIndexEntity.setStatus(new Long(value: 1));
esIndexEntity.setTitle(wNews.getTitle());
```

画面 4:
```java
if(wNews.getUserId()!null){
esIndexEntity.setUserId(wNews.getUserId());
}
```

画面 5:
```java
esIndexEntity.setTitle("media");
Index.Builder builder = new Index.Builder(esIndexEntity);
```

画面 6:
```java
builder.id(aparticle.getId().toString());
builder.refresh(true);
```

画面 7:
```java
Index build = builder.index(2sIndexConstants.ARTICLE_INDEX).build();
jestClient.execute(build);
```

画面 8:
```java
aparticleMapper.insert(aparticle);
//ap article content an article content
ApArticleContent aparticleContent = new ApArticleContent();
aparticleContent.setArticleId(aparticle.getId());
aparticleContent.setContent(ZipUtils.gzip(wNews.getContent()));
aparticleContentMapper.insert(aparticleContent);

ApArticleConfig aparticleConfig = new ApArticleConfig();
aparticleConfig.setArticleId(aparticle.getId());
aparticleConfig.setIsComment(true);
aparticleConfig.setIsDelete(false);
aparticleConfig.setIsDown(false);
aparticleConfig.setIsForward(true);
aparticleConfigMapper.insert(aparticleConfig);
```

画面 9:
```java
import com.heima.utils.common.ZipUtils;
import io.searchbox.client.JestClient;
import io.searchbox.client.JestResult;
import io.searchbox.core.DocumentResult;
import io.searchbox.core.Index;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

@Service
@com.heima.utils.common.ZipUtils
public class ReviewMediaArticleServiceImpl implements ReviewMediaArticleService {
    @Autowired
    private WNewsMapper wNewsMapper;
```

画面 10:
```java
Index.Builder builder = new Index.Builder(esIndexEntity);
builder.id(aparticle.getId().toString());
builder.refresh(true);
Index build = builder.index(2sIndexConstants.ARTICLE_INDEX).type(2sIndexConstants.DEFAULT_DOC).build();
jestClient.execute(build);
try {
    result = jestClient.execute(build);
} catch (JException e) {
    e.printStackTrace();
}
if(result!=null && result.isSuccessed()){
    Log.error("插入更加索引失败。message: " + result.getErrorMessage());
}
```

画面 11:
```java
//修改wNews的状态为 2
wNews.setArticleId(aparticle.getId());
updateNews(wNews, short, message: "审核成功");
//通知用户审核成功
```

画面 12:
```java
apiseMessage.set
```

画面 13:
```java
apiseMessage
```

画面 14:
```java
private void handlerTextAndImages(List<String> images, StringBuilder sb, JSONArray jsonArray) {
    for (Object obj : jsonArray) {
        JSONObject jsonobj = (JSONObject) obj;
        String type = (String) jsonobj.get("type");
        if ("image".equals(type)) {
            String value = (String) jsonobj.get("value");
            images.add(value);
        }
        if ("text".equals(type)) {
            sb.append(jsonobj.get("value"));
        }
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
