// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130907819
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

func hasPathSum(root *TreeNode, targetSum int) bool { // 定义函数/方法 hasPathSum
	if root == nil { // 若 根节点 等于 nil
		return false // 返回 false
	}
	if root.Left == nil && root.Right == nil { // 若 根节点.Left 等于 nil 且 根节点.Right 等于 nil
		return root.Val == targetSum // 返回 根节点.Val 等于 targetSum
	}
	return hasPathSum(root.Left, targetSum-root.Val) || hasPathSum(root.Right, targetSum-root.Val) // 定义函数/方法 hasPathSum
}

func build112() *TreeNode { // 定义函数/方法 build112
	n5 := &TreeNode{Val: 5}   // 把 按位与 TreeNode{Val: 5} 写入 n5 :
	n4 := &TreeNode{Val: 4}   // 把 按位与 TreeNode{Val: 4} 写入 n4 :
	n8 := &TreeNode{Val: 8}   // 把 按位与 TreeNode{Val: 8} 写入 n8 :
	n11 := &TreeNode{Val: 11} // 把 按位与 TreeNode{Val: 11} 写入 n11 :
	n7 := &TreeNode{Val: 7}   // 把 按位与 TreeNode{Val: 7} 写入 n7 :
	n2 := &TreeNode{Val: 2}   // 把 按位与 TreeNode{Val: 2} 写入 n2 :
	n13 := &TreeNode{Val: 13} // 把 按位与 TreeNode{Val: 13} 写入 n13 :
	n41 := &TreeNode{Val: 4}  // 把 按位与 TreeNode{Val: 4} 写入 n41 :
	n1 := &TreeNode{Val: 1}   // 把 按位与 TreeNode{Val: 1} 写入 n1 :
	n5.Left = n4              // 把 n4 写入 n5.Left
	n5.Right = n8             // 把 n8 写入 n5.Right
	n4.Left = n11             // 把 n11 写入 n4.Left
	n11.Left = n7             // 把 n7 写入 n11.Left
	n11.Right = n2            // 把 n2 写入 n11.Right
	n8.Left = n13             // 把 n13 写入 n8.Left
	n8.Right = n41            // 把 n41 写入 n8.Right
	n41.Right = n1            // 把 n1 写入 n41.Right
	return n5                 // 返回 n5
}

func main() { // 程序入口：跑内嵌自测用例
	root := build112()         // 把 build112() 写入 root :
	ok := true                 // 把 true 写入 ok :
	if !hasPathSum(root, 22) { // 若 取反 hasPathSum(根节点, 22
		ok = false                              // 把 false 写入 ok
		fmt.Println("FAIL hasPathSum(root,22)") // 打印输出
	}
	if hasPathSum(nil, 0) { // 定义函数/方法 hasPathSum
		ok = false                            // 把 false 写入 ok
		fmt.Println("FAIL hasPathSum(nil,0)") // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
