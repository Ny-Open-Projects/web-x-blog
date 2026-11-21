# 25.实现微聊系统之实现WebSocket的业务逻辑

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\25.实现微聊系统之实现WebSocket的业务逻辑【海量资源尽在 ubkz.com】.mp4
- 时长 20分24秒（音频 1224s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 那么接下来呢我们来看一下它的实现具体的一个实现那么下面呢我们就参考我们的讲义来做一个代码的一个编写那么我们来创建一个message的一个hander这个hander呢其实就是在处理我们的一个接收消息和我们发送消息的一个逻辑那么我们先来创建一个包就叫WebSocket那么我们先把这个包呢先创建出来就在im这个包下面呢我们就创建一个包
[00:26] 那么就叫WebSocket那么所有相关于这个WebSocket的一些代码我们都丢到这个里面来然后我们创建一个这个message handler他呢就去处理一些接收发送消息的一些逻辑那么我们写一个类那么他呢其实是要去实现我们这个hander这个接口就是text WebSocket handler这个接口那么把这个接口这个包导入进来然后呢把它标记为是一个component因为我们要把它加入到spin的容器中
[00:54] OK那么下面呢我们就要去重写它的复利中的这个方法那么我们来重写一下那么在这个里面怎么重写首先呢我们需要重写的第一个呢就是我们这个建立连接之后要去做的事情就是说我们的客户端跟我们的这个服务端建立连接之后呢我们要做什么事情呢其实呢我们是需要将我们的这个用户的一个这个Session这个对象啊我们需要去收集起来
[01:24] 那么收集起来有什么用呢就是我们前面讲这个逻辑的时候其实我们也说到我就说在这呢我们需要去判断一下你用户币到底存在不存在那么我们因为我们要去拿到这个用户币的这个session然后去给他去做一个推送数据ok所以呢只要有用户只要有用户他一旦去跟我们的服务端产生连接的时候呢我们就把这个session
[01:48] 丢到我们这个map中注意丢到这个map里面来那么我们这个map呢是一个static啊final的这样的一个类型那么我们是不是就可以保存下来了ok那么我们就可以通过这个session中来判断哎这个用户b的这个有没有这个session如果有那也说明这个用户b在线对吧那么我们就可以直接把消息推送给他ok就是这样的一个逻辑啊那么我们可以看到这个session它本身是一个map啊定一个map
[02:13] 它的key我们把它定义为是一个lock类型那么显然就是它的一个什么用户的一个ID那么value就是一个WebSocket的这样的一个session那么问题来了我们这用户的ID从哪来呢从哪来呢那么可以看到在我们登录之后就是我们连接之后在这个位置它其实并没有并不能够拿到用户传递的一些参数那么我们
[02:40] 可以通过什么呢在Session中是不是可以通过一个Attributes拿到在我们前面就是进入它之前是不是会有一个我们的一个拦截器那么在拦截器中是不是就可以做一些逻辑的处理把这个UID先丢到我们的这个Attributes中然后在我们这个位置中是不是就可以拿到我们这个UID了对不对OK它大概的逻辑就是这样的一个逻辑好那么下面我们来看一下那么咱们把这个先拷过来这个就是我们定义了
[03:10] 全局的一个这样的一个map好那么我们把这个拿过来把这个代码贴过来好嘞那么这样的话呢我们其实就实现了当用户是不是一旦连接到我们这个服务端的话那我们创业连接之后呢我们就把这个session丢到我们这个map中那么在这个map中我们是不是就可以通过这个ID用户的ID就可以去拿到它所对应的一个
[03:39] 这个Session然后呢就看到他有没有在在有没有是不是在线如果在线的话就可以把消息推送给他了OK好那么但是呢我们需要解决的问题呢就是这个UID我们前面说过是不是可以在他的前面是不是给他放一个什么的拦截器在拦截器中是不是就可以把这个UID给他丢进去啊所以呢接下来我们首先要去要写的就是他这个拦截器啊那我们来看一下他这个拦截器那么这个在这个拦截器中呢我们要做的逻辑呢就是
[04:07] 在握手之前就是在我们的客户端与服务端建立连接之前呢我们要做这样的一个事情就是我们拿到他的一个请求的一个URL也就是他这个pass然后呢我们去通过一个这个斜段做一个分割去拿到他的一个参数那么什么意思就是说我们客户端呢我们这个客户端去连接到我们服务端的时候
[04:33] 是不是通过ws冒号双斜杠是不是我们的一个地址比如说这个127.0.0.1冒号18081假设这个地址然后我们在这个里面需要去给他设置的是一个他请求路径比如说ws然后后面我们其实传递一个什么的uid对吧通过我们的一个地址是不是做一个传递那我们就需要在我们的拦截器的这个位置在拦截器的这个位置我们去对我们的请求这个pass
[05:03] 然后呢做一个分割按照一个斜杠是不是做一个分割去拿到我们所对应的一个参数哎ok那么是这样的一个逻辑啊那么所以呢我们接下来呢要写的就是这个拦截器把这个拦截器我们先丢过来那么我们来看一下啊这个拦截器拦截器啊是它然后呢我们去实现我们这个拦截器的接口把它丢过来哎然后呢我们去把它呢去呃
[05:32] 去导入这个包然后去实现它的一些这个方法那么同样的这个拦截器也要加到我们的spin的容器中所以我们给它添加一个叫做component这样的一个注解然后这个里面的逻辑我们就不去写了我们就直接call过来了因为这个也是比较简单的逻辑就是做一些判断然后做一些分割
[05:54] 那么我们来看一下如果在握手之前我们去做一个分割发现你这个分割之后来看一下你分割之后是不是通过它分割你这个长度不等于2长度不等于2我就直接return这个force就可以了就是我拒绝去握手那么肯定这连接是不成功的对吧然后我们再去做一个判断如果我拿到后面的这个数字后面的这个值它不是一个数字的话
[06:19] 在这个位置判断是否为数字是否为数字如果发现它不是因为前面是取反如果不是数字的话那么也是把它return false因为在我们的这个全局的这个map中我们要求它是一个none类型所以必须要保证传入这个参数是什么呢是一个数字你不能传一个什么abc过来对吧所以我们简单做一个校验然后如果
[06:45] 这两个义父全部都通过的话那么我们就把它只做一个浪形的一个转化然后呢丢到h build之中然后呢retin2代表着可以去握手了啊好那么这个就是一个拦截器啊拦截器那么我们有了这个拦截器之后
[07:00] 那么在我们这个handle中是不是就可以拿到我们这个UID了把它丢到这个里面来那么在我们的全局的这个map中呢就可以拿到我们的一个这个session对不对OK这个呢我们是不是只做了一个是在建立连接之后要做的一个事情那么接下来我们要做的事情呢就是当我们的这个用户客户端向我们的服务端去发送消息的时候那么我们就需要去处理他的这个消息了那我们来看一下这个处理消息的一个逻辑是怎么样的一个逻辑呢
[07:29] 那么我们去还是依然重写他的这个hunter这个方法那么在这个里面呢我们一点一点的看一看逻辑啊那么首先呢我们是需要需要我们通过我们session中是不是拿到我们这个uid对吧拿到uid那么然后呢我们需要去拿到我们的消息的内容对消息的内容的做一个解析拿到消息中的一个to id和message因为一个用户去向另外一个用户去发送消息的时候
[07:59] 它是不是一定会携带我们的一个to id就是你要发给谁对吧以及消息的内容是什么那么我们把这两个内容的分装成一个阶层支付券去做一个发送那么我们是不是在这个位置可以对我们发送的消息的内容做一个解析拿到这两个内容ok那么拿到这两个内容之后我们就去构造一个我们的message这样的一个对象那么在这个位置构造的时候我们使用的是message build这样的一个对象
[08:28] 这样的一个方法因为在我们前面的这个message中我们给它增加了一个来看一下增加了一个build这样的一个注解它就会帮我们生成一个build这样的一个方法所以通过这个build的方式就可以做一个构造我们的对象OK那么当我们构造好一个message之后我们先把它保存到我们的mocoDB里面去然后下面我们就判断判断这个to这个用户是否存在就是你发给的目标用户存在在不在线
[08:58] 那么我们就去这个session里面去拿这个他的一个session那么如果能够拿到那么并且他是处于open的一个状态的话那么我们就向他去发送一个消息他发送一个消息然后呢去更新我们这个状态把它更新成为2就已读这个状态因为在前面的这个状态C5中呢他的这个状态是1对吧就未读这个状态那么在这个点呢有一个点还需要说明的一点就是我们像
[09:26] 我们的客户就是用户币去发一个消息的时候那么具体发这个消息的内容我们暂时可能还是确定不了所以我们就先把这个message就给他去做一个序列化序列化成一个json去做一个发送OK那么如果需要去
[09:45] 规定或者说去协商这个格式的话到时候再去改这个逻辑就可以了所以我在这个位置加了一个todook好那么接下来我们就把这个逻辑我们就贴过来这个逻辑我们就讲完了这个逻辑就按照我们刚刚所分析的所分析的这个它的一个流程去编写那个逻辑好那么把这个当然上面这个也需要把它也丢过来好那么把它丢到这把这个包导入进来
[10:15] 好嘞那么有了它之后呢我们继续看下面的逻辑那么下面呢就需要去构造一个message的这个对象就我们自己写的这个message的这个对象哎OK那么构造完成之后呢我们就需要把它保存到我们的mongo db里面去那么mongo db呢就需要按照我们刚刚所自己写的一个这个dao是不是做一个保存的哎OK好那么把它丢到栅栏是不是做这样的一个c5的一个操作
[10:43] 那么接下来就需要去判断我们的用户是否在线是否在线好把它丢过来OK好那么来看一下那么判断它是否在线刚刚杰德我们也说过通过我们的全局的System在这然后去通过 UID就是这个to的ID就是你发给的目标用户去拿它的一个System看能不能拿到如果能够拿到那说明它肯定在线那么去发消息如果拿不到拿不到的或者说
[11:16] 那个用户用你的目标用户并不在线那么并不在线的话那么你不做任何处理了把这个消息保存到芒果DB就OK了好那么到这里呢我们的这个发送消息逻辑啊是不是就搞定了哎OK那么我们这个拦截器也搞定了那么接下来呢我们就需要去写一个我们的一个config这个类这个类我相信大家应该都记得啊就是我们前面在讲我们的WebSocket的时候就讲过这个类
[11:42] 在这个类里面是不是就可以去配置和注册我们的一个WebSocket好那么把这个格式去整理一下那么在这个里面我们可以看到那么我们把刚刚的这个message handler以及我们这个拦截器都注入进来然后在这个里面我们设置了它的一个请求的URL就是ws下面的UID跟我们刚刚所分析的地址是一样的这样的一个地址
[12:08] 然后呢我们给他去设置这个允许做一个跨域的请求设置一个拦截器好那么config这个类啊什么就搞定了那么接下来呢我们来编写一个启动类啊编写一个启动类那么就可以去做一个测试了对不对好像我们还应该缺少一个配置吧在这个application中我们并没有指定我们的服务的
[12:31] 端口对不对如果你没有指定端口的话那么这个想象肯定是不合适的因为我们需要通过我们这个端口才能够去访问到他因为毕竟你建立WebSocket的连接之前先要借助于http的一个连接对吧那么所以我们打开一个我们的一个工程我们打开我们的manager工程把它来打开一下ok打开我们来看一下这个里面的配置在这那么是不是需要有这样的一个配置把它扣过来
[13:02] 然后呢我们丢到这我们改成18081因为不能跟我们那个冲突ok好到这里呢我们的这个配置是不是就搞定了那么接下来呢我们来做一个测试啊来看一下下面呢我们去做这个测试啊测试呢我们借助于两个工具来做测试那么我们就先来去把它启动吧启动好之后呢我们再来做一个测试ok那么我们就到这然后呢去直接run一下
[13:29] 或者我们debug启动吧一会儿我们可以去打一些断点我们来看一下这种消息的处理啊OK好那么我在这儿吧我在这里面呢我去打两个断点一个呢是在这儿一个是在我们这个用户在我们跟我们建立连接之后啊OK好那么现在我这个服务呢就跑起来了然后呢我们来做一个测试啊那么在这儿呢我已经打开了两个这个测试的一个工具
[13:57] 一个呢就是我的谷歌的安装这个插件另外一个就在线的这个工具啊我们来测一下那么我们用这个谷歌的这个插件呢我们来模拟用户一而这个在线呢我们来模拟这个用户二就是我要用户一向这个用户二去发送这个消息我们来看一下那么这样我们在这个这个这个呃在我们这个就是拦截器里面我们也打一个钝点啊然后呢我们去看一下它的一个连接啊然后呢我们点击这个open
[14:26] 那么现在呢你看请求是不是就来了往下面走走拿到他请求是不是等于看一下他的SS那么显然是不是有两个数据WS和1001对吧通过然后呢继续往下面走到这呢我们可以看到他呢不是数字是数字所以呢就没有return to继续往下走把它丢到Hbuild里面去然后通过好那么现在呢我是不是就去把我的这个sense可以丢到我的这个把sense丢到我这个map中对吧
[14:56] 而map现在是空的没有任何的内容然后我通过走那么现在我这个用户是不是我这个session里面其实就有了有了是不是一个map中是不是有了一个session了那么这是我第一个用户是不是就连接成功了我们来看第二个用户我点击开启连接走那么下面我们来看一下它的请求也是一样对吧你看一下OK没问题然后通过走
[15:24] 那我们来看一下到这呢他要把这个1002是不是再丢进去那么在原有的map中是不是已经有一个了对吧然后呢我们再丢一个进去走再丢一个进去好嘞那么现在呢我这个1002这个用户是不是也连接成功了那么接下来呢我让这个1001给1002去发一个消息那么发什么消息呢我们来看一下那么消息的内容长什么样呢那么显然是不是根据他是不是来的对吧OK那么我们就来一个Jason一个字符串
[15:52] 然后呢这个里面要发送的是一个叫to id叫什么呢改成这个英文to id我发给谁呢1002然后呢再来写一个叫message叫什么呢比方说message我们就叫你好发这样的一个消息然后呢我们点击这个发送走那么可以看到请求是不是就进入到我这个里面来然后呢往下面走走拿到我的这个uid是不是1001
[16:23] 然后我们继续往下面看走去做一个解析然后走走是不是拿到这个数据了message就是这个你好然后我们去构造一个message的对象message对象然后我们去做一个数据的一个保存那么现在显然就保存到数据库里面去了我们来检查一下有没有呢来看一下那么1001向这个1002去发一个消息是不是叫message的这个你好OK好那么现在是不是已经有了这个
[16:53] 发送完消息了那么我们来判断一下那么1002看在不在线那么发现了这1002在线因为这session中我们已经拿到了他的一个session然后我们接下来是不是就需要向我们的1002去发送消息了然后往下面走去发送消息发一个消息给他好那么我们来看一下1002他有没有接触到消息你会发现那么1002是不是已经接触到消息了说你好
[17:18] 好然后呢我们就可以继续通过了那么这个逻辑呢是不是去修改我们的一个状态来看一下目前这个状态呢它的状态是几呢来看一下状态是1是未读是不是然后呢点击这个通过走那我们来看一下它的一个状态就会变成几呢是不是就变成了2对吧已经被修改了哎OK这个是1001向1002发消息那么反过来我们是不是也可以让1002给1001去发一个消息啊那么我就发一个什么呢
[17:47] 发一个to这个ID就1001内容呢就是说在的在的你有什么事你有什么事OK就发这样的一句话然后我们点击这个发送走那么依然呢断点会进入到我们这个handle中对吧然后呢走去拿到它走走走拿到然后呢去分装我们的一个消息对象然后往下面走走然后呢去判断它在不在线然后呢走
[18:18] 走走OK到这是不是就已经向我们的1001推送了消息了来看一下有没有呢你可以看到在1001这个位置是不是也拿到这个数据了OK那么现在呢我是不是1001也可以向1002再去发送消息啊那么但是我测试的时候呢我把这个连接给它关闭掉好嘞那么现在我这个连接就关闭了那么连接关闭呢我们就来看一下它能不能再次发送成功了呢叫你好在的有什么事没事随便聊聊
[18:48] 没事随便聊聊然后点击这个发送走那么请求是不是又进入我们的这个方法我们再来看一下走走走走走通过然后呢继续往下面看走走就构造这个session对象这个match对象保存没有问题那么我来看一下数据有没有保存进去呢看一下是不是有这个消息了没事随便聊聊然后呢我们继续往下面看走走判断判断我们什么呢你看
[19:17] 这个session中session中是不是已经是已经是这个有虽然是有但是它的状态不是open状态对不对所以呢我们是不是就不会执行这个里面的逻辑ok这样的话呢我们这个消息它肯定还是处于什么呢未读这个状态ok你看状态是不是还是等于1但是我们这个逻辑呢写的还是有点不是太好就是我们应该再加一个这个逻辑就是
[19:46] 当用户去断开这个连接的时候我们是不是可以让他去把这个Sense给他去移除掉对吧把这个Map中的Sense给他移除掉OK那这个逻辑就交给大家去做吧这个应该也比较容易就是我们再去重写一下他的一个连接关闭的一个方法拿到一个这个Sense ID做一个Sense的Remo是不是就可以了OK好那么大家可以把这个逻辑呢去完善一下好
[20:12] 那么现在我们是不是就已经完成了一个这样的一个消息的一个发送了OK好那么关于我们WebSocket的一个代码的一个编写我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 和 WebSocket 的即时通讯（IM）服务端实现，包括消息处理、会话管理、拦截器配置和调试过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 MessageHandler 类的代码，定义了 @Component 注解、私有属性 messageDAO 和 SESSIONS，以及 afterConnectionEstablished 方法用于获取用户 ID。
画面2：展示 IM 服务的流程图，用户A发送消息到 IM 服务器，服务器存入 MongoDB 消息表，然后判断用户B是否在线，若在线则发送给用户B。
画面3：在 IntelliJ IDEA 中创建 MessageHandshakeInterceptor 类。
画面4：展示 MessageHandshakeInterceptor 类的代码，实现 beforeHandshake 方法，用于校验路径并设置用户 ID。
画面5：展示 ImApplication 启动类的代码，使用 @SpringBootApplication 注解。
画面6：展示 MessageHandler 类中 handleTextMessage 方法的代码，用于处理文本消息，包括保存到 MongoDB、判断接收方是否在线、发送消息和更新消息状态。
画面7：展示 WebSocketConfig 配置类的代码，配置 WebSocketHandler 和拦截器。
画面8：展示一个简单的 WebSocket 客户端界面，用于测试消息发送。
画面9：展示应用启动日志，显示 Tomcat 成功启动。
画面10：展示一个简单的 WebSocket 客户端界面，用于测试消息发送。
画面11：在调试模式下查看 MessageHandler 类中 handleTextMessage 方法的执行过程，变量显示了 session 和 msg 的值。
画面12：在调试模式下查看 MessageHandler 类中 handleTextMessage 方法的执行过程，变量显示了 jsonNode 和 msg 的值。
画面13：在调试模式下查看 MessageHandler 类中 handleTextMessage 方法的执行过程，变量显示了 session 和 msg 的值。
画面14：展示一个简单的 WebSocket 客户端界面，用于测试消息发送。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
import cn.itcast.haoke.im.pojo.UserData;
import com.fasterxml.jackson.databind.JsonNode;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.socket.TextMessage;
import org.springframework.web.socket.WebSocketSession;
import java.util.HashMap;
import java.util.Map;

