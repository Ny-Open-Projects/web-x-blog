# 06.ReactJS入门之mock数据

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day02-Ant Design以及Ant Design Pro入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day02-Ant Design以及Ant Design Pro入门\06.ReactJS入门之mock数据【海量资源尽在 ubkz.com】.mp4
- 时长 7分21秒（音频 442s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来我们来看一下数据的这个Mock那么Mock的意思呢其实就是在做模拟由于呢我们现在的这种开发模式啊就是在做前后端的分离那么大概呢它就是这样的一个意思啊就是说当我们的前端啊这个是我们的前端这个团队那么这个是我们的后端啊这个团队那么前端和后端呢我们是分离开发的
[00:29] 那么前端系统他是不是要去请求我们后台系统是不是去拿数据啊但是呢在我们开发的过程中啊你后台系统并没有把这个接口是不是写好对吧也就是说你不能够返回数据啊这个数据你返回不了对吧因为你还没有写好这个功能嘛那么前端系统是不是就因为说你没有返回这个数据那么我这个前端这个事情是不是就不做了那么我功能是不是就不开发了呢
[00:57] 其实并不是那么在前台系统呢他呢可以做什么呢可以自己做一个模拟哎我模拟去生成这样的一个数据对不对那么我去模拟其实就是一个Mock这个操作啊做一个模拟那么我基于我这个模拟的一个情况下我去开发我的功能那么等到我所有的功能都开发完成了对吧然后呢后台系统呢是不是也开发完成了那么这个时候呢我们再去调用你真正的这个地址
[01:25] 对吧然后再去拿这个数据那么这样的话是不是我们就是你前端这个团队和我们后端这个团队相互之间没有影响啊OK所以呢我们这个Mock他也是比较重要的啊但是比较好的一点呢是在Uni啊这个框架中呢他对这个Mock呢做了非常好的一个支持那么我们就可以很轻松的能够实现啊这个Mock这个操作
[01:53] 那么这个需要怎么做呢我们这样来做啊那么我们首先呢在我们项目的根目录中啊创建一个Mock啊这样的一个目录这个就是我们项目的根目录创建一个Mock这个目录然后呢在这个下面呢我们创建一些这个JS文件那么这个下面JS文件呢都是我们去做一些模拟生成数据的一些JS文件那么我们把这个数据这个拷过来来看一下那么显然我们可以看到
[02:25] 在这个里面的定义了asport去导出导出一个谁呢这样的一个数据那么这个对象啊然后呢我们模拟一个什么get请求get什么请求呢根目录下面的ds下面的一个list这样的一个请求这个请求地址注意这个请求地址是不是刚好就是我们刚刚所写的这个请求地址啊ok那么我们发起的是一个什么请求呢来看一下刚才我们可以看到他发起的其实是一个
[02:53] 是不是一个get请求是不是你看在这是不是get请求OK好那么这是一个get请求那么我们在这个mark下面我们去做模拟的时候是不是也是模拟get请求那么当我们去请求这个地址的时候那么我给它返回一个数据通过一个res其实有response的意思那么通过它点json返回一个json数据那么返回对象对象中包含了一个date和一个max number
[03:22] 那么我们为了区分原来的一个数据我们给它初始的四个值对吧最大就是4那么这样的话我们就知道这个数据是我们模拟得来的一个数据好那么这样的话我们就可以去完成这个模拟的一个动作那么我们来刷新页面看一下效果有没有请求到我们的数据走你看他有请求到数据吗是不是依然是没有的对吧那么为什么会这样呢原因是我们没有去重启这个服务我们需要把这个服务重启一下
[03:52] 然后呢Ctrl CCtrl C然后呢我们再来启动一下看一下效果啊等待它的启动稍微有一点点慢啊等待它的启动那么启动完成之后呢我们到这个里面来看一下这个效果啊那么我们刷一下啊刷一下它呢已经是启动了对吧那么我们来看一下它有没有请求我们的数据呢哎你发现它是不是已经请求会数据了对不对但是呢我们现在好像是
[04:30] 有点报错啊报错什么意思呢我们来看一下他说不能够读取我们这个属性啊这个map那么可能是我们拿这个值呢还是有点问题我们来排查一下好那么我们来看一下刚刚呢我们去排查了一下这个问题啊是什么意思呢就是说这个错误呢是指我们呢在我们做这个页面渲染的时候啊他呢其实是拿不到我们这个map的啊
[04:59] 就是说我们这个拿了个值呢它是有点问题的那么这个问题在哪里呢是我们在刚刚在写这个模型的时候啊出了点问题那么来看一下那么当我们去做这个初始化这个操作的时候啊那么我们是不是去请求到数据之后我们会调用我们的put然后呢去调用我们这个按的new date的这个方法
[05:21] 那么要注意的是那么刚刚写这个位置呢有点有点问题啊那么这个位置呢他不应该拿到state这个去做一个处理因为你state就是原来这个数据对不对不能拿到它那么所以呢这个里面的我们其实还有一个参数叫什么呢result就是你的结果数据就是说我们去传递到我们的调用我们这个方法那么在这个里面呢我们会把这个参数呢
[05:47] 传递到这个位置一个result我们通过这个result去获取它的一个data这才是什么呢才是我们的一个结果数据啊咱们在这去说明一下result代表的是我们请求到的这个数据啊这个代表的是我们请求到的数据然后呢我们再去刷新一下看效果其实我们可以发现这个效果是不是已经就ok了那么我们可以在这个mock里面呢我们再来给它添加一个数据比如说再来一个解读5啊再来一个
[06:18] 然后呢这个我们给它写成5然后呢我们刷新一下你看数据是不是就变成5了那么点击变成678910那么这样的话我们是不是就成功的去模拟了什么模拟了我们的服务端返回这个数据那么等到以后呢我们的服务端真正的把这个服务的接口开发好之后呢我们是不是直接对接
[06:43] 就可以了哎OK当然了我们是不是前后端分离的时候就需要前端这个团队跟我们后端团队把这个数据结构是比较约定好哎OK好那么这样的话我们就啊已经实现了这样的一个效果啊所以我们可以看到在这个UMI这个框架中啊他呢已经是将这个Mock是不是已经就做了很好的一个支持啊所以我们可以很好的去实现这样的效果啊好那么关于这个Mock的这个呃
[07:12] 知识的讲解我们就讲到这里那么在后面我们开发过程中这个Mock我们也会用的比较多好那么我们就先讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 mock 数据模拟 API 请求以解决开发中没有真实后端服务的问题。

