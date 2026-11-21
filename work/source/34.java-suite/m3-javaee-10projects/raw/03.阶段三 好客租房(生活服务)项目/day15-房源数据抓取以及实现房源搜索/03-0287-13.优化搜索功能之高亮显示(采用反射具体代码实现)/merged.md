# 13.优化搜索功能之高亮显示（采用反射具体代码实现）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day15-房源数据抓取以及实现房源搜索
- 源文件：03.阶段三 好客租房(生活服务)项目\day15-房源数据抓取以及实现房源搜索\13.优化搜索功能之高亮显示（采用反射具体代码实现）【海量资源尽在 ubkz.com】.mp4
- 时长 22分48秒（音频 1369s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接着继续那么接下来呢我们来优化一下我们的搜索功能前面呢我们只是做了一些基本的实现好那么下面我们来做两个优化一个呢就是去做高亮显示另外一个呢就是做一个分页的一个查询好那我们来看首先来看这个高亮那么这个高亮呢它的操作呢就需要在我们的服务端上去做操作了
[00:24] 那么我们回到我们刚刚所写的这个Service中我们去编写一个高量查询的一个代码逻辑啊那么这个逻辑怎么去写呢我们来看一下啊之前我们的一个查询呢是不是它会自动给我们去做一个数据的一个分装会得到一个我们这样的一个集合最后就可以拿到这样的一个内容了但是呢它自动去分装的一个结果中呢并不包含高量的信息所以我们必须呢去做一个手动处理
[00:52] 即使你在这个位置做了一个指定我需要在做一个这样的高量他也不会有这样的一个返回啊也需要我们手动做处理怎么处理呢那么就在下面这个位置我们需要去实现一个呃叫做我们来看一下啊呃实现一个叫做search啊这个search result Mapper这样的一个接口那我们去去做一个匿名的一个实现new一个他new一个他
[01:19] 好那么在这个里面呢就需要去实现一个map result这样的一个方法那么要注意的是啊一旦我们去设置了这个map然后呢它呢就不会去做一个自动的一个映射也就是说这个里面都需要我们去手动去完成一个映射那么手动完成映射呢就代表着说你不仅仅是需要处理这个高量的这个字段一些非高量字段的一些数据的一些这个
[01:48] 去传到我们对象中也需要我们做一个分装做一个处理那我们来看一下这个代码应该怎么样去编写那么首先我们来看一下这个map result它是不是有这么几个内容传递给我们一个是response一个就是class一个就是这个pageable那么这个是分页相关的数据那么这个就是我们的一些response对吧这个是我们这个类那么也就是说我们在这个位置其实是需要先去拿到我们这个response它里面的什么呢
[02:17] 是不是可以拿到应该的hex那么这个是不是他的一个命中的一个这个数据对吧然后呢我们去做一个这样的一个判断那么如果如果什么呢如果是应该是他那么如果空等于他的话那么就意味着什么那么就意味着我们是不是没有命中任何的一些这个东西我们来看一下
[02:44] 它不是空那就应该是它等于0因为它是个none然后或者是等于0那么就是没有命中没有命中数据没有命中数据我们应该去return一个new或者我们先return一个none那么returnnone其实有问题的那么你即使没有命中数据其实你也需要去把我们的对象返回所以我们这块不应该去return new
[03:14] 不应该去return null,应该去return new一个我们这个对象就是聚合的这样的一个配置对象那么我们去new一个它具体的一个实现类然后它这个里面的需要去传递一些内容那么首先我们来看一下它是需要一个list还需要一个什么呢配置able那么这个吧咱们把这个信息都给它传递回去那么第一个是list
[03:42] 那么list呢我们是不是可以给它来一个空的list对吧connection然后呢来空的一个list然后呢第二个参数呢就是pageable那么就我们把这个pageable传回去然后呢还有呢第三个参数就是0就是它的一个这个长度我们来看一下是不是应该这样去写它的一个total就是一个数我们查询的数据的一个数据量
[04:10] 数据量大小那么我们给他返回0就可以了这个是在没有命中数据的情况下面那么如果我们走到下面来是不是这个数据他就已经命中了命中之后我们其实就需要对他去做一个便利了对吧我们应该来一个便利便利谁就是 response点get head然后他拿到的是一个什么来看一下他拿到的一个search search head那么我们继续再去点点这个里面
[04:40] get这个我们来看一下getheight那么这样的话就会拿到这样的一个search height我们把这个改一下拿到这个对象那么通过这个search height我们就可以去拿到它里面的一些这个内容比如说可以get什么source as map就可以拿到这样的一个map再去做一些相关的一些操作那么接下来我们在这个里面要注意
[05:08] 那么现在我们这个里面是不是拿到都是我们一条一条的数据对吧那我们就需要去做一些这个分装那么也就是说需要在外面我们首先有要有一个list去接收去接收我们这个对象那么我们写一个就叫list等于new一个arriv list好嘞那么写给他然后在这个位置我们需要去new一个我们这个对象但是我们在这个位置要注意虽然我们在这个位置使用的是这个host data
[05:35] 但是为了我们的代码通用性在这个位置我们就不使用直接使用这个对象了而是使用什么呢使用反射来去做因为通过这个范形是不是也可以去拿到一个反射然后去做一些相关的一些操作这样的话我们的代码性是不是就更加的通用对不对好,我们来看一下怎么样去做那么首先需要在这个位置我们先拿到一个t这个对象然后它等于什么呢
[06:04] 或者说我们来一个obj吧然后呢它等于我们通过一个reflect然后呢有一个utils这个是sprint的工具类点然后呢我们去new一个叫get我们看一下啊这个里面有一个叫做我们去获取啊获取它的一个获取我们新的一个对象来看一下啊
[06:31] 怎么会没有呢我们来看一下应该是有我们看一下这个代码它应该是有应该是我们要通过往下面走然后再找一下那么是在这个位置然后在这个位置new instance有但是为什么没有new instance那么是不是我们导的这个包有点问题呢
[07:02] 刚刚我们可能搞的包有点问题那么我们应该使用的是他在 call 里面的应该是用的是他这个里 call 里面的有一个叫 new instance然后我们需要谁需要我们这个 class然后去就说我们通过他的去得到一个对象那么不能用 t 那就 object叫 object
[07:29] 拿到这个object那么拿到之后呢我们就可以往这个里面去给他去丢数据了对吧那么怎么样去丢呢首先呢我们是需要拿到你这个对象中的每一个这个数据那么怎么拿到呢拿到它然后呢get有一个get source是不是就是我们这个原数据然后呢as map那么就会去作为一个map去返回那么我们就拿到一个这个map吧那么拿到这个map那么我们是不是就可以对它去做便利了对吧那么我们也
[07:58] 简单来写就这样来写然后呢去做一个便利他呢来一个entry set然后呢然后这个位置这个位置应该是我们看啊他拿到的是一个这个entry set那么在这个位置也应该去通过一个map点entry set再去做一个获取这样才是比较对的啊那么我们拿到他之后呢要注意的是这个里面get key那么get key呢其实就是
[08:28] get key其实就是我们的一个拿到数据的一个这个name对吧然后呢get valueget keyget key就是我们的一个value也就是我们那个字段名那么get value就是值那么我们就需要去找到这个对象这个属性给他把值呢写回去那么怎么样去写那么通过一个fieldfield utils然后这个是apache浪包下面的这样的一个这样的一个工具包然后呢我们去
[08:57] 去写入一个Field写入一个Field的一个数据那么写入一个Field然后他接收的是应该是四个这个参数四个参数那么首先第一个是这个Field第二个是Target你的一个写入的一个写入的一个这个目标对吧然后呢然后呢这个是他的一个Value然后呢这个是他的一个这个是否是强制去写入就是说如果你是一个Private
[09:25] 就是私有的话那么就需要去做一个强制的一个写入那么现在我们显然是私有所以说这个我们要把它设置为错所以说我们来调用四个参数的这个方法好,那我们来看一下那么writer去写入进去来看一下去写,那我们就调用调用它然后首先第一个是Field那么Field我们先要去拿到这个Field对吧来看一下怎么去拿那么我们来看一下它的几个参数我们来看一下
[09:52] 那么其实它有这个是吧这个参数那么它首先第一个呢是一个其实它还有上面这个参数这个可以直接是一个object是目标然后呢field name那么我们其实选择这个可能会更合适一点那么首先第一个呢我们把这个obj给它第二个呢就是我们去传入的一个我们的一个这个属性名那么就通过这个点点get什么keyget key
[10:21] 然后第三个就是我们要传入的值点get value然后就是设置为一个true就强制写入就是这样的一个操作它会有一个看一下应该是在这个位置会有点会有点这个问题就是它的一个类型的问题我们来看那么这个类型这个问题我们就给它去限制一下限制拿到这个位置拿就是来一个stream来一个object好这样的话拿到是不是就就就OK了
[10:50] 然后呢这个位置呢有异常那么异常呢我们就给他去做一个这个补货吧那么我们就直接来一个try cut的一个补货那么到这个位置呢要注意啊我们只做了什么事情呢我们只做了这个非高量字段的这个数据的写入啊写入这个操作那么高量呢是不是还没有去做呀那么接下来我们才需要去
[11:17] 处理我们这个高量那么高量怎么去玩呢我们还是需要这个susheat去拿点get一个这个highland field拿到它那么拿到它之后它呢也是一个我们来看一下它呢拿到是一个map那么我们是不是直接对它就可以做一个便利做一个便利那么怎么去便利呢还是通过一个这个复循环去做一个便利复循环去做一个便利
[11:46] 然后我们要去遍历map那么还是去把它转成一个entry set那么所对应的是不是拿到一个map entry对吧然后我们来看一下,拿到这个entry好,然后这个里面怎么去拿那么首先可以看到它的key也是这么串也就是它的高量那个字段后面高量这个值那么所以我们需要拿到它高量的值这个高量值稍微麻烦一点那么get value然后就需要
[12:15] 获取它的fragment然后它本身就是有因为有会有多个这样的一个分割那么我们还需要拿到它的一个这个叫是一个宿主然后我们还需要对这个宿主继续做便利这话可能会稍微有点麻烦一点稍微的麻烦一点这样的话可以保证我们拿数据比较全然后这个位置我们还需要写一个streambuilder然后sb等于new一个streambuilder
[12:44] 因为我们去做一个收集啊那么sb.append去添加谁呢就是fragment然后呢toString拿到它里面的一个内容去把它收集起来就可以了然后呢我们再把它再写到我们的一个这个字段里面去那么哪个字段呢这个就关键了啊这个就是我们去写入我们写入的高量写入高量的这个内容那么这个看一下怎么玩呢
[13:14] OBJ还是我们的这个对象没有问题那么第二个呢就是Key呢就是拿到它然后呢值呢就是要注意了不是这个S3的value而是谁呢而是拿到SB然后呢toString拿到它的一个值去给它去做一个写入好那么到这里呢我们是不是基本上就完成了这个数据的一个编写啊最后呢return就可以了return啊return谁哎还没有那么我们是不是写了一个OBJ还没有把它加到集合里面去啊
[13:43] 那么怎么加集合呢是不是应该上面订一个list点按的点按的添加一个obj那么它显然也会有一个这个就是类型转化错误那么我们还是需要把前面的这个改成t改成t然后呢把这个做一个强转就好了做一个这样的一个强转他们就会肯定会转成一个这样的一个对象然后呢我们还是去new一个它的一个这个实现然后呢去传递这么几个内容跟上面这个是一样的
[14:12] 首先第一个集合就这个list那第二个呢第二个呢就是这个PageAble对吧PageAble那么我们看一下传递它传递它那么我们是不是还需要拿到拿到一个数据的长度数据长度其实就是上面的它对吧拿到它这个就是我们数据的一个总的一个长度OK好那么现在我们是基本上是不是已经就实现了这样的一个这个就是我们手动吧
[14:42] 去做这样的一个映射的一个这样代码逻辑那我们在这个位置打一个断点然后呢把我们这个服务呢重新跑起来我们来做一个测试啊然后把这个API这个server停掉然后呢做一个debug的一个启动那么API这个API server然后debug走然后等待它的一个启动好那么现在这个服务呢就跑起来了我们来做一个测试啊还是刚刚我们那个查询来看一下啊比如说我们去查询这个配置占据1对吧新村走
[15:10] 那我们来看一下哦他没有去执行我们这个逻辑啊为什么没有去执行呢呃原因是我们呃是不是前面做过这个缓存呢那么我们就来一个比如说来一个新村然后呢来一个新吧看会怎么样走那么我们看到呃断点呢已经就进入了好那么我们来跟一下这个断点的逻辑啊然后呢拿到他的响应的值发现他是有内容的并不是没有然后呢往下面走走拿到一个这个object对吧
[15:40] 然后呢继续往下面走那么拿到我们这个拿到这个entry看一下这个entry啊entry是什么内容呢我们来看一下entryentry呢就是我们的image图片然后呢我们去强制去写到我们的这个对象里面去那么这个object就是我们刚刚所创建的这个对象啊是不是就这个host date这样的一个对象然后呢去把它写进去走那么写进去之后啊那么我会发现我们的obj里面看一下啊那么obj里面
[16:09] 它其实就已经有了一个数据了看到没有在这个位置是不是已经有了一个数据了OK好那我们接着继续让它去写入写入一个两个没有问题没有问题对吧没有问题往下走走没有问题走走走等待它写入走没有问题依然是OK的走好那么我们继续让它写入哎呀出问题了那么什么问题呢我们去通过一下来看一下这个日志的输出那么在日志输出里面我们会发现
[16:41] 他有一个问题就是他不能够去写入一个什么的这个URL就说我们的数据啊在响应回来的数据中的是包含了谁的包含了这个URL但是呢在我们对象中是没有所以你这样去写入是不对的所以我们需要在前面做一个判断啊怎么判断呢就是我们通过一个field的field点然后呢我们去get一个field然后呢这个class呢就是这个
[17:11] object它是需要class我们看一下get field它是需要class那就是我们上面的classZZ然后字段名称那就是我们的 entryget什么key字段名然后它拿到的field判断是不是等于空是不是就OK了那么这个field如果我们发现如果发现什么
[17:35] 如果我们发现这个空等于这个field那么就代表我们这个字段是不存在的对吧那么就是我们的continue继续执行是不是就OK了好那我们再来重启做一个测试好那么我们再继续测试看一下它效果会怎么样然后发送请求走然后它是不是就进入我们刚刚这个断点的这个位置然后我们走走这些都没有问题我们就直接通过吧然后我们进入高亮这个位置在这个位置打一个断点
[18:05] 然后通过走那么现在显然是不是我们的看一下我们的obj对象那么obj是在这那么点开来看一下这个里面怎么没有数据obj它是没有分装到数据吗我们来看一下应该是有分装到有这个是有然后我看一下如果
[18:35] 刚刚我们这个逻辑是不是有点问题了如果它等于空的话就continue应该是对的但是为什么没有分装到数据呢就比较奇怪那我们就通过吧我们再来看一下那么把这个断点先拿掉走然后呢我们再来执行一下看一下到底什么情况它已经拿到数据了但是这个标题是ok了但是其他的不太ok那么也就是我们刚刚的逻辑它有点问题有点问题那我们来看一下到底什么问题然后呢走
[19:08] 这个已经被缓存了再来一个2走然后呢往下面走看一下啊走走没有问题走走然后拿到一个对象object的对象没问题然后呢走我们来看一下啊这一块这个它是有有点问题的就是我们这个entity然后呢拿到一个get keyget key是一个imager然后呢在我们这个class中
[19:38] 这个里面它应该是有啊应该是有我们的一个这个image的但是就会比较奇怪啊它为什么没有呢这个我们来看一下啊这个是hostdate然后点一下它然后呢hostdate这个里面这个里面啊是有我们的这个属性但是它的判断的结果呢是没有
[20:07] 那我们就需要来看一下到底是什么情况那么我们来看一下到底什么情况在这个位置应该是他丢了一个东西就是get field他还有一个就是说还有这个参数就是我们要强制去读取他这个私有的这个属性要不然你读不到所以说我们这个位置还是缺一个什么的缺一个true这个参数导致我们是不是没有读到导致我们没有读到这个字段那我们再去重启一下等待他的一个执行
[20:36] 好那么我们接着继续再来做一次测试然后呢我们走请求看他会怎么样呢走走走拿到这回就对了没有问题那么我们下面这个位置打一个断点然后呢通过然后呢我们来看一下我们这个把这个断点就拿掉吧上面这个断点拿掉走通过然后呢我们去看一下我们的这个高量的处理啊那么高量处理我们就已经拿到这个SB里面其实拿到数据了就高量处理然后再把它回写到我们这个
[21:06] 字段中就可以了而这个字段呢就是我们的一个title然后就给写回去了然后呢通过走那么最终的一个把这个断点就拿掉了走那么最终的一个结果呢就是我们刚刚所看到这样的结果那么所有的数据是不是就基本上都有了对吧都有了然后呢这高亮显示也OK其他数据也OK但是这个里面还有一个小问题就是这个ID呢它还没有那么这个ID怎么做呢那么我们还需要在上面最上面这个位置啊当你去拿到obj的时候呢就需要给它去
[21:36] 去做一个写入一个ID还需要把这个拷贝过来拷贝给他然后呢给这个obj去写一个谁呢注意我们这个就只能写死了这个ID然后呢去拿到他的一个这个value那么怎么拿呢那就是那就是这个我们通过这个src-hat点get点hat点get什么呢get有一个ID看到了吗有个ID
[22:05] 去测这样的一个写入才会拿到数据啊那我们依然呢把这个服务呢重启一下那么等待它的一个重启好那么我们接着继续往下面看啊那么我们再来做一个测试就是把它设置为这个第三页啊走那么看一下这个结果会怎么样然后呢我们就直接放行吧然后呢这个就通过了然后呢来看一下啊那么这个ID是不是也有了这个高亮是不是也有了其他字段是不是也有了那么显然呢我们现在是不是已经就
[22:34] 实现了这样的一个接口的一个高量对吧就是我们代码的逻辑我们就写完了那么下面我们需要去整合到我们的一个前端去做一个显示那这样我们先把这个视频先停一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解如何在 Elasticsearch 搜索结果中实现高亮显示功能，主要通过自定义 SearchResultsMapper 类和 FieldUtils 工具类完成。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程讲义 PDF 的目录结构，当前章节为“4.1、高亮”，并预览了代码编辑器中的部分代码。
画面 2: 在 SearchService.java 中，使用 NativeSearchQueryBuilder 构建搜索查询，代码中高亮了 AggregatedPageImpl 类型。
画面 3: 在 SearchResultsMapper 类中，定义了 mapResults 方法，用于将搜索响应映射为 AggregatedPage，代码中高亮了 NewInstance 类型的建议。
画面 4: 在 SearchResultsMapper 类中，代码逻辑用于遍历搜索结果，通过反射工具类 ReflectUtils 获取对象字段并写入。
画面 5: 在 SearchResultsMapper 类中，代码逻辑用于遍历搜索结果的源数据（sourceAsMap），并使用 FieldUtils.writeField 方法写入对象字段。
画面 6: 在 SearchResultsMapper 类中，代码逻辑用于处理非英文字段，使用反射获取字段并写入对象。
画面 7: 在 SearchResultsMapper 类中，代码逻辑用于处理高亮字段，使用 StringBuilder 拼接高亮片段。
画面 8: 在 SearchResultsMapper 类中，代码逻辑用于将高亮片段写入对象字段，使用 FieldUtils.writeField 方法。
画面 9: 在 SearchResultsMapper 类中，代码逻辑用于处理高亮字段，使用 StringBuilder 拼接高亮片段。
画面 10: 在 SearchResultsMapper 类中，代码逻辑用于获取对象字段，使用 FieldUtils.getField 方法。
画面 11: 在 SearchResultsMapper 类中，代码逻辑用于处理高亮字段，使用 StringBuilder 拼接高亮片段。
画面 12: 展示 HouseData.java 类的定义，使用 @Document 注解指定索引名和类型。
画面 13: 在 SearchResultsMapper 类中，代码逻辑用于将高亮片段写入对象字段，使用 FieldUtils.writeField 方法。
画面 14: 展示课程讲义 PDF 的目录结构，当前章节为“4.1、高亮”，页面为空白。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
.house-title{
    overflow: hidden;
    white-space: nowrap;
}
```

画面 2:
```java
SearchQuery searchQuery = new NativeSearchQueryBuilder()
        .with()
        .with()
        .build();
