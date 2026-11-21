# 10.Ant Design入门之美化布局和引入导航条

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day02-Ant Design以及Ant Design Pro入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day02-Ant Design以及Ant Design Pro入门\10.Ant Design入门之美化布局和引入导航条【海量资源尽在 666java.com】.mp4
- 时长 4分48秒（音频 288s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来美化一下我们这个页面啊刚刚呢我们已经完成了我们的一个这样的一个效果对吧整个布局都已经ok了但是呢这个页面的这个样式啊有点丑啊咱们来美化一下那么这样我们先把这个代码我们先拷过来然后呢我们来看一下他做了哪些美化的一些动作啊好那么我们可以看到在这个layout中呢我们对这个sender是不是就是我们
[00:28] 左侧的这个菜单啊做了这样的一个美化指定它的一个宽度然后呢设置它的一个样式啊这个是最小的一个高度是100VH那么这个VH是什么意思呢就是指的我们可视的可视界面的一个这个高度啊就是相当于是说百分之百
[00:48] 然后我们下面可以看到头的一个信心是样式,设置的是背景色,设置为是一个白色然后是文本是做一个剧度然后padding是设置为0,内编剧为0其他的相信大家都能够看出来,也能看懂然后在下面这个尾部的话设置了一个文本的剧度然后显示的是后台系统,Crate by黑马程序员
[01:16] 好 那我们来刷新看一下页面的一个效果那么效果就是这样的一个效果其实可以看到那么我们左边这个菜单是100%去高度是占有可视窗口的100%然后上面这个头部分是一个白色的一个为底这样一个头然后是文本的剧中然后中间这个内容是将我们的一个内容做一个显示它的一个内编剧是2424的这样的一个显示的一个效果
[01:46] OK好那么这是我们这样的一个显示效果当然如果显示我们的list的话那么可以看一下list那么也是这样的一个效果对吧那么所有我们后续显示内容都会在这个里面去把它显示出来好那么然后呢我们接着继续啊我们就把这个左侧的这个导航条呢我们导进来那么我们使用这个menu作为一个组件啊来我们去找一下吧找一下这个menu啊menu呢是在
[02:16] 导航条我们来找一下在这以它为例那么我们找一个这个样式的就是这个黑色这种样式的那么你其实可以展开来看一下它里面也显示了一些它的一些代码那么我们可以把这个直接贴过来去使用那么我这样为了保证保持和我们这个讲义中一致那么我就把这个拿过来来看一下就是把我们讲义中这个代码去贴过来
[02:45] 那么我把这个内容这个靠过来这个靠一下就是我们需要在我们的页面中在我们这个布局里面找到布局吧找到这个里面然后我们再去除了这个layout之外咱们把这个menu还有这个icon这两个的引用进来这两个组件的引用进来然后我们再去把这个submenu这个我们也做一个定义下面我们会用到然后我把这个setup
[03:14] 这个靠过来其他的我们保持不变哎去哪了在这啊把这个靠过来下面的还是依然是不变把它呢就剔掉好那么然后呢我们刷新的页面来看一下效果啊那么可以看到那么这个看一下它是缺少一个啊缺少一个状态啊咱们把这个状态呢也靠过来状态里面有一个初始的一个值啊咱们把它也贴过来把它靠过来好保存
[03:48] 好那么这个呢就是我们的一个把菜单就加进来了这样的一个效果其实你可以看到和官网所看到这个效果是一样的啊是就是这样的一个效果啊不同的是呢我们上面多了一个放logo的一个位置啊后续我们会放logo啊所以这块多了一个这个logo的一个这个div放一个这个div放在这里下面就是一个menu
[04:12] menu中里面有一个menu.item就是每一个元素然后如果是有这种折叠的这种菜单的话我们把它称之为叫什么叫submenu就是子菜单子菜单下面再去包含菜单就可以了就是这样的一个效果好那么菜单我们就搞定了那么接下来其实我们要做的事情就是给菜单去添加它的每一个链接那么我们放到下一个视频我们来做一个讲解好那么关于我们
[04:42] 布局美化以及引入导航条我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Ant Design 的 Menu 组件构建一个带有侧边导航栏的 React 应用布局。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了在浏览器中运行的前端页面，包含 Tab 1、Tab 2、Tab 3 三个标签页，以及 Header 和 Footer。
画面 2: 展示了浏览器中页面的另一个视图，左侧有深色背景，顶部有 Header，底部有 Footer，页面内容区域显示“hello antd we are 第一个 tabs”。
画面 3: 展示了 Typora 编辑器中的 Markdown 文档，内容为课程大纲，当前章节为“2.3.5、引入导航条”，并显示了部分 React 代码，用于定义 BasicLayout 组件。
画面 4: 展示了 Ant Design 官网的组件文档页面，左侧是组件列表，右侧是“Layout”组件的示例，包含 Header、Sider、Content、Footer 的布局结构。
画面 5: 展示了 Ant Design 官网的“Menu”组件文档页面，演示了带子菜单的导航菜单，鼠标悬停在“Navigation One”上。
画面 6: 展示了 Typora 编辑器中的 Markdown 文档，内容为课程大纲，当前章节为“2.3.5、引入导航条”，并显示了部分 React 代码，用于引入 Menu 和 SubMenu 组件。
画面 7: 展示了 IntelliJ IDEA 中的 React 代码编辑器，显示了 BasicLayout 组件的代码，其中包含 Layout、Header、Content、Footer 的结构。
画面 8: 展示了 Typora 编辑器中的 Markdown 文档，内容为课程大纲，当前章节为“2.3.5、引入导航条”，并显示了部分 React 代码，用于引入 Menu 和 SubMenu 组件。
画面 9: 展示了 IntelliJ IDEA 中的 React 代码编辑器，显示了 BasicLayout 组件的代码，其中包含 Menu 组件的配置，如 defaultSelectedKeys、defaultOpenKeys、mode、theme、inlineCollapsed 等属性。
画面 10: 展示了 Typora 编辑器中的 Markdown 文档，内容为课程大纲，当前章节为“2.3.5、引入导航条”，并显示了部分 React 代码，用于定义 Menu 组件的子菜单结构。
画面 11: 展示了 Ant Design 官网的“Menu”组件文档页面，演示了“Menu”组件的使用，包括一个按钮用于切换菜单展开/折叠状态。
画面 12: 展示了 IntelliJ IDEA 中的 React 代码编辑器，显示了 BasicLayout 组件的代码，其中包含 Menu 组件的子菜单结构，包括多个 Menu.Item 和 SubMenu。
画面 13: 展示了 Typora 编辑器中的 Markdown 文档，内容为课程大纲，当前章节为“2.3.5、引入导航条”，并显示了部分 React 代码，用于定义 BasicLayout 组件的构造函数。
画面 14: 展示了 Typora 编辑器中的 Markdown 文档，内容为课程大纲，当前章节为“2.3.5、引入导航条”，并显示了部分 React 代码，用于定义 BasicLayout 组件的构造函数。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面 3:
```jsx
import React from 'React';
import { Layout } from 'antd';

const { Header, Footer, Sider, Content } = Layout;

class BasicLayout extends React.Component {
  render() {
    return (
      <Layout>
        <Sider width={256} style={{ minHeight: '100vh', color: 'white' }}>
        </Sider>
        <Layout>
          <Header style={{ background: '#fff', textAlign: 'center', padding: 0 }}>
          </Header>
          <Content style={{ margin: '24px 16px 0', background: '#fff', minHeight: 360 }}>
            {this.props.children}
          </Content>
          <Footer style={{ textAlign: 'center' }}>后台系统 ©2018 Created by 黑马程序员</Footer>
        </Layout>
      </Layout>
    );
  }
}

export default BasicLayout;
```

