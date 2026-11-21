# 11-SpringBoot事件监听

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/2.SpringBoot 第二天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\2.SpringBoot 第二天\11-SpringBoot事件监听_【海量资源尽在 ubkz.com】.mp4
- 时长 23分57秒（音频 1437s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 介绍完Spring Boot的自动配置原理的分析之后接下来我们来介绍一下Spring Boot的另外一个机制叫做监听的机制其实呢说到这个监听机制我相信大家并不是很陌生我们之前在学习JavaScript的时候就介绍过我们可以定义一个按钮对吧然后在按钮上绑定一个单击事件单击事件将来一被点击就会触发一个函数我函数的代码的内容逻辑是我们自己定义的
[00:32] 这就是我们JS里边的一个监听的机制就是事件监听机制嘛OK啊,一样的道理哈那么比如说我们在Windows上比如说我们打开一个计算器可以来简单的演示一下计算器上呢这个地方呢也是一样有很多的按钮对吧那么比如说我这个8号按钮8这个按钮我一点它是不是在这个地方就把8显示到这个地方了那一样的嘛这个按钮呢就是一个事件源就是事件发生那个地方这个按钮组件对吧
[01:00] 那么当我们一点那个点击那个动作其实就是一个事件单击事件那么一点击这个单击事件之后呢这个8就输出了那么它内部肯定要执行一些逻辑的代码操作的对吧那么这个代码的操作呢我们就称为监听器将来呢这个按钮绑定或者注册了某一个监听器之后呢用户在操作的时候就会进行监听器代码的回调并且啊这一个按钮或者是一个事件源上
[01:29] 还可以注册多个监听器也可以监听多个事件的发生你比如说看这最少得有两个你看我鼠标移到这个按钮上是不是它会改变它的样式对吧OK这是一个鼠标移入过来它是一个操作然后第二个点一下不是也是一个事件吗所以这一个事件源上是不是可以绑定很多个事件的OK就是个意思
[01:54] 所以我们Spring Boot里面监听机制也类似只不过它是对对象的一些操作比如说去监听对象的一些变化属性的变化和对象声明周期的一些创建销毁等等这些功能它不是说监听这个按钮被点了还是不点怎么着但是Spring Boot的监听机制它的思想都是一样的而Spring Boot的监听机制它是对我们Java监听机制的一种封装所以首先我们先来聊一聊
[02:22] Java的事件监听机制Java的事件监听机制呢它也是这么几个角色事件 事件源监听器刚才说过了那么事件呢它是event它要求Java里边所有事件对象都必须继承自一个对象叫做event object这么一个类的对象那么第二个事件源呢就是任意的object对象了也就是说你可以监听任意的对象对应的一个属性啊
[02:50] 创建啊销毁啊声明究其的一些变化情况所以是object第三个listener就是监听器那么监听器这个东西呢它要求Java里边所有的监听器呢都必须实现这个event listener这么一个接口OK大概我们就说了一下Java里边的这个监听的机制这么几个对象OK那么说完这个事之后呢接下来我们就来聊一聊Spring Boot的监听机制其实呢我们
[03:15] 用Spring Boot的监听机制不需要像这么麻烦好像之前我们可能还得我们自己去绑定这个事件对吧然后自己来完成很多很多的业务逻辑操作OK那么在Spring Boot里边呢它其实给我们提供好了对应的一些个监听器的回调因为Spring Boot项目启动的时候会提供几个监听器的回调而我们可以实现这些监听器的接口在项目启动的时候就完成一些操作
[03:44] 它内部已经把注册监听的一些动作都给我们写好了只是把监听器的接口暴露给我们了我们需要干的事呢只需要来实现这个接口并且把接口的方法给它复写了将来我们在项目启动的时候就可以来完成对应的一个方法的回调了OK简单的看一下这么几个监听器的接口ApplicationContextInitializer好这么一个就是初始化的时候会调用这个
[04:14] SpringApplicationRunListener这有一个监听器还有一个Command9Runner还有一个ApplicationRunner这门有四个那么接下来我们就在代码里边来详细的说这四个的功能和作用简单的去演示一下打开IDR打开IDR之后我们还是一样新创建这么一个模块加一个模块下一步写一个GrupID com.it黑码
[04:46] artifact id呢我们就起名为Spring Boot-listenerlist1n1r好嘞就叫这个名就可以了然后下一步然后listener呢这个地方我们也不用加任何的东西了我们直接finish就完事了好ok项目创建完事之后呢接下来我们就可以在这里边来定义我们自己对应的一个监听器了定义我们自己的监听器呢我们就这样我们就写一个包的名称
[05:17] 其实那个Initializer它不叫监听器但是呢我们把它叫做当作监听来用没问题啊就是我们说的第一个你看它的名字是不是不叫Listener但是我们把它当作监听器来用一点问题都没有它的原理机制都类似好在这个地方呢我们来看一下第一个呢叫做APPAPPApplicationInitializer好就这么一个这么一个你看这玩意呢它是一个
[05:47] interface对吧而这个interface呢它里边就有一个方法叫做insulator这个方法那么我们干这个需要写这个的实现类怎么办呢那我只需要把这个复制一下然后我们自己创建这么一个比如说我们就起my好这个名字起完了之后呢我们只需要来实现一下这么一个接口实现完了之后呢接下来我们给它把这个包导进来把未实现的方法给它复写一下里边只需要输出一句话
[06:16] 输出个什么话呢我们就输出这个好就可以了然后呢我们把这个方法名呢也给它输出一下OK简单的把这个代码写完这是第一个写完了之后呢接下来我们再来把其他的几个都给它写一下第二个呢叫做我们直接搜一下wrong listener你如果记不住的话就搜它的一个对应的一个名称好这个地方有个wrong listeners不是这个我们是wrong listener是这个名啊
[06:49] 这个这个接口你看这个接口里边是不是有一大堆的方法待会我们再来解释几个方法我们先把它写出来好class然后呢my好wrong listener然后同样呢implements这个地方的这个接口然后呢把包一捣并且呢把这些方法都给它实现一下这么多方法那么这些个方法呢我们可以来简单的看一下稍等我们打开我们自己定义的这个第一个呢叫做starting
[07:19] 这个starting你注意看看这个名字你注意看starting就是启动嘛是吧你注意看下边的这些名字环境准备context就是我们的上下文IOC容器那个准备然后context loader加载start的启动完成然后正在运行runningfailed失败你会发现这些方法其实是不是好像都跟生命周期相关的方法它就描述了这么一个状态一个过程
[07:45] 从上到下这些状态和过程依此的推进是吧其实这个呢就是一个Spring Boot启动的时候会触发各种不同的事件然后呢我们可以在不同的位置去实现这个方法来做一些事情好Starting呢我们一个个来写一下Starting第一个呢就是我们的项目启动启动中这个没有什么用啊就是说告诉一下项目开始启动了告诉你一下
[08:15] 比如说123开始跑了跑的那一步调用这个starting然后呢我们可以来挨个的把这些打印一下看一下它们到底在什么时候被调用的第二个是environmentenvironment表示环境通过环境呢可以来获取对应的一些配置属性的信息对吧环境开始准备了就是这个环境环境环境对象开始准备就开始准备的意思就是还没有
[08:45] 弄好嘛对不对然后呢还现在不能获取对应的配置的一些信息啊那么第三个呢叫做context preparedcontext prepared呢表示了我们的一个就是我们的上下文对象开始准备啊那么这个时候呢你可能还没有去加载IOC的容器对吧因为他开始准备还没有准备好嘛然后这个呢叫做context loadedcontext loaded呢表示了加载啊加载
[09:15] 上下文对象开始加载其实这个地方加载的时候它需要去干很多很多事比如说它要创建Spring Boot启动的时候那些个bin那一百多个非常的多所以这个地方它开始加载给你说一下然后started表示了这个玩意已经加载完成了好加载完成started加载完成了加载完成了之后接下来再看runningrunning表示了它开始运行了
[09:44] 开始运行这个地方没改改一下这个表示呢我们的程序啊就是项目已经启动完成然后呢开始运行OK最后一个呢其实就是一个失败就是当项目启动失败的时候其实在一场里边会去触发这么一个fail的项目启动失败OK那么简单的我们把这些方法呢都给它实际说了一下说了一下之后呢接下来我们还有两个
[10:14] 还有两个我们可以看叫做command run, none runner和application runner我们把这两个也分别的去写一下还是一样我们如果不好起名的话我们先看一下command run那么这个接口里边非常简单就这么一个方法run方法ok吧好我们来写一下先不要去管这几个都是干啥的我们先把它写出来一看然后待会我们再说干什么的implements command line runner
[10:44] 把这个方法呢给它实现一下实现一下之后呢我们sout一下common line runner好哎把这个地方呢打印一个字符串名字然后点点run方法OK这样就弄完了弄完了其实呢还有一个跟他一个兄弟一样的叫做spreen runner好spreen runner第二class就这么一个哎不是这个spreen runner
[11:15] 叫做applicationappliapplicationrunner就这么一个东西applicationrunner呢我们找一下它这个名字你看applicationrunner就这么一个它里边你看是不是也有一个run方法对吧一样的所以呢我们也可以来实现一下它好我们来实现一下myapplicationrunnerok然后呢我们来实现一下applicationrunner这么一个东西实现完了之后呢同样的它里边也有个run方法
[11:45] 然后我们直接打印一下打印一下之后呢这个地方呢application runner呢我们来看一下这个application runner呢这个地方呢其实呢这个参数啊它跟刚才那个run方法你注意看啊command line runner你看稍微有点区别啊其他都是一样啊run方法这里边传了个string点点就是可变参的一个args然后呢这个command line runner呢application runner呢它里边封装这么一个对象所以呢他们两个待会我们来区分一下就可以了好
[12:15] 这个里边的软方法那么这四个都写完了之后呢接下来我们来看一下我们把四个呢都被它注册到Spring的容器里边去component给它注册一下注册一下之后咱们挨个呢加上这个component注解好加完了之后呢我们来启动看一下它们会不会自动的被调用其实你会发现只有两个会被调用还有两个呢不会被调用啊好我们先来看这个
[12:46] 我们把这个项目给它启动一下正在启动中你注意看我们最后两个ApplicationRunner的run方法和CommonLine的run的run方法这两个是不是执行了而这两个执行了之后还有两个呢还有两个比较长的那个这个Context叫做InitialLayer没有被执行还有一个呢是SpringApplicationRunnerListener它也没有被执行因为这两个
[13:24] 它要执行的话是需要我们进行一个配置的OK或者说需要我们注册那么这两个直接放到IOC容器里边就可以被自动的执行那么我们先来说这两个你注意看这两个其实干的事是一模一样的而且呢他们的代码呢也基本上方法名都一样对吧这两个只是你的参数不一样你的参数不一样这两个的执行时机呢都是一模一样的是当当当我们的一个项目
[13:54] 启动后来执行OK来执行的时候呢执行谁呢执行这个run的方法那么可以干什么呢其实呢我们比如说我们可以在这个地方呢通过这个run方法我们这个方法是不是会被自动调用那么自动调用呢就非常棒了我们在项目启动之后呢想干一些事情我们就可以在这run方法里边来完成来看了干什么事呢比如说你现在用缓存
[14:19] 我们一般用Redis的时候我们在项目启动的时候总期望Redis能够把数据库的一些信息提前加载进来作为缓存为什么这样做呢为了防止我们第一个人用户访问的时候缓存里面没数据他去查询数据库那么这个动作我们一般称为缓存的预热的动作对吧我们可以在这里边来完成因为它是自动被毁掉的对不对OK那么接下来我们可以来看一下我们这两个run方法
[14:48] 一个是String的args,我们可以把args打印一下,因为直接打印数组出现的是地址值,打印一下args,common application render也同样打印一下,但是这个args是个对象,那么我们看一下,这个args里面有个方法叫做getSource,
[15:18] Args它返回的也是一个字无串的数组所以我们也可以用这个ary erase.islist把这个包裹一下同样的也能获取到对应的参数信息这个Args是啥呢你看现在有没有我们重新来启动一下其实现在是没有什么Args的可以来看一看你看Args是不是空输入Args是啥呢就是我们传递的那些参数比如说我们传递的一些参数我们可以来看一下
[15:51] 在这个地方呢我们可以来配一下配一下之后呢比如说我们配一个name等于itcastok配完了之后呢我们再来启动你可以看一下我们传的那个参数是不是就可以获取出来了可以吧ok啊没有问题是吧所以呢这个还是比较简单的哈这两个呢两个都一样你用哪个都可以啊两个一般我们只用其中的一个而且他们呢也是一起被调用的好嘞那么这两个说了一下之后呢我们来说这个这两个
[16:20] 那么这两个要想去生效的话需要配置一下在哪个地方配呢其实呢就是在我们的meta info的spring factories里边去配我们比如说我们来配一下meta-info然后呢这个文件很熟悉了.factory变y为i加es好这么一个文件其实有个小技巧你看这个文件它如果变了样式啊干了一个图标就证明你写对了
[16:49] 那么这个怎么去配呢这个文件将来在我们整个工程启动的时候会自动被扫描到它是一个固定的写法对吧然后它是一种建制对的方式比如说你要配这个的话我们这样我们把这个名这个名这个名的全路径名我们给它复制一下注意啊是全路径名就是这个接口的名称然后呢放到这个键的位置等于谁呢等于你自己定义的这么一个实现类好我们把它的引用给它复制一下
[17:19] 放到这个位置当然你想换行的话呢也可以啊我们就不换了不换了之后呢接下来我们就配了一个对吧这个配了吧这个没配对吧那么我们可以来看一下能不能生效走看一下日志打印诶注意看啊生效了吧这个地方是不是打印出来了这个initial layer了对不对被执行了它是在什么时候执行的呢你注意看它是不是在这个图标就是这个图标叫做banner
[17:46] banner打印完之后呢它就来初始化或者说init这个init呢我们可以用于在项目还没有去准备IOC容器之前呢去检测一些资源是否存在对吧就这个意思那么这个我们会配了之后呢那第二个是不是都是一样一样的好我们把这个的名字呢全录进名我们给它复制一下并且呢放到我们这个里边来好等于谁呢等于我们自己定义的这个玩意儿的名字好粘过来
[18:17] 站过来之后呢什么都不用干了我们重新启动一下可以来看一下效果哎 到错了你看这个地方是吧他说一个非法的参数异常非法参数异常那个参数呢我们exception我们就不看了我们来看cause by一般我们是不是都是原因啊原因我们看cause by他说没有一个匹配的方法异常哪个没有匹配呢说你这个my这个springapplication wrong listener没有一个匹配的方法哎 没有什么匹配方法呢
[18:45] 他说没有一个init的匹配方法这个init匹配方法呢需要两个参数init啥意思呢一般提这个init就是构造的意思他说没有一个构造哪个构造呢需要两个参数的构造一个是screwed application的构造还有一个磁步串的构造他为什么需要构造呢我们可以来看一下我们第一次来实现这个接口可能不熟悉没关系啊我们点到这个接口里边去然后呢我们看一下它的实现类其实人家给我们定义了实现类的你看这是我们自己写的吧
[19:15] 人家也有一些实现类对吧OK啊那么点进去看这个实现类呢实现了它对吧实现了它之后呢你注意看这个地方你看它里边前面定了一些成员变量然后呢在这个地方你看它是不是提供了这么一个构造方法对不对名字跟这个类名是一样的然后呢这个构造方法有两个参数一个是Spring ApplicationOK吧还有一个是String Axe一些接收的参数那么这个两个呢其实呢是这个意思
[19:42] Spring Application其实就是我们真正项目启动的时候那个事件源了那么将来这个事件源上可以产生很多个不同的生命周期相关事件所以在这个监听器里边要把这个事件源搞进来那么差不多它弄完了之后它给我们提供了这么一个我们也可以照着抄一个那么我们在我们自己写的这个里边来写一个构造
[20:10] 注意啊这个构造如果不存在就会报错刚才我们看到了对吧constructor好我们也自己写一个没问题了吧OK没问题了之后呢它告诉你说什么不能自动注入对吧是一个语法检测的问题那么其实你看这个complement是不是没有什么用啊对吧所以呢我们把它删掉了不让它自动注入了然后这样就不会有什么问题了那么这样弄完了之后呢我们再来启动看一下能不能行哎你看好了是吧没有报任何的错那么现在我们来看
[20:40] 你看starting项目启动中第一个方法是不是就被调用了对吧你看在最上边调用的那什么都这个基本上不会被用的然后第二个呢或者说你在项目启动的时候呢你可以这样做在starting的位置呢你可以检测一些硬件的环境是否是好的对不对当然这个呢其实都是一些当然他用的比较少然后呢environment就是我们的环境正在准备中环境对象正在准备准备可以来加载这些配置信息了然后呢加载完配置信息之后呢我们
[21:09] 这个地方就可以来打印这个图标打印完图标之后呢context prepared准备来准备上下文的一个对象了好上下文的对象准备好了这个意思就是环境对象已经准备好了然后呢准备好了之后才会加载这个图标的因为这个图标呢是根据我们的配置信息出来的但是我们可以来看context prepared上下文开始加载然后呢打印了一些日志然后呢上下文加载完成了之后然后对吧然后呢开始启动启动完成了
[21:39] 到这个地方呢我们的启动就完成了或者说到这个地方我们的IOC容器就出发好了待会我们可以来看一些日志的信息然后这两个是不是执行这是刚才我们自己写的两个最后呢告诉你项目真正的启动完成开始运行OK啊 弄完了其实你会发现啊我们如果自己要来去实现Spring Boot提供的这些监听机制的话呢在项目启动的时候它给我们搞了很多很多的事件发布了一下我们只需要写这些监听器来监听
[22:09] 就可以了那么当然这个内部呢其实是这样做的我们可以来看看原码就是在Spring Boot项目启动的时候或者说在Spring Boot内部它给我们定义了很多生命周期相关的事件我们可以瞧一瞧Spring Boot这个地方这个包Spring Boot这个包核心的这个包然后呢我们可以看一下ORG Framework Spring Boot这个包包里边有一个叫做ContextContext里边我们找到这个EventEvent是不是就是事件啊OK
[22:37] 那么你看啊Spring Boot给我们定义了很多个事件啊我们可以看啊比如说我们随便找一个Application prepared对吧Application是不是开始准备啊你看刚才我们是不是也有一个什么Context prepared对吧它发布这么一个事件比如说Application starting是吧Event你看我们是不是有一个Starting是吧都是Event嘛它发布这么一个事件那发布了这个事件之后呢将来这些监听器接口它内部已经给你注册好了你需要干的事呢就是来实现就可以了
[23:07] 我们可以来看一下这个事件你看这个事件它继承自这么一个类那这个类我们再来看你看它是不是又去继承了一个APP event再点进去看APP event继承了一个event object那个event object你看是不是我们Java YouTube包的event object最终其实我们说Spring Boot的事件就是我们对我们的Java的事件的一个封桌对吧OK那么简单的我们了解了一下Spring Boot的事件监听
[23:36] 的使用方式那么将来呢我们代码呢可能就不能说我们在里边只是输出了我们要来完成具体的业务逻辑的一些操作在不同的时机你要来完成不同的事情的OK那么Spring Boot对应的事件监听的一个机制我们就简单的介绍到这个地方

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Spring Boot 应用程序的监听机制，包括 SpringApplicationRunListener、ApplicationRunner、ApplicationListener 等接口的使用和执行时机。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: PPT 标题页，显示“Spring Boot 监听机制”。
画面 2: IDE 中展示项目结构，选中了 SpringApplicationRunListeners.java。
画面 3: 展示 SpringApplicationRunListener.java 中的 contextPrepared、contextLoaded、started、running 方法及其注释。
画面 4: 在 IDE 中右键点击 MySpringApplicationRunListener.java，弹出菜单。
画面 5: 在 IDE 中搜索并选中 ApplicationRunner.class。
画面 6: 展示 Spring Boot 源码中 ApplicationRunner 接口的定义。
画面 7: 编写 MyApplicationRunner 类，实现 ApplicationRunner 接口，并在 run 方法中打印 args.getSourceArgs()。
画面 8: 编写 MyApplicationContextInitializer 类，实现 ApplicationContextInitializer 接口，并在 initialize 方法中打印信息。
画面 9: 运行 SpringBootListenerApplication，控制台输出了 MyApplicationContextInitializer 的初始化信息。
画面 10: 展示 SpringApplicationRunListener 的源码，其中包含 starting、environmentPrepared、contextPrepared、contextLoaded、started、running、failed 等方法。
画面 11: 控制台输出了 MySpringApplicationRunListener 的 starting 方法执行信息。
画面 12: 在 MySpringApplicationRunListener 中重写 starting 方法，打印“starting...项目启动中”。
画面 13: 展示 Spring Boot 源码中 org.springframework.boot.context.event 包下的类结构。
画面 14: 在 MySpringApplicationRunListener 中重写 environmentPrepared、contextPrepared、contextLoaded、started、running、failed 方法，分别打印对应阶段的信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```java
void contextPrepared(ConfigurableApplicationContext context);
// Called once the application context has been loaded but before it has been
// refreshed.
// @param context the application context

void contextLoaded(ConfigurableApplicationContext context);
// The context has been refreshed and the application has started but
// @link CommandLineRunners and @link ApplicationRunners have not been called.
// @param context the application context.
// @since 2.0.0

void started(ConfigurableApplicationContext context);
// Called immediately before the run method finishes, when the application context
// has been refreshed and all @link CommandLineRunners and @link ApplicationRunners
// have been called.
// @param context the application context.

void running(ConfigurableApplicationContext context);
// Called when a failure occurs when running the application.
// @param context the application context or @code null if a failure occurred before
// the context was created.
```

