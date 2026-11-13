// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// JsObject 模拟 JS 对象：prototype 类似构造函数的 .prototype，proto 即 __proto__。
type JsObject struct { // 定义类型
	prototype *JsObject // prototype 乘 JsObject
	proto     *JsObject // proto 乘 JsObject
}

// instanceOf 沿 __proto__ 链查找是否命中 B.prototype。
func instanceOf(a, b *JsObject) bool { // 定义函数/方法 instanceOf
	p := a         // 把 数组 写入 p :
	for p != nil { // 把 nil { 写入 for p !
		if p == b.prototype { // 若 节点 等于 b.prototype
			return true // 返回 true
		}
		p = p.proto // 把 节点.proto 写入 节点
	}
	return false // 返回 false
}

func main() { // 程序入口：跑内嵌自测用例
	// 忠实复刻参考：print(instanceOf(None, None)) -> False
	if instanceOf(nil, nil) { // 定义函数/方法 instanceOf
		fmt.Println("FAIL expected False") // 打印输出
		os.Exit(1)                         // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
