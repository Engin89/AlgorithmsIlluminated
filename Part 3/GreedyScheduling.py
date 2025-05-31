with open("problem13.4_long.txt", 'r') as infile:
    text = infile.read()
    text_lines = text.splitlines()
    text = text_lines[1:]
jobs = [(float(t.split(" ")[0]), float(t.split(" ")[1])) for t in text]


def GreedyScheduling(tasks, use_diff=True):
    weighted_sum = 0
    duration = 0
    if use_diff:
        schedule = sorted([(i, task[0], task[1], task[0] - task[1]) for i, task in enumerate(tasks, 1)],
                          key=lambda x: (-x[3], -x[1]))
    else:
        schedule = sorted([(i, task[0], task[1], task[0] / task[1]) for i, task in enumerate(tasks, 1)],
                          key=lambda x: (-x[3], -x[1]))
    schedule = [(task[1], task[2]) for task in schedule]
    for task in schedule:
        duration += task[1]
        weighted_sum += duration * task[0]
    return weighted_sum


print(GreedyScheduling(jobs, use_diff=True), GreedyScheduling(jobs, use_diff=False))
