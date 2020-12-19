import os
from execution_time import execution_time
# link task https://adventofcode.com/2020/day/18
path_to_file = os.path.join(".", r"data_task\18.txt")

def read_data(path_to_file):
  with open(path_to_file) as f:
      return [i.replace("\n", "").replace(" ", "") for i in f]


def get_sum(str_s, step):
    sum_all = 1
    list_s = str_s.split("*")
    if step == 1:
        for i in list_s:
          j = i.split("+")
          sum_all = sum_all*int(j[0]) + sum([int(i) for i in j[1:]])
    else:
        list_sum = [sum([int(j) for j in i.split("+")]) for i in list_s]
        for i in list_sum:
          sum_all = sum_all*i
    return sum_all

def get_sum_all_for_str(str_in, step):
    sum_all = 0
    while "(" in str_in:
        index_r = str_in.rindex("(")
        index_l = str_in[index_r + 1:].index(")") + index_r + 1
        str_new = str_in[index_r + 1:index_l]
        sum_str_new = get_sum(str_new, step)
        str_in = str_in[:index_r] + "%s" % sum_str_new + str_in[index_l + 1:]
        sum_all += sum_str_new
    return get_sum(str_in, step)

data = read_data(path_to_file)

@execution_time
def print_solve(test_data, step):
    print("Answer step %s: %s" % (step, sum([get_sum_all_for_str(i, step) for i in test_data])))

print_solve(data, 1)
print_solve(data, 2)

