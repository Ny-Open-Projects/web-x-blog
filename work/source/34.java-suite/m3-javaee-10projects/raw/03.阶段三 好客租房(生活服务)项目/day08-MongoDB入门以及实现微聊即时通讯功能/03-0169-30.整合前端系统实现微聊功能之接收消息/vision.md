# 画面线理解：30.整合前端系统实现微聊功能之接收消息

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\30.整合前端系统实现微聊功能之接收消息【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:13, 00:29, 01:01, 01:12, 01:36, 01:55, 02:34, 02:52, 03:49, 03:59, 04:42, 05:16, 05:31, 05:41
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:53:33

1) 这一组画面整体在讲什么（一句话）：
演示基于 WebSocket 的即时通讯（IM）功能实现，包括客户端与服务端的连接、消息收发、以及分布式架构的解决方案。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 WebSocket 在线调试工具界面，服务端地址为 ws://127.0.0.1:8081/ws/1002，已连接成功，可发送测试消息。
画面 2: 展示 PDF 文档内容，其中包含 JavaScript 代码片段，用于处理用户消息并更新状态。
画面 3: 在 IntelliJ IDEA 中展示 `wsmain.js` 文件，代码中定义了 `handle` 函数，用于创建客户端并监听消息发送和接收事件。
画面 4: 在 PDF 文档中展示 `onlyMessage` 类的 `connect` 方法，用于建立 WebSocket 连接并绑定消息事件。
画面 5: 在 PDF 文档中展示 `connect` 方法的完整代码，包括 `onmessage`、`onopen` 和 `onclose` 事件的处理。
画面 6: 在 PDF 文档中展示 `IMClient.js` 文件的构造函数，用于初始化 WebSocket 客户端。
画面 7: 在 IntelliJ IDEA 中展示 `chat.js` 文件，代码中使用 Axios 发送消息，并通过 `handle` 函数处理服务器返回的数据。
画面 8: 展示本地开发服务器的聊天界面，左侧为用户列表，右侧为聊天窗口，同时显示了浏览器的 Network 面板。
画面 9: 在 PDF 文档中展示 `connect` 方法的代码，其中包含 `onmessage` 事件的处理逻辑。
画面 10: 在 PDF 文档中展示 `handle` 函数的代码，用于处理接收到的消息并更新状态。
画面 11: 展示 WebSocket 调试工具界面，发送了包含文本消息的 JSON 数据，成功接收并显示。
画面 12: 展示本地聊天应用界面，用户“lisi”与“李四”进行对话，同时显示了浏览器的 Network 面板。
画面 13: 展示本地聊天应用界面，用户“lisi”与“李四”继续对话，同时显示了浏览器的 Network 面板。
画面 14: 在 PDF 文档中展示“分布式 Socket 解决方案分析”，指出 Session 对象集中存储的问题，并提出采用分布式消息系统解决。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```javascript
import ...
const handle - (currentUser, handleMsg) -> {
    const client - new IMClient(config.wsBaseUrl + "/" + currentUser, handleMsg);
    // 发送消息
    client.addEventListerner(IMEvent.MSG_TEXT_SEND, data -> {
        let dataPacket = new DataPacket({
            type: IMEvent.MSG_TEXT_SEND,
            content: data
        })
        client.sendDataPacket(data)
    })
    // 接收消息
    client.addEventListerListener(IMEvent.MSG_TEXT_REC, data -> {
        handleMsg(data)
    })
    // 注册身份
    client.addEventListerListener(IMEvent.CONNECTED, () -> {
        let dataPacket = new DataPacket({
            type: IMEvent.USER_REG,
            content: currentUser
        })
        client.sendDataPacket(dataPacket)
    })
}
```

画面 4:
```javascript
this.onMyMessage - onlyMessage: {
    this.addEventListerener(IMEvent.CONNECTED, () => {
        this.serverOnConnected();
    })
    // this.addEventListerener(IMEvent.CONNECTED, () => {
    //     this.clearMsgQueue();
    // })
    this.addEventListerener(IMEvent.DISCONNECTED, () => {
        this.serverOnDisconnected();
    })
}
```

画面 5:
```javascript
connect() {
    if (!this._socket) {
        this._socket = new WebSocket(this._url);
        this._socket.onmessage = (evt) => {
            this.onMessage(evt.data);
            if (this.onMyMessage) {
                this.onMyMessage(evt.data);
            }
        }
        this._socket.onopen = (ws) => {
            this.onOpen(ws);
        }
        this._socket.onclose = ws => {
            this.onClose(ws);
        }
    }
}
```

画面 6:
```javascript
修改wsmain.js文件：
const client = new IMClient(config.wsBaseUrl + "/" + currentUser, handleMsg);

修改IMClient.js文件：
constructor(url, onlyMessage) {
    this._url = url;
    this._autoConnect = true;
    this._handlers = {};
    this._DataPacketQueue = [];
    this._isOpened = false;
    this._onlyMessage = onlyMessage;
    this.addEventListerener(IMEvent.CONNECTED, () => {
        this.serverOnConnected();
    })
    // this.addEventListerener(IMEvent.CONNECTED, () => {
    //     this.clearMsgQueue();
    // })
    this.addEventListerener(IMEvent.DISCONNECTED, () => {
        this.serverOnDisconnected();
    })
}
```

画面 7:
```javascript
let (to_user, from_user) = this.props.chatInfo;
axios.get('http://127.0.0.1:8081/message', {params: {
    toId: to_user,
    fromId: from_user
}}).then(data => {
    this.setState({
        infos: data,
        isLoading: true,
        fromId: from_user,
        client: handle(from_user, (data) => {
            let newList = [...this.state.infos];
            newList.push(JSON.parse(data.content));
            this.setState({
                infos: newList
            })
        })
    });
});
```

画面 10:
```javascript
fromId: from_user
}).then(data => {
    this.setState({
        infos: data,
        isLoading: true,
        fromId: from_user,
        client: handle(from_user, (data) => {
            let newList = [...this.state.infos];
            newList.push(JSON.parse(data.content));
            this.setState({
                infos: newList
            })
        })
    });
});
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 14:
标题: 6、分布式Socket解决方案分析
问题: 前面的实现中，将Session对象放到全局的Map中，当连接变得非常多时，这将成为系统瓶颈，因为不能进行分布式部署。
解决方案: 采用分布式消息系统进行解决。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
