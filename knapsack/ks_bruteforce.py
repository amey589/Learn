import itertools

# the goal is to pick the items in bag which give max value
# but the bag weight should not be more than BAG_WEIGHT

# each bagged item has tuple structure as (name,weight,value)
a =[("a",6,30),
    ("b",3,14),
    ("c",4,16),
    ("d",2,9)]
print "\n The bagged items are " + str(a)

BAG_MAX_WEIGHT = 12
all_pos = []
for index in range(1,len(a)+1):
    comb = itertools.combinations(a,index)
    for item in comb:
        all_pos.append(item)

#print "\n" + str(all_pos)
#print "\n length of all_pos is " + str(len(all_pos))

w_min = 0 
v_max = 0
winner_tup = None
for item in all_pos:
    total_w = 0
    total_v = 0
    for name,w,v in item:
        total_w = total_w + w
        total_v = total_v + v
    if total_w > BAG_MAX_WEIGHT:
        total_v = 0;
    if total_v > v_max:
        v_max = total_v
        winner_tup = item

print "\n Max bag weight allowed is " + str(BAG_MAX_WEIGHT)
print "\n The v_max is " + str(v_max)
print "\n The winning tuple is " + str(winner_tup)
                
