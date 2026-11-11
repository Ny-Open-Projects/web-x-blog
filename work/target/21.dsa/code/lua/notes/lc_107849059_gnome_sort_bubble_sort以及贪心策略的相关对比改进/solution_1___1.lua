-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107849059
-- Gnome Sort（侏儒排序）+ Bubble Sort（冒泡排序）+ 贪心找零 对比
local function gnome_sort(arr) -- local function gnome_sort(数组)
	local a = {} -- 把 {} 写入 local a
	for i, v in ipairs(arr) do
		a[i] = v
	end -- 遍历取 值
	local i = 1 -- 把 1 写入 local i
	while i <= #a do -- 把 #数组 do 写入 while i <
		if i == 1 or a[i] >= a[i - 1] then -- 若 下标 i 等于 1 or 数组[下标 i] 不低于 数组[下标 i 减 1] then
			i = i + 1 -- 把 下标 i 加 1 存入 下标 i
		else -- 否则
			a[i - 1], a[i] = a[i], a[i - 1] -- 把 数组[下标 i], 数组[下标 i 减 1] 写入 a[i - 1], a[i]
			i = i - 1 -- 把 下标 i 减 1 存入 下标 i
		end -- 终点
	end -- 终点
	return a -- 返回 数组
end -- 终点

local function bubble_sort(arr) -- local function bubble_sort(数组)
	local a = {} -- 把 {} 写入 local a
	for i, v in ipairs(arr) do
		a[i] = v
	end -- 遍历取 值
	local swapped = true -- 把 true 写入 local swapped
	while swapped do -- while swapped do
		swapped = false -- 把 false 存入 swapped
		for i = 1, #a - 1 do -- 把 1, #数组 减 1 do 写入 for i
			if a[i] > a[i + 1] then -- 若 数组[下标 i] 超过 数组[下标 i 加 1] then
				a[i], a[i + 1] = a[i + 1], a[i] -- 把 数组[下标 i 加 1], 数组[下标 i] 写入 a[i], a[i + 1]
				swapped = true -- 把 true 存入 swapped
			end -- 终点
		end -- 终点
	end -- 终点
	return a -- 返回 数组
end -- 终点

local function coin_change(coins, amount) -- local function coin_change(硬币面额, 目标金额)
	local cs = {} -- 把 {} 写入 local cs
	for i, v in ipairs(coins) do
		cs[i] = v
	end -- 遍历取 值
	table.sort(cs, function(x, y)
		return x > y
	end) -- 排序
	local remaining = amount -- 把 目标金额 写入 local remaining
	local count = 0 -- 把 0 写入 local count
	for _, coin in ipairs(cs) do -- 遍历取 coin
		while remaining >= coin do -- 把 coin do 写入 while remaining >
			remaining = remaining - coin -- 把 remaining 减 coin 存入 remaining
			count = count + 1 -- 把 计数 加 1 存入 计数
		end -- 终点
	end -- 终点
	if remaining == 0 then
		return count
	else
		return -1
	end -- 若 remaining 等于 0 then return 计数 else return 减 1 终点
end -- 终点

local function eq_arr(x, y) -- local function eq_arr(x, y)
	if #x ~= #y then
		return false
	end -- 若 #x ~ 赋值为 #y then return false 终点
	for i = 1, #x do
		if x[i] ~= y[i] then
			return false
		end
	end
	return true -- 返回 true
end -- 终点

assert(eq_arr(gnome_sort({ 3, 2, 1 }), { 1, 2, 3 }), "g") -- 断言校验
assert(eq_arr(bubble_sort({ 3, 2, 1 }), { 1, 2, 3 }), "b") -- 断言校验
assert(coin_change({ 1, 5, 10, 25 }, 63) == 6, "c") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
