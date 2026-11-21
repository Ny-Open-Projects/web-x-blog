# 31.分布式Socket解决方案分析

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\31.分布式Socket解决方案分析【海量资源尽在 ubkz.com】.mp4
- 时长 7分2秒（音频 422s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 刚刚呢我们在做测试的时候后面我发现好像有个问题啊就是呃在这个里面呢我们点击李四的时候啊并没有把这个所有的这个聊天记录都拿到包括后面我们这个进行闲聊的这个内容啊就是这个什么张三的啊我是张三啊不记得了吗等等一些这个消息并没有拿到为什么呢原因是啊并不是我们这个出bug了啊而是我们并没有传递一个我们分页的数据因为他默认就拿十条数据
[00:27] 因为我们是不是在我们的Controller里面是不是做了一个默认值默认是不是拿失调啊哎呀OK那么这个呢我们就暂时就这样了我们就不去做一个具体的一个这个这个改造了那么大家也可以去让他去支持一个分页啊因为我们前端的并没有实现个分页那么你也可以把这个位置改大比如改成100把这个值调大一点对吧那就可以拿到这个数据了哎呀OK这个其实并不是什么太大的一个问题啊
[00:53] 好嘞那么接下来呢我们来看一下最后一个问题啊其实这个这个问题呢是呃就是我们会出一个解决方案但是呢我们今天呢不做一个解决呃我们在呃第二天就是我们在第二天的后面课程中呢我们会去做这样的一个解决啊那么我们来看一下它究竟是一个什么问题呢是分布式的一个suck it的一个解决方案
[01:20] 那么在前面我们的实践中呢我们是将我们这个session啊我们去把它去丢到我们的一个呃还记得吗丢到我们的一个map中的啊就是我们将所有的一个用户的一个在线的一个session都丢到这个里面来哎都丢到这那么丢到这个里面有没有问题呢大家可以思考一下想一想有没有问题呢是不是有啊那么如果说我现在客户端有非常多对吧那么我是不是就会有很多的一些这种session都会丢到我这个map里面
[01:48] 那么必然是不是会对我的这个整个这个服务器会有一些这种压力对吧哎OK因为建立连接很多吧那么我这个时候如果想要对我的服务器做一个分布式的话显然肯定做不了啊做不了为什么呢如果说你在这个里面啊如果说你你在A这个服务器里面去存了一些这个session那么我做了分布式我有个B服务器在这个里面是不是就拿不到你这个里面的一些这个对象啊对不对OK那么
[02:17] 这个问题应该怎么样去解决呢啊应该怎么样去解决那我们就简单的来分析一下他这个解决方案当然了之前的有人提出这个解决方案就是什么呢就是我们可以把这个map啊我们不要定义在我们的这个全局我们把这个map呢哎丢到哪里呢我们丢到我们那个redis里面去啊我们创建一个redis然后呢把它呢往这个redis里面一丢然后呢我们在其他的一些这个服务中呢在我们其他的一些服务中啊
[02:47] 我们其他节服务中那我们都去到我们Redis里面去取不就可以了吗好像这种解决方案听起来是OK的但是实际上你在做的时候它是不行的为什么不行的原因是这个WebSocket的一个session这个对象它是一个保持在线的这样一个对象它是没有办法做一个序列化的没有办法把它丢到一个Redis中的
[03:14] 所以这种方案是行不通的所以接下来我们就要去分析一下我们给大家给出的解决方案呢是通过这种消息系统去做一个解决接下来我们就来看一下这个什么这个消息系统怎么样去解决啊那么我在这个位置画了这样的一个简易的一个图啊那么这个图什么意思呢给大家来讲解一下就是在我们的左边这个位置呢是我们的一个socket的客户端在中间的这个呢是我们的一个socket的一个服务端
[03:42] 然后呢右边这个呢是我们的一个消息系统那我们来看一下那么当我的客户端非常多的时候我画了很多这个圆圈代表着我的客户端客户很多啊然后呢我这个socket呢我做了这样的一个分布式然后呢我每一个这个每一个这个节点中呢我都是保存了一个这个map保存了一个map保存了map然后呢我的这个每一个这个每一个这个服务端呢它都去
[04:11] 订阅我消息系统的一个订阅一个消息吧订阅一个消息OK就是这样的一个架构然后呢我们来看一下那么如果现在我有两个客户端一个是客户端A一个是客户端B那么客户端A呢他呢把消息发送到他发消息要给B然后但是呢这个A这个用户是和我们的这个服务器是不是建立了一个通道建立一个WebSocket的一个连接
[04:39] 那么我们把这个连接是不是丢到这个map里面来他要发送给B但是我们这个B用户他这个连接不是和他建立连接的而是和下面的这个建立了一个连接那么建立连接之后是不是在这个里面他要发送给B那么显然这个map中是不是就没有B的一个生成你没有办法直接发送怎么办这个时候我们就可以这个用户去发送一个消息给我们的消息系统
[05:05] 那么我们这个消息系统接收到消息之后呢就把这个消息发送给我其他的一些这个客户端那么由于我这个服务是不是订阅了我这个消息对吧所以他就能够接收到我这个消息那么接收到这个消息之后呢我去看一下我这个map中有没有B的这个sense呢发现诶如果有好那我们拿到给他发给消息那么消息是不是就发给B了那么同样的假设我这个是C
[05:32] 那么这个系统是不是也订阅了我的这个消息他是不是也能够拿到我的消息但是呢在他的这个netmap中呢有没有B的这个sensor呢发现没有所以他就不做任何处理了他也能够接收到消息但是呢他不做任何的处理但是他呢可以接收到消息但是他要做处理为什么呢因为在他的内部是不是有一个这个B的一个这个通道在这做一个建立啊
[05:57] OK那么通过这种消息订阅的这种方式是不是就可以解决我们的一个socket的一个分布式的这样的一个问题OK那么我们为什么要去给他做分布式就是原因就是如果你全部都集中在一台的话一台服务器的话那么这个服务器它肯定是撑不住的对不对当你的这个用户量越来越大的时候它肯定撑不住的那么我们通过这种解决方案来做一个解决在我们下一天的课程中我们会学习一个消息系统
[06:25] 然后我们借助于这个消息系统来做这样的一个解决OK好那么关于我们的一个分布式的这样的一个Socket的一个解决方案的分析我们就讲到这其实大家可以去网上去搜一下这样的一个问题其实在网上也是有很多人提出一些解决方案那么目前相对比较靠谱的一个解决方案就是
[06:46] 通过消息这样的一种解决方案来做一个解决OK那么我们也将在我们的项目中具体的去做这样的一个方案的一个实现只是我们今天先不做这样的实现了OK好那么关于这样的一个方案的一个分析我们就讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲一个基于 WebSocket 的即时通讯（IM）系统，重点讲解了如何通过消息中间件解决分布式 Session 管理问题。

