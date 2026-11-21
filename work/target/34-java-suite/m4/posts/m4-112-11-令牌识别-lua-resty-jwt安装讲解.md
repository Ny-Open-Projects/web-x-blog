---
title: "OpenResty 令牌识别与抢单实现：lua-resty-jwt 校验、非热点直下单与 Lua 操作 Redis 集群"
date: 2026-11-18
categories: [Java后端进阶全套, M4 六大进阶项目, 千亿级电商秒杀解决方案]
tags: [Java, 项目实战, OpenResty]
---

# OpenResty 令牌识别与抢单实现：lua-resty-jwt 校验、非热点直下单与 Lua 操作 Redis 集群

上一章解决了登录发令牌和热点商品隔离，这一章把抢单链路补完：用户登录后每次请求都携带 JWT 令牌，令牌识别不再穿透到后台，而是前移到 Nginx/OpenResty 层用 Lua 脚本完成；令牌有效后，先判断商品在 Redis 里有没有被隔离成热点，非热点商品直接走订单系统下单（重点控超卖），热点商品把抢单信息发进 Kafka 排队，由订单系统订阅消费。抢购入口本身也在 Lua 层，所以还需要一套 Lua 操作 Redis 集群的工具。

## 先给结论

- 令牌校验前移到 OpenResty：用 lua-resty-jwt 在 Nginx 层解析 JWT，有效才放行抢单，无效直接 401 提示重新登录，比穿透到后台识别快很多倍。
- token.lua 封装成独立模块：判空 → Bearer 格式校验并去前缀 → jwt:verify → 用 verified 属性决定返回 200 还是 401，识别逻辑到处可复用。
- 非热点抢单的坑不止超卖：超卖靠一条带条件的 UPDATE（行锁 + `seckill_num >= count`）解决；抢单中途变热点靠 islock 判断，返回 205 改走排队流程。
- 热点排队防重复：Redis hash 字段自增 increment 返回 1 才真正发 Kafka，大于 1 说明已在排队，无论点多少次只排一次。
- Lua 想查 Redis 集群得装 lua-resty-redis-cluster 插件：拷贝 redis_slot.c 与 rediscluster.lua，gcc 编译出 so，并放开被注释掉的 EXPIRE 指令。
- 再封装一层 rediscluster.lua 工具：init → 写命令 → commit → close 的固定套路，提供 get / setex / hget / hset / hincrby 五个能力。

## 令牌识别前移到 Nginx：安装 lua-resty-jwt 并封装 token.lua

以前的微服务架构里没有 Lua 识别这一层，请求会跳转到后端服务去识别令牌，效率低。现在的流程是：用户登录拿到令牌后访问微服务，每次把令牌携带过去，Nginx 层用 Lua 脚本识别令牌——有效就去抢单，无效直接告诉用户"令牌无效请重新登录"。

先安装 Lua 库 lua-resty-jwt，它负责令牌的生成与校验。用 OPM 安装只需四条命令：

```bash
# 安装仓库管理工具包
yum install yum-utils
# 添加 OpenResty 仓库地址
yum-config-manager --add-repo https://openresty.org/package/centos/openresty.repo
yum install openresty-resty
yum install openresty-opm
# 安装 lua-resty-jwt
opm get skylothar/lua-resty-jwt
```

也可以直接下载库文件，在 nginx.conf 里用 lua_package_path 指定库文件位置。它的 API 就两个：`jwt:verify(密钥, 令牌)` 做校验，`jwt:sign({header, payload})` 做生成，无论哪个都必须带密钥。

识别令牌的地方可能很多，把校验逻辑封装成独立模块 token.lua：

