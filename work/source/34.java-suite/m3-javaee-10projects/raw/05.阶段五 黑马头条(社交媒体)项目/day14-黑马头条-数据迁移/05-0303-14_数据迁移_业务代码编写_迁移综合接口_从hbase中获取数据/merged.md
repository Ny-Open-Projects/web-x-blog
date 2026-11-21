# 14_数据迁移_业务代码编写_迁移综合接口_从hbase中获取数据

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day14-黑马头条-数据迁移
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day14-黑马头条-数据迁移\14_数据迁移_业务代码编写_迁移综合接口_从hbase中获取数据【海量资源尽在 666java.com】.mp4
- 时长 6分47秒（音频 407s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那这里边还有一个方法没有写啊那这个呢咱们要去把这个方法给写一下那这个呢主要呢是从HBase中去查查完之后呢你要去组装成这么一个类组装成这么一个对象返回就可以好吧先在这去判断一下啊在这去写if 前的ID 浪吧浪等于ID这时候你直接returnreturn一个浪就可以好吧
[00:32] 下面咱们就可以去做一些判断首先咱们要去返回的还是当前的ArticleQuality然后是ArticleQuality等于一个None然后下面就可以去查询查询的方式其实咱们要去怎么查询你看就是当前的StorageClient打有一个GetStorageLitEntityList需要去根据一个list去查询这里边
[01:02] 他们这个表呢还是当前的这个表啊还是这个表是这里边啊它是有一个叫做type list好吧好是这么list啊那这个list没有是吧这里的装的是啥呢装的是一个一个的对象那这个对象呢其实是一个class的数组啊class的集合list然后是class错了啊class
[01:44] 然后装的是class最终的是你需要去new一下在这个new的话你怎么办呢这里边装的数据啊咱们可以这么啊arraySarrayS啊等于一个arrayS点有一个叫做slist这里边就可以去装一些数据比如说咱们要去返回的是谁啊apArticle的class为什么呢有一个是apArticleConfig的class好吧
[02:18] 为什么呢?
[02:19] 还有一个是AParticlecontent的Service就玩切钱嘛,RTCREcontent,content,serclass还有一个是APauthorclass那这个装那么多,就是那么多这是几个,就根据这些类型去查询就可以好,那这个返回之后,这个制度报错了呢?
[02:47] 我看看啊
[02:51] 说是有一个list然后是scrn这是一个scrn对吧说这是scrn不对这里边还少参数是吧少参数这里边还少一个rootkeyrootkey是谁呢你可以看一下当前的这块内容去转换的时候它就会把你的AP article的ID转成了什么rootkey所以说这个rootkey就好拿了吧就是这个ID是吧
[03:22] 这个ID咱们要去转换一下他转换了一个street类型的叫dat有一个叫做 convert utils.toStreet然后你把它进来ID装进去就好了那这样的话咱们就算是设置完了最终的就能去返一个结果好点这个叫啥叫object list了object list作为这个类型咱们现在需要自己去自己去扬转好吧
[03:53] 咱们就可以去判断一下主要是最终是要转成这么个对象就可以了好首先在这去看if当不等于当前的object list然后是&v当是object list.is empty然后咱们就可以去评了插群的话主要就是先去把它扭出来扭一个然后咱们就可以去做判断if
[04:26] 之前还得去干嘛还得去做循环这个在list.for好这时候是比如说叫value好吧然后咱们就可以去做判断了判断value.instanceof比如说叫dpArticle这时候它肯定就是先判断这个dpArticle然后它肯定就是dpArticle了好这时候就可以把它放到这里边
[04:56] dlsetaparticle这样的话就把当前那个value装进去啊这个需要强转好那这是一个然后下面是不是一样啊然后是valueinstanceof第二个是当前的aparticlecontent啊然后呢是这个啊articlequality.setcontent好
[05:34] 那就是还是value但是你还是要强转一下还有接着往下看然后这个是value instance of咱们还有一个叫做config是吧config然后呢还是articlequantity.有一个set有一个config好吧还是value强转还有最后一个是吧最后一个叫value然后是instance然后是叫什么ap author
[06:18] 好等于他的时候呢咱们就可以再去设置一个啊设置最后一个那就是Value啊最终强者就可以了啊那行那这样的话咱们就说转了啊说完之后呢你直接去返回这个对象就可以了啊直接return当前的哪一个呢嗯我看看啊是在哪返回啊啊在这啊在这啊把它给返回好了那这样的话这个方法咱们就算写完了啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 代码中通过反射机制动态设置对象属性，以实现从数据库查询结果中构建 ArticleQuantity 实体对象。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 ArticleQuantityServiceImp.java 文件中 getArticleQuantityByArticleIdForBase 方法的初始代码结构，包含对 articleQuantity 对象的初始化和属性赋值逻辑。
画面 2：在代码中添加了对 articleQuantity 对象的初始化语句，但尚未完成属性赋值。
画面 3：在代码中添加了对 articleQuantity 对象的初始化语句，但尚未完成属性赋值。
画面 4：在代码中添加了对 articleQuantity 对象的初始化语句，但尚未完成属性赋值。
画面 5：在代码中添加了对 articleQuantity 对象的初始化语句，但尚未完成属性赋值。
画面 6：在代码中添加了对 articleQuantity 对象的初始化语句，但尚未完成属性赋值。
画面 7：在代码中添加了对 articleQuantity 对象的初始化语句，但尚未完成属性赋值。
画面 8：在代码中添加了对 articleQuantity 对象的初始化语句，但尚未完成属性赋值。
画面 9：在代码中添加了对 articleQuantity 对象的初始化语句，但尚未完成属性赋值。
画面 10：在代码中添加了对 articleQuantity 对象的初始化语句，但尚未完成属性赋值。
画面 11：在代码中添加了对 articleQuantity 对象的初始化语句，但尚未完成属性赋值。
画面 12：在代码中添加了对 articleQuantity 对象的初始化语句，但尚未完成属性赋值。
画面 13：在代码中添加了对 articleQuantity 对象的初始化语句，但尚未完成属性赋值。
画面 14：在代码中添加了对 articleQuantity 对象的初始化语句，但尚未完成属性赋值。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
if(null != aparticle){
    articleQuantity = new ArticleQuantity();
    articleQuantity.setArticle(aparticle);
    ArticleContent aparticleContent = apArticleContentService.getArticleById(aparticle.getArticleId());
    articleQuantity.setArticleContent(aparticleContent);
    ArticleConfig aparticleConfig = apArticleConfigService.getArticleId(aparticle.getArticleId());
    articleQuantity.setArticleConfig(aparticleConfig);
    Author apAuthor = apAuthorService.getAuthorId(aparticle.getAuthorId());
    articleQuantity.setAuthor(apAuthor);
    articleQuantity.setArticleQuantity();
    return articleQuantity;
}
```

画面 2：
```java
if(null != aparticle){
    articleQuantity = new ArticleQuantity();
    articleQuantity.setArticle(aparticle);
    ArticleContent aparticleContent = apArticleContentService.getArticleById(aparticle.getArticleId());
    articleQuantity.setArticleContent(aparticleContent);
    ArticleConfig aparticleConfig = apArticleConfigService.getArticleId(aparticle.getArticleId());
    articleQuantity.setArticleConfig(aparticleConfig);
    Author apAuthor = apAuthorService.getAuthorId(aparticle.getAuthorId());
    articleQuantity.setAuthor(apAuthor);
    articleQuantity.setArticleQuantity();
    return articleQuantity;
}
```

画面 3：
```java
if(null != aparticle){
    articleQuantity = new ArticleQuantity();
    articleQuantity.setArticle(aparticle);
    ArticleContent aparticleContent = apArticleContentService.getArticleById(aparticle.getArticleId());
    articleQuantity.setArticleContent(aparticleContent);
    ArticleConfig aparticleConfig = apArticleConfigService.getArticleId(aparticle.getArticleId());
    articleQuantity.setArticleConfig(aparticleConfig);
    Author apAuthor = apAuthorService.getAuthorId(aparticle.getAuthorId());
    articleQuantity.setAuthor(apAuthor);
    articleQuantity.setArticleQuantity();
    return articleQuantity;
}
```

画面 4：
```java
if(null != aparticle){
    articleQuantity = new ArticleQuantity();
    articleQuantity.setArticle(aparticle);
    ArticleContent aparticleContent = apArticleContentService.getArticleById(aparticle.getArticleId());
    articleQuantity.setArticleContent(aparticleContent);
    ArticleConfig aparticleConfig = apArticleConfigService.getArticleId(aparticle.getArticleId());
    articleQuantity.setArticleConfig(aparticleConfig);
    Author apAuthor = apAuthorService.getAuthorId(aparticle.getAuthorId());
    articleQuantity.setAuthor(apAuthor);
    articleQuantity.setArticleQuantity();
    return articleQuantity;
}
```

画面 5：
```java
if(null != aparticle){
    articleQuantity = new ArticleQuantity();
    articleQuantity.setArticle(aparticle);
    ArticleContent aparticleContent = apArticleContentService.getArticleById(aparticle.getArticleId());
    articleQuantity.setArticleContent(aparticleContent);
    ArticleConfig aparticleConfig = apArticleConfigService.getArticleId(aparticle.getArticleId());
    articleQuantity.setArticleConfig(aparticleConfig);
    Author apAuthor = apAuthorService.getAuthorId(aparticle.getAuthorId());
    articleQuantity.setAuthor(apAuthor);
    articleQuantity.setArticleQuantity();
    return articleQuantity;
}
```

画面 6：
```java
if(null != aparticle){
    articleQuantity = new ArticleQuantity();
    articleQuantity.setArticle(aparticle);
    ArticleContent aparticleContent = apArticleContentService.getArticleById(aparticle.getArticleId());
    articleQuantity.setArticleContent(aparticleContent);
    ArticleConfig aparticleConfig = apArticleConfigService.getArticleId(aparticle.getArticleId());
    articleQuantity.setArticleConfig(aparticleConfig);
    Author apAuthor = apAuthorService.getAuthorId(aparticle.getAuthorId());
    articleQuantity.setAuthor(apAuthor);
    articleQuantity.setArticleQuantity();
    return articleQuantity;
}
```

画面 7：
```java
if(null != aparticle){
    articleQuantity = new ArticleQuantity();
    articleQuantity.setArticle(aparticle);
    ArticleContent aparticleContent = apArticleContentService.getArticleById(aparticle.getArticleId());
    articleQuantity.setArticleContent(aparticleContent);
    ArticleConfig aparticleConfig = apArticleConfigService.getArticleId(aparticle.getArticleId());
    articleQuantity.setArticleConfig(aparticleConfig);
    Author apAuthor = apAuthorService.getAuthorId(aparticle.getAuthorId());
    articleQuantity.setAuthor(apAuthor);
    articleQuantity.setArticleQuantity();
    return articleQuantity;
}
```

画面 8：
```java
if(null != aparticle){
    articleQuantity = new ArticleQuantity();
    articleQuantity.setArticle(aparticle);
    ArticleContent aparticleContent = apArticleContentService.getArticleById(aparticle.getArticleId());
    articleQuantity.setArticleContent(aparticleContent);
    ArticleConfig aparticleConfig = apArticleConfigService.getArticleId(aparticle.getArticleId());
    articleQuantity.setArticleConfig(aparticleConfig);
    Author apAuthor = apAuthorService.getAuthorId(aparticle.getAuthorId());
    articleQuantity.setAuthor(apAuthor);
    articleQuantity.setArticleQuantity();
    return articleQuantity;
}
```

画面 9：
```java
if(null != aparticle){
    articleQuantity = new ArticleQuantity();
    articleQuantity.setArticle(aparticle);
    ArticleContent aparticleContent = apArticleContentService.getArticleById(aparticle.getArticleId());
    articleQuantity.setArticleContent(aparticleContent);
    ArticleConfig aparticleConfig = apArticleConfigService.getArticleId(aparticle.getArticleId());
    articleQuantity.setArticleConfig(aparticleConfig);
    Author apAuthor = apAuthorService.getAuthorId(aparticle.getAuthorId());
    articleQuantity.setAuthor(apAuthor);
    articleQuantity.setArticleQuantity();
    return articleQuantity;
}
```

画面 10：
```java
if(null != aparticle){
    articleQuantity = new ArticleQuantity();
    articleQuantity.setArticle(aparticle);
    ArticleContent aparticleContent = apArticleContentService.getArticleById(aparticle.getArticleId());
    articleQuantity.setArticleContent(aparticleContent);
    ArticleConfig aparticleConfig = apArticleConfigService.getArticleId(aparticle.getArticleId());
    articleQuantity.setArticleConfig(aparticleConfig);
    Author apAuthor = apAuthorService.getAuthorId(aparticle.getAuthorId());
    articleQuantity.setAuthor(apAuthor);
    articleQuantity.setArticleQuantity();
    return articleQuantity;
}
```

画面 11：
```java
if(null != aparticle){
    articleQuantity = new ArticleQuantity();
    articleQuantity.setArticle(aparticle);
    ArticleContent aparticleContent = apArticleContentService.getArticleById(aparticle.getArticleId());
    articleQuantity.setArticleContent(aparticleContent);
    ArticleConfig aparticleConfig = apArticleConfigService.getArticleId(aparticle.getArticleId());
    articleQuantity.setArticleConfig(aparticleConfig);
    Author apAuthor = apAuthorService.getAuthorId(aparticle.getAuthorId());
    articleQuantity.setAuthor(apAuthor);
    articleQuantity.setArticleQuantity();
    return articleQuantity;
}
```

画面 12：
```java
if(null != aparticle){
    articleQuantity = new ArticleQuantity();
    articleQuantity.setArticle(aparticle);
    ArticleContent aparticleContent = apArticleContentService.getArticleById(aparticle.getArticleId());
    articleQuantity.setArticleContent(aparticleContent);
    ArticleConfig aparticleConfig = apArticleConfigService.getArticleId(aparticle.getArticleId());
    articleQuantity.setArticleConfig(aparticleConfig);
    Author apAuthor = apAuthorService.getAuthorId(aparticle.getAuthorId());
    articleQuantity.setAuthor(apAuthor);
    articleQuantity.setArticleQuantity();
    return articleQuantity;
}
```

画面 13：
```java

