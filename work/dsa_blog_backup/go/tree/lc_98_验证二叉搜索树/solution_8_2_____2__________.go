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
	res := []int{}            // 把 []int{} 写入 res :
	var dfs func(n *TreeNode) // var dfs func(元素个数 乘 TreeNode)
	dfs = func(n *TreeNode) { // 把 func(元素个数 乘 TreeNode) { 写入 dfs
		if n == nil { // 若 元素个数 等于 nil
			return // return
		}
		dfs(n.Left)              // dfs(元素个数.Left)
		res = append(res, n.Val) // 把 append(结果, 元素个数.Val) 写入 结果
		dfs(n.Right)             // dfs(元素个数.Right)
	}
	dfs(root)                         // dfs(根节点)
	for i := 0; i < len(res)-1; i++ { // 让 下标 i 从 0 开始计数
		if res[i] >= res[i+1] { // 若 结果[下标 i] 不低于 结果[下标 i 加 1]
			return false // 返回 false
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
