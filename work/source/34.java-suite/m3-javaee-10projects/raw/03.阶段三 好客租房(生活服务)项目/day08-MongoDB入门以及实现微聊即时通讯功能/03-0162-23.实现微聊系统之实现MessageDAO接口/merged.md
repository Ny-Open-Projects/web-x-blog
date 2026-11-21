# 23.实现微聊系统之实现MessageDAO接口

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\23.实现微聊系统之实现MessageDAO接口【海量资源尽在 ubkz.com】.mp4
- 时长 21分30秒（音频 1291s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就来编写我们刚刚所写的这个message dao的它的实现类那么在这个下面呢我们来创建一个这个包就叫impl然后呢我们去编写一个它的实现类那么写一个类呢就叫message什么的dao然后呢impl然后呢它呢是一个类啊所以呢我们就写它定义它是class然后呢它呢要去实现
[00:26] 去我们的一个message然后呢一个dao然后呢我们首先呢把它标记为这是一个component就是我们sprint的一个组件然后呢我们去实现它的定义的几个方法有这么多方法那我们就一个一个来看吧这几个方法的一个编写那么在这几个方法中啊应该是这个相对是比较复杂一点的就是去查询它的一个聊天记录啊来人记录
[00:55] 那么我们来大概编写一下他的一个思路啊就是这个呢我们首先他这个实现的是是查询啊查询这个点对点的对吧这个消息的一个记录啊消息的一个记录那么我们要去查询的话那我们应该怎么去做呢那我们来看一下那么首先我们可以看到在这个位置呢去需要去做查询那么一定是需要我们的mongo db的呃template对吧所以我们先把这个mongo dbtemplate我们先给他注进来
[01:24] OK先把它注入进来然后我们叫用它就可以去完成一个查找那么查询呢是不是可以叫用this.mongodb然后呢这个template点什么的fend去做一个查询那么其实我们可以看到那么fend查询的时候呢其实就是通过两个参数那么一个呢就是query一个呢就是我们的这个查询的一个对象的这个class那么所以呢我们就给它去定义这么两个这个参数
[01:52] 那么query呢我们先把它设置为空那么一会儿我们来写这个query那第二个参数就class那么就是message点什么呢class点class哎呦OK好那么接下来我们只要把这个query搞定是不是就OK了所以我们来看一下这个query怎么去做首先呢我们来定义一个queryquery呢是这个core这个包下面的query啊别搞错然后呢有一个query然后呢它等于什么呢query点什么呢query
[02:19] 然后他要通过一个Creator去做一个实现所以我们来先去做一个注释这个快运其实我们要去完成两件事情那么第一件事情我们就要去设置它的一个查询条件查询条件那么第二件事情就要做什么呢做一个分页所以说这两个事情别忘记所以我们先去做的是第一个事情就是查询的条件所以我们定义一个Creator
[02:49] Cartina它呢等于什么呢去new一个CartinaCartina然后呢我们把这Cartina是不是给它传递过去对吧传到这OK然后呢它呢是需要做什么呢注意我们要查询的是点对点的也就是从A到B或者是什么呢B到A的这样的一个消息所以呢我们需要用all用all去做一个这样的一个传递那么它里面呢我们来看一下
[03:15] 他又需要什么呢又需要多个这个cretina是不是作为一个out的一个条件啊哎ok所以呢我们又需要在上面呢又需要给他去做什么的定义那我们来看一下那么上面呢我们又需要去定义什么呢cretina然后呢我们定义一个from吧这个from从谁到谁的对吧那么在这个里面呢我们就需要通过cretina点然后呢will然后呢设置一个条件啊设置一个条件
[03:45] 那么什么条件呢是不是就是从我们的就是这个formid等于它然后呢并且toid是不等于它的所以我们在这个位置呢应该是要这样去写去new一个new一个critter然后呢我们需要给它设置一个and点一个and的一个操作
[04:10] 那么在这个里面呢他呢又需要去设置什么呢又设置这个多个所以呢我们又需要在这个里面给他设置多个什么设置来看一下Cretina点什么ValveValve谁呢是不是就是我们的这个数据啊我们来看一下我们这个数据那么我们这个数据呢我们要来看一下叫我们现在是不是还没有数据啊那么我们现在还没有数据来看一下它的结构吧是不是我们需要查找的是From中的
[04:38] 这个ID等于我们传入的这个什么的form ID所以怎么写呢应该是叫做from.id它呢意义是等于这个from ID对吧form ID然后呢这第一个条件那么第二个这个条件呢它应该是什么呢第二个条件是我们的这个to对吧to这个对象他的ID他的ID他点这个ID
[05:08] 一是什么呢to id这是我们的第一个这个条件对不对这个呢就是啊这个就是我们什么呢用户a发送发送给用户b啊b的这个数据啊这样的一个数据或者这样的一个条件是不是那么发送人是这个a然后呢这个接收人是b哎OK这个是啊这个是这样的一个条件啊
[05:36] 那么我们是不是就可以把它是不是传递到我们这个这个里面来OK这第一个是不是就搞定了那么接下来我们要写的是第二个对吧那么第二个是什么呢就是我们的这个发送人是B到A的对吧其实我们条件是用户B发送给用户A的这样的一个条件去查询他一个记录那么我们才能够去形成一个完整的这样的一个记录对不对OK
[06:04] 好那么我们在这个位置就去设置一下吧这个我们改成to吧to然后呢form.id要设置为什么呢要设置为to id然后呢to.id要设置为form id那么我们现在是不是有了两个条件了把这个条件也给他也给他要丢过来ok
[06:25] 那么丢过来之后我们就构造完成Kartina我们查询的一个条件那么接下来我们就需要给它设置这个分页那么前面我们也说过这个分页那么接下来我们要使用另外一种分页来做一个实现那么就是在这个位置添加一个什么呢Viz添加一个Viz一个PagePageAble那么PageAble那么在这个位置我们其实要去给它定义叫做Page什么呢Request这样的一个对象
[06:55] 这样的对象然后呢page request对象它等于page request.off我们可以看到是不是有有这几个参数那么其实我们应该选择的是第一个因为我们要设置它的这个配置第一页然后页数然后以及它的set就是我们每一页查询的数据那么其实呢我们还需要传递一个sort就是我们要去做一个排序
[07:22] 大家可以想一下我们现在呢是根据上面的两个条件是不是这两个条件是不是我们做了一个数据的一个查找那么我们是不是需要把这两个数据按照一定的排序顺序去给它组合起来形成一个消息的一个聊天记录
[07:38] 那么根据什么呢其实就是根据我们的消息的发送的时间对不对做一个正序的排序那么最早的消息是在最上面那我们看到的永远是最新的消息在最下面对不对我们应该这样去做所以我们应该选用的是上面这个方法OK那么我们来一个什么的off那么我们用第一个配置那就是配置然后第二个就是漏死然后第三个要注意的是我们要给它设置一个sort
[08:06] source by什么呢我们给设置它一个应该是叫asc对吧正序排序根据某一个字段去做一个正序的排序那么哪个字段呢我们来看一下在我们这个里面是不是有个叫做send date这个字段OK那么在这个位置我究竟应该写的是下滑线的这个呢还是我写的是驼奔的这个呢OK那么其实它结果都是一样的
[08:31] 这个无所谓因为它会自动做一个识别因为我们是不是加了这样的一个fail的这样的一个注解OK都行那么我这块就给它设置为这个图分OK好那么在这个位置还有一个小细节需要大家注意一下
[08:45] 就这个配置要注意那么配置他是从零开配置呢我们是其实要给他去减一的减一那么如果我们不减一的话那么他这个计算的结果是不对的所以呢我们就要注意一下这个在这个位置要给他去做一个减一的一个操作这个要切记OK那么我们把这个配置request就给他丢过来好嘞那么这样的话我们其实就实现了一个查询的条件以及这个分页OK那么把这个query要给他丢过来这个别忘记
[09:14] 好到这个位置呢我们其实已经就把这个查询就搞定了那么接下来我们其实就要做一个测试啊做一个测试看我们这个方法写的对不对啊他能不能够查到对应的一些这个数据OK那么接下来呢我们把下面的一些这个单元测试我们也创建好然后呢我们去测一下OK那么我们进入到我们这个里面啊然后呢我们去找到我们这个单元测试然后呢我们创建这样的一个包
[09:44] 创建这样的一个包就是我们这个deo的这个包把这个包名我们靠过来我们去创建一个单元测试ok然后在下面呢我们去写一个这个test然后呢matched deo的一个测试用力然后呢在上面呢我们给它添加两个注解这两个注解那么相信大家应该是现在很熟悉了对吧因为我们用的是比较多的然后呢我们来看一下
[10:13] 这个呢是注入我们的一个message.do那么把它注入进来ok注入进来之后呢这个我们就先不管它了这个是编译器的一个报错因为它检测到我们没有写那个启动类所以它说这个会有错误ok那然后呢我们去做一个这个这个sale因为我们现在还没有数据对不对那么我们这个还没有办法去做一个没有办法去做一个测试那这样我们先把这个sale这个
[10:41] 这个动作给他做完因为C5的这个实现是相对比较简单的那么我们一会儿是不是好方便我们测试我们先找到一个C5这个操作那么他返回来那就直接调用类似点这个template点做一个什么呢C5就OK了这个相对比较简单的但是在这个里面我们要去也需要处理一些这个逻辑我们需要写入写入他的一个发送时间
[11:13] 发送的一个时间那么点set一个什么呢叫做setDate叫newDate发送的时间然后呢我们还需要去给它设置一个它的一个状态应该都是1都是未读状态消息我们一开始写入都是未读状态是不是所以说我们要把它设置为1OK好那么这两个呢我们就搞定了OK然后呢我们接下来呢就需要去
[11:40] 去调用这个方法去先去写入一些数据我们好做一个测试啊所以呢我们接下来就可以把这个test这个save这个方法我们拷过来了好那么把这个拷过来这个呢我们来先拷一个我们先看一下他到底在干什么啊就是我们去new一个这个时间new一个这个user哎ok好嘞那么我们可以看到这个消息呢其实就是from是1001
[12:12] to呢是1002也就是说张三这个用户发送给李四一条消息消息的内容呢是你好哎OK然后呢下面呢又会发一条消息是谁呢来看一下是变成from是谁呢1002就是李四发给张三一条消息啊你好然后呢继续往下面再去发就是在这然后呢张三跟他讲说哎发送人张三
[12:40] 然后呢我正在学习开发IM然后呢李四又给他发个消息了就是一个消息的对话我们做了这样的一个模拟然后呢拿到他OK最后打印一个OK好那么这样的话呢就是那么李四呢给他响应就说那很好啊大概呢就是这样的意思啊我们把这个数据先保存起来那保存起来之后呢我们去做这样的一个查询查询的一个测试OK那么我们丢到这
[13:12] 那么好嘞那么测试用力其实我们就写好了那么接下来我们需要我们需要写一个启动类啊但是我们这个讲一中的并没有去写这个启动类对不对那么我们就直接来写一个吧那么启动类呢我们就写一个类啊就叫im什么的applicationapplication然后呢我们把它设置为这是一个Spring Boot application哎呀ok
[13:40] 然后我们下面是不是就要去写一个MEM方法然后我们去设置它的spring application.ronron什么呢就是imapplication.class然后设置一个args它的一个参数ok好那么这样的话我们就可以去启动我们这样的一个应用了那么像接下来我们在这个里面就可以先去测试我们这个save方法看一下我们这个数据是否能够保存到我们的这个mongo db中ok
[14:10] 好那么我们来看一下在这个位置包错了包错了原因是我们没有写它的一个配置文件那么我们这个配置文件丢了把它靠过来在前面我们是不是写过这样的配置文件我们来把它丢过来在这个里面它很关键的需要配置一下我们的这个mango db的一个连接支付串对吧所以在这个我们改个名这个我们就叫就是我们的工程名把它丢过来然后我们再次启动我们做一个测试
[14:40] 好那么现在这个服务呢已经就跑起来了那么我们其实可以看到他已经就执行结束了打印了这个OK那我们来看一下数据我们那个mango db里面的数据啊那么我刚刚执行了一下查询那么可以看到其实数据啊已经又来了对吧那你好你好我正在学习这个m开发那很好啊这是不是他们张叉和李氏的一个对话呀哎OK这是这四条消息啊四条消息那么呃那么这说明什么呢我们刚刚所写的这个
[15:09] 这个C5操作是不是没有问题啊但是其实这个C5操作里面也有点小问题就是在这个位置呢我们没有去给它去当然了我们没有给它去设置什么的ID啊没有给它去set一个ID这个ID呢你不设置那么MongoDB呢也会去给你自动去做一个生成其实你设置不设置啊都行但是呢如果说啊如果说如果说我们要是在我们去做编码的时候有统一的这种要求的时候呢我们就给它去写一下
[15:39] 就来一个object id点get也可以去做一个生成那么这个你可以去加也可以不加生成的结果其实都是一样的那么接下来关键的一个点就需要去我们去测试一下我们查询这个方法我们去查询一下1001和1002发送人是1001发送的目标是1002然后我们去拿它的第一页的消息然后我们总共拿几条拿一条然后我们来看一下它会打印什么样的结果
[16:15] 那我们可以看到现在是不是已经就拿到数据了其实但是呢他只有一条数据啊那么这样我们为了测试我们这个方法他查询的对不对所以我们在这个位置呢打印比如说我们打印10拿10条数据因为呢他总共的也就4条对吧也就是说全部都会拿到数据那我们来再次测试一下啊看他拿到的数据是不是我们的4条数据如果能拿到那就说明我们刚刚写这个逻辑啊他是OK的好那么现在我们可以看到他是不是已经拿到了这4条数据
[16:44] 并且呢它的一个顺序啊就是它的一个这样的一个顺序呢也是按照我们发送消息的这样的一个顺序哎OK当然我们可以为了测试啊我们可以这么来玩一下就是我们给它设置成一个DESC我们来看一下这个有没有生效啊我们是仅仅做一个测试啊然后呢我们也可以把这个query这个这个查询啊我们可以把它打印出来我们来看一下啊那么我们来再次执行一下哎OK再次执行走
[17:12] 好那么我们可以看到它的一个执行的一个结果呢是这样的一个结果那么首先呢最外面的一个这个query它是一个all啊all的一个查询那么就是我们上面有两个条件是吧一个是all但是呢它的内部可以看到啊那么这样我们把这个call贴出来吧贴出来呢大家更容易去看一下啊那么我们来看一下在这然后呢我们看到最外面其实它是一个all查询对吧然后呢它是一个中括号中括号然后呢它的一个结束符呢是在
[17:42] 是在哪里呢是在这儿是在这个位置那么也就是说这个里面的几个我看结束符是在这里这个是它的一个结束符那么它的内部是一个and条件它等于这1001and这个to等于1002然后这是一个条件对吧然后后面的这个是andform等于它然后它等于它这是另外一个条件
[18:09] 这个条件和后面这个条件他们俩是一个什么关系呢是一个all的关系所以就能够正确的查出我们的这个数据并且呢可以看到这个排序的这个位置呢是给他设置-1那么也就需要做一个倒序的一个排序那我们来看一下拿到数据对不对呢是不是最后一条先拿到了那很好啊我也在学等等等等是吧你也好你好
[18:31] 其实把我们这个顺序是不颠倒了那么也就是说我们刚刚所写的逻辑它是OK的我们就把这个代码给它还原回来OK那么它就是一个按照我们的业务来逻辑来讲它应该就是一个正序的一个排序OK那么这个打印我们也不需要了好嘞那么到这里呢我们是不是就已经实现了我们的这个第一个这个查询以及我们的这个新增对吧那么我们还有一些其他的
[18:57] 一些这个实现的我们就参考我们的讲义那我们的把这个实现给他来完成一下那么这个叫做FedMeshByID根据组件去做查询这个就非常简单了我们就不直接把它贴过来就贴到这吧OK那么就根据我们的组件去做一个查询就可以了再要特别提一点的是在这个MongoDB的一个这个complete中他提供了一个方法叫做FedByID就根据组件去做一个查询所以我们直接给他提供这个组件就可以了
[19:28] 这是这个那么还有一个呢是更新一个我们的一个状态啊那么我们把这个逻辑呢也靠过来在这个内部呢有一点点的小逻辑需要大家注意一下啊就是我们要去更新我们的一个消极的一个状态的时候呢要做一个判断就是说如果你的消极状态等于一的时候我们要设置为他的一个发送时间是这个如果你的状态设置为这个二的时候就是已读的时候我们把它的一个
[19:55] 这个ray的时间就是读取的时间设置为当前的这个时间这个小逻辑大家一定要注意ok好嘞那么下面的这个save跟我们这个写的呢是一样的没有问题然后呢我们再来去看它的一个叫做deletedelete一个操作那么来靠过来看一下那么在这个里面呢我们去构造我们的query就是id等于它然后做一个删除这样的肯定是没有问题的ok好那么这个就是我们所实现的一个dao
[20:23] 那么关于刚刚所写的其他的几个方法呢我就不做测试了大家可以自行去做一个测试应该是没有问题的这个呢其实我在去整理这个课程的时候这个代码都已经测试过了都是没有问题的OK好那么到这里呢我们这个message.do的一个实现类是不是就搞定了其实重点要给大家所讲的是这个第一个这个方法把这个逻辑搞明白了那么其实这个整个我们这个查询的逻辑
[20:52] 或者说我们这个就能够实现这样查询这个业务了哎呀OK但是要注意的一点的是在我们这个实现中啊我刚刚所写的这个实现跟我的这个讲义中的这个代码呢稍微有点不同其实它是一样的那么这个代码我们简单来说一下就是它先构造了一次一个form的这样的一个条件然后加一个and然后再去加后面那个它那么我们刚刚写的呢是我先设置设置一个and的一个
[21:17] 按的一个操作符然后呢再去添加这两个啊其实他是最终得到的都是一样的只是他写法表达有所不同而已啊OK好那么关于这个message的一个deo的一个实现呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Spring Boot 和 MongoDB 实现一个简单的点对点消息系统，包括 DAO 层接口与实现、实体类定义、测试类编写及配置文件设置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 MessageDAO 接口定义，包含 findByFromAndTo 方法，用于查询指定发送者和接收者之间的消息列表。
画面 2: 展示 MessageDAOImpl 类中 findByFromAndTo 方法的实现，使用 Criteria 构建查询条件。
画面 3: 展示 MessageDAOImpl 中 findByFromAndTo 方法的实现，使用 Criteria 和 Query 对象构建查询，并调用 mongoTemplate.find。
画面 4: 展示 Message 实体类的定义，包含 id、msg、status、sendDate、readDate、from、to 等字段，并使用 @Builder、@Indexed 等注解。
画面 5: 展示 MessageDAOImpl 中 findByFromAndTo 方法的实现，构建 Criteria 条件并设置分页参数 PageRequest。
画面 6: 展示在 MessageDAOImpl 中使用 Criteria 构建查询条件，其中包含 fromId 和 toId 的条件。
画面 7: 展示 MessageDAOImpl 中 saveMessage 和 deleteMessage 方法的实现，调用 mongoTemplate 的 save 和 delete 方法。
画面 8: 展示 PDF 文档中 Message 实体类的构建示例，包含设置 id、msg、from、to、status 等属性并调用 saveMessage 方法。
画面 9: 展示 ImApplication 主类，使用 @SpringBootApplication 注解，定义 main 方法。
画面 10: 展示 application.properties 配置文件，设置 spring.application.name 和 spring.data.mongodb.uri。
画面 11: 展示 TestMessageDAO 测试类中 testSave 方法，调用 messageDAO.saveMessage 保存消息。
画面 12: 展示 TestMessageDAO 测试类中 testQueryList 方法，调用 messageDAO.findByFromAndTo 查询消息并打印。
画面 13: 展示 PDF 文档中 TestMessageDAO 测试类的 testSave 方法，用于测试消息保存功能。
画面 14: 展示 MessageDAOImpl 类的完整定义，包含导入的包和 @Component 注解。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
import com.mongodb.client.result.DeleteResult;
import com.mongodb.client.result.UpdateResult;
import org.bson.types.ObjectId;

