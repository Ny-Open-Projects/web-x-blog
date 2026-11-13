// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145084192
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

func sumOfLeftLeaves(root *TreeNode) int { // 定义函数/方法 sumOfLeftLeaves
	leftSum := 0                  // 把 0 写入 leftSum :
	var travese func(n *TreeNode) // var travese func(元素个数 乘 TreeNode)
	travese = func(n *TreeNode) { // 把 func(元素个数 乘 TreeNode) { 写入 travese
		if n == nil { // 若 元素个数 等于 nil
			return // return
		}
		left := n.Left                                            // 把 元素个数.Left 写入 left :
		if left != nil && left.Left == nil && left.Right == nil { // 若 左边界 不等于 nil 且 左边界.Left 等于 nil 且 左边界.Right 等于 nil
			leftSum += left.Val // leftSum累加 左边界.Val
		}
		travese(n.Left)  // travese(元素个数.Left)
		travese(n.Right) // travese(元素个数.Right)
	}
	travese(root)  // travese(根节点)
	return leftSum // 返回 leftSum
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true                     // 把 true 写入 ok :
	if sumOfLeftLeaves(nil) != 0 { // 若 sumOfLeftLeaves(nil) 不等于 0
		ok = false                // 把 false 写入 ok
		fmt.Println("FAIL nil=0") // 打印输出
	}
	root := &TreeNode{Val: 3}            // 把 按位与 TreeNode{Val: 3} 写入 root :
	root.Left = &TreeNode{Val: 9}        // 把 按位与 TreeNode{Val: 9} 写入 root.Left
	root.Right = &TreeNode{Val: 20}      // 把 按位与 TreeNode{Val: 20} 写入 root.Right
	root.Right.Left = &TreeNode{Val: 15} // 把 按位与 TreeNode{Val: 15} 写入 root.Right.Left
	root.Right.Right = &TreeNode{Val: 7} // 把 按位与 TreeNode{Val: 7} 写入 root.Right.Right
	if sumOfLeftLeaves(root) != 24 {     // 若 sumOfLeftLeaves(根节点) 不等于 24
		ok = false                  // 把 false 写入 ok
		fmt.Println("FAIL tree=24") // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
