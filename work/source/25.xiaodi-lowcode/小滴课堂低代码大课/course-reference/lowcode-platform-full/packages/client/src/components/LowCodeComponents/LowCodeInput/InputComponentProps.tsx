import { Input } from "antd";
import { useMemo } from "react";
import type { IInputComponentProps } from "@lowcode/share";
import {
  fillComponentPropsByConfig,
  inputComponentDefaultConfig,
} from "@lowcode/share";
import { FormContainer, FormPropLabel } from "..";

export default function InputComponentProps(_props: IInputComponentProps) {
  const props = useMemo(() => {
    return fillComponentPropsByConfig(_props, inputComponentDefaultConfig);
  }, [_props]);

  return (
    <FormContainer layout="vertical" config={props}>
      <FormPropLabel prop={props.title} name="title" label="标题：">
        <Input />
      </FormPropLabel>
      <FormPropLabel prop={props.text} name="text" label="默认输入的内容：">
        <Input />
      </FormPropLabel>
      <FormPropLabel
        prop={props.placeholder}
        name="placeholder"
        label="占位符："
      >
        <Input />
      </FormPropLabel>
    </FormContainer>
  );
}