public interface MessageDAO {
    /**
     * 查询点对点聊天记录
     * @param fromId
     * @param toId
     * @param page
     * @param rows
     * @return
     */
    List<Message> findByFromAndTo(Long fromId, Long toId, Integer page, rows);
}
```

画面 2:
```java
@Override
public List<Message> findByFromAndTo(Long fromId, Long toId, Integer page, Integer rows) {
    return this;
}
```

画面 3:
```java
@Override
public List<Message> findByFromAndTo(Long fromId, Long toId, Integer page, Integer rows) {
    Criteria criteria = new Criteria().orOperator();
    Query query = Query.query(criteria);
    return this.mongoTemplate.find(query, null, Message.class);
}
```

画面 4:
```java
@Builder
public class Message {
    @Id
    private ObjectId id;
    private String msg;
    /**
     * 消息状态，1-未读，2-已读
     */
    @Indexed
    private Integer status;
    @Field("send_date")
    @Indexed
    private Date sendDate;
    @Field("read_date")
    @Indexed
    private Date readDate;
    @Indexed
    private User from;
    @Indexed
    private User to;
}
```

画面 5:
```java
// 用户A发送给用户B的条件
Criteria criteriaTo = new Criteria().andOperator(
    Criteria.where("from_id").is(fromId),
    Criteria.where("to_id").is(toId)
);

