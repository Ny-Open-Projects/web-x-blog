# 声音线转写：18_后端通用封装-通用Controller

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day06-黑马头条-通用后端
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day06-黑马头条-通用后端\18_后端通用封装-通用Controller【海量资源尽在 666java.com】.mp4
- 时长：4分8秒（音频 249s）
- 转写：faster-whisper-large-v3 / 语言 zh / 8 段
- 生成时间：2026-10-28 11:44:15

## 逐段转写（教师原声）

[00:00] 好下面呢咱们就来去说一下当前那个通用的Controller的编写啊那这个呢其实也比较简单了啊那咱们就在这直接去写了啊呃打开当前的admin端然后在这去创建一个Controller在这去创建一个类这个类呢叫common Controller然后呢写上之后呢咱们在这啊去加上一些东西叫request mapping rest Controller啊好是request mapping
[00:31] 好的这个路径咱们还是按照之前的路径一样写API是吧然后是v1然后是admin然后下面是common好吧行下面咱们就可以去注入当前咱们写通用的serviceprivatecommon Service好common Service注入一下注入进来之后咱们在这就可以去写方法了首先咱们是要去写三个方法就可以
[01:01] 好吧三个三个方法啊第一个呢是public response result现在是listlist里边咱们可以去设置很多是吧你是哪种方式比如说你要是统计啊还是说按条件查询呢还是没条件啊咱们都可以在这去设置需要看你的参数是啥request body这里边有个common dtodto好完事啊那这在这你就可以直接干嘛呢直接去订当前的common
[01:31] Service.list把DTO装进去在上面咱们也可以去带一个Boss mapping这里边咱们可以设置一个叫list好吧叫list行那这个就算是完了然后下面还有还有两个方法是吧咱们再进一下public什么 response result是叫update然后这里边还是commentDTO
[02:01] 然我在前面你还要再去加什么东西一个requestreqrequest body然后调用Service直接加就可以了直接调用就可以了return common Service.update当然这个update咱们也知道这边它其实具有两种功能是吧一个啥呢一个是新增二个是修改是吧也是根据你反正过来到一个model来去区分也是新增和修改
[02:32] 这个怎么叫update好吧主要是根据当前的参数区分可以是新增或修改还有最后一个是吧叫public response result然后是delete然后这里边其实就跟应该是最简单的一个request body然后还是当前什么common-dtl好dtl最终的你在这去丢就可以了return什么return当前的common-Service.delete
[03:03] DTO好吧在这啊加上PostPostMapping这是叫Delete诶?
[03:12] 找个坏了Delete这个的话咱们就算是做完了啊做完之后呢咱们一会儿啊就可以去基层前端来去测一下刚才我说的那三个功能是吧比如说分别是什么用户列表什么敏感词还有什么频道
[03:32] 咱们这时候看看好用还是不好用是吧那这时候咱们可以去重启一下启动一下当前的项目看看有没有问题好吧直接右键debug收到好正在启动看看有没有报错没有报错就没有问题好这个好像是没有问题他没有报错那这时候咱们通用的comment通用的这种后端的这种接口咱们就说到这里
