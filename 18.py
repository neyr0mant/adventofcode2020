import os
from leadtime import execution_time

path_to_file = os.path.join(".", r"test_data\18.txt")

def read_data(path_to_file):
  with open(path_to_file) as f:
      return [str_.replace("\n", "").replace(" ", "") for str_ in f]


def get_sum(str_s, first=True):
    sum_all = 1
    list_s = str_s.split("*")
    if first:
        for i in list_s:
          j = i.split("+")
          sum_all = sum_all*int(j[0]) + sum([int(i) for i in j[1:]])
    else:
        list_sum = [sum([int(j) for j in i.split("+")]) for i in list_s]
        for k in list_sum:
          sum_all = sum_all*k
    return sum_all

def get_sum_all_for_str(str_in, first=True):
    sum_all = 0
    while "(" in str_in:
        index_r = str_in.rindex("(")
        index_l = str_in[index_r+1:].index(")") + index_r+1
        str_new = str_in[index_r + 1:index_l]
        sum_str_new = get_sum(str_new, first=first)
        str_in = str_in[:index_r] + "%s" % sum_str_new + str_in[index_l+1:]
        sum_all += sum_str_new
    return get_sum(str_in, first=first)

data = read_data(path_to_file)

@execution_time
def get_solve(test_data, first=True):
    print("Answer step %s: %s" % (1 if first else 2, sum([get_sum_all_for_str(i, first=first) for i in test_data])))

get_solve(data)
get_solve(data, first=False)

