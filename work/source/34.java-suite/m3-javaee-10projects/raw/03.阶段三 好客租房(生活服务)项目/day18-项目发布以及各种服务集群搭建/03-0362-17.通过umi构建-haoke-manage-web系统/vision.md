# 画面线理解：17.通过umi构建-haoke-manage-web系统

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day18-项目发布以及各种服务集群搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day18-项目发布以及各种服务集群搭建\17.通过umi构建itcast-haoke-manage-web系统【海量资源尽在 ubkz.com】.mp4
- 抽帧：12 帧 @ 00:01, 00:12, 00:13, 00:52, 01:20, 01:25, 01:40, 01:42, 01:48, 01:49, 01:53, 02:08
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:57:43

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
