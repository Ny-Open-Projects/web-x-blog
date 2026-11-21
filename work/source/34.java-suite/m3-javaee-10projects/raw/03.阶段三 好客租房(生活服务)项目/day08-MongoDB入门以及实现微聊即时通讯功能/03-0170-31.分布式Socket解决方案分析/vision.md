# 画面线理解：31.分布式Socket解决方案分析

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\31.分布式Socket解决方案分析【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:10, 00:13, 00:21, 00:27, 00:30, 00:34, 01:20, 01:24, 01:29, 03:18, 06:31, 06:46, 06:49
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:54:12

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
