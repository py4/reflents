import matplotlib.pyplot as plt
class Data:
	def __init__(self, agents):
		self.data = {}
		self.logic = {}
		logics = ['Go to G', 'Random']
		for agent in agents:
			self.logic[agent.rep] = logics[agent.logic_i]
			self.data[agent.rep] = []

	def add_score(self, rep, score):
		self.data[rep].append(score)

	def plot_scores(self, size, count):
		legends = []
		for rep,arr in self.data.items():
			plt.plot(range(len(arr)), arr)
			legends.append(rep+' = '+self.logic[rep])

		plt.xlabel('Cycle')
		plt.ylabel('Score')
		plt.title('Table Size = '+str(size)+"*"+str(size)+" , num of agents: "+str(count))
		plt.legend(legends, loc='upper left')
		plt.show()

