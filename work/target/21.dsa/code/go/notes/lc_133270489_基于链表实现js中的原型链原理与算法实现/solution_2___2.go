// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// Proto 模拟 JS 对象：属性查找沿原型链向上进行。
type Proto struct { // 定义类型
	name  string            // name string
	props map[string]string // props 映射表[string]string
	proto *Proto            // proto 乘 Proto
}

func newProto(name string, parent *Proto) *Proto { // 定义函数/方法 newProto
	return &Proto{name: name, props: map[string]string{}, proto: parent}
}

func (p *Proto) set(key, value string) { // 定义函数/方法 set
	p.props[key] = value // 把 value 写入 p.props[key]
}

// get 沿原型链查找属性，命中返回 (value,true)，否则 ("",false)。
func (p *Proto) get(key string) (string, bool) { // 定义函数/方法 get
	cur := p         // 把 节点 写入 cur :
	for cur != nil { // 把 nil { 写入 for cur !
		if v, ok := cur.props[key]; ok { // 若 值, ok : 赋值为 当前值.props[key]; ok
			return v, true // 返回 值, true
		}
		cur = cur.proto // 把 当前值.proto 写入 当前值
	}
	return "", false // 返回 「」, false
}

func main() { // 程序入口：跑内嵌自测用例
	objectProto := newProto("Object.prototype", nil) // 把 newProto(「Object.prototype」, nil) 写入 objectProto :
	objectProto.set("x", "x")                        // objectProto.set(「x」, 「x」)
	functionProto := newProto("Function.prototype", objectProto)
	functionProto.set("y", "y")                            // functionProto.set(「y」, 「y」)
	arrayProto := newProto("Array.prototype", objectProto) // 把 newProto(「Array.prototype」, objectProto) 写入 arrayProto :
	arrayProto.set("z", "z")                               // arrayProto.set(「z」, 「z」)

	obj := newProto("obj", objectProto)        // 把 newProto(「obj」, objectProto) 写入 obj :
	funcObj := newProto("func", functionProto) // 把 newProto(「func」, functionProto) 写入 funcObj :
	arr := newProto("arr", arrayProto)         // 把 newProto(「数组」, arrayProto) 写入 arr :

	if v, ok := obj.get("x"); !ok || v != "x" { // 若 值, ok : 赋值为 obj 查找 「x」); 取反 ok 或 值 不等于 「x」
		fmt.Println("FAIL get x") // 打印输出
		os.Exit(1)                // os.Exit(1)
	}
	if v, ok := funcObj.get("y"); !ok || v != "y" { // 若 值, ok : 赋值为 funcObj 查找 「y」); 取反 ok 或 值 不等于 「y」
		fmt.Println("FAIL get y") // 打印输出
		os.Exit(1)                // os.Exit(1)
	}
	if v, ok := arr.get("z"); !ok || v != "z" { // 若 值, ok : 赋值为 数组 查找 「z」); 取反 ok 或 值 不等于 「z」
		fmt.Println("FAIL get z") // 打印输出
		os.Exit(1)                // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
