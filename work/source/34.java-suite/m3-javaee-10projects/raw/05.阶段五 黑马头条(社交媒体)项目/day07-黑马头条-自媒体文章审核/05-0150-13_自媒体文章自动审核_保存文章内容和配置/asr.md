# 声音线转写：13_自媒体文章自动审核_保存文章内容和配置

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day07-黑马头条-自媒体文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day07-黑马头条-自媒体文章审核\13_自媒体文章自动审核_保存文章内容和配置【海量资源尽在 666java.com】.mp4
- 时长：5分2秒（音频 303s）
- 转写：faster-whisper-large-v3 / 语言 zh / 10 段
- 生成时间：2026-10-28 11:48:31

## 逐段转写（教师原声）

[00:00] 好那咱们就继续做下面咱们就来去把当前的这个东西给去保存一下这个怎么保存的其实这个东西就比较简单了咱们可以直接去拗出来个东西叫AP article.com拗出来一个东西先保存它好吧然后你就可以往里边去设置了非常简单然后是.set什么呢set的东西里边其实就没几个是吧第一个是什么IDcontainer好,add your ID
[00:31] 其实你就可以直接从article.get id就可以了那为什么他能拿到呢其实呢这个字你应该知道啊因为咱们在保存他的时候呢可以看一下这里边咱们设置了一个逐渐返回其实就能去保存的时候就能直接拿到当前这个id好吧行那这个设置完之后咱们再往下看啊这边还有什么东西ap article.setconvent
[01:01] AP article content.setcontent.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.content.
[01:32] 然后再去然后怎么着去注入一个是吧private什么AP articleconfigconfigmapper注进来之后咱们这时候就能用了然后往下走往下走你可以直接去加AP然后是content.set
[02:04] 不是再载,insert就把当前这个数据加进去,没事了没问题啊那这个保存完之后呢其实里边还少一步啊还少一步,少哪一步呢就这个内容啊咱们需要去加密需要加密啊你看咱们之前保存的数据呢其实当前的内容啊找到内容表吧内容表就是它稍等啊,这个有点慢你看内容啊
[02:34] 这个内容是这样的是吧这并不是真正的内容咱们再去展示文章内容的时候是不是解压过是吧所以说咱们在这先去先去做一个加密这个加密的方式也比较简单咱们直接调一个公居类就可以了叫ZIPUTUSZIPUTUS要是这干嘛呢有一个ZIP这样的话就咱们一两个把这个文章内容装进去就可以了啊好这样就可以了啊那么下面呢就来去保存当前的这个位置
[03:07] 当前这个config咱们在这也可以去new一个new一个当前的aparticleconfig, 等于new一个ap好,入出来之后咱们可以直接去设置了config rset有一个article id那就容易beparticle.getid是吧然后再往下往下的话其实都是一些不耳之可以直接设置为库就可以了
[03:38] 往下走config.set比如说你的关注是吧我们可以去设置一个比如说有一个还有啥呢aparticleconfig.set下面还有一个就是isdelete是否需要删除是吧ok咱们可以去设置aparticle是否可以删除aparticleconfig.set
[04:12] 是否可以去下载是吧不是要下载是吧就咱们看一下AP article config.sets is forward应该是转发转发是设置为true那这个设置完了这个删除的话咱们可以设置为first可以看一下当前的表是在当前的这是否可评论是吧
[04:41] 然后是否转发是否下架还有是否已删除OK行没问题啊那这个咱们就设置完了设置完之后呢咱们可以直接去保存了啊AP然后这是一个config myprtl in third就把当前那个config给保存就可以了OK那这个啊这两个咱们也就保存完了
