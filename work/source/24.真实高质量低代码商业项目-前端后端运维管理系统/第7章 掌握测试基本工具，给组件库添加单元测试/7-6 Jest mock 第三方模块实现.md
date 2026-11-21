大家好，上节课呢，我们使用 just 点 fn 创建了一个函数。

这个函数呢看起来很普通，但是呢它有很多的玄机在里面。

它可以监控这个函数本身的调用情况，被什么参数调用，调用了多少次啊，等等一系列的信息。

那么在测试中呢，可以对我们回调函数进行一个良好的测试和监控。

这节课呢，我们来到 mock function 另外一个功能，我们发现呢，就是这个手动 mock，也就是 mock 一个第三方文件的实现。

做到狸猫换太子。

好，那么现在呢，我创建了一个文件呢，或者说是模块，称之为 user。

大家可以看到呢，这里面我调用了一个 axios，我已安装好的这个模块，里面调用 axios 点 get，它的 URL 呢是我之前跟大家讲的一个在线的 URL API。

我们可以看它会返回一系列用户的信息，user 一的时候啊，这有一系列的信息。

好，那么我们这里呢，返回的是 user data 中的 user name。

好，那么现在呢，我们直接在一个 case 中调用这个函数，并且打印它的返回值。

那么就在这里，先那么 return，那么就是 get user name。

哦，它是一个，它调用这个一啊参数，它的返回呢是个 promise 啊。

这里面呢，我们称之为 name。

然后呢，在其中呢，我们把这个 name 打印出来。

好，我们来看一下。

好，我们可以看到。

等待一会儿，因为他要发送这个真正的网络请求。

就说我们拿到了这个一个真实的数据，我们可以看到在这里我们这个返回呢也是这个 Brett，所以我们拿到它的值。

但是呢，在测试中呢，我们应该和这个真实世界的一个数据呢给它脱离开，不让它真的去请求这个 API。

这种副作用呢会让我们的测试呢变得非常不稳定和脆弱。

所以呢，我们现在需要使用一种方法呢去替换第三方库的一个实现。

好，我们发现了这里真正发送异步请求的呢，这个是 axios 点 get 这个方法，所以呢，我们需要对它的实现呢进行一个替换。

我们应该怎么样做呢？

我们来看一下，我们在 mock test 点 js 中，首先呢把这个 axios 给它引过来，那么就是 const axios require axios。

注意呢，我这里采用了这个 common js 的写法，因为在 js 中当中呢，你假如要支持 es modules 的写法的话，要做这个另外的配置。

或者呢，你是要使用这个 babel 在 run 之前进行一次转换。

这里为了方便啊，我就不做这些事儿了，我就直接使用 commonjs。

好，然后呢，完成这一步呢以后呢，我们要调用这个 jest 点 mark。

啊，这个方法，这里面呢写你要 mark 这个模块。

特别注意呢，这里是字符串而不是变量，我们要 mark excel。

啊，我们就这么写。

好，这个意思呢就是说 jest 目前接管 excel 的这个整个模块的一个实现。

现在我们就可以来狸猫换太子了。

好，我们来可以在 axios 点 get 上面，然后呢调用这个方法。

啊，我们调用的方法呢，大家会看，实际是跟我们上一节课的这个 mark function 时候一样的。

这里有一系列的方法。

我们这里呢，首先调用一个最长的啊，调这个 mark implementation。

在这里面呢，你可以真正写这个你想要的这个 get 的实现。

这里我很简单，那么就是 it return promise their resolve.这里面呢，把它这个数据换掉啊，data user name啊，Viking。

好，换完以后呢，我们来看一看啊，大家会看到现在它打印的出来已经是Viking啊。

这个方法的意思呢，mock implementation呢，意思就是直接来模拟它的实现啊，等于呢就是我们使用后这个函数啊改写了它真正的实现。

那就是当我们在 XO 点 get 在 user 中调用这个方法的时候呢，它会替换成我们对应的实现。

