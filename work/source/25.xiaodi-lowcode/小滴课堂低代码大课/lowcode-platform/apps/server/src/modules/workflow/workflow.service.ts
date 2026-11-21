import { Injectable, NotFoundException, ForbiddenException, Inject } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { WfGraph } from './entities/wf-graph.entity';
import { WfNodeDef } from './entities/wf-node-def.entity';
import { WfRun } from './entities/wf-run.entity';
import { WfRunNode } from './entities/wf-run-node.entity';
import { WfGeneratedPage } from './entities/wf-generated-page.entity';
import { WfAudit } from './entities/wf-audit.entity';
import { CreateWorkflowDto } from './dto/create-workflow.dto';
import { RunWorkflowDto } from './dto/run-workflow.dto';
import { runDag, AuditEntry } from './engine/dag';
import { renderPageToHtml } from './engine/render-page';
import { PageSchema } from '@lowcode/shared';
import { NODE_REGISTRY, NODE_CONTRACTS } from './nodes/registry';
import { WorkflowServices } from './nodes/providers';

@Injectable()
export class WorkflowService {
  constructor(
    @InjectRepository(WfGraph) private graphRepo: Repository<WfGraph>,
    @InjectRepository(WfNodeDef) private nodeDefRepo: Repository<WfNodeDef>,
    @InjectRepository(WfRun) private runRepo: Repository<WfRun>,
    @InjectRepository(WfRunNode) private runNodeRepo: Repository<WfRunNode>,
    @InjectRepository(WfGeneratedPage) private pageRepo: Repository<WfGeneratedPage>,
    @InjectRepository(WfAudit) private auditRepo: Repository<WfAudit>,
    @Inject('WORKFLOW_SERVICES') private services: WorkflowServices,
  ) {}

  private toGraphJson(dto: CreateWorkflowDto) {
    return { nodes: dto.nodes, edges: dto.edges };
  }

  async create(dto: CreateWorkflowDto, tenantId?: string | null) {
    const g = this.graphRepo.create({
      name: dto.name,
      version: dto.version ?? 1,
      graphJson: this.toGraphJson(dto),
      status: 'draft',
      tenantId: tenantId ?? undefined,
    });
    return this.graphRepo.save(g);
  }

  async list(tenantId?: string | null) {
    return this.graphRepo.find({
      where: tenantId ? { tenantId } : undefined,
      order: { createdAt: 'DESC' },
    });
  }

  /** 节点目录：供前端画布渲染（与后端注册表同源） */
  nodeCatalog() {
    return NODE_CONTRACTS;
  }

  async get(id: string, tenantId?: string | null) {
    const g = await this.graphRepo.findOne({ where: { id } });
    if (!g) throw new NotFoundException(`workflow ${id} not found`);
    // 租户隔离：携带 tenantId 时，禁止跨租户访问他人图定义
    if (tenantId && g.tenantId && g.tenantId !== tenantId) {
      throw new ForbiddenException(`workflow ${id} 不属于当前租户`);
    }
    return g;
  }

  async update(id: string, dto: CreateWorkflowDto) {
    await this.get(id);
    await this.graphRepo.update(id, {
      name: dto.name,
      version: dto.version ?? 1,
      graphJson: this.toGraphJson(dto),
    });
    return this.get(id);
  }

  async remove(id: string) {
    await this.get(id);
    await this.graphRepo.delete(id);
    return { deleted: id };
  }

  /**
   * 执行图：拓扑排序 → 逐节点执行 → 落运行记录与节点级追踪。
   * 引擎只调用 NODE_REGISTRY 中的执行实现，对主平台零侵入。
   */
  async run(id: string, dto: RunWorkflowDto, tenantId?: string | null) {
    const g = await this.get(id, tenantId);
    const effectiveTenant = tenantId ?? dto.tenantId;
    const graphJson = (g.graphJson as any) ?? { nodes: [], edges: [] };
    const run = await this.runRepo.save(
      this.runRepo.create({
        graphId: g.id,
        trigger: dto.trigger,
        tenantId: effectiveTenant,
        status: 'running',
      }),
    );
    const ctx = {
      tenantId: effectiveTenant,
      runId: run.id,
      caller: 'rest',
      services: this.services,
      audit: async (e: AuditEntry) => {
        await this.auditRepo.save(this.auditRepo.create(e));
      },
    };
    try {
      const result = await runDag(
        { nodes: graphJson.nodes ?? [], edges: graphJson.edges ?? [] },
        NODE_REGISTRY,
        ctx,
        async (nodeId, status, input, output, durationMs) => {
          await this.runNodeRepo.save(
            this.runNodeRepo.create({
              runId: run.id,
              nodeId,
              status: status as WfRunNode['status'],
              inputMd: input,
              outputMd: output,
              durationMs,
            }),
          );
        },
      );

      // 把运行过程中产出的 PageSchema 持久化为可渲染页面（取最后一个 page 输出）
      let generatedPageId: string | undefined;
      for (const bag of Object.values(result)) {
        const pg = (bag as any)?.page as PageSchema | undefined;
        if (pg && typeof pg === 'object' && Array.isArray(pg.nodes)) {
          const gp = await this.pageRepo.save(
            this.pageRepo.create({ graphId: g.id, tenantId: effectiveTenant, schemaJson: JSON.stringify(pg) }),
          );
          generatedPageId = gp.id;
        }
      }

      await this.runRepo.update(run.id, { status: 'success', finishedAt: new Date() });
      return { runId: run.id, generatedPageId, result };
    } catch (e: any) {
      await this.runRepo.update(run.id, { status: 'failed', finishedAt: new Date() });
      throw e;
    }
  }

  // ---- 生成的页面（composePage 节点产出，可被渲染端消费）----

  listPages(tenantId?: string | null) {
    return this.pageRepo.find({
      where: tenantId ? { tenantId } : undefined,
      order: { createdAt: 'DESC' },
    });
  }

  async getPage(id: string) {
    const p = await this.pageRepo.findOne({ where: { id } });
    if (!p) throw new NotFoundException(`page ${id} not found`);
    return p;
  }

  async renderPage(id: string): Promise<string> {
    const p = await this.getPage(id);
    const schema = JSON.parse(p.schemaJson) as PageSchema;
    return renderPageToHtml(schema);
  }

  // ---- 商业化运营视图：运行统计 + 审计 ----
  // 租户隔离：携带 tenantId 时仅统计该租户数据。

  async getStats(tenantId?: string | null) {
    const qb = this.runRepo.createQueryBuilder('r');
    const where = tenantId ? 'r.tenantId = :t' : '1=1';
    const total = await qb.where(where, { t: tenantId }).getCount();
    const byStatus = await this.runRepo
      .createQueryBuilder('r')
      .select('r.status', 'status')
      .addSelect('COUNT(*)', 'cnt')
      .where(where, { t: tenantId })
      .groupBy('r.status')
      .getRawMany();
    return { total, byStatus };
  }

  async listAudit(tenantId?: string | null, limit = 50) {
    return this.auditRepo.find({
      where: tenantId ? { tenantId } : undefined,
      order: { createdAt: 'DESC' },
      take: limit,
    });
  }
}
