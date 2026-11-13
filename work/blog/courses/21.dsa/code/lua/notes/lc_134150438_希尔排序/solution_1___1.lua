-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134150438
-- 数据结构与算法之排序: 希尔排序 — Lua 版（方案1）
local function shell_sort(nums) -- local function shell_sort(数组)
	local v = { table.unpack(nums) } -- 把 {table.unpack(数组)} 写入 local v
	local n = #v -- 把 #值 写入 local n
	local gap = n // 2 -- 把 元素个数 写入 local gap
	while gap > 0 do -- while gap 超过 0 do
		for i = gap + 1, n do -- 把 gap 加 1, 元素个数 do 写入 for i
			local key = v[i] -- 把 值[下标 i] 写入 local key
			local j = i - gap -- 把 下标 i 减 gap 写入 local j
			while j >= 1 and v[j] > key do
				v[j + gap] = v[j]
				j = j - gap
			end
			v[j + gap] = key -- 把 key 写入 v[j + gap]
		end -- 终点
		gap = gap // 2 -- 把 gap 存入 gap
	end -- 终点
	return v -- 返回 值
end -- 终点
assert(table.concat(shell_sort({ 5, 2, 4, 6, 1, 3 }), ",") == "1,2,3,4,5,6") -- 打印输出
assert(table.concat(shell_sort({ 9, 8, 7, 6, 5, 4, 3, 2, 1 }), ",") == "1,2,3,4,5,6,7,8,9") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
