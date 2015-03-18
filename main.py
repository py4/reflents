from env import Env

initial_size = 30
max_size = 36
size_step = 2
initial_count = 2
max_count = 8
step_count = 2

for size in range(initial_size, max_size, size_step):
    for count in range(initial_count, max_count, step_count):
        env = Env(size, size, count)
        env.simulate()
        env.data.plot_scores(size, count)
