# 画面线理解：04.ReactJS入门之dva的使用（实现点击事件）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day02-Ant Design以及Ant Design Pro入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day02-Ant Design以及Ant Design Pro入门\04.ReactJS入门之dva的使用（实现点击事件）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:40, 02:55, 04:34, 07:59, 09:44, 10:50, 12:36, 14:45, 15:27, 15:58, 17:04, 18:56, 20:05
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:15:35

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
import React from 'react';
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
