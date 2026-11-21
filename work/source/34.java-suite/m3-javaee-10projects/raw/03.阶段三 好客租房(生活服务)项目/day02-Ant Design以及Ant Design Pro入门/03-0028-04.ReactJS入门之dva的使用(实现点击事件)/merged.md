# 04.ReactJS入门之dva的使用（实现点击事件）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day02-Ant Design以及Ant Design Pro入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day02-Ant Design以及Ant Design Pro入门\04.ReactJS入门之dva的使用（实现点击事件）【海量资源尽在 ubkz.com】.mp4
- 时长 20分7秒（音频 1207s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接着刚刚的内容继续那么我们刚刚的实现呢是将我们的数据啊就之前呢我们这个数据呢是在我们的Pager这一层然后呢我们现在把这个Pager这一层的数据分离到了Model这一层由Model做了这个管理那么我们最终实现的效果呢就是这样的一个效果但是呢我们这个按钮的一个事件是不是还没有去实现呢那么我们来看一下
[00:28] 在我们之前的这个实现是不是在这个里面直接做一个this.setState去做一个数据的更新但是大家想一想现在你这样去做一更新能够去更新我们的State的状态的数据吗那显然是更新不了对不对因为我们这个数据现在已经放到什么呢model这一层那么你在这个位置它怎么能够更新呢所以它是更新不了那么接下来呢我们就来
[00:56] 来解决这个问题解决什么问题呢就是我们需要在我们的这个Pager这个层然后呢触发我们的一些相关的事件然后呢他呢去更新或者去调用我们这个model这一层的这个方法然后呢去做一些更新啊做这样的事情好那么来看一下这个怎么做呢我们看一下
[01:18] 那么我们就需要在这个model这一层对吧我们添加一个什么呢reduce的这个方法用于更新我们的stagedo数据那我们来看一下这个怎么玩呢就需要在我们的这个model这一层我们添加一个reduce添加个reduce这样的一个配置项配置项然后这个下面注意这个下面我配置的都是什么呢都是定义
[01:47] 定义的一些什么呢函数啊一些函数那我们来看一下这个函数函数名呢你随便写啊比如说我就叫andnew一个什么呢date哎这个总可以吧那么function那么要注意的是在这个function中呢它呢会给我们传递一个参数叫什么呢叫state注意的是那么这个state这个state它指的是什么呢指的是
[02:17] 指的是我们更新之前的那个状态数据是我们更新之前的那个数据而不是我们更新之后那个数据千万要记住那么我们该如何去更新数据呢如何更新数据那么我们就需要通过什么呢return然后呢返回更新后的数据返回更新后的数据去做这样的一个更新
[02:46] 那么这个里面的逻辑应该怎么去写呢那我们是不是就可以把前面我们这个里面的这个逻辑是不是给它靠过来把这个先给它注释掉因为这个代码显然是不能在这个位置是不是执行了好那么我们来看一下那么把这个逻辑我们拷贝到这个里面来那么我们看一下这个max number它这个值是从过哪里来呢是不是拿到我们状态的这个里面的值那么这个状态的值怎么拿到呢它是不是说
[03:14] 这个状态的这个值他已经给我们传递到这个位置了对吧已经传到这个位置所以我们就可以通过这个state这个传入的一个参数就可以拿到我们之前的max number这个数据那么拿到这个数据好他就搞定了那么下面我们来看一下这个集合是不是也是可以通过state去拿到他里面的一个什么呢是不是date对吧一个date
[03:43] 然后呢这个date是不是就可以把这个数组是不是给它展开然后呢我们再加一个max number是不是就可以形成一个新的一个数组新的数组那么原来我们的逻辑是通过this.setState去做一个数据的更新但是现在能这样更新吗不行啊是不可以的那么前面我们说过那么如何去更新呢通过returnreturn什么呢return它来看一下
[04:12] returnreturn什么呢return我们这个新的这个数据return你新的这个数据就可以了那么我们的新的数据那么数据中它原来叫什么data而不是叫datalist所以我们改成data这个大家能够理解吗
[04:28] 然后呢这个max number那就是这个max number这个没有任何问题这个是OK的好那么现在我们是不是就已经在我们的model这一层完成了这个函数的一个定义那么关键的问题来了对吧你这个函数是不是定义好了对吧定义好了那么我们如何在我们的pager这一个层去调用我们这个model这一层的这个数据呢或者这个函数呢怎么样去调用
[04:57] 那么依然呢是要通过我们DADVA所提供的这个connector来做一个调用它呢我们知道它的作用是什么是不是做连接是不是用于连接我们的model层和我们的这个pager这一层呢哎呀OK好那我们来看一下这个应该怎么去做啊这么去做
[05:20] 那么大家可以看一下我们这connect怎么去用是不是通过一个修饰符然后去使用的对吧然后呢我们传递第一个参数是不是也是一个函数这个函数的作用我们知道啊第一个这个我们先把它删掉先缓我们再说那么第一个这个函数它的作用是不是就把这个返回的这个数据绑定到哪里呢是不是this.purpose
[05:48] 绑定到这个里面来对吧把这个数据绑定上去那么要注意的是我们这个connect连接符那么它呢这个修饰符然后呢它呢也接收什么呢接收第二个什么呢第二个第二个函数那么这个函数的一个它的一个作用它的作用是什么呢是将什么呢
[06:17] 将我们的这个定义的函数绑定到绑定到哪里呢绑定到this.purpose中注意这是它的第一个作用啊就将我们定义的函数绑定到这个里面来然后呢还有什么作用呢它还有个作用啊就是可以去调用什么呢调用我们modelmodel层中
[06:50] 定义的函数它有两个作用第一呢是把我们的一个定义的函数绑定到这个里面来第二呢就是调用Mogut的定义的函数那么看到这大家可能会有点不太明白这个是什么意思呢对不对好的我们来写一下代码大家就明白了那么我们在这个位置给它传递第二个参数这个参数呢也是一个函数同样呢我们采用的是箭头函数的一种表达方式然后呢括号
[07:19] 然后呢箭头大括号还是这样去写那么这个里面我们来看一下他所接收的一个参数叫什么呢参数他也是一个函数啊那么这个函数的名字叫什么呢叫dispatcher那么这个dispatcher他的一个作用是什么注意那么dispatcher的一个作用啊他的作用啊他的作用就非常非常重要也很关键了就是什么呢可以去
[07:50] 调用什么呢我们model乘定义的什么呢定义的函数定义的函数dispatcher是不是就是做这种分发这种作用的好那么接下来呢我们就来看一下它呢如何去调用我们model这个地方写错了model11L那么model乘的这个函数的呢我们来看一下怎么去做
[08:19] 那么前面我们说过第二个函数它的作用有两个第一个呢是把它绑定到this.prefs中然后呢第二个呢是我们调用我们model层的函数我们先来实现第一个那么它的写法呢是不是就和前面这种写法一样啊也是一个什么呢return啊returnreturn然后呢一个对象然后这个里面呢我们去定一些函数比如说叫什么呢叫and啊我就写一个and
[08:49] 这个函数为了和我们前面写这个函数名的区分所以我们就那个地方-写写一个&然后我们这个地方写一个什么写一个function写一个function就写个function好那么&这个function那么这个里面我们接收什么我们先不做接收没有任何参数然后我们是不是就可以注意
[09:13] 当我们去调用了一个and当我们去定义了一个and这个函数的话我们做一个return那么我们就已经将什么呢已经将这个返回到这个函数绑定到哪里呢this.propstu那么绑定到这个里面了好那我们就先写到这
[09:36] 那么我们现在既然已经绑定到类似点Purpose中那么我们是不是就可以在下面的这个位置注意是不是在我们下面这个位置那么我们就可以直接去调用它了点什么呢AND看明白了吗是不是我直接就可以调用我这个AND这个方法而这个AND这个方法是不是由我的这个函数
[10:00] 帮我是不是绑定到我认识点prop中对吧绑在这个里面来那我就可以调用了好那么接下来关键点来了就需要去看一下我们去如何在这个函数中去调用model这一层所定义的函数呢那么就需要通过它了那么通过这个dispatch然后呢我们去做一个执行执行什么呢我们给它去指定一个什么呢
[10:29] 指定一个这个它的函数指定一个函数这个函数名呢我们需要通过一个type属性去做一个指定做一个指定type那么注意那么这一块这个怎么指定呢我们来看一下在我们model这一层是不是我们有一个方法名叫做按new date对吧那么我们就可以把它靠过来但是这样行吗可以吗
[10:55] 不可以的为什么呢大家可以想一下那么前面我们提到过model这一层可能呢会有很多的一些这个model层那么如果有两个model中都有这个NNU对的这个函数那么我该调用哪一个呢对不对那么我该如何区分呢哎没错就是通过前面的什么呢命名空间namespace命名空间去加一个他斜杠注意有个斜杠就是说
[11:22] 这个命名空间下面的这个函数这个函数那么就可以做一个调用了那么OK在这儿是不是我们就是通过什么呢通过这个dispatcher通过这个dispatcher去调用什么呢我们这个model中定义的这个函数对吧通过它就可以做一个调用那么调用的时候呢我们需要去通过什么呢通过这个type属性
[11:51] 去指定指定什么指定我们的函数名函数名那么它的格式它的一个格式格式是这样的格式叫什么呢namespacenamespace斜个加一个函数名OK它的一个格式是这样的格式那么我们这样的话就可以完成一个调用了好那么来看一下效果这个搞定了没有点击点火走走走
[12:23] 找是不是没有任何问题ok所以我们可以看到这样的一种实现方式是不是我们就已经完成了什么我们配置跟我们的model的这一层的一个分离好我们一起来看一下这个讲义那么在讲义中的跟我们的实现的方法的基本上类似基本类似那么我们也是需要在我们的model这一层的增加一个reduce
[12:49] 然后我们可以定义一系列这个函数当然我们现在是不是只有一个函数你是不是在下面还可以接着定义很多的函数都是可以的然后在函数内部要注意的是我们要想去更新数据那么你需要返回的就是更新的这个数据更新这个数据通过这个return去做更新而不是通过那个什么setSig来做一个完成好然后
[13:15] 当我们在model这一层我们所定义了这个函数之后我们就可以在我们的page这一层进行去调用它那么怎么调用的我们来看一下它是通过了什么通过了连接器对吧的第二个参数那么将我们所定义的看在这跟我们刚刚的写法稍微有点不同但是是一样的那么我们来看一下
[13:45] 他们这个名字叫什么呢叫做map dispatcher to properties那么就是说将我们这个dispatcher映射到我们的一个类似点什么publish中好那么把它映射进来我们是不是就可以直接调用它了哎呀ok然后呢我们来看一下它返回的这个数据注意它返回这个数据就是将我们的这个函数绑定到啊
[14:09] 这个race.publess中那么我们是不是定义了这样的一个函数那么这个函数中是不是就通过一个dispatcher就可以去调用model中的这个方法对吧当然了你要指定它的一个type是它的命名空间下面的这个函数的这个名字那么我们就能够在我们下面的这个什么click这个事件中调用我们所定义的这个函数注意这个函数名和我们
[14:39] 在model从含重名定义是一样的但是它不是这个函数大家别搞混所以我们刚刚实现的时候我在这个位置显示就是个and就是个and你看它掉的是一个and这个千万别搞混OK这个就它的一个实现那么下面我们还是把这个流程用这个图解的方式给大家来重新的梳理一下帮助大家做一个理解好那么
[15:06] 前面的这个呢就不需要了把它全部的删掉然后呢我们来看一下那么我们把刚刚的这个model这一层的这个定义啊我们拷贝出来这个呢是我们model层的一个定义咱们把它放到这个画图板里面去再放到左边然后呢我们来看一下接下来呢是在我们的这个配置这一层对吧配置这一层那么看一下这个
[15:35] 那么有点有点截不了截不了这个图这样我把这个就删掉了因为这个就没用了对我们现在而言是没用了好那么这样的话我看好像差不多好可以把这个各种函数也删掉吧没用好那么这样的话就截全了那么我们来截一个图截一个图我们来一起分析一下那么把这个图呢我们也抠过来丢在这里丢在这里好
[16:09] 搞定那么我们来看一下首先第一步呢我们是不是在我们的model这一层呢做了这样的一个函数的一个定义啊对吧通过一个函数定义好那么当我们定义好之后啊那么我们就可以在我们的pager呢这一层然后呢我们去做一个事情做什么事情呢通过我们这个connector它的第二个这个参数的这个函数做一件事情就是
[16:39] 把我们的这个按的这个方法绑定到哪里呢是不是绑定到我们这个race.properties2是不是绑定到这儿绑定到这个里面绑定到这儿那么这个可以把它认为这是第一步第一步那么这个是不是第二步对吧绑定到这个里面来那么绑定到这个里面来之后呢我们是不是就可以通过这个按钮的onclick事件然后呢去调用
[17:12] 他对吧是不是调用他那么我们画一个这个啊然后呢他呢去就可以去调用他了啊就可以去调用这个函数这个呢就是我们第三步对吧第三步然后呢进行调用调用这个函数啊调用这个函数那么当我们调用这个函数的时候然后呢要注意的是关键点就来了那么在这个里面呢我们通过一个dispatcher
[17:41] 那么这个dispatch是我们这个连接器是不是给我们去传入的一个参数那么这个dispatch它就能够去调用什么呢调用我们这个调用我们这个reduce中所定义的这个函数就能调用它这个是不是就叫什么呢这是第几步了第四步去调用我们这个model
[18:14] model中的这个函数叫model的函数然后呢我们调用这个函数在这个函数中呢它由于返回了一个return返回了一个新的一个对象那么我返回的这个新的这个对象相当于就在更新了我这个state的这个数据是不是相当于更新了我们这个数据更新了这个数据这个呢就是更新数据第五步就是
[18:45] 更新我们的一个状态数据更新了我们这个状态数据那么我们这个更新状态数据之后那么我们呢就可以看到这个React这个框架呢对吧然后呢他呢就会去调用什么呢调用我们这个run的这个方法对吧就会调用我们这个run的这个方法这样去写这样去画React框架就会调用我们这个
[19:15] render这个方法第几步呢第六步是我们的React.js框架框架就会调用我们的什么呢render函数函数进行什么呢进行渲染进行叫重新渲染重新渲染OK好那么最终我们所看到的一个效果是不是就是当我们一点击重新渲染这个页面是不是就出来了
[19:49] 哎OK好这个呢就是我们整个的一个这个动态的一个这样的一个实现啊好关于这个实现呢我们就先讲到这里那么这个关键点就是在我们的这个model这一层是不是定义这个函数啊那么怎么去调用它哎OK好那么我们就先讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 DVA（基于 Redux 的框架）在 React 项目中管理状态，包括定义 model、连接组件与 model、以及通过 dispatch 触发状态更新。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 DVA 的 model 定义结构，包含 namespace、state 和 reducers，其中 reducers 中定义了 addNewData 函数用于更新状态。
画面 2: 展示了 React 组件中使用 this.props.dataList 显示列表数据，并通过 onClick 事件修改状态。
画面 3: 展示了 React 组件中 onClick 事件的代码，用于更新状态。
画面 4: 展示了 DVA model 中 reducers 的 addNewData 函数，用于根据 state 更新数据。
画面 5: 展示了 DVA 的 @connect 装饰器，用于将 state 和 dispatch 映射到组件的 props。
画面 6: 展示了 React 组件中 onClick 事件的代码，用于更新状态。
画面 7: 展示了 DVA 的 @connect 装饰器，用于将 state 和 dispatch 映射到组件的 props。
画面 8: 展示了如何使用 connect 将 state 和 dispatch 映射到组件的 props。
画面 9: 展示了 DVA 的 @connect 装饰器，用于将 state 和 dispatch 映射到组件的 props。
画面 10: 展示了 React 组件中使用 this.props.dataList 显示列表数据，并通过 onClick 事件修改状态。
画面 11: 展示了 DVA 的 @connect 装饰器，用于将 state 和 dispatch 映射到组件的 props。
画面 12: 展示了 DVA 的 @connect 装饰器，用于将 state 和 dispatch 映射到组件的 props。
画面 13: 展示了 DVA 的 @connect 装饰器，用于将 state 和 dispatch 映射到组件的 props。
画面 14: 展示了如何使用 connect 将 state 和 dispatch 映射到组件的 props。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```javascript
export default {
  namespace: 'list',
  state: {
    data: [1, 2, 3],
    maxNum: 3
  },
  reducers: {
    addNewData(state) {
      let maxNum = state.maxNum + 1;
      let newArr = [...state.data, maxNum];
      return {
        data: newArr,
        maxNum: maxNum
      };
    }
  }
};
```

