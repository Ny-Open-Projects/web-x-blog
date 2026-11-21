# 9-15-使用 npm link 本地测试组件库

上节课完成了生成两种格式文件的工作，现在看我们 build 出来的文件都差不多了。在组件库发布之前，有一个很重要的环节：在本地测试一下打包出来的文件是否好用。因为现在输出的不是原来的 build 文件，而是 ESM 和 UMD 两种文件，本地测试是一个非常常见的需求。

我们要在其他的 Vue 3 项目中使用 OpsFlow 组件库，常见的做法是：在另一个项目的 package.json 中声明这个依赖，OpsFlow 组件库已经发布到 npm 上，用 npm install 安装。但现在有个需求：假如 OpsFlow 组件库在本地有一个新的修改，比如改变了 LText 组件的样式，需要在使用它的项目里测试。最笨的方法是发布一个新版本到 npm，然后修改测试项目的版本号，重新安装再测试，特别费时费力。

如果有一个方法可以直接把这个依赖关联到本地文件系统就好了：不是从 npm registry 下载，而是直接关联到本地。npm 推出了一个功能叫 npm link，可以把项目中的依赖 link 到本地。

过程是这样的：先来到需要被依赖或链接的文件夹中，运行 `npm link`。等一下之后会看到一个提示，它创建了一个软链接，链接到 lib/node_modules，也就是在全局环境中创建一个软链接，指向我们本地的 OpsFlow 组件库。然后在使用它的地方，比如 v3-ts-basic 这个项目，运行 `npm link OpsFlow-components`，它就在项目的 node_modules 文件夹下创建链接。看一下链接的过程：从本地实现链接到全局，再通过全局链接到真正使用它的项目。等于经过全局这个中转站，v3-ts-basic 引用组件库的时候就等于在引用本地的文件夹，这就是 npm link 的妙用。

这里还要修改一点：导入组件库的时候，怎么知道它引用的是哪个文件呢？需要在组件库里做一些修改。回到 OpsFlow 组件库项目，打开 package.json，添加一些字段确定入口文件。第一个大家都熟悉：package.json 有一个特殊字段 main，规定一个包的入口文件，它是伴随 Node.js 诞生而出现的标准。main 要指向 dist 下的 OpsFlow-components.umd.js，也就是 UMD 格式。

当然我们还创建了 ESM 格式，它怎么使用呢？这里还有一个非官方的字段，但已经到了 proposal 的阶段，称为 module。由于 package.json 的概念一开始是服务于 Node.js 的，main 字段的文件很可能是 CommonJS 格式的；为了使用 ES6 modules、享受 tree shaking 的红利，Webpack 和 Rollup 联合推出了 module 字段，专门对应 ES6 modules 的入口文件路径。当你使用 Webpack 或 Rollup 引入一个包时，如果支持 pkg.module 字段，会优先使用 ES6 模块规范的版本，这样就可以使用 tree shaking 机制。我们的库输出了两种格式，这里就对应写上 ES modules 格式的入口。这样根据不同的场景，它会自动选择哪个入口文件进行加载。最后还要把 types 加上，也就是 TypeScript 的入口文件，当然是 index.d.ts。

添加完毕后，来到使用它的项目 v3-ts-basic。为了提示引用正确，我先在 package.json 中添加了一个假的 OpsFlow-components 版本，然后在 main.ts 引入：`import OpsFlowComponents from 'OpsFlow-components'`。保存后点过去可以看到，它跳转的地址是 OpsFlow 组件库 dist 下面的 index.d.ts 定义文件，说明链接完全成功了。

接下来把样式文件一并引入测试，它在 dist 下面的 bundle.css。因为组件库是一个插件，采用全局插件化的方式，所以可以用 use 调用。这时我们发现它报出了一个类型错误。假如你用的是 JS 测试项目，这个错误是不会出现的，只有 TS 项目才有。提示非常长，我直接解释一下大体原因：OpsFlow 组件库项目中使用的是自己 node_modules 下面的 Vue 的 App 类型，use 的 plugin 参数类型是它自己的 App 类型；而测试项目 node_modules 中的 Vue 的 App 类型，因为两个 Vue 的版本不一样，类型就不一样，于是报出这个错误。真实场景下不会出现，因为真实场景下组件库的 Vue 在上节课添加的 peerDependency 中，使用的是主项目的 Vue 版本。

所以这里要暂时做一个处理，让组件库使用测试项目也就是 v3-ts-basic 中的 Vue 版本，两个项目使用相同的 Vue 依赖。方法还是 npm link：先来到 OpsFlow 组件库项目，然后到上一层，也就是 v3-ts-basic 项目的 node_modules/vue，对它运行 npm link。这样组件库的 vue 就 link 到了使用它的项目中的 vue 版本。运行后它创建了一堆软链接，两个项目使用了同样的 Vue 版本。再看，错误消失了，问题迎刃而解。

现在总算可以开始测试了。来到 App 中添加一个 LText 作为测试，保存后运行项目。发现出现了一个编译错误，是 ESLint 报出来的：因为现在的依赖是 link 过来的，并不在 node_modules 中，所以 ESLint 没有忽略它，好心地把这个文件 lint 了一遍，发现一堆错误。这是打包好的代码，当然无法通过 ESLint 的检验。这个在真实场景中也不会出现，因为真实场景组件库肯定在 node_modules 中。所以这里来个暂时很 low 的做法：直接来到组件库的 ESM 文件顶部，加一个 eslint-disable 注释，让 ESLint 放过它。这时候就成功了。

刷新一下，可以看到组件出现了，Hello there 显示出来，选一下发现样式也都添加上去了，打包出来的样式文件里的简单样式也都生效了，没问题。项目现在总算通过测试了。npm link 过程一波三折，也学到了很多知识。我们发现，打包后的代码可以成功地在其他 Vue 3 项目中完美运行。这节课就到这里，谢谢大家，再见。