2) 按时间顺序列出每张画面的要点：
画面1: 在 Typora 中查看课程笔记，内容为“1.1.4. mock数据”，并展示如何在项目中创建 MockListData.js 文件并输入模拟数据。
画面2: 在 IntelliJ IDEA 中打开 MockListData.js 文件，展示其中的模拟数据代码。
画面3: 在 IntelliJ IDEA 中，光标位于 MockListData.js 文件的 res.json() 函数内，展示模拟数据。
画面4: 在 IntelliJ IDEA 中，光标位于 MockListData.js 文件的 res.json() 函数内，展示模拟数据。
画面5: 在 IntelliJ IDEA 中，光标位于 MockListData.js 文件的 res.json() 函数内，展示模拟数据。
画面6: 在 IntelliJ IDEA 的终端中，显示 webpack 编译成功，提示“Compiled successfully in 594ms”。
画面7: 在浏览器中，显示一个 TypeError 错误：“Cannot read property 'map' of undefined”，并展示网络请求返回的数据。
画面8: 在 IntelliJ IDEA 中，光标位于 MockListData.js 文件的 res.json() 函数内，展示模拟数据。
画面9: 在 IntelliJ IDEA 中，光标位于 MockListData.js 文件的 res.json() 函数内，展示模拟数据。
画面10: 在 IntelliJ IDEA 中，光标位于 MockListData.js 文件的 res.json() 函数内，展示模拟数据。
画面11: 在浏览器中，显示一个空的列表页面，网络请求成功返回数据。
画面12: 在 IntelliJ IDEA 中，光标位于 MockListData.js 文件的 res.json() 函数内，展示模拟数据。
画面13: 在 Typora 中查看课程笔记，内容为“1.1.4. mock数据”，并展示如何在项目中创建 MockListData.js 文件并输入模拟数据。
画面14: 在 Typora 中查看课程笔记，内容为“1.1.4. mock数据”，并展示如何在项目中创建 MockListData.js 文件并输入模拟数据。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面1:
```javascript
export default {
  'get /ds/list': function (req, res) { //模拟请求返回数据
    res.json({
      data: [1, 2, 3, 4],
      maxNum: 4
    });
  }
};
```

