from agent import Agent
from random import randint

#get_pos
#apply_logic
#update_state

class Env:
    def __init__(self, row_c, column_c, agent_count):
        self.row_c = row_c
        self.col_c = column_c
        self.agent_count = agent_count
        self.board = [[0 for x in range(column_c)] for y in range(row_c)]
        self.agents = []
        self.cycle = 0
        self.done = False

        for i in range(agent_count):
            while True:
                init_row = randint(0,self.row_c-1)
                init_col = randint(0,self.col_c-1)
                if(self.board[init_row][init_col] != 0):
                    continue
                else:
                    break
            self.board[init_row][init_col] = chr(65+i)
            self.agents.append(Agent(chr(65+i), init_row, init_col, 0))

    def dump_board(self):
        print("current_board:  ")
        print("********************")
        for i in range(self.row_c):
            print ' '.join([str(x) for x in self.board[i]])
        print("********************")

    def get_state(self):
        dic = {}
        for agent in self.agents:
            dic[agent.rep] = (agent.row, agent.col)
        return dic

    def notify_agents(self):
        current_state = self.get_state()
        for agent in self.agents:
            agent.apply_logic(current_state)

    def update_state(self):
        new_pos = []
        for agent in self.agents:
            p_row = agent.row
            p_col = agent.col
            if(agent.move == 'U' and p_row != 0):
                self.board[p_row-1][p_col] = agent.rep
                agent.row = p_row - 1
                new_pos.append((p_row - 1, p_col))
                continue

            if(agent.move == 'D' and p_row != self.row_c - 1):
                self.board[p_row+1][p_col] = agent.rep
                agent.row = p_row + 1
                new_pos.append((p_row + 1, p_col))
                continue

            if(agent.move == 'L' and p_col != 0):
                self.board[p_row][p_col-1] = agent.rep
                agent.col = p_col - 1
                new_pos.append((p_row, p_col - 1))
                continue

            if(agent.move == 'R' and p_col != self.col_c - 1):
                self.board[p_row][p_col+1] = agent.rep
                agent.col = p_col + 1
                new_pos.append((p_row, p_col + 1))
                continue

            self.board[p_row][p_col] = agent.rep

        if(len(new_pos) != len(set(new_pos))):
            self.done = True
        else:
            for i in range(self.row_c):
                for j in range(self.col_c):
                    if not (i,j) in new_pos:
                        self.board[i][j] = 0

    def simulate(self):
        while not self.done:
            self.report()
            self.notify_agents()
            self.update_state()
            self.update_scores()
            self.cycle += 1

    def report(self):
        print("=======================")
        print("cycle:  "+str(self.cycle))
        self.dump_board()
        for agent in self.agents:
            print("score of "+agent.rep+" : "+str(agent.score))
        print("=======================")

    def update_scores(self):
        for agent in self.agents:
            agent.score = self.get_score(agent)

    def get_score(self, agent):
        dist = 0
        for agentt in self.agents:
            dist += agent.get_dist_to(agentt.row, agentt.col)
        return (self.row_c + self.col_c - (float(dist) / len(self.agents)))




