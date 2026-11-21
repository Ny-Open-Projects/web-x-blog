# 13_自媒体文章自动审核_保存文章内容和配置

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day07-黑马头条-自媒体文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day07-黑马头条-自媒体文章审核\13_自媒体文章自动审核_保存文章内容和配置【海量资源尽在 666java.com】.mp4
- 时长 5分2秒（音频 303s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们就继续做下面咱们就来去把当前的这个东西给去保存一下这个怎么保存的其实这个东西就比较简单了咱们可以直接去拗出来个东西叫AP article.com拗出来一个东西先保存它好吧然后你就可以往里边去设置了非常简单然后是.set什么呢set的东西里边其实就没几个是吧第一个是什么IDcontainer好,add your ID
[00:31] 其实你就可以直接从article.get id就可以了那为什么他能拿到呢其实呢这个字你应该知道啊因为咱们在保存他的时候呢可以看一下这里边咱们设置了一个逐渐返回其实就能去保存的时候就能直接拿到当前这个id好吧行那这个设置完之后咱们再往下看啊这边还有什么东西ap article.setconvent
[01:01] AP article content.setcontent.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.
[01:32] 然后再去然后怎么着去注入一个是吧private什么AP articleconfigconfigmapper注进来之后咱们这时候就能用了然后往下走往下走你可以直接去加AP然后是content.set
[02:04] 不是再载,insert就把当前这个数据加进去,没事了没问题啊那这个保存完之后呢其实里边还少一步啊还少一步,少哪一步呢就这个内容啊咱们需要去加密需要加密啊你看咱们之前保存的数据呢其实当前的内容啊找到内容表吧内容表就是它稍等啊,这个有点慢你看内容啊
[02:34] 这个内容是这样的是吧这并不是真正的内容咱们再去展示文章内容的时候是不是解压过是吧所以说咱们在这先去先去做一个加密这个加密的方式也比较简单咱们直接调一个公居类就可以了叫ZIPUTUSZIPUTUS要是这干嘛呢有一个ZIP这样的话就咱们一两个把这个文章内容装进去就可以了啊好这样就可以了啊那么下面呢就来去保存当前的这个位置
[03:07] 当前这个config咱们在这也可以去new一个new一个当前的aparticleconfig, 等于new一个ap好,入出来之后咱们可以直接去设置了config rset有一个article id那就容易beparticle.getid是吧然后再往下往下的话其实都是一些不耳之可以直接设置为库就可以了
[03:38] 往下走config.set比如说你的关注是吧我们可以去设置一个比如说有一个还有啥呢aparticleconfig.set下面还有一个就是isdelete是否需要删除是吧ok咱们可以去设置aparticle是否可以删除aparticleconfig.set
[04:12] 是否可以去下载是吧不是要下载是吧就咱们看一下AP article config.sets is forward应该是转发转发是设置为true那这个设置完了这个删除的话咱们可以设置为first可以看一下当前的表是在当前的这是否可评论是吧
[04:41] 然后是否转发是否下架还有是否已删除OK行没问题啊那这个咱们就设置完了设置完之后呢咱们可以直接去保存了啊AP然后这是一个config myprtl in third就把当前那个config给保存就可以了OK那这个啊这两个咱们也就保存完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在 Heima 新闻后台管理系统中，通过 Java 代码实现文章审核通过后，将文章内容、配置信息等持久化到数据库的完整流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 ReviewMediaArticleServiceImpl.java 文件中，展示代码结构，包含导入包如 org.springframework.beans.factory.annotation、org.springframework.stereotype.Service 等，以及类定义和注解。
画面 2: 代码中定义了 String split = images.split(regex, "");，使用 StringBuilder 构建字符串，并调用 aparticle.setImages(sb.toString())。
画面 3: 代码中调用 aparticle.setChannelId(Integer channelId) 设置频道ID。
画面 4: 代码中创建 AparticleContent 对象并设置其内容，调用 aparticleContentMapper.insert(aparticleContent)。
画面 5: 代码中定义了 @Value("${FILE_SERVER_URL}") private String fileServerUrl; 和 @Autowired private ApArticleMapper apArticleMapper;。
画面 6: 代码中声明了 @Autowired private ApArticleContentMapper apArticleContentMapper; 和 @Autowired private ApArticleConfigMapper apArticleConfigMapper;，并开始编写 reviewSuccessSaveAll 方法。
画面 7: 在 Navicat for MySQL 中，展示 ap_article_content 表的结构，包含字段如 id, user_id, title, content, type, channel_id, labels, created_time, status, publish_time 等。
画面 8: 代码中调用 aparticleContentMapper.insert(aparticleContent)。
画面 9: 代码中调用 AparticleConfig aparticleConfig = new AparticleConfig();。
画面 10: 代码中为 aparticleConfig 设置 articleId。
画面 11: 代码中为 aparticleConfig 设置 comment 和 delete 状态。
画面 12: 代码中为 aparticleConfig 设置 forward 和 down 状态。
画面 13: 在 Navicat for MySQL 中，展示 ap_article_content 表的数据，包含多条记录，如 id 为 3100、3101 等，content 字段值为 "[type=text]"。
画面 14: 代码中调用 aparticleConfigMapper.insert(aparticleConfig)。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
import java.util.concurrent.ThreadPoolExecutor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.util.StringUtils;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.commons.CommonsMultipartFile;
import org.springframework.web.multipart.commons.CommonsMultipartResolver;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.ServletRequestAttributes;
import org.springframework.web.multipart.MultipartRequest;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.Multipart

