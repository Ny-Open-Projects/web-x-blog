import { BadRequestException, Injectable } from '@nestjs/common';
import { AliOssModule } from 'src/utils/modules/ali-oss.module';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { Resources } from './entities/resources.entity';
import type { UploadType } from '@lowcode/share';

@Injectable()
export class ResourcesService {
  constructor(
    private readonly alioss: AliOssModule,
    @InjectRepository(Resources)
    private readonly resourcesRespository: Repository<Resources>,
  ) {}

  /**
   * 资源上传服务层
   */
  async upload(
    file: Express.Multer.File,
    type: UploadType,
    account_id: number,
  ) {
    let url = '';
    try {
      url = await this.alioss.uploadToAliOss(file);
    } catch (error) {
      return error;
    }

    await this.resourcesRespository.save({
      url,
      type,
      account_id,
      name: Buffer.from(file.originalname, 'latin1').toString('utf8'), // 解决中文名乱码问题
    });

    return { msg: '上传成功' };
  }

  /**
   * 删除资源服务层
   */
  async deleteResource(id: number, account_id: number) {
    // 查询数据库当前的资源是否存在
    const resources = await this.resourcesRespository.findOneBy({ id });
    if (!resources) throw new BadRequestException('资源不存在');

    await this.alioss.deleteFromAliOss(resources.url);
    await this.resourcesRespository.delete({ id, account_id });

    return { msg: '删除成功' };
  }

  /**
   * 资源获取的服务层
   */
  async getResources(type: UploadType, account_id: number) {
    return await this.resourcesRespository.findBy({ type, account_id });
  }
}
