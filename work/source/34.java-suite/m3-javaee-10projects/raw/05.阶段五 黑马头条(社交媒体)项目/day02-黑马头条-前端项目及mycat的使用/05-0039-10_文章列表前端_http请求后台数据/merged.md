# 10_文章列表前端_http请求后台数据

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day02-黑马头条-前端项目及mycat的使用
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day02-黑马头条-前端项目及mycat的使用\10_文章列表前端_http请求后台数据【海量资源尽在 666java.com】.mp4
- 时长 11分53秒（音频 713s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们就继续往下讲刚才咱们把这个页面的已经调完了下面咱们就去发后台的请求去把数据给获取到那首先咱们还是要去分析当前已经存在的页面那里边其实有一些方法咱们需要知道比如说这里边有个mythosmythos里边是有两个方法是吧最起码的你要知道这个方法是干嘛的就是咱们用的最多的应该是这个方法那这个方法其实就是来去干嘛的
[00:29] 切换什么呢咱们的table的这种标签是吧也叫栏目啊那这个怎么怎么办呢就在这啊比如说我要去哎现在是推荐我想你改成招那这时候他应该是重新发送请求他触发的就是这个方法咱们也可以来调一下啊可以把没用的先给删掉啊比如说all right哎好然后是一点什么一直但还里里边还有一个啊而这个呢没有呢也删掉用咱们这里边并
[01:02] 嗯不会用到他所以把它给删掉就可以了啊这时候呢咱们可以刷一下啊你点一下OK那这时候是不是一这时候是不是二你再刷一下这时候里边会有个问题他默认的并不会去选择一个他选择完一个之后呢他也不会去弹窗也就是说当前这个方法并没有必要用是吧也就是说初始化的时候他没有那这时候呢咱们咱们呢需要有这么一个操作啊就是说呃用户一进来之后呢我就让他钱
[01:33] 显示推荐这一栏目并且呢主要展示的也是推荐的一些内容那这个怎么办呢这时候呢咱们可以在这看啊这里边其实有些参数咱们可以可以去简单看一下下边呢是有一个主动触发主动触发设置页面就是这东西他就会去触发当前这个方法那这怎么写呢咱们把它回来这有个Rated那是不是还有个Mounted是吧
[02:03] 咱们就用monty的去做好吧来忘记怎么写啊m o u n t e dm o u n t e d啊好再加兜号啊把刚才这句话呢给拷过来拷过来之后呢咱们来刷一下先看一看这是个啊这个二啊好点一下刷嗯啊这是吧你看这一块那种我把它给删了啊完了啊这个呢这个啊刷一下你看默认选中的是不是渣味的
[02:43] 我想让他选中当前这个推荐怎么办呢这设置为几啊OK啊他从零开始嘛所以说咱们再刷一下啊这时候你看是不是这个方法就能触发并且这个推荐是不是也选中了OK啊那这样的话呢咱们就算是把这个效果给做出来了那做出来之后啊咱们现在就要想办法去发送请求那发请求该怎么发呢
[03:08] 就这块啊咱们先先不要发请求啊咱们首先呢应该知道啊咱们要去发请求的话呢首先咱们应该往后台传什么数据咱们后台接口里边啊那我这已经打开了啊就是咱们当去请求一个叫article里边有个load当前的接口的时候他需要去传什么呢DTO那DTO里边呢其实就是当前的这些参数啊就这些参数这些参数你应该从前台往后台去传
[03:39] 所以说呢这个参数啊咱们要去设置一下啊那行那咱们呢就从笔记中把这个参数啊给考过来啊啊就是一个拍上不思哎拿过来之后咱们再来说一说好点啊是是不是考到当前的有个这种地图里边啊好那考过来之后啊这里面是有一个
[04:00] load dir是你可以去设置请求的这种什么到底是load more还是load new是吧咱们设置为11的话是load more或者是load都可以index0是初始的一个东西咱们这个先不用管它然后tag是杠杠all这个大家还有没有印象杠杠all是不是就是查询所有的这种channel id也就是咱们并没有去设置频道是吧
[04:23] size是20是吧目前的话咱们先写死两个参数一个是最大的时间一个是最小的时间好吧那行那这个参数啊有了那参数有了之后呢咱们还要再去分析就是目前的话咱们去该如何去发请求那发请求的话比如我在这啊去写一个load方法叫this.load好吧load没有咱们就创建出来好吧load这里边啊我应该是发请求啥呢发送
[04:57] 请求并且呢获取到什么数据然后是什么呢数据展示到哪啊数据吧数据展示到页面上这个数据啊是这样啊这数据的话其实有一个叫table list最终的咱们是把当前的数据放到table list中就完事了啊行那这一步咱们先不做咱们下面先去把这数据给拿到先看看该怎么去拿
[05:32] 那该怎么去拿呢首先那发请求该怎么发呀咱们是不是之前学过叫striam是吧striam是不是这样啊这样里边是不是咱们可以去设置什么url或者什么呃就是type是吧不懂url或者什么type是吧我们都可以在这里去设置啊当然了咱们这个
[06:02] 当前的项目中已经封装了一个工具类所以说咱们不用写这种strem.fetch了直接可以用它的工具类就可以它的工具类在哪呢在当前的comment下面有一个request.js里边你看里边是有两个方法封装了第一个是post第二个是getOK这两个其实里边封装的大家也看到了就是strem.fetch里边你可以设置master的url type是吧当前的post你可以设置为
[06:31] 包里是吧前面三个啊加包里是吧你都可以去设置所以说呢怎么样想用它怎么办呢哎用用这个就可以了啊那想用它怎么办呢首先第一步是不是要先导进来呀导进来怎么导啊还是 import然后当前呢他是在呃请个名吧叫请个名要 request 好吧不浪谁呀是当前的什么呃爱可然后是 common什么一个是 request
[07:06] 这个就是JS这行是吧好像是换个名我看看好像也不行放到上面其实这个辩护其实没有问题你直接在你的当前的方法中调用就可以了你看这里边刚才说了咱们是有什么POST和GET请求所以说你直接在这用就可以怎么用这就request
[07:46] 这里边你可以直接去发请求当然这个get请求啊咱们需要去设置几个参数啊可以看一下他封装的东西啊他封装的东西呢第一个是pass就是你的什么API就你的URL啊然后第二个呢是PyramusPyramus呢他就会给你去封装当前的这种什么问号和按的符号是吧所以说这个东西啊还是挺好用的所以说你在这啊直接去写谁的就可以了比如说第一个
[08:15] 什么事URL第二个呢就是咱们Z4.2Pyramus好吧这个东西可以拷过来啊写错的话就拷过来那这个URL是啥呢URL那这个URL呢其实是这样啊URL的话就是咱们之前的哪个呢当前的这个接口地址对吧拷过来拷过来然后是加一个load好吧默认先让他去搭载load对吧好没问题啊
[08:52] 那这个加完之后啊那最终咱们的参数该怎么去拿呢咱们可以看一眼啊最终的他呢是有一个叫什么来着看看啊getget里边呢是有一个response是吧然后最终呢咱们是有一个response你可以准备tun就可以了他这有一个permiss去封装的所以说咱们可以干嘛呢点什么然后呢然后这边有个res这样的话呢其实就拿到了谁呀拿到了当前的res
[09:24] IS这个对象你们可以打印一下json.f y res这样的话其实就拿到了当前的数据行那咱们就来试一试但这个load的话其实应该是在这去调用ok这里调用了没问题我把这个alert删掉行那咱们去刷新一下看看能不能请求到咱们的数据好像不行是吧这边说抱错了首先呢这有一个东西叫comment说找不着request
[09:57] 好来看一下啊这有没有写错加一个杠吧好吧comment然后是request.jsrequest没问题啊咱们再刷一下啊好呃发送了是吧但是猪居好像没有拿到他返回的是一个浪那为什么返回的是一个浪呢咱们来看一下啊f12再刷一下当前的请求啊的确是发了啊他是
[10:37] 但是的确是没有拿到数据啊response里边的确是没有东西啊那这那这个是怎么回事呢啊现在大家一定要知道啊目前的话咱们是前后端分离那当前这个项目呢是node去起的那后端后端项目呢咱们是用的是sperm boot是吧他去启动的他两个肯定是出现了跨域的问题所以说呢咱们在当前的项目中啊呃前前段的项目中啊有一个configsconfigs里边有个config.js
[11:04] 里边呢你可以在这啊去设置当前的一个这种路径啊设置路径你看咱们现在呢可以去请求9603那怎么请求呢你在前面呢必须加一个头条然后最终把头条给过滤掉他这样的话才能去转发通过代理的方式去请求咱们的9603当前的一个微服务所以说怎么办呢你真正去发请求的时候呢加一个头条然后下一个杠
[11:34] 然后这时候呢咱们再来试一下行不行来刷新好你看啊现在目前的话这个数据是不是就拿到了呀OK啊那数据拿到了然后下面呢咱们就把这个数据啊给封装到咱们的页面上去展示好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Weex 项目中集成并使用 `wxc-tab-page` 组件，实现标签页功能，并通过自定义请求模块与后端 API 交互。

