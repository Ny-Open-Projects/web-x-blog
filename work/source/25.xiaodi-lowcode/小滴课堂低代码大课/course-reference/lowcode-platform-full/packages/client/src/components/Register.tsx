import { useTitle } from "ahooks";
import RegisterOption from "./Register/RegisterOption";
import WechatLogin from "./Login/WechatLogin";

interface IRegisterProps {
  changeState: () => void; // 切换弹窗
}

export default function Register(props: IRegisterProps) {
  useTitle("小滴低代码平台 - 注册");
  return (
    <div className="h-full flex items-center justify-center">
      <div className="w-[368px] rounded-lg shadow-lg bg-white p-6 space-y-2 border-gray-200">
        <div className="space-y-2 px-12 text-center">
          <span className="font-bold cursor-pointer">快速注册</span>
        </div>

        {/* 注册输入框 */}
        <RegisterOption />

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
            已有账号？
            <span
              onClick={props.changeState}
              className="text-blue-500 cursor-pointer"
            >
              去登录
            </span>
          </span>
        </div>
      </div>
    </div>
  );
}
