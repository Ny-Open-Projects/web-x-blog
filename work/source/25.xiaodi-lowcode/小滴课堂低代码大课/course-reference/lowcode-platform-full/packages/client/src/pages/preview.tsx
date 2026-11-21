import { observer } from "mobx-react-lite";
import { useEffect } from "react";
import { FloatButton } from "antd";
import { useNavigate } from "react-router-dom";
import { CaretLeftOutlined } from "@ant-design/icons";
import { generateComponent } from "./Editor/EditorCanvas";
import { useStoreComponents } from "~/hooks";

const PreviewCanvas = observer(() => {
  const { store, getComponentById, localStorageInStore } = useStoreComponents();

  // 从本地或者服务端读取组件信息
  useEffect(() => {
    localStorageInStore();
  }, []);

  return (
    <>
      {store.sortableCompConfig
        .map((id) => getComponentById(id))
        .map((conf) => generateComponent(conf))}
    </>
  );
});

export default function Preview() {
  // 返回编辑页面
  const nav = useNavigate();

  return (
    <div className="w-screen h-screen flex items-center justify-center overflow-hidden bg-[#f1f2f4]">
      <div className="w-[380px] h-[700px] bg-white text-left overflow-y-auto overflow-x-hidden">
        {/* 预览的组件页面 */}
        <PreviewCanvas />
        {/* 返回按钮 */}
        <FloatButton icon={<CaretLeftOutlined />} onClick={() => nav(-1)} />
      </div>
    </div>
  );
}
