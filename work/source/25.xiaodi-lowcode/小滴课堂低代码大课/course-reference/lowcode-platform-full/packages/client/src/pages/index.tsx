import { useEffect } from "react";
import { useLocation, useNavigate, Outlet } from "react-router-dom";
import { useStoreAuth } from "../hooks";

function Home() {
  const { isLogin } = useStoreAuth();
  const location = useLocation();
  const nav = useNavigate();
  function befoceRouterChange(pathname: string) {
    // 已登录，访问根路径或者登录注册页要跳转到编辑页
    if (isLogin.get())
      ["/", "/login_or_register"].includes(pathname) && nav("/editor");
    // 未登录,访问具有权限页面要跳转到登录注册页
    else pathname !== "/login_or_register" && nav("/login_or_register");
  }

  useEffect(() => {
    befoceRouterChange(location.pathname);
  }, [location.pathname]);

  return <Outlet />;
}
export default Home;
