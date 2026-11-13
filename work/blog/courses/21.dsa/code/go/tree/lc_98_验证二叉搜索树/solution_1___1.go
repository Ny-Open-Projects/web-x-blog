// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/131631290
package main // 引入依赖

import (
	"fmt"
	"math" // 引入依赖
	"os"
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

func isValidBST(root *TreeNode) bool { // 定义判定函数 isValidBST
	var dfs func(n *TreeNode) (bool, int, int) // var dfs func(元素个数 乘 TreeNode) (bool, int, int)
	dfs = func(n *TreeNode) (bool, int, int) { // 把 func(元素个数 乘 TreeNode) (bool, int, int) { 写入 dfs
		if n == nil { // 若 元素个数 等于 nil
			return true, math.MaxInt64, math.MinInt64 // 返回 true, math.MaxInt64, math.MinInt64
		}
		lok, lmin, lmax := dfs(n.Left)                   // 把 dfs(元素个数.Left) 写入 lok, lmin, lmax :
		rok, rmin, rmax := dfs(n.Right)                  // 把 dfs(元素个数.Right) 写入 rok, rmin, rmax :
		ok := lok && rok && lmax < n.Val && n.Val < rmin // 把 lok 且 rok 且 lmax 小于 元素个数.Val 且 元素个数.Val 小于 rmin 写入 ok :
		return ok, min(lmin, n.Val), max(rmax, n.Val)    // 返回 ok, 取较小值 lmin, 元素个数.Val), 取较大值 rmax, 元素个数.Val)
	}
	r, _, _ := dfs(root) // 把 dfs(根节点) 写入 r, _, _ :
	return r             // 返回 右指针
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		vals []interface{} // vals []interface{}
		want bool          // want bool
	}{ // }{
		{[]interface{}{2, 1, 3}, true},
		{[]interface{}{5, 1, 4, nil, nil, 3, 6}, false},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if g := isValidBST(buildTree(c.vals)); g != c.want { // 若 g : 赋值为 isValidBST(buildTree(字符.vals)); g 不等于 字符.want
			ok = false                                            // 把 false 写入 ok
			fmt.Printf("FAIL %v=%v want %v\n", c.vals, g, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
