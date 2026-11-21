import React, { useMemo } from "react";
import { Alert } from "antd";
import { getDefaultValueByConfig } from "..";
import type { IAlertComponentProps } from ".";
import { alertComponentDefaultConfig } from ".";

export default function AlertComponent(_props: IAlertComponentProps) {
  const props = useMemo(() => {
    return {
      ...getDefaultValueByConfig(alertComponentDefaultConfig),
      ..._props,
    };
  }, [_props]);

  return (
    <Alert
      type={props.type}
      message={props.title || "请输入文本"}
      showIcon={props.showIcon}
      closable={props.showClose}
    />
  );
}
