# 13_自媒体文章管理_发布文章mapper定义

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\13_自媒体文章管理_发布文章mapper定义【海量资源尽在 666java.com】.mp4
- 时长 11分47秒（音频 707s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就来完成当前发布文章的一个Map文件这Map文件比较多咱们一块块去说首先第一个就是当前有一个WM MatterView然后是当前的什么Map这个Map其实亮这Map的话有一个方法就是查询这查询的话是有两个三数第一个是UID就是当前用户然后第二个是一个Values这个Values的话其实就是当前的URL什么意思你可以打开这边打开它
[00:28] 对吧咱们要通过当前的URL去查到当前某一个对象比如说我有一个这么URL是吧我就查到当前那个对象有可能会传多个那我就返回多个对象这个能明白吗那为什么要这么做呢因为最终咱们能拿到URL但是要做过年的时候是不是要拿到ID因为这个表中这个表中存的时候是不是当前的ID所以说你要通过当前的URL去拿到一个ID值好吧行这个咱们说完之后咱们继续往下看
[00:58] 这个麦粉文件咱们要去写下把它拷贝一下拷到当前的麦粉文件中是好这又错了拷到当前的接口这是多个参数你不用想要干嘛一个param我把这个值给他拷过来好外地拷一个这是y64好那这个写完之后咱们就把当前的麦粉文件也拿过来好那这个你看
[01:46] 你看再来看一眼首先你要去查询当前的ID URL其实就这两个值最终是拿到这个ID然后你条件就是当前用户还有就是你到底是哪个URL到底是哪一个URL最终是一个印有可能传过来是多个URL好最终是拿到这个ID就可以了好吧行那这个拿到拿到完之后咱们再往下看
[02:09] 下面还有还有哪些麦粉这里边还有一个叫wsnews其实这个就是关系表是吧这个关系表这里边有两个方法咱们考虑咱们再说到当前这个东西到这个接口好第一个是根据当前的这种news去删除说你需要改变修改的时候咱们需要去根据前的文章ID去删除某些关系表修改的时候用当然还有这个东西
[02:40] 这个是保存保存他们的关系保存他们的关系那这个呢其实就是当前的一些比如说当前存储的这种Metal ReelsMetal Reels里边的ID然后最终呢你要去怎么去存跟当前的News ID是什么关系你看啊咱们可以打开这个你看当前31013101是不是有可能有可能会有多个数据啊
[03:04] 有可能会有多数据啊那这个好像不太我这数据可能不太不太好啊但你你能看明白啊比如你看啊4100里边他也可能会有多个图片有可能啊你看4100里边有可能有多多个图片看到了吧这没问题啊呃行那这个啊这个所以说呢咱们在这儿啊也需要去把这个东西给加进来啊处理他们的关系也就是说要保存他们的关系啊嗯那这里边咱们在这再去加一些拍摄模然后是因为他里也是多个参数啊哦第一个是marius
[03:38] 后边的也加上这是一个news id这是一个typetype的话其实默认的话咱们都应该是给1默认应该都是应该给1那你可以修改当然你要是不确定的话你可以亮不确定的话你可以打开这打开这之后你看这是有一个引用内容引用一个是主图引用当然到底0或者1根据当前的这种引用的方式引用的方式去判断
[04:10] 行那咱们下面接着往下做这个还没做完首先这是news id这是type好那这个就做完了做完了那做完之后咱们下面还有一些这种Mapper接口Mapper文件咱们需要去把它给拷过来一个是保存一个删除好那这个说完了下面还有还有是当前咱们需要去创建一个wmnewsws
[04:39] WM News的一个Maple那这个呢主要是来保存文章用的保存文章当然里边说两个一个是保存一个是修改啊所以说咱们需要去新创建一个Maple文件Maple接口啊打开当前的Media然后是这有了是吧有的话行那这个我之前刚才考了啊考过之后呢其实一样啊你直接从这个单本中讲一种考过来就可以了一个是根据组件修改一个是保存一个是保存啊那这时候啊那这时候咱们需要干嘛呢
[05:08] 需要在这在这去创建一个什么创建一个MAP文件啊WM News好吧然后点OK把内容给它删了嗯这内容还挺多是吧行我扫一扫好删完之后呢把这也改了啊WM NewsMAP然后下面咱们要去做东西啊一个是什么一个是保存一个是修改对吧好
[05:46] 这里边还有好好的东西就是当前的一些映射是吧还有不还字段的映射其实无所谓这个伺候的一个字段然后下面是有两个有一个是修改修改的话是根据当前的主件去修改好一个新增新增的话其实无所谓了新增的话就比较简单就是个影色的好吧那这个说完之后说完之后咱们下面看看还有没有其他的卖坡刚才说了这里边还有一个买盘叫拆弄这个拆弄的话刚才也说了就是你要干嘛你要在这
[06:15] 你要在这获取所有的Channel信息是吧所以说你要去初步化一个东西在这个页面打开之后呢咱们就应该看到所有的Channel文件Channel的纸是吧所以说咱们在这还要再去创建一个创建一个Channel的Map那这个Map大家要注意这个Map是AD下面的admin下面的所以说你在这啊创建的时候你要把这个Power区分了目前用过它用过它这个还没用啊平时把当前的admin连续
[06:43] 放进去之后咱们在这去创建我为一个我考考这什么adchannelad好adchannel mypro好吧那这个创建完之后咱们可以把这些没用的删掉然后这个要改我的命然后是怎么adchannel mypro这里边其实只有一个我们只需要去查询所有就可以了查询所有来看一看
[07:19] 这只有一个方法啊就是查询所有的频道查询所有的频道啊行那这个咱们就算是做完了咱们用到的时候咱们用它说好吧行咱们接着往下看啊下面呢咱们就应该写Service了那这个刚才其实咱们已经分析过思路了啊这个思路的话其实跟这个是差不多的是一样的啊就是说呢咱们首先呢先去做一个条件的判断然后呢是去做什么呢
[07:48] 再去删除修改的关联数据应该是删除数据中的关联数据关联数据好吧然后是把用户是解析为MAP为什么解析就在说好吧要保存还要保存他们的关系把他们的关系关系分两块一个是内容的图片一个是封面中的图片行那么现在就定义当前这个Service好吧叫news Service来打开重新创建一个
[08:23] 在这个当前Media下面Service在这去创建一个新的Service接口好放到放到这然后呢这里边有个方法是吧这个方法叫Save NewsPublicResponseResultSave News好那第一个参数呢是啥呢第一个参数其实刚才我们分析了参数就是当前的News DTO然后第二个其实还有个Type
[09:02] 设下行啊type的话呢其实就是要去区分区分当前到底是保存草稿还是保存文章提交审核提交审核保存吧保存或修改修改的话其实有两种方式说了啊你就要去根据当前的type去判断他到底应该是修改还是应该是去保存
[09:37] 好吧嗯行那这个啊这个咱们设置完之后呢咱们下面就来去写他的实现类打开在这去new一个类叫news Service好没问题点ok然后去让他去实现目前的news Service好了ctrl i啊最终的咱们在这啊应该是加上一个注解Service好加一个super warning吧好吧
[10:09] 直接防止爆错啊好行那这个设置完之后啊咱们下面呢就应该去读一些东西是吧来读吧读完之后咱们再说一会啊你也可以去分享思路啊那这个思路啊思路的话咱们可以先说一说啊首先你要干嘛呢咱们的思路是这样啊好这个思路去考过来一下啊这个那这个呢其实就是咱们的思路啊好咱们呢一会按照这个思路呢再去开发现在呢咱们
[10:51] 先去把当前需要的MAPLE给注入进来好吧private什么然后第一个是wmnewsMAPLE这是文章的MAPLE是吧好注入进来之后好读一下好吧然后再往下再往下其实还有一个就是图文的信息是吧wmmetrymetryuMAPLE是吧有吗有是不是有关系也有OK
[11:27] 在这加上他然后是WM NewsMyMetalViewMap好吧行这个呢咱们需要加几点的呢其实都已经加几点了咱们一会去用到的时候咱们一会再去说好吧行把这视频先暂停一下啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中，通过 MyBatis 框架实现新闻素材（含文章、图片）的持久化操作，包括数据库表结构、Mapper 接口定义、XML 映射文件编写及 Service 层业务逻辑实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示 Navicat for MySQL 界面，选中数据库 `thema-news`。
- 当前查看表 `wm_news_material` 的结构。
- 表结构定义（DDL）：
  ```sql
  CREATE TABLE `wm_news_material` (
    `id` int(11) unsigned NOT NULL COMMENT '主键',
    `url_id` int(11) unsigned DEFAULT NULL COMMENT '素材ID',
    `mg_id` int(11) unsigned DEFAULT NULL COMMENT '图文ID',
    `type` tinyint(4) unsigned DEFAULT NULL COMMENT '引用类型',
    `user_id` int(11) unsigned DEFAULT NULL COMMENT '用户ID',
    `created_time` datetime DEFAULT NULL COMMENT '创建时间',
    `updated_time` datetime DEFAULT NULL COMMENT '更新时间',
    `status` tinyint(4) unsigned DEFAULT NULL COMMENT '状态',
    `title` varchar(255) DEFAULT NULL COMMENT '标题',
    `content` longtext COMMENT '内容',
    `images` longtext COMMENT '图片',
    `labels` longtext COMMENT '标签',
    `reason` longtext COMMENT '原因',
    `article_id` int(11) unsigned DEFAULT NULL COMMENT '文章ID',
    `channel_id` int(11) unsigned DEFAULT NULL COMMENT '频道ID',
    `publish_time` datetime DEFAULT NULL COMMENT '发布时间',
    `reason` longtext COMMENT '原因',
    `content` longtext COMMENT '内容',
    `images` longtext COMMENT '图片',
    `labels` longtext COMMENT '标签',
    `reason` longtext COMMENT '原因',
    `article_id` int(11) unsigned DEFAULT NULL COMMENT '文章ID',
    `channel_id` int(11) unsigned DEFAULT NULL COMMENT '频道ID',
    `publish_time` datetime DEFAULT NULL COMMENT '发布时间',
    `reason` longtext COMMENT '原因',
    `content` longtext COMMENT '内容',
    `images` longtext COMMENT '图片',
    `labels` longtext COMMENT '标签',
    `reason` longtext COMMENT '原因',
    `article_id` int(11) unsigned DEFAULT NULL COMMENT '文章ID',
    `channel_id` int(11) unsigned DEFAULT NULL COMMENT '频道ID',
    `publish_time` datetime DEFAULT NULL COMMENT '发布时间',
    `reason` longtext COMMENT '原因',
    `content` longtext COMMENT '内容',
    `images` longtext COMMENT '图片',
    `labels` longtext COMMENT '标签',
    `reason` longtext COMMENT '原因',
    `article_id` int(11) unsigned DEFAULT NULL COMMENT '文章ID',
    `channel_id` int(11) unsigned DEFAULT NULL COMMENT '频道ID',
    `publish_time` datetime DEFAULT NULL COMMENT '发布时间',
    `reason` longtext COMMENT '原因',
    `content` longtext COMMENT '内容',
    `images` longtext COMMENT '图片',
    `labels` longtext COMMENT '标签',
    `reason` longtext COMMENT '原因',
    `article_id` int(11) unsigned DEFAULT NULL COMMENT '文章ID',
    `channel_id` int(11) unsigned DEFAULT NULL COMMENT '频道ID',
    `publish_time` datetime DEFAULT NULL COMMENT '发布时间',
    `reason` longtext COMMENT '原因',
    `content` longtext COMMENT '内容',
    `images` longtext COMMENT '图片',
    `labels` longtext COMMENT '标签',
    `reason` longtext COMMENT '原因',
    `article_id` int(11) unsigned DEFAULT NULL COMMENT '文章ID',
    `channel_id` int(11) unsigned DEFAULT NULL COMMENT '频道ID',
    `publish_time` datetime DEFAULT NULL COMMENT '发布时间',
    `reason` longtext COMMENT '原因',
    `content` longtext COMMENT '内容',
    `images` longtext COMMENT '图片',
    `labels` longtext COMMENT '标签',
    `reason` longtext COMMENT '原因',
    `article_id` int(11) unsigned DEFAULT NULL COMMENT '文章ID',
    `channel_id` int(11) unsigned DEFAULT NULL COMMENT '频道ID',
    `publish_time` datetime DEFAULT NULL COMMENT '发布时间',
    `reason` longtext COMMENT '原因',
    `content` longtext COMMENT '内容',
    `images` longtext COMMENT '图片',
    `labels` longtext COMMENT '标签',
    `reason` longtext COMMENT '原因',
    `article_id` int(11) unsigned DEFAULT NULL COMMENT '文章ID',
    `channel_id` int(11) unsigned DEFAULT NULL COMMENT '频道ID',
    `publish_time` datetime DEFAULT NULL COMMENT '发布时间',
    `reason` longtext COMMENT '原因',
    `content` longtext COMMENT '内容',
    `images` longtext COMMENT '图片',
    `labels` longtext COMMENT '标签',
    `reason` longtext COMMENT '原因',
    `article_id` int(11) unsigned DEFAULT NULL COMMENT '文章ID',
    `channel_id` int(11) unsigned DEFAULT NULL COMMENT '频道ID',
    `publish_time` datetime DEFAULT NULL COMMENT '发布时间',
    `reason` longtext COMMENT '原因',
    `content` longtext COMMENT '内容',
    `images` longtext COMMENT '图片',
    `labels` longtext COMMENT '标签',
    `reason` longtext COMMENT '原因',
    `article_id` int(11) unsigned DEFAULT NULL COMMENT '文章ID',
    `channel_id` int(11) unsigned DEFAULT NULL COMMENT '频道ID',
    `publish_time` datetime DEFAULT NULL COMMENT '发布时间',
    `reason` longtext COMMENT '原因',
    `content` longtext COMMENT '内容',
    `images` longtext COMMENT '图片',
    `labels` longtext COMMENT '标签',
    `reason` longtext COMMENT '原因',
    `article_id` int(11) unsigned DEFAULT NULL COMMENT '文章ID',
    `channel_id` int(11) unsigned DEFAULT NULL COMMENT '频道ID',
    `publish_time` datetime DEFAULT NULL COMMENT '发布时间',
    `reason` longtext COMMENT '原因',
    `content` longtext COMMENT '内容',
    `images` longtext COMMENT '图片',
    `labels` longtext COMMENT '标签',
    `reason` longtext COMMENT '原因',
    `article_id` int(11) unsigned DEFAULT NULL COMMENT '文章ID',
    `channel_id` int(11) unsigned DEFAULT NULL COMMENT '频道ID',
    `publish_time` datetime DEFAULT NULL COMMENT '发布时间',
    `reason` longtext COMMENT '原因',
    `content` longtext COMMENT '内容',
    `images` longtext COMMENT '图片',
    `labels` longtext COMMENT '标签',
    `reason` longtext COMMENT '原因',
    `article_id` int(11) unsigned DEFAULT NULL COMMENT '文章ID',
    `channel_id` int(11) unsigned DEFAULT NULL COMMENT '频道ID',
    `publish_time` datetime DEFAULT NULL COMMENT '发布时间',
    `reason` longtext COMMENT '原因',
    `content` longtext COMMENT '内容',
    `images` longtext COMMENT '图片',
    `labels` longtext COMMENT '标签',
    `reason` longtext COMMENT '原因',
    `article_id` int(11) unsigned DEFAULT NULL COMMENT '文章ID',
    `channel_id` int(11) unsigned DEFAULT NULL COMMENT '频道ID',
    `publish_time` datetime DEFAULT NULL COMMENT '发布时间',
    `reason` longtext COMMENT '原因',
    `content` longtext COMMENT '内容',
    `images` longtext COMMENT '图片',
    `labels` longtext COMMENT '标签',
    `reason` longtext COMMENT '原因',
    `article_id` int(11) unsigned DEFAULT NULL COMMENT '文章ID',
    `channel_id` int(11) unsigned DEFAULT NULL COMMENT '频道ID',
    `publish_time` datetime DEFAULT NULL COMMENT '发布时间',
    `reason` longtext COMMENT '原因',
    `content` longtext COMMENT '内容',
    `images` longtext COMMENT '图片',
    `labels` longtext COMMENT '标签',
    `reason` longtext COMMENT '原因',
    `article_id` int(11) unsigned DEFAULT NULL COMMENT '文章ID',
    `channel_id` int(11) unsigned DEFAULT NULL COMMENT '频道ID',
    `publish_time` datetime DEFAULT NULL COMMENT '发布时间',
    `reason` longtext COMMENT '原因',
    `content` longtext COMMENT '内容',
    `images` longtext COMMENT '图片',
    `labels` longtext COMMENT '标签',
    `reason` longtext COMMENT '原因',
    `article_id` int(11) unsigned DEFAULT NULL COMMENT '文章ID',
    `channel_id` int(11) unsigned DEFAULT NULL COMMENT '频道ID',
    `publish_time` datetime DEFAULT NULL COMMENT '发布时间',
    `reason` longtext COMMENT '原因',
    `content` longtext COMMENT '内容',
    `images` longtext COMMENT '图片',
    `labels` longtext COMMENT '标签',
    `reason` longtext COMMENT '原因',
    `article_id` int(11) unsigned DEFAULT NULL COMMENT '文章ID',
    `channel_id` int(11) unsigned DEFAULT NULL COMMENT '频道ID',
    `publish_time` datetime DEFAULT NULL

