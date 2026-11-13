-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134053461
-- 数据结构与算法之排序: 侏儒排序 — Lua 版（方案1）
local function gnome_sort(nums) -- local function gnome_sort(数组)
	local v = { table.unpack(nums) } -- 把 {table.unpack(数组)} 写入 local v
	local i = 1 -- 把 1 写入 local i
	while i <= #v do -- 把 #值 do 写入 while i <
		if i == 1 or v[i - 1] <= v[i] then
			i = i + 1
		else
			v[i - 1], v[i] = v[i], v[i - 1]
			i = i - 1
		end -- 否则
	end -- 终点
	return v -- 返回 值
end -- 终点
assert(table.concat(gnome_sort({ 5, 4, 3, 2, 1 }), ",") == "1,2,3,4,5") -- 打印输出
assert(table.concat(gnome_sort({ 3, 1, 2 }), ",") == "1,2,3") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
