import { createStoreAuth } from "../store";
import { computed, action } from "mobx";
import { useNavigate } from "react-router-dom";

export const storeAuth = createStoreAuth();
export function useStoreAuth() {
  const nav = useNavigate();
  // 判断是否登录，创建可响应的计算属性的函数
  const isLogin = computed(() => !!storeAuth.token);

  // 登录
  const login = action(async (token: string) => {
    storeAuth.token = `Bearer ${token}`;
    localStorage.setItem("token", storeAuth.token);
    nav("/editor");
  });
  return { login, isLogin };
}
