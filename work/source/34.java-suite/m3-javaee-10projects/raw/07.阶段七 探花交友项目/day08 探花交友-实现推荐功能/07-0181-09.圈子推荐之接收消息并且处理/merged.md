# 09.圈子推荐之接收消息并且处理

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\09.圈子推荐之接收消息并且处理_【海量资源尽在 666java.com】.mp4
- 时长 24分2秒（音频 1442s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接着继续那么前面呢我们已经完成了消息的一个发送那么接下来呢我们就来处理我们的消息啊所以说我们需要去创建一个工程来去接收消息那么这个工程的名字呢我们就把它称之为叫做Rickmong的然后呢就是我们的其实就是推荐了处理我们推荐的这个消息啊那我们来拷贝一下那么在这个里面呢我们来创建一个这个module啊那么点击这个next
[00:29] 然后往下面去走把这个itacast改成这个my-tank-recommend然后呢下一步啊然后呢我们去拷贝一下它然后呢点击finish完成那么这样的话呢我们这个工程呢就创建好了那么接下来呢我们就把一些相关的一些依赖呢我们都拷贝进来把这个dependence然后呢去拷贝一下然后呢把它啊拷贝到这ok
[00:56] 好那么这样的话我们就把所需要的依赖就考进来了那我们来看一下需要哪些依赖那么首先是这个SpinBoot然后StarWeb然后Test这个都是SpinBoot相关的一些依赖还有我们的Redis MongoDB然后一些常用的一些工具包这个CommerceLangIO然后有RockMQ相关的一些依赖
[01:20] 然后海浪book以及我们的这个时间处理啊那么这是基本的一些这个依赖好那么接下来呢我们就可以在我们的工程中啊去编写一些相关的一些逻辑了当然了首先我们需要把这个配置文件是不是先给他搞定对吧那我们写一个obligation of properties这样的一个文件那么写到这个里面来啊写一个他然后呢把配置文件内容呢我们来拷贝一下拷贝到这个里面来
[01:49] 那么在这个配置文件中啊我们可以看到那么我们指定它的一个application的一个name然后它的端口然后呢rock.mq相关的一些配置然后呢release相关的配置然后呢再加上什么呢mongodb相关的一些配置那么就是一些基本的所需要的一些这种配置
[02:08] 那么这样的话呢我们就可以去做具体的实现了对吧然后当然了我们还需要去写一个我们这个log4j那么我们把这个呢也创建出来吧那么就这个log4j的一个配置文件啊非常简单的啊这样的一个配置文件当然了我们接下来呢是不是就可以去编写相关的一些这个逻辑了对吧那么首先第一个呢我们就需要去
[02:35] 把我们的这个数据啊就说在前面的我们其实讲到那么我们LockedMQ这个是不是去把消息发送到这个里面来然后呢我们需要有一个推荐系统然后去接收这个消息并且呢把它去写入到我们的MongoDB里面来那么在写入MongoDB那么就需要有一个我们的一个数据结构了那么接下来呢我们来看一下这个数据结构
[03:00] 那么把它称之为叫什么呢Recommend圈子这样的一个数据结构那么我们就直接就来看一下它这个结构吧那么在这个结构中的其实是非常简单的一个结构就是用于满足我们的一个推荐模型的这样的一个结构那么推荐模型的最标准的或者说我们至少你是需要有三个字段对吧一个呢就是你的用户ID那就它
[03:28] 那么另外一个呢就是我们的public id要注意了这个就是指的我们所前面所添加的那个pid那个字段这第二个那么第三个呢就是我们这个score一个得分score得分那么至少是需要这三个对不对啊那么其实呢我们还需要什么呢第四个这个字段就是data这个是不是可以用于我们对数据去做一个这个划分
[03:54] 那么哪些用于做测试哪些用意去做我们的一个训练我们的推荐模型所以说我们这个Data时间戳其实也是需要的也就是说我们需要有这四个这样的一个字段那么上面这个ID这个字段其实就是我们这个对象在我们的MongoDB中的一个组件OK好那么我们就把这个内容就拷贝到拷贝到我们的这个工程中那么首先我们先来去打一个包
[04:24] 那么就是在我们的这个里面创建一个这个包啊就是Pojo啊这个包然后呢我们把我们这个就是对象啊拷贝到我们这个包里面来就是非常简单的啊这样的一个对象但是呢大家一定要去理解这么几个字段啊它的一个意义啊OK好那么接下来呢我们就来编写具体的逻辑了那么就需要去创建不同的一些包了那么我们需要创建一个
[04:52] 我们的一个message这个包那我们就把它也创建出来啊message啊message好那么这样的话是不是有了这个message包了呃当然了我们还是需要有一个启动类的对吧那我们来拷贝一下吧那我们拷贝我们这个server下面这个启动类那我们把它拷贝到这个里面来那我把它称之为叫什么recommend啊recommend recommend好那么这是我们的recommend obligation然后呢我们来看这个里面的一些配置啊
[05:22] 那么首先我们来看一下这个我们扫描包肯定是不需要的对不对然后我们也不需要把它排除掉如果把这个排掉的话那我芒果DP可能就不能使用了好那么把这个就格式化一下然后我们来拷贝一下那么所需要就是Rickmonger的application这样的一个对象这样的class
[05:43] 好然后呢我们把它呢就关掉啊这样的话就OK这个没有问题啊这个也没有问题这个没有问题了好那么接下来呢我们就需要在这个message中啊我们去编写一些相关的逻辑那我们需要去写一个什么呢就叫这个圈子啊message啊consumer啊这样的一个对象好那我们去写一下他他呢我们来看一下啊首先呢他是需要去实现我们的一个这个接口啊就是RocketMQ的一个list呢
[06:12] 这样的一个接口然后呢他需要去实现这个接口中的一些这个方法就是一个on message这个方法那么当我们有消息之后呢就会去执行这个方法然后呢我们这个上面呢这个类上面啊还需要去添加两个这个注解那么第一个呢就是这个comment啊comment这样的一个注解就是把它加入到我们的一个这个spin容器那第二个呢就是我们的rog的mq的一个message listener
[06:41] 然后呢第一个指定我们的一个topic第二呢指定我们的一个consumer的一个组哎呦ok好那么指定这俩之后呢那我们就相当于我们去监听了这个topic然后呢我们这个topic一旦有消息的话那么就会执行我们这个里面的这个方法那么具体的方法逻辑是不是就是在这个里面去做一个完成了那我把这个s改成message啊呃messageok好那么下面我们就来编写这个具体的业务逻辑
[07:09] 那么首先呢我们需要呢把我们这个消息呢我们来处理一下那么这个消息接收到的肯定是一个json对吧那我们就需要对它去做一个反序列化拿到我们消息中的一些这个所需要的数据啊那我们去定义一个我们的一个叫什么呢就是object Mapper就是json啊那么定义一个static吧进一代的final一个object json
[07:37] object一个map然后定一个map等于去new一个object mapOK好那么有了map之后那么下面我们就去做一个反序列化叫什么read value然后message应该我们就用什么read tree用tree就可以了这样的话会比较简单一些那么我们去接收一下接收一下那么这个就是一个json node
[08:07] 那么然后呢我们来看一下这个是呃有异常那么有异常的我们就来捕获一下我们这个异常那么就去拆开来处理一下那么我们去把这个io去掉就直接用exception去做一个捕获呃然后呢上面呢我们还是把我们的log4j啊这个去定义出来然后呢static啊fano然后呢写一个log呃log然后呢我们去定义一下它log等于然后呢我们定义一个
[08:37] log点log factorylog factory然后点get log然后呢去得到一个trends message consumer点class点class好那么这样的话有了这个log对象然后呢我们去记录一下日志那么就是这个就是什么呢就是我们的这个消息处理失败失败然后呢我们把这个message我们给它呢去打印出来message打印出来
[09:07] 好嘞好那么有了这个今天node之后啊那么接下来我们就可以获取到相关的一些这个值了那么首先呢我们来参考一下之前呢我们所发送这个消息中的一些这个内容啊那我们来看一下那么这个是我们前面所发送的这个消息啊大概有这么四个啊四个那么我们就来看一下
[09:30] 好那么这四个这个内容啊那么我们就对它呢把它丢到上面吧丢到这来然后呢我们对它去做一个这个注释好那么接下来呢我们就来获取到这些内容啊那么首先呢第一个是type点点给了什么呢这个type啊type然后呢as什么的lungas这个int啊它是一个int类型的
[09:54] 好那我们来接受一下这个的就是一个这个type这第一个那第二个的是public id这个呢是一个none类型这个是一个stream类型的那么我们定义一个stream类型的一个public id等于什么呢等于 json node.get谁呢get他.as一个text好那么这个呢就搞定那么接下来呢
[10:21] 这个Data是Lung类型的对吧那我们就用去Lung去接收那么Data那么拿到一个Data as什么呢as Lung好这样的话也就OK了下面还有个UID那么UID也是Lung类型那直接写OK没有问题还有谁呢是PIDPID然后呢这个是PID也是Lung类型的没有问题好那么到这里呢我们是不是已经就拿到我们所需要的一些这个数据了对吧
[10:48] 那么接下来呢我们就需要对我们这个不同这个type呢去做出相关的一些处理因为每一个type它所对应的这个计分的规则呢是不一样的对吧所以我们需要对它做一些这个处理啊当然我们在这个位置吧先来去new一个对象啊那么就是刚刚我们所写这个叫做圈子圈子我们叫什么呢叫来看一下啊就我们刚刚所写的这个pose中的
[11:17] 叫做recommend圈子圈子在后面那么也就是说这个叫recommend圈子对象然后呢这个对象等于去new一个又一个他然后呢我们可以先给他去填充一些所需要的一些这个数据recommend.set什么呢setPublicID那么要注意这个中的PublicID它就是什么呢lang类型的所以需要填充的是这个PID这块别搞错
[11:45] 然后我们再来看一下那么还需要去填充的是一个这个score得分一会来填充那么date那就是刚刚的这个什么呢date还需要填充谁呢就是这个ID那么这个是一个叫做object IDget得到一个新的一个ID然后再去set去user ID那么就是这个叫什么呢user ID好那么是不是有这
[12:10] 有这四项填写好了那么还差一项的就是谁呢就是我们那个就是我们那个score下面处理那么需要针对每一种不同的这个type是不是去做处理那我们可以用一个switch去做一个处理比如说1它怎么处理那么我们去写一个它那么这个里面写一个break然后呢我们来参考一下前面所写的这个内容
[12:39] 那么我们去看一下啊那么一呢一到七来看一下啊那我们就直接把它丢到这来吧加一个注释写到这好那么一呢是发动态那么二呢是浏览三呢点赞啊等等那么一呢这个发送动态就会稍微有一点呃繁琐那么我们一会儿最后来处理它啊我们先来处理其他的啊那么呃第二个呢就是这个二哎第二个呢是这个二啊那么呃还有一一直到几呢七对吧
[13:09] 好那我们来写一下那么这个是这个是3然后呢我们来写一下这个是写差不多吧然后呢这个是4 5 6然后呢7那么当然了最后还有一个什么呢default那么default呢也需要一个break那么我们如果这个改成
[13:39] 改成7那么如果 default的话我们就应该把recommend圈子对象他点score那么就应该设置为0对吧是double类型的设置为0好那么我们来处理前面的1到7那么1我们最后做处理先来处理这个2那么如果是浏览的话我们就给他设置几分来看一下那么给他设置点set什么scoreset score
[14:07] 那么score呢我们来看一下它是浏览是一分那么就是写1D对吧然后呢这个3呢3是点赞点赞的是加5那就是5D然后呢这个4呢是喜欢的是8对吧8然后呢5呢是什么我看一下5是评论评论的是加10那就是5是10D
[14:34] 然后呢6呢是什么6是取消点赞取消点赞那么取消点赞呢我们来看一下啊那么点赞的是五分取消呢就应该什么呢-5分-5然后呢7呢是取消哎看一下上面啊取消喜欢那么喜欢呢喜欢所对应的是八分那就是-8D然后呢还有谁呢还有就是
[15:02] 这是不是就OK了对吧好那么接下来是不是我们需要处理这俩那么一个是文字的长度一个是图片的一个个数那么我们想要知道这个文字的长度和图片个数的话那么我们必须要去在我们这个新增这个里面去拿到我们的public这个对象那么才可以去做一个做一个这样的一个判断所以说在我们这个中是不是也需要
[15:31] 去拿到我们的这个对象通过我们这个public id呢去做一个这个查询那么在这个位置呢我们就需要去查询对吧查询mongodb那我们就直接来注入吧叫mongo啊mongo呃然后呢template啊去注入进来然后呢我们直接去查就ok了好那么我们来看一下前面我们配置中啊那么有没有这个mongo的配置啊哎呃这个啊看一下是不是有mongo的配置啊
[16:00] 所以说我们直接就可以去查了好那么我们来看一下在这个位置我们就通过什么呢来查一下race.mongo-template.这个分的什么呢问或者翻着byid就可以了然后呢id呢new一个object id然后呢把这个publish id传递过去那第二个呢就是我们的一个publish点然后呢这个我们这个对象是不是还没有啊
[16:31] 没有的话那我们就我们可以去做一个依赖也可以去拷贝过来那我们就直接拷贝过来吧这样可能更简单一点那我们来看一下那么然后呢当然我们如果是也可以去依赖一下它那么这样吧我们就依赖吧这样的话可能做的话这样显得我们更专业一些然后呢我们去把它呢拷贝一下然后呢我们还是需要
[16:59] 然后我们需要这样来拷贝那先拷贝它吧然后呢在我们这个recommend中啊然后下面去添加一下呃这是artifact id啊把它来写一下呃然后呢还有就是我们上面的group id就是它把它呢丢过来好然后呢还有呢就是我们的这个版本啊版本呃版本的话它应该是不需要去莫言找到上面这个版本了
[17:28] 那么我们来给他写一下Watson这个Watson那么Watson也是上面我们所写的这个1.0.0的1.0这样的一个快照版好那么把它丢到这来好那么导入进来那么在这个里面我们就可以直接去使用这个对象了这样的话会更专业一些好那么叫publish.class好OK
[17:55] 那么这样的话呢我们其实就已经啊去完成了啊啊完成了这个查询那么拿到这个publish这样的一个啊这样的一个对象啊接下来呢我们就给他去计算一个score了对吧那我们在这吧int去来一个score啊等于什么呢先设置为应该叫应该用什么呢呃我们就就用int吧
[18:20] 然后呢我们来看一下啊这个怎么样去做一个计算那么首先呢来看他的文字的这个长度啊那我们首先获取到他的一个get什么呢text文本啊然后呢这个是他的一个文本好那么我们去做判断啊if那么我们去拿到他文本的一个认死长度啊text那么如果他的这个长度啊
[18:47] 呃是在50以内那就是什么呢就是呃大于0并且啊这个长度那么我们是不是应该呃那我们应该这样去写啊不应该这样去写那么就写一个这个呃叫int吧int然后呢我们定义它的一个length然后呢我们把这个拷贝过来那么我们这样去拷一下好那么拿到这个length啊长度去做一个判断如果它大于0啊
[19:20] 大于0并且它小于等于50的话那么给它记几分呢是不是记一分对吧那么就是这个我们这个recommend圈子这个对象点set score那么就设置为那我们就最后来设置吧这样我们就先给它去直接写到这个里面来它等于几呢1它等于1那么else if判断
[19:48] 那么如果这个长度在50到100之间呢那我们来写一下这个就应该是大于50并且这个Lens呢小于等于100那么这个就是几分呢我们来看一下这个就是两分这个就设置为2那么else一幅else一幅的话那么那就直接else吧直接else如果是
[20:16] 大于100以上那么就记三分啊去设置一个三好那么这个是不是就OK搞定对吧这个逻辑就搞定了好那么接下来看下面这个逻辑就是图片的个数那么下面的我们就需要拿到他的一个这个呃就是没救死然后呢去判断一下啊那么我们还需要去先判断是不是为弄了那我们就做一个判断呃有tools.isempty啊
[20:45] 如果他不为空的话我们再去判断他的这个size啊哎呀应该是不需要判断了直接去加就好了就是我们这个score呀去加等于他就是去加他的这个这个速度的这个长度就可以了那么因为每一张这个图片就记一分嘛那所以直接去累加就可以了啊然后呢走到这儿呢我们再去给他写到他的这个对象中啊
[21:14] 那么再来写一下点set scorescore需要去转一下那就用这个doubledouble.valueof好这样的话就可以去转成一个double了好嘞好那么这样的话是不是就完事了那么走到最后呢我们就需要把它保存到我们的mongo里面来做一个save一个保存那么save呢我们来看一下就是这个对象
[21:41] 那么首先呢我们确定对象是他没有问题但是要注意了那么保存的集合是谁呢要注意那么这个集合那我们不能去把所有每一天的这个日子都存储到一个这个集合中或者是一个表里面来啊那我们需要呢去按照每一天的时间呢去做一个存储也就是说每一天呢都是写到这个什么呢这个
[22:08] 这当天的这个表里面来而并不是写到所有的一个里面去啊那所以说在这个里面我们就需要去给他定义一个什么呢Connection一个Name啊定义一个呃呃这Name啊叫Name呃Connection的一个Name它等于什么呢就是等于我们叫Rickmonde啊Rickmonde然后呢这个圈子
[22:38] 然后呢下滑线呢再来一个日期就是年月日啊那我们就去new一个我们那个data time然后呢to string然后呢yyy年月的mm日就是dd啊这样的话呢就会得到一个年月日啊这个表明啊传递到这个位置来那么就是把它写到这个表里面来这个就是我们
[23:04] 将这个数据啊写入到我们的一个蒙狗啊蒙狗db好那么这样的话是不是就完成了一个写入了哎OK好那么接下来我们来看一下我们的讲义啊那么这个呢是我们的这个接收消息在这啊那么去创建工程没有问题然后呢编写配置文件也没有问题那么这个是log4j的配置文件上面是我们这个对象啊这个对象那么所存储对象
[23:32] 然后下面这个是具体的逻辑的一个处理那么应该跟我们写的没有问题首先拿到这么几个数据然后去填充这个对象然后分别对1231到7去做一个处理那么这个处理应该跟我们写的刚才是一样的对吧一样的OK好然后最后去把数据保存到我们的mongoDB中这样的话就OK了好那么关于这个消息的一个接收处理那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中实现 RocketMQ 消息消费，处理动态推荐相关的业务逻辑，包括消息接收、数据解析、MongoDB 操作和评分逻辑。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示课程目录结构，当前章节为“1.6.2 配置文件”，并预览了后续开发步骤的多张截图。
画面 2: 显示 `application.properties` 配置文件内容，包含 RocketMQ 和 Redis 的配置。
画面 3: 显示 `RecommendQuanZi` POJO 类的定义，包含 `id`, `publishId`, `score`, `date` 等字段。
画面 4: 显示 `QuanZiMsgConsumer` 类的初始结构，使用 `@RocketMQMessageListener` 注解监听 `tanhua-quanzi` 主题。
画面 5: 在 `QuanZiMsgConsumer` 类中，定义了 `private static final Logger` 字段，并导入了多个日志框架。
画面 6: 在 `onMessage` 方法中，使用 `ObjectMapper` 解析 JSON 消息，提取 `type`, `publishId`, `date`, `userId`, `pid` 字段。
画面 7: 继续在 `onMessage` 方法中，创建 `RecommendQuanZi` 对象并设置其属性。
画面 8: 在 `switch` 语句中，为 `case 6` 添加了 `break;`。
画面 9: 在 `switch` 语句中，为 `case 1` 和 `case 3` 添加了 `break;`，并为 `case 2` 和 `case 3` 设置了评分逻辑。
画面 10: 在 `switch` 语句中，为 `case 1` 添加了 `Publish publish = this.mongoTemplate.findById(...)` 代码。
画面 11: 在 `switch` 语句中，为 `case 1` 完成 `Publish publish = this.mongoTemplate.findById(...)` 代码。
画面 12: 在 `switch` 语句中，为 `case 1` 添加了根据 `publish.getText()` 长度计算 `score` 的逻辑。
画面 13: 在 `switch` 语句中，为 `case 1` 添加了 `try-catch` 块，并在 `catch` 块中记录错误日志。
画面 14: 在 `switch` 语句中，为 `default` 分支添加了 `recommendQuanZi.setScore(0d);` 代码，并在 `catch` 块中记录错误日志。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面 2:
```properties
spring.application.name=itcast-RocketMQ
server.port=10082
# RocketMQ相关配置
spring.RocketMQ.nameServer=192.168.31.1:9876
spring.RocketMQ.producer.group=tanhua
# Redis相关配置
spring.redis.jedis.pool.max-wait = 5000ms
spring.redis.jedis.pool.maxIdle = 10
spring.redis.jedis.pool.minIdle = 10
spring.redis.cluster.nodes=192.168.31.1:6379,192.168.31.1:6380,192.168.31.1:6381,192.168.31.1:6382
spring.redis.cluster.maxRedirects=5
# mongodb相关配置
spring.data.mongodb.uri=mongodb://192.168.31.81:27017/tanhua
```

