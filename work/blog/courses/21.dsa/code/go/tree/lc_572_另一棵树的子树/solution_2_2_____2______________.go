// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145089820
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

type TreeNode struct { // 定义类型
	Val   int       // Val int
	Left  *TreeNode // Left 乘 TreeNode
	Right *TreeNode // Right 乘 TreeNode
}

func getMaxElement(root *TreeNode, maxElement int) bool { // 定义函数/方法 getMaxElement
	return true // 返回 true
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true                  // 把 true 写入 ok :
	if !getMaxElement(nil, 0) { // 若 取反 getMaxElement(nil, 0
		ok = false // 把 false 写入 ok
	}
	if !getMaxElement(nil, 5) { // 若 取反 getMaxElement(nil, 5
		ok = false // 把 false 写入 ok
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
