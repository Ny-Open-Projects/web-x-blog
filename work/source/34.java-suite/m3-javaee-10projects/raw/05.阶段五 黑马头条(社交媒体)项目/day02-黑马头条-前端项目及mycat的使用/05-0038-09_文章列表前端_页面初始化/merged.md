# 09_文章列表前端_页面初始化

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day02-黑马头条-前端项目及mycat的使用
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day02-黑马头条-前端项目及mycat的使用\09_文章列表前端_页面初始化【海量资源尽在 666java.com】.mp4
- 时长 8分25秒（音频 506s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就把前端的文章列表的开发呢咱们给做完了啊后端的话咱们昨天已经做完了啊然后下面咱们主要是说这个前端那前端该怎么做呢那做之前的大家呢应该先去再次去熟悉一下当前这个加载的过程啊那加载过程这样啊一开始的话呢当前假如说你启动当前这个项目以后呢首先呢会加载一个叫entry.js
[00:27] 那在GS里边其实主要是做了两个事第一个是加载了一个view它会把这个app这个给加载然后第二个非常重要就是当前这个.root.gs就是它这里面其实就去又去引入了一个叫routers那routers指定的是谁呢指定的是当前这目录有一个routers index
[00:49] 好那咱们去找一下那这个at是谁at指的就是当前src的根目录是吧在src rooters下面有个index当前的这个js可以找一找rooters有个index.js没问题吧好打开那打开完之后这个其实也没有做啥事它主要是来合并路由那合并谁呢合并了一个叫当前目录下面有一个home那这home的话就是它是吧打开
[01:18] 那home里边呢其实定义了一些东西啊其实目前的话就两块内容我来看一下啊第一块内容呢其实这是写好的啊第一个呢是有一个layout.man是吧第二个是配置丝home有一个index你看啊这个呢算是一个复节点是吧这是算是子节点啊这个home是在layout下面那行啊那这个组件的话呢像配置丝
[01:46] 咱们之前说过配置私政目录下面是咱们自己定义的一些这种view不是叫组件所以说咱们所有的模块都会在配置私下边创建那layout是一个通用的那通用的组件它包含了啥咱们可以简单看一样比如说compound有个layout好往下看有一个layoutlayout-man.view是吧这里边其实有一个二级路由的视图是吧OK这个不用管它主要是这个东西
[02:16] 这个是有一个底部菜单看到了吧底部菜单的话它会自动的去把你加进来好那咱们主要在咱们开发的时候最应该关心的是哪个呢最应该关心的是当前的你自己的模块比如说咱们现在有一个主页主页里边就是index.mew好那里边没有东西行咱们也可以去刷一下你看目前的话它只有啥呢只有底部菜单但是这里边内容它是没有的那好那我们的
[02:45] 列表该怎么去展示呢那咱们采用的呀采用的主要呢就是当前的VXUI里边提供的一个东西叫顶部标签栏哎顶部标签栏这时候呢咱们可以把它的原本啊先拷过来拷过来之后呢咱们再去改好吧好先拷过来啊直接放到哪啊直接放到你的index.view里边放进放进来之后啊那最终咱们的一个效果是啥呢你可以打开讲义啊
[03:17] 讲义里边呢是有一个叫做效果演示那这个呢其实呢就是咱们最终的一个效果比如说上面呢是有一个搜索框是吧还有一些菜单下面还有一些这种咱们要展示请求后台去展示这个数据对吧那行啊那咱们来看一下啊目前的话呢这个能不能完成呢其实呢咱们需要在这里边一步一步的进行改造才行好吧咱们看一下啊打开当前这个现在他说呀这块是报错了
[03:47] 那为什么报错呢他说你是找不到当前一个点config的东西那点config是啥呢是咱们之前去讲这个底部材料的时候已经说过了啊这因为呢他要去初始化一个这种titles是吧但是config里边是不是当前目录并没有啊所以说呢怎么在这啊去创建一个configconfig.ds好那里边内容是啥呢内容的话呢你可以去可以去参考谁呢哎我把下子关掉啊
[04:21] 你可以去参考里边这个东西是吧咱们之前也打开过啊所以说我就不打开了咱们直接从笔记中把它拷过来好吧好就这东西放到这之后啊你再来去看啊最终的咱们就有一个上上方的菜单这菜单的话就包含了动态是吧推荐扎味pattern是吧像这些菜单像OK咱们可以刷一下看看有没有这时候是不是已经有了呀是吧
[04:56] 那没问题啊那这个为什么这个样式好像不太好看呢其实没有问题啊咱们一会儿再去调啊又是再去调OK那这个展示完之后啊这里边内容好像给咱们给咱们自己的东西还差很多是吧来看一下啊效果展示里边首先呢这个效果里边啊来看一下啊目前这块内容呢是里边已经包含了这个数据呢咱们一会儿发请求咱去拿然后中间的这一部分啊
[05:28] 这部分刚才咱们也展示了现在缺失的是上面这一部分是吧好那咱们把上面这部分呢也给加进来好吧那这个怎么加呢其实这样啊当前的VIX呢它是可以去嵌套可以去嵌到其他的组件可以嵌到其他组件那这时候呢咱们就可以嵌套一个组件那组件是谁呢其实在咱们这个已经提供好的代码中呢已经封装了一个东西叫在components
[05:56] compound里边有一个busbus里边有一个是home8.6就这个组件那这个组件怎么加进来呢加进来的话其实很容易首先你要去引入进来我把这个style直接放到下面直接要不然的话操作也太麻烦了这时候咱们就可以引入当前的组件我们引入import是吧import然后是怎么起个名字好flom谁呀
[06:27] Vlam当前的SRCSRC怎么写啊是不是当前的什么一个这东西啊然后是然后呢然后下面是然后下面是是吧好那这样的话就加进来了啊目前加进来之后呢你会发现啊目前这东西啊咱们在这加杠吧好吧目前这东西好像是变灰色的是吧
[06:58] 这次的话就相当于没有引入这是怎么办呢你要在当前的这块内容呢去这有个compound组件你要把当前的这个东西呀给声明一下才行啊声明完之后你会发现啊这个就算是有效了啊有效之后呢那我怎么去在页面上去把它给装进来呢其实呢咱们可以在这啊直接写就可以在写之前呢我建议啊就是在这去加一个div啊把它都放进来啊这边呢是咱们的一个列表是吧
[07:28] 这一块内容啊好那这个是列表下面咱们再去另一个dab就专门去装这个前的搜索搜索的部分那怎么写呢其实你直接写这个组件就可以了号目什么完了这样的话就算是加进来了啊那行咱们就来可以去试一试啊可以试一试看看这个效果怎么样稍等好目前这个部分是不是就加进来了
[08:09] OK啊那没有问题啊当前这个东西哎已经加进来了然后咱们下面那咱们下面该干嘛了呢咱们下面呢就来去具体的去发起一些请求去把他们的数据给加载进来好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Weex UI 组件库开发一个带标签页的新闻应用首页，包括路由配置、布局结构和数据配置。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示项目结构，选中 `layouts` 文件夹下的 `layout.Vue`。
画面 2: 在 `router.js` 中定义路由，将 `/` 路由指向 `Layout` 组件，`/home` 路由指向 `Home` 组件。
画面 3: 查看 `layout_main.Vue` 文件，展示其模板结构，包含 `<router-view>` 和 `<div class="main-body">`，并导入 `Menu` 组件。
画面 4: 在 Weex Playground 中查看 `wxc-tab-page` 组件的使用方法和示例效果。
画面 5: 在文档中查看“2.1 创建文件”部分，提到创建 `src/api/home/index.js` 文件用于封装数据请求。
画面 6: 查看 `index.Vue` 文件，展示 `wxc-tab-page` 的模板结构，包含 `wxc-pan-item`。
画面 7: 查看 `config.js` 文件，展示导入 `Config` 的代码和 `export default` 的配置对象。
画面 8: 查看 `config.js` 文件，展示 `tabStyles` 对象的样式配置。
画面 9: 查看 `config.js` 文件，展示 `tabTitles` 数组和 `tabStyles` 对象的配置。
画面 10: 查看 `config.js` 文件，展示 `tabTitles` 数组和 `tabStyles` 对象的配置。
画面 11: 查看 `index.Vue` 文件，展示 `wxc-tab-page` 的模板结构，包含 `wxc-pan-item`。
画面 12: 查看 `index.Vue` 文件，展示 `script` 部分的代码，导入组件并定义数据和方法。
画面 13: 查看 `index.Vue` 文件，展示 `wxc-tab-page` 的模板结构，包含 `wxc-pan-item`。
画面 14: 在 Weex Playground 中展示应用的预览效果，包含一个二维码。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面 2:
```javascript
import Layout from '@/components/layouts/layout_main'
import Home from '@/pages/home/index'
let routes = [
  {
    path: '/',
    component: Layout,
    children: [
      {
        path: '/home',
        name: 'Home',
        component: Home
      }
    ]
  }
]
export default routes;
```

