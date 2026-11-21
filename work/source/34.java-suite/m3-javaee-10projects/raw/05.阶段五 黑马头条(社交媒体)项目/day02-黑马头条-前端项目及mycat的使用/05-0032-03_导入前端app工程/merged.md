# 03_导入前端app工程

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day02-黑马头条-前端项目及mycat的使用
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day02-黑马头条-前端项目及mycat的使用\03_导入前端app工程【海量资源尽在 666java.com】.mp4
- 时长 4分18秒（音频 258s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就把咱们的APP的前端工程导入到咱们的开发工具里边啊那这个这个工程单展呢这工程是在当前第二天的资料中有一个前端项目项目里边就是这么一个无念你呀叫黑马leader news appok啊然后这时候呢你把它拷贝到一个干净的目录下边你看我这是拷到了当前地盘有一个黑马leader news有一个code哎这里边是
[00:29] 把它拷到了这那拷到了这之后呢你就可以用当前的外部SOM这个开发工具打开就可以啊打开完之后呢咱们首先呢可以启动一下看一下这个运行的效果来启动非常简单右键有一个什么show npm script是吧然后是点start就可以了好那这时候呢它就是正在启动稍等一下启动完之后呢它会自动去帮你打开一个页面
[01:01] 然后启动完之后呢这边就能去展示当前的一个效果稍等好这边已经是百分之四五十了稍等一下好九十好了啊那这时候已经启动完了啊那启动完之后呢就是这么一个效果那这个效果呢其实呢是咱们的前端人员后期呢又去做了一些这种开发你看比如说这里边有一些菜单是吧呃什么家伙啊pason啊没有是吧还有下面有问题啊视频我的是吧
[01:32] 咱们主要呢是基于当前的这个架子呢进行咱们的业务开发就可以当然那这里边啊大家也能看明白啊那这块呢是一个手机对吧是一个移动端那你说我能不能用手机去调试呢也可以也是可以的啊那这时候呢你点开它稍等这网络稍微有点慢啊那这时候呢你需要在你的手机上去下载一个客户端
[02:00] 那安卓呢就下载安卓就行了如果是iOS那就下载一个iOS那下完之后呢里边呢是有一个扫码的功能你只要把这个码扫完之后呢就能在手机上进行调试但是呢这一块呢是有个问题什么问题呢就是要求啊你必须选用什么要求呢就是你的电脑跟你的手机必须在同一个局域网下边你才能去用同时呢你要去修改两部配置文件
[02:30] 比如说来看一看当前的啊这有一个配置文件有一个config有一个config.js啊在最上面啊这有一个IP这个IP是谁呢这个IP应该是你电脑本机的IP那这个IP你怎么查呢其实非常简单右键打开啊不对啊应该是这样右键啊双击行了双击然后是点点下属性
[03:03] 属性完之后呢这块呢是有一个IP你看我的IPv4这个地址呢是192.168.25.3所以说你在这儿也应当设置的是当前的这个地址那这是一处啊应该还有第二处第二处是当前的webpackdv.config.js啊这里边呢也是你要设置同一个IP地址就可以了那这时候呢你下载完客户端之后扫描这个码就可以比如说来我给你们打开一个演示一下
[03:32] 稍等好下面呢我就给你们演示一下我这边是连上了一个客户端来打开这个呢就是我的手机然后你下载完之后呢就是这么一个东西就这么个东西啊然后你点开它比如我在手机上去点操作一下而这里边呢就可以有什么教程啊实力啊咨询和关于那这时候上面还有一个叫扫描二维码看到了吗OK你点一下扫描二维码啊就直接扫描当前的二维码就可以点
[04:05] 好大家能看到像现在我的手机上也出来了这么一个界面看到了吗我也可以在这边去进行选到开发的时候呢咱们就可以在这上面进行调试

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 WebStorm 中导入并运行一个 Weex 项目，配置开发环境，并通过 Weex Playground App 在手机上预览应用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 Windows 文件资源管理器中，定位到 day02 文件夹，选中名为 "weex启动流程.png" 的图片文件。
画面 2: 在 WebStorm 中打开项目 "heima-leadnews-app"，在左侧项目结构中选中 "package.json" 文件，右键选择 "Run 'start'"。
画面 3: 在 WebStorm 中，项目结构中选中 "package.json"，终端中显示构建过程，进度为 25%。
画面 4: 终端中构建进度更新至 26%，显示正在处理多个 .Vue 文件。
画面 5: 终端中构建进度更新至 55%，显示正在处理多个 .js 文件。
画面 6: 在 WebStorm 中，项目结构中选中 "package.json"，右键选择 "Run 'start'"。
画面 7: 在浏览器中打开 Weex Preview 页面，显示一个手机界面的预览，包含搜索框和底部导航栏，右侧有一个二维码。
画面 8: 在 WebStorm 的文档中，显示了关于运行命令和配置的说明，提到可以使用 "npm run serve" 命令或扫描二维码在手机上体验。
画面 9: 在 WebStorm 中，打开 "config" 文件夹下的 "config.js" 文件，显示了配置代码，其中包含 "devtool"、"env"、"cacheBusting"、"cssSourceMap"、"proxyTable" 等配置项。
画面 10: 在 WebStorm 中，打开 "config" 文件夹下的 "config.js" 文件，显示了配置代码，其中包含 "root"、"host"、"port"、"historyApiFallback" 等配置项。
画面 11: 在 WebStorm 中，打开 "config" 文件夹下的 "config.js" 文件，显示了配置代码，其中包含 "root"、"host"、"port"、"historyApiFallback" 等配置项。
画面 12: 在 WebStorm 中，打开 "config" 文件夹下的 "webpack.dev.conf.js" 文件，显示了配置代码，其中包含 "const chalk = require('chalk');"、"const path = require('path');"、"const webpack = require('webpack');" 等配置项。
画面 13: 在手机屏幕上，显示了 Weex Playground App 的界面，点击了 "扫描二维码" 按钮。
画面 14: 在电脑屏幕上，显示了 Weex Preview 页面，浏览器地址栏显示 "http://192.168.253.3:8082/dist/index.html"。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 9:
```javascript
// https://webpack.js.org/configuration/devtool/#development
devtool: 'eval-source-map',
env: JSON.stringify('development'),
// If you have problems debugging webpack files in devtools,
// set this to false. It may help
// https://Vue-loader.vuejs.org/en/options.html#cachebusting
cacheBusting: true,
// CSS SourceMaps off by default because relative paths are "buggy"
// with this option, according to the CSS-Loader README
// https://github.com/webpack/css-loader#source-map
// In our experience, they generally work as expected,
// just be aware of this issue when enabling this option.
cssSourceMap: false,
proxyTable: {
  '/toutiao': {
    target: 'https://m.toutiao.com/', //新闻地址
    changOrigin: true, //是否跨域
    pathRewrite: {
      '/toutiao': ''
    }
  }
},
autoOpenBrowser: false
```

画面 10:
```javascript
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
let ip = require('ip').address('WLAN');
const config = {
  root: ROOT,
  host: '192.168.253.3',
  port: 8081,
  historyApiFallback: true
};
```

画面 12:
```javascript
const commonConfig = require('./webpack.common.conf');
const webpackMerge = require('webpack-merge');
const chalk = require('chalk');
const path = require('path');
const webpack = require('webpack');
// root ip
let ip = '192.168.253.3';
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '127.0.0.1';
// const ip = require('ip').address('WLAN');
// const ip = '1