画面 6:
```jsx
import React from 'React';
import { Layout, Menu, Icon } from 'antd';

const { Header, Footer, Sider, Content } = Layout;
const SubMenu = Menu.SubMenu;

class BasicLayout extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      collapsed: false,
    };
  }
```

画面 7:
```jsx
import React from 'React';
import { Layout } from 'antd';

const { Header, Footer, Sider, Content } = Layout;

class BasicLayout extends React.Component {
  render() {
    return (
      <Layout>
        <Sider width={256} style={{ minHeight: '100vh', color: 'white' }}>
        </Sider>
        <Layout>
          <Header style={{ background: '#fff', textAlign: 'center', padding: 0 }}>
          </Header>
          <Content style={{ margin: '24px 16px 0', background: '#fff', minHeight: 360 }}>
            {this.props.children}
          </Content>
          <Footer style={{ textAlign: 'center' }}>后台系统 ©2018 Created by 黑马程序员</Footer>
        </Layout>
      </Layout>
    );
  }
}

export default BasicLayout;
```

画面 9:
```jsx
import React from 'React';
import { Layout, Menu, Icon } from 'antd';

const { Header, Footer, Sider, Content } = Layout;
const SubMenu = Menu.SubMenu;

class BasicLayout extends React.Component {
  render() {
    return (
      <Layout>
        <Sider width={256} style={{ minHeight: '100vh', color: 'white' }}>
        </Sider>
        <Layout>
          <Header style={{ background: '#fff', textAlign: 'center', padding: 0 }}>
          </Header>
          <Content style={{ margin: '24px 16px 0', background: '#fff', minHeight: 360 }}>
            {this.props.children}
          </Content>
          <Footer style={{ textAlign: 'center' }}>后台系统 ©2018 Created by 黑马程序员</Footer>
        </Layout>
      </Layout>
    );
  }
}

export default BasicLayout;
```

