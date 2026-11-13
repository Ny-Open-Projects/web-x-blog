-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233483
-- LeetCode 153. 寻找旋转排序数组中的最小值 — Lua 版（方案1：二分查找）

-- 0 基下标语义与 TS 参考一致（Lua 数组本身 1 基，读取时 +1）
local function findMin(nums) -- local function findMin(数组)
	local low = 0 -- 把 0 写入 local low
	local high = #nums - 1 -- 把 #数组 减 1 写入 local high
	while low < high do -- while low 小于 high do
		local pivot = low + (high - low) // 2 -- 防溢出写法（Lua 5.4 整数除法）
		if nums[pivot + 1] < nums[high + 1] then -- 若 数组[pivot 加 1] 小于 数组[high 加 1] then
			high = pivot -- 把 pivot 存入 high
		else -- 否则
			low = pivot + 1 -- 把 pivot 加 1 存入 low
		end -- 终点
	end -- 终点
	return nums[low + 1] -- 返回 数组[low 加 1]
end -- 终点

-- 自测：与 LeetCode 官方用例一致
assert(findMin({ 1, 2, 3 }) == 1, "case 1 failed") -- 断言校验
assert(findMin({ 3, 4, 5, 1, 2 }) == 1, "case 2 failed") -- 断言校验
assert(findMin({ 4, 5, 6, 7, 0, 1, 2 }) == 0, "case 3 failed") -- 断言校验
assert(findMin({ 11, 13, 15, 17 }) == 11, "case 4 failed") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
