from aocd import data, submit

data_list = list(map(int, data.split("\n")))

def two_sum_2020(d):
    for i in range(len(d)):
        for j in range(i, len(d)):
            if d[i]+d[j] == 2020:
                return d[i]*d[j]
#submit(two_sum_2020(data_list), part="a", day=1, year=2020)



def three_sum_2020(d):
    for i in range(len(d)):
        for j in range(i, len(d)):
            for k in range(j, len(d)):
                if d[i]+d[j]+d[k] == 2020:
                    return d[i]*d[j]*d[k]
submit(three_sum_2020(data_list), part="b", day=1, year=2020)
