import { LoadingOutlined, WechatOutlined } from "@ant-design/icons";
import { Modal } from "antd";
import ClassNames from "classnames";
import { useRequest } from "ahooks";
import { useEffect, useMemo, useState } from "react";
import { useStoreAuth } from "../../hooks/useStoreAuth";
import { getWechatLogin, checkScan } from "../../api/wechat-login";

export default function WechatLogin() {
  const [ticket, setTicket] = useState("");
  const [qrcodeUrl, setQrcodeUrl] = useState("");
  const [wechatLoading, setWechatLoging] = useState(false);
  const [activeQrcode, setActiveQrcode] = useState(true);

  const { login } = useStoreAuth();

  /**
   * 获取ticket和二维码地址
   */
  const { run: execWechatLogin, loading: loadingWithWechatLogin } = useRequest(
    getWechatLogin,
    {
      manual: true,
      onSuccess: ({ data }) => {
        setTicket(data.ticket);
        setQrcodeUrl(data.qrcodeUrl);
      },
    }
  );

  /**
   * 轮询接口请求
   */
  const { run: execCheckScan } = useRequest(() => checkScan({ ticket }), {
    manual: true,
    debounceWait: 2000,
    onSuccess: ({ data }) => {
      if (!wechatLoading) return;
      if (!data) {
        execCheckScan();
        return;
      }
      setWechatLoging(false);
      login(data);
    },
  });

  // 微信登录按钮动态样式
  const classNames = useMemo(() => {
    return ClassNames({
      "cursor-wait pointer-events-none opacity-50": wechatLoading,
      "flex items-center justify-center rounded-md text-sm font-medium duration-500 border h-10 px-4 py-2 w-full bg-[#00b32c] text-white hover:bg-green-500 active:text-black mb-2":
        true,
    });
  }, [wechatLoading, loadingWithWechatLogin]);

  // 二维码组件显示隐藏逻辑
  useEffect(() => {
    if (ticket === "") return;

    setWechatLoging(true);
    execCheckScan();

    const timeout = setTimeout(() => {
      setActiveQrcode(false);
    }, 120 * 1000);

    return () => {
      clearTimeout(timeout);
    };
  }, [ticket]);

  // 重新展示二维码
  function refreshQrcode() {
    execWechatLogin();
    setActiveQrcode(true);
  }

  return (
    <>
      <button className={classNames} onClick={execWechatLogin}>
        {wechatLoading && <LoadingOutlined className="mr-2" />}
        <WechatOutlined className="text-2xl mb-1" />
        &nbsp;微信账号登录
      </button>
      <Modal
        open={wechatLoading}
        okButtonProps={{ hidden: true }}
        cancelButtonProps={{ hidden: true }}
        onCancel={() => setWechatLoging(false)}
      >
        <div className="w-full h-full flex flex-col items-center justify-center">
          <div
            onClick={refreshQrcode}
            className="w-[200px] h-[200px] border rounded-xl flex items-center justify-center cursor-pointer"
          >
            {loadingWithWechatLogin ? (
              <LoadingOutlined className="text-8xl" />
            ) : activeQrcode ? (
              <img src={qrcodeUrl} />
            ) : (
              <span className="text-lg text-center">
                二维码已过期
                <br />
                点击重新刷新
              </span>
            )}
          </div>
          <span className="font-mono text-xl mt-5">扫码登录小滴低代码平台</span>
        </div>
      </Modal>
    </>
  );
}
