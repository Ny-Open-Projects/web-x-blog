import { useMemo } from 'react'
import { Checkbox, Form, Input } from 'antd'
import type { ICheckboxComponentProps } from '@lowcode/share'
import { checkboxComponentDefaultConfig, fillComponentPropsByConfig } from '@lowcode/share'
import { FormContainer, FormContainerWithList, FormPropLabel } from '..'

export default function CheckboxComponentProps(_props: ICheckboxComponentProps) {
  const props = useMemo(() => {
    return fillComponentPropsByConfig(_props, checkboxComponentDefaultConfig)
  }, [_props])

  function getListItem() {
    return {
      id: '',
      value: `选项${props.options.value.length + 1}`,
    }
  }

  return (
    <>
      <FormContainer layout="vertical" config={props}>
        <FormPropLabel prop={props.title} name="title" label="默认展示的标题：">
          <Input />
        </FormPropLabel>

        <FormPropLabel prop={props.defaultChecked} name="defaultChecked" label="默认选择的选项：">
          <Checkbox.Group
            options={props.options.value.map(item => ({
              value: item.id,
              label: item.value,
            }))}
          />
        </FormPropLabel>
      </FormContainer>

      <FormContainerWithList
        keyName="options"
        id={props.id.value}
        items={props.options.value}
        newItemDefaultValue={getListItem()}
      >
        <Form.Item label="选项名称：" name="value">
          <Input />
        </Form.Item>
      </FormContainerWithList>
    </>
  )
}
