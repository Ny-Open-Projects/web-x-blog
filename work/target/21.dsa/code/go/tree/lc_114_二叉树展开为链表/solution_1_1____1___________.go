// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145007192
package main // 引入依赖

import (
	"fmt"
	"os"
	"reflect"
) // 引入依赖

type TreeNode struct { // 定义类型
	Val   int       // Val int
	Left  *TreeNode // Left 乘 TreeNode
	Right *TreeNode // Right 乘 TreeNode
}

func flatten(root *TreeNode) { // 定义函数/方法 flatten
	var prev *TreeNode           // var 前一个 乘 TreeNode
	var dfs func(node *TreeNode) // var dfs func(节点 乘 TreeNode)
	dfs = func(node *TreeNode) { // 把 func(节点 乘 TreeNode) { 写入 dfs
		if node == nil { // 若 节点 等于 nil
			return // return
		}
		dfs(node.Right)   // dfs(节点.Right)
		dfs(node.Left)    // dfs(节点.Left)
		node.Right = prev // 把 前一个 写入 node.Right
		node.Left = nil   // 把 nil 写入 node.Left
		prev = node       // 把 节点 写入 前一个
	}
	dfs(root) // dfs(根节点)
}

func toList(root *TreeNode) []int { // 定义函数/方法 toList
	res := []int{}    // 把 []int{} 写入 res :
	for root != nil { // 把 nil { 写入 for root !
		res = append(res, root.Val) // 把 append(结果, 根节点.Val) 写入 结果
		root = root.Right           // 把 根节点.Right 写入 根节点
	}
	return res // 返回 结果
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
	root := buildTree([]int{1, 2, 5, 3, 4, -1, 6}) // 把 buildTree([]int{1, 2, 5, 3, 4, 减 1, 6}) 写入 root :
	flatten(root)                                  // flatten(根节点)
	got := toList(root)                            // 把 toList(根节点) 写入 got :
	want := []int{1, 2, 3, 4, 5, 6}                // 把 []int{1, 2, 3, 4, 5, 6} 写入 want :
	if !reflect.DeepEqual(got, want) {             // 若 取反 reflect.DeepEqual(got, want
		fmt.Printf("FAIL got=%v want=%v\n", got, want) // 打印输出
		os.Exit(1)                                     // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
