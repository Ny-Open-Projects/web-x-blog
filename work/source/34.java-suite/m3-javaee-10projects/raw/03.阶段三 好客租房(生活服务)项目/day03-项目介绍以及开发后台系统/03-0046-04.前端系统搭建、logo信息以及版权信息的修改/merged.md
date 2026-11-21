# 04.前端系统搭建、logo信息以及版权信息的修改

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day03-项目介绍以及开发后台系统
- 源文件：03.阶段三 好客租房(生活服务)项目\day03-项目介绍以及开发后台系统\04.前端系统搭建、logo信息以及版权信息的修改【海量资源尽在 ubkz.com】.mp4
- 时长 13分1秒（音频 781s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下我们的后台系统的搭建啊那么后台系统呢我们依然采用的是当前比较流行的这种开发模式什么开发模式呢前后端分离那么什么叫做前后端分离呢我们来看一下那么前后端的是指那么假设呢这个是我的前端这个团队那么这个呢是我的后端这个团队
[00:28] 那么前后端做一个分离就是说我有两个团队那么两个团队呢同时去做这个项目的开发那么这个呢是我的一个时间轴这是我的一个时间轴往下面走那么前后端做分离呢也就是说同样的时间轴那么前后端两个团队是并行做一个开发那么他们之间的这个接口的调用或者连条怎么做呢
[00:55] 来看一下那么前端这个团队他们在开发的过程中后端这个团队是不是也在开发那么他想要去调用后台系统所提供的接口那么这个时候呢能不能调到他其实是调不到的为什么呢因为后台系统是还没有开发好对不对没有开发好那么后台这个时候怎么办呢我们是不是前面也讲过一个方式叫什么呢默克对不对
[01:21] 那么在前台这个系统中他只需要自己去模拟啊这样的一个实现是不是就可以了对吧那么什么时候可以做真正的连条呢哎等到我们的后台系统把这个接口开发好之后那么我是不是就可以去做一个连条了哎OK啊他是这样的开发模式这种开发模式模式呢最大的好处呢就是前后端的互不影响并且呢他们是做一个并行的开发这样开发效率呢是比较高的啊哎OK
[01:51] 好 那么我们来看一下在前端这个系统中我们采用了pro这个系统作为我们的一个模板系统作为改造而我们的后端主要是以这个sprint boot加这个double为我们的主要的一个架构来实现我们后台的服务的一个提供当然了我们还使用了像sprintmvc以及mybasics这样的一些框架ok好 那么继续往下面看那么首先我们先来搭建我们的前端
[02:20] 这个系统啊前端系统那么我们根据前面我们所学习的pro的一些入门的一些知识呢再参考我们的这两个文档啊这两个文档那么一个是我们的PRD一个呢就是我们的一个产品的一个原型这样的一个文档然后呢我们将我们这个后台系统页面呢做一些这个改造咱们把它改造出来OK好那么我们根据这个
[02:44] 讲义的步骤咱们一步一步的把它去创建一下那么也希望大家也按照这个步骤一步一步的来那么首先我们先找到先找到我们的相关的一些资料这个资料在哪里是在我们的开发环境相关的是在外面这个里面在我们资料目录下面有一个叫做ITcast浩克
[03:09] manager然后呢一个web.zip啊这个文件那么我们把这个文件我们去打开然后呢把这个目录解压到什么呢解压到我们的这个code下面啊在我code下面呢有一个叫itcast浩克这个目录我把它解压到这个里面来那么这个文档资料中的这个文档呢或者说资料中的一些这种资料
[03:35] 资料文件大家也都会拿到的这样的资料的好然后我把它导入到我的文件夹里面那么导入进来之后我就需要把它导入到我的idea开发工具中那么我打开我的idea然后在这个位置是不是点击一个import projector然后我们选中它然后点击ok然后我们选中上面它下一步然后下一步
[04:02] 然后呢然后呢我们点击这个下一步等待他的一个扫描完成之后啊然后呢我们点击这个非禁止完成那么就会把这个项目呢是不是就导入进来了那么导入这个项目呢是指仅仅是把我们的一些原码是不是导入进来那么我们还没有去给他添加一些依赖对不对所以接下来我们就需要给他去执行一些相关的一些命令然后呢去导入一些他所需要的依赖
[04:31] 那么我们通过导入的命令是不是这个t yarn然后 install去做一个安装然后即可以导入它的一些相关的依赖然后我们通过这个t yarn然后start就可以启动这个服务好那我们来做一个操作那我们进入这个项目然后在这个位置打开我们的控制台然后我们就输入一个什么的t yarn然后 install等待它的一个安装敲错了varn install
[05:04] 然后我们等待它的一个安装你看它对我们这个package去做一个解析然后去导入那么总共有2306个那么我们就稍等一下那么我现在把这个视频先暂停一下好那么我们可以看到现在已经E-Store完成了就是已经把相关的一些依赖都已经导入进来了在这个位置有一个叫做Node Modules这个里面有好多的依赖OK
[05:34] 好那么下面呢我们就来继续往下面走那么下面我们去输入这个t yarn start来启动我们这个系统然后呢我们在这个位置来输入一下start然后呢去启动我们这个系统那么启动之后呢它就会打开浏览器访问到我们这个页面啊我们一起来看一下那么等待它的一个启动稍微有一点点慢
[06:05] 那这样然后呢我依然的是把视频呢先暂停一下启动起来之后呢咱们再继续好那么我们看到呢已经启动完成了并且呢它已经打开了我们这个浏览器我们来看一下这个效果那么这个效果呢大家应该是比较熟悉的对吧看到这个它默认了有一个desktop的这个页面不过呢我们可以看到在上面这个部分呢我已经对它做了一个修改
[06:33] 包括他已经有了这个房源管理对吧有一个叫新增房源对吧有这样的一个效果还有呢叫房源管理然后呢有什么看房请求啊等等一些这个菜单呢已经都添加好了哎OK好那么我们接着后面我们会讲这个内容啊那我们接着继续啊
[06:52] 那么下面呢我们来看一下那么在我们这个菜单的上面大家有没有发现啊这个logo这个部分呢已经被我们修改成这个浩克租房然后呢管理系统啊那么改成这样的一个logo那么我们已经把它默认的一个logo已经改掉了对吧那么下面我们就来探讨一下这个logo它究竟是在哪个位置去做一个修改那么这个呢我们主要是以这个讲解部分为例啊那我们来看一下
[07:21] 包括以及一些这个版本信息大家可以观察到在我们下面这个位置我们已经把他这个版本信息呢也改掉了那我们就来看一下这两个内容呢究竟是在哪个位置去做一个修改那么我们找一下啊前面我们其实说过整个呢他是不是有一个布局的页面对吧那我们想要找到这个位置是不是要去找到他的布局的页面啊那我们找到
[07:47] 在这个src这个下面是不是有一个叫做layout然后在这个layout下面是不是有叫basic layout还记得这个文件吗我们打开来看一下那么在这个里面我们switch一下要不然他会报错你看他说是要切换到这个切换这个语言切换谁呢是不是React js gxx这种语言那我们点击这个切换那么这样的话他就没有这个编译这个报错了
[08:13] 这个工具一个提示的一个错误好那么我们先不管他啊让他去慢慢切换我们继续往下面看那么我们找到下面呢会有一个runner是吧那么你看是不是在这runner这个方法然后呢有一个return啊有个return在这那我们其实可以看到呢他呢是不是通过哎在上面吧啊在上面这个位置啊在这他定义了一个layout对吧下面用到了这个这个layout我们来看一下
[08:43] 那么在这个layout中他定义了一个layout然后我们继续往下面看那么我们找到在这个位置在这个位置他是不是有一个叫做center一个menu对吧通过他你看这是不是有个logo等于这个括号一个logo那么这个center menu是谁我们其实可以去找一下点一下他按住control去点一下点一下我们会发现他是一个导入一个center的一个menu
[09:13] 但是呢这个send这个menu它并不是并不是我们这个pro或者并不是这个按的design说提供的一个UI而是自己写的一个UI那么前面我们在讲这个pro项目的时候呢也提到过是不是在这个目录下面comments这个目录下面都是放的一些公用的一些这个UI组件对吧那我们可以看到它呢是不是就是一个自定义的一个组件好那我们来找一下
[09:40] 那么在这comments下面找到这个send menu那么我们找到它是不是有个send menu看到了吗是不是在这个位置那么在这个位置下面由于它后面是没有写什么什么json那么它默认找的是不是就这个index.js文件那么我们打开来看一下在这个index.js文件中那么最后我们来看它return这个位置return是不是它用的是send menu对吧send menu
[10:07] 然后呢我们可以看到最后返回的是不是就是这样的一个内容啊对吧那我们来看一下这个这个send menu那么究竟是谁呢我们找一下点一下他那么我们点击进来呢会发现是不是在这个位置他定义了一个这个send menu对吧send menu那么我们来找一下他的一个这个logo在哪呢我们找一下啊那么其实我们往下面找找到在下面的这个位置是不是有一个DIV
[10:36] 那么在这个DIV里面我们可以看到是不是在这个位置是不是有一个H1的一个标签是不是写了一个浩克租房管理系统那么是不是通过这个位置就已经修改完成我们的一个logo那么也就是说
[10:51] 那么我们讲这个的意思就是告诉大家我们如何去在一个模板系统上面去根据我们自己的一个需求去做一个改造那么我们是不是根据重复一下那么根据我们这个layout对吧根据我们basic layout找到我们上面发现他引用的是一个叫做send menu往下面找找到是不是在这个位置是不是send menu
[11:16] 那么在send menu他引入的是comments下面的一个send menu那我们找到这个下面是不是有一个send menu找到他然后在这个里面他是不是有个returnreturn的这个sender然后在这个位置是不是有个div去放了我们这个logo那么这样的话我们是不是就找到了ok好那我们来看一下这个讲义他是不是也是这么说的那么在这个basic layout中是不是有一个这样的一个定义对吧然后我们就打开它发现在这个位置对吧
[11:43] 好 那我们来看一下那么在底部的我们的这个页面的版本信息在哪呢那么同样的方法是不是要找到我们这个布局文件找到layout basic这个layout那么layout下面的我们还是找到最下面去最tun的这个位置那么显然的我们可以看到它是不是在这个位置有一个photo就是我们这个尾部的这样的一个标签
[12:07] 那我们来点一下看一下那么在这个位置你看注意啊我点击它是不是会跳到这个里面来那么这个folder在哪里呢来看一下folder呢就是在这个layout下面是不是一个folder检验文件打开它啊就是这个文件那么在这个文件中是不是下面呢写了一些我们这个呃这个项目的一些版本信息对吧这个2018啊这个黑马晨星源博学股出品啊那么这样的一个信息那么这是不是就根据我们的一个需求做了改造那么呃
[12:34] 同学们如果说你们去做这种项目的时候是不是要改这个logo和它的版本信息的话是不是通过这两个位置是不是就可以做一个自定义的改造啊哎呦OK好那么我们通过这样的改造呢就已经实现了这样的一个效果啊哎呦OK好那么关于这个前端这个系统的一个搭建以及我们去修改它的logo以及它的版本信息的内容呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解如何修改前端项目中的 Logo 和版权信息，涉及文件路径、组件代码和样式调整。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程大纲，当前章节为“2.1、前端搭建”，并显示项目文件夹结构，其中“用户管理”文件夹被选中。
画面2：展示“itcast-haoke”项目文件夹，其中包含“开发环境相关”、“快捷启动脚本”、“dubbo”等文件夹和文件。
画面3：在 IntelliJ IDEA 中打开项目，终端显示依赖安装警告信息。
画面4：终端显示 Webpack 编译成功，应用运行在 http://localhost:8000。
画面5：展示“2.1.2、修改Logo以及版权信息”章节，指出全局布局文件位于“src/layouts”目录下，选中“BasicLayout.js”。
画面6：在“BasicLayout.js”文件中，导入了多个 React 和 Ant Design 相关模块，包括 logo、Footer、Header 等。
画面7：展示“BasicLayout.js”中包含的 <Authorized> 组件和 <Footer> 组件的嵌套结构。
画面8：展示“BasicLayout.js”中导入的模块列表，包括 logo、Footer、Header 等。
画面9：展示“SideMenu.js”文件中，定义了 isMainMenu 函数和 handleOpenChange 方法。
画面10：展示“SideMenu.js”中 <Sider> 组件的样式配置，包括 width、theme 等属性。
画面11：展示“SideMenu.js”中 <Sider> 组件的样式配置，其中 width 属性被修改为 256。
画面12：展示“BasicLayout.js”中 <div className={styles.logo} id="logo"> 的代码，以及在 Footer.js 中的版权信息。
画面13：展示“Footer.js”文件内容，包含 <GlobalFooter> 组件和版权信息。
画面14：展示“2.1.2、修改Logo以及版权信息”章节，选中“Footer.js”文件。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面5：
```
全局的布局文件在：
└── src
    ├── assets
    ├── components
    ├── i18n
    ├── layouts
    │   └── BasicLayout.js
    │   └── Footer.js
    │   └── Header.js
    │   └── MenuContext.js
    └── pages
```