```lua
local jwt = require "resty.jwt"
-- 密钥与后台保持一致，直接从后台拷贝
local secret = "Sp116a005YaNS7605Lmf5q+USL.INSLiK5bCP6ZuF55ge66yR"

local _M = {}

function _M.check(auth_header)
    local response = {}
    -- 1. 令牌为空：未登录
    if auth_header == nil then
        response["code"] = 401
        response["message"] = "请登录"
        return response
    end
    -- 2. 校验 Bearer 格式，并截取后面的令牌
    local token = string.match(auth_header, "Bearer(.+)")
    if token == nil then
        response["code"] = 401
        response["message"] = "令牌无效"
        return response
    end
    -- 3. 用密钥校验令牌
    local jwt_obj = jwt:verify(secret, token)
    if jwt_obj.verified == false then
        response["code"] = 401
        response["message"] = "令牌无效"
        return response
    end
    -- 4. 校验通过，返回解析后的令牌信息
    response["code"] = 200
    response["message"] = "令牌有效"
    response["body"] = jwt_obj
    return response
end

return _M
```

三个关键点：令牌以 `Bearer 空格` 的格式传过来，校验前要去掉这个前缀；校验结果对象上有 verified 属性，等于 true 表示校验成功、false 表示失败；成功时把解析后的明文塞进 body 一起返回。整个模块完全可以抽出去当独立库用。

写个测试脚本验证它可用——只做判断测试，不做别的事：

```lua
-- jwt_check.lua
ngx.header.content_type = "application/json;charset=utf8"
local cjson = require "cjson"
local jwttoken = require "token"
-- 获取请求头中的令牌
local auth_header = ngx.var.http_authorization
-- 调用令牌校验，结果响应给客户端
local result = jwttoken.check(auth_header)
ngx.say(cjson.encode(result))
```

Nginx 里配一个 location 指向这个脚本，重新加载配置后用 Postman 测：请求 `http://192.168.211.137/token`，请求头 `Authorization: Bearer <令牌>`，返回 code 200、message 令牌有效，body 里就是解析出的 username 等明文；故意把令牌写乱或多按一个空格，立刻变 401 令牌无效——校验链路没有问题。

## 抢单分流与非热点下单：一条 UPDATE 控住超卖

抢单入口在 Nginx 层，配置两个 location：

```nginx
# 抢单操作：先经过 Lua 脚本做令牌校验和热点判断
location /lua/order/add {
    content_by_lua_file /usr/local/openresty/nginx/lua/seckill-order-add.lua;
}
# 后端微服务网关
location /api/ {
    proxy_pass http://192.168.0.102:8001;
}
```

完整抢单流程是七步：判断该商品用户是否 24 小时内购买过；购买过则直接提示无法购买；没购买过则判断商品是否热点商品；非热点走非热点抢单流程，热点走热点抢单流程；热点还要判断用户是否已排队，没排过队才进入排队；下单过程交给订单系统，订单系统通过订阅队列读取用户下单信息再下单。

判断热点与否就看 Redis：热点商品隔离后会在 Redis 里有对应信息，没有就是非热点。非热点商品表面上只是减库存、加一条订单，实际有三个必须处理的问题：

1. **超卖**：十个人并发抢只剩一件的商品，很可能下出多个订单；
2. **下单失败回滚**：递减成功后下单失败，库存要回滚，用分布式事务（阿里的 Seata）解决；
3. **中途变热点**：查看时还不是热点，下单的瞬间变成了热点，此时不能再走普通下单，必须改走热点排队流程，否则库存数据会不精准。

超卖用一条 SQL 就能控住，核心是利用数据库行锁：

```java
@Update("update tb_sku set seckill_num = seckill_num - #{count} " +
        "where id = #{id} and seckill_num >= #{count} and islock = 1")
int dcount(@Param("id") String id, @Param("count") Integer count);
```

update 天然具备行锁：你减成功了，别人同时减一定不成功；条件里再要求当前剩余库存大于等于递减数量，库存不足的请求受影响行数直接是 0。最后的 `islock = 1` 是测试阶段补上的——商品一旦被锁定（islock=2，说明已被隔离成热点），就不允许再递减，这个坑在压测时暴露得非常典型，后面细说。

