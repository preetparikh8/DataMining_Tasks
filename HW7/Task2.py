
# coding: utf-8

# In[1]:

import Orange


raw_data = ["YELLOW,SMALL,STRETCH,ADULT",
"YELLOW,SMALL,STRETCH,CHILD",
"YELLOW,SMALL,DIP,ADULT",
"YELLOW,SMALL,DIP,CHILD",
"YELLOW,LARGE,STRETCH,ADULT",
"YELLOW,LARGE,STRETCH,CHILD",
"YELLOW,LARGE,DIP,ADULT",
"PURPLE,SMALL,DIP,ADULT",
"PURPLE,SMALL,DIP,CHILD",
"PURPLE,LARGE,STRETCH,ADULT",
"PURPLE,LARGE,STRETCH,CHILD",
"PURPLE,LARGE,DIP,ADULT",
"PURPLE,LARGE,DIP,CHILD"]


# write data to the text file: data.basket
f = open('data2.basket', 'w')
for item in raw_data:
    f.write(item + '\n')
f.close()

# Load data from the text file: data.basket
data = Orange.data.Table("data2.basket")


# Identify association rules with supports at least 0.3
rules = Orange.associate.AssociationRulesSparseInducer(data, support = 0.3)


# print out rules
print "%4s %4s  %s" % ("Supp", "Conf", "Rule")
for r in rules[:]:
    print "%4.1f %4.1f  %s" % (r.support, r.confidence, r)


