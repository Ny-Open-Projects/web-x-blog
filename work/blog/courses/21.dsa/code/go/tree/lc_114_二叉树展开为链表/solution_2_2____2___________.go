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

func flatten(root *TreeNode) *TreeNode { // 定义函数/方法 flatten
	list := []*TreeNode{}               // 把 [] 乘 TreeNode{} 写入 list :
	stack := []*TreeNode{}              // 把 [] 乘 TreeNode{} 写入 stack :
	node := root                        // 把 根节点 写入 node :
	for node != nil || len(stack) > 0 { // 把 nil 或 长度(栈) 超过 0 { 写入 for node !
		for node != nil { // 把 nil { 写入 for node !
			list = append(list, node)   // 把 append(列表, 节点) 写入 列表
			stack = append(stack, node) // 把 append(栈, 节点) 写入 栈
			node = node.Left            // 把 节点.Left 写入 节点
		}
		node = stack[len(stack)-1]   // 把 栈[长度(栈) 减 1] 写入 节点
		stack = stack[:len(stack)-1] // 把 栈[:长度(栈) 减 1] 写入 栈
		node = node.Right            // 把 节点.Right 写入 节点
	}
	size := len(list)           // 把 长度(列表) 写入 size :
	for i := 1; i < size; i++ { // 让 下标 i 从 1 开始计数
		prev := list[i-1] // 把 列表[下标 i 减 1] 写入 prev :
		curr := list[i]   // 把 列表[下标 i] 写入 curr :
		prev.Left = nil   // 把 nil 写入 prev.Left
		prev.Right = curr // 把 当前值 写入 prev.Right
	}
	if size > 0 { // 若 大小 超过 0
		return list[0] // 返回 列表[0]
	}
	return nil // 返回 nil
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
