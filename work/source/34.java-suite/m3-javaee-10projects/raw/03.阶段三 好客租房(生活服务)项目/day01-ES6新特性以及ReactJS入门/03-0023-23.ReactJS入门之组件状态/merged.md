# 23.ReactJS入门之组件状态

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day01-ES6新特性以及ReactJS入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day01-ES6新特性以及ReactJS入门\23.ReactJS入门之组件状态【海量资源尽在 ubkz.com】.mp4
- 时长 17分30秒（音频 1050s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们来看一下组件的状态啊组件的状态呢也是非常重要的一个内容我们一起来看一下那么每一个组件呢它都有一个状态那么它的值呢保存在this.state中当这个状态的值发生变化的时候那么React框架会自动调用run的方法然后呢重新渲染我们这个页面那么我们接下来呢就写一个案例
[00:29] 我们来给大家演示一下那么我们在这个pages下面呢写一个页面写一个叫什么呢叫list这样的一个解释然后呢我们依然呢写一个list的组件import导入叫React然后呢from谁呢React对吧好然后呢下面我们写个classlist然后呢继承谁呢叫React.component
[00:59] 然后呢我们下面写一个exportexport什么呢default什么呢list哎OK好那么我们先把这个组件呢先写好在这个里面我们要实现的是不是叫random方法哎OK好那么random方法里面写什么内容呢我们一会儿再说啊一会儿再说这样咱们就先实现这个random方法吧然后呢我在这写一个return什么呢括号然后后面写一个内容
[01:30] 那么在这个位置呢我写一个DIVDIV在DIV中呢我写一个UL然后呢UL中呢我写一个LA然后呢1然后呢写2写3好来看效果那么我相信啊这个效果是不是大家一定能够看懂也能够写出来没有任何问题啊那么我在下面呢我再来一个按钮叫button然后呢它的值呢叫什么呢点我比如说我写个点我
[02:00] 那么我看一下这个位置是不是有个按钮那么我们想要实现的效果什么效果呢就是说我点击一次点我然后呢后面追加一个4再点击点我追加一个5以此类推哎呀OK这个效果大家明白了吗哎呀OK那么想要实现这个效果呢其实有两部分第一部分就是我们这个123的初始值你不能写死到我们页面对不对哎呀OK那么这个应该怎么做我们来看一下那么我们来看一下怎么做呢
[02:29] 我们这样来做啊刚才我们说过是不是它有一个状态值啊那这个状态是怎么用的我们首先呢要写它的一个构造函数啊那么构造函数中呢有一个叫properties那么这个properties它呢是固定写法我们就要用super复类中的这个构造函数把它传递过去然后呢下面我们就要用this.state关键点来了
[02:56] this.stated它保存的就是我们组件的一个状态它等于什么呢等于我们可以写一个叫datalist等于比如说叫什么呢123这个注意不能用等于冒号datalist是123是123因为它是个对象它是个对象那么下面我们在这个位置我是不是就不用这样去写了对不对那么应该怎么写呢是不是可以这样来写
[03:24] 那么我要插入我一个json的代码那我必须写一个大括号那么我在这写一个什么呢是不是可以写一个this.叫做data什么呢this.什么state.data什么呢list注意这个l是大写而不是小写点什么呢点一个map点一个map点map是不是可以对它做一个循环做一个循环那么这个map怎么写呢我们来看一下
[03:53] map中是不是接收一个回调函数那么这个回调函数怎么样去写我们来看一下我在这直接写一个键轴函数那么它的参数是这样来写参数是不是有一个叫做value还有个叫什么index其实index对我们来讲没什么用现在我们也写着吧那么我们拿到这个值之后我们是不是可以直接return一个什么呢
[04:19] DIV然后呢这个里面写一个什么呢写一个这个value值好来看效果来刷新看一下那么显然呢我们这个错了不应该用DIV应该用什么LI应该用LI因为你UL下面所对应的是不是就LI啊好那么我可以看到这个效果跟我们刚刚写死的这个效果是不是一样啊好那么首先第一个我们这个工作就做完了那么接下来我们来看一下我们该如何给这个按钮添加一个点击事件呢
[04:50] 这样来添加是不是在一个button下面写一个onclickonclick那么我们这个里面是不是要写我们的代码那么我写一个函数那么这个函数呢同样的我是使用那个箭头函数它箭头指向到它这个大家能看懂吗是不是就没有参数的一个函数那么当我点击当我点击的时候那么我要执行这个函数那我要执行什么呢那么有同学肯定会这么去想
[05:18] 那我是不是应该先拿到啊拿到之前的这个这个值去对他做一个修改啊去做一个修改那么有的人又会想我为什么修改这个值呢啊为什么修改这个值那么大家想一想啊就是说我想点击这个按钮想要去增加一个我网页中的一个内容那么大家注意那么刚刚我们讲到这句话啊就是说
[05:44] 当这个State值发生变化的时候他会重新调用run的方法那么也就意味着说我们只要改变他的值那么他是不是就能够去给我们去重新刷新这个页面对不对好的我们来先来看一下这个效果怎么样做呢当然有同学肯定会想到说这个比较简单我这样来写看一下这样行不行State然后我重新给他复值是不是就可以了
[06:13] 等于什么呢比如说来一个来一个这个data list123来一个什么的再加一个4你肯定会这样去想这样行不行呢我们来看效果刷新一下当我点击点我走走走有反应吗没有那么我们来看一下有没有报错呢来看一下那么有没有报错有没有报错来刷新一下你看他有没有报错呢
[06:44] 有报错有报错你看他说这个listrun的这个list我们来看一下是不是这个报错我先把这个拿掉拿掉刷新一下这个是我们在循环的时候有一个有一个这个k的问题有一个这个k的问题那么这个怎么做我们给他来一个k吧k等于什么呢先写个index我们先保证他不报错
[07:14] 好你看这样的话是不是就不报错了然后呢下面的我们把刚刚这个代码拿过来我们来看一下这样写OK不OK点点点点点点那么是不是说既没有报错也没有什么的啊也没有去实现我们这样的效果对不对啊那么哎同学们要注意了那么这个stay的这个值是不能够这样去修改的
[07:40] 你初始值可以这样去设置但是你修改它的值的时候不能这样去修改那么应该怎么样修改呢你要这样去修改要注意了要通过list点什么的setstate这个方法去修改它的值修改什么呢修改它的叫datalist然后呢修改什么呢修改成1234我们来看一下效果看有没有效果好然后呢我们来刷新一下看效果那么点击点我走
[08:10] 是不是有效果当我点击点我的时候是不是就多了一个4那么它这个原理是不是就是当我们去修改了这个state中的data list这个值它是不是会React框架会重新帮我们去调用这个方法那么是不是会重新做一次循环OK那么当我再次点击点我的时候有没有效果呢来测试一下走走走
[08:39] 会发现没有效果为什么呢因为你这个值是不是一直是1234所以他的值没有发生变化他就不会再去做一个重新渲染这个大家明白了吗ok好那么我们接下来要做的事情是不是就是说我可以让他什么的不断的去做增加那么我显然这个位置是不是不能够写死那么应该怎么做应该怎么做
[09:04] 好那么我们是不是应该这么去玩那么我是不是每一次应该拿到它的一个新的一个数字那么怎么拿到呢我是不是可以这样来拿到比如说我定义一个new一个rary新数字它等于什么它等于什么它是不是可以等于我之前的这个list.state中的datalist注意这个li是大写
[09:33] date list然后呢我给他干嘛呢来个三个点还记得这个运算符吗叫做什么呢展开运算符把它展开啊扩展运算符展开是不是就是我们拿到原来这个值123然后呢我再给他加一个值加一个什么值呢大家想一想加一个什么值那么我是不是可以在原来这个上面给他再增加一个属性叫什么呢叫做最大的一个数量之几
[10:02] 是不是就是3这个大家能够理解吗增加一个最大的一个数量number是不是就是3那么我在这个位置是不是就可以去设置一个它的一个最大的一个number等于this.state中的maxnumber然后呢加1这个大家能够理解吗是不是我拿到之前这个里面的值我给它加1是不是就ok了好那么我们把它拿过来
[10:32] 加1是不是作为扩展那么我新的一个数组就是是不是就是在原有的这个基础之上我再加一个我最大的一个这个值是不是就形成了一个新的一个数组那么设置为新的一个数组在这大家能够理解吗那么我最大的这个number是不是就是我的最大的这个number这个大家能够理解吗哎呀OK好那么这样的话我们是不是就完成了这样的一个数字数据的一个更新
[11:00] 好来看一下效果ok吗帮我点击点我走哎你发现是不是有走走走走哎ok是不是就实现了这样的一个动态增加的一个效果好那么这个大家能够理解吗好那么可以看到在我们的这个刚刚的实践过程中啊是不是使用了我们前面所讲的es6的一些新特性啊ok好那么接下来我们继续往下面看
[11:29] 那么下面的我们对这个过程的给大家做一个分析啊可能的有些同学还是不是很明白啊到底这个期间他发生了什么怎么就会我点击这个按钮然后他更新了这个值那么他为什么就会去把我这个页面中就会做一个更新呢那他到底是怎么玩的啊我们把这个过程呢给大家来梳理一下
[11:52] 好,那么我们来截一个图,来截一个图给大家来讲解一下那么前面这个图呢,我们就不需要了,把它删掉好,截一个什么图呢?
[12:02] 我们首先呢,来看一下我们这个页面啊,咱们把这个页面这个图先截过来放到哪呢?
[12:09] 放到我们这个画图板里面,放到这个位置啊,放到这个位置然后呢,我们把这个,我们刚刚写这个代码呢,我们也拷过来,我们来看一下
[12:20] 这个代码中的一些这个内容哎这样我就截个图哎直接截图吧呃截图呢会方便一点好那么我把这个图呢也放到我的这个画图板里面去然后呢我们把这个过程呢哎这个有点啊有点遮住原来这个图了啊咱们把它移动一下然后呢把它贴过来放到这个位置来看一下啊显示出来了好
[12:52] OK没有问题那我们来看一下刚刚我们到底发生了什么发生了什么来看一下首先呢我们说第一步的一个操作就是什么呢你看
[13:03] 这个是我的一个整个我组件的一个什么呢构造函数在我的构造函数中我是不是对我这个state是不是做了一个初始值做了个初始值那么有了这个初始值之后呢我这个run的方法在执行的时候那么我是不是就可以去做一个什么呢渲染是不是我在这个位置对它是不是做一个这个循环对吧做一个这个循环这个是不是就是我们的第一步这个操作对吧
[13:32] 第一步操作是不是就是我们获取获取什么呢我们这个state中的数据然后呢进行循环是不是进行做一个循环那么就可以显示出我们这样的一个效果所以你看第一步是不是做一个这样的一个循环然后呢它就会显示出这样的一个效果画这样的一个图给大家做一个示意图
[14:02] 好那么做这样的效果那么当我们显示完成之后呢我点击这个点我这个按钮当我点击这个按钮的时候呢它就会执行我这个函数对吧执行我这个箭头这个函数那么这个是我的第二步执行这个函数第二点击这个按钮执行这个函数那么在这个函数中呢它做什么事情呢是不是就去什么呢去
[14:31] 更新我们的state中的数据是吧做一个什么呢更新通过这个set state这个方法去更新我们这个数据做一个更新当我们这个更新之后注意啊当我们这个值更新之后呢我们这个值是不是就已经发生了变化对吧发生了变化啊他已经这个值就发生了变化那么这个是第三步啊这个值发生变化第三步这个
[15:01] 值state中的这个值发生了更新发生了更新也就发生了变化那么发生了变化之后我们React框架就会触发一个什么的run的方法的一个执行那么假设在这个位置这个位置这个就是我们的React框架框架那么这个React框架它就会去干嘛呢
[15:32] 调用我们这个方法重新做一个执行重新做一个执行重新去执行这个run的这个方法好这个就是第几步呢这个第四步是吧重新执行执行run的方法run的方法进行渲染做这样的一个事情好那么通过这四步的一个操作是不是就可以实现这样的一个效果点击点击点击这样的一个效果
[16:08] OK好那么我们来看一下来回顾一下组件的一个状态那么前面我们说过那么每一个组件呢它都有一个状态都保存在this.state中你们可以看到是不是在这个里面保存它的一个状态值当它的值发生变化的时候呢远岸框架会自动调用它run的方法重新做一个页面的一个渲染那么这里面呢有两个点需要我们注意第一个是
[16:37] 这个state这个值的这个初始的话需要在构造函数中完成你可以看到是不是在这个里面去完成它的一个初始那么第二呢就是要想修改这个值你不能直接给它做复值而是需要调用什么呢this.setstate的方法去做一个完成而不是直接对这个值进行做一个修改
[16:59] OK这个是我们需要做一个注意的那么在我们去做这个组件状态更新的时候大家一定要注意一点就是一旦这个值发生变化那么就会重新调用run的方法就会导致我们这个页面的一个重新的一个渲染OK这个一定要注意
[17:20] 通过这样的特性我们就可以做出很多一些这样的功能出来OK好那么关于组件的一个状态我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 React 组件中使用 state 管理数据，并通过 setState 方法实现列表的动态更新。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示项目结构，选中并编辑 `src/pages/List.js` 文件，内容为一个空的 React 组件模板。
画面 2: 在 `List.js` 中开始编写组件代码，导入 React，定义 `List` 类并开始 `render` 方法。
画面 3: 在 `render` 方法中，为 `<ul>` 标签添加了三个 `<li>` 标签，用于展示列表项。
画面 4: 在 `render` 方法中，开始编写 `this.state.dataList.map` 的代码，用于遍历数据。
画面 5: 完成 `map` 方法的代码，返回一个 `<li>` 元素，显示当前项的值。
画面 6: 在按钮的 `onClick` 事件中，开始编写 `this.state` 的代码，准备修改状态。
画面 7: 在 `onClick` 事件中，为 `<li>` 标签添加了 `key` 属性，值为 `index`。
画面 8: 与画面 7 相同，未发生实质变化。
画面 9: 在 `onClick` 事件中，开始编写 `this.setState` 方法，准备更新状态。
画面 10: 在 `onClick` 事件中，开始编写 `let maxNum = this.state.maxNum + 1;` 代码，用于计算新的最大值。
画面 11: 在 `onClick` 事件中，完成 `let newArr = [...this.state.dataList, maxNum];` 代码，用于创建新的数组。
画面 12: 切换到图像编辑软件 PicPick，界面为黑色画布，无实际代码内容。
画面 13: 切换回代码编辑器，显示 `List.js` 文件的完整代码，包括 `constructor`、`render` 方法和 `setState` 的实现。
画面 14: 显示 Typora 编辑器中的 Markdown 文档，内容为 React 状态管理的讲解，其中包含与代码对应的注释。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<module version="4" inherit-compiler-output="true">
  <component name="NewModuleRootManager" />
  <exclude-output />
  <orderEntry type="sourceFolder" forTests="false" />
