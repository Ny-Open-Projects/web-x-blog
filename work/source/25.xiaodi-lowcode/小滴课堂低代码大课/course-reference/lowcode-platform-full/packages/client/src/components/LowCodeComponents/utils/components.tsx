import { Form, Button, Input, Modal, Image, message } from "antd";
import { ulid } from "ulid";
import type {
  FormItemProps,
  FormProps,
  InputProps,
  InputRef,
  ImageProps,
} from "antd";
import { useEffect, useMemo, useState, useRef } from "react";
import type { FC, ReactNode, RefAttributes } from "react";
import type {
  TComponentPropsUnion,
  TransformedComponentConfig,
  IResources,
} from "@lowcode/share";
import { objectOmit, UploadType } from "@lowcode/share";
import { useStoreComponents } from "~/hooks";
import {
  UploadOutlined,
  LoadingOutlined,
  CloudUploadOutlined,
  DeleteOutlined,
} from "@ant-design/icons";
import { useRequest } from "ahooks";
import { deleteResource, getResources, uploadFile } from "~/api/resource";

// Form表单的子项二次封装判断是否该隐藏
interface IFormPropLabelProps extends FormItemProps {
  prop: {
    isHidden: boolean;
  };
}
export const FormPropLabel: FC<IFormPropLabelProps> = (props) => {
  // 如果isHidden为true不展示该子项
  if (props.prop.isHidden) {
    return null;
  } else {
    // 判断完后，删除prop
    return (
      <Form.Item {...objectOmit(props, ["prop"])}>{props.children}</Form.Item>
    );
  }
};

// Form表单最外层二次封装组件
interface IFormContainer extends FormProps {
  config: TransformedComponentConfig<Record<string, any>>;
  onValuesChangeAfter?: (
    changedValues: Record<keyof TComponentPropsUnion["props"], any>
  ) => void;
}
export const FormContainer: FC<IFormContainer> = (props) => {
  const [form] = Form.useForm();
  const { updateCurrentComponent } = useStoreComponents();

  // 将数据转成一维，方便设置表单数据 {src:{xxx}} => {src:'xxx'}
  const propValues = useMemo(
    () =>
      Object.entries(props.config)
        .map(([key, value]) => {
          return { [key]: value.value };
        })
        .reduce((acc, cur) => {
          return { ...acc, ...cur };
        }, {}),
    [props.config]
  );

  useEffect(() => {
    form.setFieldsValue({ ...propValues });
  }, [form, propValues]);

  // 表单值改变重新更新 store 中的值
  function handleValuesChange(
    changedValues: Record<keyof TComponentPropsUnion["props"], any>
  ) {
    updateCurrentComponent(changedValues);
    // 二维码组件的单独处理背景颜色
    props.onValuesChangeAfter?.(changedValues);
  }

  return (
    <Form
      form={form}
      layout="vertical"
      onValuesChange={handleValuesChange}
      {...objectOmit(props, ["onValuesChangeAfter"])}
    >
      {props.children as ReactNode}
    </Form>
  );
};

// 新增表单列表组件具体逻辑
interface FormListItemProps<T> {
  index: number;
  isExpand: boolean;
  newItemDefaultValue: T;
  children: ReactNode;
  onClick: () => void;
  keyName?: string;
}

export const FormListItem: FC<FormListItemProps<any>> = (props) => {
  const {
    updateCurrentCompConfigWithArray,
    updateCurrentComponent,
    getCurrentComponentConfig,
  } = useStoreComponents();

  // 每项的值发生改变触发事件修改 store 的值
  function handleValuesChange(changeValues: Record<string, any>) {
    // 转成二维数组，取第一个元素 key+value
    const objEntry = Object.entries(changeValues)[0];
    // {link:'xxx'}  =>   [[link,'xxx']]

    // 初始化时组件属性没有 key， updateCurrentComponent 修改值同时需要新增;
    // console.log(toJS(getCurrentComponentConfig.get()?.props));
    if (
      (getCurrentComponentConfig.get()?.props as any)?.[
        props.keyName ?? "items"
      ] === undefined
    ) {
      updateCurrentComponent({
        [props.keyName ?? "items"]: [
          {
            ...props.newItemDefaultValue,
            ...changeValues,
          },
        ],
      });

      return;
    }

    // 二次修改 form 值，取对应 key 修改 store 值
    updateCurrentCompConfigWithArray({
      key: props.keyName ?? "items",
      field: objEntry[0],
      index: props.index,
      value: objEntry[1],
    });
  }

  // 删除无用 key 属性
  const values = { ...(objectOmit(props, ["key"] as any) as any) };
  console.log(values);
  const [form] = Form.useForm();

  // store 的数据改变触发 form 表单视图更新
  useEffect(() => {
    props.isExpand && form?.setFieldsValue({ ...values });
  }, [values]);

  return (
    <div className="border my-1 p-2" onClick={props.onClick}>
      {props.isExpand ? (
        <Form form={form} layout="vertical" onValuesChange={handleValuesChange}>
          {props.children}
        </Form>
      ) : (
        <span className="cursor-pointer flex items-center justify-center">
          点击展开
        </span>
      )}
    </div>
  );
};

