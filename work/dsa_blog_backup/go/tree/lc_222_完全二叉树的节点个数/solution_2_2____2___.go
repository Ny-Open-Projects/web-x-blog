// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145052590
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

func countNodes(root *TreeNode) int { // 定义函数/方法 countNodes
	if root == nil { // 若 根节点 等于 nil
		return 0 // 返回 0
	}
	return countNodes(root.Left) + countNodes(root.Right) + 1 // 返回 countNodes(根节点.Left) 加 countNodes(根节点.Right) 加 1
}

func main() { // 程序入口：跑内嵌自测用例
	root := &TreeNode{Val: 1}           // 把 按位与 TreeNode{Val: 1} 写入 root :
	root.Left = &TreeNode{Val: 2}       // 把 按位与 TreeNode{Val: 2} 写入 root.Left
	root.Right = &TreeNode{Val: 3}      // 把 按位与 TreeNode{Val: 3} 写入 root.Right
	root.Left.Left = &TreeNode{Val: 4}  // 把 按位与 TreeNode{Val: 4} 写入 root.Left.Left
	root.Left.Right = &TreeNode{Val: 5} // 把 按位与 TreeNode{Val: 5} 写入 root.Left.Right
	root.Right.Left = &TreeNode{Val: 6} // 把 按位与 TreeNode{Val: 6} 写入 root.Right.Left
	ok := true                          // 把 true 写入 ok :
	if countNodes(root) != 6 {          // 若 countNodes(根节点) 不等于 6
		ok = false                 // 把 false 写入 ok
		fmt.Println("FAIL tree=6") // 打印输出
	}
	if countNodes(nil) != 0 { // 若 countNodes(nil) 不等于 0
		ok = false                // 把 false 写入 ok
		fmt.Println("FAIL nil=0") // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
