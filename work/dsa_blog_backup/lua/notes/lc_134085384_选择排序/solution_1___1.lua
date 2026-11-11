-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134085384
-- 数据结构与算法之排序: 选择排序 — Lua 版（方案1）
local function selection_sort(nums) -- local function selection_sort(数组)
	local v = { table.unpack(nums) } -- 把 {table.unpack(数组)} 写入 local v
	local n = #v -- 把 #值 写入 local n
	for i = 1, n - 1 do -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
		local m = i -- 把 下标 i 写入 local m
		for j = i + 1, n do
			if v[j] < v[m] then
				m = j
			end
		end
		v[i], v[m] = v[m], v[i] -- 把 值[映射表], 值[下标 i] 写入 v[i], v[m]
	end -- 终点
	return v -- 返回 值
end -- 终点
assert(table.concat(selection_sort({ 5, 4, 3, 2, 1 }), ",") == "1,2,3,4,5") -- 打印输出
assert(table.concat(selection_sort({ 3, 1, 2 }), ",") == "1,2,3") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
