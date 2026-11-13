// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145083302
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

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode { // 定义函数/方法 lowestCommonAncestor
	if root == nil || root == p || root == q { // 若 根节点 等于 nil 或 根节点 等于 节点 或 根节点 等于 节点
		return root // 返回 根节点
	}
	left := lowestCommonAncestor(root.Left, p, q)   // 把 lowestCommonAncestor(根节点.Left, 节点, 节点) 写入 left :
	right := lowestCommonAncestor(root.Right, p, q) // 把 lowestCommonAncestor(根节点.Right, 节点, 节点) 写入 right :
	if left != nil && right != nil {                // 若 左边界 不等于 nil 且 右边界 不等于 nil
		return root // 返回 根节点
	}
	if left != nil { // 若 左边界 不等于 nil
		return left // 返回 左边界
	}
	return right // 返回 右边界
}

func main() { // 程序入口：跑内嵌自测用例
	root := &TreeNode{Val: 3}                 // 把 按位与 TreeNode{Val: 3} 写入 root :
	root.Left = &TreeNode{Val: 5}             // 把 按位与 TreeNode{Val: 5} 写入 root.Left
	root.Right = &TreeNode{Val: 1}            // 把 按位与 TreeNode{Val: 1} 写入 root.Right
	root.Left.Left = &TreeNode{Val: 6}        // 把 按位与 TreeNode{Val: 6} 写入 root.Left.Left
	root.Left.Right = &TreeNode{Val: 2}       // 把 按位与 TreeNode{Val: 2} 写入 root.Left.Right
	root.Right.Left = &TreeNode{Val: 0}       // 把 按位与 TreeNode{Val: 0} 写入 root.Right.Left
	root.Right.Right = &TreeNode{Val: 8}      // 把 按位与 TreeNode{Val: 8} 写入 root.Right.Right
	root.Left.Right.Left = &TreeNode{Val: 7}  // 把 按位与 TreeNode{Val: 7} 写入 root.Left.Right.Left
	root.Left.Right.Right = &TreeNode{Val: 4} // 把 按位与 TreeNode{Val: 4} 写入 root.Left.Right.Right
	p := root.Left                            // 把 根节点.Left 写入 p :
	q := root.Right                           // 把 根节点.Right 写入 q :
	lca := lowestCommonAncestor(root, p, q)   // 把 lowestCommonAncestor(根节点, 节点, 节点) 写入 lca :
	if lca == nil || lca.Val != 3 {           // 若 lca 等于 nil 或 lca.Val 不等于 3
		fmt.Printf("FAIL got=%v want=3\n", lca) // 打印输出
		os.Exit(1)                              // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
