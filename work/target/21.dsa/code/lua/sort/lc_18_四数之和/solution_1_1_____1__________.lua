-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133894317
-- LeetCode 18. 四数之和 — Lua 版（方案1）
local function four_sum(nums, target) -- local function four_sum(数组, 目标值)
	local arr = { table.unpack(nums) } -- 把 {table.unpack(数组)} 写入 local arr
	table.sort(arr) -- 排序
	local res = {} -- 把 {} 写入 local res
	local n = #arr -- 把 #数组 写入 local n
	for i = 1, n do -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
		if i == 1 or arr[i] ~= arr[i - 1] then -- 若 下标 i 等于 1 or 数组[下标 i] ~ 赋值为 数组[下标 i 减 1] then
			for j = i + 1, n do -- 把 下标 i 加 1, 元素个数 do 写入 for j
				if j == i + 1 or arr[j] ~= arr[j - 1] then -- 若 下标 j 等于 下标 i 加 1 or 数组[下标 j] ~ 赋值为 数组[下标 j 减 1] then
					local left, right = j + 1, n -- 把 下标 j 加 1, 元素个数 写入 local left, right
					while left < right do -- while 左边界 小于 右边界 do
						local s = arr[i] + arr[j] + arr[left] + arr[right] -- 把 数组[下标 i] 加 数组[下标 j] 加 数组[左边界] 加 数组[右边界] 写入 local s
						if s == target then -- 若 字符串 等于 目标值 then
							res[#res + 1] = { arr[i], arr[j], arr[left], arr[right] } -- 把 {数组[下标 i], 数组[下标 j], 数组[左边界], 数组[右边界]} 写入 res[#res + 1]
							left = left + 1 -- 把 左边界 加 1 存入 左边界
							right = right - 1 -- 把 右边界 减 1 存入 右边界
							while left < right and arr[left] == arr[left - 1] do
								left = left + 1
							end
							while left < right and arr[right] == arr[right + 1] do
								right = right - 1
							end
						elseif s < target then
							left = left + 1 -- 把 左边界 加 1 写入 elseif s < target then left
						else
							right = right - 1
						end -- 否则
					end -- 终点
				end -- 终点
			end -- 终点
		end -- 终点
	end -- 终点
	return res -- 返回 结果
end -- 终点
local got = four_sum({ 1, 0, -1, 0, -2, 2 }, 0) -- 把 four_sum({1, 0, 减 1, 0, 减 2, 2}, 0) 写入 local got
assert(#got == 3, "count " .. #got) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
