class Agent:
	def __init__(self, rep, init_row, init_col, logic_i):
		self.rep = rep
		self.row = init_row
		self.col = init_col
		self.logic_i = logic_i
		self.move = 'N'
		self.score = 0

	def apply_logic(self, current_state):
		if(self.logic_i == 0):
			self.apply_middle(current_state)
		if(self.logic_i == 1):
			self.apply_random(current_state)
		if(self.logic_i == 2):
			self.apply_go_down(current_state)

	def apply_middle(self, current_state):
		r = []
		c = []
		for rep,pos in current_state.items():
			r.append(pos[0])
			c.append(pos[1])

		middle_r = int(reduce(lambda x, y: x + y, r) / len(r))
		middle_c = int(reduce(lambda x, y: x + y, c) / len(c))

		if(middle_r > self.row):
			self.move = 'D'
		elif(middle_r < self.row):
			self.move = 'U'
		elif(middle_c > self.col):
			self.move = 'R'
		elif(middle_c < self.col):
			self.move = 'L'


	#def apply_random(self):
	#def apply_go_down(self):


	def get_dist_to(self, r, c):
		return abs(r - self.row) + abs(c - self.col)