</module>
```

画面 2:
```javascript
import React from 'React';

class List extends React.Component {
  render() {
    return (
      <div>
        <ul>
          <li>1</li>
          <li>2</li>
          <li>3</li>
        </ul>
        <button>点我</button>
      </div>
    );
  }
}
```

画面 3:
```javascript
import React from 'React';

class List extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      dataList: [1, 2, 3]
    };
  }

  render() {
    return (
      <div>
        <ul>
          <li>1</li>
          <li>2</li>
          <li>3</li>
        </ul>
        <button>点我</button>
      </div>
    );
  }
}
```

画面 4:
```javascript
import React from 'React';

class List extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      dataList: [1, 2, 3]
    };
  }

  render() {
    return (
      <div>
        <ul>
          {this.state.dataList.map((value, index) => {
            return <li key={index}>{value}</li>
          })}
        </ul>
        <button>点我</button>
      </div>
    );
  }
}
```

画面 5:
```javascript
import React from 'React';

class List extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      dataList: [1, 2, 3]
    };
  }

  render() {
    return (
      <div>
        <ul>
          {this.state.dataList.map((value, index) => {
            return <li key={index}>{value}</li>
          })}
        </ul>
        <button onClick={() => {
          this.setState({
            dataList: [1, 2, 3, 4]
          });
        }}>点我</button>
      </div>
    );
  }
}
```

画面 6:
```javascript
import React from 'React';