2) 按时间顺序列出每张画面的要点：
画面1：展示前端聊天界面，用户“lisi”与“zhangsan”对话，浏览器开发者工具中显示了 WebSocket 连接和消息数据，其中一条消息的 payload 为：{"id": 1002, "username": "lisi", "msg": "你好", "to": {"id": 1001, "username": "zhangsan"}, "sendDate": "2018-12-09T17:45:31.307+0800", "status": 2}。
画面2：终端显示了从服务端获取的聊天消息列表，其中包含多个 Message 对象，例如：{"id": "5c0d472139a2184000000000", "from": {"id": 1001, "username": "lisi"}, "to": {"id": 1002, "username": "zhangsan"}, "msg": "hello", "status": 2, "sendDate": "2018-12-09T17:45:31.307+0800"}。
画面3：与画面2内容相同，为重复展示。
画面4：展示 IntelliJ IDEA 中的 MessageHandshakeInterceptor.java 文件，其中 beforeHandshake 方法用于解析路径并提取 uid：String path = request.getURI().getPath(); String[] ss = StringUtils.split(path, separatorChar: '/'); if(ss.length != 2) { return false; } if(StringUtils.isNumeric(ss[1])) { return false; } attributes.put("uid", Long.valueOf(ss[1])); return true;。
画面5：展示了一个文件夹结构的缩略图，选中的是 MessageHandshakeInterceptor.java 文件。
画面6：展示 MessageController.java 文件，其中包含 @RequestMapping("message") 和 @CrossOrigin 注解，以及一个被注释掉的 //获取消息列表。
画面7：前端聊天界面显示用户“lisi”发送了“我是李四”，浏览器开发者工具中显示了新的 WebSocket 消息。
画面8：展示 PDF 文档，标题为“6、分布式Socket解决方案分析”，内容指出问题：Session 对象放到全局的 Map 中，当连接变得非常多时，这成为了系统瓶颈，解决方案：采用消息系统进行解决。
画面9：展示 MessageController.java 文件，其中 queryMessageList 方法的代码：@GetMapping("message") public List<Message> queryMessageList(@RequestParam("fromId") Long fromId, @RequestParam("toId") Long toId, @RequestParam(value = "page", defaultValue = "1") int page, @RequestParam(value = "rows", defaultValue = "10") int rows) { return this.messageService.queryMessageList(fromId, toId, page, rows); }。
画面10：展示 MessageHandler.java 文件，其中包含 afterConnectionEstablished 和 handleTextMessage 方法，用于管理 WebSocket 会话和处理消息：protected void handleTextMessage(WebSocketSession session, TextMessage textMessage) throws Exception { Long uid = (Long) session.getAttributes().get("uid"); Long toId = jsonNode.get("toId").asLong(); String msg = jsonNode.get("msg").asText(); }。
画面11：与画面8内容相同，为重复展示。
画面12：展示 PDF 文档中的架构图，图中包含“socket客户端”、“socket服务端”和“消息系统”三个模块，其中“socket客户端”通过“订阅”和“发送消息”与“socket服务端”交互，而“socket服务端”通过“Map (session)”管理会话，并与“消息系统”交互。
画面13：与画面12内容相同，为重复展示。
画面14：与画面12内容相同，为重复展示。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面4：
@component
public class MessageHandshakeInterceptor implements HandshakeInterceptor {
    @Override
    public boolean beforeHandshake(ServerHttpRequest request, ServerHttpResponse response, WebSocketHandler wsHandler, Map<String, Object> attributes) throws Exception {
        String path = request.getURI().getPath();
        String[] ss = StringUtils.split(path, separatorChar: '/');
        if(ss.length != 2) {
            return false;
        }
        if(StringUtils.isNumeric(ss[1])) {
            return false;
        }
        attributes.put("uid", Long.valueOf(ss[1]));
        return true;
    }
}

