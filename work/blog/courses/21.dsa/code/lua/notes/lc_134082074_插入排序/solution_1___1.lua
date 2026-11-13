-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134082074
-- 数据结构与算法之排序: 插入排序 — Lua 版（方案1）
local function insertion_sort(nums) -- local function insertion_sort(数组)
	local v = { table.unpack(nums) } -- 把 {table.unpack(数组)} 写入 local v
	for i = 2, #v do -- 把 2, #值 do 写入 for i
		local key = v[i] -- 把 值[下标 i] 写入 local key
		local j = i - 1 -- 把 下标 i 减 1 写入 local j
		while j >= 1 and v[j] > key do
			v[j + 1] = v[j]
			j = j - 1
		end
		v[j + 1] = key -- 把 key 写入 v[j + 1]
	end -- 终点
	return v -- 返回 值
end -- 终点
assert(table.concat(insertion_sort({ 5, 4, 3, 2, 1 }), ",") == "1,2,3,4,5") -- 打印输出
assert(table.concat(insertion_sort({ 3, 1, 2 }), ",") == "1,2,3") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
