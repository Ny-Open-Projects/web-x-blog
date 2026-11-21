import { Button, Form, Input } from "antd";
import { useSendCode } from "../../hooks";
import { useRequest } from "ahooks";
import { getLoginWithPhone } from "../../api/user";
import { useStoreAuth } from "../../hooks/useStoreAuth";

export default function Captcha() {
  const [form] = Form.useForm();
  const { sendCodeTemplate } = useSendCode(form, "login");
  const { login } = useStoreAuth();
  //  验证码登录请求
  const { run, loading } = useRequest(
    async (values) => await getLoginWithPhone(values),
    {
      manual: true,
      onSuccess: ({ data }) => {
        login(data);
      },
    }
  );

  return (
    <div className="space-y-4">
      <div className="space-y-2">
        <Form onFinish={run} form={form}>
          <Form.Item
            label="账号"
            name="phone"
            rules={[
              { required: true, message: "请输入手机号!" },
              { pattern: /^1\d{10}$/, message: "请输入正确的手机号!" },
            ]}
          >
            <Input placeholder="请输入手机号" />
          </Form.Item>

          {sendCodeTemplate}

          <Form.Item>
            <Button
              type="primary"
              htmlType="submit"
              className="w-full"
              loading={loading}
            >
              登录
            </Button>
          </Form.Item>
        </Form>
      </div>
    </div>
  );
}
