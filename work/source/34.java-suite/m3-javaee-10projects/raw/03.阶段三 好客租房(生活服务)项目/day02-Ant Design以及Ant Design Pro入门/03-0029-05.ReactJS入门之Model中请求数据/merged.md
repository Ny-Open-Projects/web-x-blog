# 05.ReactJS入门之Model中请求数据

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day02-Ant Design以及Ant Design Pro入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day02-Ant Design以及Ant Design Pro入门\05.ReactJS入门之Model中请求数据【海量资源尽在 ubkz.com】.mp4
- 时长 13分7秒（音频 787s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下在model这一层中呢我们如何去请求数据啊那么前面呢我们的数据啊是写死的就是说我们现在做到呢虽然是我们将我们这个页面啊就是我们pager这一层和我们model这一层呢做了分离但是呢我们会发现在我们model中的这个初始化的这个数据啊
[00:23] 它依然是我们写死在我们的model层的这显然是不合适的也不合理的那我们在我们实际开发的过程中那么更多的时候初始的数据都是通过我们的后台的这种服务去加载到的数据也就是我们的一个RX的一个一步加载那么在我model这一层我们又该如何去一步去加载数据呢
[00:50] 那我们接下来要做的事情呢就是这样的一个事情好那么首先呢我们需要在src下面创建一个目录叫做util啊所以这个呢是我们自己定义的一个目录叫util然后呢在下面呢我们写一个文件叫request.js所以这个文件呢我们就直接来做拷贝啊然后把这个内容我们拷过来那么我们也不用去呃管它里面内容了这个基本上我们就是
[01:20] 写死这样就可以了直接去调用就OK好那么我们就有了一个request.js那么通过它就可以去发送这个请求那么下面我们关注的是不是要关注这个model中怎么去写那么我们就需要在model中定义一个叫做effect这样的一个属性来定义它的一个相关的方法我们把这靠过来我们来讲解一下好来看一下
[01:49] 那么我们在我们的model中增加了一个effect这样的一个配置用于我们义务加载数据然后我们在下面定义了一个unit date这样的一个函数这样的一个函数那么这个函数注意前面是不是有一个信号
[02:05] 那么我们前面有这个信号的话那么就代表着我们是不是可以做这种异步的这种操作对吧好那么他的接受两个参数一个呢是叫Paramers就是我们的一些参数但是这个呢我们现在可能用不着先不管他先写的啊然后第二个参数叫做什么呢Saga然后呢Effects那么这个是什么意思呢这个是我们通过这个对象就可以拿到我们的需要去请求的一个
[02:32] 请求的一个函数啊所以呢我们通过它就可以拿到一个call和put通过这个call就可以做一个请求做一个请求那么这个时候呢要注意了我们去我们去使用这个call的时候啊那么我们需要在我们的这个model中呢去添加一个这个request你看我们是不是在定call的时候是不是要去使用一个request这个对象啊所以呢我们要把它呢先导入进来
[03:01] 这个request对象是不是就是我们刚刚所写的有tel下面的request.js就它把它导入进来就有了一个request对象那么下面我们就可以使用这个request对象然后进行call然后在我们的这call的前面我们定义了一个什么叫做yield它是不是就是我们所谓的做一步然后我们可以看到第二个参数就是url
[03:27] URL我们所定义它的是请求我们的数据的一个地址叫DS什么叫DS呢叫Data SourceDS下面的一个list那么这个地址现在我们显然肯定是不存在的是不是那么我们先就这样去请求一会我们来看一下它会怎么样当我们把这个定义完成之后它就可以拿到我们的一个数据叫Data数据
[03:51] 然后呢我们最后是不是需要把我们这个数据然后呢要更新到我们的state zone它才能够去更新我们的页面也就是说我们想要更新页面那么你最终其实要是更新的就是这个state的数据对不对所以呢我们需要在这个一步请求之后达到这个数据之后啊还要想办法去更新它那么怎么去更新它呢哎这样来更新我们要通过一个这个put这个操作注意
[04:20] 通过这个put的操作put的操作是干嘛的呢它可以去调用我们reduce中的函数它可以调用这个里面的函数那么我们这个里面的函数是不是就可以去更新我们的这个是this的数据所以呢它是这样的一个逻辑啊就是说我们可以通过这个put
[04:40] 然后去调用我们这个Reduce中的这样的一个函数然后通过Reduce这个函数就可以去更新了我们State最终就会导致我们这个页面的更新它是这样的一个逻辑好,我们来看一下它去调用什么我们的Reduce中的叫做UndernewDate这个方法指定这个方法名然后我们传递一个叫做Date然后一个Date
[05:08] 这后面这个data呢是我们去拿到的一个数据而前面这个data呢是我们的一个属性名啊属性名那么我们也就意味着说当我们这个请求成功之后啊他呢会调用我们这个方法对吧调用这个方法去完成一个初始化那么大家想一想那么之前我们所写的这个逻辑他是不是目的是为了做一个新增而我们现在呢想要他去完成一个初始化的一个操作所以在这个里面呢最开始我们
[05:37] 得有一个判断判断什么呢如果你传入的这个什么呢state中的这个有date这个值你看是不是你看是不是说我们去将这个数据这个date这个数据是不是要传递到我们这个方法中来所以我们要判断如果state中这个存在这个date这个数据
[06:02] 那么如果存在Date数据的话那么我们就给它做一个return是不是就可以了state.date做一个return好那么这个就代表着是不是如果如果这个state中state中存在什么呢存在这个Date数据那么就直接返回其实呢这个在做什么呢在做这个初始化的
[06:34] 操作在做这个操作那么我们来看一下前面的这个是不是就没有必要了对吧这个我们就不需要给它设置一个出水值了OK这个大家能够理解吗好那么现在呢我们是不是已经定义了一个一步的一个方法对吧那么关键点就问题来了那么这个方法什么时候调用呢好那么这样我们先来看一下这个页面的效果吧刷新一下来看一下你看现在报错报什么错呢是在我们页面中啊
[07:02] 他是不是需要拿到我们这个data list做一个map操作但是呢在我们当前的这个proposy中并没有data list这个属性所以呢他就报错了那么我们应该怎么做大家想一想现在我们是不是已经定义好了这样的一个异步的一个函数那么这个函数那么他在什么时候去调用呢这是一个问题把这个问题解决掉那么就可以了那么大家想一想
[07:31] 那么什么时候去调用它呢是不是就应该是在我们这个页面加载完成之后是不是去调用我们的一些初始化的相关的函数对不对大家还有没有印象我们前面讲过React.js中的那个什么的生命周期函数有印象吗那么我们就可以在干嘛呢来看一下就可以在我们这个list中我们给它添加一个生命周期函数那么什么生命周期函数呢是不是就是
[07:59] 当我们的这个组件加载完成之后我们去做一个初始化的操作这个大家能不能够理解当我们的组件在加载完成之后做一个初始化操作那么问题来了我在这个里面对吧但是我呢配置这一层他的又如何能够调用我这个model层里面的这个这个定义的这个方法呢怎么样定义直接肯定是不能定义的是不是
[08:30] 那么应该怎么做呢哎OK其实我们前面是不是讲过啊是不是就是我们这个connect它的的第二个这个第二个这个参数是不是就是把一些这个函数绑定到啊我们的这个publish中的对不对哎OK好那么是不是跟我们前面这个写的逻辑又几乎一样了对吧好那么我们是不是就可以这么来玩在我们的这个中呢第二个这个函数中呢我们再给它绑定一个
[08:58] 再给它绑定一个函数比如说叫init这个操作这样吧我们前面这个使用的是传统的方式下面这个呢我们就使用这个箭头的方式吧然后呢冒号然后呢括号是不是然后呢箭头因为没有参数吧没有参数那就直接其他就可以了因为初始化是没有参数的啊那么这个里面怎么玩呢就可以调用什么呢
[09:24] 依然是通过这个dispatch去做一个调用调用谁呢命名空间下面的什么呢不是按着new data了而是什么呢而是刚刚写的这个init data大家能够理解吗我们调用这个init然后呢我们是不是就把这个init的这个函数绑定到race.pubtist中那么我们在这个里面是不是就可以调用什么呢race.pubtist然后呢点什么呢init操作调用它你看啊
[09:53] 通过它的调用是不是就可以调用它对吧然后呢在这个里面呢又通过dispatcher去调用那么它是不是就可以调用这个里面所定义的函数它就是这样的一个逻辑那么在这个里面呢它呢又去通过我们去做一个异步的一个操作然后呢最后呢又去调用我们上面的这个函数那么这个函数最后返回来看一下这个函数
[10:23] 对吧你看put叫用它它呢叫用这个函数这个函数的返回这个函数的返回是不是在这做返回返回呢就导致我们state数据的更新那么state数据更新那么就导致我们的页面的这个run的方法的一个执行所以后是不是就会有这样的一个效果好来刷新看一下效果走那么显然我们可以看到这是不是也是有问题的对吧
[10:49] 你看它说不能读取这个属性不能读取这个属性那么为什么是这样呢我们可以来看一下它有没有发起请求呢我们来看一下并没有发起请求那么这样我们先把这个错误给它解决掉就是说我们在这个model中那么咱们这个数据呢我们先给它这样先给它保留但是呢我们这个里面呢我们没有数据没有数据那么最大的来一个1好
[11:24] 那我们这样我们是不是就已经先保证了他不报错编译不报错这样的话是不是就他能拿到我们的一个数据但是是不是没有数据那么当我们组件加载完成之后他就去干嘛呢他就去加载数据了看到没有是不是这个DS下面的list那么我们来看一下他请求是不是请求到是一个什么是一个JS请求的是一个HTML显然他肯定会报错对不对
[11:51] 报什么错呢报这个解析出错哎呦OK那么由于我们现在呢并没有这个请求这个路径那么没有这样的一个服务是不是没有办法拿到数据所以导致他这个出错啊这是没有任何疑问的这肯定是这样的对吧那么我们又该如何解决这个问题呢我们一会儿来讲这个问解决问题啊好那我们先来看一下这个讲义那么在我们model中请求数据是不是应该这么去玩
[12:18] 那么我们首先就有一个request.js他呢负责去一步请求通过他一步请求我们的一个一步请求我们的一个服务对吧请求一个服务然后呢我们在modo中呢我们就可以去导入这个request然后加一个什么呢effect然后呢我们通过他呢去做我们的一步的这个请求ok然后呢我们在我们的页面中呢就可以在我们的组件加载完成之后呢
[12:47] 做一个初始化的操作对吧然后呢dispatch再去调用我们model中的这个方法ok这样的一个逻辑那么最后是不是就可以看到这样的效果他是不是就请求当然了你返回html当然会报错了对吧ok好那么关于这个model中的请求数据呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 React 项目中使用 Dva 框架进行状态管理，包括定义 model、连接组件、处理数据更新和调试错误。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- IDE 中显示 `List.js` 文件，其中包含 `connect` 函数用于将 model 中的 `dispatch` 方法绑定到组件的 `this.props`。
- 代码中定义了 `dispatch` 的 `add` 函数，其 `type` 属性为 `namespace + '/addNewData'`。
- 组件 `List` 继承自 `React.Component`，其 `render` 方法返回一个包含 `ul` 和 `button` 的结构。

