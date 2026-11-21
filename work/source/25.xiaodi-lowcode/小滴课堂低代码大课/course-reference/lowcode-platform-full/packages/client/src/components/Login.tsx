import { useTitle } from "ahooks";
import { useState } from "react";
import Account from "./Login/Account.tsx";
import Captcha from "./Login/Captcha.tsx";
import WechatLogin from "./Login/WechatLogin";

interface ILoginProps {
  changeState: () => void;
}
export default function Login(props: ILoginProps) {
  useTitle("小滴低代码平台 - 登录");
  const [activeKey, setActiveKey] = useState(1);

  return (
    <div className="h-full flex items-center justify-center">
      <div className="w-[368px] rounded-lg shadow-lg bg-white p-6 space-y-2 border-gray-200">
        <div className="space-y-2 px-12 text-center">
          <span
            onClick={() => setActiveKey(1)}
            className={[
              "mr-[10px] cursor-pointer",
              activeKey ? "font-bold" : "text-[#aaaaaa]",
            ].join(" ")}
          >
            密码登录
          </span>
          <span
            onClick={() => setActiveKey(0)}
            className={[
              !activeKey ? "font-bold" : "text-[#aaaaaa]",
              "cursor-pointer",
            ].join(" ")}
          >
            验证码登录
          </span>
          <p className="text-zinc-500 text-xs">登录后方可体验小滴低代码平台</p>
        </div>

        {/* 账号密码登录输入框 */}
        {!!activeKey && <Account />}

        {/* 手机验证码登录输入框 */}
        {!activeKey && <Captcha />}

        <div className="flex items-center space-x-2">
          <hr className="flex-grow border-zinc-200" />
          <span
            className="text-zinc-400 dark:text-zinc-300 text-sm"
            data-id="14"
          >
            或者
          </span>
          <hr className="flex-grow border-zinc-200" />
        </div>
        {/* 微信登录 */}
        <WechatLogin />
        <div className="text-sm flex justify-center text-[#aaaaaa]">
          <span>
            还没账号？
            <span
              onClick={props.changeState}
              className="text-blue-500 cursor-pointer"
            >
              去注册
            </span>
          </span>
        </div>
      </div>
    </div>
  );
}