@Component
public class MessageHandler extends TextWebSocketHandler {
    @Autowired
    private MessageDAO messageDAO;
    private static final ObjectMapper MAPPER = new ObjectMapper();
    private static final Map<Long, WebSocketSession> SESSIONS = new HashMap<>();

    @Override
    public void afterConnectionEstablished(WebSocketSession session) throws Exception {
        Long uid = (Long) session.getAttributes().get("uid");
        // 更新消息状态为已读
    }
}
```

画面2：
无代码，为流程图。

画面3：
```java
package cn.itcast.haoke.im.WebSocket;
public class MessageHandshakeInterceptor {
```

画面4：
```java
public boolean beforeHandshake(ServerHttpRequest request, ServerHttpResponse response, WebSocketHandler handler, Map<String, Object> attributes) {
    String path = request.getURI().getPath();
    String[] ss = StringUtils.split(path, '/');
    if (ss.length != 2) {
        return false;
    }
    if (!StringUtils.isNumeric(ss[1])) {
        return false;
    }
    attributes.put("uid", Long.valueOf(ss[1]));
    return true;
}
```

画面5：
```java
package cn.itcast.haoke.im;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class ImApplication {
    public static void main(String[] args) {
        SpringApplication.run(ImApplication.class, args);
    }
}
```

画面6：
```java
// 将消息保存到MongoDB
message = this.messageDAO.saveMessage(message);
// 判断用户是否在线
WebSocketSession toSession = SESSIONS.get(toId);
if (toSession != null && toSession.isOpen()) {
    // TODO 具体格式需要和前端对接
    toSession.sendMessage(new TextMessage(MAPPER.writeValueAsString(message)));
    // 更新消息状态为已读
    this.messageDAO.updateMessageState(message.getId(), status: 2);
}
```

画面7：
```java
import org.springframework.context.annotation.Configuration;
@EnableWebSocket
public class WebSocketConfig implements WebSocketConfigurer {
    @Autowired
    private MessageHandler messageHandler;
    @Autowired
    private MessageHandshakeInterceptor messageHandshakeInterceptor;

