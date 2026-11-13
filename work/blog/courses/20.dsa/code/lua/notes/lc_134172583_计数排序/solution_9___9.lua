-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134172583
-- 数据结构与算法之排序: 计数排序 — Lua 版（方案9）
local function count_sort(nums) -- local function count_sort(数组)
	if #nums == 0 then
		return nums
	end -- 若 #数组 等于 0 then return 数组 终点
	local mx, mn = nums[1], nums[1] -- 把 数组[1], 数组[1] 写入 local mx, mn
	for _, v in ipairs(nums) do -- 遍历取 值
		if v > mx then
			mx = v
		end -- 若 值 超过 mx then mx 赋值为 值 终点
		if v < mn then
			mn = v
		end -- 若 值 小于 mn then mn 赋值为 值 终点
	end -- 终点
	local range = mx - mn + 1 -- 把 mx 减 mn 加 1 写入 local range
	local count = {} -- 把 {} 写入 local count
	for i = 1, range do
		count[i] = 0
	end -- 让 下标 i 从 1 走到 range（Lua 1 基）
	for _, v in ipairs(nums) do
		count[v - mn + 1] = count[v - mn + 1] + 1
	end -- 遍历取 值
	for i = 2, range do
		count[i] = count[i] + count[i - 1]
	end -- 让 下标 i 从 2 走到 range（Lua 1 基）
	local output = {} -- 把 {} 写入 local output
	for i = #nums, 1, -1 do -- 把 #数组, 1, 减 1 do 写入 for i
		local idx = nums[i] - mn + 1 -- 把 数组[下标 i] 减 mn 加 1 写入 local idx
		output[count[idx]] = nums[i] -- 把 数组[下标 i] 写入 output[count[idx]]
		count[idx] = count[idx] - 1 -- 把 计数[idx] 减 1 写入 count[idx]
	end -- 终点
	return output -- 返回 输出
end -- 终点
assert(table.concat(count_sort({ 5, 3, 8, 3, 1 }), ",") == "1,3,3,5,8") -- 打印输出
local big =
	count_sort({ 102, 103, 108, 107, 101, 102, 102, 102, 107, 103, 109, 108, 102, 101, 104, 102, 104, 106, 109, 102 })
assert(#big == 20 and big[1] == 101 and big[20] == 109) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
