-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134350547
-- LeetCode 384. 打乱数组 — Lua 版（方案2）
local ShuffleArray = {} -- 把 {} 写入 local ShuffleArray
ShuffleArray.__index = ShuffleArray -- 把 ShuffleArray 写入 ShuffleArray.__index
function ShuffleArray.new(vals)
	return setmetatable({ orig = { table.unpack(vals) }, cur = { table.unpack(vals) } }, ShuffleArray)
end
function ShuffleArray:reset() -- function ShuffleArray:reset()
	self.cur = { table.unpack(self.orig) } -- 把 {table.unpack(self.orig)} 写入 当前值
	return self.cur -- 返回 self.当前值
end -- 终点
function ShuffleArray:shuffle() -- function ShuffleArray:shuffle()
	local n = #self.cur -- 把 #self.当前值 写入 local n
	for i = n, 2, -1 do -- 把 元素个数, 2, 减 1 do 写入 for i
		local j = math.random(i) -- 把 math.random(下标 i) 写入 local j
		self.cur[i], self.cur[j] = self.cur[j], self.cur[i] -- 把 self.当前值[下标 j], self.当前值[下标 i] 写入 self.cur[i], self.cur[j]
	end -- 终点
	return self.cur -- 返回 self.当前值
end -- 终点
math.randomseed(42) -- math.randomseed(42)
local sa = ShuffleArray.new({ 1, 2, 3 }) -- 把 ShuffleArray.new({1, 2, 3}) 写入 local sa
local sh = sa:shuffle() -- 把 sa:shuffle() 写入 local sh
table.sort(sh) -- 排序
assert(table.concat(sh, ",") == "1,2,3") -- 打印输出
local r = sa:reset() -- 把 sa:reset() 写入 local r
assert(table.concat(r, ",") == "1,2,3") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