画面 4:
```java
starting() {
    out.println("Starting...项目启动中");
}

environmentPrepared(ConfigurableApplicationContext context) {
    out.println("environmentPrepared...上下文对象开始准备");
}

contextLoaded(ConfigurableApplicationContext context) {
    out.println("contextLoaded...上下文对象加载完成");
}

started(ConfigurableApplicationContext context) {
    out.println("started...上下文对象加载完成");
}

running(ConfigurableApplicationContext context) {
    out.println("running...项目启动完成，开始运行");
}

failed(ConfigurableApplicationContext context, Throwable exception) {
    out.println("failed...项目启动失败");
}
```

画面 6:
```java
/**
 * Interface used to indicate that a bean should {@code run()} when it is contained
 * within a {@link SpringApplication}. Multiple {@link ApplicationRunner} beans can be
 * defined within the same application context and can be ordered using the {@link Ordered}
 * interface or the {@link @Order} annotation.
 * @author Phillip Webb
 * @since 1.3.0
 */
@FunctionalInterface
public interface ApplicationRunner {
    void run(ApplicationArguments args) throws Exception;
}
```

画面 7:
```java
package com.theima.springbootslistener.listener;

import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.stereotype.Component;

@Component
public class MyApplicationRunner implements ApplicationRunner {
    @Override
    public void run(ApplicationArguments args) throws Exception {
        System.out.println("ApplicationRunner...run");
        System.out.println(args.getSourceArgs());
    }
}
```

