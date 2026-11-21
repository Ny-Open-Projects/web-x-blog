# 09.Ant Design入门之布局

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day02-Ant Design以及Ant Design Pro入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day02-Ant Design以及Ant Design Pro入门\09.Ant Design入门之布局【海量资源尽在 666java.com】.mp4
- 时长 13分19秒（音频 799s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下布局布局呢是指我们整个这个网页的一个布局啊那么布局呢其实我们在做前端开发的时候用的还是比较多的啊所以呢我们来一起来看一下这个布局啊这个知识那么首先呢我们先来看一下官方的这个文档啊在这个文档中呢
[00:23] 他呢关于这个layout布局呢也讲了一些东西啊包括他的一些设计的规则啊尺寸啊交互啊视觉啊等等那么这个呢我们就不带大家也一点一点去读了啊那么大家可以自己去阅读一下好那么我们接着来继续往下面看那么往往我们在做后台系统设计的时候啊那么我们通常呢都是把它设计为三部分这样一个布局那么一般呢就是在左边这块是一些菜单
[00:53] 然后呢上边的是我们的一些投信息然后呢中间的这一块呢是我们的一些这个显示的主要的一些这个页面啊然后呢当然了有一些这个系统呢还会设置下面的一个尾部信息那么这块信息呢会显示一些这个我们的一些公司的版权呢还有我们的一些系统的版本信息啊
[01:14] 可能会显示在这个位置啊哎OK好这是我们比较常见的一种这个布局的形式那么下面呢我们就通过我们这个按着底站呢我们来去实现啊这样的一个布局好那么下面我们来看一下它的一个整体做一个布局怎么做呢呃关于这个组布局的组件呢我们回过头来我们再来看啊
[01:35] 那么首先我们在我们的SRC目录下面创建一个目录叫做layouts那么注意这个它也是UMI这个框架所约定的一个目录这个目录所存放的就是一些我们的布局的一些文件好然后我们在这个目录下面创建一个index.js文件要注意的是一旦你这个文件的创建那么就意味着这个index.
[02:03] JS文件将是我们整个这个项目的一个全局的一个布局或者说它或者是一个基础的一个布局
[02:11] 好然后呢我们来看一下这个布局怎么样去写那么我们是不是还是要参考这个官方这个文档那么我们继续往下面看在官方我们可以看到它下面是不是有一个代码的演示那么你看这是它第一个这个演示对吧上中下这样的一个布局然后呢这个是什么呢上啊然后呢有这个菜单有一个这个内容呀还有一个footer那么ok呃这种结构是不是更符合我们的一些这个做后台系统啊
[02:40] 对吧更符合是这样的一个后台系统那么所以我们是不是可以参考什么呢其实像下面的这个我们继续往下面看像这个是不是更符合一点对吧更符合一点因为它左边的这个左边的这个菜单这个部分是不是就是独立的一块对吧独立的一块然后右边这一块再去设置它的头内容一些内容OK好
[03:06] 那么我们来看一下这个其实你随意你可以用这个也可以用这个这个是都可以的好那么我们来看一下它的一些代码点开来看一下那么代码我们来找到你可以看到这个是它前面的第一个布局对吧然后这个是第二个第三个这个第四个好那么咱们这边就可以采用第四个布局作为我们的一个基础的一个布局
[03:32] 那么这个布局应该怎么去写呢我们来看一下那么我们就在这个位置去写一个我们的一个基础的一个布局那么首先呢导入谁呢导入reactorfrom啊from谁呢是不是reactor啊reactor然后导入完成之后呢我们写一个类叫做什么呢叫basic啊basic layout啊layout那么什么叫basic layout呢
[04:04] 其实就是我们那个基础的一个布局对不对然后呢我们去继承谁呢是不是继承一个React的点什么的comment然后呢我们再继续往下面写这个位置我们写一个什么的export啊export然后呢写一个default叫做basic layout这是我们的基础的一个布局然后呢我们继续往下面去写这个位置写一个render这个方法渲染这个方法
[04:32] 这个写的内容呢格式啊还是跟我们之前写的格式都是一样的啊那么我们来参考一下官网它的一些写法啊你看首先这个位置是我们导入一个layout来把它拷过来是不是导入一个就放到这吧导入一个layout然后呢下面呢我们是要定义它的一些这个什么hinder啊forter啊conductor啊setter啊对吧一些这个组件那么咱们把它导出来定义一下
[05:01] 然后呢我们来看一下接下来呢我们就需要在我们的这个run的这个方法中是不是我们把这个是不是拷过来对吧这个呢是一个叫JSX的这样的一个语法那么把它拷过来这样是不是就产生了我们的一个布局啊好那么我们接下来呢这个是不是就已经是搞定了那么我们下面是不是就可以去尝试的去查看一下我们的这个布局它有没有生效呢来看一下效果
[05:30] 那么我们进入这个里面来那么我们随意点一个吧比如说叫mytips那么我们的这个布局是不是并没有生效啊对吧并没有生效那怎么办呢那我们来重启一下啊重启一下把这个服务呢重启一下然后呢control c给它结束掉好然后呢我们再来启动我们的这个服务那我们来看一下效果啊
[05:54] 好那么我们看到它已经启动成功了来看一下效果那么在我们的页面中已经可以看到是不是有这样的一个效果那么是不是这个布局基本上是已经是OK了但是我们这个样子是不是长的是有点丑那么一会我们来去把它去调整一下那么它整个就比较好看一些了好那么接下来我们就来看一下我们的讲义那么我们首先来看一下它个组件的一个
[06:22] 刚刚我们就写了一个最基本的布局然后我们就可以看到一个这样的一个效果那么我们来对照这个组件的一个概述我们一起来看一下这个layout它就是一个布局的容器那么在这个容器下面它可以去设置一些什么hider,saddle,conductor等一些这种布局的一些对象对吧它可以放在任何的附容器中
[06:50] 那么下面这个像这个Handle你看这个Handle它呢是属于顶部的布局自带的默认样式可以下面可以嵌套任何的元素只能放在Layout中那么你看它是不是只能放在这个Layout里面来这个Center也左边的这个侧边栏是不是也是一样对吧Conduct内容部分Folder是我们底部部分放在这个Layout中那么所以呢我们往往的布局呢就是通过这么几部分
[07:20] 这么几部分去组成的好那么刚刚我们是不是已经参考了官方的一个它的布局的一个文档然后去我们自己写了一个叫basic这样的layout对吧那么已经ok写好了需要给大家特别说明的一点是在vumi这个框架中我们约定的目录中就是layout是下面的index.js文件
[07:45] 他呢将被作为全局的一个布局文件啊OK那么下面呢我们后面也会看到他的一个效果啊那么我们在讲义中呢写了一个内容叫做接下来我们配置一个路由啊那么要注意的是那么我们先来看这个路由吧那么这个路由的配置呢是这样的在我们config.js文件中配置了一个pass斜杠然后呢我们指定的comment是我们的点点斜杠中的layouts其实找的就是我们这个
[08:12] 这个文件对不对OK那我们对这个路由的意思是什么意思呢就是说
[08:17] 如果你需要去自己去定义啊去定义或者说去指定这个路由方式的话那么就配置这样的一个路由如果你不配置那么就代表了什么呢我们采用这个污名给我们提供的一个默认的一个路由那么OK那么我们再到这选择就不做一个配置了啊不做配置了那么一会儿我们要想配置也可以去配置一下啊这个我们都行啊都可以的好那么我们接着继续往下面看
[08:45] 那么我们尝试的去访问一下其他页面比如说像这个mytips还有我们前面写这个listlist这个页面那么大家可以发现无论我们访问哪个页面那么它都是显示这样的一个效果是不是其实就验证了我们前面所说的这一点就是怎么呢这个layouts下面的index.js文件作为全局的一个布局文件也就是说
[09:11] 无论你访问哪个页面那么他都会显示的是我们对各布局中的这样的内容对不对但是大家想一想那么这显然是不合理的对不对那么我写我我访问我这个mytips那么我本意是不是就是需要显示我这个mytips的内容但是呢我又希望我这个mytips要
[09:34] 他有一个外部的一个怎么外部的一个这个布局是不是采用我们这个前级的布局啊那么也就是说我们需要在这contact的这个内容部分显示出我们每个页面啊不同的一些页面的一些内容啊那么这样的效果那么应该怎么做呢来看一下那么接下来呢我们就需要去调整一下我们的布局文件在布局文件中呢要注意的是这contact内容呢你不能写死注意这个地方是不能写死的
[10:03] 这个地方怎么写要注意了那么这个地方我们要通过一个什么呢通过我们的一个解释代码就写一个什么呢race.props.什么呢有个trojan这个相信大家的并不陌生啊并不陌生就是我们通过我们这个props中的这个trojan就可以去把我们这个页面中的整个这个内容作为了一个
[10:31] 它的一个子页面然后呢在这个布局中给它显示出来好那我们来看一下效果ok一刷新啊这个效果就出来了你可以看到这个是不是就是我们那个mytips那么外面这个布局是不是依然还是存在那么我们可以访问一下我们这个list这个页面看一下
[10:50] 那么依然是不是也是OK的到我们点点我是不是没有任何问题OK这样的话其实我们就完成了一个效果就是我们只要定义了我们整个系统中的一个布局那么我们只需要去编写我们里面的一些其他的页面那么它就会直接加入到我们这个布局中那这样的话我们是不是只要写这个不同组件就可以了
[11:11] 所有的这个组装这个过程是不是交由我们这个污秘这个框架来完成啊哎OK好没错是这样的所以这个呢就是我们所讲的这个此页面的一个使用的布局那么我们把我们的这个布局文件中的contact内容的替换成类似点props中的这个trojan那么就可以去反显示出我们不同页面中的一些啊
[11:33] 不同页面中的一些这个效果当然了如果你选择手动配置路由的话那么我们就需要在我们这个下面去添加一个什么的realtors然后再去配置我们的mytabs等等那么这个就属于手动的一个配置如果你觉得你自己有必要手动配置那么就配置如果没有必要手动配置的话那么就按照UMI它官方所给我们的一个
[12:00] 这样的一个默认的一个请求路由方式进行请求就可以了啊这两种方式都行啊这个大家可以自由选择啊那么为了不混淆大家呢那么我在这呢再写一句话去给大家去说明一下啊说明那么下面的这个路由配置啊下面这个路由配置呢是表明啊表明什么啊是表明你需要啊你需要
[12:29] 通过手动配置的方式进行访问我们这个页面对吧而什么呢不采用这个5米5米这个默认的这种方式默认的路由方式路由方式这个大家一定要注意路由方式好那么这个呢我给大家去注意一下OK
[12:56] 好那么当然了上面我们所讲的这个呢它道理呢也是一样的啊也是一样的所以我们在那加一个加一个备注或者说明吧就是非必须啊这个千万大家别搞错了啊非必须好那么如果你需要手动那就手动配置如果不手动配置的话那就采用默认啊OK好那么OK这个我们是不是就搞定了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Ant Design Pro 的 Layout 组件构建后台管理系统经典三部分布局，并集成 TabPane 组件实现页面切换。

