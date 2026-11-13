-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145565975
-- LeetCode 922. 按奇偶排序数组II — Lua 版（方案2）
local function sort_array_by_parity_ii(nums) -- local function sort_array_by_parity_ii(数组)
	local sorted = { table.unpack(nums) } -- 把 {table.unpack(数组)} 写入 local sorted
	table.sort(sorted) -- 排序
	local res = {} -- 把 {} 写入 local res
	local odd, even = 2, 1 -- 把 2, 1 写入 local odd, even
	for _, item in ipairs(sorted) do -- 遍历取 item
		if item % 2 == 1 then -- 若 item 对…取模 2 等于 1 then
			res[odd] = item -- 把 item 写入 res[odd]
			odd = odd + 2 -- 把 odd 加 2 存入 odd
		else -- 否则
			res[even] = item -- 把 item 写入 res[even]
			even = even + 2 -- 把 even 加 2 存入 even
		end -- 终点
	end -- 终点
	return res -- 返回 结果
end -- 终点
local a = sort_array_by_parity_ii({ 4, 2, 5, 7 }) -- 把 sort_array_by_parity_ii({4, 2, 5, 7}) 写入 local a
assert(#a == 4 and a[1] == 2 and a[2] == 5 and a[3] == 4 and a[4] == 7) -- 断言校验
local b = sort_array_by_parity_ii({ 2, 3 }) -- 把 sort_array_by_parity_ii({2, 3}) 写入 local b
assert(b[1] == 2 and b[2] == 3) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
