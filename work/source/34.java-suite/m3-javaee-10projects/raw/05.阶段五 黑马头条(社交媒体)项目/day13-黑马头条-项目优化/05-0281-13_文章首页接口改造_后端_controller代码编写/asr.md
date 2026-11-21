# 声音线转写：13_文章首页接口改造_后端_controller代码编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day13-黑马头条-项目优化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day13-黑马头条-项目优化\13_文章首页接口改造_后端_controller代码编写【海量资源尽在 666java.com】.mp4
- 时长：3分32秒（音频 212s）
- 转写：faster-whisper-large-v3 / 语言 zh / 7 段
- 生成时间：2026-10-28 12:17:11

## 逐段转写（教师原声）

[00:00] 好继续往下讲刚才这个Service咱们已经写完了下面咱们就写Controller这时候你需要在这去创建一个Controller是v2版本的所以说咱们在这再去创建一个包这包叫做Controller下边的v2然后你就可以在这里边去创建咱们的这个类叫做什么咱们叫做什么叫article t s l e或是article home
[00:32] 号码v2方式叫Controller好让他同时也去实现之前的叫什么叫article然后是叫home奇怪了home然后是Controller API它是有三个方法咱们需要去重写下分别是loadload more和load new这个首先要去加上这东西叫什么叫restcontroller再加一个叫什么request mapping
[01:03] 在这个地址是不一样的记得要注意一下他们是叫什么来着API然后是V2然后是ARTICLE这是ARTICLE最终咱们就可以去一个一个去设置了首先你要去输入前的Service还是前Service叫APPARTICLEservice好吧加上之后的时候你在这去可以去加你的在下边加
[01:34] 都一样啊再一个叫post mapping别错了啊post mapping好第一个呢是叫做loadload啊load第二个呢咱们可以去拷贝一下那是叫做load more不是小写啊然后下面是一个load new加完之后呢那这个这个调用的方法肯定是不太一样的啊这时候咱们可以去照用load v2
[02:11] 首先第一个值咱们还是当前的ArticleConstants点有一个叫做load默认都是load最终咱们可以把DTO装进去然后你说第三个猜数是force还是true第一个猜数是true只有load如果load的话它会打开首页的时候第一次会加载的是load所以说它肯定是首页
[02:43] 但是你打开之后你可以上拉或者下拉去加的更多或者加的更新的时候这个就不是处理所以说咱们可以把它拷过来拷过来之后拷过来这个就是first这个也是first好当然这个也不是load mode这是什么这是load new改一改好有问题是吧稍微改一改这样就可以了
[03:18] 这样的话咱们这个前的这种control啊也算是改造完了然后下面呢咱们就可以去把前端也给写了然后呢咱们可以把这个地址改完之后呢一块来去测试一下好吧
