# 29.整合前端系统实现微聊功能之发送消息

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\29.整合前端系统实现微聊功能之发送消息【海量资源尽在 ubkz.com】.mp4
- 时长 9分3秒（音频 543s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们来看一下这个发送消息和接收消息的一个前端整合的一个这个逻辑啊那么我们还是去进入我们这个window啊这个页面在这个window这个解释中呢我们可以看到它呢有一个叫做send message的一个方法因为我们去点击这个发送的时候呢它会调用这个方法所以我们需要去重新去修改一下这个方法的一些逻辑啊那我们来看一下这个里面的逻辑是怎么样去
[00:28] 写着呢这样我们还是把这个代码呢贴过来我们把这个把这个吧就给他拿掉吧然后我们拷贝到这然后呢下面呢没拷完哈然后呢到这一直拷贝到这里来在这好嘞那么这个代码就拷好了那么这个逻辑是什么一个逻辑我们简单的来说一下就是当我们去发送消息的时候呢他呢去
[00:54] 会拿到我们那个station的一个client然后呢去做一个emit的一个invert去做一个弹出弹出我们的一个这个那个事件然后呢把我们的这个数据去做一个json的一个序列化然后呢去做一个发送这个呢它在内部呢还做了一个数据的一个包装啊一会儿我们再说这样的话呢我们就按照我们所需要的一个格式什么to id发给谁然后呢message是什么内容是不是按照这样的一个结构去做一个
[01:21] 数据的发送因为发送的阶层就按照我们刚刚所测试的这样的一个消息的结构去做一个消息的发送ok那么这个就是一个发送那么接着继续往下面看那么下面我们要去修改一个im的client的解释因为在这个里面它去对我们发送的一个消息发送的一个消息来看一下在还在下面
[01:50] 我们来搜一下吧现在就是在发送这个消息这个在这那么他对我们发送的这个消息会做一个包装会做个包装那么其实呢我们这个消息是没有必要包装的直接去发送他就可以了所以呢我们在这个位置把这个逻辑给他住掉然后呢我们直接就干嘛呢直接给他去做一个发送就可以了我们不做一个这个包装直接做发送调用我们这个socket调用我们这个socket去做一个这个发送就OK
[02:19] 好那么这个呢就是这样的一个逻辑不做一个包装了直接做发送就可以了这个呢就是我们的一个发送的一个情况那我们来看一下他是否能够去把这个消息发送成功呢我们来看一下那么现在呢我们就模拟我们的用户这个1001这个用户是不是去登录然后呢我们去给他发送个消息发送给1002就是李四啊这个用户那我们来看一下他有没有去建立这个WS这个连接呢
[02:48] 有没有建立我们可以看到是不是已经建立这个连接了但是有问题现在我们还没有去给他修改一个修改他的一个地址没有去修改一个地址那么我们需要修改一下WebSocket的地址他是在下面的有一个叫做common下面这个地址显然是不对的地址对吧所以我们需要给他去修改一下按照我们格式去做一个修改把它拷过来
[03:18] 那么需要注意的是在这个位置在这个位置我们不能把它写死所以我们就把它拿掉就到这就可以了然后在我们用户去创建连接的时候把这个用户ID再给它丢过去那么在哪个位置去创建用户连接我们来看一下我们这个逻辑是在我们的这个里面在这在我们这个页面加载完之后去做这样的一个Handle看一下这个Handle
[03:47] 在这个里面的去做一个连接啊去做一个连接所以在这个位置呢我们其实是有必要去拿到他的一个设置他的一个请求这个地址的啊那么在这个位置呢我们需要去把这个URL呢给他去重新去添加一个这个ID啊那个这个ID是哪来的呢我们来看一下那么在这个下面是不是我们去叫我们这个Hunter啊然后呢把这个ID给他传过去但是呢
[04:15] 我们不能这么去传不能去传递我们的local story下面的 id那么我们把代码我们调整一下代码有点问题那么调整一下把它注释一下然后它其实传递其实就是我们from这个user把它传过去把它传过去然后我们叫这个hander拿到 current user然后去在下面去做一个拼接斜杠去加一个它就改成我们的
[04:44] 自己的一个这个连接了对吧来看一下那我们来刷新一下看一下这个效果那么把它把它清掉把它清掉之后呢我们去点击这个理事走那么现在呢我们建立了一个连接可以看到请求地址是不是就是1270.0.1下面的18081那么我们这个断点就来了然后呢我们就通过吧把这个断点全部都放行我们就不去查看它了走OK
[05:11] 好那么这样的话呢我们已经就建立了一个连接啊建立了一个连接那么下面呢我们来看一下他的一个发送消息那么我现在是不是向李四发消息就是说没事随便聊聊那么随便写下什么呢比如说hello然后呢我们发消息走那么他所发送的一个消息我们可以看到这个send有点问题不能去做一个发送这个逻辑呢还是有一点问题的就是
[05:42] 刚刚我们可以看到在我们这个位置发送消息的时候send这个message的时候我们去调用我们的emit这个invent然后它其实会调用我们下面的发送的一个方法那么这个方法其实我们也是不需要它去包装了然后我们直接把这个date去做一个发送我们再来测试一下直接去发送这个date它会调用我们这个
[06:10] 这个里面的方法去做一个发送OK好那么这样的话他就应该去应该去能够去做一个发送了我们来测试一下发行走然后呢我们把这个清掉然后我们点击李四去建立一个连接然后呢通过好那么现在呢这个连接呢他就建立好了但是呢我们还发现有个小问题就是当他建立连接的时候呢他会向服务端发送一个消息
[06:38] 这个消息其实我们现在没有必要发送了那么我们把这个逻辑给他调一下是在这个位置啊是在他呃这个里面呢有一个叫做注册身份就是当我们的这个呃当我们去去连接到的时候呢需要去注册一个这样一个身份啊其实是我们没有必要去做这样一个注册的那么我们把这个把这个逻辑啊就给他先给他啊先给他这个注了吧就不需要去添加这个的注册身份了
[07:08] 把这个住掉好那么再来刷新看一下效果走刷新一下那我们来点击这个李四走那么现在呢我们来看一下有没有建立连接呢有哎你看这个时候他是不是就没有去发消息了对吧然后那么写一个哈喽点击发送走那么OK是不是现在我们是不是可以看到这个消息是不是已经发送到我们的服务端了那么现在消息有没有去
[07:41] 我们有没有保存起来呢来看一下哎看到了是不是这个hello啊这个消息是不是已经有了那么现在呢我们有没有把消息推送到我们的1002这个用户呢来看一下那么在这个链接下面是不是就属于1002他是不是也拿到哎我看一下能不能拿到呢呃拿到这个好像并没有拿到消息因为呢呃我哦这个呢是这样的一个问题啊
[08:07] 原因是我们刚刚是不是重启了我们的一个Tomcat服务器对吧那么我们这个并没有重新的去刷新一下重新连接一下这个会有点问题的点击开启我们再来测试一下那么hello我再发一个hello周他又发送了一个hello那么数据肯定有现在就会有两个hello你看一个两个对吧然后在前面这个里面拿到消息了吗心上拿到了消息内容就是hello这个大家应该还记得前面我们是不是把这个服务重启了一下对吧重启了一下
[08:37] 它就连接其实就断开了所以它就拿不到这个消息了OK好那么到这里我们其实就完成了一个是发送的逻辑刚刚我们去修改代码还是比较多的然后大家也可以去拿到我修改之后的代码去做一个测试就可以了OK这个就是一个发送消息的一个逻辑好那么我们先把这个视频也先暂停一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 WebSocket 的即时通讯（IM）前端聊天功能的实现，包括消息发送、客户端事件处理和网络调试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中“5.3、发送消息”章节，代码片段为 chat-window.js 中的 sendMsg 函数，定义了消息数据结构 pdata。
画面 2: 在 IntelliJ IDEA 中展示 chat-window.js 文件，高亮显示 sendMsg 函数中将 pdata 数据通过 this.state.client.emitEvent 发送。
画面 3: 同画面 2，代码中高亮显示了 this.setState 更新消息列表和发送事件的逻辑。
画面 4: 在 IntelliJ IDEA 中展示 IMClient.js 文件，代码中定义了消息处理函数 dispatchMessage 和 dispatchDataPacket。
画面 5: 在 IntelliJ IDEA 中展示 IMClient.js 文件，代码中定义了 sendDataPacket 函数，用于向服务器发送数据包。
画面 6: 在浏览器中展示聊天界面，用户“lisi”与“lisi”对话，同时在 Advanced Rest Client 中显示了 WebSocket 连接成功。
画面 7: 在 IntelliJ IDEA 中展示 chat-window.js 文件，代码中高亮显示了更新状态和发送事件的逻辑。
画面 8: 在浏览器中展示聊天界面，显示联系人列表，包括“zhangsan”、“li”、“wangwu”、“zhao”、“lumpi”。
画面 9: 在 IntelliJ IDEA 中展示 wsmain.js 文件，代码中定义了客户端事件监听器，用于处理消息发送、接收和用户注册。
画面 10: 在浏览器中展示聊天界面，联系人列表中“lumpi”旁边显示加载中状态。
画面 11: 在 IntelliJ IDEA 中展示 wsmain.js 文件，代码中定义了客户端事件监听器，用于处理消息发送、接收和用户注册。
画面 12: 在浏览器中展示聊天界面，用户“lisi”发送了“hello”消息，同时在 Advanced Rest Client 中显示了发送的 JSON 数据。
画面 13: 在浏览器中展示 WEBSOCKET 在线测试工具页面，显示了发送和接收的消息记录。
画面 14: 展示 PDF 文档中“5.3、发送消息”章节，代码片段为 chat-window.js 中的 sendMsg 函数，定义了消息数据结构 pdata。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```javascript
sendMsg = () => {
  let {to_user,from_user,avatar} = this.props.chatInfo;
  let pdata = {
    id: this.guid(),
    // from_user: from_user,
    // to_user: to_user,
    from: {
      id:this.state.fromId
    },
  };
```