画面 3:
```Vue
<template>
  <div class="wrapper">
    <div class="router-body"><router-view></router-view></div>
    <div class="main-body"><Menu></Menu></div>
  </div>
</template>

<script>
// 引入底部菜单
import Menu from '@/components/menus/menu'

export default {
  name: 'Weex-Layout-Mian',
  components: {Menu}
}
</script>

<style scoped>
.wrapper {
  flex-direction: column;
  flex-wrap: wrap;
}

.router-body {
  flex: 1;
  flex-direction: column;
  border: 1px solid red;
}
</style>
```

画面 6:
```Vue
<template>
  <wxc-tab-page ref="wxc-tab-page"
    :tab-titles="tabTitles"
    :tab-styles="tabStyles"
    title-type="icon"
    tab-page-height="tabPageHeight"
    @wxcTabPageCurrentTabSelected="wxcTabPageCurrentTabSelected"
  >
    <list v-for="(demo, key) in tablist" :key="key">
      <cell v-for="(v, key) in v" :key="key">
        <wxc-pan-item text-id="1" + (v) + '+' + (key)
          url="https://HS.m.taobao.com/trip/ticket/detail/index.html?scnId=2675"
        >
          <div class="content">
            <text>{{(key)}}</text>
          </div>
        </wxc-pan-item>
      </cell>
    </list>
  </wxc-tab-page>
</template>

<style scoped>
.item-container {
  width: 750px;
  background-color: #f2f3f4;
}

.border-cell {
  background-color: #f2f3f4;
  width: 750px;
  height: 24px;
  align-items: center;
  justify-content: center;
  border-bottom-width: 1px;
  border-style: solid;
  border-color: #b8b8b8;
}
</style>
```

