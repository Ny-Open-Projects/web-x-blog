/**
 * 副作用节点的可替换 Provider 接口。
 *
 * 设计意图（可商用 / 零外部依赖可跑通）：
 *  - 工作流里"发短信 / 传 OSS / 存表单"都是副作用，不应把具体云厂商逻辑写死在节点里。
 *  - 节点执行时从 `ExecCtx.services` 取对应 Provider；默认给一份 in-memory / console 实现，
 *    保证不连任何外部服务也能把整条链路跑通（用于开发、测试、演示）。
 *  - 生产环境在 WorkflowModule 里把这里替换成阿里云 / 腾讯云等真实实现即可，节点代码不动。
 */

import { Repository } from 'typeorm';
import { WfSubmission } from '../entities/wf-submission.entity';

export interface SmsSendOptions {
  phone: string;
  template: string;
  params?: Record<string, unknown>;
}

export interface SmsProvider {
  readonly name: string;
  send(opts: SmsSendOptions): Promise<{ ok: boolean; provider: string; messageId?: string }>;
}

export interface OssUploadOptions {
  key: string;
  content?: string;
  size?: number;
  contentType?: string;
}

export interface OssProvider {
  readonly name: string;
  upload(opts: OssUploadOptions): Promise<{ url: string; key: string }>;
}

export interface FormRecord {
  id: string;
  formId: string;
  data: Record<string, unknown>;
  tenantId?: string;
  createdAt: string;
}

export interface FormStore {
  save(opts: { formId: string; data: Record<string, unknown>; tenantId?: string }): Promise<FormRecord>;
}

export interface WorkflowServices {
  sms: SmsProvider;
  oss: OssProvider;
  formStore: FormStore;
}

// ---------------------------------------------------------------------------
// 默认实现（开发 / 演示 / 单元测试用，不依赖任何外部服务）
// ---------------------------------------------------------------------------

let _seq = 0;

export class MemoryFormStore implements FormStore {
  private items = new Map<string, FormRecord>();

  async save(opts: { formId: string; data: Record<string, unknown>; tenantId?: string }): Promise<FormRecord> {
    const id = `sub_${Date.now()}_${++_seq}`;
    const rec: FormRecord = {
      id,
      formId: opts.formId,
      data: opts.data,
      tenantId: opts.tenantId,
      createdAt: new Date().toISOString(),
    };
    this.items.set(id, rec);
    return rec;
  }
}

export class ConsoleSmsProvider implements SmsProvider {
  readonly name = 'console';

  async send(opts: SmsSendOptions) {
    // 生产实现应调用短信网关；此处仅打印，便于本地验证链路。
    console.log(`[sms:console] -> ${opts.phone} tpl=${opts.template}`, opts.params ?? {});
    return { ok: true, provider: 'console', messageId: `msg_${Date.now()}` };
  }
}

export class LocalOssProvider implements OssProvider {
  readonly name = 'local';

  async upload(opts: OssUploadOptions) {
    const url = `https://oss.local/${encodeURIComponent(opts.key)}`;
    console.log(`[oss:local] upload ${opts.key} -> ${url}`);
    return { url, key: opts.key };
  }
}

export const DEFAULT_SERVICES: WorkflowServices = {
  sms: new ConsoleSmsProvider(),
  oss: new LocalOssProvider(),
  formStore: new MemoryFormStore(),
};

/**
 * 真实表单存储（M6）：落库到 wf_submission，使 formSubmit 节点具备可追溯业务数据。
 * 其余 Provider（短信/OSS）仍保留 console/local 默认实现，生产在 WorkflowModule 替换即可。
 */
export class DbFormStore implements FormStore {
  constructor(private repo: Repository<WfSubmission>) {}

  async save(opts: { formId: string; data: Record<string, unknown>; tenantId?: string }): Promise<FormRecord> {
    const e = this.repo.create({
      formId: opts.formId,
      data: opts.data,
      tenantId: opts.tenantId,
    });
    const saved = await this.repo.save(e);
    return {
      id: saved.id,
      formId: saved.formId,
      data: saved.data,
      tenantId: saved.tenantId,
      createdAt: saved.createdAt.toISOString(),
    };
  }
}
