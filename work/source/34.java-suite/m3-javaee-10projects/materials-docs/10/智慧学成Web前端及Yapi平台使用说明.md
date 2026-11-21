# 智慧学成Web前端及Yapi平台使用说明

- 来源：10.阶段十 万信金融项目\JavaEE中级进修课资料（新版）\08.基于大数据的智慧学成项目课程\day03\资料\第3章-课程分析\文档\智慧学成Web前端及Yapi平台使用说明【海量资源尽在 666java.com】.pdf
- 页数：10
- 抽取：pypdf 文本层



<!-- page 1 -->
Yapi 平台  
yapi 平台是为智慧学成 Web 前端原型提供 mock 模拟数据 , 以便展⽰  !
1. 源码  
源码位置 :
使⽤需要解压到指定位置, 例如 : ~/work/xuecheng ⽬录下  !
PS: 源码解压需要和你的 docker 在同⼀服务器上 , 这样容器编排时才能使⽤
 
2. docker-compose.yml 配置  
项⽬使⽤了 docker-compose 编排 , 所有容器相关的配置都在 docker-compose.yml 中 , 在 docker-
compose.yml 从 160 ⾏开始是  xc-online-yapi ( mock 模拟数据  ) 的容器配置 , 你在使⽤过程中需要指定
源码位置, 需要修改 volumes 变量映射即可 , 其他配置⽆需要改动, 如下图所⽰ :
 
3. 启动  
在 docker-compose.yml ⽂件所在⽬录执⾏启动命令即可 , 启动命令如下 :
 
4. 访问  
容器默认映射 3000 端⼝ , 使⽤ : 服务器 ip:3000 即可访问 , 但不建议 , 建议的⽅式是 hosts 配置域名映射 , 使
⽤域名访问 , 我的服务器 ip 是 : 172.16.0.165, 映射域名为 : xc-online, hosts 末尾添加如下配置 :
.
└──  授课资料
    └──  第 3 章 - 课程分析
        └──  code
            └──  yapi.zip
# -d 是后台启动 , 如果不加 , 关闭终端 , 容器⼀同关闭
docker-compose up -d xc-online-yapi
172.16.0.165    xc-online

<!-- page 2 -->
访问地址为 : http://xc-online:3000, 效果如下图 :
 
PS: 默认⽤⼾名 : admin@admin.com 密码 : ymfe.org
 
5. 创建项⽬ & 导⼊接⼝数据  
登陆系统后你会发现 , 上⾯什么都没有 , 这个时候需要咱们添加⼀个项⽬并导⼊ api 数据
5.1 添加项⽬

<!-- page 3 -->
1. ⾸先点击右上⻆添加项⽬ : 
2. 填写项⽬基本信息 , 并创建 , 如下图所⽰ : 
点击创建项⽬ , 项⽬就创建成功了  !
5.2 导⼊接⼝数据  
项⽬创建项⽬按钮后 , 会⾃动跳转到项⽬⻚⾯ , 如下图所⽰ :

<!-- page 4 -->
导⼊数据步骤如下 :
1. 点击菜单栏的数据管理 :

<!-- page 5 -->
2. 在左侧数据导⼊的下拉列表选择 json:
3. 点击上传区域在弹出窗⼝选择 json 接⼝⽂件 : 
接⼝⽂件路径如下 :

<!-- page 6 -->
4. 上传成功后点击菜单栏接⼝按钮查看 , 结果如下图所⽰ : 
 
 
 
智慧学成 Web 前端  
智慧学成前端是⼤数据分析结果的展⽰ , 前端使⽤ VUE 开发 , 这⾥已在 docker 容器中配置好环境 , 启动
docker 时指定源码路径即可 !
1. 源码  
源码位置 :
使⽤需要解压到指定位置, 例如 : ~/work/xuecheng ⽬录下  !
PS: 源码解压需要和你的 docker 在同⼀服务器上 , 这样容器编排时才能使⽤
 
2. docker-compose.yml 配置  
.
└──  授课资料
    └──  第 3 章 - 课程分析
        └──  code
            └──  智慧学成 api.json
.
└──  授课资料
    └──  第 3 章 - 课程分析
        └──  code
            └──  xuecheng-online-vue.zip

<!-- page 7 -->
项⽬使⽤了 docker-compose 编排 , 所有容器相关的配置都在 docker-compose.yml 中 , 在 docker-
compose.yml 从 147 ⾏开始是  xc-online-vue ( 智慧学成 Web 前端  ) 的容器配置 , 你在使⽤过程中需要指
定源码位置, 需要修改 volumes 变量映射即可 , 其他配置⽆需要改动, 如下图所⽰ :
⼀定配置正确 , 不然 web 前端⽆法使⽤
 
3. 启动  
在 docker-compose.yml ⽂件所在⽬录执⾏启动命令即可 , 启动命令如下 :
 
4. 访问  
容器默认映射 4000 端⼝ , 使⽤ : 服务器 ip:4000 即可访问 , 但不建议 , 建议的⽅式是 hosts 配置域名映射 , 使
⽤域名访问 , 我的服务器 ip 是 : 172.16.0.165, 映射域名为 : xc-online, hosts 末尾添加如下配置 :
访问地址为 : http://xc-online:4000, 效果如下图 :
# -d 是后台启动 , 如果不加 , 关闭终端 , 容器⼀同关闭
# 注意此默认容器依赖 xc-online-yapi, 启动前需要确认已配置完成 , 后期数据落地 , 可去掉 xc-
online-yapi 的依赖 , 配置详情看后台的 :  源码配置说明
docker-compose up -d xc-online-vue
172.16.0.165    xc-online

<!-- page 8 -->
PS: ⽤⼾名 , 密码 , 验证码任意 , 但必须输⼊
登陆后 , ⻚⾯展⽰如下 :
 
 
5. 源码配置说明

<!-- page 9 -->
5.1 配置说明  
源码的配置⽂件是根⽬录的 : vue.conﬁg.js , 可配置项⽬看下图
 
5.2 docker yapi 平台 , mock 接⼝查看⽅式  
使⽤ docker yapi 接⼝时 , 接⼝地址查看⽅式如下 :
1, 登陆 docker yapi 平台点击设置
2, 在⻚⾯中间位置有接⼝地址 , 如下图所⽰ : 
PS: 使⽤ docker yapi ⽅式时 , 需要注意你的 MOCK 地址是否填正确  !

<!-- page 10 -->
配置修改后不能⽴即⽣效 , 需要重启容器命令如下  :
 
# 1, 停⽌
docker-compose stop xc-online-vue
# 2, 启动
docker-compose up -d xc-online-vue
