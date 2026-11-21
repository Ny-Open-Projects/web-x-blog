# 画面线理解：29.整合前端系统实现微聊功能之发送消息

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\29.整合前端系统实现微聊功能之发送消息【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:34, 01:30, 01:49, 02:14, 02:47, 03:37, 04:50, 05:42, 06:18, 06:46, 07:40, 08:30, 09:00
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:52:54

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Websocket 的即时通讯（IM）前端聊天功能的实现，包括消息发送、客户端事件处理和网络调试。

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