画面 3:
```java
package com.tanhua.recommend.pojo;

import ...
@Data
@NoArgsConstructor
@AllArgsConstructor
public class RecommendQuanZi {
    private ObjectId id;
    private Long publishId; // 动态id，需要转化为Long类型
    private Double score; // 待分
    private Long date; // 时间戳
}
```

画面 4:
```java
package com.tanhua.recommend.msg;

import org.apache.RocketMQ.spring.annotation.RocketMQMessageListener;
import org.apache.RocketMQ.spring.core.RocketMQListener;
import org.springframework.stereotype.Component;

@Component
@RocketMQMessageListener(topic = "tanhua-quanzi",
        consumerGroup = "tanhua-quanzi-consumer")
public class QuanZiMsgConsumer implements RocketMQListener<String> {
    @Override
    public void onMessage(String s) {
    }
}
```

画面 5:
```java
private static final Logger LOGGER = LoggerFactory.getLogger(QuanZiMsgConsumer.class);
```

画面 6:
```java
private static final ObjectMapper MAPPER = new ObjectMapper();

@Override
public void onMessage(String msg) {
    try {
        msg.put("Type", type);
        msg.put("publishId", publishId);
        msg.put("date", System.currentTimeMillis());
        msg.put("userId", userId);
        msg.put("pid", publish.getPid());
        JsonNode jsonNode = MAPPER.readTree(msg);
        int type = jsonNode.get("type").asInt();
        String publishId = jsonNode.get("publishId").asText();
        Long date = jsonNode.get("date").asLong();
        Long pid = jsonNode.get("pid").asLong();
    } catch (Exception e) {
        LOGGER.error("消息处理失败！msg = " + msg);
    }
}
```

画面 7:
```java
RecommendQuanZi recommendQuanZi = new RecommendQuanZi();
recommendQuanZi.setDate(date);
recommendQuanZi.setPublishId(pid);
recommendQuanZi.setUserId(userId);
```

画面 9:
```java
switch (type) {
    case 1:
        break;
    case 2:
        recommendQuanZi.setScore(1d);
        break;
    case 3:
        recommendQuanZi.setScore(5d);
        break;
}
```

画面 10:
```java
Publish publish = this.mongoTemplate.findById(new ObjectId(publishId), Publish.class);
```

画面 12:
```java
int score = 0;
Publish publish = this.mongoTemplate.findById(new ObjectId(publishId), Publish.class);
if (length > 0 && length <= 50) {
    score = 1;
} else if (length > 50 && length <= 100) {
    score = 2;
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面 1: PPT 标题为“1.6.2 配置文件”，左侧目录显示“1.6.2 配置文件”。
画面 14: PPT 标题为“1.7.1、发布动态”，下方显示 HTTP 请求的“Headers”和“Authorization”字段。

5) 无。

