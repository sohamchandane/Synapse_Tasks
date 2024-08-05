#customers = [[3,7],[5,4],[9,1],[22,3],[24,2]]
#customers = [[6,2],[5,4],[10,3],[20,1]] #SORTING IMPROVES WAITING TIME
#customers = [[5,2],[5,4],[10,3],[20,1]]
#customers = [[1,5],[7,6],[10,3],[16,4]]
customers = [[7,5],[10,7],[19,3],[20,6],[20,5]] #SORTING IMPROVES WAITING TIME

totalTime = 0
waitingTime = []
customers.sort()    #sort to maximise efficiency

'''
Imagine we have 2 customers coming at the same time, 20th minute,
1st customer comes at 20th minute, and his order take 5mins     [20,5]
2nd customer also omes at 20th minute, and his order take 3mins [20,3]
customers = [[20,5], [20,3]]

so waiting time for 1st customer is ***5MINS***, and for 2nd customer it would be ***8MINS***
and the avg would be 
    (5+8)/2 = 6.5 mins

if sorted, the list becomes
customers = [[20,3], [20,5]]
and since both the customers came at the same time, because even the 
smallest improvement in waiting time can bring great joy

so waiting time for each would be ***3MINS*** and ***8MIN*** respectively
and the avg would be 
    (3+8)/2 = 5.5 mins
'''

for time in customers:
    if totalTime > time[0]:
        waitingTime.append(totalTime + time[1] - time[0])
        totalTime += time[1]

    else:
        waitingTime.append(time[1])
        totalTime = sum(time)
#print(waitingTime, totalTime)
print(f"Average waiting time: {sum(waitingTime)/len(waitingTime)}")