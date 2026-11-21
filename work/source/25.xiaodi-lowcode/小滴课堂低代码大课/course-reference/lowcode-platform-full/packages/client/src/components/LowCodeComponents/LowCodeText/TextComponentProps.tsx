import { useMemo } from "react";

import { Input, Segmented } from "antd";
import type { SegmentedLabeledOption } from "antd/es/segmented";
import type { ITextComponentProps } from "@lowcode/share";
import {
  fillComponentPropsByConfig,
  textComponentDefaultConfig,
} from "@lowcode/share";
import { FormContainer, FormPropLabel } from "..";

export default function TextComponentProps(_props: ITextComponentProps) {
  const props = useMemo(() => {
    return fillComponentPropsByConfig(_props, textComponentDefaultConfig);
  }, [_props]);

  // 字体大小配置
  const options: SegmentedLabeledOption[] = [
    {
      value: "xs",
      label: "超小",
    },
    {
      value: "sm",
      label: "小",
    },
    {
      value: "base",
      label: "基础",
    },
    {
      value: "lg",
      label: "大",
    },
    {
      value: "xl",
      label: "超大",
    },
  ];

  return (
    <FormContainer config={props}>
      <FormPropLabel name="title" prop={props.title} label="展示的文本：">
        <Input placeholder="展示的文本" />
      </FormPropLabel>
      <FormPropLabel name="size" prop={props.size} label="设置文字大小：">
        <Segmented options={options} />
      </FormPropLabel>
    </FormContainer>
  );
}
