大家好，通过几节课内容呢，我们已经掌握了一个通用测试框架应该包含的几部分。

这几部分呢是断言、异步的支持、mock函数和第三方的模块。

其实呢，我们已经讲述了大部分的主要功能，但是最后呢，我还想给大家补充一部分功能。

这个功能呢，也是因为我在实际场景中遇见了具体的问题和 bug，所以呢，我觉得非常有必要呢，单独拿出来给大家讲一讲。

这就是呢，在 JavaScript 的异步编程中呢，有一类函数呢非常有趣，它能控制函数呢在特定时长后再次进行触发。

我想这些函数呢大家都很熟悉了啊，我们也经常用，比如说 set timeout、在 interval 以及 clear interval 之类等等的。

但是呢，注意呢，这种依赖现实生活中时长的代码呢，放到测试里面肯定是有问题的。

在测试中呢，像上节课说的一样，我们尽量要做到这个现实和副作用给它隔离开。

所以呢，我们现在需要一种控制时间的能力，在时间不同的区域里面呢进行一个跃迁。

那么，Jest 呢提供给我们这样的能力，它称之为 Timer Marks。

好，别的不多说，我们直接来看代码。

好，我们还是拿回我们的老朋友 fetch user，非常简单的一个函数。

然后呢，它的 callback 呢会在一秒后进行触发。

现在呢，我们来测试呢 cb 是否能够成功的进行一个触发。

好，我已经写了一个 case。

大家可以看到，我写到这里 to have been called. 当然呢，现在我们的 callback肯定是没有触发，因为我们的测试呢，大家可以看到有这个 set timeout，我们在一秒以后才能完成。

所以呢，到现在呢，我们就需要 jest 来接管测试了。

好，我们在测试的开始呢，我们调用一个 jest 内置的 API 啊，我们来看一下。

好，这个 API 呢，称之为 jest . use fake timers。

好，这个 API 呢，意思就是说。

他告诉整个测试呢。

现在呢，所有的 timer 呢，都由我伟大的 jest 进行接管了。

现在呢，接管以后呢，我们的整个 setTimeout 它也变成了一个 mock function。

我们还可以使用 expect 来测试它是否被调用了。

我们来这里看一下 expect setTimeout，那就是 to have been called to have been called times 吧。

它被调用了一次。

我们来看一下，这是通过的，没问题。

有了这里呢，然后呢，我们可以让时间向前进，让所有的 timers 都运行完毕。

我们只需要调用一个内置的方法，称之为 `jestor run all timers`。

使用这个方法呢，我们就让时间向前进，让所有的 timers 啊都运行完毕。

然后呢，我们就可以测试了啊。

Expect，那就是我们的回调呢，我们希望的回调呢，现在呢已经被调用了。

Two have been called. 同时呢，我们看看它是被用什么调用的啊？

就是 expect callback，那就是 two have been called with。

I've been called with.那么就是我们可以看一下我们的这个是 hello 啊。

好，来看一下啊。

我们现在所有的测试都通过了，所以呢，这是一个最基本的控制时间的能力。

但是呢，有的时候呢，我们还需要更细力度的一个控制。

一个简单的例子呢，就是一个 set timeout 的的一个嵌套。

我们可以看到呢，我们有一个 loop fetch user 啊，这里面呢有第一个 set timeout，然后呢，它调用 cb one 在一秒以后。

然后呢，在两秒以后呢，它又调用 C B 啊，但是它的这个参数呢变成了 two。

好，假如我们用刚才的方法，我们来看一下，我直接把这个已经写好的给它复制一下。

好，我们传入一个 F N，然后呢，expect，然后 run all timers。

这时候呢，我们 two have been called times 二。

我们来看一下，这个肯定是能通过的，但是呢，它是不是很完美？

因为我们使用 run all timers 啊，就等于呢，它一次将两个 timer 都跑完了。

这不是一个很完美的方式。

我呢想首先呢到达第一个时间点，然后进行一系列的测试，然后呢再到达第二个时间点，再完成余下的测试。

好，这时候呢我们可以使用这个 jest 给你提供的另外一个方法，它称之为 run only pending timers，它可以让你只运行目前在等待的一个 timer。

让我们来调用看一下。

好，这时候呢我把这个 run all timers 改成这个 run only pending timers，看在这里。

好，这时候呢我们就可以来判断。

To have been called times two, ah, so we come to see it, it is wrong, ah, because we only reached the first time point, that is, one second later. One second later, it should only call once, that is, one. Well, let's test it. What function to call?

Call back, that is, to have been called last with to have been last called with, ah, that is, the last call. What is it?

This is one. The first time. Well, let's see. This is passable.

然后呢，我们再让时间往前进，进入到第二个，那就是 just 点 run only pending timers，给它复制一下。

好，这时候呢应该是这个调用两次，并且呢上一次呢，因为到达了第二个 cb 的地方，那应该是二，那是 two。

那我们来看一下，OK，现在测试就通过了啊，完美，这就是自动控制多个 timers 的奥义啊。

现在呢，有的同学又来提需求了啊！

我们现在 JavaScript 呢都是自动运行到某一个时间点，到某一个结束，有没有什么方法让我自己来控制时间的流逝呢？

我想让它前进五百秒，让它前进一秒等等啊，没问题。

让我们来看看 JavaScript 是提供什么样 API 让我们这样做的啊！

首先呢，我来再复制一下一个 case，好，还是一个原始的 case。

这时候呢，我们提供了一个方法呢，它叫 advance time timers by time。

它里面是一个毫秒数，来看一下，我来复制一下。

OK，注意呢，这是毫秒啊，这个等于我们前进了五百毫秒。

那么前进了五百毫秒呢，是否到达这个CB第一次调用的时候啊？

没有到达，所以呢，我们来判断一下，把这复制过来，那么它应该是不会被通过的。

大家可以看到，它已经出错了啊，没有被跨过。

这时候呢，我们再让它前进五百毫秒，这时候到达一秒以后，它应该能成功。

好，大家看测试通过没问题。

那么现在呢，我们再让它到达第二次。

那就是让它前进到两秒以后，just their advance timers by time。

那就是两千毫秒。

这时候呢，我们把这个复制过来，看看它是否会通过。

好，复制一下，发现呢，它已经完美的通过了啊。

所以呢，我们就使用这个 advance timers by time 进行一个细粒力度的控制。

好，那么我们这节课呢，就介绍了 JS 控制时间的三种方法。

那么有三种API呢，从宏观的方面呢，到细粒度完成对Timers的一个按你需求的完美的控制，大家掌握的怎么样？

好，这节课呢就到这里，谢谢大家，再见。

