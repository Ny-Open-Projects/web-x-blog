# 18_爬虫文章审核_文章等信息保存骨架编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day11-黑马头条-爬虫系统完善&文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day11-黑马头条-爬虫系统完善&文章审核\18_爬虫文章审核_文章等信息保存骨架编写【海量资源尽在 666java.com】.mp4
- 时长 7分27秒（音频 447s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么下面就来去完成当前的文章和文章配置还有文章内容还有作者还有标签的保存操作那这个是有顺序的首先咱们要保存的是作者然后是文章然后是文章配置内容和标签作者要放到前边但是要保存文章之前咱们还是要有一个准备的操作哪个呢?
[00:27] 就是频道频道的设置获取吧这个频道的获取怎么获取呢?
[00:33] 我们要放在外边获取所以说咱们要先去获取它clnews.get什么可以获取到一个Channel ID拿到这个Channel ID之后咱们再去比方去获取频道的名称就可以了这怎么获取可以在这去判断说none不等于什么Channel ID然后这时候你就可以去获取了获取的话咱们就可以用用一个叫做ADChannel
[01:01] 咱们在这先去读刚才我读了一个可以删了好我来比特什么ad还有vip读进来之后你可以去用了点咱们有一个slack的可以把它放进去最终就能去拿到一个信息拿到信息之后你就可以再去判断不说那么不等于
[01:37] 那不等于什么呢那不等于什么ADChannel然后呢你就可以拿到当前的什么频道名称这样咱们在这儿啊在当前的这儿写一个String的ChannelNameChannelName等于一个空字串好吧然后呢你就可以直接去复制ADChannel.getName然后呢
[02:08] 就附给这个Channel Name就可以了那的话咱们就能拿到一个Channel Name啊下面刚才说了啊他要去创建的话咱们需要有一个顺序首先要去保存作者因为你保存文章的时候需要用到作者所以说你要先去保存作者信息那保存作者信息的话呢咱们这样啊怎么着呢咱们就可以直接去Save Author APAuthor
[02:43] 条件呢就是当前的CL News最终它返回的呢返回的就是一个什么就是一个当前的APUTH是一个作者的信息这里边其实呢并不是仅仅是保存但是有的话呢先去获取啊先去获取如果有的话呢它就能直接返回如果说没有的话咱们再去保存是有这么个逻辑啊咱们一会儿会去
[03:13] 实现这个东西我先去创建这个方法啊叫获取作者信息那我写的是获取啊不是所有的创建啊没有的时候再创建有的时候咱们就不创建了好吧这是一个啊然后呢下面是下面是哪个下面该什么文章是吧文章啊文章怎么办呢咱们还是有去再去弄一个方法啊
[03:46] save aap ar icre article然后是by colorcr wler好吧然后在里边参数就比较多了啊第一个是images啊因为这个图片呢咱们需要去去保存然后第二个呢是channel id第三个呢是当前的channel name第四个呢就是咱们的有一个叫做aap author.getid就是你要去获取到
[04:14] 作者的ID然后第四个呢是当前的serial news好吧这样的话呢还能去保存一篇文章叫AP articleRTICLV好那保存之后啊下面呢咱们就可以再去保存配置和内容啊好拿了之后啊咱们再去往下保存再去保存啊是怎么着文章的什么配置信息对吧那我让它配置起就比较简单了啊
[04:48] 当然咱们也可以去保存标签保存标签saveAParticle.artic.cle.label这个其实就是谁就是当前的一个AParticle的参数就可以了这个没有咱们也创建出来这是写作室保存标签
[05:29] 保存文章那这些咱们都设置完了记得往下看这个方法咱们先不实践然后下面是不是还有要去保存什么保存咱们的哪个保存咱们的文章配置是吧好保存文章配置的话就是怎么着是saveaparticle然后是config
[06:02] 就这么个方法然后咱们在这儿参数就是当前的哪个就是当前的tpArticle好吧中的它返回的就是一个网流tpArticle好拿到它之后我们在这儿去创建一个也行保存文章配置信息这是一个下面还有最后一个是吧哪个
[06:37] 保存文章内容就是sale什么APRICRE好这个里边东西就比较多了这个是content第二个就是AP article它能够给你返回当然你不返回去这也没事是吧那咱们不需要返回值了
[07:06] 好那这个东西呢咱们就保存就说到这啊但是咱们这个方法也可以去创建出来这是保存什么保存文章内容好那这样的话那所有的方法啊被创建的都创建了可以保存这一份好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中实现文章审核流程，包括文本和图片内容的审核、作者与频道信息的关联、以及文章内容的保存。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 001: 展示 ReviewCrawlerArticleService 类中处理文章审核的逻辑，包括文本和图片审核的条件判断。
画面 002: 展示 if (null != cNews) 条件判断，用于检查文章对象是否为空。
画面 003: 展示自动审核流程的入口方法 autoReviewArticleByCrawler，包含日志记录和内容获取。
画面 004: 展示图片审核失败时的处理逻辑，包括判断图片响应是否为 "pass"。
画面 005: 展示根据频道 ID 查询频道信息的代码，使用 adChannelMapper。
画面 006: 展示保存文章内容的 SQL 语句，包括插入文章表和更新文章状态。
画面 007: 展示保存作者信息的方法 saveAuthor，用于创建或更新作者。
画面 008: 展示保存文章信息的方法 saveArticleByCrawler，包含参数和注释。
画面 009: 展示保存文章标签的方法 saveArticleLabel，用于关联文章与标签。
画面 010: 展示保存文章配置的方法 saveArticleConfig，用于设置文章的配置信息。
画面 011: 展示保存文章内容的方法 saveArticleContent，用于存储文章的文本内容。
画面 012: 展示保存文章标签的方法 saveArticleLabel，用于关联文章与标签。
画面 013: 展示保存文章配置的方法 saveArticleConfig，用于设置文章的配置信息。
画面 014: 展示保存文章内容的方法 saveArticleContent，用于存储文章的文本内容。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 003:
```java
@Override
public void autoReviewArticleByCrawler(CNews cNews) throws Exception {
    long currentTimeMillis = System.currentTimeMillis();
    log.info("开始自动审核流程");
    if (null != cNews) {
        String content = cNews.getUnCompressContent();
```

