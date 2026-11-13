// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// Proto 模拟 JS 对象：拥有自己的属性 dict 与指向父原型的 proto。
type Proto struct { // 定义类型
	name  string            // name string
	props map[string]string // props 映射表[string]string
	proto *Proto            // proto 乘 Proto
}

func newProto(name string, parent *Proto) *Proto { // 定义函数/方法 newProto
	return &Proto{name: name, props: map[string]string{}, proto: parent}
}

// instanceOf 模拟 JS 的 instanceof：沿 proto 链寻找是否命中 prototype。
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
	functionProto := newProto("Function.prototype", objectProto)
	arrayProto := newProto("Array.prototype", objectProto) // 把 newProto(「Array.prototype」, objectProto) 写入 arrayProto :

	obj := newProto("obj", objectProto)        // 把 newProto(「obj」, objectProto) 写入 obj :
	funcObj := newProto("func", functionProto) // 把 newProto(「func」, functionProto) 写入 funcObj :
	arr := newProto("arr", arrayProto)         // 把 newProto(「数组」, arrayProto) 写入 arr :

	checks := []bool{ // 把 []bool{ 写入 checks :
		instanceOf(obj, objectProto),
		instanceOf(funcObj, functionProto),
		instanceOf(funcObj, objectProto),
		instanceOf(arr, arrayProto),
		instanceOf(arr, objectProto),
	}
	for _, c := range checks { // 同时取 _ 与 字符 遍历
		if !c { // 若 取反 字符
			fmt.Println("FAIL instanceOf") // 打印输出
			os.Exit(1)                     // os.Exit(1)
		}
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
