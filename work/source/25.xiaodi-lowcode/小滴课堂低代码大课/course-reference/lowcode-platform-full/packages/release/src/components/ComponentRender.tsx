"use client";

import {
  type GetReleaseDataResponse,
  type TBasicComponentConfig,
  getComponentByType,
} from "@lowcode/share";
import { useRequest } from "ahooks";
import { useImmer } from "use-immer";
import { useState } from "react";
import { message, Button } from "antd";

const usingInputType = ["input", "textArea", "radio", "checkbox"];

// 生成组件
function generateComponent(
  conf: TBasicComponentConfig,
  onUpdate: (value: any) => void
) {
  const Component = getComponentByType(conf.type);

  // 非输入类型直接渲染
  if (!usingInputType.includes(conf.type))
    return <Component {...conf.props} key={conf.id} />;
  // 输入类型需要更新回调
  else return <Component {...conf.props} key={conf.id} onUpdate={onUpdate} />;
}

// 获取组件的值
function getQuestionComponentValueField(component: any) {
  switch (component.type) {
    case "input":
    case "textArea":
      return "text";
    case "radio":
      return "defaultRadio";
    case "checkbox":
      return "defaultChecked";
    default:
      return null;
  }
}

// 组件渲染类型
interface ComponentRenderType {
  id: string;
  data: GetReleaseDataResponse;
}

// 组件渲染组件
export default function ComponentRender({ data, id }: ComponentRenderType) {
  const [isPosted, setIsPosted] = useState(false);
  // 克隆数据并进行局部状态保存
  const [localData, setLocalData] = useImmer(
    JSON.parse(JSON.stringify(data)) as ComponentRenderType["data"]
  );

  // 生成组件
  function generateComponents() {
    return localData.components
      .map((comp) => {
        return {
          id: comp.id,
          type: comp.type,
          props: comp.options,
        };
      })
      .map((comp: any) =>
        generateComponent(comp, (value) => {
          // 更新局部保存的数据
          setLocalData((draft) => {
            const target = draft.components.find(
              (item) => item.id === comp.id
            )!;
            const questionComponentValueField =
              getQuestionComponentValueField(target);
            if (questionComponentValueField)
              target.options[questionComponentValueField] = value;
          });
        })
      );
  }

  // 请求检查是否已经提交过问卷
  useRequest(
    async () => {
      const _f = await fetch(
        `${process.env.NEXT_PUBLIC_API_BASE_URL}/low_code/is_question_data_posted?page_id=${data.id}`
      );
      return _f.json() as Promise<{ data: boolean }>;
    },
    {
      onSuccess: ({ data }) => {
        // 如果已经提交过则不让再次提交
        if (data) {
          setIsPosted(true);
          message.open({ content: "您已提交过问卷，感谢您的参与" });
        }
      },
    }
  );

  // 提交问卷请求
  const { run, loading } = useRequest(
    async () => {
      // 循环判断值是否存在
      // 如果值不存在则不允许提交
      const isNotCompleted = localData.components.some((comp) => {
        const questionComponentValueField =
          getQuestionComponentValueField(comp);
        if (
          questionComponentValueField &&
          !comp.options[questionComponentValueField]
        )
          return !["defaultRadio", "defaultChecked"].includes(
            questionComponentValueField
          );

        return false;
      });
      // 若问卷未填写完整，显示提示信息
      if (isNotCompleted) return { msg: "请填写完整问卷信息", data: false };

      // 提交问卷数据
      const _f = await fetch(
        `${process.env.NEXT_PUBLIC_API_BASE_URL}/low_code/question_data?id=${data.id}`,
        {
          headers: {
            "Content-Type": "application/json",
          },
          method: "POST",
          body: JSON.stringify({
            page_id: id,
            props: localData.components
              .filter((comp) => usingInputType.includes(comp.type))
              .map((comp) => {
                return {
                  id: comp.id,
                  value: comp.options[getQuestionComponentValueField(comp)!],
                };
              }),
          }),
        }
      );

      return _f.json();
    },
    {
      manual: true,
      onSuccess: ({ msg, data }) => {
        if (data !== undefined) {
          message.warning(msg);
        } else {
          message.success(msg);
          setIsPosted(true);
        }
      },
    }
  );

  return (
    <div
      className={`${isPosted && "opacity-50 select-none pointer-events-none"}`}
    >
      {/* 组件渲染 */}
      {generateComponents()}

      {/* 提交问卷按钮 */}
      {data.components.some((comp) => usingInputType.includes(comp.type)) && (
        <div className="flex items-center justify-center">
          <Button type="primary" onClick={run} loading={loading}>
            提交问卷
          </Button>
        </div>
      )}
    </div>
  );
}