画面 2:
- IDE 中显示 `models\listData.js` 文件，其中定义了 `export default` 的 model。
- model 包含 `namespace: 'list'`，`state` 初始数据为 `{ data: [1, 2, 3], maxNum: 3 }`。
- `reducers` 定义了 `addNewData` 函数，用于处理状态更新。
- 同时显示了 Typora 中的 `讲义.md` 文件，其中包含多个代码截图和浏览器调试信息。

画面 3:
- IDE 中显示 `package.json` 文件，其中 `devDependencies` 部分包含 `umi` 和 `umi-plugin-React` 的版本号。

画面 4:
- IDE 中显示 `models\listData.js` 文件，其中 `effects` 部分定义了 `initData` 函数，使用 `sagaEffects` 进行异步操作。
- `const url = '/ds/list'`，`yield put({ type: 'addNewData', data: data })`。

画面 5:
- IDE 中显示 `models\listData.js` 文件，`effects` 部分的 `initData` 函数中 `const url = '/ds/list'`，`yield put({ type: 'addNewData', data: data })`。

画面 6:
- IDE 中显示 `models\listData.js` 文件，`reducers` 部分的 `addNewData` 函数中 `if (state.data)` 条件判断。
- `state` 对象的结构显示在右侧的代码提示框中，包含 `status`, `screen`, `scroll` 等属性。