AggregatedPage<?> AggregatedPageImpl<...> { ... }
return new AggregatedPageImpl<...>(...);
return new SearchResult(housePage.getTotalPages(), housePage.getContent());
```

画面 3:
```java
HouseData.class, new SearchResultMapper() {
    @Override
    public <T> AggregatedPage<T> mapResults(SearchResponse response, Class<T> clazz) {
        if (response.getHits().totalHits == 0) {
            return new AggregatedPageImpl<>(Collections.emptyList(), pageable,
                    Collections.emptyList(), 0L);
        }
        List<T> list = new ArrayList<>();
        return new AggregatedPageImpl<>(list, pageable, Collections.emptyList(), 0L);
    }
}
```

画面 4:
```java
List<T> result = new ArrayList<>();
if (response.getHits().totalHits == 0) {
    return new AggregatedPageImpl<>(Collections.emptyList(), pageable,
            Collections.emptyList(), 0L);
}
for (SearchHit searchHit : response.getHits()) {
    // 通过反射导入数据到对象中
    T obj = ReflectUtils.newInstance(clazz);
    searchHit.getId(), true);
    try {
        FieldUtils.writeField(obj, entry.getKey(), entry.getValue(), true);
    } catch (IllegalAccessException e) {
        e.printStackTrace();
    }
    Map<String, Object> sourceAsMap = searchHit.getSourceAsMap();
    for (Map.Entry<String, Object> entry : sourceAsMap.entrySet()) {
        Field field = FieldUtils.getField(clazz, entry.getKey(), true);
        if (null == field) {
            continue;
        }
        try {
            FieldUtils.writeField(obj, entry.getKey(), entry.getValue(), true);
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        }
    }
    list.add(obj);
}
return new SearchResult(housePage.getTotalPages(), housePage.getContent());
```

画面 5:
```java
if (response.getHits().totalHits == 0) {
    return new AggregatedPageImpl<>(Collections.emptyList(), pageable,
            Collections.emptyList(), 0L);
}
List<T> list = new ArrayList<>();
for (SearchHit searchHit : response.getHits()) {
    Object obj = ReflectUtils.newInstance(clazz);
    for (Map.Entry<String, Object> entry : searchHit.getSourceAsMap().entrySet()) {
        Field field = FieldUtils.getField(clazz, entry.getKey(), true);
        if (null == field) {
            continue;
        }
        try {
            FieldUtils.writeField(obj, entry.getKey(), entry.getValue(), true);
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        }
    }
    list.add(obj);
}
return new SearchResult(housePage.getTotalPages(), housePage.getContent());
```

画面 6:
```java
int
Integer (java.lang)
IllegalAccessError (java.lang)
IllegalArgumentException (java.lang)
IllegalMonitorStateException (java.lang)
IllegalStateException (java.lang)
IllegalThreadStateException (java.lang)
IncompatibleClassChangeError (java.lang)
IndexOutOfBoundsException (java.lang)
```

画面 7:
```java
for (Map.Entry<String, Object> entry : searchHit.getSourceAsMap().entrySet()) {
    try {
        FieldUtils.writeField(obj, entry.getKey(), entry.getValue(), true);
    } catch (IllegalAccessException e) {
        e.printStackTrace();
    }
}
for (Map.Entry<String, HighlightField> entry : searchHit.getHighlightFields().entrySet()) {
    StringBuilder sb = new StringBuilder();
    for (Text fragment : entry.getValue().getFragments()) {
        sb.append(fragment.toString());
    }
    try {
        FieldUtils.writeField(obj, entry.getKey(), sb.toString(), true);
    } catch (IllegalAccessException e) {
        e.printStackTrace();
    }
    list.add(obj);
}
return new AggregatedPageImpl<>(list, pageable, Collections.emptyList(), 0L);
```

画面 8:
```java
for (Map.Entry<String, HighlightField> entry : searchHit.getHighlightFields().entrySet()) {
    StringBuilder sb = new StringBuilder();
    for (Text fragment : entry.getValue().getFragments()) {
        sb.append(fragment.toString());
    }
    try {
        FieldUtils.writeField(obj, entry.getKey(), sb.toString(), true);
    } catch (IllegalAccessException e) {
        e.printStackTrace();
    }
    list.add(obj);
}
return new AggregatedPageImpl<>(list, pageable, Collections.emptyList(), 0L);
```

画面 9:
```java
List<T> list = new ArrayList<>();
for (SearchHit searchHit : response.getHits()) {
    // 非英文字段的数据写入
    for (Map.Entry<String, Object> entry : searchHit.getSourceAsMap().entrySet()) {
        try {
            FieldUtils.writeField(obj, entry.getKey(), entry.getValue(), true);
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        }
    }
    for (Map.Entry<String, HighlightField> entry : searchHit.getHighlightFields().entrySet()) {
        StringBuilder sb = new StringBuilder();
        for (Text fragment : entry.getValue().getFragments()) {
            sb.append(fragment.toString());
        }
        try {
            FieldUtils.writeField(obj, entry.getKey(), sb.toString(), true);
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        }
        list.add(obj);
    }
}
return new AggregatedPageImpl<>(list, pageable, Collections.emptyList(), 0L);
```

画面 10:
```java
FieldUtils.getField(Class<?> cla, String fieldName)
FieldUtils.getAllFields(Class<?> cla)
FieldUtils.getDeclaredFields(Class<?> cla)
FieldUtils.getDeclaredField(Class<?> cla, String fieldName)
FieldUtils.getDeclaredField(Class<?> cla, String fieldName, boolean forceAccess)
FieldUtils.getFieldsListWithAnnotation(Class<?> cla, Class<? extends Annotation> annotation)
```

画面 11:
```java
for (Map.Entry<String, HighlightField> entry : searchHit.getHighlightFields().entrySet()) {
    StringBuilder sb = new StringBuilder();
    for (Text fragment : entry.getValue().getFragments()) {
        sb.append(fragment.toString());
    }
    try {
        FieldUtils.writeField(obj, entry.getKey(), sb.toString(), true);
    } catch (IllegalAccessException e) {
        e.printStackTrace();
    }
    list.add(obj);
}
return new AggregatedPageImpl<>(list, pageable, Collections.emptyList(), 0L);
```

画面 12:
```java
@Data
@AllArgsConstructor
@NoArgsConstructor
@Document(indexName = "haoke", type = "house", createIndex = false)
public class HouseData {
    @Id
    private String id;
    private String title;
    private String rent;
    private String floor;
    private String image;
    private String orientation;
    private String houseType;
    private String rentMethod;
    private String time;
}
```

画面 13:
```java
for (Map.Entry<String, HighlightField> entry : searchHit.getHighlightFields().entrySet()) {
    StringBuilder sb = new StringBuilder();
    for (Text fragment :

