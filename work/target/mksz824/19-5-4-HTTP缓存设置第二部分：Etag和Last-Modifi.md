# 19-5-4-HTTP缓存设置第二部分：Etag和Last-Modifi

上节课介绍了 HTTP 缓存的两个重要 header：一个是 expires，比较简单，就是一个过期时间；另一个是 HTTP 1.1 推出的 Cache-Control，可以添加比 expires 更高级的缓存控制。这两个头作用非常相似：当命中缓存时不会发起任何 HTTP 请求，直接显示 200 from disk cache，从本地获取文件的缓存。

这节课继续介绍一开始删除的两个另辟蹊径的 HTTP 头：ETag 和 Last-Modified。通过这两个 header，服务器可以智能地为我们返回资源是否变化的信息，让浏览器更智能地根据文件是否变化利用缓存。这两个标签其实非常类似，只不过一个指示的是文件内容是否变化，另一个是文件的最后修改时间。

## 打开 ETag

直接用 nginx 来讲解。首先把之前添加的和缓存相关的 expires 都删除掉，先不让任何缓存影响我们的判断和操作；把 etag 改成 on（或者注释掉，因为一开始它就是 on 的）。文档里可以看到 etag 也是一个核心指令：etag on 或 off，可以给静态资源的 response header 添加 ETag。保存之后用 `nginx -s reload` 重启服务器。

刷新页面观察对应的 HTTP 请求。这里我使用 Firefox，因为 Chrome 在 localhost 下测试这两个字段会有一点问题。

## 第一次访问与第二次访问

第一次访问时，disable cache 以后刷新，请求的资源返回 200，肯定没问题。注意它的 response header 会添加两个头：一个是 ETag，带着一串类似哈希的标识符，这是和文件相对应的标识值，文件不变化这个值就不变化；第二个是 Last-Modified，带的是我们之前见过的 HTTP 时间，指代文件的最后修改时间。

现在是第二次访问，再次刷新，可以看到它已经不一样了。首先 status 是 304。然后看 request header：它会根据上次访问带着两个特殊的头部。第一个叫 If-None-Match，和 ETag 对应，它的值和服务器返回的值完全相同（都是 70d4c），它会询问服务器该版本是否仍然可用。服务器发现该版本是最新的、没有变化，就返回 304 Not Modified，浏览器继续使用缓存，省下了下载资源的时间。

这里注意区别：之前的 Cache-Control 直接返回 200 from disk cache，连请求都不会发送；而现在还是要发送一次询问请求，只是不重新下载资源。

If-Modified-Since 跟 If-None-Match 是一个意思，只不过它对应的是 Last-Modified，也会带上最后修改的时间，两个值完全相似，最后返回 304 Not Modified，指引你使用缓存。

## 文件修改后的行为

修改一下对应的文件，把它改成 hello 3，做一点小小的修改，然后再刷新。发现现在这个文件返回的是 200。为什么？原因是现在不匹配了：request header 带的是 70d4c，发送了一次询问请求，服务器返回的 ETag 后面一样但前面已经不一样了，说明文件做过修改。这时就不会返回 304 Not Modified 了，直接返回 200，让你重新下载。这就是整个流程。

## 缓存知识结构图

通过这个例子，我们来看一张图梳理这两节课的 HTTP 缓存知识结构。图是自上往下的：

1. 200 状态（from cache）：直接从本地缓存取，不发送请求。它由 expires 和 Cache-Control 控制。expires 是一个绝对时间（HTTP 时间），Cache-Control 是一个 max-age（相对时间），它的优先级比 expires 高，因为它是 HTTP 1.1 新推出的。假如访问在这个时间内，浏览器就不会发送新的请求，直接使用对应的缓存，非常快。
2. 304 状态：由 ETag 或 Last-Modified 控制。第一次请求时服务器返回 ETag 和 Last-Modified 两个值；再次请求时浏览器会带着两个特定的 request header，If-None-Match 和 If-Modified-Since。假如匹配，服务器直接返回 304（Not Modified），指引浏览器可以直接使用缓存。
3. 200 状态（重新下载）：假如没有上述 header，或者缓存已经过期，或者 ETag 和 Last-Modified 不匹配（说明文件进行了修改），浏览器就会直接去服务器下载最新的文件，发送一次新的请求，返回 200 状态。

这是一个比较重要的知识点，前端面试经常会考，请同学们再理解一下。合理利用 HTTP 缓存是比较简单但非常重要的加快资源加载的手段，掌握它也是一项必备的技能。
