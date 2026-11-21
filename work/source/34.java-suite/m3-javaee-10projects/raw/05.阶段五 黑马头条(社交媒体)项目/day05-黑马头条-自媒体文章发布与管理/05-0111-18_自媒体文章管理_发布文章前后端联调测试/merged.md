# 18_自媒体文章管理_发布文章前后端联调测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\18_自媒体文章管理_发布文章前后端联调测试【海量资源尽在 666java.com】.mp4
- 时长 16分45秒（音频 1005s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好这个后台代码写完之后呢咱们下面的就来去集成前端一块来去测试一下啊那好那这样啊我这个后端的已经启动了啊已经启动了这个项目微服务已经启动了启动完之后呢你这时候你可以登录前端123是吧然后点登录完成后呢你这时候你可以点一下这种发布文章首先呢你可以看一下当前这个频道有没有这个频道是不是出来了我说明咱们写那个频道接口是没有问题的啊
[00:33] 然后下面咱可以去输入一条文章是吧比如要随便写这两个标题跟标签随便写然后定时的话你可以去写此刻就是一个时间然后这个内容要去说一下这个内容的话它的里边是嵌入了一个这种跨终端的这种复文本编辑器其实咱们最主要的是有两块内容一个是两个按钮第一个按钮是当前T1第一就是你可以输入文本然后第二个你可以去算是插入一些图片好吧
[01:03] 那这样咱们可以点击一下比如点一些图片然后呢在这比如说你想去输入些东西吧这是文字啊然后呢比如说我在这文字下面想去插入一张图片这个其实它就能去找到素材库中的东西比如说全部和收藏是吧比如说找一张图片然后点进去它就能去嵌入到当前这个文章里边好吧当然你也可以在下面继续讲当然如果不想要了我也可以再删了也可以再删了啊这时候你可以再加一张啊
[01:33] 好加进来之后呢那这个内容你也可以改你也可以改你也可以去修改它你还可以去删除我又不说了这会你可以再加一个文字好吧再加文字总结的文字好吧那加上之后啊那这个文章就算是好了然后下面呢你可以有一个封面的类型有三图三图五图和自动是吧自动的话咱们之前逻辑是还知道吗自动的话就是逻辑就是去找到谁呀
[02:01] 找到当前的这个内容的图片去作为方面是吧行啊那下面就可以去找一个单图啊单图然后你可以再去上传其实上传的话还是咱们在素材库中去找到啊我点确定然后然后呢这时候呢你可以点提交点提交啊啊我这后台啊嗯等你打了没有是吧没有的话这样咱们先看一下能不能成功点提交应该这个是不是新的文章成功了
[02:27] 是吧咱们可以在这刷一下数据库我这个就是WMNews就是当前自媒体文章发布库好点一下点之后你看这个文章是不是来了叫什么111然后是这是时间然后这是时间1是吧审核还没有审核目前的话它这个status1的话就是待发布还有啥呢图片这图片还有问题这图片的话不应该是这样不应该是这样它应该是上面一个文件的ID
[02:55] 就是你这个从FastDBS中返回的一个问题啊和Omibos1啊这个啊这个有问题的有问题的话咱们就来调一下好吧调试的话呢你在这打这点啊打这点咱们可以稍微去改一下比如再去发布一下文章吧好吧二二二是点mycircle选啥都无所谓了啊然后上传一些内容比如3然后找一个图片下边你可以再加一些东西啊好吧
[03:28] 好找一个单图也确定好这时候点提交审核哎就来了是吧来了之后呢咱们可以直接去进入到前的Service去调试啊你让他过来好来了啊首先是判断当前的条件是吧我们要走哎咱们这个内容是有的啊那他是修改吗肯定不是修改因为当前没有ID他往下走好我朝大一些啊好然后这时候呢再往下看是拿到了一个content这个content可以看一下
[03:59] 这个content是不是就是你那个存储的一个content这个content是有特点的他没出在讲啊这content内容的话它是固定的比如说你可以在这右键说的啊好放开之后呢你可以去右键copy一下value然后呢你把它给放到这这个呢你看这个就是咱们的内容你看文本就是text图片就是image看到了吧文本text图片是text都是一些文本啊
[04:29] 好那这个就是一些内容好吧目前咱们只有一张图片那行啊那这个这个咱们那个当前的内容拿到了啊拿到之后呢咱们再再往下看看还有啥啊那往下走当前获取内容中的图片信息两个啊你看当前的这里边是不是只有一张图片呢那就只有一张图片啊这个数量的话只有一个数量只有一个啊现在这时候咱们就去保存保存当前的WM News
[04:57] 它是下面这个用咱们这个并没有去设置当前的自动咱们是singled就是当前的单图好那保存之后咱们可以看一下保存之后呢看WBS News里边有一些数据比如说有content还有其他的那刚才出错的原因呢刚才出错的时候呢是当前image你看当前的image有值吗看下保存完之后是不是这个image是没有值的那这个是什么时候存的还知道吗
[05:29] 这个存的时候呢是保存什么封面跟当前文章的关系的时候他这存的啊咱们可以往下走啊直接到这之后咱们再去测好吧走走走好到这到这之后你可以进入那进入之后呢你可以往下走看看到底哪块错了啊其实最终呢咱们会在这去再去更新一下文章其实更新主要内容就是谁啊就是当前images那很显然可能这句话有问题啊这有问题啊好往下走走走
[05:57] 走咱们看一下这句话到底有什么问题嗯往下走目前的话这里边存的是啥呢存的是的是他存的是他就错了啊他不应该存一个对象咱们应该存的是字幕串是吧所以说在这啊应该再加一个东西再加个东西啊嗯点什么啊加一个这种嗯来个斯图历史啊就加这个东西啊加这个东西之后呢你才能存到买卖普通是一个他的拿到拿到他的一个key好吧拿到的一个外里啊这个外里的话其实就是谁啊就是当前
[06:29] 某一个地址某一个地址啊行那这样咱们这个找到原因之后呢可以重启一下好稍等啊重启完之后呢咱们可以再去测一下再去测一下这样咱们就直接点就可以了一会儿啊等他启动完毕好了是吧好了啊好之后呢你可以点一下提交好来了啊那这样咱们直接可以定位到这啊直接定位到这好吧把这个段点给他去掉了啊往下走这段点也不要了往下走到这了
[07:05] 到日后呢你看这个其实已经拿到数据了你可以看一下Wnews里边这个数据到底对不对你看目前这个数据是不是就是当前图片的地址啊OK咱们直接放行放行完之后呢它就保存成功了咱们可以刷新一下你看最后一条数据是不是就是一个图片的地址啊好那没问题啊那目前这个思路呢咱们算是捋的差不多啊那捋完思路之后啊咱们还是要再去看一下前端那这个前端的话呢简单的去捋一捋啊大家能看懂就可以啊
[07:35] 然后首先这个页面就是在view里边有一个publish有一个index.view就这个页面这个页面里边你看上面是有个表单这个表单的话主要是收取了或者获取了当前你输入的一些数据可以看一下有哪些你看有标题是吧标题这是标题还有什么label标签还有什么频道这个频道的话就是获取的某一个ID
[08:01] 那这个频道其实就是一个Channel List这个Channel List你很显然就是怎么来的在页面当前出车话的时候咱们是不是就要去加载发送后台的接口去拿取当前的所有的Channel咱们也可以看一下这个东西Ctrl C一下然后把它拷到这V看看谁在复制值好吧这是有一个model谁在复制值你看这个是不是获取了一个Channel 4这个Channel 4你可以往后点
[08:32] 点不动是吧你可以到这个publish里边啊publish里边呢可以去找获取所有频道这里边并没有并没有的话可以看一下到底是从哪来的啊说的这有一个get channels就是publish啊应该是就在这里边啊找一找啊get publish叫get什么get channels啊不是publishget channelsget大家看一下啊是不是这东西啊是吧
[09:08] 就这东西啊这有一个这有一个路径这路径的话就在这啊APIChina你可以在这可以可以在这去找APIChinaAPIChina是不是他呀那这个地址是不是跟咱们之前写的地址是一模一样的那这样的话就能拿到数据了啊那行那这是一个这是当前咱们第一个接口啊就是你获取所有的频道那但是咱们还要再还要再去又要说啊又要说呃拿到这个数据之后呢咱们在这去做了一个循环
[09:37] 往上往上往上这最终的是把当前的itemit就是一个频道的ID往后传最终咱们存的时候是肯定是某一个频道的ID这里边没有吗找一找你看这个其实就是频道的ID好吧那行那再往下看再往下看然后还是找到这然后这里边还有个定时定时的话就是有一个时间插件去你输入当前的时间就可以了他付给谁了他付给了一个formData里边一个publishTime
[10:08] 然后你再往下看看还有什么东西啊内容内容他们又在说好吧还有封面封面的话主要是给typetype的话有有有了几个值啊你都是radio吗看到了吧要不你选一要不选三要不选零要不选负一分别对应的是单图三图无图和自动是吧呃还有就是最最后这个啊这个是一个小表单这个表单的话主要呢就是你可以获取当前的图片信息这个图片从哪来的呢哎这个图片呢主要呢就是从咱们之前那个叫什么来着啊之前那个就是
[10:38] 素材里边去获取的素材里边去获取的那行那咱们一块来看一下这个东西是怎么来的你可以找一下里边的一些东西比如说pass不是他找这个好吧看下这个方法当然你也可以去往上看他也他会出发一个方法我看哪个方法说的这个方法其实有两个有两个一个如果说你选的是一一就是单图
[11:08] 是吧要不是三三是三图无图的话就不用上传图片了是吧还有自动的话你也不用上传因为他需要从内容中去找到图片是吧所以说这个他是单图跟你的多三图他处理的方式是不一样的咱们可以看一下这个里边比如说扛车挨护一下去找往下找往下找这个其实最终咱们就会去选择单张图片是吧然后他会选用这个图像这个东西
[11:38] 那这东西呢其实就是获取了当前的什么获取了当前的一个图片信息就这东西看到了吗这个内容大家应该能看懂啊因为它最终呢就是调用谁啊get all image data也就是说啊他就会去获取所有的素材信息那这个咱们之前是写过的啊就是拿到当前的图片内容好吧但里边还有一个条件这个条件的话主要呢就是一些有了size啊配置啊是吧这个东西你可以随便设但这里边有一个东西就是收藏
[12:07] 其实刚才我也演示了比如说你在这儿去上传的时候找三图你去上传的时候你可以点收藏和点全部这时候传的条件是不一样的这时候它查询出来的东西它也不一样是吧行那这个咱们大概说了一下最终它就会去把当前的图片信息附到一个Emitter DataEmitter Data那这个Data其实就是咱们要往后才去传作为什么呢作为什么作为当前
[12:37] 封面的图片就放到了以密纸丝里面好吧行那这是一个东西啊那行那这个啊这个最终的数据啊咱们都能拿到啊也是没有问题的那在这里边还有一个东西就是刚才说了有个详细要说的就是当前的什么内容啊这内容的话呢来往上看啊那图片刚才说的差不多啊内容的话呢就是往上找往上找上传图片哎内容呢全部素材
[13:13] 再往上再往上内容在这内容在这这个是获取内容其实这个它是有一个黑马的组件黑马组件那黑马组件是谁你可以找一找找不着是吧你可以这样你可以往下去找找找这个组件其实就是这个东西这个东西这个东西的话你可以去找到当前的黑马.bue在哪呢compense editor黑马.bue可以找
[13:44] editor.compound这是吧editor.view其实这个呢就是这样这个的意思呢就是咱们要目前要做的一些东西就是它的内容是怎么来的其实这个呢就是自定义的一个编辑器这是咱们前端专门去写的一个东西然后最终的最终量最终它存的时候呢就是你如果说你文本就是纯text如果说你要是图片的话它就存image还有存image好你可以往下看
[14:14] 往下看好这个啊如果说他要是添加的话呢他就是有两种啊一个是一面纸一个是tags一个tags啊那行那这个说完之后啊最终呢咱们就可以从这个编辑器中去获取内容获取到内容之后呢这有一个方法就是这样就是有一个get contentget content啊你也可以看一下当前最终获取的格式其实是这个格式啊也就是说哪个呢也就是当前的我来关了啊也就是当前的这个东西
[14:44] 当你这东西啊他就会把这个内容里边所有的内容啊所有的内容转换为啥呢转换为一个接线啊然后是往后才去传用内容咱们必须要以这样的格式才行因为咱们前台那个用vigas去解析的时候啊必须要有这个格式好吧行啊那这个说完之后啊咱们再往下看最终他发请求是在哪发的啊我说的发请求呢主要说的是那个啥啊主要说的是文章来看一下啊往下走这里边有一个publish
[15:13] 就是publish就是个发布文章这个首先它是获得所有参数这次也是参数获得参数之后又去做了一些判断这个判断的话主要就判断你说你这标题不能小于五个字符也不能大于32个是吧还有就是内容的标签是有怎么着内容不能为空频道不能为空封面为设置咱们都要去判断然后最终在这如果说它这个ID到底有没有没有的话咱们就干嘛呢就是publish当然修改的话咱们现在还没有讲
[15:43] 现在还没有讲还没涉及到目前的话目前的话都是publish他需要去传写参数参数的话就是刚才那些表单好吧他最终会调用他那个publish articles其实你还是到这个publish.js找找啊那这就这东西看到了吗就这个publish articles就把这个参数发请求了他目前的话都是发了一个请求因为因为咱们后台的写的时候应该是写两个没看下
[16:13] 一个是保存文章一个是保存草稿草稿的话咱们并没有做啊但你也可以去测一下你也可以测一下目前的话咱们都是去正常保存都是调用的这个方法其实无所谓是吧这个的话你也可以去专门的去在前台去稍微改一改改成不同的这种请求的方式就可以了好吧那但这个AP articles你可以在这去找啊AP articles其实就是它好吧都是submit
[16:39] 好吧行那这个啊这个流程咱们就说的差不多啊大家呢可以再去看一看

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲一个新闻内容管理系统（“黑马头条”）的前端发布文章功能与后端 Java 服务端处理文章图片上传和内容校验的实现逻辑。

