-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145556343
-- LeetCode 2166. 设计位集 — Lua 版（方案2）
local Bitset = {} -- 把 {} 写入 local Bitset
Bitset.__index = Bitset -- 把 Bitset 写入 Bitset.__index
function Bitset.new(size) -- function Bitset.new(大小)
	return setmetatable({ n = size, words = {}, ones = 0, reverse = 0 }, Bitset)
end -- 终点
function Bitset:get(idx) -- function Bitset:get(idx)
	local w = self.words[(idx >> 5) + 1] or 0 -- 把 self.单词列表[(idx 超过 超过 5) 加 1] or 0 写入 local w
	return ((w >> (idx & 31)) & 1) ~ self.reverse -- 返回 ((权重 超过 超过 (idx 按位与 31)) 按位与 1) ~ self.reverse
end -- 终点
function Bitset:fix(idx) -- function Bitset:fix(idx)
	if self:get(idx) == 0 then -- 若 self:get(idx) 等于 0 then
		self.words[(idx >> 5) + 1] = (self.words[(idx >> 5) + 1] or 0) | (1 << (idx & 31))
		self.ones = self.ones + 1 -- 把 self.ones 加 1 写入 self.ones
	end -- 终点
end -- 终点
function Bitset:unfix(idx) -- function Bitset:unfix(idx)
	if self:get(idx) == 1 then -- 若 self:get(idx) 等于 1 then
		self.words[(idx >> 5) + 1] = (self.words[(idx >> 5) + 1] or 0) & ~(1 << (idx & 31))
		self.ones = self.ones - 1 -- 把 self.ones 减 1 写入 self.ones
	end -- 终点
end -- 终点
function Bitset:flip() -- function Bitset:flip()
	self.reverse = self.reverse ~ 1 -- 把 self.reverse ~ 1 写入 self.reverse
	self.ones = self.n - self.ones -- 把 self.元素个数 减 self.ones 写入 self.ones
end -- 终点
function Bitset:all()
	return self.ones == self.n
end -- 把 赋值为 self.元素个数 终点 写入 function Bitset:all() return self.ones
function Bitset:one()
	return self.ones > 0
end -- function Bitset:one() return self.ones 超过 0 终点
function Bitset:count()
	return self.ones
end -- function Bitset:计数() return self.ones 终点
function Bitset:tostring() -- function Bitset:tostring()
	local s = {} -- 把 {} 写入 local s
	for i = 0, self.n - 1 do
		s[#s + 1] = tostring(self:get(i))
	end -- 让 下标 i 从 0 走到 self（Lua 1 基）
	return table.concat(s) -- 返回 table.concat(字符串)
end -- 终点
local bs = Bitset.new(5) -- 把 Bitset.new(5) 写入 local bs
bs:fix(0)
bs:fix(3) -- bs:fix(0); bs:fix(3)
assert(bs:tostring() == "10010") -- 断言校验
assert(bs:count() == 2) -- 断言校验
bs:flip() -- bs:flip()
assert(bs:tostring() == "01101") -- 断言校验
assert(bs:count() == 3) -- 断言校验
bs:unfix(0) -- bs:unfix(0)
assert(bs:tostring() == "01101") -- 断言校验
assert(bs:all() == false and bs:one() == true) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
