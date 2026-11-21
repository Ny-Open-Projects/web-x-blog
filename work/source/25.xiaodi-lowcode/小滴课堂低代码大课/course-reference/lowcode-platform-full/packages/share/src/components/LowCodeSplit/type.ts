import type { TBasicComponentConfig, TransformedComponentConfig } from '..'

export interface ISplitComponentProps {
  text: string
  dashed: boolean
  orientation: 'left' | 'center' | 'right'
}

export type TSplitComponentConfig = TBasicComponentConfig<'split', ISplitComponentProps>

export type TSplitComponentConfigResult = TransformedComponentConfig<ISplitComponentProps>

export const splitComponentDefaultConfig: TSplitComponentConfigResult = {
  dashed: {
    value: false,
    defaultValue: false,
    isHidden: false,
  },
  orientation: {
    value: 'center',
    defaultValue: 'center',
    isHidden: false,
  },
  text: {
    value: '',
    defaultValue: '',
    isHidden: false,
  },
}
