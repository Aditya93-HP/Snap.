profits = list(map(int, input("Enter the profits separated by space: ").split()))
jobs = input("Enter the jobs separated by space: ").split()
deadlines = list(map(int, input("Enter the deadlines separated by space: ").split()))
profitNjobs = list(zip(profits, jobs, deadlines))
profitNjobs = sorted(profitNjobs, key=lambda x: x[0], reverse=True)
max_deadline = max(deadlines)
slot = [0] * (max_deadline + 1)  
ans = ['null'] * (max_deadline + 1)
total_profit = 0
for i in range(len(profitNjobs)):
    job = profitNjobs[i]
    for j in range(job[2], 0, -1): 
        if slot[j] == 0:
            slot[j] = 1
            ans[j] = job[1]
            total_profit += job[0]
            break
scheduled_jobs = [job for job in ans[1:] if job != 'null']
print("Scheduled jobs:", scheduled_jobs)
print("Total profit:", total_profit)

''' INPUT
Enter the profits separated by space: 100 19 27 25 15
Enter the jobs separated by space: a b c d e
Enter the deadlines separated by space: 2 1 2 1 3
'''
'''OUTPUT
Scheduled jobs: ['c', 'a', 'e']
Total profit: 142
'''