# 10-17-Config 配置文件第一部

到目前为止，我们已经了解了 controller、service、plugin 以及 middleware 这几大概念。现在来学习一个老朋友：config 配置。为什么说是老朋友？因为在前面的课程中我们已经多次修改过配置中的值。Egg.js 提供了强大而且可扩展的配置功能，可以自动合并应用、插件、框架的配置，并且按顺序进行覆盖，还可以根据不同的环境维护不同的配置。

仔细看一下 config.default.ts，它导出了一个 function，这个 function 当中有一个特殊的参数，称之为 appInfo。appInfo 是 Egg.js 的一个内置类型，是 EggAppInfo 类型。与之对应的信息，都是和应用有关的一系列内置信息。用自动联想看看，它有这么多信息。简单总结一下它们的作用：appInfo 上的 pkg 就是 package.json；name 就是 pkg.name；baseDir 是应用代码的目录；home 是用户的目录；root 是应用的根目录。根据不同的环境，这些值也都不同，所以说它是一系列与应用相关的内置信息。

在配置中，我们一般会配置两大类信息。第一种是应用本身的信息，以及内置插件、内置中间件的一系列配置。这些配置目前都是可以自动联想出来的。比如 config.keys，注释里写了它是为 cookie sign key 服务的，所以添加了一段随机字符串。第二个是 middleware，可以添加你一系列自定义的中间件。除了这两部分，自动联想出来的还有 config.name、config.env 等，这些都是应用本身的信息。

接下来是内置插件的信息。框架内置了一系列常用插件：onerror、session、i18n、watcher、multipart、security 等等。我们这里已经使用过 security，改了一个 CSRF，其实它有更多，比如 xframe、xssProtection 等，这些都可以联想出来并进行修改。view 也是一个对应的插件。

除了插件，还有一系列内置中间件。内置中间件从联想中可以看到，比如 bodyParser，之前提过，它用来将不同类型的 body 转换为 JavaScript object。比如可以设置 `bodyParser.jsonLimit = '10mb'`，也就是控制 JSON 格式的最大大小为十兆，比这个大的话就会抛出错误。

这一系列的配置之后，就是我们的业务逻辑配置了，里面可以包括普通的业务配置、自定义中间件的一系列配置等等。大家应该觉得奇怪：为什么要把它写成两部分？直接在 config 上面写这些配置难道不可以吗？看起来是一个意思，这样做是不是画蛇添足？其实这是为 TS 所考虑的：为了让这部分的配置选项在其他文件中也可以获取类型的自动联想。怎样实现的，下节课再说，这里先按照这样的规则书写。

说完第一个问题，也就是 config 文件的结构问题，能写哪些配置项，再说另一个重要问题：config 的多环境配置。这是一个非常常见的需求，因为程序需要在不同的环境中运行，比如本地开发环境、测试环境、生产环境等等。可以看到，除了 default 这个文件，已经存在两个文件，分别是 local 和 production。看这两个文件顾名思义就知道，不同环境的特殊配置可以添加到这两个文件当中。

最终的配置文件可以根据环境的不同，同时加载默认配置和对应的配置文件。在这个文件中，具名配置和默认配置将进行合并，合并使用的是深拷贝的模式，具名配置会覆盖默认配置的同名配置。比如在 production 环境下，就会加载 production 和 default 两个文件，production 里面相同的值会覆盖 default 里的值，最终合并成一份最终的配置。

现在用业务逻辑的值做一个实验。一个常见的需求是在不同环境下可能有不同的 URL 地址。这属于业务逻辑，所以添加到 baseConfig 里，称之为 baseURL，默认值是 defaultUrl。先测试开发环境，也就是 config.local.ts，它对应开发环境，把值修改为 baseURL 等于 localUrl。特别注意这里还没有自动联想，大家不要写错。然后在 test 的接口里对它进行输出，看得更清楚一些。配置可以从 ctx.app.config 当中拿到，输出 baseURL 到 response 里，保存看结果：这时输出的是 localUrl，说明 local 的配置已经覆盖了 default 配置，最终以 local 为准。

有的同学可能会说，local 环境是怎么和 npm run dev 这个命令绑定的？这是 Egg 框架内置的一个环境变量指定的。dev 命令明显是为本地开发服务的，运行这个命令时会设置对应的环境变量为 local，这样就会加载里面的值。

第一个任务完成，再测试一下 production 看生产环境是否好用。一样是 config.baseURL，应该等于 productionUrl。现在的任务是运行 production 环境的应用。打开 package.json，滑到 scripts 的命令，可以看到有一个 npm run start。本地开发和生产环境的目的不同：dev 命令（egg-bin run dev）会针对本地开发做很多处理，而生产运行需要一个更加简单稳定的方式，同时这个命令会使用 production 作为环境变量，对应到 config 中 production 相关的配置。

运行这个环境命令之前要特别注意：不要直接运行它，因为这个命令是直接运行最终生成的 JS 代码的。dev 其实做了两步事情：第一步是构建 TS 到 JS 的过程，第二步才是运行程序。这里我们要单独运行一个命令：首先运行 tsc。tsc 之前还有个 ets 命令，它的第一步是生成对应的 typings 文件，为我们的 TypeScript 服务，一系列联想在里面都有。打开随便一个 controller 可以看到，它会把 home、test 这些 controller 的内容导进来。运行完 ets 以后，再运行 tsc -p 这个命令，生成最终的 JS 代码。

先把之前的进程退出，然后运行第一步 npm run tsc。可以看到它 create 了一系列 helper，然后每个 TS 文件都会生成一个同名的 JS 文件，这就是编译的过程。但可以看到一个奇怪的现象：这些文件都是灰色的。这跟我们的 .gitignore 有关系：它会把所有 JS 相关的代码都加到 .gitignore 当中，所以它们不会被 git 管理。这也是使用 TypeScript 新建项目时悄悄添加的一个规则：不会将任何 JS 代码添加到代码库当中。

生成完毕后，就可以运行 npm run start。当这里输出 egg started on 7001，说明应用已经成功启动了，并且是以生产环境的模式启动的。访问一下看最终结果：baseURL 已经被覆盖变成了 productionUrl，说明配置文件的覆盖成功了。

通过这节课我们学习到了关于 Egg.js 配置文件的知识。下节课再深入讲解怎样让配置文件更好地和 TypeScript 结合起来。
