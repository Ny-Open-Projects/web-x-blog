# 声音线转写：20_爬虫数据解析保存_文章保存2

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day10-黑马头条-爬虫数据保存
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day10-黑马头条-爬虫数据保存\20_爬虫数据解析保存_文章保存2【海量资源尽在 666java.com】.mp4
- 时长：5分8秒（音频 309s）
- 转写：faster-whisper-large-v3 / 语言 zh / 10 段
- 生成时间：2026-10-28 12:04:52

## 逐段转写（教师原声）

[00:00] 好那咱们就继续完成当前这个toCLnews这个就是比较简单啊来看一下啊CLnews咱们在这去创建一个CLnewsCLnews啊等于等一个CLnews我们只需要把这个从这里边的值啊那这里边就可以了好吧首先咱们来设置啊set一个什么name这个name呢就是classitem中的是吗
[00:28] get author name就是当前的文章的名文章的作者是吧还有clnews.set什么呢label这个label的话呢说错了这个id.setlabel这个labels呢其实呢就是当前的这种标签passitem.getlabels就可以了然后再往下clnews.set当前的comment
[01:01] 这container就是pass.get然后再往下看clnews.set在玩啥呢有一个labelids这个该怎么去做其实咱们之前也是做过一个事咱们之前有一个Service叫adlabel Service咱们在这注入一个private ad
[01:35] label Service把它给注入进来之后咱们再去设置拷贝一下它点咱们有一个getlabel 看到了吗这个串其实就是哪个串刚才那个passitem.getlabels这个串好吧就是通过搜签查询它的ID然后下面还有就是tend id其实咱们也有一个
[02:06] ad label Service.getad这个是谁这个其实就是上面这个字clnews.get前的label ids好中了这个咱们就拿到了拿到完之后这个其实是kinoidkinoid是写成kino一形是吧id形象kinoid
[02:40] 设置完之后呢,咱们就可以去设置了clnews.setTitleId那这个拿到之后咱们往下看,看还有啥clnews.setTitle有吗有有一个passItem.getTitle再往下clnews.setTypeType的话呢咱们就一个什么呢pass
[03:13] 他们点get doc time就是当前的当的类型对吧crnews.setstatus默认给个1我们前面呢去讲转一下这是一个bytebyte然后再往下看啊crnews有一个set create time咱们需要去用一个date出来然后还有吗这里边咱们还要去有一个叫pass
[03:44] 有一个release就是发布时间发布时间啊咱们在这儿去最好是处理一下啊点吧这就是一个release date最好是分担一下当前这个到底是否为空strain utils date is not is not unpaid就是说它不为空不为空啊为空之后呢这时候呢咱们就可以去转换一下转换一下啊
[04:14] 这个咱们主要是从一个String的字幕券转成一个Date就可以了clnews.setAren'tDate这是一个发布时间出示时间这怎么办呢有一个DateUtils.String.put这个就是releaseDate你下面可以给一个格式怎么叫DateUtils.Date
[04:44] Time format最后一个吧Chinese是吧看一下应该是这个东西这个东西行那这个设置完之后最终的你把当前这个CL News返回就可以了那这样的话咱们这个就算是组装成功了
