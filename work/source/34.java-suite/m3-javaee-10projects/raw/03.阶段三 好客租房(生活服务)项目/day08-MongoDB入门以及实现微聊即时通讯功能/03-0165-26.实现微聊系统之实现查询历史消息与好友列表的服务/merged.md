# 26.实现微聊系统之实现查询历史消息与好友列表的服务

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\26.实现微聊系统之实现查询历史消息与好友列表的服务【海量资源尽在 ubkz.com】.mp4
- 时长 11分16秒（音频 677s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢,我们需要编写两个服务啊一个呢是查询历史消息的服务另外一个呢就是我们去还有一个呢是查询用户列表这个服务啊那么为什么要实现这两个服务呢原因是,大家可以看一下我们的一个前端的一个这样的一个页面啊那么在我们点击这个微聊的时候呢它会出现一个列表其实这个列表呢属于叫好友的列表,对吧你这个用户有哪些好友
[00:28] 然后呢首先这个是一个接口就是说我们需要给他提供一个数据提供这样的数据然后呢所以我们得要这样的一个服务然后呢我们点击每一个好友进入的时候呢有一个详细的列表那么这个里面呢就是所展现的他们之间的一个聊天的记录所以呢我们需要去给他提供的是一个查询他的聊天记录这样的一个服务那么我们才能够去完成这个动作就是说
[00:55] 当我们的用户跟他点击的时候是不是他就会跟我们的服务端产生一个WebSocket这个连接但是呢他并不是为了WebSocket并不是去拉取这个消息的内容而是用于发送消息的对吧所以说这个list的内容呢还是要通过我们的RESTful的接口拉取到我们的数据所以呢我们需要写这两个服务啊好那么下面呢我们就把这两个服务呢我们来编写一下
[01:21] 那么我们首先需要创建一个Controller的一个包那我们进入这个im这个下面然后呢我们创建一个包就是我们的Controller这个包然后在Controller下面呢我们去写一个叫message Controller这样的一个类就是我们的一个Controller我们因为我们要提供那个res4的一个接口然后呢我们给它去写这几个注解这个我相信大家一个非常熟悉的注解了对吧好然后呢我们把它也导入进来
[01:51] OK那么下面呢我们就写具体的这个实现那么下面呢我们去住一个message的一个Service但这个Service呢现在并没有并没有没关系我们先把这个代码先写好然后呢下面我们来给它创建一个这样的一个Service诶把它拷贝一下好丢到这个里面来好那么我们把这个message的这个对象啊给它导进来然后呢现在是不是还没有这个类啊那么所以呢我们需要在这个下面呢再来创建一个包叫什么呢Service
[02:22] OK那么Service就是下面这个Service对吧那么来创建一个message一个Service来找一下这个Service在哪呢在这然后我们创建一个类叫message Service把它标记为这是一个Service然后我们把它里面内容拷贝过来那么我们要去这样我们先把这个先丢过来然后我们可以看到在control里面我们是不是就可以把Service包导入进来
[02:51] 然后呢我们在他这个里面给他去创建一个这样的方法ok好这个里面内容怎么去写呢我们就调用我们之前写的这个deo这个方法去做一个去做一个这个查询就可以了那么这样咱们先把这个逻辑我们先抠过来吧我们来再来做一个解读然后呢下面是在女称啊应该是在这结束ok搞定了好那么来看一下在这个里面呢我们可以看到哎哎
[03:28] 这个格式有点问题调一下好那我们来看一下在这个位置呢它通过啊我们的Controller中传递我们的参数有form idto id就是你这个谁发给谁就是我这个好友对吧如果我点击是这点击到我这个abc这个好友的话那么就意味着什么呢我是不是就这个我就是当前这个用户对吧to谁呢是不是就是abc这个用户然后呢配置和ros就是要做一个分页
[04:00] 做个分页OK你看是不是有个这样的一个效果当然了现在我们前端呢其实并没有做分页的这样的效果只是我们在我们的服务端去提供结果的时候呢要有个分页的这个支持因为你后面的话在前端去做分页是还是比较容易的好那么然后呢在这个位置要注意了就是我们需要判断一下你拉到的这个消息列表中有没有未读的消息那么如果发现它的状态有未读的我们需要把它修改为状态为二
[04:30] 这个逻辑在我们前面去讲我们的流程的时候是不是有讲过这个逻辑在这有讲过那么发现有未读的那么就需要做一个修改如果没有直接返回就可以了OK这个逻辑在Service这一块做了一个实现我们来看一下这个Controller那么在Controller中它其实就负责去接收参数接收哪些参数有form id和tool id然后配置和ros那么如果
[04:57] 如果我们没有传递这个ros的话也没有传递这个配置的话默认给他是一池给他一个默认值好嘞那么这control了我们是不是就搞定了那么接下来我们来给他提供的是查询用户列表这个服务那么要注意的是这个我们仅仅做一个mock实现因为我们的用户的数据现在我们只是先做一个mock还没有去做真正的一个用户的一个登录ok所以我们做这样的一个简单的一个实现
[05:25] 那么他所需要的数据结构呢是长这个样子那么这个结构呢是我们通过前端的一个请求去抓取到的一个结构那么我们会根据这样的一个结构给他返回一个数据那么Controller呢就是这样来写那么我们把它来拷贝一下进入到我们这个Controller中那么创建我们的这个类UserController然后呢把这个丢过来把这个三个注解丢过来OK
[05:55] 好那么下面呢我们把这个message Service呢注入进来为什么要注入他呢哎为什么注入他呢就是我们要去来看一下这个页面啊那么在这个用户列表这个位置啊他其实呢要去显示一个什么呢除了用户信息本身之外的信息的话需要显示一个这个消息这个消息其实是需要拉取他的一个最近的一个聊天的一个聊天的一个消息的啊但是呢我们现在呢这个
[06:25] message Service或者说我们那个message的deo里面呢并没有提供一个方法可以去拉取他的最新那个消息的那么这个呢我们就突度了大家可以自己去做一下当然了我就可以简单来做就是拉取他的最早的那个消息因为我们是不是可以查查询他的列表啊我们就拿他的第一条消息就可以了这个就偷个来那么就不去做具体的一个实现了哎呀ok这个大家也去做一下应该也是非常容易的一个事情啊好那么我们把下面的这个
[06:55] 具体的实现了我们来靠过来那么我们就考它吧一直到这然后呢我们去拷贝一下OK好那么这个里面呢有一些有一些这个包呢需要我们去导一下然后呢拷贝一下然后这个是有回车的问题把回车问题给它解决掉好没问题了这个把这个包导入进来哎应该就没问题了吧来看一下好那么现在呢就没问题了
[07:29] 但是呢就这个有一个点啊需要大家注意的就是我们在这个位置啊并没有去编写一个去拿他的最新的一个消息啊这样的一个这样的一个服务啊其实去写这样的一个服务呢也是非常简单的啊非常简单的一个一种这个写法啊那么我在这呢只写的是去拿他的一个这个消息啊一条消息这个呢是其实是我们拿的是他最近的啊就是最早的这样的一个消息啊最早的这样的一个消息
[07:59] 那这样在这个位置呢我们加一个加一个说明吧就是有个todo啊这个现在又没有完全做完就是没有去没有没有读取最新消息而是读取了读取了最早的最最早的那个消息OK好那么这是我们没有去实践的一个功能啊
[08:27] 那么也希望大家呢自己能够去把这功能去做一下啊OK那么如果有同学这个不会去做这块如果觉得有问题的话有疑问的话那么也可以去做一些反馈回来啊给大家去去讲解一下好那么我们继续往下面看吧啊那么我们去拿到这个消息之后呢就给他丢到这个里面来去分装就返回就可以了反正这个里面的一个反分装的逻辑啊其实就是参考前面的他的所要求的数据结构去给他做返回就OK了
[08:57] 好那么这两个呢我们就都已经提供好了那么然后呢我们把我们这个服务呢去重启一下重启一下我们这个服务我们看一下啊这个服务重启一下好把它呢重启一下走好那么现在我们这个服务呢已经启动好了那么我来测试一下啊这两个接口OK吗走那么显然这个接口是吧OK的那么拿到他的一个消息的一个记录你好你好一直有对吧
[09:29] 这是我们之前所写的一些这个消息内容你看这个消息拿到了在的有什么事然后呢没事随便聊聊好嘞那么这就是他的一个消息的一个列表那么还有一个呢是根据这个拿他的user就是他的一个用户的一个列表我们来看一下用户的列表呢是在这儿去拿他的一个这个叫什么呢叫from id啊from id就是那就是拿谁呢拿哪个用户对吧拿哪个用户就是我这个用户
[09:58] 要去打谁呢那我就去其实是这样的我们这个呢就仅仅做一个模拟的一个实现模拟的一个实现那么formid呢我就给他去传递一下就好了那么所以呢我在这来写一个叫user然后呢写一个formid那就1001吧这样去写然后呢走那么可以看到返回的一个数据呢就是这样的一个数据那么把我现有的五个条五个数据是不是全部给他返回就可以了那我们现在是不是只够
[10:27] 够到了有五个用户OK好嘞那么当然他有一个图像点击这个图像可以看一下这个图像我们来访问一下是我们自己上传的一个图像无法访问难道是可能是这个地址是不是出问题了地址有可能是出问题了我们来看一下应该是没有问题是不是没有加http猫号风鞋杠猫不应该
[11:00] 那可能我们这个图片地址是有点问题了那这个这个没关系啊这个没有什么太大的这个影响OK好那么一会儿呢我们来试一下这个地址看能不能去访问啊那么到目前为止呢我们的这两个服务是不是就已经提供好了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解基于 Spring Boot 和 WebSocket 的即时通讯系统中，如何实现查询历史消息功能，包括控制器、服务层和 DAO 层的代码实现，以及前端界面和 REST API 的交互。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 PDF 讲义第 4.8 节“提供查询历史消息的服务”。
- 代码片段：MessageController 类的开头部分，包含包声明和导入语句。
  package cn.itcast.haoke.im.Controller;
  import cn.itcast.haoke.im.pojo.Message;
  import cn.itcast.haoke.im.Service.MessageService;
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
  package cn.itcast.haoke.im.Service;
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