    @Override
    public void registerWebSocketHandlers(WebSocketHandlerRegistry registry) {
        registry.addHandler(this.messageHandler, "/ws").addInterceptors(this.messageHandshakeInterceptor);
    }
}
```

画面8：
无代码，为客户端界面。

画面9：
无代码，为启动日志。

画面10：
无代码，为客户端界面。

画面11：
```java
// 将消息保存到MongoDB
message = this.messageDAO.saveMessage(message);
// 判断用户是否在线
WebSocketSession toSession = SESSIONS.get(toId);
if (toSession != null && toSession.isOpen()) {
    // TODO 具体格式需要和前端对接
    toSession.sendMessage(new TextMessage(MAPPER.writeValueAsString(message)));
    // 更新消息状态为已读
    this.messageDAO.updateMessageState(message.getId(), status: 2);
}
```

画面12：
```java
@Override
protected void handleTextMessage(WebSocketSession session, TextMessage textMessage) throws Exception {
    Long uid = (Long) session.getAttributes().get("uid");
    JsonNode jsonNode = MAPPER.readTree(textMessage.getPayload());
    String msg = jsonNode.get("msg").asText();
    Message message = Message.builder()
            .from(UserData.USER_MAP.get(uid))
            .to(UserData.USER_MAP.get(toId))
            .msg(msg)
            .build();
}
```

画面13：
```java
// 将消息保存到MongoDB
message = this.messageDAO.saveMessage(message);
// 判断用户是否在线
WebSocketSession toSession = SESSIONS.get(toId);
if (toSession != null && toSession.isOpen()) {
    // TODO 具体格式需要和前端对接
    toSession.sendMessage(new TextMessage(MAPPER.writeValueAsString(message)));
    // 更新消息状态为已读
    this.messageDAO.updateMessageState(message.getId(), status: 2);
}
```

画面14：
无代码，为客户端界面。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：
架构图：
- 用户A → 发送消息 → IM服务器
- IM服务器 → 存入 MongoDB 消息表
- MongoDB 消息表 → 判断用户B是否在线
- 用户B在线 → 发送给用户B
- 用户B不在线 → 标记为已读

画面8：
无 PPT 标题或表格数据。

画面14：
无 PPT 标题或表格数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

