-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134066237
-- 数据结构与算法之排序: 冒泡排序 — Lua 版（方案1）
local function gnome_sort_bubble(nums) -- local function gnome_sort_bubble(数组)
	local v = { table.unpack(nums) } -- 把 {table.unpack(数组)} 写入 local v
	local n = #v -- 把 #值 写入 local n
	for i = 1, n do -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
		for j = 1, n - i do -- 让 下标 j 从 1 走到 元素个数（Lua 1 基）
			if v[j] > v[j + 1] then
				v[j], v[j + 1] = v[j + 1], v[j]
			end
		end -- 终点
	end -- 终点
	return v -- 返回 值
end -- 终点
assert(table.concat(gnome_sort_bubble({ 5, 4, 3, 2, 1 }), ",") == "1,2,3,4,5") -- 打印输出
assert(table.concat(gnome_sort_bubble({ 3, 1, 2 }), ",") == "1,2,3") -- 打印输出
assert(#gnome_sort_bubble({}) == 0) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
