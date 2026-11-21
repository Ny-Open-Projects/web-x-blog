---
disableNunjucks: true
title: 7-6 Jest mock 第三方模块实现
date: 2026-11-17 14:46:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

上节课我们用 jest.fn() 创建了一个函数。这个函数看起来很普通，其实有很多玄机在里面：它可以监控函数本身的调用情况，被什么参数调用、调用了多少次等等一系列信息，在测试中对回调函数进行良好的测试和监控。这节课来到 mock function 的另一个功能：手动 mock，也就是 mock 一个第三方模块的实现，做到狸猫换太子。

我创建了一个模块，称为 user，里面调用了已安装好的 axios，用 axios.get 请求一个之前讲过的在线用户 API，返回值取 user data 中的 username。现在直接在一个 case 中调用这个函数并打印返回值：调用 getUsername(1)，它的返回是一个 promise，拿到 name 后打印出来。

跑一下，要等一会儿，因为它要发送真正的网络请求。可以看到我们拿到了真实的数据，返回值是 Brett。但在测试中，我们应该和真实世界的数据脱离开，不让它真的去请求 API。这种副作用会让测试变得非常不稳定和脆弱，所以需要用一种方法替换第三方库的实现。

真正发送异步请求的是 axios.get 这个方法，所以要对它的实现进行替换。在 mock.test.js 中，首先把 axios 引过来：`const axios = require('axios')`。注意这里用了 CommonJS 的写法，因为在 Node.js 中要支持 ES modules 的写法需要额外配置，或者用 babel 在运行之前做一次转换。为了方便，这里直接用 CommonJS。

然后调用 `jest.mock('axios')`，注意参数是字符串而不是变量。这行代码的意思是：Jest 目前接管 axios 整个模块的实现。现在就可以狸猫换太子了。在 axios.get 上调用方法，实际和上节课 mock function 时用到的一样。这里调用最长的一个：mockImplementation，在里面真正写你想要的 get 的实现。实现很简单，返回一个 resolve 的 promise，把数据换成 username 是 Viking。

改完之后，打印出来的值已经变成 Viking 了。mockImplementation 的意思就是直接模拟实现，等于改写了函数真正的实现：当 user 中调用 axios.get 时，会替换成我们对应的实现，所以最终返回值变成了这里定义的 Viking。

当然，还可以用上节课学的 mock function 方法测试 axios.get 有没有被调用。因为现在 axios.get 其实是一个 jest mock 类型的对象，和之前的 mockCb 是同一个类型。写 `expect(axios.get).toHaveBeenCalled()`，它能通过，因为它被调用过一次。再测它被调用了几次：`expect(axios.get).toHaveBeenCalledTimes(1)`，也能过。还可以用 toHaveBeenCalledWith 测被什么参数调用，都可行。

除了 mockImplementation，Jest 还提供了一系列快捷方式。上节课已经见过 mockReturnValue，它可以直接返回指定值：不需要写真正的实现，只写返回值即可，效果一样。它还有更简单的 mockResolvedValue，这个方法方便地返回一个 Promise resolve，等于替你包了一层。把实现替换成它，保存，返回的还是 Viking，测试也通过。大家有时间可以关注一下 mock functions 上的这一系列 API，它们是一层一层让你获得更快捷的写返回值的方法。

到这里，mock 第三方模块的写法就完成了。但有个问题：假如几个测试文件都要 mock axios 这个模块，现在的做法会显得繁琐，重复的逻辑要写好几遍。Jest 提供了一个一劳永逸的方法：在项目根目录创建一个 `__mocks__` 文件夹。如果要 mock node_modules 下面的模块，就在根目录建这个文件夹，然后在里面创建一个文件，文件名要和引用的模块完全一样，这里创建了一个 axios.js。

打开这个文件，把你要实现的逻辑完全写在这里面：我实现了一个 get，用 jest.fn 返回一个 resolve 的 promise。以后 Jest 运行测试时，会自动使用你创建的 mock 文件，不需要每次都写 mock 代码了。把手动的 mock 删掉，保存，看最终效果：测试通过，而且 console.log 显示 name 已经换成了 mock 文件里修改的值，说明 __mocks__ 直接模拟第三方库的方法已经生效。

现在测试可以完美享用第三方替代的模块了，这节课的任务也就完成了。大家是否掌握了 mock 第三方模块的两种写法呢？到这里，谢谢大家，再见。
