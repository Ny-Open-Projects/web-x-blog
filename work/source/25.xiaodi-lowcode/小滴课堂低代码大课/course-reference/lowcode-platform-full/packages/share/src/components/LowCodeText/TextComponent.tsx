import React, { useEffect, useMemo, useState } from "react";
import { getDefaultValueByConfig } from "..";
import { textComponentDefaultConfig } from ".";
import type { ITextComponentProps } from ".";

export default function TextComponent(_props: ITextComponentProps) {
  const props = useMemo(() => {
    return {
      ...getDefaultValueByConfig(textComponentDefaultConfig),
      ..._props,
    };
  }, [_props]);

  const [size, setSize] = useState("");

  useEffect(() => {
    switch (_props.size) {
      case "sm":
        setSize("text-sm");
        break;
      case "base":
        setSize("text-base");
        break;
      case "lg":
        setSize("text-lg");
        break;
      case "xl":
        setSize("text-xl");
        break;
      case "xs":
        setSize("text-xs");
        break;
      default:
        setSize("text-base");
        break;
    }
  }, [_props]);

  return <span className={size}>{props.title}</span>;
}
