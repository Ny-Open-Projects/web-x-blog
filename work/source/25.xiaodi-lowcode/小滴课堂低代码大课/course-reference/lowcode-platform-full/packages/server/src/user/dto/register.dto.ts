import { IsString, IsNotEmpty } from 'class-validator';

export class RegisterDto {
  @IsNotEmpty({ message: 'phone限制不为空!' })
  @IsString({ message: 'phone限制为string类型!' })
  phone: string;

  @IsNotEmpty({ message: 'sendCode限制不为空!' })
  @IsString({ message: 'sendCode限制为string类型!' })
  sendCode: string;

  @IsNotEmpty({ message: 'password限制不为空!' })
  @IsString({ message: 'password限制为string类型!' })
  password: string;

  @IsNotEmpty({ message: 'confirm限制不为空!' })
  @IsString({ message: 'confirm限制为string类型!' })
  confirm: string;
}
