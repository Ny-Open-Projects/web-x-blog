-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138671078
-- LeetCode 1356. 根据数字二进制下1的数目排序 — Lua 版（方案1）
local function count_bits(n) -- local function count_bits(元素个数)
	local c = 0 -- 把 0 写入 local c
	while n > 0 do -- while 元素个数 超过 0 do
		c = c + (n & 1) -- 把 字符 加 (元素个数 按位与 1) 存入 字符
		n = n >> 1 -- 把 元素个数 超过 超过 1 存入 元素个数
	end -- 终点
	return c -- 返回 字符
end -- 终点
local function sort_by_bits(nums) -- local function sort_by_bits(数组)
	local arr = { table.unpack(nums) } -- 把 {table.unpack(数组)} 写入 local arr
	table.sort(arr, function(a, b) -- 排序
		local ba, bb = count_bits(a), count_bits(b) -- 把 count_bits(数组), count_bits(b) 写入 local ba, bb
		if ba ~= bb then
			return ba < bb
		end -- 若 ba ~ 赋值为 bb then return ba 小于 bb 终点
		return a < b -- 返回 数组 小于 b
	end) -- 终点)
	return arr -- 返回 数组
end -- 终点
local a = sort_by_bits({ 0, 1, 2, 3, 4, 5, 6, 7, 8 }) -- 把 sort_by_bits({0, 1, 2, 3, 4, 5, 6, 7, 8}) 写入 local a
assert(#a == 9 and a[1] == 0 and a[2] == 1 and a[3] == 2 and a[4] == 4 and a[5] == 8 and a[6] == 3 and a[9] == 7) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
