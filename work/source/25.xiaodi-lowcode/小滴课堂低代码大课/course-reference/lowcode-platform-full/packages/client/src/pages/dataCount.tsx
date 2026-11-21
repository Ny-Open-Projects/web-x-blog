import { Button, message } from "antd";
import { FormOutlined, LineChartOutlined } from "@ant-design/icons";
import { useNavigate } from "react-router-dom";
import { useState } from "react";
import { useRequest } from "ahooks";
import type { IComponent } from "@lowcode/share";
import ComponentDatas from "./DataCount/ComponentDatas";
import { getQuestionComponents } from "~/api/low-code";
import DataSource from "./DataCount/DataSource";
import ComponentSelect from "./DataCount/ComponentSelect";

export default function Statistics() {
  const nav = useNavigate();
  const [disable, setDisable] = useState(false);
  const [components, setComponents] = useState<IComponent[]>([]);
  const [currentSelected, setCurrentSelected] = useState<IComponent>();

  // 将当前主要内容部分置灰
  function handleDisable() {
    setDisable(true);
  }

  // 获取所有问卷组件
  useRequest(getQuestionComponents, {
    onSuccess: ({ data }) => {
      if (data.length === 0) {
        setDisable(true);
        message.warning("请先创建至少一个表单组件");
        return;
      }
      setComponents(data);
      setCurrentSelected(data[0]);
    },
  });

  return (
    <div className="flex flex-col h-full bg-[#f1f2f4]">
      <header className="flex items-center shadow-sm px-10 py-4 bg-white">
        <div className="flex-1">
          小滴低代码平台数据统计 <LineChartOutlined />
        </div>
        <div className="flex-1 flex justify-end items-center">
          <Button
            onClick={() => nav("/editor")}
            className="flex items-center mr-5"
          >
            低代码编辑平台
            <FormOutlined />
          </Button>
          <img
            src="https://sdfsdf.dev/40x40.png"
            className="rounded-full border cursor-pointer"
          />
        </div>
      </header>

      <div
        className={`${
          disable && "opacity-50 select-none pointer-events-none"
        } flex flex-1 p-4  flex-grow-[2] overflow-x-hidden overflow-y-auto`}
      >
        {/* 用户问卷提交信息统计表格组件 */}
        <div className="bg-white flex-1 mr-4">
          <ComponentDatas
            components={components}
            handleDisable={handleDisable}
          />
        </div>
        <div className="bg-white flex-[1] flex flex-col">
          <ComponentSelect
            components={components}
            setCurrnetSelected={setCurrentSelected}
            currentSelected={currentSelected?.id ?? 0}
          />
          <div className="w-full text-center">
            <DataSource currentSelected={currentSelected} />
          </div>
        </div>
      </div>
    </div>
  );
}
