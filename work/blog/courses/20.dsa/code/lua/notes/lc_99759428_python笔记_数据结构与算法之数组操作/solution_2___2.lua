-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/99759428
-- 数据结构与算法之数组操作 — Lua 版（方案2）
local function two_sum(nums, target) -- local function two_sum(数组, 目标值)
	for i = 1, #nums do -- 把 1, #数组 do 写入 for i
		for j = i + 1, #nums do -- 把 下标 i 加 1, #数组 do 写入 for j
			if nums[i] + nums[j] == target then
				return { i - 1, j - 1 }
			end
		end -- 终点
	end -- 终点
	return {} -- 返回 {}
end -- 终点
local function max_sub_array(nums) -- local function max_sub_array(数组)
	local best, cur = nums[1], nums[1] -- 把 数组[1], 数组[1] 写入 local best, cur
	for i = 2, #nums do -- 把 2, #数组 do 写入 for i
		cur = cur > 0 and cur + nums[i] or nums[i] -- 把 当前值 超过 0 and 当前值 加 数组[下标 i] or 数组[下标 i] 存入 当前值
		if cur > best then
			best = cur
		end -- 若 当前值 超过 当前最优 then 当前最优 赋值为 当前值 终点
	end -- 终点
	return best -- 返回 当前最优
end -- 终点
local function rotate_array(nums, k) -- local function rotate_array(数组, 下标 k)
	local n = #nums -- 把 #数组 写入 local n
	k = k % n -- 把 下标 k 对…取模 元素个数 存入 下标 k
	local out = {} -- 把 {} 写入 local out
	for i = n - k + 1, n do
		out[#out + 1] = nums[i]
	end
	for i = 1, n - k do
		out[#out + 1] = nums[i]
	end -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
	return out -- 返回 out
end -- 终点
assert(table.concat(two_sum({ 2, 7, 11, 15 }, 9), ",") == "0,1") -- 打印输出
assert(max_sub_array({ -2, 1, -3, 4, -1, 2, 1, -5, 4 }) == 6) -- 断言校验
assert(table.concat(rotate_array({ 1, 2, 3, 4, 5, 6, 7 }, 3), ",") == "5,6,7,1,2,3,4") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
