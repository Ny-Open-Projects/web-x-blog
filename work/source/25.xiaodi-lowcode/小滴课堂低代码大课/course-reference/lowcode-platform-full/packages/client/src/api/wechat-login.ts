import request from "../utils/request";

// 获取微信二维码
export async function getWechatLogin() {
  return request("/wechat_login/login");
}

// 轮询用户是否扫码授权登录
export async function checkScan(params: { ticket: string }) {
  return request("/wechat_login/check_scan", { params });
}