画面 8:
```java
package com.theima.springbootslistener.listener;

import org.springframework.context.ApplicationContextInitializer;
import org.springframework.context.ConfigurableApplicationContext;

@Component
public class MyApplicationContextInitializer implements ApplicationContextInitializer {
    @Override
    public void initialize(ConfigurableApplicationContext applicationContext) {
        System.out.println("ApplicationContextInitializer...initialize");
    }
}
```

画面 10:
```java
void starting();

// Called once the environment has been prepared, but before the
// @link ApplicationContext has been created.
// @param environment the environment

void environmentPrepared(ConfigurableEnvironment environment);

// Called once the @link ApplicationContext has been created and prepared, but
// before sources have been loaded.
// @param context the application context

void contextPrepared(ConfigurableApplicationContext context);

// Called once the application context has been loaded but before it has been
// refreshed.
// @param context the application context

void contextLoaded(ConfigurableApplicationContext context);

// Called once the application context has been refreshed and the application has started but
// @link CommandLineRunners and @link ApplicationRunners have not been called.
// @param context the application context.

void started(ConfigurableApplicationContext context);

// Called immediately before the run method finishes, when the application context
// has been refreshed and all @link CommandLineRunners and @link ApplicationRunners
// have been called.
// @param context the application context.

void running(ConfigurableApplicationContext context);

// Called when a failure occurs when running the application.
// @param context the application context or @code null if a failure occurred before
// the context was created.
```

画面 12:
```java
public class MySpringApplicationRunListener implements SpringApplicationRunListener {
    @Override
    public void starting() {
        System.out.println("starting...项目启动中");
    }
}
```

画面 13:
```java
package org.springframework.boot.context.event;

import org.springframework.context.ApplicationEvent;
import org.springframework.context.ApplicationListener;
import org.springframework.context.event.ApplicationContextEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework

