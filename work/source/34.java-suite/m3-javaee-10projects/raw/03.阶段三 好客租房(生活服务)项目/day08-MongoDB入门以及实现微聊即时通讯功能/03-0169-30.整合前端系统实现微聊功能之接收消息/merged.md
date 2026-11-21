# 30.整合前端系统实现微聊功能之接收消息

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\30.整合前端系统实现微聊功能之接收消息【海量资源尽在 ubkz.com】.mp4
- 时长 5分42秒（音频 342s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么下面我们来看一下接收消息接收消息呢这个逻辑呢也需要去调一下跟之前逻辑呢会有点有点冲突所以我们需要去调一下什么叫接收消息呢就是假设呢我在这个位置我向1001去发消息我们来看这个位置能不能拿到消息就是这样的一个功能好,那么我们来看一下在我们这个逻辑中它需要处理的是
[00:26] 这个代码就是我们这个window中的这个代码我们已经处理过了那么其实我们要去调整的一个逻辑是在我们这个wsman这个节词中是在上有wsman这个节词中那么在这个里面我们可以看到当我们去调用这个new一个imclient的时候我们只传递了一个url那么这个时候其实我们需要的是把我们的这个叫handle message我们也给他传递过去
[00:54] 给他传递过去然后呢下面的这个我们就不需要了把这个也住掉就是接收消息这个逻辑就不需要了那么我们把这个给他传递过去之后呢我们就进入到我们这个im的client中我们在这个里面呢简单做一个逻辑的一个修改那么就是在按的这个我看一下啊在这个里面呢我们给他去添加一个叫做这个添加一个属性在这
[01:25] 就是类似点on一个message然后设置为一个on一个message然后我们下面去设置一个我们的一个方法我们看一下这个是对的然后我们去给他设置一个这个方法然后这个on my message是从这个方法去这个构造函数中传递过来的OK那么拿到一个他
[01:52] 那么拿到他之后这个其实就是前面我们的他传递过来的就是他传递到这个位置然后他到这然后又到这个位置来然后在下面注意下面的逻辑在这个逻辑里面我们有一个叫onMessage这个逻辑onMessage这个逻辑来看一下onMessage逻辑这个逻辑是不是就是当我们的客户端是不是去接触到消息的时候会执行这个代码执行这个逻辑
[02:20] 然后我们就在这个里面去判断如果我的on my message有的话那我就把这个消息拿到去调用这个方法就可以了调用这个方法其实就是我们传递过去这个方法而这个方法是谁其实就是我们刚刚的window里面的逻辑这个方法那么这个方法拿到数据之后就加到我们的states中那我们的states中发生了变化那我们的页面是不是就发生了变化了它就是这样的一个逻辑好那我们来测试一下
[02:48] 然后呢我们刷新走那么点击这个李四好嘞那么现在呢发了这么多消息那么李四呢现在给我回应一个消息啊那么发送消息的一个这个这个内容是吧就他啊那么我这个1002我要向1001去发一个消息那么哈喽那么我给他写一个什么呢我是李四看他能不能收到消息啊点击这个发送走
[03:17] 那么我们现在是不是已经发送了一个我是李四了对吧那我们在这个里面来看一下他这个位置会报错了报错是应该是我们的解释逻辑的稍微有点问题那么我们就来看一下这个里面的一些逻辑可能是我们在解析这个阶层有问题但是这个没关系我们先来看一下在这个里面我们有没有拿到消息可以看到是不是我已经拿到消息了只是我们在解释做解析的时候稍微有点问题这个我们看一下这个他的解析逻辑就OK了
[03:46] 消息已经是拿到了对吧那么我们就需要下面来看一下解析的代码是不是可能会跟我们之前的代码逻辑有点不一样的来看一下的确不一样因为我们拿到的数据其实直接就是Data对不对不需要再去拿到Data下面的Content了不需要它了直接去解析我们Data就可以了好我们再来刷新测试一下那么点击李四可以看到我是李四这个消息就来了
[04:16] 我再来给他发送个消息就是我是李四你是谁你是谁好那么我再来发一下消息走那么可以看到在这个里面是不是就拿到了你看是不是拿到消息了我是李四你是谁呢我给他再发一个消息我是怎么的张三你不记得了吗OK我点击发送走那么来看一下在这个里面是不是就收到了我是张三你不记得了吗我再给他发一下当然记得
[04:48] 老朋友大安记的老朋友了老朋友了然后呢走那么在这个里面就可以看到收到了大安记的老朋友了好那么其实这个实时通讯的其实这功能我们是基本上就搞定了对吧然后呢我们来看一下我们的数据有没有呢是不是也有你看我是李四你是谁啊张三大安记的等等所以说我们这个数据也都保存下来了那么其实我们可以到我们这个页面刷新一下
[05:19] 我在点击这个李四我就是不是就可以查询他的一个聊天记录ok所以可以看到这样是ok的没有问题好好嘞那么到这里我们这个是不是接收消息是不是也实现这样的一个效果了对吧ok好嘞

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