画面 7:
- IDE 中显示 `models\listData.js` 文件，`state` 的初始数据为 `{ data: [1, 2, 3], maxNum: 3 }`。
- `reducers` 中 `addNewData` 函数的 `if (state.data)` 条件判断。

画面 8:
- 浏览器中显示错误信息：`TypeError: Cannot read property 'map' of undefined`。
- 错误发生在 `List.render` 方法中，`this.props.dataList` 为 `undefined`。
- 错误堆栈显示 React 的组件生命周期方法调用。

画面 9:
- IDE 中显示 `List.js` 文件，`connect` 函数用于绑定 `dispatch`。
- 组件 `List` 的 `componentDidMount` 方法被注释掉。

画面 10:
- IDE 中显示 `List.js` 文件，`componentDidMount` 方法被注释掉。
- `init` 函数被定义，但未实现。

画面 11:
- IDE 中显示 `models\listData.js` 文件，`effects` 部分的 `initData` 函数中 `const url = '/ds/list'`，`yield put({ type: 'addNewData', data: data })`。

画面 12:
- IDE 中显示 `List.js` 文件，`componentDidMount` 方法中调用 `this.props.Init()`。
- `render` 方法中 `button` 的 `onClick` 事件绑定到 `this.props.add`。

画面 13:
- IDE 中显示 `models\listData.js` 文件，`state` 的初始数据为 `{ data: [1], maxNum: 3 }`。
- `reducers` 中 `addNewData` 函数的 `if (state.data)` 条件判断。

