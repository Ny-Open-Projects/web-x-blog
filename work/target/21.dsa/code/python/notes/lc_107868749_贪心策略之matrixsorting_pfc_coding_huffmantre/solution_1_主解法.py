# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107868749
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
import heapq  # 引入依赖


def matrix_sort(matrix):  # 定义函数 matrix_sort（参数：矩阵）
    # 矩阵排序：先对每一列排序，再对每一行排序
    if not matrix or not matrix[0]:  # 若 not 矩阵 or not 矩阵[0]
        return matrix  # 返回 矩阵
    rows, cols = len(matrix), len(matrix[0])  # 把 长度(矩阵), 长度(矩阵[0]) 写入 rows, cols
    # 逐列排序
    for c in range(cols):  # 让 字符 从 列数 遍历
        col = sorted(
            matrix[r][c] for r in range(rows)
        )  # 把 sorted(矩阵[右指针][字符] for 右指针 in range(行数)) 存入 col
        for r in range(rows):  # 让 右指针 从 行数 遍历
            matrix[r][c] = col[r]  # 把 col[右指针] 写入 matrix[r][c]
    # 逐行排序
    for r in range(rows):  # 让 右指针 从 行数 遍历
        matrix[r] = sorted(matrix[r])  # 把 sorted(矩阵[右指针]) 写入 matrix[r]
    return matrix  # 返回 矩阵


def build_huffman(freqs):  # 定义函数 build_huffman（参数：freqs）
    # 哈夫曼树：每次合并权值最小的两棵子树（贪心）
    nodes = [
        [w, ch] for ch, w in freqs.items()
    ]  # 把 [[权重, 字符] for 字符, 权重 in freqs.items()] 存入 nodes
    heapq.heapify(nodes)  # heapq.heapify(nodes)
    while len(nodes) > 1:  # 循环，直到不满足「长度(nodes) 超过 1」
        a = heapq.heappop(nodes)  # 把 heapq.heappop(nodes) 存入 数组
        b = heapq.heappop(nodes)  # 把 heapq.heappop(nodes) 存入 b
        heapq.heappush(nodes, [a[0] + b[0], [a, b]])  # heapq.heappush(nodes, [数组[0] 加 b[0], [数组, b]])
    return nodes[0] if nodes else None  # 返回 nodes[0] if nodes else None


def huffman_codes(freqs):  # 定义函数 huffman_codes（参数：freqs）
    root = build_huffman(freqs)  # 把 build_huffman(freqs) 存入 根节点
    codes = {}  # 把 {} 存入 codes

    def walk(node, prefix):  # 定义函数 walk（参数：节点, prefix）
        if isinstance(node, list):  # 若 isinstance(节点, 列表
            w, content = node  # 把 节点 写入 w, content
            if isinstance(content, str):  # 若 isinstance(content, str
                codes[content] = prefix or "0"  # 把 prefix or '0' 写入 codes[content]
            else:  # 否则
                walk(content[0], prefix + "0")  # walk(content[0], prefix 加 '0')
                walk(content[1], prefix + "1")  # walk(content[1], prefix 加 '1')

    walk(root, "")  # walk(根节点, '')
    return codes  # 返回 codes


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    mat = [
        [5, 3, 4],
        [1, 6, 2],
        [7, 9, 8],
    ]
    sorted_mat = matrix_sort(
        [row[:] for row in mat]
    )  # 把 matrix_sort([复制 row for row in mat]) 存入 sorted_mat
    print("矩阵排序结果:")  # 打印输出
    for row in sorted_mat:  # 逐个取出 sorted_mat 的元素（row）
        print(row)  # 打印输出

    freqs = {"A": 5, "B": 9, "C": 12, "D": 13, "E": 16, "F": 45}
    codes = huffman_codes(freqs)  # 把 huffman_codes(freqs) 存入 codes
    total_bits = sum(freqs[ch] * len(codes[ch]) for ch in freqs)
    print("哈夫曼编码:", codes)  # 打印输出
    print("总编码比特数:", total_bits)  # 打印输出
