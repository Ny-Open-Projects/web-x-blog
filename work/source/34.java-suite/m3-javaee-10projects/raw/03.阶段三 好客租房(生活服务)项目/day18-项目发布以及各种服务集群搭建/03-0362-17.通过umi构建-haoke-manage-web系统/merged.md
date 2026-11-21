# 17.通过umi构建-haoke-manage-web系统

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day18-项目发布以及各种服务集群搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day18-项目发布以及各种服务集群搭建\17.通过umi构建itcast-haoke-manage-web系统【海量资源尽在 ubkz.com】.mp4
- 时长 2分18秒（音频 138s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来部署一下我们的后台系统的这个前端啊就是因为我们做的前后端分离嘛那么我们来部署一下它那么大家应该还记得我们的前后端的分离的时候在部署的时候啊那么需要注意一下就是我们的这个前端的使用是按照designpro去做一个构建的那么我们需要通过我们的5米的去做一个build
[00:23] 那么这样的话它会帮我们去构建生成静态页面最终我们只需要去部署这个静态页面就可以了但是需要我们注意两点内容第一点就是我们生成的这个静态页面那么我们必须要通过一个web服务器去做一个支持访问才可以那么所以我们会选择使用ngx来作为一个web服务器去做这样的一个使用这是第一点那么第二点就是
[00:51] 我们呢在之前我们在我们的这个5米的中网配置其中配置了一个代理它这个代理呢是由我们在5米启动的时候它去生成的一个web服务那么这个呢不适合用于我们的这个生产环境所以呢我们需要自己呢在Nginx中做这样的一个代理的一个配置啊才是可以的好嘞那么这个呢我们把这两点先提出来我们一点一点来去解决这个问题啊
[01:18] 那么首先呢我们先来去把我们这个项目的做一个这个构建那么让他去构建生成我们的一个精彩页面那么把刚刚的这个命令拷贝过来就污名build这个命令那我们就去等待他的一个执行那么执行成功之后呢他就会去生成我们这个最终的一些这个精彩页面啊那我们稍微等待一下好那么这个呃污名呢就已经build结束了结束之后呢他在我们项目中呢就会有这样的一个目录产生就是dist
[01:48] 那么在这个里面呢就会生成一些我们最终所要去执行的一些这个静态的一些页面那么大家最终我们其实要访问的呢其实是在下面的这个有一个index.html这样的一个页面那么前面我们也说过这个呢是需要静态页面的是需要通过Nginx是不是去做一个这个支持的所以说接下来我们需要去安装我们的Nginx好那么关于我们这个安的底站啊它的一个这个构建那么我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示在 IntelliJ IDEA 中编辑 Ant Design Pro 项目的 config.js 配置文件，配置代理、样式加载等选项，并展示构建后生成的静态资源文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 IntelliJ IDEA 中打开项目，选中 config.js 文件，查看 proxy 配置，target 为 http://127.0.0.1:18080，changeOrigin 为 true，pathRewrite 为 '^/haoke/'。
画面 2: 展示 Typora 编辑器中的测试文档，包含一个 HTTP 请求示例，URL 为 http://127.0.0.1:1001/，请求体为 {"code": 1002, "msg": "登录成功"}，响应体包含 "data" 字段。
画面 3: 同画面 2，但 Typora 窗口显示了“博学谷”水印。
画面 4: 在 IntelliJ IDEA 中，项目结构视图中选中了 node_modules library root，同时 config.js 中 proxy 配置的 target 为 http://127.0.0.1:18080。
画面 5: 展示 Typora 中的文档，标题为“第二步：执行打包命令”，包含命令 mvn install -Dmaven.test.skip=true 和 umi build。
画面 6: 在 IntelliJ IDEA 中，config.js 文件中 proxy 配置的 changeOrigin 为 true。
画面 7: 在 IntelliJ IDEA 中，项目结构视图中选中了 dist 目录，同时 config.js 中显示了 disableRedirectHoist: true。
画面 8: 在 IntelliJ IDEA 中，config.js 文件中显示了 cssLoaderOptions: { modules: true, getLocalIdent: ... } 的配置。
画面 9: 同画面 8，但项目结构视图中选中了 dist 目录下的 1.async.js。
画面 10: 同画面 8，但项目结构视图中选中了 dist 目录下的 2.async.js。
画面 11: 同画面 8，但项目结构视图中选中了 dist 目录下的 3.async.js。
画面 12: 同画面 8，但项目结构视图中选中了 dist 目录下的 52.chunk.js。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```javascript
'primary-color': defaultSettings.primaryColor,
externals: {
  '@antv/data-set': 'DataSet',
},
proxy: {
  '/haoke': {
    'target': 'http://127.0.0.1:18080',
    changeOrigin: true,
    pathRewrite: { '^/haoke': '' }
  }
},
ignoreMomentLocales: true,
lessLoaderOptions: {
  javascriptEnabled: true,
}
```

画面 5:
```bash
mvn install -Dmaven.test.skip=true
umi build
```

画面 8:
```javascript
ignoreMomentLocale: true,
lessLoaderOptions: {
  javascriptEnabled: true,
},
disableRedirectHoist: true,
cssLoaderOptions: {
  modules: true,
  getLocalIdent: (context, localIdentName, localName) => {
    if (
      context.resourcePath.includes('node_modules') ||
      context.resourcePath.includes('ant_design_pro.less') ||
      context.resourcePath.includes('global.less')
    ) {
    }
  }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2: PPT 标题为“4.7. 测试”，内容包含一个 HTTP 请求示例，URL 为 http://127.0.0.1:1001/，请求体为 {"code": 1002, "msg": "登录成功"}，响应体包含 "data" 字段。
画面 5: PPT 标题为“第二步：执行打包命令”，内容包含命令 mvn install -Dmaven.test.skip=true 和 umi build。
画面 8: 无 PPT 内容。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

