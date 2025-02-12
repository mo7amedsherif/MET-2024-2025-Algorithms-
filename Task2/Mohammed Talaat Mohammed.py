cnflct_tbl = [
    {"NumOfInteraction": 30, "Conflict_sub_ID": 200, "sub_ID": 100},
    {"NumOfInteraction": 15, "Conflict_sub_ID": 300, "sub_ID": 200},
]

lvls = [
    {"sub_ID": 100, "level": 1},
    {"sub_ID": 200, "level": 2},
    {"sub_ID": 300, "level": 3},
]

def calculate_final_cost(order, cnflct_tbl):
    total_cost = 0
    for cnflct in cnflct_tbl:
        sub1_indx = order.index(cnflct["sub_ID"])
        sub2_indx = order.index(cnflct["Conflict_sub_ID"])
        if abs(sub1_indx - sub2_indx) == 1:
            total_cost += cnflct["NumOfInteraction"]
    return total_cost

from itertools import permutations
all_orders = permutations([100, 200, 300])

min_cost = float("inf")
best_order = None

for order in all_orders:
    cost = calculate_final_cost(order, cnflct_tbl)
    if cost < min_cost:
        min_cost = cost
        best_order = order

print("bast tidy up:", best_order)
print("less expensive:", min_cost)