"""Kata6: Vasya - Clerk - Can Vasya sell a ticket to each person and 
give the change if he initially has no money and sells the tickets strictly 
in the order people follow in the line? Each of them has a single 100, 50 or 25 
dollars bill, each ticket costs 25 dollars. Return YES or NO.

#1 Best Practice
def tickets(people):
  till = {100.0:0, 50.0:0, 25.0:0}

  for paid in people:
    till[paid] += 1
    change = paid-25.0
    for bill in (50,25):
      while (bill <= change and till[bill] > 0):
        till[bill] -= 1
        change -= bill

    if change != 0:
      return 'NO'
  return 'YES'

"""

# def tickets(people):
#     """Return Yes if there are change No if not."""
#   n25, n50, n100 = 0,0,0
#   for i in range(len(people)):
#     if people[i] == 25:
#       n25+=1
#     if people[i] == 50:
#       n50 += 1
#       if n25 < 1: return "NO"
#       n25 -= 1
#     if people[i] == 100:
#       n100 += 1
#       if n50 >= 1 and n25 >= 1:
#         n50 -= 1
#         n25 -= 1
#       elif n25 >= 3:
#         n25 -= 3
#       else: return "NO"      
#   return "YES"