画面2:
```javascript
let maxNum = state.maxNum + 1;
let newArr = [...state.data, maxNum];

return {
  data: newArr,
  maxNum: maxNum
};

//通过return 返回更新后的数据

effects: { //新增effects配置，用于异步加载数据
  initData(params, sagaEffects) { //定义异步方法
    const [call, put] = sagaEffects; //获取到call.put方法
    const url = "/ds/list"; //定义请求的url
    let data = yield call(request, url); //执行请求
    yield put({ //调用reducers中的方法
      type: "addNewData",
      data: data //传递ajax回来的数据
    });
  }
};
```

画面3:
```javascript
export default {
  'get /ds/list': function (req, res) { //模拟请求返回数据
    res.json({
      data: [1, 2, 3, 4],
      maxNum: 4
    });
  }
};
```

画面4:
```javascript
let maxNum = state.maxNum + 1;
let newArr = [...state.data, maxNum];

return {
  data: newArr,
  maxNum: maxNum
};

//通过return 返回更新后的数据

effects: { //新增effects配置，用于异步加载数据
  initData(params, sagaEffects) { //定义异步方法
    const [call, put] = sagaEffects; //获取到call.put方法
    const url = "/ds/list"; //定义请求的url
    let data = yield call(request, url); //执行请求
    yield put({ //调用reducers中的方法
      type: "addNewData",
      data: data //传递ajax回来的数据
    });
  }
};
```

画面5:
```javascript
export default {
  'get /ds/list': function (req, res) { //模拟请求返回数据
    res.json({
      data: [1, 2, 3, 4],
      maxNum: 4
    });
  }
};
```

画面6:
```
* webpack after omitting (968)
Y success webpack compiled in 594ms
```

画面7:
```
TypeError: Cannot read property 'map' of undefined
```

画面8:
```javascript
let maxNum = state.maxNum + 1;
let newArr = [...state.data, maxNum];

return {
  data: newArr,
  maxNum: maxNum
};

//通过return 返回更新后的数据

effects: { //新增effects配置，用于异步加载数据
  initData(params, sagaEffects) { //定义异步方法
    const [call, put] = sagaEffects; //获取到call.put方法
    const url = "/ds/list"; //定义请求的url
    let data = yield call(request, url); //执行请求
    yield put({ //调用reducers中的方法
      type: "addNewData",
      data: data //传递ajax回来的数据
    });
  }
};
```

画面9:
```javascript
let maxNum = state.maxNum + 1;
let newArr = [...state.data, maxNum];

return {
  data: newArr,
  maxNum: maxNum
};

//通过return 返回更新后的数据

effects: { //新增effects配置，用于异步加载数据
  initData(params, sagaEffects) { //定义异步方法
    const [call, put] = sagaEffects; //获取到call.put方法
    const url = "/ds/list"; //定义请求的url
    let data = yield call(request, url); //执行请求
    yield put({ //调用reducers中的方法
      type: "addNewData",
      data: data //传递ajax回来的数据
    });
  }
};
```

画面10:
```javascript
let maxNum = state.maxNum + 1;
let newArr = [...state.data, maxNum];

return {
  data: newArr,
  maxNum: maxNum
};

//通过return 返回更新后的数据

effects: { //新增effects配置，用于异步加载数据
  initData(params, sagaEffects) { //定义异步方法
    const [call, put] = sagaEffects; //获取到call.put方法
    const url = "/ds/list"; //定义请求的url
    let data = yield call(request, url); //执行请求
    yield put({ //调用reducers中的方法
      type: "addNewData",
      data: data //传递ajax回来的数据
    });
  }
};
```

画面11:
```
1
2
3
4
```

画面12:
```javascript
export default {
  'get /ds/list': function (req, res) { //模拟请求返回数据
    res.json({
      data: [1, 2, 3, 4],
      maxNum: 4
    });
  }
};
```

画面13:
```javascript
export default {
  'get /ds/list': function (req, res) { //模拟请求返回数据
    res.json({
      data: [1, 2, 3, 4],
      maxNum: 4
    });
  }
};
```

画面14:
```javascript
export default {
  'get /ds/list': function (req, res) { //模拟请求返回数据
    res.json({
      data: [1, 2, 3, 4],
      maxNum: 4
    });
  }
};
```

4) PPT 标题、架构图/流程图的结构、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