Criteria criteria = new Criteria().orOperator(criteriaFrom, criteriaTo);

PageRequest pageRequest = PageRequest.of(page, rows, Sort.by(Sort.Direction.ASC, "sendDate"));

Query query = Query.query(criteria).with(pageRequest);
return this.mongoTemplate.find(query, Message.class);
```

画面 6:
```java
where("from_id").is(fromId),
where("to_id").is(toId)
```

画面 7:
```java
@Override
public Message findMessageById(String id) {
    return null;
}

@Override
public UpdateResult updateMessageState(ObjectId id, Integer status) {
    return null;
}

@Override
public Message saveMessage(Message message) {
    return this.mongoTemplate.save(message);
}

@Override
public DeleteResult deleteMessage(String id) {
    return null;
}
```

画面 8:
```java
message = Message.builder()
    .id(ObjectId.get())
    .msg("你好啊")
    .sendDate(new Date())
    .from(new User(1001, "zhangsan"))
    .to(new User(1002, "lisi"))
    .build();
this.messageDAO.saveMessage(message);

message = Message.builder()
    .id(ObjectId.get())
    .msg("你也好")
    .sendDate(new Date())
    .from(new User(1001, "zhangsan"))
    .to(new User(1002, "lisi"))
    .build();
this.messageDAO.saveMessage(message);
```

画面 9:
```java
package cn.itcast.haoke.im;

