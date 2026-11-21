# 12.Ant Design入门之表格的基本使用

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day02-Ant Design以及Ant Design Pro入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day02-Ant Design以及Ant Design Pro入门\12.Ant Design入门之表格的基本使用【海量资源尽在 666java.com】.mp4
- 时长 7分9秒（音频 429s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下这个表格那么表格呢是在我们后台系统中做开发的时候用的非常多的这样的一个组件那么我们来看一下官方的这个文档啊官方这个文档叫表格表格呢它展示的就是行列的数据啊这个当然是这样的那么不必过多的太多太多说啊
[00:23] 那么官方呢给我们写了这样的一个示例啊你看是不是就这样的一个示例啊那么我们就拿这种最简单的示例呢我们先把它先用起来啊后面我们再去看一下它其他一些效果包括你可以看到哎它还有这样的一个效果就是将我们的这个这个列啊做一个这个合并啊然后呢还有呢像这种就是可选择的这种效果这种效果我们在做项目的时候是不是也有这种需求啊
[00:51] 包括还有这种分页这种效果然后呢你可以看到下面这种的是带这种排序的和这种筛选的还有这种筛选这种的一些这个表格功能还是比较强大的像这种叫远程加载数据就是通过阿亚克斯去获取数据的等等大家可以去自己可以去看一下它的功能还是非常丰富的
[01:15] 包括呢可以有看这种有这种什么呢就是带这种折叠的这种功能的这种表格对吧哎呀OK然后呢这种呢是可以固定一个表头啊把这个表头固定下来然后呢我们这样去下拉所以可以看到功能是非常的丰富啊然后呢这个是固定这个列固定某一个列比如说前面这两个列和最后一个列固定那中间这个内容呢可以去用个滚动条去拉
[01:42] 然后呢OK反正很多了这个我们就不一一去看了你可以看到在右侧这个里面是不是有非常多的它这种用法那么我们就采用它最基本的用法来看一下那么怎么去用呢那么我们看一下它怎么样能够实现这样的效果呢还是来看一下它右侧这个位置是不是有个show code就是它一个代码那么我们可以看到在这个代码中呢它首先导入的是一些这个table
[02:10] 一些相关的一些这个组件导入进来然后呢在这定义了一个columns就是说我们这个表格它有哪些列它有哪些列然后呢再去定义了这个什么呢就是这个对于tags因为tags这一块它有一些这个格式化的一些输出所以呢在这个位置它有一个render一个格式化的一个输出然后呢我们去render去做一个显示
[02:36] 这个是Action就是后面的这个按钮的一个这样的一个显示然后我们整个页面整个页面的一个输出去引入这个表格的话是不是通过这个table这个组件然后就可以把它引入进来了然后指定它这个datasourcedatasource就是它的数据源数据源来源于上面这个data
[02:58] 电影的这样的一个数据那么最后就可以看到有这样的一个效果那么OK那么我们基于官方的这个最基本的这个案例呢我们自己来写我们的一个这个页面啊那我们呢还是把我们的这刚刚这个写的user list这个页面我们做一个改造啊那这样我就直接把这个页面我就把这个代码我就贴过来我们来看一下啊找到我们这个user list
[03:24] 然后我们把它贴过来来看一下那么在这个里面我们写了哪些内容就是我们定义了一个数据就是我们有三条数据有这个123张三里是王虎然后所在的地址然后他有一个标签一个是程序员帅气然后是屌丝李斯是屌丝然后王虎是高富帅富二代大概写了这样的一个数据然后下面我们在这个rounder这个里面我们去怼称了
[03:52] 一个DIV这个里面包含了我们的一个表格那么这个表格中的首先指定它的一个这个Data Source然后呢我们可以看到在这个里面是不是就指定它的一个分页分页的一个情况就是说它的显示的位置在这个下面然后总的这个数据的条数是500条每一页显示10条然后呢目前当前的页是第三页
[04:21] 那么大概呢就是给他设置了一个分件的一个效果那么大家其实可以看到当我们这样可以设置分件效果的话那么我们后面去做成一些真实的一些表格的话这个是不是就会去做了然后呢我们去指定每一列每一列的一个情况比如说你第一列那对应的是名字对吧那么他有一个
[04:41] Data index名字那么然后还有key名字那么要注意的是我们写的Data index它是需要跟我们的去做一个对应的ok好然后年龄这个年龄地址标签那么在标签的位置要注意的是
[05:03] 标签呢我们由于我们显示的是一个我们提供的数据啊它是一个素组所以呢我们需要对这个素组的做一个便利然后呢去显示出这个标签用一个这个blur就是一个蓝色的一个标签把它显示出来然后呢下面还有些操作啊操作就是一个编辑一个删除我们现在呢先给它一个就是一个空的一个这个链接啊然后呢这个位置呢有
[05:29] 给大家显示一个这个叫分割线一会儿我们看一下效果大家就明白了然后呢我们进入到我们这个页面来看一下效果我们进入到这个里面来有一个叫做用户用户列表刷新但是呢可以发现现在OK了刚刚的样子有点问题没有刷新的缘故那么现在我们可以看到这就是我们的一个表格是不是已经显示出来了对吧
[05:53] 包括我们这个数据三条数据没有问题然后标签的一个格式化显示是不是也没有问题包括你可以看到后面这个操作按钮的这个操作是不是也没有问题只是我们现在过程都没有实现然后我们要想说的一个就在这这个是我们的一个分页分页其实我们可以看到
[06:12] 刚刚呢我们在我们去设置这个代码的时候是不是也设置了一些分页的一些参数那么我们可以看到最终它这个分页是不是显示出来的效果就这样的一个效果那么当前显示是第三页啊选动第三页然后呢总页数呢是有500条数据然后呢每页是不是显示10条那就是50条那么我们可以点击这个下一页啊看这个效果啊那么它是不是也把这个分页这个效果是不是也给我们集成进来了
[06:39] 所以说这个UI基本上把一些能做的功能都帮我们做好了我们只需要为它提供这种数据包括这种定义设置一些参数就可以了OK好那么我们现在这个表格是不是就已经就搞定了对吧好那么这样我们就先把这个表格的表格的这个使用我们就先讲到这里那么下面我们再去讲这种数据和我们表格的一个分离好那我们表格的基本的用法就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
import React from 'React';

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

