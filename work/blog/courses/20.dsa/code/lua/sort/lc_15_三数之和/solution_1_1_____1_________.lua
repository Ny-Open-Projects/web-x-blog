-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133845474
-- LeetCode 15. 三数之和 — Lua 版（方案1）
local function three_sum(nums) -- local function three_sum(数组)
	local arr = { table.unpack(nums) } -- 把 {table.unpack(数组)} 写入 local arr
	table.sort(arr) -- 排序
	local ans = {} -- 把 {} 写入 local ans
	local n = #arr -- 把 #数组 写入 local n
	for first = 1, n do -- 让 first 从 1 走到 元素个数（Lua 1 基）
		if first == 1 or arr[first] ~= arr[first - 1] then -- 若 first 等于 1 or 数组[first] ~ 赋值为 数组[first 减 1] then
			local third = n -- 把 元素个数 写入 local third
			local target = -arr[first] -- 把 减 数组[first] 写入 local target
			for second = first + 1, n do -- 把 first 加 1, 元素个数 do 写入 for second
				if second == first + 1 or arr[second] ~= arr[second - 1] then
					while second < third and arr[second] + arr[third] > target do
						third = third - 1
					end
					if second == third then
						break
					end -- 若 second 等于 third then break 终点
					if arr[second] + arr[third] == target then -- 若 数组[second] 加 数组[third] 等于 目标值 then
						ans[#ans + 1] = { arr[first], arr[second], arr[third] } -- 把 {数组[first], 数组[second], 数组[third]} 写入 ans[#ans + 1]
					end -- 终点
				end -- 终点
			end -- 终点
		end -- 终点
	end -- 终点
	return ans -- 返回 答案
end -- 终点
local got = three_sum({ -1, 0, 1, 2, -1, -4 }) -- 把 three_sum({ 减 1, 0, 1, 2, 减 1, 减 4}) 写入 local got
table.sort(got, function(a, b)
	return a[1] < b[1] or (a[1] == b[1] and a[2] < b[2])
end) -- 排序
assert(#got == 2) -- 断言校验
assert(got[1][1] == -1 and got[1][2] == -1 and got[1][3] == 2) -- 断言校验
assert(got[2][1] == -1 and got[2][2] == 0 and got[2][3] == 1) -- 断言校验
local g2 = three_sum({ 0, 0, 0 }) -- 把 three_sum({0, 0, 0}) 写入 local g2
assert(#g2 == 1 and g2[1][1] == 0) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
