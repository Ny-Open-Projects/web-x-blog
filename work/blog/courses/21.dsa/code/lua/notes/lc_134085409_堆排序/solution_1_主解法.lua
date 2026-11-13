-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134085409
-- 数据结构与算法之排序: 堆排序 — Lua 版（方案1）
local function heap_sort(nums) -- local function heap_sort(数组)
	local v = { table.unpack(nums) } -- 把 {table.unpack(数组)} 写入 local v
	local n = #v -- 把 #值 写入 local n
	local function sift(start, end_) -- local function sift(起点, end_)
		local root = start -- 把 起点 写入 local root
		while true do -- while true do
			local child = 2 * root -- 把 2 乘 根节点 写入 local child
			if child > end_ then
				break
			end -- 若 子节点 超过 end_ then break 终点
			local swap = root -- 把 根节点 写入 local swap
			if v[swap] < v[child] then
				swap = child
			end -- 若 值[swap] 小于 值[子节点] then swap 赋值为 子节点 终点
			if child + 1 <= end_ and v[swap] < v[child + 1] then
				swap = child + 1
			end
			if swap == root then
				break
			end -- 若 swap 等于 根节点 then break 终点
			v[root], v[swap] = v[swap], v[root] -- 把 值[swap], 值[根节点] 写入 v[root], v[swap]
			root = swap -- 把 swap 存入 根节点
		end -- 终点
	end -- 终点
	for i = n // 2, 1, -1 do
		sift(i, n)
	end -- 把 元素个数 写入 for i
	for end_ = n, 2, -1 do -- 把 元素个数, 2, 减 1 do 写入 for end_
		v[1], v[end_] = v[end_], v[1] -- 把 值[end_], 值[1] 写入 v[1], v[end_]
		sift(1, end_ - 1) -- sift(1, end_ 减 1)
	end -- 终点
	return v -- 返回 值
end -- 终点
assert(table.concat(heap_sort({ 5, 2, 4, 6, 1, 3 }), ",") == "1,2,3,4,5,6") -- 打印输出
assert(table.concat(heap_sort({ 9, 8, 7, 6, 5 }), ",") == "5,6,7,8,9") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