业务层拿到递减结果后要区分失败原因，用自定义状态码表达：

```java
public static final int DECOUNT_OK  = 200; // 库存递减成功
public static final int DECOUNT_NUM = 405; // 库存不足
public static final int DECOUNT_HOT = 205; // 商品是热点商品
public static final int ORDER_QUEUE = 202; // 抢购商品正在排队
public static final int ORDER_OK    = 200; // 抢单成功

public int dcount(String id, Integer count) {
    int dcount = skuMapper.dcount(id, count);
    if (dcount == 0) {                          // 递减失败，分析原因
        Sku sku = skuMapper.selectByPrimaryKey(id);
        if (sku.getSeckillNum() < count) {
            return StatusCode.DECOUNT_NUM;      // 库存不足
        } else if (sku.getIsLock() == 2) {
            return StatusCode.DECOUNT_HOT;      // 已被锁定，变成热点
        }
        return 0;                               // 其他异常，一般是有问题
    }
    return StatusCode.DECOUNT_OK;               // 递减成功
}
```

商品服务控制器按状态码组装响应：200 提示库存递减成功并附带查出的商品信息（下单方要用价格）；405 提示库存不足；205 提示商品已变热点。Feign 接口暴露 `@PutMapping("/dcount/{id}/{count}")` 给订单服务调用。

## 下单落库与热点改道：24 小时限制、Kafka 排队

订单系统先加上 Kafka 配置，生产者和消费者各一份，服务地址指向 kafka-server 的 9092。下单业务 add(order) 的骨架：

```java
@Autowired
private SkuFeign skuFeign;
@Autowired
private KafkaTemplate kafkaTemplate;
@Autowired
private RedisTemplate redisTemplate;

@Override
public int add(Order order) {
    // 1. Feign 调商品服务递减库存，返回 Result<Sku>
    Result<Sku> dcount = skuFeign.dcount(order.getSkuId(), order.getTotalNum());
    if (dcount.getCode() == StatusCode.DECOUNT_OK) {
        // 2. 递减成功，下单：完善订单数据并落库
        Sku sku = dcount.getData();
        order.setId(IdWorker.nextId());
        order.setOrderStatus("0");     // 订单状态：未完成
        order.setPayStatus("0");       // 支付状态：未支付
        order.setConsignStatus("0");   // 发货状态：未发货
        order.setSkuId(sku.getId());
        order.setSkuName(sku.getName());
        order.setPrice(sku.getPrice() * order.getTotalNum());  // 总价 = 单价 × 数量
        orderMapper.insertSelective(order);
        // 3. 记录抢单标识，24 小时内不能再抢该商品
        String userKey = "USER" + order.getUsername() + "_" + order.getSkuId();
        redisTemplate.boundValueOps(userKey).set("", 1, TimeUnit.MINUTES); // 演示给 1 分钟
        return StatusCode.ORDER_OK;
    } else if (dcount.getCode() == StatusCode.DECOUNT_HOT) {
        // 4. 商品变热点：改走排队流程
        String key = "SKU_" + order.getSkuId();
        Long queue = redisTemplate.boundHashOps(key).increment(userKey, 1);
        if (queue == 1) {              // 返回 1 说明是第一次排队，才真正入队
            Map<String, String> queueMap = new HashMap<>();
            queueMap.put("username", order.getUsername());
            queueMap.put("id", order.getSkuId());
            kafkaTemplate.send("new-order", JSON.toJSONString(queueMap));
        }
        return StatusCode.ORDER_QUEUE; // 202：正在排队（排过队也一样响应排队中）
    } else if (dcount.getCode() == StatusCode.DECOUNT_NUM) {
        return StatusCode.DECOUNT_NUM; // 库存不足
    }
    return 0;
}
```