2) 按时间顺序列出每张画面的要点：
画面 1: 登录页面，显示“黑马头条”登录框，要求输入用户名和密码。
画面 2: 发布文章页面，用户正在编辑文章，包含一张图片和多个图片占位符。
画面 3: 在图片上点击后弹出“添加文字”对话框，用于在图片上添加文字。
画面 4: Java 后端代码，`NewsServiceImpl.java` 中的 `coverImagesRelation` 方法，处理文章图片数据，从 JSON 中提取图片数量并创建 `Images` 对象。
画面 5: Java 后端代码，`NewsServiceImpl.java` 中的 `coverImagesRelation` 方法，校验图片类型是否匹配，若不匹配则返回错误。
画面 6: Java 后端代码，`NewsServiceImpl.java` 中的 `coverImagesRelation` 方法，若图片类型匹配，则更新数据库中的图片信息。
画面 7: Vue 前端代码，`index.Vue` 中的 `<el-form-item>` 组件，用于选择频道和发布时间。
画面 8: Vue 前端代码，`publish.js` 文件，定义了 `getChannels`、`publishArticles` 和 `modifyArticles` 等 API 请求函数。
画面 9: Vue 前端代码，`index.Vue` 中的 `<el-select>` 组件，用于选择频道，`placeholder` 为“选择日期时间”。
画面 10: Vue 前端代码，`selectImgList.Vue` 文件，定义了 `getImgData` 函数，用于获取图片列表。
画面 11: Vue 前端代码，`index.Vue` 中的 `<el-tabs>` 组件，用于切换图片展示模式，包含“单图”、“三图”等选项。
画面 12: Vue 前端代码，`heima.Vue` 文件，定义了 `addText` 和 `editText` 函数，用于添加和编辑文字。
画面 13: Vue 前端代码，`selectImgList.Vue` 文件，定义了 `transImage` 函数，用于处理图片类型，`type == "1"` 时为单图，`type == "3"` 时为三图。
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

