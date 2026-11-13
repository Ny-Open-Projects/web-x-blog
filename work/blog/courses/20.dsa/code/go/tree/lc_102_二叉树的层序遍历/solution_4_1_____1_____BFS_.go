// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130877211
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

func buildTree(vals []interface{}) *TreeNode { // 定义函数/方法 buildTree
	if len(vals) == 0 || vals[0] == nil { // 若 长度(vals) 等于 0 或 vals[0] 等于 nil
		return nil // 返回 nil
	}
	root := &TreeNode{Val: vals[0].(int)} // 把 按位与 TreeNode{Val: vals[0].(int)} 写入 root :
	q := []*TreeNode{root}                // 把 [] 乘 TreeNode{根节点} 写入 q :
	i := 1                                // 把 1 写入 i :
	for i < len(vals) {                   // for 下标 i 小于 长度(vals) {
		node := q[0]        // 把 节点[0] 写入 node :
		q = q[1:]           // 把 节点[1:] 写入 节点
		if vals[i] != nil { // 若 vals[下标 i] 不等于 nil
			node.Left = &TreeNode{Val: vals[i].(int)} // 把 按位与 TreeNode{Val: vals[下标 i].(int)} 写入 node.Left
			q = append(q, node.Left)                  // 把 append(节点, 节点.Left) 写入 节点
		}
		i++                // 下标 i 加一
		if i < len(vals) { // 若 下标 i 小于 长度(vals
			if vals[i] != nil { // 若 vals[下标 i] 不等于 nil
				node.Right = &TreeNode{Val: vals[i].(int)} // 把 按位与 TreeNode{Val: vals[下标 i].(int)} 写入 node.Right
				q = append(q, node.Right)                  // 把 append(节点, 节点.Right) 写入 节点
			}
			i++ // 下标 i 加一
		}
	}
	return root // 返回 根节点
}

func levelOrder(root *TreeNode) [][]int { // 定义函数/方法 levelOrder
	ret := [][]int{} // 把 [][]int{} 写入 ret :
	if root == nil { // 若 根节点 等于 nil
		return ret // 返回 ret
	}
	q := []*TreeNode{root} // 把 [] 乘 TreeNode{根节点} 写入 q :
	for len(q) > 0 {       // for 长度(节点) 超过 0 {
		size := len(q)              // 把 长度(节点) 写入 size :
		level := []int{}            // 把 []int{} 写入 level :
		for i := 0; i < size; i++ { // 让 下标 i 从 0 开始计数
			node := q[0]                    // 把 节点[0] 写入 node :
			q = q[1:]                       // 把 节点[1:] 写入 节点
			level = append(level, node.Val) // 把 append(level, 节点.Val) 写入 level
			if node.Left != nil {           // 若 节点.Left 不等于 nil
				q = append(q, node.Left) // 把 append(节点, 节点.Left) 写入 节点
			}
			if node.Right != nil { // 若 节点.Right 不等于 nil
				q = append(q, node.Right) // 把 append(节点, 节点.Right) 写入 节点
			}
		}
		ret = append(ret, level) // 把 append(ret, level) 写入 ret
	}
	return ret // 返回 ret
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		vals []interface{} // vals []interface{}
		want [][]int       // want [][]int
	}{ // }{
		{nil, [][]int{}},
		{[]interface{}{3, 9, 20, nil, nil, 15, 7}, [][]int{{3}, {9, 20}, {15, 7}}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if g := levelOrder(buildTree(c.vals)); !reflect.DeepEqual(g, c.want) {
			ok = false                                            // 把 false 写入 ok
			fmt.Printf("FAIL %v=%v want %v\n", c.vals, g, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