// 新增列表类型组件
interface FormContainerWithListProps<
  T extends { id: string } & Record<string, any>,
> {
  id: string;
  items: T[];
  children: ReactNode;
  newItemDefaultValue: T;
  keyName?: string;
}
export const FormContainerWithList: FC<FormContainerWithListProps<any>> = (
  props
) => {
  const { updateCurrentComponent, setItemsExpandIndex } = useStoreComponents();
  const [expandIndex, setExpandIndex] = useState(0);

  // 新增或者切换轮播图的 id 变化重置第一项为展开
  useEffect(() => {
    setExpandIndex(0);
  }, [props.id]);

  useEffect(() => {
    setItemsExpandIndex(expandIndex);
  }, [expandIndex]);

  // 添加新项按钮
  function addNewItem() {
    // 将新的数据更新 store
    updateCurrentComponent({
      [props.keyName ?? "items"]: [
        ...props.items,
        {
          ...props.newItemDefaultValue,
          id: ulid(),
        },
      ],
    });
  }
  return (
    <>
      <Button type="primary" onClick={addNewItem}>
        添加新项
      </Button>
      {props.items.map((item, index) => {
        return (
          <FormListItem
            {...item}
            index={index}
            key={item.id}
            isExpand={expandIndex === index}
            newItemDefaultValue={props.newItemDefaultValue}
            onClick={() => setExpandIndex(index)}
            keyName={props.keyName}
          >
            {props.children}
          </FormListItem>
        );
      })}
    </>
  );
};

// 已上传的每项资源组件
interface LoadResourceProps extends ImageProps {
  typeName: string;
  resourceId: number;
  onDelete: () => void;
  onClicked: () => void;
}

export const LoadResource: FC<LoadResourceProps> = ({
  src,
  resourceId,
  typeName,
  onDelete,
  onClicked,
  ...props
}) => {
  const [hover, setHover] = useState(false);

  // 删除资源接口
  const { run: execDeleteResource } = useRequest(
    () => deleteResource(resourceId),
    {
      manual: true,
      onSuccess: ({ msg }) => {
        message.success(msg ?? "删除成功");
        onDelete();
      },
    }
  );

  return (
    <div className="relative w-full h-full border">
      <div
        onClick={onClicked}
        onMouseLeave={() => setHover(false)}
        className={`overflow-hidden w-full h-full absolute top-0 left-0 bg-black/50 z-10 cursor-pointer flex flex-col items-center justify-center text-white text-lg transition-all ${
          !hover ? "hidden" : "block"
        }`}
      >
        <span className="text-sm">{props.alt}</span>
        <span>选择此{typeName}</span>
      </div>

      <Image
        src={src}
        preview={false}
        className="cursor-pointer"
        width={"100%"}
        height={"100%"}
        onMouseEnter={() => setHover(true)}
        fallback="data:image/png;base64,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"
        {...props}
      />

      <div
        onClick={execDeleteResource}
        className="float-right cursor-pointer hover:bg-neutral-400/50 p-1 rounded text-red-500/80 font-bold"
      >
        <span>删除此{typeName} </span>
        <DeleteOutlined />
      </div>
    </div>
  );
};

// 资源管理子组件详细逻辑
interface UploadComponentProps {
  visible: boolean;
  type: UploadType;
  onCancel: () => void;
  onChooise: (url: string) => void;
}