2) 按时间顺序列出每张画面的要点：
画面1：介绍 Ant Design 布局组件，展示 Header、Sider、Content、Footer 四部分结构图。
画面2：展示项目配置文件 config.js，其中 plugins 配置了 'umi-plugin-React' 并启用了 antd。
画面3：在 Ant Design 官网查看 Layout 组件的组件描述和代码演示。
画面4：在官网展示 Layout 组件的多种布局方式（Header-Sider-Content-Footer、Content-Sider-Footer、Sider-Header-Content）。
画面5：在 IDE 中打开 layouts/index.js 文件，准备编写布局代码。
画面6：在 IDE 中编辑 index.js，开始编写 BasicLayout 组件的类定义。
画面7：在 IDE 中编写 BasicLayout 组件的 render 方法，使用 Layout 组件包裹 Header、Content、Footer。
画面8：在终端看到 Webpack 编译成功，并显示应用运行在 http://localhost:8000。
画面9：在 IDE 中修改 BasicLayout 组件，将 Header、Content、Footer 作为 Layout 的子元素。
画面10：在浏览器中访问 http://localhost:8000/，显示 Header、Sider、Footer，Content 区域为空。
画面11：在 IDE 中打开 pages/MyTabs.js 文件，编写使用 Tabs 组件的 MyTabs 组件。
画面12：在 IDE 中切换到 layouts/index.js，准备在 BasicLayout 中嵌入 MyTabs 组件。
画面13：在 Typora 文档中展示配置文件，配置 routes 以使用 MyTabs 组件。
画面14：在 Typora 文档中展示访问 http://localhost:8000/myTabs 后页面效果，并介绍美化页面。

