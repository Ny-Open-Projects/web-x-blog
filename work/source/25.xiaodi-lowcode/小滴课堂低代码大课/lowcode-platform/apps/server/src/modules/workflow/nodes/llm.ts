export interface LlmMessage {
  role: 'system' | 'user' | 'assistant';
  content: string;
}

export interface LlmOptions {
  model?: string;
  temperature?: number;
  maxTokens?: number;
}

export interface LlmResult {
  text: string;
  model: string;
  usage?: { promptTokens?: number; completionTokens?: number };
}

export interface LlmProvider {
  readonly name: string;
  complete(messages: LlmMessage[], opts?: LlmOptions): Promise<LlmResult>;
}

/**
 * 默认 mock：不连任何外部服务即可跑通链路（开发 / 演示 / 测试）。
 * 接入真实模型时改用 OpenAiCompatibleLlmProvider，密钥只来自 env。
 */
export class MockLlmProvider implements LlmProvider {
  readonly name = 'mock';

  async complete(messages: LlmMessage[]): Promise<LlmResult> {
    const last = messages[messages.length - 1]?.content ?? '';
    const text = `[mock-llm] 收到 ${messages.length} 条消息，末条 ${last.length} 字。生产环境此处返回真实模型输出。`;
    return { text, model: 'mock-1', usage: { promptTokens: Math.ceil(last.length / 2), completionTokens: 12 } };
  }
}

/**
 * OpenAI 兼容网关（通义千问 / DeepSeek / 本地 Ollama 等均可）。
 * 密钥仅来自 env（LLM_API_KEY），绝不进图 JSON、绝不下发前端。
 */
export class OpenAiCompatibleLlmProvider implements LlmProvider {
  readonly name = 'openai-compatible';
  private baseUrl: string;
  private apiKey: string;
  private model: string;

  constructor(baseUrl: string, apiKey: string, model: string) {
    this.baseUrl = baseUrl;
    this.apiKey = apiKey;
    this.model = model;
  }

  async complete(messages: LlmMessage[], opts?: LlmOptions): Promise<LlmResult> {
    const url = `${this.baseUrl.replace(/\/$/, '')}/chat/completions`;
    const body = {
      model: opts?.model ?? this.model,
      messages,
      temperature: opts?.temperature ?? 0.7,
      max_tokens: opts?.maxTokens ?? 512,
    };
    const resp = await fetch(url, {
      method: 'POST',
      headers: { 'content-type': 'application/json', authorization: `Bearer ${this.apiKey}` },
      body: JSON.stringify(body),
    });
    if (!resp.ok) {
      throw new Error(`LLM 网关返回 ${resp.status}: ${await resp.text().catch(() => '')}`);
    }
    const json: any = await resp.json();
    return {
      text: json?.choices?.[0]?.message?.content ?? '',
      model: json?.model ?? this.model,
      usage: {
        promptTokens: json?.usage?.prompt_tokens,
        completionTokens: json?.usage?.completion_tokens,
      },
    };
  }
}

/**
 * 工厂：有 env 密钥走真实网关，否则返回 mock。
 * 这样图 JSON 里只需要写 prompt / model，密钥永远不落图、不下发前端。
 */
export function createLlmProvider(): LlmProvider {
  const base = process.env.LLM_BASE_URL;
  const key = process.env.LLM_API_KEY;
  if (base && key) {
    return new OpenAiCompatibleLlmProvider(base, key, process.env.LLM_MODEL ?? 'gpt-4o-mini');
  }
  return new MockLlmProvider();
}