画面 10:
```jsx
import React from 'React';
import { Layout, Menu, Icon } from 'antd';

const { Header, Footer, Sider, Content } = Layout;
const SubMenu = Menu.SubMenu;

class BasicLayout extends React.Component {
  render() {
    return (
      <Layout>
        <Sider width={256} style={{ minHeight: '100vh', color: 'white' }}>
        </Sider>
        <Layout>
          <Header style={{ background: '#fff', textAlign: 'center', padding: 0 }}>
          </Header>
          <Content style={{ margin: '24px 16px 0', background: '#fff', minHeight: 360 }}>
            {this.props.children}
          </Content>
          <Footer style={{ textAlign: 'center' }}>后台系统 ©2018 Created by 黑马程序员</Footer>
        </Layout>
      </Layout>
    );
  }
}

export default BasicLayout;
```

画面 12:
```jsx
import React from 'React';
import { Layout, Menu, Icon } from 'antd';

const { Header, Footer, Sider, Content } = Layout;
const SubMenu = Menu.SubMenu;

class BasicLayout extends React.Component {
  render() {
    return (
      <Layout>
        <Sider width={256} style={{ minHeight: '100vh', color: 'white' }}>
        </Sider>
        <Layout>
          <Header style={{ background: '#fff', textAlign: 'center', padding: 0 }}>
          </Header>
          <Content style={{ margin: '24px 16px 0', background: '#fff', minHeight: 360 }}>
            {this.props.children}
          </Content>
          <Footer style={{ textAlign: 'center' }}>后台系统 ©2018 Created by 黑马程序员</Footer>
        </Layout>
      </Layout>
    );
  }
}

export default BasicLayout;
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 3: PPT 标题为“2.3.5、引入导航条”，内容为课程大纲。
画面 6: PPT 标题为“2.3.5、引入导航条”，内容为课程大纲。
画面 13: PPT 标题为“2.3.5、引入导航条”，内容为课程大纲。
画面 14: PPT 标题为“2.3.5、引入导航条”，内容为课程大纲。

5) 无。