画面 7:
```javascript
// script
const dom = weex.requireModule('dom');
import { WxcTabPage, WxcPanItem, Utils, BindEnv } from 'weex-ui';
import Config from './config'
export default {
  components: { WxcTabPage, WxcPanItem },
  data () {
    return {
      tabTitles: Config.tabTitles,
      tabStyles: Config.tabStyles,
      tablist: [],
      demoList: [1, 2, 3, 4, 5, 6, 7, 8, 9],
      tabPageHeight: 134
    }
  },
  created () {
    this.tabPageHeight = Utils.env.getPageHeight();
    this.tablist = [...Array(this.tabTitles.length).keys()].map(i => i);
    Vue.set(this.tablist, 0, this.demoList);
  },
  methods: {
    wxcTabPageCurrentTabSelected (e) {
      const self = this;
      const index = e.page;
      if (!Utils.isNonEmptyArray(self.tablist[index])) {
        // 未加载数据请求
      }
    }
  }
}
```

画面 8:
```javascript
{
  title: 'JAVA', id: 1,
  title: 'Python', id: 2,
  title: 'VUE', id: 3,
  title: 'WEEX', id: 4,
  title: '大数据', id: 5,
  title: 'Docker', id: 6,
  title: '其它', id: 0
},
tabStyles: {
  bgColor: '#FFFFFF',
  titleColor: '#B6665B',
  activeTitleColor: '#31D3D3',
  inactiveTitleBold: true,
  iconWidth: 70,
  width: 120,
  height: 80,
  fontSize: 24,
  hasActiveButton: true,
  activeBottomColor: '#31D3D3',
  activeBottomHeight: 6,
  textPaddingLeft: 10,
  textPaddingRight: 10,
  normalBottomColor: 'rgba(0,0,0,0.4)',
  normalBottomHeight: 2,
  hasRightIcon: false,
  rightOffset: 100
}
```

画面 9:
```javascript
export default {
  tabTitles: [
    { title: '动态', id: '_dyna_' },
    { title: '推荐', id: '_all_' },
    { title: 'JAVA', id: 1 },
    { title: 'Python', id: 2 },
    { title: 'VUE', id: 3 },
    { title: 'WEEX', id: 4 },
    { title: '大数据', id: 5 },
    { title: 'Docker', id: 6 },
    { title: '其它', id: 0 }
  ],
  tabStyles: {
    bgColor: '#FFFFFF',
    titleColor: '#B6665B',
    activeTitleColor: '#31D3D3',
    inactiveTitleBold: true,
    iconWidth: 70,
    width: 120,
    height: 80,
    fontSize: 24,
    hasActiveButton: true,
    activeBottomColor: '#31D3D3',
    activeBottomHeight: 6,
    textPaddingLeft: 10,
    textPaddingRight: 10,
    normalBottomColor: 'rgba(0,0,0,0.4)',
    normalBottomHeight: 2,
    hasRightIcon: false,
    rightOffset: 100
  }
}
```

画面 11:
```Vue
<template>
  <div>
    <wxc-tab-page ref="wxc-tab-page"
      :tab-titles="tabTitles"
      :tab-styles="tabStyles"
      title-type="icon"
      tab-page-height="tabPageHeight"
      @wxcTabPageCurrentTabSelected="wxcTabPageCurrentTabSelected"
    >
      <list v-for="(demo, key) in tablist" :key="key">
        <cell v-for="(v, key) in v" :key="key">
          <wxc-pan-item text-id="1" + (v) + '+' + (key)
            url="https://HS.m.taobao.com/trip/ticket/detail/index.html?scnId=2675"
          >
            <div class="content">
              <text>{{(key)}}</text>
            </div>
          </wxc-pan-item>
        </cell>
      </list>
    </wxc-tab-page>
  </div>
</template>
``