画面 2:
```javascript
sendMsg = () => {
  let {to_user,from_user,avatar} = this.props.chatInfo;
  let pdata = {
    id: this.guid(),
    from_user: from_user,
    to_user: to_user,
    avatar: avatar,
    chat_msg: this.state.msgContent
  };
  let newList = [...this.state.infos];
  newList.push(pdata);
  this.setState({
    infos: newList
  });
  this.state.client.emitEvent(IMEvent.MSG_TEXT_SEND,JSON.stringify(pdata));
```

画面 3:
```javascript
// from user: from_user,
// toId: to_user,
// from: {
//   id:this.state.fromId
// },
// avatar: avatar,
// msg: this.state.msgContent
let newList = [...this.state.infos];
newList.push(pdata);
this.setState({
  infos: newList
});
this.state.client.emitEvent(IMEvent.MSG_TEXT_SEND,JSON.stringify(pdata));
```

画面 4:
```javascript
let handlers = this._handlers[type];
for (var i = handlers.length - 1; i >= 0; i--) {
  if (handler === handlers[i]) {
    handlers.splice(i, 1);
  }
}

/**
 * 消息封装成数据包
 */
dispatchMessage(message) {
  let dataPacket = new DataPacket(message);
  if (dataPacket.data) {
    this.dispatchDataPacket(dataPacket);
  }
}

/**
 * 处理数据包
 */
dispatchDataPacket(dataPacket) {
```

