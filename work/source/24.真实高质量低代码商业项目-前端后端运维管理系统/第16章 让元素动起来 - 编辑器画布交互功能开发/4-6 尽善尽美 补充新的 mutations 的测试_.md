大家好，上节课呢完成了 bug 的修复。

那么到目前为止呢，我们添加了很多新的交互，也就是呢在 store 中添加了非常多的 mutation 新的操作。

那么对于 store 的操作呢和交互以及界面呢，它是可以完全分开的。

所以这节课呢，我们来给 store 补充一些测试，也对于下一个需求历史记录的回滚和重做做一个预热啊。

对于那两个功能的开发呢，由于它比较复杂，我认为呢写测试呢是一种非常好的辅助手段。

来到这个 stored 测试文件中，看看到有什么样的 case。

这是之前我们写的。

好，那么我们关注点呢是在 editor 这里啊，所以我去添加了一个 only。

现在我们已经有了 should have default，应该有默认的拿到当前 current component。

然后呢，我添加了一些我们应该认为要测试的。

这里呢有这个 copy and paste component，还有这个 move component，以及呢这个 delete component。

Add and update中呢，我们有可能要做一些更新。

我们可以看到，现在测试呢都是能通过的，这里都是勾。

首先呢，我们来给更新第一个 app component is works fine。

我们发现呢，last item，这里面我们只判断了它的 text呢是不是 text 一，也就是跟这个是否是一样的。

我们第一步呢要把它属性填完全一点，因为我们现在知道呢，这些属性呢应该都是包括所有属性的。

所以呢，我这里把之前的这个 default text props给拿过来。

也就是我们的OpsFlow 组件库 里面的东西。

好，OpsFlow brick。

那么这里呢是 default text board props。

好，那么在这里呢给它做一个混入啊，把它放到这里，现在就完成了。

然后呢来判断多加一个。

那么这里呢我们希望它有新的 layer name，因为我们在添加一个新的，并且呢它应该是图层二。

现在我们里面是有一个。

那么自然呢，它新加的应该是图层二。

好，那么就是 last item 里边 layer name be 图层二。

那我们就给这个添加完毕啊。

啊，然后呢，我们就来添加我们的这个 copy and paste component。

Should works fine。

首先呢，我们要调用这个 copy component。

当然呢，我们这里呢之前已经选中了，所以我们这里直接调用就可以了。

我们这里看到我们这已经调用了 set active，我们应该是有选中的这个元素的。

好，那么就是 store点儿 commit这个 notation name呢叫 copy component。

完毕以后呢，我们希望是什么呢？

我们希望呢，我们这个 editor 当中有一个特殊的属性，大家都还记得啊，就是 store点儿 state，然后是 editor 当中的这个有一个 copy component，在这里我们希望它是有值，因为默认它是没有值的。

我们 copy 的时候呢，应该给它。

里面添加了值 to be defined。

哎，这里特别注意呢，因为我们在 editor 当中呢，copy 成功以后呢，我们会调用一个 on design view 的方法。

我们可以看到啊，success。

所以呢，我们这里要给它进行一个全局的模拟。

那么很简单，那我们直接调用 just mark。

这里呢，我们也不会判断它是否被调用过了。

所以，我们直接直接啊，把它 mark掉就可以了。

好，那么回到我们的 case 当中去啊。

我们现在写到了这里，to be defined。

那么现在 copy 完了以后，我们自然呢要调用这个 paste。

那么就是 store，继续啊，commit。

这应该是看一下啊，直接复制一下这个名称吧，比较长。

Paste copied component。

好，那么到这里呢，我们希望现在呢应该会多一项。

它应该是跟这个非常相似的啊。

我们这里是加一啊，我们现在又多了一项，所以这里应该是加二啊。

好，我们来看一下现在能否通过。

好，没问题啊，现在我们的 case 是可以通过的。

然后呢，我们就要看被 copy 这个 component 跟我们之前 copy 的是否完全一样。

那么它应该是添加到最后一个，所以我们自然呢也是取最后一个元素，就在这里啊，呃 last item。

假如呢 last item 存在的话，我们就来判断 expect last item 的 props。

我们这里呢可以调用这个 to equal，啊，因为它是一系列的这个对象进行一个比较，我们可以调用这个 to equal。