订单表里要完善的字段不少：主键 ID 用 IdWorker 生成；totalNum 是抢购数量，秒杀不限定只能抢一个；订单/支付/发货三个状态初始都是 0；skuId、商品名从递减结果里拿，总价用单价乘以数量；username 不用管，控制层解析令牌时会填进来。

抢单标识就是给"用户+商品"造一个 key 存进 Redis，值随意，key 存在即代表抢过；演示环境过期时间给 1 分钟，真实场景是 24 小时，到期自动恢复抢购，且不影响用户抢别的商品。

变热点后的排队有个防重复设计：热点商品的 Redis hash 里，以 userKey 为字段做 increment。返回 1 表示这是第一次排队，把抢单消息（username + 商品 ID，转成 JSON）发到 Kafka 的 new-order 主题，等于开始排队；返回值大于 1 说明已经排过，不再重复发消息，但仍响应 202——用户还在排队中。订单系统订阅这个主题，根据消息里的商品和用户信息下单。

控制层把令牌解析和状态码分支串起来：

```java
@GetMapping(value = "/{id}")
public Result add(@PathVariable(value = "id") String id,
                  @RequestHeader(value = "Authorization") String authorization) {
    // 解析令牌，拿到用户名
    Map<String, Object> tokenMap = JwtTokenUtil.parseToken(authorization);
    String username = tokenMap.get("username").toString();
    // 封装订单
    Order order = new Order();
    order.setSkuId(id);
    order.setCreateTime(new Date());
    order.setUpdateTime(order.getCreateTime());
    order.setUsername(username);
    int code = orderService.add(order);
    switch (code) {
        case StatusCode.ORDER_OK:
            return new Result(true, StatusCode.ORDER_OK, "下单成功！");
        case StatusCode.DECOUNT_NUM:
            return new Result(false, StatusCode.DECOUNT_NUM, "库存不足！");
        case StatusCode.ORDER_QUEUE:   // 排队不是出错
            return new Result(true, StatusCode.ORDER_QUEUE, "排队抢购中！");
        default:
            return new Result(false, StatusCode.ERROR, "抢单发生异常！");
    }
}
```

全链路测试按三个场景走：正常抢单能拿到订单，重复抢也返回成功——24 小时限制不在这层控制，而是等 Lua 脚本判断，但 Redis 里的标识确实生成了，还能看到倒计时过期；把库存改成 0 再抢，正确返回库存不足；最关键的是"中途变热点"场景。在抢单业务里加一段 Thread.sleep(20000) 制造时间窗口，先用静态页刷新三次让商品 52 变成热点（islock 被置 2），然后发起抢单——请求进来时它还是非热点，睡 20 秒期间被隔离成热点，睡醒后递减。断点调试暴露了一个 bug：锁定商品竟然递减成功了，返回 200。原因就是 DAO 里缺 `islock = 1` 条件，补上后重启再测：递减失败返回 205，业务层改走排队，响应"排队抢购中"，Redis 里 SKU_52 的 hash 出现用户排队记录，值从 1 开始；无论再点多少次，只响应排队中、计数递增，消息只发一次。

## Lua 操作 Redis 集群：插件编译与工具封装

抢购入口在 Lua 层，判断热点、防重复抢单都要查 Redis，而环境是 Redis 集群，普通单机连接方式不够用，需要安装集群插件 lua-resty-redis-cluster。

安装步骤：下载插件压缩包上传到服务器，解压出 lua-resty-redis-cluster-master，lib 目录下有两个关键文件 redis_slot.c 和 rediscluster.lua。把两个文件都拷到 OpenResty 的 lua lib 目录，再编译 C 文件：

```bash
cp redis_slot.c /usr/local/openresty/lua/lib/
cp rediscluster.lua /usr/local/openresty/lua/lib/
gcc redis_slot.c -fPIC -shared -o libredis_slot.so
```

