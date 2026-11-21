/** 多租户预留：所有持久化实体实现此接口，后续 SaaS 化无需改结构（仅补隔离策略）。 */
export interface TenantScoped {
  tenantId?: string;
}