画面 004:
```java
if (null != imageResponse || !imageResponse.equals("pass")) {
    updateNews(cNews, message: "图片内容审核失败");
}
```

画面 006:
```sql
INSERT INTO article (channel_id, title, content, author_id, status, create_time, update_time)
VALUES (?, ?, ?, ?, ?, ?, ?);

UPDATE article SET status = ? WHERE id = ?;
```

画面 007:
```java
private ApAuthor saveAuthor(CNews cNews) {
    // 创建作者
    ApAuthor apauthor = new ApAuthor();
    apauthor.setChannelId(cNews.getChannelId());
    apauthor.setAuthorName(cNews.getAuthorName());
    apauthor.setAuthorId(cNews.getAuthorId());
    apauthor.setAuthorType(cNews.getAuthorType());
    apauthor.setAuthorStatus(cNews.getAuthorStatus());
    apauthor.setAuthorCreateTime(cNews.getAuthorCreateTime());
    apauthor.setAuthorUpdateTime(cNews.getAuthorUpdateTime());
    apauthor.setAuthorRemark(cNews.getAuthorRemark());
    apauthor.setAuthorEmail(cNews.getAuthorEmail());
    apauthor.setAuthorPhone(cNews.getAuthorPhone());
    apauthor.setAuthorWechat(cNews.getAuthorWechat());
    apauthor.setAuthorWeibo(cNews.getAuthorWeibo());
    apauthor.setAuthorQq(cNews.getAuthorQq());
    apauthor.setAuthorWechatOpenId(cNews.getAuthorWechatOpenId());
    apauthor.setAuthorWechatUnionId(cNews.getAuthorWechatUnionId());
    apauthor.setAuthorWechatNickname(cNews.getAuthorWechatNickname());
    apauthor.setAuthorWechatHeadimgurl(cNews.getAuthorWechatHeadimgurl());
    apauthor.setAuthorWechatGender(cNews.getAuthorWechatGender());
    apauthor.setAuthorWechatProvince(cNews.getAuthorWechatProvince());
    apauthor.setAuthorWechatCity(cNews.getAuthorWechatCity());
    apauthor.setAuthorWechatCountry(cNews.getAuthorWechatCountry());
    apauthor.setAuthorWechatLanguage(cNews.getAuthorWechatLanguage());
    apauthor.setAuthorWechatDeviceId(cNews.getAuthorWechatDeviceId());
    apauthor.setAuthorWechatDeviceType(cNews.getAuthorWechatDeviceType());
    apauthor.setAuthorWechatDeviceModel(cNews.getAuthorWechatDeviceModel());
    apauthor.setAuthorWechatDeviceBrand(cNews.getAuthorWechatDeviceBrand());
    apauthor.setAuthorWechatDeviceVersion(cNews.getAuthorWechatDeviceVersion());
    apauthor.setAuthorWechatDeviceSystem(cNews.getAuthorWechatDeviceSystem());
    apauthor.setAuthorWechatDeviceSystemVersion(cNews.getAuthorWechatDeviceSystemVersion());
    apauthor.setAuthorWechatDeviceSystemName(cNews.getAuthorWechatDeviceSystemName());
    apauthor.setAuthorWechatDeviceSystemVersionName(cNews.getAuthorWechatDeviceSystemVersionName());
    apauthor.setAuthorWechatDeviceSystemVersionCode(cNews.getAuthorWechatDeviceSystemVersionCode());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechatDeviceSystemVersionCodeName());
    apauthor.setAuthorWechatDeviceSystemVersionCodeName(cNews.getAuthorWechat