画面 2:
```javascript
render() {
  return (
    <div>
      <ul>
        {this.props.dataList.map((value, index) => {
          return <li key={index}>{value}</li>
        })}
      </ul>
      <button onClick={() => {
        let maxNum = this.props.maxNum + 1;
        let newArr = [...this.props.dataList, maxNum];
        this.setState({
          dataList: newArr,
          maxNum: maxNum
        });
      }}>点我</button>
    </div>
  );
}
```

画面 3:
```javascript
export default List;
```

画面 4:
```javascript
export default {
  namespace: 'list',
  state: {
    data: [1, 2, 3],
    maxNum: 3
  },
  reducers: {
    addNewData: function (state) { // state: 指的是更新之前的原始数据
      let maxNum = state.maxNum + 1;
      let newArr = [...state.data, maxNum];
      return {
        data: newArr,
        maxNum: maxNum
      };
    }
  }
};
```

画面 5:
```javascript
@connect ((state) => {
  return {
    dataList: state['namespace'].data,
    maxNum: state['namespace'].maxNum
  }
}, (dispatch) => {
  return {
    add: function () {
      dispatch({
        type: 'namespace' + '/addNewData'
      });
    }
  }
})
class List extends React.Component{
  constructor(props) {
    super(props);
    // this.state = {
    //   dataList: [1, 2, 3],
    //   maxNum: 3
    // }
  }
  render() {
    return (
      <div>
        <ul>
          {this.props.dataList.map((value, index) => {
            return <li key={index}>{value}</li>
          })}
        </ul>
        <button onClick={() => {
          this.props.add();
        }}>点我</button>
      </div>
    );
  }
}
```

