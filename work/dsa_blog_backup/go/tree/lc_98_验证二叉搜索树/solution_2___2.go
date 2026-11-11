// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/131631290
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

func isValidBST(root *TreeNode) bool { // 定义判定函数 isValidBST
	if root == nil { // 若 根节点 等于 nil
		return true // 返回 true
	}
	type tup struct { // 定义类型
		node *TreeNode // 节点 乘 TreeNode
		low  *int      // low 乘 int
		high *int      // high 乘 int
	}
	stack := []tup{{root, nil, nil}} // 把 []tup{{根节点, nil, nil}} 写入 stack :
	for len(stack) > 0 {             // for 长度(栈) 超过 0 {
		t := stack[len(stack)-1]     // 把 栈[长度(栈) 减 1] 写入 t :
		stack = stack[:len(stack)-1] // 把 栈[:长度(栈) 减 1] 写入 栈
		if (t.low != nil && t.node.Val <= *t.low) || (t.high != nil && t.node.Val >= *t.high) {
			return false // 返回 false
		}
		if t.node.Right != nil { // 若 另一字符串.节点.Right 不等于 nil
			stack = append(stack, tup{t.node.Right, &t.node.Val, t.high})
		}
		if t.node.Left != nil { // 若 另一字符串.节点.Left 不等于 nil
			stack = append(stack, tup{t.node.Left, t.low, &t.node.Val})
		}
	}
	return true // 返回 true
}

func buildTree(vals []int) *TreeNode { // 定义函数/方法 buildTree
	if len(vals) == 0 || vals[0] == -1 { // 若 长度(vals) 等于 0 或 vals[0] 等于 减 1
		return nil // 返回 nil
	}
	root := &TreeNode{Val: vals[0]} // 把 按位与 TreeNode{Val: vals[0]} 写入 root :
	q := []*TreeNode{root}          // 把 [] 乘 TreeNode{根节点} 写入 q :
	i := 1                          // 把 1 写入 i :
	for i < len(vals) {             // for 下标 i 小于 长度(vals) {
		node := q[0]                        // 把 节点[0] 写入 node :
		q = q[1:]                           // 把 节点[1:] 写入 节点
		if i < len(vals) && vals[i] != -1 { // 若 下标 i 小于 长度(vals) 且 vals[下标 i] 不等于 减 1
			node.Left = &TreeNode{Val: vals[i]} // 把 按位与 TreeNode{Val: vals[下标 i]} 写入 node.Left
			q = append(q, node.Left)            // 把 append(节点, 节点.Left) 写入 节点
		}
		i++                                 // 下标 i 加一
		if i < len(vals) && vals[i] != -1 { // 若 下标 i 小于 长度(vals) 且 vals[下标 i] 不等于 减 1
			node.Right = &TreeNode{Val: vals[i]} // 把 按位与 TreeNode{Val: vals[下标 i]} 写入 node.Right
			q = append(q, node.Right)            // 把 append(节点, 节点.Right) 写入 节点
		}
		i++ // 下标 i 加一
	}
	return root // 返回 根节点
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true                                  // 把 true 写入 ok :
	if !isValidBST(buildTree([]int{2, 1, 3})) { // 若 取反 isValidBST(buildTree([]int{2, 1, 3}
		ok = false                    // 把 false 写入 ok
		fmt.Println("FAIL valid BST") // 打印输出
	}
	if isValidBST(buildTree([]int{5, 1, 4, -1, -1, 3, 6})) { // 定义判定函数 isValidBST
		ok = false                                        // 把 false 写入 ok
		fmt.Println("FAIL invalid BST detected as valid") // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