2) 按时间顺序列出每张画面的要点：
画面 1: 在 WebStorm 中编辑 `src/pages/home/index.Vue` 文件，导入 `wxc-tab-page` 组件并配置其属性，如 `tabTitles`、`tabStyles`、`tabList` 和 `tabPageHeight`。
画面 2: 继续编辑 `index.Vue`，在 `methods` 中定义 `wxcTabPageCurrentTabSelected` 方法，用于处理标签页切换事件。
画面 3: 在浏览器中打开 Weex Playground 的 `wxc-tab-page` 文档页面，查看其可配置参数表，包括 `tab-titles`、`tab-type`、`tab-page-height` 等。
画面 4: 在 Weex Preview 中预览一个包含二维码的页面，提示使用 Weex playground app 扫码。
画面 5: 在 Typora 中查看文档，内容为“2.2.1 在 src/pages/home/index.Vue 中定义 Model”。
画面 6: 在 WebStorm 中编辑 `index.Vue`，在 `mounted` 生命周期钩子中调用 `this.$refs['wxc-tab-page'].setPage(1)` 设置默认选中标签页。
画面 7: 在 WebStorm 中编辑 `index.Vue`，在 `methods` 中定义 `load` 方法，用于发起数据请求。
画面 8: 在 WebStorm 中编辑 `src/common/request.js` 文件，定义 `post` 和 `get` 方法，用于封装 HTTP 请求。
画面 9: 在 WebStorm 中编辑 `index.Vue`，在 `methods` 中定义 `request.get` 方法，用于发起 GET 请求。
画面 10: 在 IDEA 中查看 `ArticleHomeController` 类的源码，其中定义了 `countId`、`maxBhotTime`、`minBhotTime`、`size` 和 `tag` 等属性。
画面 11: 在 WebStorm 中编辑 `index.Vue`，在 `methods` 中定义 `request.get` 方法，用于发起 GET 请求。
画面 12: 在 Weex Preview 中显示编译失败的错误信息，提示找不到 `common/request` 模块。
画面 13: 在 WebStorm 中编辑 `index.Vue`，在 `template` 中定义 `wxc-pan-item` 组件，并在 `script` 中导入 `request` 模块。
画面 14: 在浏览器的开发者工具中查看网络请求，显示已加载的资源和请求状态。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面 1:
```javascript
<script>
import Home_Bar from '@/components/bars/home_bar.Vue';
const dom = weex.requireModule('dom');
import { WxcTabPage, WxcPanItem, Utils, BindEnv } from 'weex-ui';
import Config from './config';
export default {
  components: [WxcTabPage, WxcPanItem, Home_Bar],
  data () {
    tabTitles: Config.tabTitles,
    tabStyles: Config.tabStyles,
    tabList: [],
    demoList: [1, 2, 3, 4, 5, 6, 7, 8, 9],
    tabPageHeight: 1334
  },
  created () {
    this.tabPageHeight = Utils.env.getPageHeight();
    this.tabList = [...Array(this.tabTitles.length).keys().map(i => i)];
  },
  methods: {
    wxcTabPageCurrentTabSelected (e) {
      const self = this;
      const index = e.page;
      if (Utils.isNonEmptyArray(self.tabList)) {
        setUtils(() => {
          this.tabList = [...Array(this.tabTitles.length).keys().map(i => i)];
        });
      }
    }
  }
};
</script>
```

