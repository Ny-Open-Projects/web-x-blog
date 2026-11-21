# 10-23-eggjs 调试技巧

在基础知识的最后，我们来讲一讲调试的技巧。Egg.js 内置了很多本地调试的手段。现在我们的代码采用的是最落后也是最简陋的 console.log 方式，这种模式在 Node.js 应用中多多少少显得比较简单。这里介绍两种本地调试的手段，帮助大家在之后的开发过程中更好地调试模块。

首先要介绍的是 EggJS 默认启用的日志模块，也就是 logger 插件。之前写 myLogger 这个中间件的时候，我们听说过它的大名，还因为把 logger 写重名了而做过重命名。它的目的是生成日志，这个下节课再展开描述，这里说它一个侧面的作用：输出调试信息。

在 test 接口做个实验。在处理请求的时候需要打印日志，可以使用 ctx 上面注入的 logger 变量。其中有一系列方法，比如 debug，可以记录一些信息。debug 跟 console.log 的语法完全一样，接受的参数也一样。除了 debug，还有别的方法，比如 ctx.logger.info，记录一下 response 的 data。这些方法其实代表了日志内部的信息层级，从高到低有五项：none、debug、info、warn 和 error。看单词就知道它们代表严重的程度：error 表示出现错误，warn 是警告，info 是普通信息，debug 是调试信息。我们把这几个都输出出来做个实验：写一个 warning，最后是一个 ctx.logger.error，输出一个真正的 error，new Error('Whoops')。

写完后访问请求看结果。刷新后可以看到输出了一系列信息。从 info 开始，除了要输出的对应信息（resp.data 这个 object），还有很多额外的信息：发送请求的时间、类型、花了多长时间、IP、method 是 get，还有 URL 等等。同时，当输出一个 error 的时候，它会把错误的堆栈输出出来，很方便找到错误出现在哪里。

不过这里发现一个问题：我们写的 debug 没有出现，第一个出现的是 info，没找到 debug 的信息。原因是 Egg.js 默认有一个配置：默认只会输出 info 及以上，也就是 info、warn、error 这三个层级的日志到终端。所以 none 和 debug 并没有被输出。这时候需要做一个简单的配置。说起配置，来到 config.default.ts：config.logger 下有个配置叫 consoleLevel，看名称就知道是控制在 console 输出什么级别的日志。把它调整成 debug，也就是 debug 级以上都会被输出。保存后重启应用再刷新，最上面 debug 的信息就输出了，说明配置成功了。

这是第一项，输出调试信息。当然在很多情况下只输出调试信息是不够的，一个常见需求是在代码中进行断点调试，这样可以在代码中前进后退，更详细地观测特定步骤中代码运行的结果。看 package.json，这里有一个特殊的命令 npm run debug。它使用和 npm run dev 一样的 egg-bin 工具启动，所以和 run dev 非常类似，只不过 debug 是为调试而创建的，会启动一个特殊的 inspector 协议的应用供你调试使用。

这里讲 VS Code 的调试方法，因为它最简单易用。如果你想用 Chrome 调试，或者用 WebStorm 等其他编辑器调试，可以直接看官方文档，写得非常清楚。VS Code 内置了强大的调试功能，支持 Node.js 的运行环境，有三种调试方法：Auto Attach、JavaScript Debug Terminal 和 Launch Configuration。我认为第三种方式 Launch Configuration 最为方便。做法：新建一个文件，放到根目录的 .vscode 文件夹下。我因为改过设置，这个文件夹已经有了，如果没有请自行创建。在里面创建一个 launch.json，特别注意不要拼错，它是 VS Code Debug 的入口配置文件。把配置项直接拷贝过来（代码和文档中都会记录这个配置，到时候直接拷贝就好）。里面的选项顾名思义简单看一下：type 表示什么样的应用；runtimeExecutable 表示用什么来运行，这里当然是 npm；runtimeArgs 是要运行什么样的命令。这三个组合起来就是 npm run debug。console 表示使用什么样的终端，这里是 integratedTerminal，也就是 VS Code 内部的终端。还有端口、restart 等等，一看就知道是什么意思。对每一个配置感兴趣的话，官方文档写得清楚，可以自己看。

设置好以后就可以设置断点了。在 test.ts 里设置一个断点，放到 response 这里。设置完把现在运行的进程关闭掉（不关也可以，但我不想启动两个）。有了断点和 launch.json，就可以启动调试了：到 run 标签下点 start debugging，或者直接按快捷键 F5。点击后它会弹出一系列命令自动运行，可以看到里面有一系列环境变量，然后运行我们已有的程序。运行过程跟 npm run dev 非常相似，也要创建 typings 等等文件。到了 7001 说明运行成功了。这时可以进入调试：访问程序，访问成功后就会在断点处停止，代码已经跑到这里，rest 已经执行，里面有什么数据都可以一一点开查看。你可以进行 Step Over、前进后退等一系列操作，变量在左侧的 Local 和 Global 里都可以观测。断点就可以成功运行了。

通过这节课我们学习了本地调试的技巧：第一，直接反映在终端中，可以使用 ctx.logger 插件，它能提供比 console.log 更丰富的一系列信息；第二，使用断点进行调试，在 VS Code 编辑器中使用 Egg 提供好的 npm run debug 命令，就可以非常方便地在代码内进行断点调试。
