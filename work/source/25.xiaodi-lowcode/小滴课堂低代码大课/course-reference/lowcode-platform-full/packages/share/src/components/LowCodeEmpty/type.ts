import type { IImageComponentProps, TBasicComponentConfig, TransformedComponentConfig } from '..'

export interface IEmptyComponentProps {
  image: string
  description: string
  imageWidth?: number
  imageHeight?: number
  imageObjectFit: IImageComponentProps['fit']
}

export type TEmptyComponentConfig = TBasicComponentConfig<'empty', IEmptyComponentProps>

export type TEmptyComponentConfigResult = TransformedComponentConfig<IEmptyComponentProps>

export const emptyComponentDefaultConfig: TEmptyComponentConfigResult = {
  description: {
    value: '暂无数据',
    defaultValue: '暂无数据',
    isHidden: false,
  },
  image: {
    value: '',
    defaultValue: '',
    isHidden: false,
  },
  imageWidth: {
    value: 100,
    defaultValue: 100,
    isHidden: false,
  },
  imageHeight: {
    value: 100,
    defaultValue: 100,
    isHidden: false,
  },
  imageObjectFit: {
    value: 'contain',
    defaultValue: 'contain',
    isHidden: false,
  },
}
