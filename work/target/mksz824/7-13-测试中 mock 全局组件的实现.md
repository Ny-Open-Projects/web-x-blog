# 7-13-测试中 mock 全局组件的实现

前面已经掌握了组件测试和 Jest 的绝大部分要点，现在进入一个实际组件的测试，看看这些技能能否覆盖足够多的 case。选用的组件叫 UserProfile，它是一个逻辑很简单的展示组件，有两种状态：未登录时，user.isLoggedIn 为 false，显示一个登录按钮；已登录时，显示当前用户名和一个登出按钮。很自然地，我们写两个测试用例，一个测未登录，一个测已登录。除了界面之外还有一系列行为，比如点击 login 和 logout 都会触发相应的逻辑。

虽然逻辑简单，但它包含了两个有趣的难点。第一个难点：组件用到了很多全局注册的 components，也就是在 main.ts 里直接 use 的那些，比如 a-button、a-dropdown-button、router-link、a-menu 和 a-menu-item。测试中并没有注册这些组件，直接使用一定会出问题。第二个难点：它引入了三个外部模块，代码里用了 useStore、useRouter 和 message 这三个函数，后面的行为测试需要判断这些模块里的方法是否被触发。这节课先解决第一个问题。

测试的大体框架先搭好：创建一个 wrapper，写两个 case，先只测界面，行为放一放。所以直接用 jest.mock 把这三个实现 mock 掉：第一个是 main.ts 对应的模块，第二个是 vuex，第三个是 vue-router，这样三个模块就不会干扰测试了。

先让测试跑起来看看界面到底是什么样子，在第一个 case 里用 console.log 输出 wrapper.html()。结果发现测试直接抛出一系列 warning，意思就是这些组件并没有注册就直接使用了。因为它们是全局注册的，Vue 渲染到这些节点时并不知道它们从哪儿来，所以会报 Failed to resolve 的 warning。

要解决这个问题，就要在用例里把这些组件注册进去，用的是 mount 的第二个参数。这个参数称为 global，用于注册 mount 过程中全局方面的内容，上面有一个 components 选项，可以把全局内容注册进去，其中每一项就是对应组件的 object。因为这里是要 mock，只需要给每个组件添加一个 template 属性来代替真实实现。

创建一个变量叫 mockComponent，写它的虚假实现：它是一个 object，上面有 template 属性。template 是 Vue 组件的根本，这里写得很简单，一个 div 加一个 slot，因为全局组件往往包裹着 slot 内容，加上 slot 才能把里面的内容显示出来。然后建一个 globalComponents 对象，把所有用到的第三方组件一一对应到这个假实现上。

当然，也可以把 main.ts 里每个组件的实例都导出来用，但我建议不要这样做。记住单元测试的重要思想是隔离，其他组件内部怎么实现，让它们自己的单元测试去管理就好了。

替换成 globalComponents 之后再看渲染结果，mock 生效了，登录界面变成了假实现的样子，成功地用假的替换了真的。现在写第一个用例：未登录时应该显示登录按钮，断言 `expect(wrapper.get('div').text()).toContain('登录')` 就可以了。跑一下，测试通过。

第二个用例测已登录状态：传入的 user 的 isLoggedIn 为 true 时，显示登录后的样子。如果不想重新新建一个实例，可以在 wrapper 上使用 setProps 方法改变当前属性，比如 `{ user: { isLoggedIn: true, username: 'Viking' } }`。注意界面更新是异步过程，函数要加 async await。输出 HTML 后可以看到 Viking 已经出现了，但登出按钮那部分节点根本没有渲染出来。

查一下源代码就明白了：a-dropdown-button 当中有一块自定义内容，对应的是一个名称为 overlay 的具名 slot，而我们现在的实现里只有一个默认 slot，所以这块内容没有渲染出来。针对这个组件做一个特殊实现：拷贝一份，命名为 mockComponent2，里面添加一个 `<slot name="overlay" />`，然后把 a-dropdown-button 的实现替换成 mockComponent2。再看结果，剩下的 HTML 结构被成功渲染出来了，用户名和登出按钮都在。

现在可以完成第二个用例的断言：希望 HTML 里有传入的用户名，`expect(wrapper.get('.user-profile-component').html()).toContain('Viking')`；还希望登出按钮存在，用 find 加 exists 来测存在性，`expect(wrapper.find('#user-profile-dropdown').exists()).toBeTruthy()`。跑一下，测试完美通过，界面部分的测试就写完了。

这节课举了一个比较极端的例子，组件本身实现很简单，但一遇到全局组件，整件事情就变得不同寻常。希望通过这个例子让大家掌握：当组件里用到全局组件时，可以在 mount 的 global.components 里用假实现替换真实实现，让渲染成功进行。当然还有几个比较难对付的第三方库需要处理，用来测试行为，下节课再讲它们的方法。到这里，谢谢大家，再见。