class List extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      dataList: [1, 2, 3]
    };
  }

  render() {
    return (
      <div>
        <ul>
          {this.state.dataList.map((value, index) => {
            return <li key={index}>{value}</li>
          })}
        </ul>
        <button onClick={() => {
          this.setState({
            dataList: [1, 2, 3, 4]
          });
        }}>点我</button>
      </div>
    );
  }
}
```

画面 7:
```javascript
import React from 'React';

class List extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      dataList: [1, 2, 3]
    };
  }

  render() {
    return (
      <div>
        <ul>
          {this.state.dataList.map((value, index) => {
            return <li key={index}>{value}</li>
          })}
        </ul>
        <button onClick={() => {
          this.setState({
            dataList: [1, 2, 3, 4]
          });
        }}>点我</button>
      </div>
    );
  }
}
```

画面 8:
```javascript
import React from 'React';

class List extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      dataList: [1, 2, 3]
    };
  }

  render() {
    return (
      <div>
        <ul>
          {this.state.dataList.map((value, index) => {
            return <li key={index}>{value}</li>
          })}
        </ul>
        <button onClick={() => {
          this.setState({
            dataList: [1, 2, 3, 4]
          });
        }}>点我</button>
      </div>
    );
  }
}
```

画面 9:
```javascript
import React from 'React';

