import { calcValueByString, componentList } from "..";
import type { TBasicComponentConfig, TransformedComponentConfig } from ".";

// 获取组件的入口
export function getComponentByType(type: TBasicComponentConfig["type"]) {
  return componentList[type];
}

// 将组件配置属性的深层对象，转成一维，直接拿到defaultValue值作为配置属性值
export function getDefaultValueByConfig(
  componentPropsWrapper: TransformedComponentConfig<Record<string, any>>
) {
  return Object.entries(componentPropsWrapper).reduce(
    (acc, [key, value]) => {
      acc[key] = value.defaultValue;
      return acc;
    },
    {} as Record<string, any>
  );
}

// 转换组件的属性键值对数据
// {src:'xxx'} => {src:{
//                  defaultValue:'xxx',
//                  isHidden:'xxx',
//                  value:'xx'
//                 }}
export function fillComponentPropsByConfig<
  T extends TransformedComponentConfig<Record<string, any>>,
>(props: Record<string, any>, componentPropsWrapper: T): T {
  const result = {} as unknown as any;

  for (const [key, value] of Object.entries(componentPropsWrapper)) {
    result[key] = {
      isHidden: value.isHidden,
      defaultValue: value.defaultValue,
      value:
        props?.[key] !== undefined
          ? calcValueByString(props[key])
          : value.defaultValue,
    };
  }
  return result;
}
