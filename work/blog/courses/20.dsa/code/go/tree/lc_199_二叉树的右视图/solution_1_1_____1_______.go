// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145030731
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

type TreeNode struct {
	Val         int
	Left, Right *TreeNode
} // 定义类型

func buildTree(vals []int, nullVal int) *TreeNode { // 定义函数/方法 buildTree
	if len(vals) == 0 || vals[0] == nullVal {
		return nil
	} // 若 长度(vals) 等于 0 或 vals[0] 等于 nullVal { return nil }
	root := &TreeNode{Val: vals[0]}     // 把 按位与 TreeNode{Val: vals[0]} 写入 root :
	q := []*TreeNode{root}              // 把 [] 乘 TreeNode{根节点} 写入 q :
	idx := 1                            // 把 1 写入 idx :
	for len(q) > 0 && idx < len(vals) { // 定义函数/方法 len
		node := q[0]
		q = q[1:]                                    // 把 节点[0]; 节点 赋值为 节点[1:] 写入 node :
		if idx < len(vals) && vals[idx] != nullVal { // 若 idx 小于 长度(vals) 且 vals[idx] 不等于 nullVal
			node.Left = &TreeNode{Val: vals[idx]}
			q = append(q, node.Left)
		}
		idx++                                        // idx 加一
		if idx < len(vals) && vals[idx] != nullVal { // 若 idx 小于 长度(vals) 且 vals[idx] 不等于 nullVal
			node.Right = &TreeNode{Val: vals[idx]}
			q = append(q, node.Right)
		}
		idx++ // idx 加一
	}
	return root // 返回 根节点
}

// 忠实翻译 python/tree/lc_199_二叉树的右视图/solution_1_1_____1_______.py.py
func rightSideView(root *TreeNode) []int { // 定义函数/方法 rightSideView
	if root == nil {
		return []int{}
	} // 若 根节点 等于 nil { return []int{} }
	result := []int{}          // 把 []int{} 写入 result :
	queue := []*TreeNode{root} // 把 [] 乘 TreeNode{根节点} 写入 queue :
	for len(queue) > 0 {       // for 长度(队列) 超过 0 {
		levelSize := len(queue)          // 把 长度(队列) 写入 levelSize :
		for i := 0; i < levelSize; i++ { // 让 下标 i 从 0 开始计数
			node := queue[0]
			queue = queue[1:] // 把 队列[0]; 队列 赋值为 队列[1:] 写入 node :
			if i == levelSize-1 {
				result = append(result, node.Val)
			} // 若 下标 i 等于 levelSize 减 1 { 结果 赋值为 append(结果, 节点.Val) }
			if node.Left != nil {
				queue = append(queue, node.Left)
			} // 若 节点.Left 不等于 nil { 队列 赋值为 append(队列, 节点.Left) }
			if node.Right != nil {
				queue = append(queue, node.Right)
			} // 若 节点.Right 不等于 nil { 队列 赋值为 append(队列, 节点.Right) }
		}
	}
	return result // 返回 结果
}

func eqIntSlice(a, b []int) bool { return reflect.DeepEqual(a, b) } // 定义函数/方法 eqIntSlice

func main() { // 程序入口：跑内嵌自测用例
	nullVal := 1000001 // 把 1000001 写入 nullVal :
	type caseT struct {
		vals []int
		want []int
	} // 定义类型
	cases := []caseT{ // 把 []caseT{ 写入 cases :
		{[]int{1, 2, 3, nullVal, 5, nullVal, 4}, []int{1, 3, 4}},
		{[]int{1}, []int{1}},
		{[]int{}, []int{}},
		{[]int{1, 2, 3, 4, nullVal, nullVal, 5}, []int{1, 3, 5}},
		{[]int{1, 2, nullVal, 3, nullVal, 4, nullVal}, []int{1, 2, 3, 4}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		root := buildTree(c.vals, nullVal) // 把 buildTree(字符.vals, nullVal) 写入 root :
		got := rightSideView(root)         // 把 rightSideView(根节点) 写入 got :
		if !eqIntSlice(got, c.want) {      // 若 取反 eqIntSlice(got, 字符.want
			ok = false                                                             // 把 false 写入 ok
			fmt.Printf("FAIL rightSideView(%v)=%v want %v\n", c.vals, got, c.want) // 打印输出
		}
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