画面6：
@RequestMapping("message")
@CrossOrigin
public class MessageController {
    @Autowired
    private MessageService messageService;
    /*
     * 获取消息列表
     * @param fromId
     * @param toId
     * @param page
     * @param rows
     * @return
     */
}

画面9：
@GetMapping("message")
public List<Message> queryMessageList(@RequestParam("fromId") Long fromId, @RequestParam("toId") Long toId, @RequestParam(value = "page", defaultValue = "1") int page, @RequestParam(value = "rows", defaultValue = "10") int rows) {
    return this.messageService.queryMessageList(fromId, toId, page, rows);
}

画面10：
@autowired
MessageDAO messageDAO;
private static final ObjectMapper MAPPER = new ObjectMapper();
private static final Map<Long, WebSocketSession> SESSIONS = new HashMap<>();
@Override
public void afterConnectionEstablished(WebSocketSession session) throws Exception {
    Long uid = (Long) session.getAttributes().get("uid");
    // 将当前用户的session设置到map中，后面会使用相应的session通信
    SESSIONS.put(uid, session);
}
@Override
protected void handleTextMessage(WebSocketSession session, TextMessage textMessage) throws Exception {
    Long uid = (Long) session.getAttributes().get("uid");
    Long toId = jsonNode.get("toId").asLong();
    String msg = jsonNode.get("msg").asText();
}

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面8、11、13、14：
标题：6、分布式Socket解决方案分析
问题：前面的实现中，将Session对象放到全局的Map中，当连接变得非常多时，这成为了系统瓶颈，因为不能进行分布式部署。
解决方案：采用消息系统进行解决。
架构图：
- “socket客户端”模块指向“socket服务端”模块，通过“订阅”和“发送消息”进行交互。
- “socket服务端”模块包含“Map (session)”组件，用于管理会话。
- “socket服务端”模块指向“消息系统”模块，通过“订阅”和“发送消息”进行交互。

5) 无。

