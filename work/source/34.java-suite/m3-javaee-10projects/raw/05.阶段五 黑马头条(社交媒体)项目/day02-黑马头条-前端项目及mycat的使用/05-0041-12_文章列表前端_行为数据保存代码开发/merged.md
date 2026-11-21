# 12_文章列表前端_行为数据保存代码开发

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day02-黑马头条-前端项目及mycat的使用
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day02-黑马头条-前端项目及mycat的使用\12_文章列表前端_行为数据保存代码开发【海量资源尽在 666java.com】.mp4
- 时长 10分5秒（音频 606s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,下面咱们就继续往下讲刚才咱们已经把当前这个数据列表已经展示了一下那这个没有问题那这块内容其实还少一个需求大家还有没有印象在咱们第一天去讲当前这个文章列表需求的时候说了里边仅仅是有数据展示,是吧还有什么?
[00:21] 还有一个是隐藏的需求需要去干嘛呢?
[00:25] 需要去记录当前用户的行为那这行为该怎么去做呢?
[00:29] 其实咱们后台接口都已经写完了是吧那这时候呢咱们只需要干嘛呢往当前的一个表中去保存记录就可以了啊那这表呢其实就是我打开这个表啊就是AP show behavior里边这个表然后这里边呢咱们主要是往里边去记录数据那记录哪些数据呢来看一看啊首先呢第一个是D就不用说了是吧第二个是设备D这个咱们也是从后台可以拿OK最主要的是这个东西
[00:55] 叫Article ID也就是说啊当用户已经浏览完的这种文章信息都应该去记录到这去记录到这咱们主要是来干这个事啊后边其实也无所谓主要就是拿到当前的Article ID那行啊那目前的话咱们是能浏览当用户已经浏览过的所有的ID我都应该记录到当前的表中那这个怎么办呢首先呢咱们应该考虑一个事就是那这个ID该怎么拿
[01:24] 那ID怎么拿呢咱们还得去分析当前的一个东西就是数据展示的这一块内容最终咱们数据是在这展示的那ID肯定是能通过当前items.id就能拿到当前的ID所以说咱们就这么拿首先咱们在这先去写一个东西你看看笔记先去定一个对象这个对象就是来去记录当前的用户ID的OK
[01:53] 那中的你要去展示文章的时候呢是多少文章就往这个里边去装多少数据就可以了那这事拿到ID之后那这事成功之后那咱们进行保存就可以了啊那行那我现在这个对象是有了那我怎么该该怎么去把这把这个ID装进去呢这里边呢其实还有一个方法哪个方法呢咱们可以去做一个实践啊这有一个显示的实践嗯你看看啊当年他好
[02:23] 跑到咱们的当前的展示的位置啊哪个展示了呢哎就是当前的这块那块好好那这时候呢其实就在这去展示了啊展示完之后呢咱们就能去触发这个方法然后呢拿到ID并且保存到当前的刚才定义的这个变量里边咱们只需要干嘛呢哎把这个方法给写一下就可以了这个方法这个方法啊就是当前的这个受就是当前受方法
[02:54] 那这个方法该怎么写呢好来看一下啊这个方法的话咱们就先定义出来啊比如说叫售然后呢然后那这里边主要是干啥事呢那肯定会接入个ID啊ID就是article ID那咱们怎么去装进去呢那直接装进去就行了吗比如说我要用户重复看那该怎么办呢哎这事咱们一会会去考虑主要呢咱们先去往这里边去装数据然后并且呢再没有保存的数据啊就是说
[03:26] 没有进行保存的ID复一个值复值为保存之后的ID复值为啥呢复值为first这样的话就能区分了分到时候呢只去保存当前为初的ID就可以了那现在咱们先来去判断一下如果说呢咱们当前里边有个ASID
[04:02] 如果说他不等于他等于等于安利翻译的话他如果这里边并没有他啊没有他的话呢咱们就往里边去装一层数据啊他呢就等于谁呀他说了没有保存的给一个什么一个那这样的话咱们就算是做完了那负二次什么时候负呢负二次就是咱们你去保存成功之后在你保存成功之后啊咱们再来重新去设置这个值好吧这好像是有点问题是吧这里边
[04:34] 再用这个东西是不是得去加什么东西加一个Z是吧我给大家下面也是加Z好那这样的话就没有问题了行那这个写完之后呢那咱们就进行保存那保存该怎么保存在哪保存保存的时机是啥呢那你当用户去查看的时候咱们就去保存一次吗这好像这个事也不太好办对吧那咱们这样啊咱们这个思路呢就是
[05:03] 在当前crate里边出入化email的时候呢咱们就会去每隔五秒每隔五秒啊每隔五秒就干嘛呢就去提交一丝数据那的话就能保证这个数据啊是绝对是用查看的时候就能就有效的去保证用户的ID呢能够查看的文章ID都能够去存到他们的数据库中好吧那这个啊
[05:35] 那这个每个5秒怎么怎么做呀就这里面是不是用到那个定时啊所以说呢咱们在这啊这个代码已经写完了啊咱们就直接考过来我简单说一说啊其实跟咱们之前那个思路是差不多的啊只是又逻辑稍微有点区别啊就是就是就这道代码啊怎么考过来考过来之后能看懂来看一眼啊首先啊首先呢是有这么个东西你看一个set interval是吧它呢是有两个参数第一个参数是它就是我选中这一块啊它就会去
[06:05] 执行那多长多长时间执行一次呢5秒哎每5秒就会执行当前的这个函数那这函数里边干啥事呢哎这函数里边啊就掉了一个API啊并且呢是进行了保存那这个这个你看这个当前的参数呢就是AS的兽就是刚才咱们建议的当前的这个对象好吧那没问题啊那这个this啊this是在这去加了下滑线啊其实还是这个thisOK那这里边还有什么还有啥呢还有一个API
[06:34] API是这样因为咱们之前去请求数据的时候是不是自己写的这种request是吧这里边其实在给你们资料里边还有一个APIS就是SRC下面有一个APIS有个homehome里边是有个api.js咱们以后的API通通都封装到当前的APIS里边目前是home模块如果后面有什么article有其他的时候咱们还会再去进行封装
[07:02] 目前的话其实都已经封装到了api.js那行啊那这里边啊那首先呢你要想去用它的话呢你还得先去导入当前的API才可以那导入怎么导入啊导入的事就很简单了啊就在这去写一个什么import然后是当前的什么来叫API吧好吧给写个名字啊flom然后这里边是哪个是吧根目录呗是APIS
[07:37] homeapi.js可以了这个.js你可以省掉这样就算是保留了好了导入完之后咱们还要再往下看这里边最终你可以点进去进去之后你会发现其实就是调用的前的request post请求
[08:03] 那这样就能去发请求的数据到后端那这样啊那这个既然已经做完了那咱们就来去启动一下程序来去看一眼到底能不能去发请求到后端咱们可以按F12啊然后刷新一下不用重新启动好稍等看看有没有触发好触发了触发之后但是404是吧404那为啥是404呢那这一块的路径好像是有问题
[08:40] 目前是这样目前咱们做代理的时候其实都是在当前的config.js中都是走的当前的这个东西就咱们这个应该是走当前下面的东西所以说这个API你最好是改一改那怎么改呢改的话其实也很容易就是说这块路径的你用他的用谁的用你自己定义的这个路径咱们都知道是哪个是不是咱们之前定义过叫APIv1什么
[09:13] 你要是不知道的话呢你可以这样啊你可以打开当前的后端的微服务啊打开当前这看你的control中当时怎么写的你看这块是不是api v1behaviour然后是savebehaviour那就把它直接拷过来就走了啊拷过来之后啊这事儿你还要再去考虑一个问题最终呢咱们要去通过谁呀通过咱们的代理是吧那个代理的话需要去帮你去做转发
[09:40] 那这时候呢它呢是有一个前缀所以说呢前缀你要加上好稍等啊嗯行加上前缀之后呢加上前缀之后啊它就会去被这拦截拦截完之后它就会把这个过滤掉并且是转发到了9604当前这个端口号上OK那这样没问题吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲一个前端页面（文章列表页）如何通过 Vue.js 实现分页加载、用户行为记录（如点赞、收藏）以及与后端服务（Spring Boot）交互的完整流程。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程文档目录结构，重点在“6.5 多环境切换”和“7.1 文章列表需求分析”，并附带一个关于“文章首页”功能的流程图，说明用户登录状态影响文章加载，以及“用户点击文章列表进行操作”后会“记录用户行为”。
画面2：展示一个手机端网页预览界面，包含搜索框、文章列表和底部导航栏，右侧有一个二维码，提示使用 Weex playground app 扫描。
画面3：在 WebStorm 中打开 `src/pages/index.Vue` 文件，展示 Vue 组件的 `export default` 部分，包含 `components`、`data`、`created`、`mounted`、`methods` 等生命周期钩子和方法，其中 `data` 中定义了 `tabTitles`、`tabStyles`、`tablist`、`loaddir`、`index`、`tag`、`size`、`max_bohot_time`、`min_bohot_time` 等变量。
画面4：展示 `index.Vue` 文件中 `<template>` 部分的 HTML 结构，包含一个 `<div>` 包裹的 `<wx-tab-page>` 组件，以及 `<script>` 部分导入了 `Home_Bar`、`request`、`WxcTabPage`、`WxcPanItem`、`Utils`、`BindEnv` 等模块。
画面5：展示 `index.Vue` 文件中 `methods` 部分的 `load()` 方法，其中包含 `request.get('/toutiao/api/v1/article/load', this.params).then((res) => { this.tanfer(res.data); })` 用于发起网络请求并处理返回数据。
画面6：展示 `index.Vue` 文件中 `methods` 部分的 `show(id)` 方法，其中包含 `if (this.ashow[id] === undefined) { this.ashow[id] = true; }` 用于记录用户行为。
画面7：展示 `index.Vue` 文件中 `methods` 部分的 `load()` 方法，其中包含 `this.shownew = true; this.params.loaddir = 0; this.load();` 用于重置加载状态并重新加载数据。
画面8：展示 `index.Vue` 文件中 `created()` 钩子中的 `Api.saveShowBehavior(this.ashow)` 调用，用于保存用户行为。
画面9：展示 `index.Vue` 文件中 `load()` 方法内部的 `tanfer` 函数，用于将数据转换为 Model 对象，其中包含 `for (let i = 0; i < data.length; i++) { let tmp = { id: data[i].id, title: data[i].title, comment: data[i].comment, }`。
画面10：展示 `index.Vue` 文件中 `import Api from '@/apis/home/api.js'`，并展示 `export default` 部分的 `data` 中定义的 `loaddir`、`index`、`tag`、`size`、`max_bohot_time`、`min_bohot_time` 等变量。
画面11：展示浏览器开发者工具中的 Network 面板，显示了多个资源的加载情况，包括 `404` 状态的 `text/html` 和 `200` 状态的 `png` 文件。
画面12：在 WebStorm 中打开 `src/configs/webpack.dev.conf.js` 文件，展示 `proxyTable` 配置，其中包含 `'/toutiao': { target: 'http://api.toutiao.com', changeOrigin: true, pathRewrite: { '^/toutiao': '' } }` 和 `'/behavior': { target: 'http://api.toutiao.com', changeOrigin: true, pathRewrite: { '^/behavior': '' } }`。
画面13：在 IntelliJ IDEA 中打开 `BehaviorController.java` 文件，展示 `saveShowBehavior` 方法，其中包含 `return appShowBehaviorService.saveShowBehavior(dto);`。
画面14：再次展示 `src/configs/webpack.dev.conf.js` 文件中 `proxyTable` 配置，内容与画面12相同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```javascript
import Item from '@/components/cells/article_3.Vue'
import Config from './config'
export default {
  components: { WxcTabPage, WxcPanItem, Home_Bar, Item0, Item1, Item },
  data () -> {
    tabTitles: Config.tabTitles,
    tabStyles: Config.tabStyles,
    tablist: [],
    showmore: false,
    demolist: [1, 2, 3, 4, 5, 6, 7, 8, 9],
    tabPageHeight: 1334,
    load_more_text: '加载更多...',
    load_new_text: '加载更新...',
    params: {},
  },
  created () {
    this.tabPageHeight = Utils.getPageSize();
    this.tablist = [...Array(this.tabTitles.length).keys()].map(i => {});
  },
  mounted () {
    this.$refs['wxc-tab-page'].setPage(1)
  },
  methods: {
    loaddir: 1,
    index: 0,
    tag: 'all_',
    size: 20,
    max_bohot_time: 1559789043,
    min_bohot_time: 1559789043,
  },
}
```