画面 6:
```javascript
export default List;
```

画面 7:
```javascript
@connect ((state) => {
  return {
    dataList: state['namespace'].data,
    maxNum: state['namespace'].maxNum
  }
}, (dispatch) => {
  return {
    add: function () {
      dispatch({
        type: 'namespace' + '/addNewData'
      });
    }
  }
})
class List extends React.Component{
  constructor(props) {
    super(props);
    // this.state = {
    //   dataList: [1, 2, 3],
    //   maxNum: 3
    // }
  }
  render() {
    return (
      <div>
        <ul>
          {this.props.dataList.map((value, index) => {
            return <li key={index}>{value}</li>
          })}
        </ul>
        <button onClick={() => {
          this.props.add();
        }}>点我</button>
      </div>
    );
  }
}
```

画面 8:
```javascript
import React from 'React';
import { connect } from 'dva';

const mapStateToProps = (state) => {
  const listData = state['namespace'].data;
  const maxNum = state['namespace'].maxNum;
  return {
    listData, maxNum
  };
};

const mapDispatchToProps = (dispatch) => { // 定义方法，dispatch 内置函数
  return {
    addNewData: () => { // 定义方法
      dispatch({ // 通过 dispatch 调用 model 中定义的函数，通过 type 属性，指定方法名，格式：namespace/方法名
        type: 'namespace' + '/addNewData'
      };
    }
  };
};

@connect(mapStateToProps, mapDispatchToProps) // mapStateToPros、mapDispatchToProps：将方法映射到 props
class List extends React.Component{
  render() {
    return (
      <div>
        <ul>
          {this.props.dataList.map((value, index) => {
            return <li key={index}>{value}</li>
          })}
        </ul>
        <button onClick={() => {
          this.props.add();
        }}>点我</button>
      </div>
    );
  }
}
```

