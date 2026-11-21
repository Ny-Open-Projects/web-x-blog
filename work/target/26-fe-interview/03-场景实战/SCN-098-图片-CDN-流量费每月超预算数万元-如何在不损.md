---
title: [SCN-098] 图片 CDN 流量费每月超预算数万元，如何在不损体验的前提下降本？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-098：图片 CDN 流量费每月超预算数万元，如何在不损体验的前提下降本？
**答**：
- 流量 = 字节数，从四个维度降：格式（WebP/AVIF 按 Accept 协商，省 30-60%）、尺寸（按展示宽度请求裁剪图，禁止原图直出——原图常是展示尺寸的 4 倍大）、加载（懒加载 + 进视口才请求 + 占位防抖动）、缓存（长 max-age + immutable，回源率压到个位数）。
- 统一封装图片 URL 生成函数，全站收敛出口，杜绝业务方直拼原图 URL。
- 建立按域名/路径的流量日报，异常大图与异常路径报警，防止降本成果回潮。

```javascript
// 图片降本：格式协商 + 宽度裁剪 + 懒加载统一封装
function cdnImg(url, { width, quality = 75 } = {}) {
  const u = new URL(url, location.origin);
  u.host = 'img-cdn.example.com';
  // 按展示宽度 x DPR 请求裁剪图，杜绝原图直出
  u.searchParams.set('w', String(width * devicePixelRatio));
  u.searchParams.set('q', String(quality));
  // 格式协商交给 CDN：按 Accept 头自动下发 AVIF/WebP/JPEG
  return u.toString();
}

// 组件层：进视口才请求 + 宽高占位防抖动
function LazyImage({ src, width, height, alt }) {
  const ref = useRef(null);
  const [visible, setVisible] = useState(false);
  useEffect(() => {
    const ob = new IntersectionObserver(([e]) => {
      if (e.isIntersecting) { setVisible(true); ob.disconnect(); }
    }, { rootMargin: '200px' });                 // 提前 200px 预载
    ob.observe(ref.current);
    return () => ob.disconnect();
  }, []);
  return (
    <div ref={ref} style={{ aspectRatio: `${width}/${height}`, background: '#eee' }}>
      {visible && <img src={cdnImg(src, { width })} alt={alt} loading="lazy" />}
    </div>
  );
}
```