画面4：
```html
<div>
  <wx-tab-page>
  </wx-tab-page>
</div>
<script>
import Home_Bar from '@/components/bars/home_bar.Vue'
import request from '@/common/request'
const dom = weex.requireModule('dom');
import { WxcTabPage, WxcPanItem, Utils, BindEnv } from 'weex-ui';
import Item0 from '@/components/cells/article_3.Vue'
import Item1 from '@/components/cells/article_3.Vue'
import Item from '@/components/cells/article_3.Vue'
import Config from './config'
import Api from '@/apis/home/api.js'
export default {
  components: { WxcTabPage, WxcPanItem, Home_Bar, Item0, Item1, Item },
  data () -> {
    tabTitles: Config.tabTitles,
    tabStyles: Config.tabStyles,
    tablist: [],
    showmore: false,
    demolist: [1, 2, 3, 4, 5, 6, 7, 8, 9],
    tabPageHeight: 1334,
    load_more_text: '加载更多...',
    load_new_text: '加载更新...',
    params: {},
  },
}
```

画面5：
```javascript
methods: {
  load () {
    this.shownew = true;
    this.params.loaddir = 0;
    this.load();
  },
  load () {
    // 发送请求，并且获取到数据，视频展示到页面上
    request.get('/toutiao/api/v1/article/load', this.params).then((res) => {
      this.tanfer(res.data);
    })
  }
}
```