画面 5:
```javascript
setTimeout(() => {
  this.connect();
}, 5000);

// 向服务器发送数据包
sendDataPacket(dataPacket) {
  if (this._isOpened) {
    this.socket.send(dataPacket.rawMessage);
    // else {
    //   this.DataPacketQueue.push(dataPacket);
    // }
  }
}

/**
 * 事件处理
 */
// 当连接服务器时处理
serverOnConnected() {
  this._isOpened = true;
```

画面 6:
```json
{
  "id": "1544241086774524",
  "from": "lisi",
  "to": "lisi",
  "msg": "你好",
  "time": "1544241086774",
  "type": "text"
}
```

画面 7:
```javascript
// from user: from_user,
// toId: to_user,
// from: {
//   id:this.state.fromId
// },
// avatar: avatar,
// msg: this.state.msgContent
let newList = [...this.state.infos];
newList.push(pdata);
this.setState({
  infos: newList
});
this.state.client.emitEvent(IMEvent.MSG_TEXT_SEND,JSON.stringify(pdata));
```

画面 8:
无代码。

画面 9:
```javascript
import ...
const handle = (currentUser, handleMsg) => {
  const client = new IMClient(config.wsBaseUrl + "/" + currentUser);
  // 发送消息
  client.addEventListener(IMEvent.MSG_TEXT_SEND, data => {
    let dataPacket = new DataPacket({
      type: IMEvent.MSG_TEXT_SEND,
      content: data
    });
    client.sendDataPacket(dataPacket)
  });
  // 接收消息
  client.addEventListener(IMEvent.MSG_TEXT_REC, data => {
    handleMsg(data)
  });
  // 注册身份
  client.addEventListener(IMEvent.CONNECTED, () => {
    let dataPacket = new DataPacket({
      type: IMEvent.USER_REG,
      content: currentUser
    });
    client.sendDataPacket(dataPacket)
  });
```

画面 10:
无代码。

画面 11:
```javascript
import ...
const handle = (currentUser, handleMsg) => {
  const client = new IMClient(config.wsBaseUrl + "/" + currentUser);
  // 发送消息
  client.addEventListener(IMEvent.MSG_TEXT_SEND, data => {
    let dataPacket = new DataPacket({
      type: IMEvent.MSG_TEXT_SEND,
      content: data
    });
    client.sendDataPacket(dataPacket)
  });
  // 接收消息
  client.addEventListener(IMEvent.MSG_TEXT_REC, data => {
    handleMsg(data)
  });
  // 注册身份
  client.addEventListener(IMEvent.CONNECTED, () => {
    let dataPacket = new DataPacket({
      type: IMEvent.USER_REG,
      content: currentUser
    });
    client.sendDataPacket(dataPacket)
  });
```

画面 12:
```json
{
  "id": "1544241086774524",
  "from": "lisi",
  "to": "lisi",
  "msg": "hello",
  "time": "1544241086774",
  "type": "text"
}
```

画面 13:
```json
{
  "id": "1544241086774524",
  "from": "lisi",
  "to": "lisi",
  "msg": "hello",
  "time": "1544241086774",
  "type": "text"
}
```

画面 14:
```javascript
sendMsg = () => {
  let {to_user,from_user,avatar} = this.props.chatInfo;
  let pdata = {
    id: this.guid(),
    // from_user: from_user,
    // to_user: to_user,
    from: {
      id:this.state.fromId
    },
  };
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

