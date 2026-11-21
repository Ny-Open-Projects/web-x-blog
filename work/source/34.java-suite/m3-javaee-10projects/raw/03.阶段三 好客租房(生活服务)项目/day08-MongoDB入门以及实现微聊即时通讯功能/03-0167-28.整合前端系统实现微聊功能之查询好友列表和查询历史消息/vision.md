# 画面线理解：28.整合前端系统实现微聊功能之查询好友列表和查询历史消息

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\28.整合前端系统实现微聊功能之查询好友列表和查询历史消息【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:32, 01:00, 01:24, 01:47, 02:12, 02:30, 02:57, 03:22, 03:47, 04:20, 04:53, 06:00, 06:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:52:05

1) 这一组画面整体在讲一个基于 React 和 Socket.IO 的聊天系统前端部分，包括好友列表查询、单聊界面构建和消息发送功能的实现。

2) 按时间顺序列出每张画面的要点：
画面1：展示 PDF 文档中“5.1、查询好友列表”章节，代码片段为 React 组件的 componentDidMount 方法，通过 axios 发送 GET 请求获取用户列表。
画面2：展示 IntelliJ IDEA 中 chat.js 文件，代码为 componentDidMount 方法，通过 axios 获取用户列表并更新状态。
画面3：展示 PDF 文档中“5.1、查询好友列表”章节，代码片段为 render 方法中根据 isLoading 状态渲染列表或加载中提示。
画面4：展示 IntelliJ IDEA 中 application.properties 文件，配置了 Spring Boot 应用名、Dubbo 注册中心地址、Redis 连接池参数等。
画面5：展示 PDF 文档中“5.2、好友单聊”章节，代码片段为 componentDidMount 方法，通过 axios 发送 GET 请求获取聊天信息。
画面6：展示 IntelliJ IDEA 中 chat-window.js 文件，代码为 React 组件的构造函数和 handleMsgChange 方法，用于初始化状态和处理消息输入。
画面7：展示 PDF 文档中“5.2、好友单聊”章节，代码片段为 componentDidMount 方法，通过 axios 获取聊天信息并更新状态，同时处理本地存储的 uid。
画面8：展示 EditPlus 编辑器中一个包含图片 URL 的文件，代码片段为 componentDidMount 方法，通过 axios 获取聊天信息并更新状态。
画面9：展示 IntelliJ IDEA 中 chat-window.js 文件，代码为 componentDidMount 方法，通过 axios 获取聊天信息并更新状态，同时处理本地存储的 uid。
画面10：展示 IntelliJ IDEA 中 chat-window.js 文件，代码为 render 方法，返回一个包含标题、内容列表和输入框的聊天窗口结构。
画面11：展示浏览器中一个卡通头像图片。
画面12：展示浏览器中聊天界面和开发者工具的 Network 面板，显示了发送消息的请求详情。
画面13：展示 IntelliJ IDEA 中 chat-window.js 文件，代码为 render 方法，根据当前用户和聊天对象的 id 设置不同的样式类名。
画面14：展示 PDF 文档中“5.3、发送消息”章节，代码片段为 sendMsg 方法，用于构造并发送消息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```javascript
componentDidMount () => {
  axios.get('http://127.0.0.1:18081/user?fromId=1001').then((data)=>{
    this.setState({
      list: data,
      isLoading: true
    })
  })
}
```
画面2：
```javascript
componentDidMount () => {
  axios.get('http://127.0.0.1:18081/user?fromId=1001').then((data)=>{
    this.setState({
      list: data,
      isLoading: true
    })
  })
}
```
画面3：
```javascript
if (isLoading) {
  return (
    <div key={item.id} onClick={(e) => this.toChat(e, item)}>
      <img src={item.avatar} alt="avatar"/>
      <span className="name">{item.username}</span>
      <span className="info">{item.chat_msg}</span>
      <span className="time">{item.ctime}</span>
    </div>
  )
}
```
画面4：
```properties
# Spring boot application
spring.application.name = itcast-haoke-manage-api-server
server.port = 10000
#logging.level.root=DEBUG

# dubbo应用名称
dubbo.application.name = dubbo-consumer-haoke-manage

# zk注册中心
dubbo.registry.address = zookeeper://172.16.55.185:2181
dubbo.registry.client = zkclient

# redis集群配置
spring.redis.jedis.pool.max-wait = 5000
spring.redis.jedis.pool.maxIdle = 100
spring.redis.jedis.pool.minIdle = 10
```
画面5：
```javascript
componentDidMount () => {
  let {to_user, from_user} = this.props.chatInfo;
  axios.get('http://127.0.0.1:18081/message', {params: {
    toId: to_user,
    fromId: from_user
  }}).then(data => {
    this.setState({
      infos: data,
      isLoading: true
    })
  })
}
```
画面6：
```javascript
class Chat extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      info: [],
      isLoading: false,
      magContent: ''
    };
  }
  guid() {
    function S4() {
      return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1);
    }
    return (S4() + S4() + "-" + S4() + "-" + S4() + "-" + S4() + "-" + S4() + S4());
  }
  handleMagChange (event) {
    this.setState({
      magContent: event.target.value
    });
  }
}
```
画面7：
```javascript
axios.get('http://127.0.0.1:18081/message', {params: {
  toId: to_user,
  fromId: from_user
}}).then(data => {
  let newList = [...this.state.infos];
  newList.push(JSON.parse(data.content));
  this.setState({
    infos: newList
  });
});
```
画面8：
```javascript
componentDidMount () => {
  let {to_user, from_user} = this.props.chatInfo;
  axios.get('http://127.0.0.1:18081/message', {params: {
    toId: to_user,
    fromId: from_user
  }}).then(data => {
    this.setState({
      infos: data,
      isLoading: true
    })
  })
}
```
画面9：
```javascript
componentDidMount () => {
  let {to_user, from_user} = this.props.chatInfo;
  axios.get('http://127.0.0.1:18081/message', {params: {
    toId: to_user,
    fromId: from_user
  }}).then(data => {
    this.setState({
      infos: data,
      isLoading: true
    })
  })
}
```
画面10：
```javascript
return (
  <div className="chat-window">
    <div className="chat-window-title">
      <Icon onClick={this.props.hideChat} name='angle left' className='chat-ret-btn' size='large'/>
      <span>{username}</span>
    </div>
    <div className="chat-window-content">
      <ul>{infolist}</ul>
    </div>
    <div className="chat-window-input">
      <Form>
        <TextArea value={this.state.msgContent} onChange={this.handleMsgChange} placeholder="请输入"/>
        <Button onClick={this.hideChat}>关闭</Button>
        <Button primary onClick={this.sendMsg}>发送</Button>
      </Form>
    </div>
  </div>
)
```
画面12：
```http
Request URL: http://127.0.0.1:18081/message?fromId=1000&toId=1001
Request Method: GET
Status Code: 200
Remote Address: 127.0.0.1:18081
Referer Policy: no-referrer-when-downgrade
```
画面13：
```javascript
key={item.id} className={currentUser === item.from.id ? 'chat-info-right' : 'chat-info-left'}
<img src="http://itcast-haoke.oss-cn-qingdao.aliyuncs.com/1544241062743524.jpg" alt=""/>
```
画面14：
```javascript
sendMsg () => {
  let {to_user, from_user, avatar} = this.props.chatInfo;
  let pdata = {
    id: this.guid(),
    from_user: from_user,
    to_user: to_user,
    from: {
      id: this.state.fromId
    }
  }
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1：PPT 标题为“5.1、查询好友列表”，下方有“黑马程序员”和“改变中国IT教育，我们正在行动”字样。
画面5：PPT 标题为“5.2、好友单聊”，下方有“黑马程序员”和“改变中国IT教育，我们正在行动”字样。
画面14：PPT 标题为“5.3、发送消息”，下方有“黑马程序员”和“改变中国IT教育，我们正在行动”字样。
画面4：无 PPT 标题，但展示了 application.properties 文件内容。
画面12：无 PPT 标题，但展示了浏览器开发者工具中的 Network 面板。

5) 不要评价画面美观，不要输出与课程无关的内容。
