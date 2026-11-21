# 10-22-egg typescript 支持的原理

通过一系列的课程，我们对 Egg 几大概念已经有了一个粗略的认识。这节课回头来看一下，Egg 是怎样完成 TypeScript 支持的。在使用的过程中，支持 TS 是一项非常大的优势：Egg.js 的文件类型广而杂，在不同类型的文件里可以自动联想出它的属性和方法，对开发过程是一个非常大的红利。

大家都知道，Egg 的源代码不是用 TS 开发的。对 TS 的支持，它提供了 index.d.ts 这个定义文件；同时，在使用 egg-ts-helper 编写代码的过程中，每次保存都会动态生成一系列的定义文件，对现有的类型进行扩充。这节课稍微深入一下，描述它这个 TS 支持和扩充是怎样完成的。

再来看 typings 这个文件夹。不难发现，它的文件结构和我们 app 当中源代码的目录结构是完全一致的。其中 controller 和 service 这两个最好理解：打开对应的文件夹，可以看到它们都有一个 index.d.ts 文件。用 controller 举例，打开这个文件，发现一个很重要的原理：类型重载。它使用 declare 语法，将 egg 这个模块进行多次定义，比如对 IController 进行重新定义，这样新的类型就会源源不断地添加到 egg 的定义当中去。

拿 IController 来说，它会动态地把我们已有的两个 controller 文件的类型，以 class 导入的形式放置到 IController 上面去，这样新的 IController 就有了 home 和 test 这两个属性。看一下 IController 的原始定义：按住 Command 或 Control 点击，会发现它在两处出现，也就是经过了两个文件的重载：一个是我们现在的定义文件，另一个是 egg 本身提供的定义文件。在 egg 的定义文件里，IController 直接 extends 了 PlainObject。PlainObject 是一个类型，就是一个普通的 object，也就是一个 indexable type。IController 在哪里使用？它是 application 上面的一个属性，在这上面就获得了对应的类型，可以进行使用了。在 app.ts 当中做个测试：拿到 this.app.controller，它原始是一个 PlainObject，经过我们自定义文件的加持，home 和 test 这两个属性都已经添加上去，重新获得对应的定义了。service 和 controller 都一样，这里就不多说了。

用图来看一下这个过程：应该有两层。最下面一层是 egg 模块本身的定义文件，它首先定义了 IController 是一个 PlainObject；然后自动生成的 typings 文件夹往上加属性，重新进行一次重载，把 home 和 test 这两个属性添加上去，最终就生成了 IController 最终的类型。

说完 IController，接下来说 config。config 是属于比较复杂一点的类型，点开看它的原理跟 controller 是完全一致的：egg 内置的定义文件定义了内置的 config 类型，然后把我们在配置文件中定义的业务逻辑配置导入，也进行一个类型的重载，照猫画虎。这样新的 EggAppConfig 就包括内置类型和业务逻辑配置两部分了。在 app.ts 中举例也能发现这一点：this.app.config，其中 baseURL 是业务逻辑的配置，而 view 或者 multipart 都是内置的类型，所以我们就获得了这两部分的类型定义。

当然它这里有一点新的花样。回到类型文件，点一下看这个类型是怎样组合生成的：会发现这个类型被重载了很多次。最下面一个是刚才说的业务逻辑定义类型；倒数第二个是 egg 模块的类型，看文件来源可以看到来自 egg，它定义了最开始的 EggAppConfig，里面有一些配置，还有一些默认要启用的中间件的配置，比如之前说过的 bodyParser 的一些配置，还有 logger 的一些配置，这些都是内置中间件的定义。再打开上面第二个文件，从文件名可以看到它来自 node_modules 下面的 egg-view 这个模块。大家都知道这是一个插件，所以每个插件都可能有自己的一份配置：它在这里添加了 view 这么一个属性和一系列的配置，所以 this.app.config.view 里面含有的这一系列属性，其实就是从这个插件的定义里来的。最上面的一个类型来自 egg-multipart，也是一个插件，帮助 egg 上传复杂类型文件的，在这里定义了 multipart 参数的格式，比如 mode、fieldSize 等等。

了解了以后，用图表的方式对类型进行描述：会多一层。最下面是本体核心包的定义，中间有多个插件的一系列配置：view 插件会扩充一个 view 这样的属性，multipart 会扩充一个 multipart 属性；最上面是我们自动生成的业务逻辑配置的一系列属性。把这几项类型都添加起来，就获得了最终的 appConfig 类型。

再举一个和 config 非常类似的例子：app 类型最终生成的过程。点开 extend 里面的 application，会发现它和之前的运作非常一样，也会经过多次重载。上面那层点开发现是老朋友 egg-view：它作为一款插件，不仅扩展了对应的 config，还会把 application 和 context 都进行一一的扩展，所以我们就可以在调用 app 以及 ctx 的时候使用对应的属性和方法了。比如 ctx 上面有一个 render 方法，其实就来自 egg-view 的扩充；看 view 的基础定义（view.base），上面有 render、renderString、renderView 等方法。它还在 app 上进行了扩展，就是 this.app.view，这属于 application 上面的扩展，在这里也能找到。

所以我们也更了解了插件的内容：它其实有点像一个迷你的小应用，里面有配置、有扩展、有自定义启动、service 等等。所以假如你自己开发一个 plugin 插件，为了让它支持 TypeScript，要特别注意创建一个 index.d.ts，并且将扩展的类型都添加进去。官方文档也是这么说的：插件有一个 TypeScript 插件的类别，可以参考 ts-helper 自动生成的格式，在插件根目录创建 index.d.ts，然后 declare module 'egg'，把这些扩展进行一一的定义，这样就完成了整个的过程。

这就是 egg 类型文件的运作方式：采用类型重载的模式对类型进行多次定义，并且组合生成最终非常丰富的类型提示，帮助我们进行开发。