画面 3:
```html
<table>
  <thead>
    <tr>
      <th>可配置参数</th>
      <th>Type</th>
      <th>Required</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>tab-titles</td>
      <td>Array</td>
      <td>Y</td>
      <td>[]</td>
      <td>顶部显示标题</td>
    </tr>
    <tr>
      <td>tab-type</td>
      <td>String</td>
      <td>N</td>
      <td>icon</td>
      <td>显示类型 icon / text / iconFont (注)</td>
    </tr>
    <tr>
      <td>tab-page-height</td>
      <td>Number</td>
      <td>N</td>
      <td>1334</td>
      <td>Tab page 页面的高度</td>
    </tr>
    <tr>
      <td>is-tab-bar</td>
      <td>Boolean</td>
      <td>N</td>
      <td>true</td>
      <td>当设置为 false，同时 tab 配置 url 参数即可出现</td>
    </tr>
  </tbody>
</table>
```

画面 5:
```markdown
2.2.1 在 src/pages/home/index.Vue 中定义 Model
```

画面 6:
```javascript
mounted() {
  this.$refs['wxc-tab-page'].setPage(1);
},
```

画面 7:
```javascript
methods: {
  load () {
    // 发送请求，并且获取到数据，把数据展示到页面上
    // url: "",
    // type: ""
  },
  wxcTabPageCurrentTabSelected (e) {
    const self = this;
    const index = e.page;
    alert(e.page);
    this.load();
  },
  wxcPanItemPan (e) {
    if (BindEnv.supportsForAndroid()) {
      this.$refs['wxc-tab-page'].bindExp(e.element);
    }
  }
},
```

