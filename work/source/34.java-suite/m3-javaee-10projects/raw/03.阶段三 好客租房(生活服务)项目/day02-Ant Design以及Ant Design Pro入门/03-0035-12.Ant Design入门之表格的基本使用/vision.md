# 画面线理解：12.Ant Design入门之表格的基本使用

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day02-Ant Design以及Ant Design Pro入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day02-Ant Design以及Ant Design Pro入门\12.Ant Design入门之表格的基本使用【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:12, 00:37, 01:10, 01:46, 02:16, 02:41, 03:09, 03:24, 03:34, 03:54, 04:37, 05:03, 05:35, 06:54
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:20:32

1) 这一组画面整体在讲如何使用 Ant Design 的 Table 组件在 React 项目中实现数据展示与操作，包括基础用法、列配置、分页、标签渲染和数据分离等。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示 Ant Design Table 组件的代码示例，包含导入组件和定义列配置，其中一列使用自定义渲染函数。
画面 2: 展示 Table 组件的运行效果，包含 Name、Age、Address、Tags 和 Action 列，其中 Joe Black 行被选中。
画面 3: 展示 Table 组件的两种尺寸（Middle size table 和 Small size table）的渲染效果。
画面 4: 展示 Table 组件的头部分组功能，包含一个“Add a row”按钮和一个包含 name、age、address、operation 列的表格。
画面 5: 展示 Table 组件的列配置代码，定义了 name、age、address、tags 列，并对 tags 列使用自定义渲染函数。
画面 6: 展示 Table 组件的列配置代码，定义了 name、age、address、tags 列，并对 tags 列使用自定义渲染函数。
画面 7: 展示 Table 组件的代码示例，包含导入组件和定义列配置，其中一列使用自定义渲染函数。
画面 8: 展示 React 项目中 UserList.js 文件的初始代码，仅包含一个返回 <div>用户列表</div> 的 render 函数。
画面 9: 展示 UserList.js 文件中定义的数据数组和 Table 组件的初始配置，包含 pagination 属性。
画面 10: 展示 UserList.js 文件中为 Table 组件添加第一列配置，标题为“姓名”，dataIndex 为 "name"，key 为 "name"。
画面 11: 展示 UserList.js 文件中为 Table 组件添加第二列配置，标题为“年龄”，dataIndex 为 "age"，key 为 "age"。
画面 12: 展示 UserList.js 文件中为 Table 组件添加第三列配置，标题为“地址”，dataIndex 为 "address"，key 为 "address"，并添加第四列“标签”。
画面 13: 展示 UserList.js 文件中为 Table 组件添加第五列“操作”，使用自定义渲染函数，包含“编辑”和“删除”链接。
画面 14: 展示在浏览器中运行的 Table 组件效果，包含用户列表和分页控件。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```jsx
import { Table, Divider, Tag } from 'antd';

const columns = [{
  title: 'Name',
  dataIndex: 'name',
  key: 'name',
  render: text => <a href="javascript:;">{text}</a>,
}, {
  title: 'Age',
  dataIndex: 'age',
  key: 'age',
}, {
  title: 'Address',
  dataIndex: 'address',
  key: 'address',
}];
```

画面 5:
```jsx
import { Table, Divider, Tag } from 'antd';

const columns = [{
  title: 'Name',
  dataIndex: 'name',
  key: 'name',
  render: text => <a href="javascript:;">{text}</a>,
}, {
  title: 'Age',
  dataIndex: 'age',
  key: 'age',
}, {
  title: 'Address',
  dataIndex: 'address',
  key: 'address',
}, {
  title: 'Tags',
  key: 'tags',
  dataIndex: 'tags',
  render: tags => (
    <span>
      {tags.map(tag => <Tag color="blue" key={tag}>{tag}</Tag>)}
    </span>
  ),
}];
```

画面 7:
```jsx
import { Table, Divider, Tag } from 'antd';

const columns = [{
  title: 'Name',
  dataIndex: 'name',
  key: 'name',
  render: text => <a href="javascript:;">{text}</a>,
}, {
  title: 'Age',
  dataIndex: 'age',
  key: 'age',
}, {
  title: 'Address',
  dataIndex: 'address',
  key: 'address',
}];
```

画面 8:
```jsx
import React from 'react';

class UserList extends React.Component {
  render() {
    return (
      <div>用户列表</div>
    );
  }
}

export default UserList;
```

画面 9:
```jsx
const data = [{
  key: '1',
  name: '张二',
  age: 32,
  address: ['上海市', '帅气'],
  tags: ['程序员', '帅气'],
}, {
  key: '2',
  name: '李四',
  age: 42,
  address: ['北京市', '屌丝'],
  tags: ['屌丝', '富二代'],
}, {
  key: '3',
  name: '王五',
  age: 32,
  address: ['杭州市', '高富帅'],
  tags: ['高富帅', '富二代'],
}];
```

画面 10:
```jsx
class UserList extends React.Component {
  render() {
    return (
      <div>
        <Table dataSource={data} pagination={{position:"bottom",total:500,pageSize:10, defaultCurrent:1}}>
          <Column
            title="姓名"
            dataIndex="name"
            key="name"
          />
        </Table>
      </div>
    );
  }
}
```

画面 11:
```jsx
class UserList extends React.Component {
  render() {
    return (
      <div>
        <Table dataSource={data} pagination={{position:"bottom",total:500,pageSize:10, defaultCurrent:1}}>
          <Column
            title="姓名"
            dataIndex="name"
            key="name"
          />
          <Column
            title="年龄"
            dataIndex="age"
            key="age"
          />
        </Table>
      </div>
    );
  }
}
```

画面 12:
```jsx
class UserList extends React.Component {
  render() {
    return (
      <div>
        <Table dataSource={data} pagination={{position:"bottom",total:500,pageSize:10, defaultCurrent:1}}>
          <Column
            title="姓名"
            dataIndex="name"
            key="name"
          />
          <Column
            title="年龄"
            dataIndex="age"
            key="age"
          />
          <Column
            title="地址"
            dataIndex="address"
            key="address"
          />
          <Column
            title="标签"
            dataIndex="tags"
            key="tags"
            render={tags => (
              <span>
                {tags.map(tag => <Tag color="blue" key={tag}>{tag}</Tag>)}
              </span>
            )}
          />
        </Table>
      </div>
    );
  }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 14: PPT 标题为“讲义.md - Typora”，内容包含“2.4.2. 将数据分离到 model 中”，并展示了一个表格，其中包含“姓名”、“年龄”、“地址”、“标签”、“操作”列，数据行包括“张三 32 上海市 好看 编辑 删除”、“李四 42 北京市 漂亮 编辑 删除”、“王五 32 杭州市 高富帅 编辑 删除”。

5) 不要评价画面美观，不要输出与课程无关的内容。
