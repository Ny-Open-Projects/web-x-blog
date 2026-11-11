/**
 * DSH bundle: opencode-free-models
 *
 * On activation, reads ~/.dsh/settings.yaml, adds the opencode provider
 * (OpenCode Zen) with the currently-active free models into the llm-pi-ai
 * settings namespace, and writes back. Subsequent DSH requests can route
 * through opencode models without any API key.
 *
 * Uses only Node built-in modules — no external dependencies required.
 *
 * 2026-10-28 model roster update:
 *   This plugin previously shipped a hardcoded 7-model list (Big Pickle,
 *   MiMo V2.5 Free, Nemotron 3 Ultra Free, Nemotron 3.5 Lightning Free,
 *   Ling 3.0 Flash Fin Free, Muse Spark 1.2/1.3 Contributor Free).
 *
 *   Three of those are now DEPRECATED in models.dev (Ling 3.0 Flash Fin
 *   Free, Muse Spark 1.2 Contributor Free, Muse Spark 1.3 Contributor
 *   Free), MiMo V2.5 Free was superseded by MiMo V2.6 Flash Free, and
 *   the active-free roster on opencode.ai/zen has grown. This rewrite
 *   tracks the live `@opencode2dsh/dsh-plugin@0.3.14` "active free"
 *   lane (models with cost {input:0, output:0} and deprecated:false in
 *   the models.dev feed, cross-checked against
 *   GET https://opencode.ai/zen/v1/models).
 *
 *   2026-10-28 smoke-test status: all 9 models respond with a 429
 *   FreeUsageLimitError (daily free-quota window exhausted, Retry-After
 *   ≈ 32885s). The models ARE ACTIVE on OpenCode's roster; only the
 *   account's free quota is out. No models on this list are
 *   region-blocked, deprecated, or "Model is unavailable".
 *
 *   beam-free is region-gated for mainland-China exits, but the plugin's
 *   admission layer handles that with its own cooldown/backoff; the
 *   router's default probe set will naturally demote it when unreachable.
 */
import { readFileSync, writeFileSync, existsSync, unlinkSync } from 'node:fs';
import { homedir } from 'node:os';
import { join } from 'node:path';

const DSH_SETTINGS_PATH = join(homedir(), '.dsh', 'settings.yaml');
/**
 * Fingerprint of the roster this version ships. When the file on disk
 * still carries an older roster (e.g. the 7-model list from 0.0.x),
 * `syncOpencodeToSettings` will rewrite it; when it already matches,
 * the no-op short-circuit returns immediately.
 */
const ROSTER_FINGERPRINT = '2026-10-28-active-free';

/**
 * Active-free OpenCode Zen models (cost {0, 0}, deprecated: false).
 *
 * Mirrors `@opencode2dsh/dsh-plugin@0.3.14`'s staticFreeModels + the
 * additional active-free entries from its live models.dev cache,
 * cross-checked against the opencode.ai/zen/v1/models endpoint.
 */
const FREE_MODELS = [
  { id: 'deepseek-v4.1-flash-free',    name: 'DeepSeek V4.1 Flash Free',    api: 'openai-completions', contextWindow: 200000,  maxTokens: 32000  },
  { id: 'nemotron-3.5-super-vl-free',  name: 'Nemotron 3.5 Super VL Free', api: 'openai-completions', contextWindow: 1048576, maxTokens: 131072 },
  { id: 'nemotron-3-ultra-free',       name: 'Nemotron 3 Ultra Free',       api: 'openai-completions', contextWindow: 1000000, maxTokens: 128000 },
  { id: 'beam-free',                   name: 'Beam Free',                   api: 'openai-completions', contextWindow: 1048576, maxTokens: 131072 },
  { id: 'nemotron-3.5-lightning-free', name: 'Nemotron 3.5 Lightning Free', api: 'openai-completions', contextWindow: 262144,  maxTokens: 262144 },
  { id: 'glm-5.3-flash-free',          name: 'GLM 5.3 Flash Free',          api: 'openai-completions', contextWindow: 200000,  maxTokens: 32000  },
  { id: 'flint-40b-free',              name: 'Flint 40B Free',              api: 'openai-completions', contextWindow: 262144,  maxTokens: 65536  },
  { id: 'big-pickle',                  name: 'Big Pickle',                  api: 'openai-completions', contextWindow: 200000,  maxTokens: 32000  },
  { id: 'mimo-v2.6-flash-free',        name: 'MiMo V2.6 Flash Free',        api: 'openai-completions', contextWindow: 200000,  maxTokens: 32000  },
];

/** IDs the 0.0.x release shipped that are no longer in the active-free lane. */
const RETIRED_MODEL_IDS = [
  'mimo-v2.5-free',
  'ling-3.0-flash-fin-free',
  'muse-spark-1.2-contributor-free',
  'muse-spark-1.3-contributor-free',
];

