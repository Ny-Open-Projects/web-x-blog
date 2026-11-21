---
title: [FRP-188] 手写 react-router mini：history 监听 + 路径匹配 + useParams？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-188：手写 react-router mini：history 监听 + 路径匹配 + useParams？

**答**：
- 三层结构：**history 层**（包装 pushState/popstate，提供订阅）、**match 层**（路径模式 `/user/:id` 编译为正则，提取 params）、**React 绑定层**（Router context + useParams/useNavigate hooks）。
- popstate 只在浏览器导航（前进/后退）触发，`pushState/replaceState` **不触发任何事件**——所以 push 后要手动通知订阅者。
- 匹配：`/user/:id` → 正则 `^\/user\/([^\/]+)$` + keys=['id']；match 返回 `{ params, pathname }`。
- 嵌套路由的 Outlet 用 context 传递"当前匹配的剩余层级"，mini 版只实现单层。

```javascript
// 简化实现，帮助理解 react-router mini
// —— 1. history 层 ——
function createHistory() {
  const listeners = new Set();
  let current = { pathname: location.pathname, search: location.search };

  function notify() {
    current = { pathname: location.pathname, search: location.search };
    listeners.forEach(fn => fn(current));
  }
  window.addEventListener('popstate', notify);   // 只有浏览器导航触发！

  return {
    get location() { return current; },
    listen(fn) { listeners.add(fn); return () => listeners.delete(fn); },
    push(to) {
      history.pushState({}, '', to);
      notify();                                   // pushState 不触发 popstate：手动通知
    },
    replace(to) {
      history.replaceState({}, '', to);
      notify();
    },
  };
}

// —— 2. match 层：路径模式 -> 正则 ——
function compilePath(pattern) {
  const keys = [];
  const source = pattern
    .replace(/\/:([^\/]+)/g, (_, key) => {       // /:id -> 捕获组
      keys.push(key);
      return '/([^\\/]+)';
    })
    .replace(/\/*/g, '\\/*');                    // 尾斜杠宽容
  return { regex: new RegExp(`^${source}$`), keys };
}

function matchPath(pattern, pathname) {
  const { regex, keys } = compilePath(pattern);
  const m = pathname.match(regex);
  if (!m) return null;
  const params = {};
  keys.forEach((key, i) => (params[key] = decodeURIComponent(m[i + 1])));
  return { pattern, params, pathname };          // useParams 的数据源
}

// —— 3. React 绑定层 ——
const RouterContext = React.createContext(null);

function Router({ children, history = createHistory() }) {
  const [location, setLocation] = useState(history.location);
  useEffect(() => history.listen(setLocation), [history]);   // 订阅：导航 -> 重渲染
  return (
    <RouterContext.Provider value={{ location, history }}>
      {children}
    </RouterContext.Provider>
  );
}

function Route({ path, element }) {
  const { location } = useContext(RouterContext);
  const match = matchPath(path, location.pathname);
  return match
    ? <MatchContext.Provider value={match}>{element}</MatchContext.Provider>
    : null;
}

function useParams() {
  return useContext(MatchContext)?.params ?? {};   // 从最近 match 读 params
}
function useNavigate() {
  const { history } = useContext(RouterContext);
  return (to, { replace } = {}) => replace ? history.replace(to) : history.push(to);
}

// 使用：
// <Router><Route path="/user/:id" element={<User />} /></Router>
// User 组件内 const { id } = useParams();  navigate('/user/2') -> popstate 链路或手动 notify -> 重渲染
```
