import { useMemo } from 'react'

import { Input, Segmented } from 'antd'
import type { SegmentedLabeledOption } from 'antd/es/segmented'
import type { ISplitComponentProps } from '@lowcode/share'
import { fillComponentPropsByConfig, splitComponentDefaultConfig } from '@lowcode/share'
import { FormContainer, FormPropLabel } from '..'

export default function SplitComponentProps(_props: ISplitComponentProps) {
  const props = useMemo(() => {
    return fillComponentPropsByConfig(_props, splitComponentDefaultConfig)
  }, [_props])

  const options: SegmentedLabeledOption[] = [
    {
      value: 'left',
      label: '距左',
    },
    {
      value: 'center',
      label: '距中',
    },
    {
      value: 'right',
      label: '距右',
    },
  ]

  return (
    <FormContainer config={props}>
      <FormPropLabel prop={props.text} name="text" label="文字：">
        <Input placeholder="请输入文字" />
      </FormPropLabel>

      <FormPropLabel prop={props.dashed} name="dashed" label="是否设置为虚线：">
        <Input placeholder="请输入虚线" />
      </FormPropLabel>

      <FormPropLabel prop={props.orientation} name="orientation" label="文字位置：">
        <Segmented options={options} />
      </FormPropLabel>
    </FormContainer>
  )
}
