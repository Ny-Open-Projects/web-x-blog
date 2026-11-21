import { Injectable, NotFoundException, ForbiddenException } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { PageDef } from './entities/page-def.entity';
import { PageSchema } from '@lowcode/shared';
import { renderPageToHtml } from '../workflow/engine/render-page';

export interface CreatePageInput {
  name: string;
  schema: PageSchema;
  tenantId?: string | null;
}

export interface UpdatePageInput {
  name?: string;
  schema?: PageSchema;
}

@Injectable()
export class PageBuilderService {
  constructor(
    @InjectRepository(PageDef) private readonly repo: Repository<PageDef>,
  ) {}

  async create(input: CreatePageInput): Promise<PageDef> {
    const e = this.repo.create({
      name: input.name,
      schemaJson: JSON.stringify(input.schema),
      tenantId: input.tenantId ?? null,
    });
    return this.repo.save(e);
  }

  async update(id: string, input: UpdatePageInput, tenantId?: string | null): Promise<PageDef> {
    const e = await this.get(id, tenantId);
    if (input.name !== undefined) e.name = input.name;
    if (input.schema !== undefined) e.schemaJson = JSON.stringify(input.schema);
    return this.repo.save(e);
  }

  list(tenantId?: string | null): Promise<PageDef[]> {
    const where = tenantId ? { tenantId } : {};
    return this.repo.find({ where, order: { createdAt: 'DESC' } });
  }

  async get(id: string, tenantId?: string | null): Promise<PageDef> {
    const e = await this.repo.findOne({ where: { id } });
    if (!e) throw new NotFoundException(`page ${id} not found`);
    if (tenantId && e.tenantId && e.tenantId !== tenantId) {
      throw new ForbiddenException('跨租户访问被拒绝');
    }
    return e;
  }

  async render(id: string, tenantId?: string | null): Promise<string> {
    const e = await this.get(id, tenantId);
    const schema = JSON.parse(e.schemaJson) as PageSchema;
    return renderPageToHtml(schema);
  }
}
