// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107868749
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
	"sort"    // 「sort」
)

func matrixSort(matrix [][]int) [][]int { // 定义函数/方法 matrixSort
	if len(matrix) == 0 || len(matrix[0]) == 0 { // 若 长度(矩阵) 等于 0 或 长度(矩阵[0]) 等于 0
		return matrix // 返回 矩阵
	}
	rows, cols := len(matrix), len(matrix[0]) // 把 长度(矩阵), 长度(矩阵[0]) 写入 rows, cols :
	for c := 0; c < cols; c++ {               // 让 字符 从 0 开始计数
		col := make([]int, rows)    // 把 make([]int, 行数) 写入 col :
		for r := 0; r < rows; r++ { // 让 右指针 从 0 开始计数
			col[r] = matrix[r][c] // 把 矩阵[右指针][字符] 写入 col[r]
		}
		sort.Ints(col)              // sort.Ints(col)
		for r := 0; r < rows; r++ { // 让 右指针 从 0 开始计数
			matrix[r][c] = col[r] // 把 col[右指针] 写入 matrix[r][c]
		}
	}
	for r := 0; r < rows; r++ { // 让 右指针 从 0 开始计数
		sort.Ints(matrix[r]) // sort.Ints(矩阵[右指针])
	}
	return matrix // 返回 矩阵
}

type huffNode struct { // 定义类型
	weight int       // weight int
	ch     byte      // 字符 byte
	left   *huffNode // 左边界 乘 huffNode
	right  *huffNode // 右边界 乘 huffNode
}

func buildHuffman(freqs map[byte]int) *huffNode { // 定义函数/方法 buildHuffman
	nodes := []*huffNode{}     // 把 [] 乘 huffNode{} 写入 nodes :
	for ch, w := range freqs { // 同时取 字符 与 权重 遍历
		nodes = append(nodes, &huffNode{weight: w, ch: ch}) // 把 append(nodes, 按位与 huffNode{weight: 权重, 字符: 字符}) 写入 nodes
	}
	for len(nodes) > 1 { // for 长度(nodes) 超过 1 {
		sort.Slice(nodes, func(i, j int) bool { return nodes[i].weight < nodes[j].weight })
		a := nodes[0]     // 把 nodes[0] 写入 a :
		b := nodes[1]     // 把 nodes[1] 写入 b :
		nodes = nodes[2:] // 把 nodes[2:] 写入 nodes
		nodes = append(nodes, &huffNode{weight: a.weight + b.weight, left: a, right: b})
	}
	if len(nodes) == 0 { // 若 长度(nodes) 等于 0
		return nil // 返回 nil
	}
	return nodes[0] // 返回 nodes[0]
}

func huffmanCodes(freqs map[byte]int) map[byte]string { // 定义函数/方法 huffmanCodes
	root := buildHuffman(freqs)               // 把 buildHuffman(freqs) 写入 root :
	codes := map[byte]string{}                // 把 映射表[byte]string{} 写入 codes :
	var walk func(*huffNode, string)          // var walk func( 乘 huffNode, string)
	walk = func(n *huffNode, prefix string) { // 把 func(元素个数 乘 huffNode, prefix string) { 写入 walk
		if n == nil { // 若 元素个数 等于 nil
			return // return
		}
		if n.left == nil && n.right == nil { // 若 元素个数.左边界 等于 nil 且 元素个数.右边界 等于 nil
			if prefix == "" { // 若 prefix 等于 「」
				codes[n.ch] = "0" // 把 「0」 写入 codes[n.ch]
			} else { // 否则
				codes[n.ch] = prefix // 把 prefix 写入 codes[n.ch]
			}
			return // return
		}
		walk(n.left, prefix+"0")  // walk(元素个数.左边界, prefix 加 「0」)
		walk(n.right, prefix+"1") // walk(元素个数.右边界, prefix 加 「1」)
	}
	walk(root, "") // walk(根节点, 「」)
	return codes   // 返回 codes
}

func main() { // 程序入口：跑内嵌自测用例
	mat := [][]int{{5, 3, 4}, {1, 6, 2}, {7, 9, 8}}     // 把 [][]int{{5, 3, 4}, {1, 6, 2}, {7, 9, 8}} 写入 mat :
	sortedMat := matrixSort(mat)                        // 把 matrixSort(mat) 写入 sortedMat :
	wantMat := [][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}} // 把 [][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}} 写入 wantMat :
	if !reflect.DeepEqual(sortedMat, wantMat) {         // 若 取反 reflect.DeepEqual(sortedMat, wantMat
		fmt.Printf("FAIL matrixSort=%v\n", sortedMat) // 打印输出
		os.Exit(1)                                    // os.Exit(1)
	}
	freqs := map[byte]int{'A': 5, 'B': 9, 'C': 12, 'D': 13, 'E': 16, 'F': 45}
	codes := huffmanCodes(freqs) // 把 huffmanCodes(freqs) 写入 codes :
	totalBits := 0               // 把 0 写入 totalBits :
	for ch := range freqs {      // 把 range freqs { 写入 for ch :
		totalBits += freqs[ch] * len(codes[ch]) // totalBits累加 freqs[字符] 乘 长度(codes[字符])
	}
	if totalBits != 224 { // 若 totalBits 不等于 224
		fmt.Printf("FAIL huffman totalBits=%d want=224\n", totalBits) // 打印输出
		os.Exit(1)                                                    // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