3) 出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面2：
```javascript
export default {
  plugins: [
    'umi-plugin-React', {
      // 暂时不启用任何功能
      dva: true, // 开启了 dva 功能,
      antd: true
    }
  ]
}
```

画面5：
```javascript
import React from 'React';
```

画面6：
```javascript
export
exports (index.d.ts, node) any
external (lib.dom.d.ts) External
EXT frag_depth (lib.dom.d.ts)
executor(resolve: (value?: PromiseLike< void
expectedClass (... args: any) 'T
expirationTime
EXT texture_filter anisotropic (lib.dom.d.ts.
ExtendableEvent (lib.webworker.d.ts)
ExtendableMessageEvent (lib.webworker.d.ts)
```

画面7：
```javascript
import React from 'React';
import [Layout] from 'antd';
const (Header, Footer, Sider, Content) = Layout;
class BasicLayout extends React.Component {
  render() {
    return (
      <Layout>
        <Sider>Sider</Sider>
        <Layout>
          <Header>Header</Header>
          <Content>Content</Content>
          <Footer>Footer</Footer>
        </Layout>
      </Layout>
    )
  }
}
export default BasicLayout;
```

画面8：
```text
Compiling
success webpack compiled in 7s 525ms
DONE Compiled successfully in 703ms
App running at:
- Local: http://localhost:8000/ (copied to clipboard)
- Network: http://172.16.55.244:8000/
```