所以呢，我们能看到当前的这个最终的返回值变成了我们这里定义的这个 Viking。

啊，当然呢，我们也可以使用上节课学习的 mock function 的一些方法来测试 XO 点 get 它有没有被调用。

因为呢，现在 XO get 呢其实它也是一个 jest mock 类型的对象，跟我们这个 mock cb 呢是一个类型。

啊，我们来看一下。

啊，我们先写 expect x o dot get，那就是 to have been called。

它被调用过，我们来看一下。

好，没问题，因为呢，它被调用过一次，就是在这里面被调用过，那没问题啊。

我们再来测试一下，它被调用过几次？

expect x o dot get to have been called times。

它应该是一次。

我们可以看它也能过啊！

大家可以去测试啊。

To have been called with被什么样的参数调用？

其实呢，就是被这么一个参数调用都可以进行一个测试。

好，除了这个 mock implementation 这个方法呢，jest 呢还提供了一系列的快捷方式。

其实我们上节课已经看到了啊，我们的快捷方式有一个叫 mock return value，它可以直接让你返回这个它的 value。

我们来看一下，我们来这里。

mark return value. Here, it's very simple. We can just delete these. We don't need to write a real implementation. We just need to write a return, and that's it. Delete. Okay, let's take a look. No problem. Now we can also achieve the same effect. Even more, it has a simpler method. Let's take a look here. We can see that mark return value has a mark result value. This mark result value means just provides another shortcut method.

它呢可以直接方便的返回一个 Promise resolve。

我们来看一下，我们来给它修改一下，我们让它更简单一些。

那么就在这里啊。

那么等于呢，它其实就包了这么一层，把它这个删掉，保存。

哎，我们可以看到现在呢，它返回的还是 Viking，而且我们的这个测试也是通过的。

好，那么大家呢有时间可以关注一系列这个 Mark Functions 上面的一系列这个 API。

等于它呢，是一层一层的让你获得呢更快捷的一个写 return 的方法。

好，那么其实呢，我们现在已经完成了 mock 第三方模块这个写法。

当然呢，现在有个问题就是，假如是几个测试文件都要 mock Excel 的话，这个模块的话呢，我们现在的做法呢会显得有一点繁琐，重复的逻辑呢我们要写好几遍。

Excel 呢还提供一个一劳永逸的方法啊。

你可以在你要 mark 的地方呢，创建一个杠杠 marks 杠杠的文件夹啊。

我们来看一下，这里呢我已经创建，我们只要把这个重命名。

假如说呢我们要 mark node modules 下面的模块，我们就把这个在根目录下面创建一个刚才我说的这个文件夹呢，就是杠杠 marks，然后呢杠杠。

好，之后呢你再创建一个文件，这个文件呢要跟你引用的这个文件的文件名呢完全一样，所以我这里创建了一个叫 xo 点 js 的文件。

我们点开啊，这时候呢，你就可以把你自己要实现的逻辑呢，完全的写在这里面了。

我们可以看到，这里面我实现了一个 get jest fn promise 的 resolve，然后直接给它返回。

现在呢，我们创建这个文件呢，在 mock 点 test 点 js 文件中呢，在这个 jest 运行测试的时候呢，它就会自动使用你创建的这个 mock 文件，不需要每次都写冒会代码了。

现在呢，让我们把这个我们手动的冒给它删掉。

好，那么我们保存一下，看看我们现在最终的效果。

这时候呢，我们看到呢，我们测试是通过的，而且 console 的 log 现在显示呢 name 啊已经换成了我在这里面修改的这个 mock，说明呢我们这个杠杠 marks 这个第三方库直接模拟的这个方法呢已经生效了。

好，我们现在呢测试可以完美享用第三方替代的模块了。

我们这节课的任务也就完成了。

大家是否掌握了 mock 第三方模块的两种写法呢？

好，那到这里，谢谢大家，再见。