画面6：
```javascript
import React from 'React';
import { Layout } from 'antd';
import DocumentTitle from 'React-document-title';
import isEqual from 'lodash/isEqual';
import memoizeOne from 'memoize-one';
import { connect } from 'dva';
import ContainerQuery from 'React-container-query';
import classNames from 'classnames';
import pathToRegexp from 'path-to-regexp';
import { enquireScreen, unenquireScreen } from 'enquire-js';
import FormatMessage from 'umi/locale';
import SideMenu from '@/components/SiderMenu';
import Authorized from '@/utils/Authorized';
import SettingDrawer from '@/components/SettingDrawer';
import logo from '@/assets/logo-heima.png';
import Footer from '@/Footer';
import Header from '@/Header';
import Context from './MenuContext';
import Exception403 from '@/pages/Exception/403';

const { Content } = Layout;

// Conversion router to menu.
function formatter(data, parentAuthority, parentName) {
  return data
    .map(item => {
      let locale = 'menu';
      if (parentName && item.name) {
        locale = `${parentName}.${item.name}`;
      } else if (item.name) {
        locale = item.name;
      }
      return {
        ...item,
        locale,
      };
    })
    .filter(item => item.name);
}
```

画面7：
```javascript
<Content style={this.getContentStyle()}>
  <Authorized authority={routerConfig && routerConfig.authority} noMatch={<Exception403 />}>
    {children}
  </Authorized>
</Content>
<Footer />
</Layout>
return (
  <React.Fragment>
    <DocumentTitle title={this.getPageTitle(pathname)}>
      <ContainerQuery query={query}>
        <Context.Provider value={this.getContext()}>
          <div className={classNames(param)}>{layout}</div>
        </Context.Provider>
      </ContainerQuery>
    </DocumentTitle>
  </React.Fragment>
);
```