画面9：
```javascript
<Header>Header</Header>
<Content>Content</Content>
<Footer>Footer</Footer>
```

画面11：
```javascript
import React from 'React';
import [Tabs] from 'antd'; // 第一步，导入需要使用的组件
function callback(key) {
  console.log(key);
}
class MyTabs extends React.Component{
  render() {
    return (
      <Tabs defaultActiveKey="1" onChange={callback}>
        <TabPane tab="Tab 1" key="1">hello antd wo de 第一个 tab</TabPane>
        <TabPane tab="Tab 2" key="2">Content of Tab Pane 2</TabPane>
        <TabPane tab="Tab 3" key="3">Content of Tab Pane 3</TabPane>
      </Tabs>
    )
  }
}
export default MyTabs;
```

画面13：
```javascript
export default {
  plugins: [
    'umi-plugin-React', {
      dva: true, // 开启 dva 功能
      antd: true // 开启 Ant Design 功能
    }
  ],
  routes: [
    {
      path: '/',
      component: '../layouts',
      routes: [
        {
          path: '/myTabs',
          component: './myTabs'
        }
      ]
    }
  ]
}
```

4) 出现的 PPT 标题、架构图/流程图的结构、表格数据：
画面1：标题为“2.3、布局”，图示中 Header 指向 Layout，Sider 指向 Layout，Content 指向 Layout，Footer 指向 Layout。
画面3：标题为“组件描述”，内容为：
- Header：顶部容器，自带默认样式，其下可嵌套任何元素，只能放在 Layout 中。
- Sider：侧边栏，自带默认样式，其下可嵌套任何元素，只能放在 Layout 中。
- Content：内容容器，自带默认样式，其下可嵌套任何元素，只能放在 Layout 中。
- Footer：底部容器，自带默认样式，其下可嵌套任何元素，只能放在 Layout 中。
画面4：展示 Layout 组件的三种布局结构。
画面14：标题为“2.3.4、美化页面”，图示中展示了 TabPane 组件的使用。

5) 无。

