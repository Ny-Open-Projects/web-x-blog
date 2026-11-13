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

// instanceOf 沿 proto 链查找是否命中 prototype。
func instanceOf(obj, prototype *Proto) bool { // 定义函数/方法 instanceOf
	p := obj       // 把 obj 写入 p :
	for p != nil { // 把 nil { 写入 for p !
		if p == prototype { // 若 节点 等于 prototype
			return true // 返回 true
		}
		p = p.proto // 把 节点.proto 写入 节点
	}
	return false // 返回 false
}

func main() { // 程序入口：跑内嵌自测用例
	objectProto := newProto("Object.prototype", nil) // 把 newProto(「Object.prototype」, nil) 写入 objectProto :
	objectProto.set("a", "aaa")                      // objectProto.set(「数组」, 「数组」)
	functionProto := newProto("Function.prototype", objectProto)
	functionProto.set("b", "bbb") // functionProto.set(「b」, 「b」)

	obj := newProto("obj", objectProto)        // 把 newProto(「obj」, objectProto) 写入 obj :
	funcObj := newProto("func", functionProto) // 把 newProto(「func」, functionProto) 写入 funcObj :

	// obj.get("a") -> aaa
	v, ok := obj.get("a")  // 把 obj 查找 「数组」) 写入 v, ok :
	if !ok || v != "aaa" { // 若 取反 ok 或 值 不等于 「aaa」
		fmt.Println("FAIL get a") // 打印输出
		os.Exit(1)                // os.Exit(1)
	}
	// obj.get("b") -> None (undefined)
	if _, ok := obj.get("b"); ok { // 若 _, ok : 赋值为 obj 查找 「b」); ok
		fmt.Println("FAIL get b should be None") // 打印输出
		os.Exit(1)                               // os.Exit(1)
	}
	// func.get("a") -> aaa
	v, ok = funcObj.get("a") // 把 funcObj 查找 「数组」) 写入 v, ok
	if !ok || v != "aaa" {   // 若 取反 ok 或 值 不等于 「aaa」
		fmt.Println("FAIL func get a") // 打印输出
		os.Exit(1)                     // os.Exit(1)
	}
	// func.get("b") -> bbb
	v, ok = funcObj.get("b") // 把 funcObj 查找 「b」) 写入 v, ok
	if !ok || v != "bbb" {   // 若 取反 ok 或 值 不等于 「bbb」
		fmt.Println("FAIL func get b") // 打印输出
		os.Exit(1)                     // os.Exit(1)
	}
	// instanceOf(func, objectProto) -> True
	if !instanceOf(funcObj, objectProto) { // 若 取反 instanceOf(funcObj, objectProto
		fmt.Println("FAIL instanceOf") // 打印输出
		os.Exit(1)                     // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