画面 14:
- Typora 中的 `讲义.md` 文件，其中包含 `button` 的 `onClick` 事件绑定到 `this.props.addNewData()`。
- 浏览器开发者工具中显示错误信息：`Uncaught at _called at _called`，`Generator.prototype._invoke`，`at http://localhost:8000/js/...`。
- 错误提示“返回的数据不是json导致”，并建议“查看后端需求”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```javascript
// 并且，将返回的数据，绑定到this.props
// 接收第二个函数，这个函数的作用：将定义的函数绑定到this.props中，调用model层中定义的函数
connect ((state) => {
    return {
        dataList: state[namespase].data,
        maxNum: state[namespase].maxNum
    }, (dispatch) => { // dispatch的作用：可以调用model层定义的函数
        return {
            add: function () {
                dispatch({ // 通过dispatch调用model中定义的函数，通过type属性，指定函数命名
                    type: namespace + '/addNewData'
                });
            }
        }
    });
}
class List extends React.Component{
    render() {
        return (
            <div>
                {this.props.dataList.map((value, index)=>{ 
                    return <li key={index}>{value}</li>
                })}
                <button onClick={() => {}}>点击我</button>
            </div>
        );
    }
}
```

画面 2:
```javascript
export default {
    namespace: 'list',
    state: {
        data: [1, 2, 3],
        maxNum: 3
    },
    reducers: { // 定义的一些函数
        addNewData: function (state) { // state: 指的是更新之前的的状态数据
            let maxNum = state.maxNum + 1;
            let newArr = [...state.data, maxNum];
            return {
                data: newArr,
                maxNum: maxNum
            }
        }
    },
    effects: { // 新增effects配置，用于异步加载数据
        *initData({params, sagaEffects}) { // 定义异步方法
            const {call, put} = sagaEffects; // 获取到call、put方法
            const url = '/ds/list'; // 定义请求的url
            let data = yield call(request, url); // 执行请求
            yield put({ // 调用reducers中的方法
                type: 'addNewData',
                data: data // 传递ajax回来的数据
            });
        }
    }
}
```

画面 3:
```json
{
    "name": "itcast-reactjs",
    "version": "1.0.0",
    "main": "index.js",
    "license": "MIT",
    "devDependencies": {
        "umi": "2.2.4",
        "umi-plugin-React": "^1.2.2"
    }
}
```

画面 4:
```javascript
let maxNum = state.maxNum + 1;
let newArr = [...state.data, maxNum];
return {
    data: newArr,
    maxNum: maxNum
}
// 通过return 返回更新后的数据
effects: { // 新增effects配置，用于异步加载数据
    *initData({params, sagaEffects}) { // 定义异步方法
        const {call, put} = sagaEffects; // 获取到call、put方法
        const url = '/ds/list'; // 定义请求的url
        let data = yield call(request, url); // 执行请求
        yield put({ // 调用reducers中的方法
            type: 'addNewData',
            data: data // 传递ajax回来的数据
        });
    }
}
```

画面 5:
```javascript
reducers: { // 定义的一些函数
    addNewData: function (state) { // state: 指的是更新之前的的状态数据
        let maxNum = state.maxNum + 1;
        let newArr = [...state.data, maxNum];
        return {
            data: newArr,
            maxNum: maxNum
        }
    }
},
effects: { // 新增effects配置，用于异步加载数据
    *initData({params, sagaEffects}) { // 定义异步方法
        const {call, put} = sagaEffects; // 获取到call、put方法
        const url = '/ds/list'; // 定义请求的url
        let data = yield call(request, url); // 执行请求
        yield put({ // 调用reducers中的方法
            type: 'addNewData',
            data: data // 传递ajax回来的数据
        });
    }
}
```

画面 6:
```javascript
maxNum: 3
reducers: { // 定义的一些函数
    addNewData: function (state) { // state: 指的是更新之前的的状态数据
        if (state.data

