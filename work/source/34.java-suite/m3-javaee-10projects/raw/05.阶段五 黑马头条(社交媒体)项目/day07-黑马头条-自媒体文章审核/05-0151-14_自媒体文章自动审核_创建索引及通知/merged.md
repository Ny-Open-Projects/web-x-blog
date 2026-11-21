# 14_自媒体文章自动审核_创建索引及通知

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day07-黑马头条-自媒体文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day07-黑马头条-自媒体文章审核\14_自媒体文章自动审核_创建索引及通知【海量资源尽在 666java.com】.mp4
- 时长 13分38秒（音频 819s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就来去创建所有啊那所以的话呢咱们其实咱们之前呢去有一个类什么叫ESDSindexEntity这个类啊咱们之前是用过的咱们主要的是来创建这个类然后最终的是保存到所有库中就可以了啊可以拿过来拿过来之后呢可以去拗一下等于ES好
[00:29] 我们只要把这个值给填充完整就可以那这个里边值咱们看一下里边有啥DS INDEX 点什么首先咱们要去设置一个叫SET ID这ID咱们现在通常都会用谁呢会用前的APRTQ.GET用它用它就可以了这个咱们可以设置为浪表6它需要一个浪值好吧然后再往下DS INDEX.SET 什么设置一个CHINOD
[00:57] 他里边需要个创造D创造D是不是怎么有AP article就叫创造D是吧他们是有一个创造D的这个创造D好像也不行咱们也可以去设立一个lang value好lang value好吧也可以这样防止报错咱们可以直接new一个langnew一个langnew一个lang再往下看下面还有吗下面还有比如说ES index
[01:32] content是谁?
[01:34] wmuse.getcontent是吧好再往下dsindex.set下面还有一个叫publish time这个发布时间其实咱们可以直接用当前的时间就可以了因为这个其实已经发布了好吧然后再往下往下的话其实咱们还有dsindex.set
[02:02] set status默认给1就可以了好1啊也是个lang类型是吧也用来个lang啊lang类型好这样就可以了啊再往下es indexes index啊而set title把这个wm news的什么set title装进去好还有吗
[02:33] 就是用户ID咱们要设啊es-index-set 往前的一个useID这ID的话其实咱们也拿到了wm-news.getID它防止出错是吧直接咱们可以去wm-user.getIDwm-news 这样吧这样下到了好吧
[03:06] 防止出错了wnews.getUserID不等于none然后这时候咱们往里边去设置好吧就是它那这个咱们就设置完了那出错了吗没问题好设置完之后这里边咱们还要去设置一个东西这个东西就是咱们设置了一个tagindex.setTag这个tag是谁呢
[03:45] Tag 咱们其实应该有个admin吗constance没有是吧没有的话咱们就可以直接设一个media好吧他是一个自媒体他是自媒体啊这个设置完之后啊那这个东西咱们就算创建完了啊创建完之后啊咱们下面就要去创建索引了啊创建索引只是把这个当前内容准备好了好吧创建索引不知道大家还没有印象啊咱们再去写一下首先咱们要去创建一个index builder啊在这去创建一个什么index
[04:15] 比如说他叫啥呢叫builder好吧等于new一个什么index好这边装的就是谁呀as index entity可以装个对象再往下咱们就可以去builder idid咱们可以再去设置一个再去重新设置一个就是eparticle.getid然后咱们可以去toastprint一下因为他有接收当前的一个subtree
[04:47] 然后再往下咱们就可以去刷新一下build.refresh这是true设置完之后咱们现在就可以真正保存了比如说build.index这个index的第一个值第一个值就是咱们的这个es的什么es的索引库的名称是吧有es index constant给咱们这件设伙.
[05:17] IP article index 是不是叫APApp info article然后下面还有什么呢下面还要设置一个typetype 其实也是当前这里边DS index constants有一个defund uc这个就是啊.build最终这个就是拿到一个build拿到一个build之后呢那这东西那你说该怎么去设置呢
[05:46] 这里边咱们还要再去试试个东西就是怎么样去注入一个test plant在上面再去注入private dest plant好 这样之后咱们就可以在这去直接去执行往下走走在这打什么呢打一个esq的
[06:21] 就得装进去就完事了好,不用它返回的是一个当前的就这个咱们用这个东西咱们上次讲过用它去返回是吧我们这需要去踹一下啊就去踹一下不用它返回用谁返回呢用它的一个实现类去返回就实现类的是就谁呀叫 testresultsuresult怎么叫result好吧用它去接受是比较好的
[06:54] 接收完之后咱们下面就可以去拿到这个值了怎么判断其实咱们在这可以直接去判断ifresult不等于none不等于none的result.thisok这时候咱们就可以去设置值这样的话就算是插入索引成功了就算是插入索引成功了
[07:29] 要是成功的咱们可以提示一句话咱们先设置一个非这个非好吧是非之后呢咱们就可以去打印日志啊印日志这个东西该怎么打印呢咱们之前讲过是吧在上边加个数据加一个叫log复接log复接log复接复或者serv复接都可以啊然后下面咱们就可以去设置在这啊比如说打印一个logloglog.error
[08:07] 第一个咱们就可以去设置值比如说插入更新索引失败插入更新索引失败可以设置一个message这个message就是result.get error message完事了这个咱们就印完了印完之后下面还有一个东西这儿如果说这出错的话咱们也可以提示一下log
[08:40] 比如说我们叫什么呢执行执行ESES创建所有人失败创建所有人失败我们也可以给一个message这个message呢其实也是它是吧一点get message那这个就说这完了说这完之后啊这里边你说真正结束了吗
[09:13] 这里边咱们还要去干嘛呢还要去修改状态修改WM News状态为几啊有吗因为现在都已经审核成功显示发布了据说咱们还要再去修改状态还要再去通知用户通知用户审核成功好那这不是好做啊
[09:43] 首先呢,咱们在这, wmnews.setstator是9是吧,是9啊然后呢,咱们要去在这啊,不用在这,不用这么去设置啊不用这么去设置,咱们直接就可以,直接用update是吧update,好,第一个呢是wmnews第二个呢,就是以前的,是吧,然后给一个short好,下面呢是审核成功是审核成功,审核成功
[10:16] 那这个就算是完了这里边咱们还可以去设置一些其他的比如说这里边咱们需要设置一个一旦审核成功之后咱们需要去把当前API-9做上关联据说咱们在这去设置一个东西叫API-9之前你没审核之前你肯定是没有API-9 ID的现在你审核之后把API-9 ID需要去关联上
[10:43] 好吧行那这个咱们就做完了啊刚才说还要去要去通知用户去审核成功啊你说咱们在这啊要去再去注入一个message注入一个miple啊找到这找到这啊再去注一个啊private方式叫什么呢ap user messagemiple好
[11:13] 其实呢就是往这里边呢去插入一条数据是吧再往下走啊往下来来来来好在这去写啊首先呢咱们要去创建一个AAP user messageOK等于new一个AAP它好那咱们可以设置了这是第一个AAP user message.set user id就是wnews.get user id啊然后呢再往下AAP user message.set
[11:43] set一个corridor time,new一个date然后再往下,ap-user.set没有一个is read,咱们可以可读吗可以设置为一个first然后是ap-user.contentcontent的话你肯定可以提示一句话比如说你的文章审核成功
[12:16] 好咱们下面再设一个ap user点什么呢set一个叫做type这type是啥呢咱们可以看一下当时那种啊ap messageap user message啊找一找找不着吗哦找一找ap user message啊这呢啊比较太多了啊呃这个一啊取消关注是吧还有什么呢点赞点赞
[12:51] 取消转发收藏点赞评论审核通过审核通过评论这里边好像没有是吧自媒体认证反馈转发现在我们可以设一个108好吧咱们现在108是啥呢108就是目前的文章审核通过好吧文章审核通过在这写文章审核通过最终咱们就可以保存了保存的保存的APU SERVER MESSAGE MYPORT
[13:22] 把当前的什么AAP user message进去就完事了好吧到此呢这个东西咱们就算是写完了一会儿呢咱们再去用当前的单元测试去测试一下好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