然后呢，我们要跟它相等的是 clone components。

零第一项选中的是第一项啊，所以说我们可以跟这个进行个比较，这样呢就代表我们这个拷贝呢是跟我们选中的这个元素呢是完全一致的。

我们来看一下，发现呢这个 case 是可以通过，那说明呢这个拷贝加粘贴这个 component 这功能是没问题的。

下一步呢我们稍微复杂一点，那就是 move component should work fine，也就是移动 component 这是一个单独的 mutation。

所以呢，我们要先拿到这个旧的值，那么就是拿到现在的这个 current component。

我们叫 current element。

我们这里是有一个 getter 的啊，那就是 getters 点 get current element。

它的返回我们知道 getters 它是没有这个任何的 type，它是 any 的，所以我们这里要给它指定一下，我们希望它是一个 component data 类型。

也就是我们的这个 element 类型，现在呢我们就可以拿到旧的值了。

好，我们来看一下，我们这里缓存一个旧的值，称之为 old value。

那么应该是 current element，可以看到现在呢可以很舒适的点出所有的这个属性了啊。

left，我们要拿到它的 left 值，而且呢我们希望呢它是一个数字类型的，自然呢要加这个 parse int。

由于它可能等于你 find。

所以我们给它设一个默认的值啊，是零。

现在呢，我们就拿到了它的旧的值，拿到旧的值了以后，我们就可以开始移动了啊。

首先呢，我们希望它往左移动，那就是 commit 啊。

这个名称呢叫这个 move component。

它的这个值呢，我来复制一下吧。

好，我们来看一下啊，向 direction 向 left 移动，amount 是五 px，id 呢是 current element 的 id。

接下来呢，我们就希望它是成功的。

这个属性是更改成功的，那么自然呢就是 expect a current element 啊。

我们希望它现在这个元素的值，我们可以看一下。

那 left 就是 to be，我们希望它等于什么呢？

自然是，因为它是向左移动呢，自然是要减去啊 old value 减去五啊，它的 left 值呢应该是减小，再加上 px。

来看一下结果。

好，没问题啊，说明我们向左移动是没问题的。

我们趁着它的这个热乎劲儿啊，再让它向右移动啊。

好，我们知道向右呢是 right，这里呢希望是三。

再复制一下这个。

好，这时候呢应该是 old value 减去五，然后它向右移动再加三，应该是这么一个值。

我们来看一下最终的结果能不能通过。

好，没问题啊，比较复杂这个移动呢也就解决了。

当然呢，还有两个 case 是 top or bottom，大家可以自行在这里补充一下。

对于这种不同的情形呢，最好是将它所有的情形都写的这样，代码覆盖率才会高，而且呢，测试的内容呢会更准确一些。

因为 top 和 bottom 也是另外的一个维度的两个计算。

好，那么 move 写完以后呢，我们这个 update 这里呢要给它更新一下啊。

update 呢，我们都知道呢，我们来看一下我们这个 update 啊，move component update。

现在呢，我们多加了一个 isRoot，它可以更改这个 updated component 它根的一个属性啊，不是直接更改它的 props，所以我们针对这个啊进行一个特殊的测试，等于呢多加一个 case，我们在这里后面进行一个补充啊 new props are a key，我们就知道呢我们要找一个存在的 key 啊，就是 layer name。

我们呢，给它这个 value 改成这个 new layer 吧。

那么它的这个 is root，我们知道呢，要给它设置成 true。

现在呢，我们可以再次触发它的这个 commit。

当然呢，使用的是 new props too。

好，现在呢，我们就希望它的这个 layer name 是被更新的啊。

那么就是 current element layer name。

To the new layer, 添加了这个新的这个测试情况，让我们来看一下。

好，那么现在呢，我们的这个所有测试就通过了。

还有一个 delete，我相信这个东西就很简单了，大家可以自己写一下，触发一个 delete，然后呢，我们希望它的这个整个的 components 应该是少一项。

测试的补充呢就到这里。

从测试来看呢，我们目前的 mutations 的逻辑呢没有什么问题，它都能按照我们的需求呢进行一系列的运作。

这节课的目的也就达到了，到这里，谢谢大家，再见。

