# day03-19-传统登录实现方式-功能实现

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-5 实现传统登录方式并分析问题
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-5 实现传统登录方式并分析问题\day03-19-传统登录实现方式-功能实现_【海量资源尽在 666java.com】.mp4
- 时长 20分52秒（音频 1253s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 接口定义好之后呢咱接下来就实现功能咱们前面分析过了说这个传统的登录方式它其实主要是进行增删改查当中的查询对吧那咱在实现功能的时候是不是应该先写数据访问层是吧那数据访问层呢咱看看啊Account这边呢因为咱之前是不是实现过这个数据不操作所以说这边呢你看Mapper接口Mapper Interface文件这一套东西是不是都已经有了
[00:32] 所以说呢咱这次在实现登录功能的时候呢数据方案层咱就不用管咱就直接从哪一层开始写对右层就是Service所以咱找到这个接口然后呢在这个接口里边呢我们需要再定义一个方法就是实现登录的一个方法方案名呢自然还是叫什么login对这个参数呢跟control上那个接口里边呢肯定是保持一致的这呢仍然是acc
[01:05] account什么呀login DTO对吧呃这个返回值呢那就是谁呀返回值返回值呢我们是不是返回这个account DTO就OK了对不对跟上面保持一致吧那这样子的话我们就在业务层的接口里边呢定义了一个方法用来实现登录功能那接下来咱找到它的实现类在这个实现类里边呢我们要重写这个login方法
[01:46] 我们看一下在这个位置啊那接下来呢就在这个方案里边呢把传统的这种登录方式这个代码给编写一下那具体的这个思路的话其实我们一般可以有两种做法啊我在这给大家写一下一般有两种做法第一种呢就是第一种呢就是根据什么呀用户名和密码进行一次什么呀查询
[02:17] 查到数据呢就证明登录成功查不到就是登录失败还有一种做法就是先根据什么呀用户名进行查询然后再比对什么呀密码这种方式我觉得也是挺简单挺好理解的就是我查的时候呢只根据用户名查我不带密码不带密码一起玩对不对我只根据用户名查那查出来的话
[02:51] 我再去比对什么呀密码那如果用户名都查不出来那就自然就是登录什么呀失败所以这是分成了两步上面是分成了一步啊那我们这样的准备分成两步去走为什么呢因为咱们的密码注册时候大家也看到了是不是进行加密了是不是你看咱的表里边这个看的啊你看这个表你看这个密码是不是都进行加密了对不对所以说呢
[03:21] 咱准备是分两次啊先根据用户名进行查如果查到了再比对一下这个什么呀密码因为这个过程当中我们还要进行加密解密相关的一些操作啊所以说呢咱准备按照这个思路走一走这个需要大家注意的那么按照这个思路走的话呢自然是不是先进行一次查询根据什么来查对根据用户名去查那这里边呢有一个小小的这个诱逻辑我们需要跟大家说一说
[03:51] 前面的其实大家也见过这个东西哪个东西呢来大家看一下我把可抗它这个实体内打开打开之后大家看这我们的这个用户啊分两种一种是C端用户一种是什么呀B端用户呃我们这有一个业务就说C端用户呢在登录的时候呢他是手机号就是那个用户名啊手机号有用的就这个如果你是C端用户你这个手机号就是作为用户名去用那如果你是B端用户
[04:24] 那就是用这个user name做用户名去登录了所以C端用户和B端用户在这点稍微有点不一样密码还是这个密码所以说呢我们这儿呢要分成两种情况进行判断这是需要给大家说一说的所以说呢我们这儿呢就需要先判断这个用户它是哪一种用户是C端的还是什么呀B端那它是C端还是B端用户这个信息从哪去呢从这里边
[04:54] 那也就是说呢将来前端页面发请求的时候呢他其实呃他带的参数里边就会告诉我们他是C端还是什么呀B端用户而且这个数据将来是封装到这个对象里边所以我们从这里边取这个数据就行那这里边我们直接就进行这个if判断那就是if啊count log in DTO.getDomain对吧点我们要判断一下当然这个我们就不区分代码写了啊
[05:24] 看看他是不是谁啊c就是他是不是c端用户如果是c端用户呢对如果是c端用户我们怎么进行查询呢我们应该是根据什么呀对他的这个用户名我们刚才说就是什么呀手机号啊来我在这写一下注释注意了如果是c端如果是c端用户那么用户名
[05:58] 就是对手机号那么else就表示它是什么呀对else就表示它是B端用户那如果呢是B端用户登录那B端用户登录呢怎么办对那么用户名就是就是账号呗就是账号就是账号所以我们是分成这两个用情况了
[06:34] 其中呢这个B端用户我们目前暂时不用管他因为我们目前还不涉及到B端用户咱目前全是什么呀C端用户就是借钱的人呢投资人呢这些都属于什么呀C端用户这个一定要注意那我说C端用户他的用户名就是什么呀手机号所以我们在进行这个查询的时候其实就是根据什么来查的呀对根据手机号来查的那根据手机号查询的话我们以前有没有实现过这个功能我们找一找
[07:05] checkmobilecheckmobile是干嘛啊这个不是对不对下面也没有对吧那咱这样咱把根据手机号进行查询这段代码咱单独摘出来放到一个方法里好吧这样子呢也便于这个将来更通用那咱就在下面吧单独定义方法了啊private这个它的反应值一定是ACC OUNT吧
[07:39] 查询嘛对不对查出来一定是这个跟表对应的这个实体类这个发明呢比较好奇就叫get a c c o u n tby 什么呀by mobile 嘛咱是不是根据手机号来进行查询呢对吧所以说我们就写上 m o b i l e那参数自然就是对参数自然就是手机号好吹音m o b i l e这咱单独啊
[08:09] 定义这么一个方法来实现根据手机号进行什么查询这里边代码非常简单吧正查询咱以前写过调哪个方法对MP封装好的什么呀get one这里边是要一个warp对象对不对我们直接new了啊这个代码咱以前都写过这里边这个范形是不是就是这个ACC OONT这个实体类这是条件构造器嘛对不对那咱还采用那个Lambda的那种写法吧
[08:40] 这种写法呢它的字段名不容易写错啊我们是做什么查询呢根据手机号对吧而且是不是相等判断第二应该调哪个方法依Q根据哪个字段进行查询呢对accaccountlambda.h呢可以这么写然后呢这个值是多少呢就是咱传进来的这个什么呀参数没错这个代码基本上咱就
[09:08] 想啊对吧然后呢把他查出来的这个对象直接作为返回值就给他返回来就行对然后啊大家看B端用户我们说B端用户呢他也要做查询但是他是根据什么呀账号查了这个账号其实指的就是这个什么Uber name那你看这个是根据手机号这个是根据账号那咱把这里边这个代码咱也摘出来啊单独定义到一个方法里边那这个代码其实跟这段写起来几乎是什么呀
[09:40] 对一样的我就粘一下改一改那这样的就不叫什么get account by什么mobile我们要改成get account by什么username对吧那这个参数也自然要换成什么对user username然后呢这儿是不是也得改一改对不对字段换了吗字段要根据user name去查吗对我们找一找这个谁
[10:14] 对get username没错然后呢参数呢就是这个值啊就是这个user name搞定了吧对就是这么写的啊所以说这两个查询倒是比较简单呃这两个发展单独定义好之后呢在这就可以调用了呗那如果是C端用户我就准备怎么写C端用户呢你就调用这个方法呗那直接就是get什么呀account by什么呀mobile然后手机号呢
[10:47] 那手机号自然是不是从这里边去呗前端传的时候呢里边肯定是带有什么手机号那B端用户这边是不是换一个方法就行了调这个get account by什么呀user name那这个user name呢也是从DTO对象里边来取的对没错啊所以说这里边我们首先要根据用户名进行查询但是由于C端和B端用户呢它这个用户名表示的意思是不一样一个是手机号一个是账号所以说咱这加了一个
[11:21] 小逻辑这两个方案是不是都返回了有account的对象是吧那咱在外边声明一个吧acc account对然后呢我们在这接收一下就行了这个我不用做过多解释了是吧说这呢这块代码是咱先根据用户名进行了查询那查完之后是不是要出结果了对不对出什么结果那要么存在要么不存在嘛如果用户名都不存在是不是就没有必要往后走
[11:59] 是吧我们就可以抛一场我在这就要做判断的一副什么呀哎查完之后如果他还未空如果他还是空的证明这个用户名啊或者这个手机号他都不存在那我们接下来就没有必要往下继续进行了我就要抛一场此之后还是咱自己定义的那个business对吧exception那里边具体的这个
[12:32] 异常的提示内容呢我们从哪找我们从accountaccount erroraccount error扣到里边呢我们找一个合适的这应该是什么呀用户不存在是吧这里边有用户不存在吗那就是用户未注册呗就是这个一个意思未注册就是不存在嘛是不是提示这个信息就OK了我们就可以跑异常那当然呢也有可能什么呀
[13:04] 那根据用户名呢我们查出来查出来之后接下来要做什么事我是不是得比对一下你的密码是不是正确对不对这个密码咋比对啊这个密码要想比对的话我们得通过工具类了因为我们前面给大家说过嘛这个密码是不是经过加密的它不是说这个原始的那个密码我们直接一比对就完事了它不是这么一回事
[13:33] 所以说呢加密呢我们是通过工具类来加密的那么现在比对密码呢我们也得通过什么呀工具类进行比对那我们还得找一找那个工具类啊那个工具类大家还有印象吗是不是叫password youtube吧password对就是他password youtube他里边呢有一个方法叫verify去看所以就是这个方法那大家看一下这个方法有几个参数啊对两个参数第一个参数就是原始密码
[14:06] 或者说呢第一个参数就是前端页面提交过来的密码第二个参数呢对第二个参数就是表里边那个密码就是正确的密码所以我们应该调用一下这个方法第一个参数呢就是DTO里边的传过来的那个密码第二个参数就是谁里边的啊Conda里边就是咱查出来的这个密码这个大家能看懂吗我现在不就是要拿着
[14:37] 前端页面传过来的密码跟正确的密码做什么呀做比对嘛由于他们是这个这是加密后的嘛对不对所以你要比对得通过人家这个工具类去比对就OK了这是需要大家注意的那我们这是不是得结合什么呀是不是得结合一幅判断是不是所以说我们这需要把一幅给他加上我们写上一幅把整个这一块呢全给他包起来
[15:12] 如果这个方法反而出的话就表示什么所以表示密码是正确的啊你要是正确的话那咱怎么着啊你看按照这个方法设计我们是不是要返回一个dt对象这个dt对象将来是要呃响应到前面页面上对不对这里边包含有一些信息那这个dt对象我们现在是不是还不存在呢那怎么办那这个dt对象是这样你不能自己6啊你自己6一个的话它里边的属性值是不是都是空的对不对
[15:40] 所以说我们应该把查出来的这个我看看对象他的使用值是不是给谁啊给这个地球啊我们应该这么做那这是不是又涉及到这个一个转换是吧这个能用吗能用吧这还就调他就行了这咱以前用过那我们就在就在哪啊就在这呗我可看他地球我看到地球等于我们调一下这个方法把刚才查出来的
[16:15] 这个看到对象扔进去啊然后呢我们就直接把它作为返回值在这就进行什么呀返回就行了对密码正确我就直接把这个对象给返回了那当然有可能最终会出现什么问题啊密码是什么呀不正确的那密码不正确呢密码不正确的话它是不是继续往后走了吗对不对你看这是正确才能进来那不正确继续往下走不正确呢往后还走着还有啥意义啊所以说如果
[16:50] 衣服没有成功执行他就往下走了就证明是密码错密码错过这还是跑一场还是跑一场这个异常就是应该是密码错过对不对啊看的error code来看这里边有没有有没有什么呀有没有哎105吧对啊用后面换密码错就用这个我们把这个信息作为返回值给他干什么呀返回来就行了这不是不是return啊是抛抛一个异常
[17:26] 不是return然后你看这就是咱们传统的这个登录的实验方式咱整体过一遍啊呃我们是先根据用户名进行查询对不对那由于呢又分C端和B端用户所以说我们这儿加了一个if elseC端用户呢他的用户名就是手机号B端用户呢用户名就是账号然后各查各的就行了呃查完之后如果这个用户名都不存在那直接就跑一场了就这个用户为注册对不对那如果用户名存在的话我们接下来还要比对他们的什么呀
[17:56] 密码如果密码也正确了我就把这个对象返回了如果密码不正确我接下来就要抛什么抛异常这是咱目前写的这个要逻辑但这里边还缺一个细节缺什么细节大家看一下这看一下这个登录界面我们本身实现的这个登录功能是完全可以通过什么就进行登录这是一个验证码对不对这是密码吗不是这是验证码
[18:24] 那你说我填一个手机号点击发送然后我手机上得到一个验证码我验证码往这一填是不是点登录就能正常登录了对不对需要密码不需要那么什么时候需要做这个密码的交易呢我们前面说过如果你把短信验证码这个功能给干什么关闭了我们是我们是排还需要通过这个什么密码进行登录因此呢你这里边得判断这种情况呀
[18:49] 而且你是得先判断这种情况对不对如果它是通过验证码登录的话那你还用管这个事吗就是比对密码这个事吗大家想一下用没有对不用了啊不用了所以说呢你在比对密码这个衣服之前应该先做这个判断做什么判断呢就是你有没有或者你现在是不是在使用验证码进行登录咱看前面这个地方这个配置你还有印象吗
[19:20] 这个值如果为处就表示开启了什么呀短信验证码登录否则的话就表示就是密码登录是不是所以我在这需要做这个判断啊我在哪呢对在这如果它为处是证明什么呀对如果它为处是证明来我在这把注释写上如果为处表示采用短信验证码登录
[19:58] 然后呢无需比叫什么呀密码所以如果你是短线验证码登录的话上面只要查诶账户是存在的那直接我们就可以干什么呀对return这个DTO对象对没错这就完事了啊所以说这个业务逻辑你千万不要忘要不然将来你会发现你短线验证码这种登录方式你登不了所以你看啊上面先查用户名是不存在存在的话我得判断
[20:28] 如果你是短信验证码登录的话那直接就返回了只要你的验证码听的没问题你就可以登录那如果说它是false就证明了它采用的是密码登录方式那既然来就比对密码对不对如果密码不对就干什么呀跑一场这个样子的话咱们这个传统的这种登录方式的这个代码咱基本上就写完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示在 IntelliJ IDEA 中为一个账户服务编写登录功能的 Java 代码，包括根据用户类型（手机号或用户名）查询账户、验证密码并返回账户 DTO。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示项目结构，选中 `AccountServiceImpl.java` 文件，准备编写代码。
画面 2: 在 `AccountServiceImpl.java` 中，弹出“选择要实现的方法”窗口，显示 `AccountService` 接口的抽象方法列表。
画面 3: 在 `AccountServiceImpl.java` 中，光标位于 `if` 语句后，准备编写逻辑。
画面 4: 在 `AccountServiceImpl.java` 中，光标位于 `else` 语句后，准备编写逻辑。
画面 5: 在 `AccountServiceImpl.java` 中，光标位于 `private Account getAccountByMobile(String mobile)` 方法的 `getOne` 调用处。
画面 6: 在 `AccountServiceImpl.java` 中，光标位于 `private AccountDTO convertAccountEntityToDTO(Account entity)` 方法的 `if (entity == null)` 语句后。
画面 7: 在 `AccountServiceImpl.java` 中，光标位于 `Account` 类的 `getDomain()` 方法上，显示方法列表。
画面 8: 在 `AccountServiceImpl.java` 中，光标位于 `throw new` 语句后，准备输入异常类。
画面 9: 在 `AccountServiceImpl.java` 中，光标位于 `throw new BusinessException(AccountErrorCode.E_130104);` 语句后。
画面 10: 在 `AccountServiceImpl.java` 中，光标位于 `if (PasswordUtil.verify(...))` 语句后。
画面 11: 在 `AccountServiceImpl.java` 中，光标位于 `return accountDTO;` 语句后。
画面 12: 在 `AccountServiceImpl.java` 中，光标位于 `if (smsEnable)` 语句后。
画面 13: 在 `AccountServiceImpl.java` 中，光标位于 `throw new BusinessException(AccountErrorCode.E_130101);` 语句后。
画面 14: 在 `AccountServiceImpl.java` 中，光标位于 `return convertAccountEntityToDTO(account);` 语句后。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
import cn.icast.wanning2p.account.AccountService;
import com.baomidou.mybatisplus.extension.Service.impl.ServiceImpl;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;
import cn.icast.wanning2p.account.Service.AccountService;
import cn.icast.wanning2p.account.Mapper.AccountMapper;
import cn.icast.wanning2p.account.entity.Account;