class List extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      dataList: [1, 2, 3]
    };
  }

  render() {
    return (
      <div>
        <ul>
          {this.state.dataList.map((value, index) => {
            return <li key={index}>{value}</li>
          })}
        </ul>
        <button onClick={() => {
          this.setState({
            dataList: [1, 2, 3, 4]
          });
        }}>点我</button>
      </div>
    );
  }
}
```

画面 10:
```javascript
import React from 'React';

class List extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      dataList: [1, 2, 3],
      maxNum: 3
    };
  }

  render() {
    return (
      <div>
        <ul>
          {this.state.dataList.map((value, index) => {
            return <li key={index}>{value}</li>
          })}
        </ul>
        <button onClick={() => {
          let maxNum = this.state.maxNum + 1;
          let newArr = [...this.state.dataList, maxNum];
          this.setState({
            dataList: newArr,
            maxNum: maxNum
          });
        }}>点我</button>
      </div>
    );
  }
}
```

画面 11:
```javascript
import React from 'React';

class List extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      dataList: [1, 2, 3],
      maxNum: 3
    };
  }

  render() {
    return (
      <div>
        <ul>
          {this.state.dataList.map((value, index) => {
            return <li key={index}>{value}</li>
          })}
        </ul>
        <button onClick={() => {
          let maxNum = this.state.maxNum + 1;
          let newArr = [...this.state.dataList, maxNum];
          this.setState({
            dataList: newArr,
            maxNum: maxNum
          });
        }}>点我</button>
      </div>
    );
  }
}
```

画面 12:
无代码内容。

画面 13:
```javascript
import React from 'React';

class List extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      dataList: [1, 2, 3],
      maxNum: 3
    };
  }

  render() {
    return (
      <div>
        <ul>
          {

