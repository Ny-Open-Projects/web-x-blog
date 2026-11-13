// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145089162
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

func diameterOfBinaryTree(root *TreeNode) int { // 定义函数/方法 diameterOfBinaryTree
	ans := 0                           // 把 0 写入 ans :
	var depth func(node *TreeNode) int // var 深度 func(节点 乘 TreeNode) int
	depth = func(node *TreeNode) int { // 把 func(节点 乘 TreeNode) int { 写入 深度
		if node == nil { // 若 节点 等于 nil
			return 0 // 返回 0
		}
		leftDepth := depth(node.Left)   // 把 深度(节点.Left) 写入 leftDepth :
		rightDepth := depth(node.Right) // 把 深度(节点.Right) 写入 rightDepth :
		if leftDepth+rightDepth > ans { // 若 leftDepth 加 rightDepth 超过 答案
			ans = leftDepth + rightDepth // 把 leftDepth 加 rightDepth 写入 答案
		}
		if leftDepth > rightDepth { // 若 leftDepth 超过 rightDepth
			return leftDepth + 1 // 返回 leftDepth 加 1
		}
		return rightDepth + 1 // 返回 rightDepth 加 1
	}
	depth(root) // 深度(根节点)
	return ans  // 返回 答案
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true                          // 把 true 写入 ok :
	if diameterOfBinaryTree(nil) != 0 { // 若 diameterOfBinaryTree(nil) 不等于 0
		ok = false                // 把 false 写入 ok
		fmt.Println("FAIL nil=0") // 打印输出
	}
	root := &TreeNode{Val: 1, Left: &TreeNode{Val: 2, Left: &TreeNode{Val: 4}, Right: &TreeNode{Val: 5}}, Right: &TreeNode{Val: 3}}
	if diameterOfBinaryTree(root) != 3 { // 若 diameterOfBinaryTree(根节点) 不等于 3
		ok = false                 // 把 false 写入 ok
		fmt.Println("FAIL tree=3") // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