编译报 lua.h 不存在的错，是 Lua 版本/依赖问题：要么删掉自带 Lua 版本，要么装 lua-devel，然后重新执行编译。装完还要改 rediscluster.lua：它的指令清单里有 HMGET（哈希查询）、HMSET（哈希添加）、GET（普通类型查询），但过期指令 EXPIRE 被注释掉了，把注释去掉，让它支持设置过期时间——抢购标识依赖过期机制，这条必须放开。

使用套路是固定的五段式：创建连接对象 → init 初始化 → 编写要执行的命令（此时并没有执行）→ commit 提交指令才真正执行 → close 关闭连接。把它封装成工具模块：

```lua
local rediscluster = require "resty.rediscluster"

-- Redis 集群连接配置
local config = {
    name = "test",
    serv_list = {
        { ip = "192.168.211.137", port = 7001 },
        { ip = "192.168.211.137", port = 7002 },
        { ip = "192.168.211.137", port = 7003 },
        { ip = "192.168.211.137", port = 7004 },
        { ip = "192.168.211.137", port = 7005 },
        { ip = "192.168.211.137", port = 7006 }
    }
}

local _M = {}

-- 根据 key 查询字符串
function _M.get(key)
    local red_c = rediscluster:new(config)
    red_c:init()
    red_c:rget(key)                 -- 只是编写命令，尚未执行
    local result = red_c:commit()   -- 提交指令后才真正执行，返回结果集
    red_c:close()
    return result
end

-- 添加字符串并设置过期时间
function _M.setexp(key, value, time)
    local red_c = rediscluster:new(config)
    red_c:init()
    red_c:set(key, value)
    red_c:expire(key, time)         -- 过期指令，靠前面放开的注释才可用
    red_c:commit()                  -- 这次执行没有结果集返回
    red_c:close()
end

-- 根据两层 key 查询哈希数据
function _M.hget(key1, key2)
    local red_c = rediscluster:new(config)
    red_c:init()
    red_c:hmget(key1, key2)
    local result = red_c:commit()
    red_c:close()
    return result[1]                -- 返回的是集合，这里只需要一条记录
end

-- 向哈希添加数据
function _M.hset(key1, key2, value)
    local red_c = rediscluster:new(config)
    red_c:init()
    red_c:hmset(key1, key2, value)
    red_c:commit()
    red_c:close()
end

-- 哈希字段自增
function _M.hincrby(key1, key2, num)
    local red_c = rediscluster:new(config)
    red_c:init()
    red_c:hincrby(key1, key2, num)
    local result = red_c:commit()
    red_c:close()
    return result
end

return _M
```

五个方法覆盖了抢单脚本需要的全部操作：get 查用户标识判断 24 小时内是否抢过；hget 查 SKU_商品ID 判断是否热点；setexp 写抢购/排队相关标识并带过期；hset 写哈希数据；hincrby 做排队计数。有了这套工具，下一节就可以在 Lua 层写出完整的抢单脚本。

## 小结

- 令牌识别从后台搬到 OpenResty：lua-resty-jwt 的 verify/sign 加上自封装的 token.lua，判空、去 Bearer 前缀、verified 判定，Postman 一把验证通过。
- 非热点抢单的本质是"带条件的 UPDATE"：行锁 + seckill_num >= count 控超卖，islock = 1 挡住已变热点的商品，失败原因用 405/205 状态码区分。
- 下单链路三件事：订单落库（IdWorker 主键、三个初始状态、总价）、USER+用户名+商品ID 的 24 小时抢单标识、变热点后 increment 计数防重复排队并只发一次 Kafka。
- Redis 集群的 Lua 操作靠 lua-resty-redis-cluster：拷文件、gcc 编译、放开 EXPIRE 注释，再封装成 init→命令→commit→close 套路的工具模块，五个方法直接服务抢单脚本。
- 测试是这套设计的试金石：中途变热点场景靠 sleep 制造时间窗口，直接暴露了"锁定商品仍可递减"的 bug，也验证了只排一次队的约束。
