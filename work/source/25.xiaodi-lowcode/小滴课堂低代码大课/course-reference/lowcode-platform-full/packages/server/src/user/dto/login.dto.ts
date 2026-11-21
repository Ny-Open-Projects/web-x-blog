import { IsString, IsNotEmpty } from 'class-validator';

export class PasswordLoginDto {
  @IsNotEmpty({ message: 'phone限制不为空!' })
  @IsString({ message: 'phone限制为string类型!' })
  phone: string;

  @IsNotEmpty({ message: 'password限制不为空!' })
  @IsString({ message: 'password限制为string类型!' })
  password: string;
}

export class PhoneLoginDto {
  @IsNotEmpty({ message: 'phone限制不为空!' })
  @IsString({ message: 'phone限制为string类型!' })
  phone: string;

  @IsNotEmpty({ message: 'sendCode限制不为空!' })
  @IsString({ message: 'sendCode限制为string类型!' })
  sendCode: string;
}
