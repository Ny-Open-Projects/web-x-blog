# 画面线理解：26.实现微聊系统之实现查询历史消息与好友列表的服务

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\26.实现微聊系统之实现查询历史消息与好友列表的服务【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:50, 01:35, 02:06, 02:37, 03:23, 04:06, 05:32, 06:06, 07:10, 08:52, 09:38, 10:20, 11:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:50:31

1) 这一组画面整体在讲什么（一句话）：
讲解基于 Spring Boot 和 WebSocket 的即时通讯系统中，如何实现查询历史消息功能，包括控制器、服务层和 DAO 层的代码实现，以及前端界面和 REST API 的交互。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 PDF 讲义第 4.8 节“提供查询历史消息的服务”。
- 代码片段：MessageController 类的开头部分，包含包声明和导入语句。
  package cn.itcast.haoke.im.controller;
  import cn.itcast.haoke.im.pojo.Message;
  import cn.itcast.haoke.im.service.MessageService;
  import org.springframework.beans.factory.annotation.Autowired;
  import org.springframework.web.bind.annotation.*;
  import java.util.List;

画面 2：
- PDF 讲义内容延续，展示 MessageController 类的 @RestController 和 @RequestMapping 注解。
  @RestController
  @RequestMapping("message")
  @CrossOrigin
  public class MessageController {

画面 3：
- 展示 IntelliJ IDEA 中的 MessageHandler.java 文件，其中包含 WebSocket 会话管理的代码。
  private static final Map<Long, WebSocketSession> SESSIONS = new HashMap<>();
  @Override
  public void afterConnectionEstablished(WebSocketSession session) throws Exception {
      Long uid = (Long) session.getAttributes().get("uid");
      // 将当前用户的session放置到map中，后面会使用相应的session通信
      SESSIONS.put(uid, session);
  }
  @Override
  protected void handleTextMessage(WebSocketSession session, TextMessage textMessage) throws Exception {
      Long uid = (Long) session.getAttributes().get("uid");
      JsonNode jsonNode = MAPPER.readTree(textMessage.getPayload());
      Long toId = jsonNode.get("toId").asLong();
      String msg = jsonNode.get("msg").asText();

画面 4：
- PDF 讲义内容，展示 MessageController 中的 queryMessageList 方法的参数注解。
  @RequestMapping(value = "/queryMessageList")
  public List<Message> queryMessageList(@RequestParam("fromId") Long fromId,
                                        @RequestParam("toId") Long toId,
                                        @RequestParam(value = "page", defaultValue = "1") Integer page,
                                        @RequestParam(value = "rows", defaultValue = "10") Integer rows) {
      return this.messageService.queryMessageList(fromId, toId, page, rows);
  }

画面 5：
- PDF 讲义内容，展示 MessageService 类的开头部分。
  package cn.itcast.haoke.im.service;
  import cn.itcast.haoke.im.dao.MessageDAO;
  import cn.itcast.haoke.im.pojo.Message;
  import org.springframework.beans.factory.annotation.Autowired;
  import org.springframework.stereotype.Service;
  import java.util.List;

画面 6：
- IntelliJ IDEA 中的 MessageService.java 文件，展示 queryMessageList 方法的实现。
  @Service
  public class MessageService {
      @Autowired
      private MessageDAO messageDAO;
      public List<Message> queryMessageList(Long fromId, Long toId, Integer page, Integer rows) {
          List<Message> list = this.messageDAO.findListByFromAndTo(fromId, toId, page, rows);
          for (Message message : list) {
              if (message.getStatus().intValue() == 1) {
                  // 修改消息状态为已读
                  this.messageDAO.updateMessageState(message.getId(), status: 2);
              }
          }
          return list;
      }

画面 7：
- 展示了前端聊天界面（Simple Web Socket Client）和浏览器开发者工具的 Network 标签页。
- 前端界面显示了聊天消息列表，包括“abc”、“dddd”等用户发送的消息。
- Network 标签页显示了多个 HTTP 请求，包括 GET /index.html、GET /mock/index、POST /chat、GET /user 等。

画面 8：
- PDF 讲义内容，展示 JSON 格式的消息数据结构。
  {
    "id": 5,
    "from_user": 1,
    "to_user": 3,
    "chat_time": 1531045313395,
    "chat_msg": "12",
    "info_type": null,
    "username": "Spike",
    "avatar": "public/icon.png"
  },
  {
    "id": 6,
    "from_user": 1,
    "to_user": 3,
    "chat_time": 1531045313395,
    "chat_msg": "12",
    "info_type": null,
    "username": "spike",
    "avatar": "public/icon.png"
  }

画面 9：
- 前端聊天界面更新，显示了新的聊天消息，包括“你好”、“你也好”、“你更好”、“hello”等。
- Network 标签页显示了新的 HTTP 请求，包括 POST /chat、GET /user 等。

画面 10：
- IntelliJ IDEA 中的 UserController.java 文件，展示获取用户列表的代码。
  @RestController
  @CrossOrigin
  @RequestMapping("user")
  public class UserController {
      @Autowired
      private MessageService messageService;
      // 获取用户列表（模拟实现）
      @GetMapping
      public List<Map<String, Object>> queryUserList(@RequestParam("fromId") Long fromId) {
          List<Map<String, Object>> result = new ArrayList<>();
          for (Map.Entry<Long, User> userEntry : UserData.USER_MAP.entrySet()) {
              Map<String, Object> map = new HashMap<>();
              map.put("id", userEntry.getValue().getId());
              map.put("avatar", "http://itcast-haoke.oss-cn-qingdao.aliyuncs.com/images/2018/12/08/15442410962743524.jpg");
              map.put("from_user", fromId);
              map.put("to_user", null);
              map.put("username", userEntry.getValue().getUsername());
          }
      }

画面 11：
- PDF 讲义内容，展示 UserController 中的 queryUserList 方法的注解和部分代码。
  @RestController
  @CrossOrigin
  @RequestMapping("user")
  public class UserController {
      @Autowired
      private MessageService messageService;
      // 获取用户列表（模拟实现）
      @GetMapping
      public List<Map<String, Object>> queryUserList(@RequestParam("fromId") Long fromId) {
          List<Map<String, Object>> result = new ArrayList<>();
          for (Map.Entry<Long, User> userEntry : UserData.USER_MAP.entrySet()) {
              Map<String, Object> map = new HashMap<>();
              map.put("id", userEntry.getValue().getId());
              map.put("avatar", "http://itcast-haoke.oss-cn-qingdao.aliyuncs.com/images/2018/12/08/15442410962743524.jpg");
              map.put("from_user", fromId);
              map.put("to_user", null);
              map.put("username", userEntry.getValue().getUsername());
          }
      }

画面 12：
- Advanced REST Client 插件界面，展示对 /user 接口的 GET 请求。
  Status: 200
  Response:
  [
    {
      "id": 101,
      "from_user": 1001,
      "to_user": 1001,
      "avatar": "http://itcast-haoke.oss-cn-qingdao.aliyuncs.com/images/2018/12/08/15442410962743524.jpg",
      "username": "zhangsan"
    }
  ]

画面 13：
- Advanced REST Client 插件界面，展示对 /user 接口的 GET 请求，返回多个用户数据。
  [
    {
      "to_user": 1001,
      "id": 1001,
      "avatar": "http://itcast-haoke.oss-cn-qingdao.aliyuncs.com/images/2018/12/08/15442410962743524.jpg",
      "from_user": 1001,
      "username": "zhangsan"
    },
    {
      "to_user": 1002,
      "id": 1002,
      "avatar": "http://itcast-haoke.oss-cn-qingdao.aliyuncs.com/images/2018/12/08/15442410962743524.jpg",
      "from_user": 1002,
      "username": "lisi"
    },
    {
      "to_user": 1003,
      "id": 1003,
      "avatar": "http://itcast-haoke.oss-cn-qingdao.aliyuncs.com/images/2018/12/08/15442410962743524.jpg",
      "from_user": 1003,
      "username": "wangwu"
    }
  ]

画面 14：
- PDF 讲义内容，展示 JSON 格式的消息数据结构。
  {
    "avatar": "http://it
