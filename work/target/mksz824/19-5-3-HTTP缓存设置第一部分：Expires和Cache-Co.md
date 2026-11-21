# 19-5-3-HTTP缓存设置第一部分：Expires和Cache-Co

上节课我们在本地成功安装并配置了 nginx，这节课来看性能优化的另外一个维度：通过对 nginx 一些配置的修改，改变 HTTP 协议的一些返回项，从 HTTP 的传输层面进行优化。介绍的第一个点是 HTTP 缓存。缓存这个词大家一听都比较熟悉，多少知道它的策略，这节课通过实例追根溯源，让你对 HTTP 缓存的理解更上一层楼。我认为它是最简单也是最实用的性能优化策略：请求新资源时不用发送新的请求，而是从本地文件进行读取。

## 准备：去掉干扰的响应头

开始测试之前需要在配置中添加一点东西，因为 nginx 的默认配置会添加两个返回头。刷新页面，点击文件，可以看到有一个 ETag 和 Last-Modified 两个头，这两个属性会扰乱我们的判断，先暂时去掉，下节课再讨论它们对缓存的影响。

在 nginx 的配置文件中添加一系列指令。第一个是 `etag off`；第二个是 add_header，这个指令用来在返回头添加一个自定义 header，要特别注意的是在 http 这个 block 下面添加。我们想把 Last-Modified 去掉，假如你要去掉一个返回头，把它的值设置成空就可以了：

```nginx
etag off;
add_header Last-Modified "";
```

添加完毕后要重启服务，输入 `nginx -s reload` 进行重启。重新访问，发现它还是 memory cache，因为第一次访问后已经把文件 cache 住了。可以点击 disable cache 刷新一次，现在就没有 cache 了；把 disable cache 去掉再刷新一次，可以看到起作用了：response headers 里 ETag 和 Last-Modified 两个 header 都消失了。现在我们获得了一个非常纯净简约的配置。

## Expires

这个页面我已经做了小的修改，只留下一个 HTML 文件和一个比较大的 JS 文件。这两个请求每次刷新返回的都是 200 OK，waterfall 可以提示我们每次都会发送新的请求，根本没有任何缓存。

现在添加第一个缓存头：Expires。它的解释是：响应头包含一个日期和时间，在这个时间以后响应过期。nginx 提供了一个内置模块，让我们快速添加这个指令，叫 ngx_http_headers_module。指令就是 expires，添加对应的时间就能指定过期时间，时间单位可以是 h（小时）、m（分钟）、s（秒）。这里添加一个很短的五秒：

```nginx
expires 5s;
```

重启 nginx 后访问，刷新一下，可以看到它添加了对应的响应头 Expires，返回的是一个 HTTP 日期：当前访问是 20 秒的时间点，过期时间是 25 秒，也就是五秒之后。假如现在已经超过五秒，下次刷新时已经过期，还是会重新发送请求。但假如我们很快地进行刷新，缓存就生效了：状态还是 200 OK，但 size 这一列特别要注意，点击可以看到 from memory cache，几乎瞬间就返回了对应的响应，说明缓存已经生效。

## Chrome 对 HTML 的小 hack

这里我们发现一个神奇的现象：JS 文件可以完美地返回 200 from disk cache，缓存已经生效；但 index.html 并没有按照我们的预想进行缓存。

这其实是 Chrome 浏览器帮我们完成的一个小的 hack：它在请求任何 HTML 文件的时候，都会添加一个对应的 request header。可以看到 expires 它是有的，但 request header 中有一个 Cache-Control: max-age=0。添加完这个以后它会把缓存去掉。这是因为网站的 HTML 文件很可能会经常更新，如果强行缓存掉，很可能会造成问题。

这时候我们就发现了一个新的 header：Cache-Control，这正是接下来要讲的内容。

## Cache-Control

Expires 很好理解，但有一些小瑕疵：它返回的是一个日期，日期来自服务器的时间，而服务器的时间有可能和用户的客户端时间不一致，这时就会引发问题。

为了解决 Expires 的这些弊端，出现了第二个实现缓存的 header，称为 Cache-Control。它是这么描述的：通用消息头字段被用于 HTTP 请求和响应中，特别注意，请求也可以通过指定的指令来实现缓存机制。它是 HTTP 1.1 推出的响应，比 Expires 提供更多的选项和场景。

其中重要的属性就是 max-age。它和 expires 设置一个到期时间不一样，描述的是从这次请求以后多少秒之后该资源被缓存。通俗一点来讲，就是通知浏览器：五秒之内不要烦我，你自己从缓存区取文件刷新就可以了。

我们的 nginx expires 这个指令，可以同时添加 expires 响应头和 Cache-Control 响应头。点击刚才的文件：除了刚才说的 expires，还设置了 Cache-Control: max-age=5，它们代表的过期时间是一致的，是为了适应不同 HTTP 版本的兼容性。Cache-Control 比 expires 有更高的优先级，当设置了 Cache-Control 时，先从 Cache-Control 取对应的值。

## no-store

Cache-Control 还可以添加更多选项。比如 no-store，文档里写的是：缓存不应储存有关客户端请求或服务器响应的任何内容，即不使用任何缓存。用 add_header 添加一个对应的响应头：

```nginx
add_header Cache-Control "no-store";
```

添加完毕后刷新页面，可以看到已经添加了 Cache-Control: no-store，再次刷新还是不会走缓存，而是重新发起一次 HTTP 请求，这就是 Cache-Control 的作用。

## 小结

这节课我们了解了 HTTP 缓存的两个关键 header：expires 和 Cache-Control，它们对于资源在本地的缓存有着至关重要的作用，使用好这两个 header 也是实现 HTTP 缓存的关键。当然还有两个字段没有介绍，就是一开始删除掉的 ETag 和 Last-Modified，下节课了解这两个 header 会起到什么样的作用。