画面 9:
```javascript
@connect ((state) => {
  return {
    dataList: state['namespace'].data,
    maxNum: state['namespace'].maxNum
  }
}, (dispatch) => {
  return {
    add: function () {
      dispatch({
        type: 'namespace' + '/addNewData'
      });
    }
  }
})
class List extends React.Component{
  constructor(props) {
    super(props);
    // this.state = {
    //   dataList: [1, 2, 3],
    //   maxNum: 3
    // }
  }
  render() {
    return (
      <div>
        <ul>
          {this.props.dataList.map((value, index) => {
            return <li key={index}>{value}</li>
          })}
        </ul>
        <button onClick={() => {
          this.props.add();
        }}>点我</button>
      </div>
    );
  }
}
```

画面 10:
```javascript
render() {
  return (
    <div>
      <ul>
        {this.props.dataList.map((value, index) => {
          return <li key={index}>{value}</li>
        })}
      </ul>
      <button onClick={() => {
        this.props.add();
      }}>点我</button>
    </div>
  );
}
```

画面 11:
```javascript
@connect ((state) => {
  return {
    dataList: state['namespace'].data,
    maxNum: state['namespace'].maxNum
  }
}, (dispatch) => {
  return {
    add: function () {
      dispatch({
        type: 'namespace' + '/addNewData'
      });
    }
  }
})
class List extends React.Component{
  render() {
    return (
      <div>
        <ul>
          {this.props.dataList.map((value, index) => {
            return <li key={index}>{value}</li>
          })}
        </ul>
        <button onClick={() => {
          this.props.add();
        }}>点我</button>
      </div>
    );
  }
}
```

画面 12:
```javascript
@connect ((state) => {
  return {
    dataList: state['namespace'].data,
    maxNum: state['namespace'].maxNum
  }
}, (dispatch) => {
  return {
    add: function ()

