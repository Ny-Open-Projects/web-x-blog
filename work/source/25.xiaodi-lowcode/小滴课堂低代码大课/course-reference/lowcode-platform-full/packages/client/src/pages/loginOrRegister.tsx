import { useState } from "react";
import Register from "../components/Register";
import Login from "../components/Login";

export default function LoginOrRegister() {
  // 切换弹窗逻辑
  const [loginOrRegister, setLoginOrRegister] = useState(true);
  const changeState = () => {
    setLoginOrRegister(!loginOrRegister);
  };

  return (
    <div className="h-full bg-[url('/bg.jpg')] bg-repeat bg-cover">
      {loginOrRegister ? (
        <Register changeState={changeState}></Register>
      ) : (
        <Login changeState={changeState}></Login>
      )}
    </div>
  );
}
