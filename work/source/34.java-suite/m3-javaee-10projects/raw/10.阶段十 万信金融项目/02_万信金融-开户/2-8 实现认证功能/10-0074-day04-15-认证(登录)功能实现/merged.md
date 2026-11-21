# day04-15-认证(登录)功能实现

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-8 实现认证功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-8 实现认证功能\day04-15-认证(登录)功能实现_【海量资源尽在 666java.com】.mp4
- 时长 23分34秒（音频 1414s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 飞运代理这一块的准备工作我们搞定之后呢接下来就可以实现登录功能了啊但是这个登录功能啊我们需要先给大家说道说道首先呢我们要给大家说的是这个登录功能这个代码不能像以前一样这个我想写到哪写到哪啊这就有规定了为啥有规定呢呃是因为咱给大家提供的这个UA这个服务啊它采用了这么一个框架
[00:28] 叫spring security os 2这个框架集成的一个框架那么你使用了这个框架你就得按照人家框架的这个什么呀整体设计或者规定来那么他要求呢我们这个认证或者登录这一块的代码必须写到这个地方大家注意看我先找到这个地方啊就在ua工程里边呢有一个都闷都闷里边不一定是放实体类的啊这里边有一个这个名字比较长有一个你看
[01:00] 后缀是什么结尾是什么Handler找到他那么在这个类里边有一个方法就叫证明Authentication名字也比较长这个方案名或者说这个单词就是认证的意思就认证的意思按照这个框架的要求我们的实现登录或者实现认证的代码应该写到方案里边别的地方你不能乱写这是首先你要知道而且别的代码
[01:30] 整个UA这个共同的其他地方代码你也不用管不用管了你只需要按照要求在这边写我们实现认证或者登录功能代码就行了那在动手写这个代码之前呢我们要先整体了解一下这个方法因为这个方法呢也是框架提供的那这个方法你看既有参数又有什么呀返回值那因此呢我们对这些参数和返回值必须有一个很清楚的一个认识一个了解
[01:58] 要不然呢我们将来在这里边没法实现功能因为你在实现认证功能的时候一定会离不开这些参数还有这个什么呀反位值的对不对那咱先说参数吧有几个参数三个参数是吧这三个参数都是干嘛用呢咱接下来看看讲义里边呢有详细的说明啊关于这个方法好我们接下来看一下第一个参数字不刷类型啊多闷表示什么意思呢他表示你此次登录的这是B端用户还是C端用户
[02:28] 这个提以前提过吧B端C端对不对那这个值呢是由接入方就是前端传过来他传C就是C端用户登录他传B就是B端用户登录这是区分你是C端用户还是B端用户的第二个参数呢也是字幕上类型是用来设置或者表示什么呀登录方式就是你是用账号密码登录的还是我们的什么呀短信验证码这个咱以前在讲注册的时候是不是提过这个事
[02:58] 我们默认是不是通过短信验证码对吧当然我们也可以嫌麻烦的话也可以把短信验证码给它关掉然后改成什么呀这号密码登录而且我们当然说了嘛手机号默认就是什么呀密码对那这个值呢也是由接入方就前端传过来他想用密码认证他就传一个值他想用这个短信认证就传另外一个值就行具体是什么值一会再说然后第三个参数叫tokentoken咱前面提过是不是另牌对吧
[03:27] 但是你要注意啊这儿呢他只是一个参与名我说参与名是不是其他名字都想对不对所以其实这我觉得哎呀叫token的话容易误导大家容易误导大家什么呀容易让大家认为这就是另牌了但是这可不是另牌啊你要注意我们这是不是在实现什么功能登录功能我们说了登录成功之后是不是才可以生成另牌是不是说这个地方可不是另牌啊可不另牌那这个参与是干嘛的呢你看前边
[03:56] 这个类啊他的名字很长对吧你看什么user name password authentication token啥意思呢第三个参数是用来封装前端传过来的账号和什么呀密码对账号密码然后是封装到这个对象里边所以说一定要注意他不是另牌啊所以说这个参数是用来封装前端传过来的这个账号和密码因为我们将来是不是要校验你的账号密码是否正确啊
[04:26] 正确了我才生成什么呀另一盘啊所以这个你一定要注意这是这三个参数的作用然后我们再看一下啊这个方法呢还有一个什么呀返回值叫unified什么呀user details那么这个对象呢是用来你看这说了登录成功的时候返回来你登录不成功呢你就另说我可以跑一场对不对那你登录成功了那么我就要返回这个对象
[04:55] 那个这个反而这个对象干嘛呢你看好啊跟当前用户或账号有关的一些信息你都可以存到或者封装到这个什么呀对象里面哎因此呢你就知道哦这个对象其实就是同这个对象其实就是什么呀成功之后对吧成功之后我用来存或者封装这个当前登录用户的一些什么呀基本信息的而且你封装成这个对象之后呢这个框架
[05:22] 这个框架会自动根据这个对象里边内容去生成什么呀令牌注意看了啊这句话非常非常关键非常非常关键令牌是怎么生成的是在登录成功之后由这个框架自动注意是自动也就是说将来我们在写代码的时候并不会由我们去编写什么呀生成令牌这种代码你不用管登录成功之后呢你把用户的基本信息封装到这个对象里边剩下事你就不用管
[05:50] 这个框架会根据这个对象里边内容去生成什么呀令牌当然大家也能猜到封装到这个对象里边的内容应该会作为GWT令牌的第几部分存进去想想咱以前说过GWT令牌分几部分三部分其中哪一部分是咱自定义的可以对第二部分但是这个事你不用管这个事你不用管他就帮我们自动这个把这个令牌就干什么呀生成了而且令牌里边就保存了咱用户的一些什么呀对一些基本的一些数据
[06:22] 所以说呢我们在实现这个登录功能的时候啊你一定要对这个方法的参数还有什么呀这个返回值这个相关的一些东西必须要搞清楚清楚了之后呢咱接下来就开始动手编写这个具体的认证或者说登录这个功能的相关代码那这里边的话我们大概可以分成这几个步骤这个整个洗牙来代码有点多但是还是比较清晰的第一步呢就是
[06:55] 取数据啥意思啊你看我们说了前端就是接入端传过来的数据是不是都在这里边啊所以你得从这里边先把数据给干什么呀对取出来那就是从客户端吧好吧从客户端取数据那第二步就是什么呀取到数据之后呢取到数据之后第二步就是把这个数据发到谁那边对统一账号那边嘛让他进行什么呀教用教验是吧所以第二步呢就是
[07:31] 远远程调用统一账号服务进行账号密码什么呀叫验对那接下来呢那叫验的时候呢就该出结果了嘛对不对要么成功要么什么呀失败所以说我们就可以先考虑失败的情况这里边可以进行异常对处理如果出问题了我就跑异常那当然了他也可能会
[08:04] 认证什么呀通过认证通过他肯定就不会走这了就接着往下走了那认证通过之后呢我们该干啥吗那就是什么呀教研通过我就要干什么呀对那就是登录成功呗登录成功把用户数据封装到哪个对象里边对就是这个对象对象中
[08:38] 所以整体呢就是四个步骤就是咱需要写的代码咱一个一个来吧咱接下来就先编写第一步的代码第一步的代码呢就是从客户端取数据那我们要取的数据其实主要是来自于这个第三个参数前两个参数一般是作为判断用的咱暂时先不管它先用不着咱是先从这个第三个参数里边取数据这里边我们说存有什么账号和什么密码咱把账号密码都要取一下先取账号吧
[09:08] 怎么取呢他有现成的方法token点get什么呀name这个你可以认为他就是什么呀对就是账号我们呃声明一个变量接收一下啊就是就叫什么什么呀stream username是账号然后密码怎么取啊密码是token点get你觉得会是谁呢他不是他啊不是他是这个方法
[09:39] 这个方法返回的就是密码但是呢他不是字不刷类型对不对但是我们的字我们的这个密码一定是字不刷啊我们的密码一定是字不刷所以说我们给他转换成一个什么呀字不刷类型就行了然后呢我们就可以这个也声明一个变量吧声明一个叫啥名呢叫p i e s e n te d 吧p a s s w r d对吧person t 的person t 的password
[10:13] 我们起这么一个名字来接收这个什么呀密码那现在账户密码都取出来了那你接下来你要做一些基本的判断比如说他为不为空啊是不是如果为空的话那我是不是就跑一场对你相当于账号为空吗是不是所以这里边呢我就要干什么呀做一些判断当然密码是不是也得判断密码为空是不是也不行啊所以接下来我就要做一些判断呃字符刷这个非空教验我们应该可以有一些工具类吧string youtube对
[10:44] 点ease blank啊easeamper的ease blank我们用ease blank用它就行了这个方法的话你要想了解的话你可以这个看一下它的原码啊这个代码咱观察起来还是比较方便的你看看它是判断一个脑和它的一个什么呀长度对不对所以我们就用它就行判断谁啊判断user name吧是不是我们要判断这俩我们可以把这个代码往下放
[11:16] 当然我们这是不是要结合一幅进行判断一幅如果我一哭我就要干什么要抛一场抛哪一场是不是还是抛咱们以前那什么business不是的因为我们在现在用的是一些框架所以说我们要按照人家的要求来我们要抛这个叫bad credit tillnecception那就是第一个了就是第一个这里边的话
[11:53] 参数呢是这个提示信息这里边你可以提示这个什么呀账户维库就行了那同样的道理这个密码是不是也是如此我们粘过来然后呢改一改就行了那这我应该给个什么提示信息啊那就是密码维库密码所以我们从客户端取出来这两个数据之后呢要做一些最基本的一些什么呀对判断
[12:26] 这还有一个小问题啊这有个小问题那如果密码为空的话其实到这步是不是就为空那你在兔子追问这儿是不该报空指针异常是不是来这样咱稍微改一改稍微改一下啊这里边有一些细节咱这样子呗我这样子改就行了啊这样呢我得他改成这个这就完了明白什么意思吧哦他这是obj 的obj 类型的话我就不用他来盘算我就可以是什么呀
[13:00] 如果他等于闹是不是密码为空如果他不等于闹的话我就给他转换成字母串是不是接受一下后边就可以拿他用了对不对这样稍微做一下修改啊一定要注意了呃原因在于这啊如果密码为空其实你调这个方法的时候是不是得到就是空然后你再调吐存方法他会跑异常所以说呢我这呢是调这个方案之后我就先判断他会不会空不为空的情况下我再调什么呀吐存方法得到这个密码
[13:30] 我这儿呢稍微改造一下那接下来的话我们就该进行这个什么样第二步了啊第二步呢就是我们说了呢把刚才的这个账号密码然后远程调用或者远程请求发到哪边统一账号这边让他进行什么呀脚印呃这个怎么实现呢我们是不是就想起来要用这个什么呀对这个代理非你这个代理调login方法但是大家看他这要的是一个login dto对象对不对
[14:00] 因此按照他的要求我们需要把账号密码这些信息是不是先封装到对象里边然后是不是就把对象给远程传过去就可以了对不对所以我们这先做一个准备工作account log inDTO对不对我直接拗一个了对然后开始往里边存东西都存什么东西咱看看有个set do men我们有
[14:31] 咱刚才说了这个认证方案第一个参考不就传过来B端和C端用户吗我们需要把它扔进来扔进来之后呢一块呢传到同一账户那边他想怎么用那是他的事他可能会做一些判断是不是那接下来不就是账号密码了账号账号其实我们用的就是这个谁啊这个set什么呀yoyo name这也是我们的账号嘛那另外呢这里边也有一个细节需要注意的
[15:03] 我们这个手机号呢我们也给他设置成这个优质内容因为之前咱也给大家说过嘛嗯我们一般登录的时候可能就是把手机号作为什么呀账号去登录啊所以说这个地方手机号这个值也得付一下将来用哪个到时候再说啊我们接下来还有什么呀密码密码不就是前面这个密码对吧就是这个密码所以这是我们把需要传过去的这些数据是不是先给他封装成什么呀对这个DTO对象
[15:37] 然后接下来我们是不是就可以干什么呀把它注入进来吗是不是把它注入到这里边就跟以前一样我注进来之后然后是不是掉了个音方法就可以发起远程警觉了是吗反正咱以前是这么做的但是这次不行啊这次不行这次为啥不行你看咱这个环境不一样啊你看咱当前这个类你看我上面有没有加死不用相关的一些注解比如说Service啊component啊这注解有没有加没有证明这个类将来
[16:07] 并没有就是交给直接进行什么样管理所以我们在这进行注入不行注入不行那怎么办但是我需要是不是代理对象对不对这个时候我们就需要通过稍微原始的一点写法这一块我们给大家提供的一个工具类我们直接拿用就行了就是叫什么APPLSATLNapplication
[16:38] packs help这是我们给大家提供好的一个工具类这里边有给的b那么这个方法呢就是帮我们得到他的这个什么呀代理对象你只需要把这个接口给他就行剩下事咱就不用管对我们就可以得到这个代理对象了然后呢我们接收一下接收一下这个对象呃这报错呢是我们需要强转的因为给他并返回的是我们这个类型我们这需要做一个强转就对就这个样子
[17:15] 那代理对象有了之后呢接下来自然是不是就调用他的什么方法给那个login发起远程请求然后呢把这个DTO对象给干什么呀传过去那其实这行代码一执行其实说白了这个DTO对象是不是就被远程传到ArkConner这边是不是就到这具体位置应该是这对不对那这边ArkConner这边校验完之后处理完之后呢是不是返回了有这个rest response我们得接受一下
[17:47] 那将来成功与否是不是就从这里边取数据了对不对他返回到这个信息都在这里边吧所以说我们得接受一下那其实到这儿为止的话咱们第二步是不是就走完了对我们已经发起远程调动了把这儿面都传过去了也得到这个结果那接下来就是针对这个结果进行分析了那就两种情况要么就是这里边出问题了就是没成功那我就抛异常或者做一些异常处理
[18:16] 那如果成功了那我就把一些用户的一些数据是封装热这个对象里边然后干什么呀反过来就行那所以说我接下来就开始走第三步了啊开始判断怎么判断是不是从这里边取东西吗呃这里边大家应该知道里边是不是判断这个时间扣到就行了那我们说呢零表正常了非零就表示出问题了是不是那我这里边就好判断了呀我就可以怎么写衣服这个什么呀
[18:43] rest response.get什么呀code 嘛如果怎么写对不等于0就表示这个认证没有通过就是出问题了那我接下来还是跑一场跑哪一场呢还是刚才这个bad对这个一场那这里边呢我们就嗯也需要给一个提示信息那这就是登录失败呗对不对就是登录失败那就是登录失败就行
[19:15] 然后呢这里边也有可能会因为什么来登录失败了有可能是因为这个C端和B端用户啊因为C端和B端用户将来登录的时候我们的处理是不一样但这呢这块判断我们可以先放一放可以先不用管因为我目前登录一定是C端用户登录目前啊一定是C端用户登录我这个呢我们暂时先不做判断我们只判断一下哎反而值如果不是0就证明登录失败
[19:43] 那如果是零是不是就证明成功了成功之后我们要做什么事呢这就是第四步那登录成功了就说你的账号密码都正确对吧交易通过那我们接下来要做的事呢那就是把用户相关的信息是不是开始往这个对象里边进行什么呀对进行封装啊那这个对象的话就是我们需要自己干什么呀扭一下对自己扭啊等于扭对自己扭一下
[20:14] 你玩之后呢大家一定要注意这里边呢我们是通过他的代餐构造啊代餐构造然后把相关的一些数据给他存进去我们也其实也不需要存啥东西就是账号密码啊还有他的一些什么呀权限信息对吧那账号的话那不就是哪个账号那账号其实不就是这个吧有点内幕是吧这不就是账号吗当然了你这个账号呢他应该
[20:44] 这建议成功之后这里边存的是不是也有对吧你也可以从这里边去都可以我要是从这里边取的话应该怎么去rest response第二response点get什么他的返回的数据是不是存在result里边对吧点get什么 username也是可以的都可以这是我们要存进去的第一个数据就是账号第二个数据就是这个什么密码然后第三个数据就是
[21:21] 它涉及到的一些权限但是权限这一块目前咱还不涉及因为咱目前只是做认证还没有做这个授权啊所以第三个参数目前你先采用这么一个固定写法呃他是调用了一个工具类啊叫AUTHORUTILS.REITAUTHORUTILS.REIT这是干嘛呢你先不用管啊这个将来我们在做授权的时候再说所以这儿呢第三个参数你先不用管先放到这儿就行了
[21:51] 这是我们相当于目前是相当于把账号和密码是不是先放进去那然后还没有完我们还需要往里边再放东西还需要放什么东西呢来我们还需要放这个东西我们需要把手机号也给他放进去对这个手机号因为我们将来这些东西都有用啊都是有用的嗯然后最终封装好之后呢我们最终是不是就把这个对象作为返回值干什么呀返回就行了因为这个方法认证这个方法整体
[22:29] 最终要的是不是就这个反悔值对不对你看这是咱整个这个四步就全部想那如果出问题的话是不是就是登录失败那如果成功的话我们是就把账号密码还有一些将来将来还有一些权限信息是不是就封装到这里边然后返回来我们要做的事是做完了但是其实整个这个事还没做完刚开始咱们在讲义里边也说了就是你把这个对象返回之后框架会根据里边内容去生成什么地板但是这个事用咱管吗不用管
[23:00] 你也接触不到这一点我们要做的事呢就是把这个对象就返回了剩下的事就是他会根据这个对象的内容生成令牌而且这个令牌里边存的就有咱刚才说的这些什么呀这些内容啊手机号啊账号啊对吧权限啊这些都在这里所以说呢我们在用OAuth2还有GWT这些技术来实现这个认证功能的时候呢这个代码主要就是写到这个方案里边一共四个步骤啊关于这块这个
[23:31] 内容我们就说到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解如何在 UAA 工程中实现自定义的用户认证处理器，通过重写 authentication 方法调用账户服务完成登录认证，并处理异常和返回用户信息。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 页面，内容为“2. 注意检查启动类上的注解”和“3. 在UAA工程的domain包中找到IntegrationUserDetailsAuthenticationHandler类，并实现其中的authentication方法”。
画面 2: 在 IDE 中打开 `IntegrationUserDetailsAuthenticationHandler.java` 文件，高亮显示 `public UnifiedUserDetails authentication(String domain, String authenticationType, UsernamePasswordAuthenticationToken token)` 方法。
画面 3: 展示 PPT 页面，内容为“2. 注意检查启动类上的注解”和“3. 在UAA工程的domain包中找到IntegrationUserDetailsAuthenticationHandler类，并实现其中的authentication方法”。
画面 4: 在 IDE 中，`IntegrationUserDetailsAuthenticationHandler.java` 文件中，光标位于 `token` 变量上，显示其类型为 `UsernamePasswordAuthenticationToken`。
画面 5: 在 IDE 中，`IntegrationUserDetailsAuthenticationHandler.java` 文件中，高亮显示 `public static boolean isBlank(String str)` 方法，并有注释说明空白字符定义。
画面 6: 在 IDE 中，`AccountController.java` 文件中，光标位于 `AccountController` 类上。
画面 7: 在 IDE 中，`AccountController.java` 文件中，光标位于 `AccountController` 类上。
画面 8: 在 IDE 中，`AccountController.java` 文件中，光标位于 `AccountController` 类上。
画面 9: 在 IDE 中，`IntegrationUserDetailsAuthenticationHandler.java` 文件中，高亮显示 `public UnifiedUserDetails authentication(String domain, String authenticationType, UsernamePasswordAuthenticationToken token)` 方法。
画面 10: 在 IDE 中，`IntegrationUserDetailsAuthenticationHandler.java` 文件中，光标位于 `AccountAgent.login(accountLoginDTO)` 方法调用处。
画面 11: 在 IDE 中，`IntegrationUserDetailsAuthenticationHandler.java` 文件中，高亮显示 `throw new BadCredentialsException("登录失败");` 语句。
画面 12: 在 IDE 中，`IntegrationUserDetailsAuthenticationHandler.java` 文件中，高亮显示 `UnifiedUserDetails unifiedUserDetails = new UnifiedUserDetails(restResponse.getResult().getUsername(), presentedPassword, AuthorityUtils.createAuthorityList("ROLE_ADMIN"));` 语句。
画面 13: 在 IDE 中，`IntegrationUserDetailsAuthenticationHandler.java` 文件中，光标位于 `AccountLoginDTO` 类的 `setMobile()` 方法上。
画面 14: 在 IDE 中，`IntegrationUserDetailsAuthenticationHandler.java` 文件中，高亮显示 `UnifiedUserDetails unifiedUserDetails = new UnifiedUserDetails(restResponse.getResult().getUsername(), presentedPassword, AuthorityUtils.createAuthorityList("ROLE_ADMIN"));` 语句。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
public class IntegrationUserDetailsAuthenticationHandler {
    // 认证处理
    @Param domain 用户域，如前端用户、后端用户等
    @Param authenticationType 认证类型，如密码认证、短信认证等
    @Param token
    @Return
    public UnifiedUserDetails authentication(String domain, String authenticationType, UsernamePasswordAuthenticationToken token) {
        return null;
    }
    private UnifiedUserDetails getUserDetails(String username) {
        Map<String, UnifiedUserDetails> userDetailsMap = new HashMap<>();
        userDetailsMap.put("admin", new UnifiedUserDetails("admin", "111111", AuthorityUtils.createAuthorityList("ROLE_ADMIN")));
        userDetailsMap.put("zufan", new UnifiedUserDetails("zufan", "111111", AuthorityUtils.createAuthorityList("ROLE_ADMIN")));
        return userDetailsMap.get(username);
    }
}
```

画面 4:
```java
public class IntegrationUserDetailsAuthenticationHandler {
    // 认证处理
    @Param domain 用户域，如前端用户、后端用户等
    @Param authenticationType 认证类型，如密码认证、短信认证等
    @Param token
    @Return
    public UnifiedUserDetails authentication(String domain, String authenticationType, UsernamePasswordAuthenticationToken token) {
        // 从客户端获取数据
        String username = token.getPrincipal();
        if (StringUtils.isBlank(username)) {
            throw new BadCredentialsException("用户名为空");
        }
        if (token.getCredentials() == null) {
            throw new BadCredentialsException("密码为空");
        }
        // 2. 调用统一账户服务，进行账户密码校验
        AccountLoginDTO accountLoginDTO = new AccountLoginDTO();
        accountLoginDTO.setDomain(domain);
        accountLoginDTO.setUsername(username);
        accountLoginDTO.setPassword(token.getCredentials().toString());
        AccountAgent accountAgent = (AccountAgent) ApplicationContextHolder.getBean(AccountAgent.class);
        RestResponse<AccountDTO> restResponse = accountAgent.login(accountLoginDTO);
        // 3. 异常处理
        if (restResponse.getCode() != 0) {
            throw new BadCredentialsException("登录失败");
        }
        // 4. 登录成功，把用户数据封装到UnifiedUserDetails对象中
        UnifiedUserDetails unifiedUserDetails = new UnifiedUserDetails(restResponse.getResult().getUsername(), token.getCredentials().toString(), AuthorityUtils.createAuthorityList("ROLE_ADMIN"));
        unifiedUserDetails.setMobile(restResponse.getResult().getMobile());
        return unifiedUserDetails;
    }
}
```

画面 5:
```java
public static boolean isBlank(String str) {
    return str == null || str.trim().length() == 0;
}
```

画面 6:
```java
// 2. 调用统一账户服务，进行账户密码校验
AccountLoginDTO accountLoginDTO = new AccountLoginDTO();
accountLoginDTO.setDomain(domain);
accountLoginDTO.setUsername(username);
accountLoginDTO.setPassword(presentedPassword);
AccountAgent accountAgent = (AccountAgent) ApplicationContextHolder.getBean(AccountAgent.class);
RestResponse<AccountDTO> restResponse = accountAgent.login(accountLoginDTO);
// 3. 异常处理
if (restResponse.getCode() != 0) {
    throw new BadCredentialsException("登录失败");
}
// 4. 登录成功，把用户数据封装到UnifiedUserDetails对象中
UnifiedUserDetails unifiedUserDetails = new UnifiedUserDetails(restResponse.getResult().getUsername(), presentedPassword, AuthorityUtils.createAuthorityList("ROLE_ADMIN"));
unifiedUserDetails.setMobile(restResponse.getResult().getMobile());
return unifiedUserDetails;
```

画面 10:
```java
// 2. 调用统一账户服务，进行账户密码校验
AccountLoginDTO accountLoginDTO = new AccountLoginDTO();
accountLoginDTO.setDomain(domain);
accountLoginDTO.setUsername(username);
accountLoginDTO.setPassword(presentedPassword);
AccountAgent accountAgent = (AccountAgent) ApplicationContextHolder.getBean(AccountAgent.class);
RestResponse<AccountDTO> restResponse = accountAgent.login(accountLoginDTO);
// 3. 异常处理
if (restResponse.getCode() != 0) {
    throw new BadCredentialsException("登录失败");
}
// 4. 登录成功，把用户数据封装到UnifiedUserDetails对象中
UnifiedUserDetails unifiedUserDetails = new UnifiedUserDetails(restResponse.getResult().getUsername(), presentedPassword, AuthorityUtils.createAuthorityList("ROLE_ADMIN"));
unifiedUserDetails.setMobile(restResponse.getResult().getMobile());
return unifiedUserDetails;
```

画面 12:
```java
// 4. 登录成功，把用户数据封装到UnifiedUserDetails对象中
UnifiedUserDetails unifiedUserDetails = new UnifiedUserDetails(restResponse.getResult().getUsername(), presentedPassword, AuthorityUtils.createAuthorityList("ROLE_ADMIN"));
unifiedUserDetails.setMobile(restResponse.getResult().getMobile());
return unifiedUserDetails;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“UAA服务架构篇”，内容为“2. 注意检查启动类上的注解”和“3. 在UAA工程的domain包中找到IntegrationUserDetailsAuthenticationHandler类，并实现其中的authentication方法”。
画面 3: PPT 标题为“UAA服务架构篇”，内容为“2. 注意检查启动类上的注解”和“3. 在UAA工程的domain包中找到IntegrationUserDetailsAuthenticationHandler类，并实现其中的authentication方法”。
画面 6: PPT 标题为“UAA服务架构篇”，内容为“2. 注意检查启动类上的注解”和“3. 在UAA工程的domain包中找到IntegrationUserDetailsAuthenticationHandler类，并实现其中的authentication方法”。
画面 9: PPT 标题为“UAA服务架构篇”，内容为“2. 注意检查启动类上的注解”和“3. 在UAA工程的domain包中找到IntegrationUserDetailsAuthenticationHandler类，并实现其中的authentication方法”。
画面 10: PPT 标题为“UAA服务架构篇”，内容为“2. 注意检查启动类上的注解”和“3. 在UAA工程的domain包中找到IntegrationUserDetailsAuthenticationHandler类，并实现其中的authentication方法”。
画面 11: PPT

