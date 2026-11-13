-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134982348
-- LeetCode 977. 有序数组的平方 — Lua 版（方案2）
local function sorted_squares(nums) -- local function sorted_squares(数组)
	local n = #nums -- 把 #数组 写入 local n
	local out = {} -- 把 {} 写入 local out
	local l, r, idx = 1, n, n -- 把 1, 元素个数, 元素个数 写入 local l, r, idx
	while l <= r do -- 把 右指针 do 写入 while l <
		local a = math.abs(nums[l]) -- 把 math.取绝对值 数组[左指针]) 写入 local a
		local b = math.abs(nums[r]) -- 把 math.取绝对值 数组[右指针]) 写入 local b
		if a > b then
			out[idx] = a * a
			l = l + 1 -- 若 数组 超过 b then out[idx] 赋值为 数组 乘 数组; 左指针 赋值为 左指针 加 1
		else
			out[idx] = b * b
			r = r - 1
		end -- 否则
		idx = idx - 1 -- 把 idx 减 1 存入 idx
	end -- 终点
	return out -- 返回 out
end -- 终点
assert(table.concat(sorted_squares({ -4, -1, 0, 3, 10 }), ",") == "0,1,9,16,100") -- 打印输出
assert(table.concat(sorted_squares({ -7, -3, 2, 3, 11 }), ",") == "4,9,9,49,121") -- 打印输出
assert(table.concat(sorted_squares({ 1, 2, 3 }), ",") == "1,4,9") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