画面9：
```javascript
isMainMenu = key => {
  const { menuData } = this.props;
  return menuData.some(item => {
    if (key) {
      return item.key === key || item.path === key;
    }
    return false;
  });
};

handleOpenChange = openKeys => {
```

画面10：
```javascript
[styles.light]: theme === 'light',
return (
  <Sider
    trigger={null}
    collapsible={collapsed}
    breakpoint="lg"
    onCollapse={onCollapse}
    width={256}
    theme={theme}
    className={siderClassName}
  >
    <div className={styles.logo} id="logo">
      <Link to="/">
        {/* <img src={logo} alt="logo" /> */}
        <h1>好客租房 - 管理系统</h1>
      </Link>
    </div>
    <BaseMenu
      {...this.props}
      mode="inline"
      handleOpenChange={this.handleOpenChange}
      onOpenChange={this.handleOpenChange}
      style={{ padding: '16px 0', width: '100%', overflowX: 'hidden' }}
    />
  </Sider>
```

画面12：
```javascript
<div className={styles.logo} id="logo">
  {/* <img src={logo} alt="logo" /> */}
  <h1>好客租房 - 管理系统</h1>
</div>

// 在Footer.js文件中修改版权信息：
import React, { Fragment } from 'React';
import { Layout, Icon } from 'antd';
import GlobalFooter from '@/components/GlobalFooter';

const FooterView = () => {
  <GlobalFooter>
    <Fragment>
      Copyright <Icon type="copyright" /> 2018 黑马程序员 博学谷 出品
    </Fragment>
  </GlobalFooter>
};

export default FooterView;
```

画面13：
```javascript
import React, { Fragment } from 'React';
import { Layout, Icon } from 'antd';
import GlobalFooter from '@/components/GlobalFooter';

const FooterView = () => {
  <GlobalFooter>
    <Fragment>
      Copyright <Icon type="copyright" /> 2018 黑马程序员 博学谷 出品
    </Fragment>
  </GlobalFooter>
};

export default FooterView;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面5：
标题：“2.1.2、修改Logo以及版权信息”
内容：展示“全局的布局文件在：”目录结构，其中“BasicLayout.js”被选中。

画面14：
标题：“2.1.2、修改Logo以及版权信息”
内容：展示“将logo部分修改为：”按钮，以及“全局的布局文件在：”目录结构，其中“Footer.js”被选中。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

