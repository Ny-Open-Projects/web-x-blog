# 10-20-Extend 扩展 第二部分

这节课继续介绍扩展 extend 的方式。上节课介绍的是最简单的 helper 扩展，这节课要面对的是我们使用最多的几大金刚的扩展方式。

先梳理一下在不同的文件中怎样对它们进行访问。application 是全局的应用对象，只有一个实例：在 ctx 上有 app 这个属性可以访问 application；在 controller 和 service 当中可以通过 this.app 访问，因为我们继承了基类，基类上面就有 this.app 这个属性；在 middleware 中可以通过传参的方式访问 application，它会以参数的形式传递进来。context 上下文对象每次请求生成一个实例：controller 和 service 通过继承拿到 this.ctx 进行访问；middleware 中在返回的 function 的第一个参数里拿到 ctx。request 和 response 很自然都是 ctx 上面的属性，拿到 ctx 就能拿到这两个对象。

梳理完毕后讲讲怎么新建扩展。它们的扩展方式都特别一致，我这里用 application 举例说明。首先在 extend 当中创建一个新的文件，现在已经有了 helper。特别注意文件名称要是 application，不要拼错，说明我们是在整个 application 对象上进行扩展：要扩展哪个对象，就要起同名的文件名称。如果是 context 或者 request、response，就要起同样的名称，比如 context 就叫 context.ts，以此类推。框架会把 application.ts 中定义的对象与 Koa application 的 prototype 对象进行合并，在应用启动的时候，会基于扩展后的 prototype 生成一个对应的 app 对象。

扩展有两种形式：方法的扩展和属性的扩展。

方法的扩展非常简单。创建一个测试方法返回一段没有意义的字符串。export default 还是返回一个 object，在其中添加方法，方法叫 echo，参数叫 message，返回一个 string。在 extend 文件当中，这个 this 对应的就是 application 对象，可以拿到 application 上面的现有属性和方法；假如你是 context 扩展，这个 this 就是 context 对象。我们做个测试，要拿到 application 上面的属性，所以要做一个类型断言：把 Application 先拿过来，写 `const that = this as Application`。这时候就拿到一系列信息了。直接 return 一个 hello 加上 message，还可以拿到 application 上面的信息，比如 that.config.name。这样对应的扩展就完成了，很简单。

然后在 controller 当中进行使用：经过扩展，app.echo 这个方法已经出现了，有自动提示，可以直接调用并填入参数。第一个任务完成。

方法扩展完毕后说说属性的扩展。属性扩展比方法扩展要复杂一点。一般来说，因为属性的计算只需要进行一次，所以一定要实现缓存，否则多次访问属性时会计算多次，降低应用的性能。

举一个实例来演示。我们希望在应用中有一个 axios 的实例，进行特定请求的发送。大家记得去安装 axios，我这里已经装好了。看对应的文档：Creating an instance，可以使用 axios.create 方法，传入一系列参数就会返回一个对应的 instance。实现缓存的思路大家都有：赋值的时候使用一个特殊的属性名称，然后判断这个属性名称是否存在。官方推荐使用 getter 和 symbol 的模式。symbol 类型不常见，可以把它看成一个特殊的函数，返回一个唯一的 symbol 值。文档中这么描述：symbol 是一种基本的数据类型，返回的 symbol 值是唯一的，一个 symbol 值能作为对象属性的标识符，这是该数据类型仅有的目的。看到这一行说明它跟我们的需求是绝配：我们正是要拿到对象属性的标识符判断是否存在，symbol 正好可以生成唯一的对象标识符，是一个很完美的解决方案。

来看怎样完成。首先创建一个对应的 getter，说明它是一个属性，我们称之为 axiosInstance。在这个 getter 里进行判断：假如不存在，也就是 this 上面没有对应的 axios 属性，就进行创建。刚才说了 symbol 可以用作对象上面的属性。创建时需要先创建对应的 symbol，很好创建：使用大写 AXIOS_INSTANCE 作为变量名（这是一个约定规则），调用 Symbol() 并写入一串相关的字符串，比如 `Symbol('application#axios')`，它返回的是唯一的一个值。

在 getter 内部：假如 this 上没有这个 symbol 属性，就创建，`this[AXIOS_INSTANCE] = axios.create(...)`，把 axios import 进来。create 的参数还是发送狗狗这个 API：baseURL 应该是 https://dog.ceo，再加一个 timeout 为 5000，也就是五秒以后它会自动断开。最后直接把它返回：`return this[AXIOS_INSTANCE]`。这样就完成了 getter 的属性写法。每次调用这个属性不会重复创建实例，只有第一次会创建。

这时候属性已经扩展上去了，在 test.ts 中做对应的测试：`const response = await this.app.axiosInstance.get(...)`。还有一个问题：axiosInstance 现在是 any 类型，需要指定它的类型。返回的应该是 AxiosInstance 类型，从 axios 导入过来，给 getter 添加一个返回类型。再看一下，这时候都能拿到对应的一系列方法了。我们简单拿一个 get，还是发送随机图片的请求，把 URL 复制过来，最后用 console.log 输出 response.data。访问一下 URL，请求成功，console 也能显示出 axios 对应的信息，任务完成。

application 扩展的写法就写到这里。我们学习了它上面方法和属性两方面的扩展，其中属性扩展的写法稍微复杂一点。有兴趣的话可以自己去完成 context 的扩展方式，它和 application 几乎完全一致。通过这两节课，我们就掌握了 Egg.js 当中扩展（extend）的概念。
