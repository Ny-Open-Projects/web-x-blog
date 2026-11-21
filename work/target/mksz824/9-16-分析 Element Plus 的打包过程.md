# 9-16-分析 Element Plus 的打包过程

上节课我们使用 npm link 在本地测试了组件库的打包情况。了解我教学方式的同学知道，在一块内容的最后，我喜欢来一个源码分析。这节课分析优秀的开源组件库是怎样打包的，选用 Element Plus 作为分析对象，只分析 es modules 模块打包生成的过程，其他类型的模块大家可以自行去了解。

首先把它的代码 clone 下来。第一步来到 package.json 文件，观察它的入口文件。在最下面可以看到，它的入口文件和我们的非常类似，也是这几个字段：main、module 和 typings。main 对应的一般是 UMD 格式，指向 lib 下面的 index.js；module 对应 es module 格式，指向 lib 下面的 index.esm.js；还有 typings，类型文件，对应 lib 下面的 index.d.ts。初步猜测它应该也会生成这两种模块类型。

下面的任务就是找哪个命令用来生成 ES modules 的代码。看 scripts 里的一系列命令，往上翻可以看到密密麻麻各种各样的命令，大家别被吓坏。明确目的：找 build 命令，和我们的一样，它也有一个 build。build 是由一系列命令组成的，用 && 符号连接了一大堆 build。最前面是 yarn bootstrap 和 yarn clean:lib，从名称就知道是做前期准备工作，可能是删除文件夹、frozen 一些 lock file，我们不管，只看后面的。后面都是以 yarn build: 开头的一系列命令，每个 build 代表要生成不同的最终内容。我们只关注 ESM，所以聚焦在 `yarn build:esm-bundle` 上，顾名思义，这一看就是生成 ESM 模块的 bundle 文件，应该就是我们要找的。

看这个命令，感觉非常亲切。它由两部分组成：前面是 `rollup --config` 加一个配置文件，这是学了这么久的部分，非常熟悉；后面是 tsc 相关的命令，用来生成一系列 types 文件，我们不管，只看前面。

和配置文件打了这么长时间交道，打开这个 rollup.config.bundle.js 一看，映入眼帘的是非常熟悉的配置：一大堆插件，有 node-resolve（直接 import node_modules 下的模块）、TypeScript（已经见识过）、Vue（已经用到了）。唯一没见过的是 terser 插件。它的应用很简单，看文档就知道：它做的事是压缩和混淆代码。还记得我们生成的 ESM 文件内容都是没有经过压缩的，使用这个插件可以进一步压缩和混淆，让体积变得更小。

接下来看 export default 的内容。首先是 input，入口文件是 packages 下的 element-plus/index.ts。打开 index.ts，发现它很长，import 了一大堆组件，但结构和我们非常相似：第一步把所有组件一一导入；然后把 components 放到一个组件数组中；后面还有不一样的，它有一个 plugins 数组，是除组件之外可以作为插件的合集，比如这里的 loading。看一下 loading 的源代码，打开 loading 的 index.ts，它 export default 一个插件对象，上面有一个 install 属性的函数。函数里做两件事：第一，注册一个叫 loading 的 directive；第二，在熟悉的 config.globalProperties 上添加一个全局属性 $loading，这样就可以直接使用这个方法了。

再看 install 的实现：循环 components，调用 forEach，在 forEach 中调用 app.component，传入 component.name 和 component 的真正实现；plugins 也调用 forEach，使用 app.use 循环使用插件。这样就把组件和插件都注册到了 Vue 实例上。最后 export 所有组件，还有一个默认导出：导出一个 object，上面有 version 版本号，还有最重要的 install 方法。所以它的入口文件虽然组件众多，但整体架构跟我们的非常类似。

入口文件分析完了。output 没什么可说的：format 导出的是 es modules，file 的路径是 lib/index.esm.js，正好和 module 字段呼应起来，说明这个命令就是用来生成这种格式文件的。

接下来是添加插件，把插件一一罗列，我们已经很清楚了，只不过它添加了一些针对项目的独特配置，比如 TypeScript 的 override 里加了 include 和 exclude，这是跟它项目相关的，不细看了。最后它的 external 写法有点意思，来分析一下。external 可以返回一个 function，返回布尔值。可以看到它有两种情况，中间用了两个竖线，都返回 true 的话模块就被忽略。第一个是 vue：我们知道 Vue 在 peerDependencies 里，验证一下，打开它的 package.json，Vue 确实在 peerDependencies 当中，所以依赖 Vue 的存在，自然要把它忽略掉。第二个调用了一个 deps：它是从 package.json 里把 pkg 拿出来，`deps = Object.keys(pkg.dependencies)`，把项目的 dependencies 都拿过来，然后表达式采用了一个 some。意思就是把 dependencies 里的内容全都忽略掉。

最终结果就是：假如 import 的是 peerDependencies 里的内容，或者 dependencies 里的内容，都会被忽略掉。这样就完成了入口文件到 ESM 文件的生成过程。虽然它是一个很复杂的项目，但经过这样的分析，它和我们的组件库生成过程非常类似，只不过要生成的内容更多，所以分解成了更多的命令。有兴趣的话，大家可以自己探索其他命令的具体实现。这节课的源码分析就到这里，谢谢大家，再见。
