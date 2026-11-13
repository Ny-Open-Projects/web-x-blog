// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144994166
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

func isBalanced(root *TreeNode) bool { // 定义判定函数 isBalanced
	var height func(*TreeNode) int   // var height func( 乘 TreeNode) int
	height = func(n *TreeNode) int { // 把 func(元素个数 乘 TreeNode) int { 写入 height
		if n == nil { // 若 元素个数 等于 nil
			return 0 // 返回 0
		}
		lh := height(n.Left)                                // 把 height(元素个数.Left) 写入 lh :
		rh := height(n.Right)                               // 把 height(元素个数.Right) 写入 rh :
		if lh == -1 || rh == -1 || lh-rh > 1 || rh-lh > 1 { // 若 lh 等于 减 1 或 rh 等于 减 1 或 lh 减 rh 超过 1 或 rh 减 lh 超过 1
			return -1 // 返回 减 1
		}
		if lh > rh { // 若 lh 超过 rh
			return lh + 1 // 返回 lh 加 1
		}
		return rh + 1 // 返回 rh 加 1
	}
	return height(root) != -1 // 返回 height(根节点) 不等于 减 1
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		vals []interface{} // vals []interface{}
		want bool          // want bool
	}{ // }{
		{nil, true},
		{[]interface{}{1, 2, 2, 3, 3, nil, nil, 4, 4}, false},
		{[]interface{}{3, 9, 20, nil, nil, 15, 7}, true},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if g := isBalanced(buildTree(c.vals)); g != c.want { // 若 g : 赋值为 isBalanced(buildTree(字符.vals)); g 不等于 字符.want
			ok = false                                            // 把 false 写入 ok
			fmt.Printf("FAIL %v=%v want %v\n", c.vals, g, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