画面 8:
```javascript
if (!this.stream) {
  this.stream = weex.requireModule('stream');
  return this.stream;
}

post: function (path, body) {
  let stream = this._check();
  return new Promise((resolve, reject) => {
    stream.fetch({
      method: 'POST',
      url: path,
      type: 'json',
      body: body
    }, (response) => {
      if (response.status == 200) {
        resolve(response.data);
      } else {
        reject(response);
      }
    }, () => {
    });
  }),
  get: function (path, params) {
    let stream = this._check();
    if (params) {
      let tmp = querystring.stringify(params);
      if (path.indexOf('?') == -1) {
        tmp = '?' + tmp;
      } else {
        tmp = '&' + tmp;
      }
      path += tmp;
    }
    return stream.get(path);
  }
```

画面 9:
```javascript
methods: {
  request.get (url, params) {
    const self = this;
    const index = e.page;
    alert(e.page);
    this.load();
  }
},
```

画面 10:
```java
Integer countId;
// 最大时间
Date maxBhotTime;
// 最小时间
Date minBhotTime;
// 分页大小
Integer size;
// 资源范围，比如频道 ID
String tag
```

画面 11:
```javascript
methods: {
  request.get (url, params) {
    const self = this;
    const index = e.page;
    alert(e.page);
    this.load();
  }
},
```

画面 12:
```text
failed to compile.
./node_modules/babel-loader/lib/.node_modules/Vue-loader/lib/selector.js?type=script&index=0!./src/pages/home/index.Vue
Module not found: Can't resolve 'common/request' in 'D:\heima\leadnews.code\heima-leadnews-app\src\pages\home'
```

画面 13:
```html
<wxc-pan-item text-id="1" + (v) + ' + ' + (key)>
  <div class="content">
    <text>{{key}}</text>
  </div>
</wxc-pan-item>
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 3: 展示了 Weex Playground 中 `wxc-tab-page` 组件的配置参数表，表格包含列：可配置参数、Type、Required、Default、Description。
画面 5: 展示了文档内容，标题为“2.2.1 在 src/pages/home/index.Vue 中定义 Model”。

5) 无。

