import os

path_to_file = os.path.join(".", r"test_data\18.txt")

def read_data(path_to_file):
  with open(path_to_file) as f:
      return [str_.replace("\n", "") for str_ in f]

def get_summ(str_s, first=True):
  sum_all = 1
  list_s = str_s.replace(" ", "").split("*")
  if first:
    sum_all = 1
    for i in list_s:
      j = i.split("+")
      sum_all = sum_all*int(j[0]) + sum([int(i) for i in j[1:]])
  else:
    list_sum = [sum([int(j) for j in i.split("+")]) for i in list_s]
    for i in list_sum:
      sum_all = sum_all*i
  return sum_all

def get_summ_all_for_str(str_in, first=True):
    summ_all = 0
    while "(" in str_in:
      index_r = str_in.rindex("(")
      index_l = str_in[index_r+1:].index(")") + index_r+1
      str_new = str_in[index_r + 1:index_l]
      sum_str_new = get_summ(str_new, first=first)
      str_in = str_in[:index_r] + "%s" % sum_str_new + str_in[index_l+1:]
      summ_all += sum_str_new
    return get_summ(str_in, first=first)

data = read_data(path_to_file)
print(sum([get_summ_all_for_str(i) for i in data]))
print(sum([get_summ_all_for_str(i, first=False) for i in data]))

