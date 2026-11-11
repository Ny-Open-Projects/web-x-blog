// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130877211
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

type TreeNode struct { // 定义类型
	Val   int       // Val int
	Left  *TreeNode // Left 乘 TreeNode
	Right *TreeNode // Right 乘 TreeNode
}

func buildTree(vals []interface{}) *TreeNode { // 定义函数/方法 buildTree
	if len(vals) == 0 || vals[0] == nil { // 若 长度(vals) 等于 0 或 vals[0] 等于 nil
		return nil // 返回 nil
	}
	root := &TreeNode{Val: vals[0].(int)} // 把 按位与 TreeNode{Val: vals[0].(int)} 写入 root :
	q := []*TreeNode{root}                // 把 [] 乘 TreeNode{根节点} 写入 q :
	i := 1                                // 把 1 写入 i :
	for len(q) > 0 && i < len(vals) {     // 定义函数/方法 len
		node := q[0]                         // 把 节点[0] 写入 node :
		q = q[1:]                            // 把 节点[1:] 写入 节点
		if i < len(vals) && vals[i] != nil { // 若 下标 i 小于 长度(vals) 且 vals[下标 i] 不等于 nil
			node.Left = &TreeNode{Val: vals[i].(int)} // 把 按位与 TreeNode{Val: vals[下标 i].(int)} 写入 node.Left
			q = append(q, node.Left)                  // 把 append(节点, 节点.Left) 写入 节点
		}
		i++                                  // 下标 i 加一
		if i < len(vals) && vals[i] != nil { // 若 下标 i 小于 长度(vals) 且 vals[下标 i] 不等于 nil
			node.Right = &TreeNode{Val: vals[i].(int)} // 把 按位与 TreeNode{Val: vals[下标 i].(int)} 写入 node.Right
			q = append(q, node.Right)                  // 把 append(节点, 节点.Right) 写入 节点
		}
		i++ // 下标 i 加一
	}
	return root // 返回 根节点
}

func levelOrder(root *TreeNode) [][]int { // 定义函数/方法 levelOrder
	if root == nil { // 若 根节点 等于 nil
		return [][]int{} // 返回 [][]int{}
	}
	q := []*TreeNode{root} // 把 [] 乘 TreeNode{根节点} 写入 q :
	res := [][]int{}       // 把 [][]int{} 写入 res :
	for len(q) > 0 {       // for 长度(节点) 超过 0 {
		size := len(q)              // 把 长度(节点) 写入 size :
		level := []int{}            // 把 []int{} 写入 level :
		for i := 0; i < size; i++ { // 让 下标 i 从 0 开始计数
			n := q[0]                    // 把 节点[0] 写入 n :
			q = q[1:]                    // 把 节点[1:] 写入 节点
			level = append(level, n.Val) // 把 append(level, 元素个数.Val) 写入 level
			if n.Left != nil {           // 若 元素个数.Left 不等于 nil
				q = append(q, n.Left) // 把 append(节点, 元素个数.Left) 写入 节点
			}
			if n.Right != nil { // 若 元素个数.Right 不等于 nil
				q = append(q, n.Right) // 把 append(节点, 元素个数.Right) 写入 节点
			}
		}
		res = append(res, level) // 把 append(结果, level) 写入 结果
	}
	return res // 返回 结果
}

type tc struct { // 定义类型
	root *TreeNode // 根节点 乘 TreeNode
	want [][]int   // want [][]int
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []tc{ // 把 []tc{ 写入 cases :
		{buildTree(nil), [][]int{}},
		{buildTree([]interface{}{3, 9, 20, nil, nil, 15, 7}), [][]int{{3}, {9, 20}, {15, 7}}},
		{buildTree([]interface{}{1, 2, 3}), [][]int{{1}, {2, 3}}},
		{buildTree([]interface{}{1}), [][]int{{1}}},
	}
	for idx, c := range cases { // 同时取 idx 与 字符 遍历
		got := levelOrder(c.root)            // 把 levelOrder(字符.根节点) 写入 got :
		if !reflect.DeepEqual(got, c.want) { // 若 取反 reflect.DeepEqual(got, 字符.want
			fmt.Printf("case %d failed: got %v want %v\n", idx, got, c.want) // 打印输出
			os.Exit(1)                                                       // os.Exit(1)
		}
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
