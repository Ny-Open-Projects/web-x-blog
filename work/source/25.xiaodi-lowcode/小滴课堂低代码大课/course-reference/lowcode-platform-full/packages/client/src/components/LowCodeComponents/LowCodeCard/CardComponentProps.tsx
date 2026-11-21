import { Input } from "antd";
import { useMemo } from "react";
import {
  type ICardComponentProps,
  cardComponentDefaultConfig,
  fillComponentPropsByConfig,
} from "@lowcode/share";
import { FormContainer, FormPropLabel, UploadEditOrChooiseInput } from "..";

export default function CardComponentProps(_props: ICardComponentProps) {
  const props = useMemo(() => {
    return fillComponentPropsByConfig(_props, cardComponentDefaultConfig);
  }, [_props]);

  return (
    <FormContainer layout="vertical" config={props}>
      <FormPropLabel prop={props.coverImg} name="coverImg" label="封面图片:">
        <UploadEditOrChooiseInput propName="coverImg" type="image" />
      </FormPropLabel>
      <FormPropLabel prop={props.title} name="title" label="标题:">
        <Input />
      </FormPropLabel>
      <FormPropLabel prop={props.description} name="description" label="描述:">
        <Input />
      </FormPropLabel>
    </FormContainer>
  );
}