import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class ImApplication {
    public static void main(String[] args) {
        SpringApplication.run(ImApplication.class, args);
    }
}
```

画面 10:
```properties
spring.application.name=itcast-haoke-im
spring.data.mongodb.uri=mongodb://172.16.55.185:27017/testdb
```

画面 11:
```java
this.messageDAO.saveMessage(message);
System.out.println("ok");
```

画面 12:
```java
public void testQueryList() {
    List<Message> list = this.messageDAO.findByFromAndTo(fromId: 1001L, rows: 10);
    for (Message message : list) {
        System.out.println(message);
    }
}
```

画面 13:
```java
@RunWith(SpringRunner.class)
@SpringBootTest
public class TestMessageDAO {
    @Autowired
    private MessageDAO messageDAO;

    @Test
    public void testSave() {
        Message message = Message.builder()
            .id(ObjectId.get())
            .msg("你好啊")
            .sendDate(new Date())
            .from(new User(1001, "zhangsan"))
            .to(new User(1002, "lisi"))
            .build();
        this.messageDAO.saveMessage(message);

        message = Message.builder()
            .id(ObjectId.get())
            .msg("你也好")
            .sendDate(new Date())
            .from(new User(1001, "zhangsan"))
            .to(new User(1002, "lisi"))
            .build();
        this.messageDAO.saveMessage(message);
    }
}
```

画面 14:
```java
package cn.itcast.haoke.im.dao.impl;

import cn.itcast.haoke.im.dao.MessageDAO;
import cn.itcast.haoke.im.pojo.Message;
import cn.itcast.haoke.im.pojo.User;
import com.mongodb.client.result.DeleteResult;
import com.mongodb.client.result.UpdateResult;
import org.bson.types.ObjectId;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Sort;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.data.mongodb.core.query.Update;
import org.springframework.stereotype.Component;

@Component
public class MessageDAOImpl implements MessageDAO {
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 8: PDF 文档中显示了“4.1. 在创建 itcast-haoke-im 工程”、“4.2. 编写 MessageDAO”、“4.3. 实现”、“4.4. 测试”等章节标题。
画面 13: PDF 文档中显示了“编写实现类”章节标题。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

