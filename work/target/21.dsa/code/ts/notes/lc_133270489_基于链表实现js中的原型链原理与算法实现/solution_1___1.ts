// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  class Proto {
    // 定义类型
    name: string; // name: string;
    props: { [k: string]: string }; // props: { [下标 k: string]: string };
    proto: Proto | null; // proto: Proto 按位或 null;
    constructor(name: string, parent: Proto | null = null) {
      // 把 null) { 写入 constructor(name: string, parent: Proto | null
      this.name = name; // 把 name; 写入 this.name
      this.props = {}; // 把 {}; 写入 this.props
      this.proto = parent; // 把 parent; 写入 this.proto
    }
    set(key: string, value: string): void {
      this.props[key] = value;
    }
  }
  function instanceOf(obj: Proto, prototype: Proto): boolean {
    // 定义函数/方法 instanceOf
    let p: Proto | null = obj; // 把 obj; 写入 let p: Proto | null
    while (p !== null) {
      // 循环，直到不满足「节点 不等于 null」
      if (p === prototype) return true; // 若 节点 全等于 prototype，直接返回 true
      p = p.proto; // 把 节点.proto 存入 节点
    }
    return false; // 返回 false
  }
  const object_proto = new Proto('Object.prototype', null); // 把 new Proto(「Object.prototype」, null) 存入 object_proto
  const function_proto = new Proto('Function.prototype', object_proto);
  const array_proto = new Proto('Array.prototype', object_proto); // 把 new Proto(「Array.prototype」, object_proto) 存入 array_proto
  const obj = new Proto('obj', object_proto); // 把 new Proto(「obj」, object_proto) 存入 obj
  const func = new Proto('func', function_proto); // 把 new Proto(「func」, function_proto) 存入 func
  const arr = new Proto('arr', array_proto); // 把 new Proto(「数组」, array_proto) 存入 数组
  const cases: { got: boolean; want: boolean }[] = [
    { got: instanceOf(obj, object_proto), want: true },
    { got: instanceOf(func, function_proto), want: true },
    { got: instanceOf(func, object_proto), want: true },
    { got: instanceOf(arr, array_proto), want: true },
    { got: instanceOf(arr, object_proto), want: true },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    if (c.got !== c.want) {
      fail = true;
      console.log('FAIL got', c.got, 'want', c.want);
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
