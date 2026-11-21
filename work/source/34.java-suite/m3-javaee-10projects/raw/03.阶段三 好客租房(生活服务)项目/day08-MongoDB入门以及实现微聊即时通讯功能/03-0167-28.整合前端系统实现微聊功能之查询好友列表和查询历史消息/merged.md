# 28.整合前端系统实现微聊功能之查询好友列表和查询历史消息

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\28.整合前端系统实现微聊功能之查询好友列表和查询历史消息【海量资源尽在 ubkz.com】.mp4
- 时长 6分43秒（音频 404s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们就来整合我们的前端的去做一个功能的一个实现那么首先第一个呢我们先去改造它的一个查询好友的一个列表那么这个页面呢是在这个chat这个JS中啊我们来找一下在前端的这个页面中module找到这个下面啊有一个查询我们来看一下在这个下面呢它有一个查询用户的一个列表是在这个位置啊可以看一下是不是在这个位置然后呢我们把这个代码给它替换过来
[00:29] 就是在在这把它剔掉那么我们就是去通过我们的这个地址去做我们这样的一个查询我服务买地先设置为是1001去做这样的一个查询好嘞那么我们大家这个地址我们先暂时先这么写死先这么写死好那我们先去测试一下它的一个逻辑然后呢在我们下面的这个位置去做我们的这个数据渲染的时候呢可能也会有一点不同因为这图片是不一样的我们来看一下
[00:58] 这个头像的是不一样的所以我们把这个逻辑也拷过来就义父的这个判断这个逻辑拷过来一直到到这到这把它剃掉OK好这就是我们这个逻辑然后我们来看一下我们这个页面刷新一下这个页面那么其实可以看到这个位置这个还少一个那个横杠那么这个横杠我们把这个服务给它重启一下因为刚刚我们并没有重启把它重启一下
[01:27] 因为我们刚修改代码之后并没有重启啊OK那么等待他的一个重启好那么现在重启好了我们来测试一下刷新那么显然可以看到在这个位置是不是已经拿到对应的数据了哎OK好那么这个我们第一个逻辑是不是就搞定了那么下面我们来看他的第二个逻辑就是好友的一个登聊就是我们点击啊点击每一个这个好友的时候我们去进入他的一个这个页面啊那么我们来看一下他的一个逻辑呢是在这儿
[01:58] 下面呢我们当我们点击啊点击每一个这个好友的时候呢会去干嘛呢做一个去打开它下面的一个这个就是一个window啊一个window在这个位置有一个这个window啊那么其实对应的一个代码逻辑呢是在这个下面来看一下是在这个下面那么首先我们要去给它去修改的是它的这个就是页面加载完的一个这样的一个方法
[02:25] 那么来看一下是这个逻辑把这个逻辑要给它剃掉有的剃掉那么我们来看一下这个拷贝把它拷过来要注意代码的格式pdf拷贝不是特别好拷贝它有一个代码格式的问题那么这样我还是直接往这个里面去拷往我们这个idea里面去拷那么为了保险起见我先把这个先注掉
[02:52] 然后呢我再去做一个拷贝好那么这个就拷过来了拷过来之后呢我们继续往下面拷一直拷贝到拷贝到这然后呢这个呢是在他的下一行到这拷贝好那么这个方法就完整的拷贝过来了然后呢去发起get请求去拉取我们的一个消息拉取完之后呢去做这样的一个逻辑的一个处理
[03:20] 好那么在下面呢有一个我们的一个显示啊因为结构会发生一些变化那么显示呢也会有点变化就是在下面的这个判断这个位置啊我们来找到它的一个判断的这个位置在这把它呢也剔掉好这样的一个逻辑把这个呢也给它剔掉哎OK好嘞那么这个时候呢哎是不是有点有点格式上面的问题啊来看一下啊应该是回车的一些回车的换行的问题啊来看一下
[03:50] 那么在这个位置显然不能这么去写对吧然后这个也是也是这个格式的问题然后Cn这个地方扫一个横杠这个要注意一下好嘞那么现在我们基本上是不是已经把这个页面就整理好了来看一下是不是有一个横杠所以有个横杠的问题在这个里面有一个Cn横杠没问题
[04:20] 好那么现在的这个逻辑呢就搞定了那么下面我们就来测试一下测试点击单聊的一个效果我找到谁呢找到李四然后点击走那么是不是就把李四的这个所发的一个消息是不是就全部都拿出来了你好啊你也好啊等等等等是不是就有这样的一个这个消息但是好像没有我们去自己啊发出的这个这个消息啊这个可能会有点问题啊来看一下点击这个李四
[04:49] 那么他所发起的一个请求是做了一个是我看一下啊from 1001 to 1002没问题啊那么在这个里面呢返回的数据应该是有你好您也好然后呢我在学习这个那很好你好这个数据是有但是呢他这个显示的一个格式呢会有点问题啊就是我们在这个位置他有一个
[05:18] 小这个逻辑就是去做这样的一个判断如果我们去返回的这个这个ID如果是等于他的话就是我们当前这个用户ID然后等于我们返回这个ID的话就把它丢到这个右边去就是分我自己和对方或者好友这样的一个样式可能在这个位置这个ID会有点不一样我们来简单的来处理一下这个问题
[05:46] 好那么我们来看一下其实呢不是格式不是那个逻辑的问题是格式的问题啊还是我们这个横杠的问题啊来看一下那么他这个css我们这个chat横杠然后呢info杠还有杠啊我们之前把这个杠也丢掉了right放在右边然后呢这样的话他就ok了再测一下还是我们刚刚这个代码拷贝的一个格式的问题点一理事轴那么这样的话是不是就出现这样的一个效果了哎我发了一下消息你好你也好
[06:16] 我在学习这个很好你好在的有什么事没事随便聊聊我们一直是不是就是拿这个李四是不是做一个这样的一个测试就是这样的一个消息的结果那么OK到这里呢我们是不是就已经完成了他的一个好友的一个列表以及他的一个单聊这样的一个效果对吧那么接下来我们就要看发送消息了那么发送消息呢我们放到下一个视频来做一个讲解那么OK那么前面这两个功能的一个整合呢我们就先讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
dubbo.registry.address = ZooKeeper://172.16.55.185:2181
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

