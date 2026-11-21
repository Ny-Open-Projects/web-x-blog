# 02.实现前端的mock服务

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day07-完善前端功能以及WebSocket入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day07-完善前端功能以及WebSocket入门\02.实现前端的mock服务【海量资源尽在 ubkz.com】.mp4
- 时长 19分1秒（音频 1142s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接下来呢实现第一个功能就是为我们的前端系统呢来提供一个Mock服务在这呢我们其实写了一个名字叫做伪Mock服务啊那么为什么叫伪呢其实是我们并没有采用第三方的一些Mock的一些框架而是我们自己来实现一个Mock的这样的一个服务所以呢把它称之为叫做伪Mock服务啊好那么接下来我们来看一下这个应该怎么去做
[00:28] 那么首先呢我们需要去分析一下那么在我们的首页中呢一些除了这个之外的一些其他的一些请求啊那么看一下下面的一些菜单还有下面的一些这个资讯啊等等一些数据的一些请求那么我们来看一下刷新一下页面啊刷新走
[00:45] 那么我们点开这个network我们就可以看到他的一些请求的地址包括他的一些请求的一些这个结果然后呢来筛选一下通过这个xhr做一个这个筛选那么我们点击这个位置啊这个是obsense我们找到下面的这个getpost这个请求获取数据这个请求那么他的请求的结果是不是这样的一个结果的数据啊那么其实是不是就是说我们只需要
[01:13] 在我们的这个API这个里面对吧在API这个下面那么我们只要为他提供这样的一个的请求然后呢响应这样的数据是不是就可以完成一个Mock的一个支持了OK所以所以说还是比较简单的那么下面我们来看一下他的一个这个数据那么其实呢我在这个位置已经
[01:35] 整理好了大概我们需要给他就提供了8个这样的一个Mock的服务那么可以看到有这个叫什么index的menu就是首页这个菜单index的info就是首页的一个资讯的数据还有就FAQ就是首页的一个下面这个数据我们来看一下就是下面的
[01:57] 这个问答这个数据还有下面的一些这个房源的一些数据啊等等都是为了为他提供了这样的一个数据这个数据呢都是按照我们原有的一个数据来先做一个提供啊所以呢称之为叫做Mock嘛对吧好那么接下来我们来看怎么做啊那么我们把它呢写到一个Publish文件那么我们打开我们的项目啊在resource这个下面我们创建一个文件这个文件呢就叫这个MockData.publish文件
[02:26] 那么我们把它加到Git里面去接下来把这个数据我们拷贝到这个文件中那么拷进来之后我们会发现在这个位置是有一些中文的转码那么这样的话我们去查看这个文件的时候并不太友好所以我们需要把这个
[02:45] IDEA做一个设置让它显示的是中文那么怎么设置是在这个位置有一个settings下面有一个editor下面有一个叫failencodings我们下面有个go把这个go去打一下就是说去让它通过我们native2ask这样的转码就是通过我们转码工具去做一个转码然后我们点击apply去应用
[03:10] 然后我们可以看到在这个里面它显示的是不是就是中文了但是要注意的是它这个文件的内容实际上的还是转码之后那个编码那么只是显示的显示中文了OK这样的话我们看起来就会比较友好一些好那么下面我们来看一下现在我们已经有了这个配置文件了那么接下来我们要解决的问题就是需要去读取这个配置文件中的内容
[03:37] 那么我们就需要去在这个位置是不是创建一个类装进一个类就叫mockmockconfigure那么这个其实我们前面也写过读取配置文件对吧好那么我们来看一下首先呢把它标记为是一个configuration然后呢我们去读取我们的配置文件叫properties source然后呢我们给它去指定一个指定我们的文件的一个路径是不是就是class pass下面的有一个叫做mock
[04:06] Data properties文件是不是读取它然后呢我们希望它去帮我们去做一个自动的一个自动的一个是不是转化或者说自动的一个读取是不是叫做configurationpublish然后呢我们去指定它的一个前缀就是谁呢看一下前缀是不是有一个mock对吧那么前缀是不是就mock然后呢下面我们是不是就可以去写各种各样的一些
[04:34] 对应的一些这个后面的它的一些参数对吧这样的话是不是就可以完成做一个数据的一个读取OK那么总共呢有有这么多啊咱们一个一个来啊这个叫info那么去call一下然后呢还有呢叫faq啊把它也call过来OK那么下面的这个就不call了吧那我们直接拷贝这个讲义中的这个内容啊那么把它call过来到这个faq这个位置faq那么在这
[05:03] 把它来拷贝一下OK好那么拷贝之后拷贝之后那么这样的话我们其实就已经拿到这个数据了对不对但是我们在其他的位置要使用它的时候还有get set的方法所以我们在这个位置加一个什么的date加一个date助解这样的话就会帮我们去生成生成一些我们的get set的方法OK好那么现在我们是不是就已经完成了我们的一个数据的一个读取
[05:31] 那么接下来呢我们就需要为他提供我们这个Controller那么我们在下面这个位置呢来写一个类就叫mockcontroller那么这个里面内容怎么写呢我们来看一下首先把它标记为是一个Controller或者我们直接用这个restcontroller吧好呢然后呢我们写一个叫request mapping
[05:59] 然后我们设置它叫什么叫Mock然后下面是不是就可以写各种各样的一些方法了对吧当然我们需要先把我们刚刚所写的叫Mock什么Config是不是先注入进来因为我们需要这个里面的一些数据OK把它注入进来注入进来之后下面我们就可以写各种各样的一些方法那么返回值是不是就可以返回的是一个String然后我们写一个方法名就和它一样
[06:29] 叫indexed menu然后呢这个里面内容怎么去写呢我们去写一个request叫get mappingget mapping什么呢是不是就叫indexed menu那么return是不是直接return就可以了return this.mocconfig.什么呢叫get indexindexed menu这样的话是不是就提供了一个Moc服务了OK那我们把我们这个服务呢来重启一下重启一下
[06:56] 那么就是他就是他吧这个API他然后呢我们就重启那么重启之后呢我们来做一个测试看一下我们这个有能不能够成功的返回我们这个数据啊OK好那么我们来看一下他能不能够去去拿到这个数据啊那么在重启的过程中啊我们来打开我们的这个测试工具是不是就是我们restclient的这个测试工具那我们来看一下他是否能够去查询到我们这个数据啊
[07:25] 那么这个地址是不是就MOOC然后呢下面我们来一个indexed menu那么现在呢等待它的一个启动现在启动好了然后呢我们走来发送那么可以看到是不是已经拿到这个数据了对吧拿到这个数据了OK没有任何问题那么现在呢我们是不是就需要把它是不是集成到我们的一些前台系统中那么把这个地址是不是拷贝一下然后呢我们进入到我们的前台系统
[07:53] 那么在前台系统中的是不是有个home.js文件那么在这个.js文件中的我们来看一下那么下面是不是这个menu是把它改造一下对不对那么改造这样我们先把这个我们先给他拷贝一份然后我们做一个做一个注释做个注释OK好然后我们在这个里面我们去把这个地址给他贴过来那么贴到贴到这但是要注意的是
[08:21] 那么我们现在呢要发起的请求不是post请求而是什么呢get请求因为我们后台所要求他的一个请求数据是通过get的方式啊所以呢我们通过get去请求这个地址然后我们来刷新看一下这个效果会怎么样呢走看他是否能够正常的去查询到数据呢
[08:44] OK那么但是发现并不行那么为什么呢其实可以看到在这个位置是不是他提示我们了说我们并没有去支持这个CORS那么我们需要给我们的后台服务的Controller是不是添加一个注解让他支持这个跨域OK那么添加一个什么呢CORS这样的一个支持好那么这样的话是不是就支持了我们的一个跨域然后我们来重启一下
[09:14] 那么等待它重新启动然后我们做一个测试就可以了OK好那么这样看一下它启动好了吗还没有好等待它的一个启动那么启动完成之后那我们就可以看到那么它是否能够去拿到我们的一个数据如果能够拿到那么我们是不是第一个这个Mock就搞定了那么我们第一个搞定那么后面的第二个第三个是不是就是相同的方法了OK好那我们来刷一下看效果走
[09:47] 那么有没有拿到数据呢我们来看一下那么我们可以看到他查询我们的index的menu是不是已经地址改成我们的这个地址了对吧然后呢我们点击这个all啊我们来看一下那么下面呢我们找到这个index的menu在这个下面是不是通过get请求请求我们这个服务所拿到的数据是不是就这样的一个数据啊
[10:09] 跟我们的这个Node.js是不是所提供的一个数据是一模一样哎这样的话呢就先保证我们的功能它是ok的好你看一下是不是没有任何问题啊功能是ok的好那么现在我们第一个这个是不是就搞定了其他的是不是就一样了那么其他的我就不去一个一个去写了啊那么我就把这个啊就直接就贴过来吧那么资讯呢问答呢啊把它这个都贴过来那么这个实现的逻辑啊都是一样的啊这个就不重复了
[10:38] 好然后呢还有的是下面的一些这个资讯资讯还有我的中心好那么把它贴过来之后那我们是不是就需要去改一下我们的前端的一些这个请求的地址OK好那我们来看一下我们就一个一个来做一个改造吧好那么我们进入到我们的这个前端那么在前端这个里面呢我们就直接来给他做一个这个改造
[11:07] 那么这个我们显然的是不是就应该这样去做一个改造对吧mark下面的什么indexindex info那么再加一个index然后来一个info好那么要注意把它改成什么get请求ok那么这样咱们把它全部先把它改成get请求ok好那么faq那么faq是不是就是index下面faq那么把它call一下那么就这样来call
[11:35] 是不是拷贝到这个位置来好然后呢下面的这个呢是我们的一些房源的信息那么就index host来看一下是不是index这个host好那么这样的话我们是不是首页啊是不是基本上就OK了来刷新一下看效果啊这样的话呢我们就可以看到啊它应该是没问题的有报错啊我们来看一下什么情况这个呢发起的什么请求呢
[12:11] get请求没问题我们来看一下这个是get请求我们这个服务并没有重启对吧刚刚我们把它贴进来之后并没有重启所以我们来重启一下重启一下服务我们来做个测试好那么我先把这个视频暂停一下好那么现在我们这个服务就重启好了我们来看一下那么刷新一下看效果那么可以看到
[12:36] 是不是已经就去请求了我们所Mock的服务然后拿到这个数据功能跟之前是一模一样的对吧那么在我们前面的修改过程中我们只修改了前面的几个那么后面还有两个一个是查询的资讯一个就是我们的我的中心还没有做修改那我们一起来修改一下这个查询资讯在哪里呢在这个位置是在这个就有一个资讯我们点击它
[13:02] 那么点击它之后呢上面有三个这个tab按钮一个资讯一个头条还有一个问答啊这样的一个这三个切换然后呢我们来看一下它的一个请求那么当我点击这个头条的时候那么可以看到它所请求的这个地址是不是就是这个叫infos然后呢list然后呢所传递的参数呢就是有这么几个参数哎OK那么我们是不是就可以把它去改造一下对吧就改造一下那么这块怎么改造呢
[13:31] 可以看一下在前面我们的实现的过程中呢在Controller中啊那么我们就也是根据它的一个类型去返回啊三个不同的这个数据也就是说匹配这个123所以呢需要在请求的这个链接的后面啊给我们去传递一个参数就这个type这个参数啊那我们来改造一下来找一下这个位置啊那我们可以看到它的一个这个地址是不是这个份的
[13:57] 然后我们找到这个fund.js这个文件那么在这个里面其实我们可以看到它是不是有一些这个URL的信息其实我们去给它改造一下这个URL是不是就可以了那么我们来看一下那么在这个位置我们就给它前面去写一下我们的地址来拷贝一下这个地址就是前面的mock前面这个都是一样的对吧然后我们来一个info这个list然后我们需要一个问号去传递一个type等于谁呢
[14:26] 等于去加一个它下面的这个那我们就直接写死吧那就直接写1就好了那么下面这个date这个这个就不需要了对吧哎OK那么呃这个我们就给它注掉吧就呃注掉好注掉然后呢这个呢这个把逗号去掉然后呢同理下面会就会变成什么呢这个改成什么呢改成2对吧这改成2然后呢把这个下面给它也注掉
[14:54] 好然后呢同理那么下面这个改成3这个改成3然后呢把这个也给他住掉好这样的话呢我们把这个地址就改完了改完之后呢他最终的加载是在哪个里面是在这个有个叫load more这个里面去做一个加载我们来看一下这个里面的一些具体的加载的一个动作在哪里呢我们找到他的一个请求是不是在这里做一个这个加载那我们来改成什么呢get请求
[15:21] 然后呢URL是不是就它然后呢下面这个参数这个参数是不是就没有了对吧那么我们把这个参数给它去掉好那么这样的话我们是不是就改造完成了来刷新看一下效果那么到这个里面刷新走等待它的一个刷新那我们可以看到它现在它的请求它的请求type我还找不到这个type这个属性找不到type这个属性那么它可能还需要这个type属性那这样
[15:53] 我们把这个type属性呢还是给他去做一个保留但是呢我们URL是不是已经涵盖了这个携带了这个type这个数据对吧那么这样咱们为了这个最小化的去改动前端这个代码那我们给他还原把这个还是保留然后呢把这个呢逗号加回来好这样的话我们来看一下效果他是否能够请求我们的一个服务呢来看一下
[16:21] 好那现在呢是不是已经就已经就加载到我们的数据了对吧那么可以看到他的请求是不是type等于1然后呢去拿这个数据是不是拿到我们这样的一个数据啊对吧拿到这个数据然后呢我们点击这个头条是不是就去type等于2去拿这个数据没有问题然后呢type等于3去拿这个数据啊也没有任何问题啊都是一样的好那么现在呢我们是不是就已经把这个是不是做完了那么还有一个呢是
[16:50] 在下面这个位置有个叫mineinfo就是我的中心在这个里面在这个下面的有一个请求是不是叫infoinfo是不是就是看一下是不是mineinfo这个地址我们把它也改一下那么还是进入到我们这个前端这个系统中找到一个mine下面有一个mine.js然后这个里面我们找下他的一个请求数据的一个地址是不是是在这个是上传头像这个我们先不管他找到一个info
[17:20] 是不是mineinfo在这那我们去改一下改成getget一个地址我们也call一下call一下地址就是这样的一个地址把它call过来然后去网站一贴那么就是moke下面的mineinfo我们来看地址对不对就是mineinfomoke下面mineinfook没有任何问题
[17:40] 那么这样的话呢我们就去做一个这个请求那么这个参数参数就保留吧我们就看一下他是否能够去拿到这个数据就可以了然后呢我们到这个myinfo这个里面呢我们来刷新一下刷新看一下效果OK那么这样的话呢他是不是就请求到我们这个地址然后呢去拿到我们这个数据
[18:03] OK先保证拿到数据然后的功能呢跟之前是一样的哎这样的话我们就实现了这个MOOC的服务那么这样的话呢我们其实呢就是已经为我们的一个前端系统是不是提供了这个MOOC服务这样的话呢从理论上来讲我们是不是就可以把这个Node.js这个服务给它停掉了我们就不需要这个服务了对不对但是呢我们其实有一些服务呢我们并没有去修改比如说像这面的点击这个按钮之后
[18:33] 的这个我们并没有去做一个修改那么他目前的请求的还是Node.js的这个服务所以Node.js这个服务我们先做一个保留哎OK好那么关于我们这个mock服务的一个功能呢我们就讲到这里那么其实我们这样做的一个目的呢就是哎那么我们要把这个所有的请求呢都有我们自己来做一个提供而不需要这个通过Node.js为他提供这样的一个服务哎OK好那么关于这个mock服务呢我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Spring Boot 构建一个 Mock 服务，为前端 React 应用提供模拟数据支持，包括配置、控制器编写和前端调用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示前端 React 应用在 http://localhost:9000/home 的页面，显示“一线江景度假洋房”广告和多个功能图标。
画面 2: 展示 PDF 文档，标题为“1. 仿mock服务”，内容说明为前端系统提供 mock 服务，包括 GraphQL 查询列表、更新房源功能、Redis 缓存和 WebSocket 门。
画面 3: 展示 IntelliJ IDEA 中的 MockConfig.java 文件，代码内容为：
```java
package cn.itcast.haoke.dubbo.api.config;
import org.springframework.context.annotation.Configuration;
@Configuration
@PropertySource("classpath:mock-data.properties")
@Component
@ControllerAdvice (org.springframework.web.bind.annotation)
@ConfigurationProperties (org.springframework.context.boot.context.properties)
@Conditional (sun.misc)
@ConditionalOnBean (org.springframework.boot.autoconfigure.condition)
@ConditionalOnClass (org.springframework.boot.autoconfigure.condition)
@ConditionalOnEnabledResourceChain (org.springframework.boot.autoconfigure.condition)
@ConditionalOnExpression (org.springframework.boot.autoconfigure.condition)
```
画面 4: 展示 IntelliJ IDEA 中的 MockConfig.java 文件，代码内容为：
```java
class MockConfig {
    String indexMenu;
    String indexInfo;
    String indexFaq;
    String indexHouse;
    String indexList;
    String infosList1;
    String infosList2;
    String infosList3;
    String my;
```
画面 5: 展示 IntelliJ IDEA 中的 MockController.java 文件，代码内容为：
```java
import cn.itcast.haoke.dubbo.api.config.MockConfig;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
@RequestMapping("mock")
@RestController
public class MockController {
    @Autowired
    private MockConfig mockConfig;
    @GetMapping("indexMenu")
    public String indexMenu() {
        return this.mockConfig.getIndexMenu();
    }
```
画面 6: 展示 Advanced REST Client 中的请求页面，URL 为 http://127.0.0.1:18080/mock/indexMenu，状态为 200。
画面 7: 展示 IntelliJ IDEA 中的 MockController.java 文件，代码内容为：
```java
import org.springframework.web.bind.annotation.RestController;
public class MockController {
    @RequestMapping("mock")
    @RestController
    public class MockController {
        @Autowired
        private MockConfig mockConfig;
        @GetMapping("indexMenu")
        public String indexMenu() {
            return this.mockConfig.getIndexMenu();
        }
```
画面 8: 展示 PDF 文档，内容为 MockController.java 文件中的 infosList 方法，代码内容为：
```java
@GetMapping("infos/list")
public String infosList(@RequestParam("type") Integer type) {
    switch (type) {
        case 1:
            return this.mockConfig.getInfosList1();
        case 2:
            return this.mockConfig.getInfosList2();
        case 3:
            return this.mockConfig.getInfosList3();
    }
    return this.mockConfig.getInfosList1();
```
画面 9: 展示浏览器开发者工具 Network 面板，显示多个请求状态为 403，包括 /infos/list 和 /faq。
画面 10: 展示浏览器开发者工具 Network 面板，显示请求 /infos/list 的响应内容，包含“历史半年销售业绩突破中”等文本。
画面 11: 展示 IntelliJ IDEA 中的 find.js 文件，代码内容为：
```javascript
url: 'http://127.0.0.1:18080/mock/infos/list?type=2'
```
画面 12: 展示浏览器开发者工具 Network 面板，显示请求 /infos/list 的响应内容，包含“历史半年销售业绩突破中”等文本。
画面 13: 展示 IntelliJ IDEA 中的 my.js 文件，代码内容为：
```javascript
this.state = {
    uname: '',
    avatarPath: false,
    openAvatar: false,
    openImage: false,
    avatar: ''
};
componentWillMount = () => {
    axios.get('http://127.0.0.1:18080/mock/my/info', {
        user_id: localStorage.getItem('uid')
    }).then(ret => {
        this.setState({
            uname: ret.data.username,
            avatarPath: ret.data.avatar
        });
```
画面 14: 展示 PDF 文档，内容与画面 2 相同，标题为“1. 仿mock服务”，内容说明为前端系统提供 mock 服务，包括 GraphQL 查询列表、更新房源功能、Redis 缓存和 WebSocket 门。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 3:
```java
package cn.itcast.haoke.dubbo.api.config;
import org.springframework.context.annotation.Configuration;
@Configuration
@PropertySource("classpath:mock-data.properties")
@Component
@ControllerAdvice (org.springframework.web.bind.annotation)
@ConfigurationProperties (org.springframework.context.boot.context.properties)
@Conditional (sun.misc)
@ConditionalOnBean (org.springframework.boot.autoconfigure.condition)
@ConditionalOnClass (org.springframework.boot.autoconfigure.condition)
@ConditionalOnEnabledResourceChain (org.springframework.boot.autoconfigure.condition)
@ConditionalOnExpression (org.springframework.boot.autoconfigure.condition)
```
画面 4:
```java
class MockConfig {
    String indexMenu;
    String indexInfo;
    String indexFaq;
    String indexHouse;
    String indexList;
    String infosList1;
    String infosList2;
    String infosList3;
    String my;
```
画面 5:
```java
import cn.itcast.haoke.dubbo.api.config.MockConfig;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
@RequestMapping("mock")
@RestController
public class MockController {
    @Autowired
    private MockConfig mockConfig;
    @GetMapping("indexMenu")
    public String indexMenu() {
        return this.mockConfig.getIndexMenu();
    }
```
画面 8:
```java
@GetMapping("infos/list")
public String infosList(@RequestParam("type") Integer type) {
    switch (type) {
        case 1:
            return this.mockConfig.getInfosList1();
        case 2:
            return this.mockConfig.getInfosList2();
        case 3:
            return this.mockConfig.getInfosList3();
    }
    return this.mockConfig.getInfosList1();
```
画面 11:
```javascript
url: 'http://127.0.0.1:18080/mock/infos/list?type=2'
```
画面 13:
```javascript
this.state = {
    uname: '',
    avatarPath: false,
    openAvatar: false,
    openImage: false,
    avatar: ''
};
componentWillMount = () => {
    axios.get('http://127.0.0.1:18080/mock/my/info', {
        user_id: localStorage.getItem('uid')
    }).then(ret => {
        this.setState({
            uname: ret.data.username,
            avatarPath: ret.data.avatar
        });
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2: PPT 标题为“1. 仿mock服务”，内容为：
- 为前端系统提供mock服务
- 前端系统中通过GraphQL查询房源列表
- 实现后台系统的更新房源功能
- 为接口服务添加Redis缓存
- WebSocket入门
画面 8: PPT 标题为“1. 仿mock服务”，内容为：
- 为前端系统提供mock服务
- 前端系统中通过GraphQL查询房源列表
- 实现后台系统的更新房源功能
- 为接口服务添加Redis缓存
- WebSocket入门
画面 14: PPT 标题为“1. 仿mock服务”，内容为：
- 为前端系统提供mock服务
- 前端系统中通过GraphQL查询房源列表
- 实现后台系统的更新房源功能
- 为接口服务添加Redis缓存
- WebSocket入门

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