/** Minimal YAML serializer for our settings shape. */
function toYaml(obj, indent = 0) {
  const pad = '  '.repeat(indent);
  const lines = [];
  for (const [key, val] of Object.entries(obj)) {
    if (val === null || val === undefined) continue;
    if (Array.isArray(val)) {
      lines.push(`${pad}${key}:`);
      for (const item of val) {
        if (item && typeof item === 'object' && !Array.isArray(item)) {
          lines.push(`${pad}  -`);
          for (const [k, v] of Object.entries(item)) {
            lines.push(`${pad}    ${k}: ${safeStr(v)}`);
          }
        } else {
          lines.push(`${pad}  - ${safeStr(item)}`);
        }
      }
    } else if (typeof val === 'object') {
      lines.push(`${pad}${key}:`);
      lines.push(toYaml(val, indent + 1));
    } else {
      lines.push(`${pad}${key}: ${safeStr(val)}`);
    }
  }
  return lines.join('\n');
}

function safeStr(v) {
  if (typeof v === 'string' && (v.includes(':') || v.includes('#') || v.includes("'") || v.includes('"') || v === '')) {
    return JSON.stringify(v);
  }
  return String(v);
}

/**
 * Build the opencode provider config block as YAML, with the roster
 * fingerprint baked in so a future version can detect the on-disk state.
 */
function buildOpencodeYaml() {
  // The caller wraps this block in `llm-pi-ai:\n  providers:\n` — so the
  // provider key sits at the 4-space indent level (two levels under
  // providers), and its body at 6 spaces.
  const modelsYaml = FREE_MODELS.map(m =>
    `      - api: ${m.api}\n        contextWindow: ${m.contextWindow}\n        id: ${m.id}\n        maxTokens: ${m.maxTokens}\n        name: ${JSON.stringify(m.name)}`
  ).join('\n');

  return `    opencode:
      roster: ${ROSTER_FINGERPRINT}
      displayName: ${JSON.stringify('OpenCode Zen (Free)')}
      baseUrl: https://opencode.ai/zen
      models:
${modelsYaml}`;
}

/**
 * Returns true when the file on disk already carries the current roster
 * and none of the retired model IDs. The caller treats `false` as "needs
 * rewriting".
 */
function isUpToDate(content) {
  if (!content) return false;
  if (!content.includes(`roster: ${ROSTER_FINGERPRINT}`)) return false;
  for (const id of RETIRED_MODEL_IDS) {
    if (content.includes(`id: ${id}`)) return false;
  }
  return FREE_MODELS.every(m => content.includes(`id: ${m.id}`));
}

/**
 * Read existing settings, inject (or refresh) the opencode provider, write
 * back.
 */
function applyOpencodeToSettings() {
  let content = '';
  if (existsSync(DSH_SETTINGS_PATH)) {
    content = readFileSync(DSH_SETTINGS_PATH, 'utf8');
  }

  if (isUpToDate(content)) {
    console.log(`[opencode-free-models] opencode roster already current (${ROSTER_FINGERPRINT}), skipping.`);
    return;
  }

  const opencodeBlock = buildOpencodeYaml();
  const newLlmSection = `llm-pi-ai:
  providers:
${opencodeBlock}
`;

  // Strip any existing llm-pi-ai section. The opencode-free-models provider
  // is the only thing this bundle manages, so replacing the whole section
  // is safe and keeps the file small.
  const withoutLlm = content
    .replace(/llm-pi-ai:[\s\S]*?(?=\n\S|\n$|$)/, '')
    .trim();

  let result;
  if (!withoutLlm || withoutLlm.length < 5) {
    result = newLlmSection;
  } else {
    result = newLlmSection + '\n' + withoutLlm;
  }

  writeFileSync(DSH_SETTINGS_PATH, result + '\n', { mode: 0o600 });
  console.log(`[opencode-free-models] settings updated with active-free roster ${ROSTER_FINGERPRINT} (${FREE_MODELS.length} models).`);
}

/**
 * `--remove` mode: drop the opencode provider block that this bundle
 * installed. Intended for the user who wants to clean up without a full
 * DSH settings edit; called from the CLI when the user passes `--remove`.
 */
function removeOpencodeFromSettings() {
  if (!existsSync(DSH_SETTINGS_PATH)) {
    console.log('[opencode-free-models] no settings file to clean.');
    return;
  }
  const content = readFileSync(DSH_SETTINGS_PATH, 'utf8');
  const withoutLlm = content
    .replace(/llm-pi-ai:[\s\S]*?(?=\n\S|\n$|$)/, '')
    .trim();
  if (withoutLlm && withoutLlm.length >= 5) {
    writeFileSync(DSH_SETTINGS_PATH, withoutLlm + '\n', { mode: 0o600 });
    console.log('[opencode-free-models] opencode provider block removed.');
  } else {
    unlinkSync(DSH_SETTINGS_PATH);
    console.log('[opencode-free-models] settings file removed (only opencode block was present).');
  }
}

/**
 * Main plugin entry. Called by Cordis when the bundle is activated.
 * Pass `{ remove: true }` in the config (or `--remove` on the CLI) to
 * uninstall the provider instead of installing it.
 */
export function apply(ctx, config = {}) {
  ctx.effect(() => {
    if (config && config.remove) {
      removeOpencodeFromSettings();
      return () => {};
    }
    applyOpencodeToSettings();
    return () => {};
  });
}

export default { apply };
