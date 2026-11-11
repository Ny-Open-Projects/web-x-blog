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

func isLeafNode(n *TreeNode) bool { // 定义判定函数 isLeafNode
	return n != nil && n.Left == nil && n.Right == nil // 返回 元素个数 不等于 nil 且 元素个数.Left 等于 nil 且 元素个数.Right 等于 nil
}

func sumOfLeftLeaves(root *TreeNode) int { // 定义函数/方法 sumOfLeftLeaves
	if root == nil { // 若 根节点 等于 nil
		return 0 // 返回 0
	}
	total := 0                 // 把 0 写入 total :
	stack := []*TreeNode{root} // 把 [] 乘 TreeNode{根节点} 写入 stack :
	for len(stack) > 0 {       // for 长度(栈) 超过 0 {
		n := stack[len(stack)-1]     // 把 栈[长度(栈) 减 1] 写入 n :
		stack = stack[:len(stack)-1] // 把 栈[:长度(栈) 减 1] 写入 栈
		if n.Left != nil {           // 若 元素个数.Left 不等于 nil
			if isLeafNode(n.Left) { // 定义判定函数 isLeafNode
				total += n.Left.Val // 总和累加 元素个数.Left.Val
			} else { // 否则
				stack = append(stack, n.Left) // 把 append(栈, 元素个数.Left) 写入 栈
			}
		}
		if n.Right != nil { // 若 元素个数.Right 不等于 nil
			stack = append(stack, n.Right) // 把 append(栈, 元素个数.Right) 写入 栈
		}
	}
	return total // 返回 总和
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