画面6：
```javascript
methods: {
  show (id) {
    // 没有进行存储id赋值为ture，保存之后的id为false
    if (this.ashow[id] === undefined) {
      this.ashow[id] = true;
    }
  }
}
```

画面7：
```javascript
methods: {
  load () {
    this.shownew = true;
    this.params.loaddir = 0;
    this.load();
  },
  load () {
    // 发送请求，并且获取到数据，视频展示到页面上
    request.get('/toutiao/api/v1/article/load', this.params).then((res) => {
      this.tanfer(res.data);
    })
  }
}
```

画面8：
```javascript
created () {
  this.tabPageHeight = Utils.getPageSize();
  this.tablist = [...Array(this.tabTitles.length).keys()].map(i => {});
  let this = this;
  let timer = setTimeout(function () {
    let result = Api.saveShowBehavior(this.ashow);
    result.then((d) => {
      // 标记已经处理完成
      let ids = d.data;
      for (let i = 0; i < ids.length; i++) {
        this.ashow[ids[i].id] = false;
      }
    });
  }, 5000);
}
```

画面9：
```javascript
tanfer: function (data) {
  for (let i = 0; i < data.length; i++) {
    let tmp = {
      id: data[i].id,
      title: data[i].title,
      comment: data[i].comment,
    }
  }
}
```

画面10：
```javascript
import Api from '@/apis/home/api.js'
export default {
  components: { WxcTabPage, WxcPanItem, Home_Bar, Item0, Item1, Item },
  data () -> {
    loaddir: 1,