export const UploadComponent: FC<UploadComponentProps> = ({
  type,
  visible,
  onCancel,
  onChooise,
}) => {
  const uploadRef = useRef<HTMLInputElement>(null);

  const iconClassName = "text-3xl text-center block";
  const typeName = type === "image" ? "图片" : "视频";

  const [resources, setResources] = useState<IResources[]>([]);

  // 获取资源接口
  const { run: execGetResources, loading: loadingWithGetResources } =
    useRequest(async () => await getResources(type), {
      manual: true,
      onSuccess: ({ data }) => {
        setResources(data);
      },
    });

  // 上传资源接口
  const { run: execUpload, loading: loadingWithUpload } = useRequest(
    async (formData: FormData) => await uploadFile(formData),
    {
      manual: true,
      onSuccess: () => {
        // 资源上传成功之后重新请求资源获取的接口，拿到最新值
        execGetResources();
      },
    }
  );

  // 打开弹窗重新获取资源
  useEffect(() => {
    visible && execGetResources();
  }, [visible]);

  // 选择一个资源打开后触发
  const handleUploadChange = async () => {
    const files = uploadRef.current?.files;
    if (!files) return;

    const formData = new FormData();
    formData.append("type", type);
    formData.append("file", files[0]);

    // 调用上传接口
    execUpload(formData);

    // 清空掉files
    uploadRef.current.value = "";
  };

  // 如果是图片直接地址显示，如果是视频则截取视频第一帧作为封面
  function getVideoFirstFrameOrImage(url: string, type: UploadType) {
    return type === "image"
      ? url
      : `${url}?spm=qipa250&x-oss-process=video/snapshot,t_0,f_png,w_0,h_0,m_fast`;
  }

  return (
    <Modal
      title={`选择上传${typeName}`}
      open={visible}
      onOk={onCancel}
      onCancel={onCancel}
      cancelButtonProps={{ hidden: true }}
    >
      {loadingWithGetResources ? (
        <LoadingOutlined className={`${iconClassName} text-center`} />
      ) : (
        <div className="grid grid-cols-3 grid-rows-3 gap-x-4 gap-y-10 mt-6">
          <div
            onClick={() => uploadRef.current?.click()}
            className={`cursor-pointer text-gray-600 border select-none hover:border-dashed flex flex-col justify-center items-center ${
              resources.length <= 0 && "py-4"
            } ${"opacity-50 cursor-not-allowed"}`}
          >
            {loadingWithUpload ? (
              <LoadingOutlined className={iconClassName} />
            ) : (
              <CloudUploadOutlined className={iconClassName} />
            )}

            <span className="block text-center py-2 font-mono font-bold">
              {typeName}上传
            </span>

            <input
              hidden
              type="file"
              ref={uploadRef}
              accept={type === "video" ? "video/*" : "image/*"}
              onInput={handleUploadChange}
            />
          </div>

          {resources.map((item) => {
            return (
              <LoadResource
                onDelete={execGetResources}
                resourceId={item.id}
                typeName={typeName}
                alt={item.name}
                src={getVideoFirstFrameOrImage(item.url, item.type)}
                key={item.id}
                onClicked={() => onChooise(item.url)}
              />
            );
          })}
        </div>
      )}
    </Modal>
  );
};

// 资源管理组件
interface UploadEditOrChooiseInputProps
  extends InputProps,
    RefAttributes<InputRef> {
  propName: string;
  type: "video" | "image";
  listOptions?: {
    keyName?: string;
    defaultValues: Record<string, any>;
  };
}
export const UploadEditOrChooiseInput: FC<UploadEditOrChooiseInputProps> = ({
  type,
  propName,
  listOptions,
  ...props
}) => {
  const [visible, setVisible] = useState(false);

  const {
    updateCurrentComponent,
    updateCurrentCompConfigWithArray,
    getCurrentComponentConfig,
    store,
  } = useStoreComponents();

  // 选择某个已经上传的资源
  function handleChooise(url: string) {
    setVisible(false);
    // 选择列表形式的资源上传组件时修改 stroe 的方法
    if (listOptions !== undefined) {
      if (
        (getCurrentComponentConfig.get()?.props as any)?.[
          listOptions.keyName ?? "items"
        ] === undefined
      ) {
        updateCurrentComponent({
          [listOptions.keyName ?? "items"]: [
            {
              ...listOptions.defaultValues,
              [propName]: url,
            },
          ],
        });

        return;
      }

      updateCurrentCompConfigWithArray({
        key: listOptions.keyName ?? "items",
        field: propName,
        index: store.itemsExpandIndex,
        value: url,
      });
    } else {
      // 选择非列表形式的资源上传组件时修改 stroe 的方法
      updateCurrentComponent({ [propName]: url });
    }
  }

  return (
    <>
      <Input
        {...props}
        suffix={
          <UploadOutlined
            className="cursor-pointer"
            onClick={() => setVisible(true)}
          />
        }
      />
      <UploadComponent
        type={type}
        visible={visible}
        onChooise={handleChooise}
        onCancel={() => setVisible(false)}
      />
    </>
  );
};
