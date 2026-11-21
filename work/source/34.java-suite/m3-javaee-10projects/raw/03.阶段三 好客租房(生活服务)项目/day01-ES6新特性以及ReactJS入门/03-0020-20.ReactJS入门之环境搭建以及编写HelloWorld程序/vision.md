# 画面线理解：20.ReactJS入门之环境搭建以及编写HelloWorld程序

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day01-ES6新特性以及ReactJS入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day01-ES6新特性以及ReactJS入门\20.ReactJS入门之环境搭建以及编写HelloWorld程序【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:11, 00:54, 01:44, 03:18, 04:50, 05:17, 05:48, 06:53, 08:25, 09:45, 11:50, 12:43, 13:54, 14:26
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:10:30

1) 这一组画面整体在讲如何使用 Umi 框架创建并运行一个 React 项目，包括项目初始化、配置文件修改、页面开发和构建部署。

2) 按时间顺序列出每张画面的要点：
画面 1: 在 IntelliJ IDEA 中，通过“New Project”对话框选择“Static Web”模板，项目名称为“itcast-reactjs”，项目路径为“F:\code\itcast-reactjs”。
画面 2: 显示了新建项目后的项目结构，包含“src”、“config”、“pages”等目录，以及“package.json”等文件。
画面 3: 在终端中执行命令 `yarn add umi --dev`，安装 Umi 作为开发依赖。
画面 4: 在 `package.json` 文件中，添加了 `"devDependencies": { "umi": ">=2.4" }`，并执行 `yarn install` 安装依赖。
画面 5: 展示了 Umi 项目目录结构，包括 `src`、`config`、`pages` 等目录，并在 `config.js` 中添加了 `export default {};`。
画面 6: 在 `config.js` 中添加了 `plugins: ['umi-plugin-react', { //暂时不启用任何功能 }]`。
画面 7: 在 `HelloWorld.js` 文件中添加了 `export default () => { return <div>Hello world</div>; }`，并启动开发服务器。
画面 8: 浏览器显示了 Umi 开发服务器的 404 页面，提示创建 React 组件。
画面 9: 在终端中执行 `umi dev`，启动开发服务器，显示编译成功并提供本地和网络访问地址。
画面 10: 在 `config.js` 中添加了 `plugins: ['umi-plugin-react', { //暂时不启用任何功能 }]`。
画面 11: 在终端中执行 `umi build`，进行项目构建，显示构建成功并输出文件大小。
画面 12: 在 EditPlus 编辑器中打开 `dist/umi.js` 文件，显示了构建后的 JavaScript 代码。
画面 13: 在 EditPlus 编辑器中打开 `dist/umi.js` 文件，显示了构建后的 JavaScript 代码，其中包含 `use strict` 和 `Symbol` 等内容。
画面 14: 在 IntelliJ IDEA 中，通过“New Project”对话框选择“Static Web”模板，项目名称为“itcast-reactjs”，项目路径为“F:\code\itcast-reactjs”。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 3:
```bash
F:\code\itcast-reactjs>yarn add umi --dev
yarn add v1.12.1
info No lockfile found.
[1/4] Resolving packages...
... to regex@3.0.2
```

画面 4:
```json
{
  "name": "itcast-reactjs",
  "version": "1.0.0",
  "license": "MIT",
  "devDependencies": {
    "umi": ">=2.4"
  }
}
```

画面 5:
```js
// 导出一个对象，暂时设置为空对象，后面再填入内容
export default {};
```

画面 6:
```js
export default {
  plugins: [
    'umi-plugin-react',
    //暂时不启用任何功能
  ]
};
```

画面 7:
```js
export default () => {
  return <div>Hello world</div>;
};
```

画面 9:
```bash
success webpack compiled in 636ms
DONE. Compiled successfully in 6645ms
App running at:
- Local: http://localhost:8000 (copied to clipboard)
- Network: http://172.16.55.194:8000/
```

画面 11:
```bash
F:\code\itcast-reactjs>umi build
[16:10:44] webpack compiled in 5s 983ms
DONE. Compiled successfully in 3992ms
File sizes after gzip:
77.24 KB dist/umi.js
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 5: PPT 标题为“2.3.1. 创建项目”，内容包括“我们依然选择使用UmiJS作为构建工具”。
画面 6: PPT 标题为“2.3.2. 配置项目”，内容包括“在config.js文件中输入以下内容，以便后面使用”。
画面 7: PPT 标题为“2.3.3. 创建页面”，内容包括“在HelloWorld.js文件中输入如下内容”。
画面 9: PPT 标题为“2.3.4. 构建和部署”，内容包括“现在我们写的js，必须通过umi编译后才能正常的执行”。

5) 无。
