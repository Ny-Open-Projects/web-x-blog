from string import Template

WELCOME = Template("Hello $name, your order ${order_id} is $status")

if __name__ == "__main__":
    print(WELCOME.substitute(name="Alice", order_id=7, status="shipped"))
    print(WELCOME.safe_substitute(name="Bob"))    # 缺键:保留 $order_id 原样

    try:
        WELCOME.substitute(name="Alice")
    except KeyError as e:
        print("missing key:", e)

    print(Template("${name}s book").substitute(name="Alice"))   # 边界定界
    user_input = "Robert'); DROP TABLE users;--"
    print("template does not execute:", Template("msg: $x").substitute(x=user_input))
