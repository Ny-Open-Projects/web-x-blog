---
disableNunjucks: true
title: 7-7 Jest mock Timers
date: 2026-11-17 15:47:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

通过几节课的内容，我们已经掌握了通用测试框架应该包含的几部分：断言、异步支持、mock 函数和 mock 第三方模块，其实已经讲了大部分主要功能。最后我想再补充一部分，这个功能是因为我在实际场景中遇到过具体的问题和 bug，才觉得非常有必要单独拿出来讲一讲。

JavaScript 的异步编程中有一类函数非常有趣，它能控制函数在特定时长后再次触发，比如 setTimeout、setInterval、clearInterval 等，大家都很熟悉。但要注意，这种依赖现实生活中时长的代码放到测试里肯定有问题。测试中要尽量像上节课说的那样，把现实和副作用隔离开，所以我们需要一种控制时间的能力，可以在时间区域里做跃迁。Jest 提供了这样的能力，称为 Timer Mocks。

不多说，直接看代码。还是拿回老朋友 fetchUser，一个非常简单的函数，它的 callback 在一秒后触发。现在测试 cb 是否能成功触发，我已经写了一个 case，断言写成 toHaveBeenCalled。现在 callback 肯定没有触发，因为测试里有 setTimeout，要一秒以后才能完成。

所以现在需要 Jest 来接管时间。在测试开始时调用一个内置 API：`jest.useFakeTimers()`。这个 API 告诉整个测试：现在所有的 timer 都由 Jest 接管了。接管以后，setTimeout 也变成了一个 mock function，我们还可以用 expect 测试它是否被调用：`expect(setTimeout).toHaveBeenCalledTimes(1)`。跑一下，通过，没问题。

有了这个，我们就可以让时间向前进，让所有 timer 都运行完毕。调用一个内置方法：`jest.runAllTimers()`。之后就可以断言了：期望的回调现在已经被调用，`expect(callback).toHaveBeenCalled()`；同时看看它是被什么调用的：`expect(callback).toHaveBeenCalledWith('hello')`。跑一下，所有测试都通过了。这是最基本的控制时间的能力。

但有时需要更细粒度的控制。一个简单的例子是 setTimeout 的嵌套：有一个 loopFetchUser，里面第一个 setTimeout 在一秒后调用 cbOne，两秒后又调用 cb，参数变成 two。假如用刚才的方法：传入函数，runAllTimers，然后断言 `toHaveBeenCalledTimes(2)`，肯定能通过，但它是不是完美？因为 runAllTimers 等于一次把两个 timer 都跑完了。我想首先到达第一个时间点，做一系列测试，再到达第二个时间点，完成余下的测试。

这时可以用 Jest 提供的另一个方法：runOnlyPendingTimers，它只运行目前在等待的 timer。把 runAllTimers 改成它，再判断 `toHaveBeenCalledTimes(2)`，可以看到它是错的，因为只到达了第一个时间点，一秒后只应该调用一次，改成 1。再测最后一次被什么函数调用：`toHaveBeenLastCalledWith(1)`，也就是最后一次调用的参数是一，能通过。然后让时间继续前进进入第二个时间点：再调用一次 `jest.runOnlyPendingTimers()`。这时应该是调用两次，并且上一次的参数应该是二。跑一下，测试通过，完美，这就是自动控制多个 timers 的奥义。

现在有同学提新需求了：现在是自动运行到某一个时间点，有没有方法自己控制时间的流逝？比如让它前进五百秒、前进一秒等。没问题。复制一个原始的 case，Jest 提供了一个方法叫 advanceTimersByTime，参数是一个毫秒数。注意是毫秒：前进五百毫秒，还没有到达 cb 第一次调用的时间点，所以判断它没有被调用，测试会出错，可以看到确实报错了，时间没有被跨过。再让它前进五百毫秒，到达一秒以后，应该能成功，跑一下通过。再让它到达第二次：`jest.advanceTimersByTime(2000)`，前进到两秒以后，把断言复制过来，测试完美通过。所以就用 advanceTimersByTime 做细粒度的控制。

这节课介绍了 Jest 控制时间的三种方法：runAllTimers、runOnlyPendingTimers 和 advanceTimersByTime，从宏观到细粒度，完成对 timers 按需求的完美控制。大家掌握得怎么样？这节课就到这里，谢谢大家，再见。
