#Problem from HackerRank
#https://www.hackerrank.com/challenges/py-the-captains-room/problem


rooms = [1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2]
num = 5 

def captains_table(rooms, num):
    for i in rooms:
        if rooms.count(i) == 1:
            return i
   

print captains_table(rooms,num)