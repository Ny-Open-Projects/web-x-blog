import { Injectable, UnauthorizedException } from '@nestjs/common';
import { PassportStrategy } from '@nestjs/passport';
import type { StrategyOptions } from 'passport-jwt';
import { ExtractJwt, Strategy } from 'passport-jwt';
import { Repository } from 'typeorm';
import { InjectRepository } from '@nestjs/typeorm';
import { jwtConfig } from 'config';
import { User } from '../user/entities/user.entity';

@Injectable()
export class JWTstrategy extends PassportStrategy(Strategy, 'jwt') {
  constructor(
    @InjectRepository(User) private readonly userRepository: Repository<User>,
  ) {
    super({
      secretOrKey: jwtConfig.secret,
      jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
    } as StrategyOptions);
  }
  /**
   * 验证令牌是否有效
   * @returns 当令牌有效时，返回当前用户的属性集合（除密码之外）
   * @throws 当令牌无效时，抛出异常
   */
  async validate(data: { id: number; iat: number; exp: number }) {
    if (!data) throw new UnauthorizedException('请先登录');

    if (data.exp - data.iat <= 0)
      throw new UnauthorizedException('登录已过期，请重新登陆');

    const user = await this.userRepository.findOne({ where: { id: data.id } });
    if (!user) throw new UnauthorizedException('出现错误，请重新登录');

    return { ...user, password: '' };
  }
}
