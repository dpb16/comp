def knapsack(max_wt,profit,wt):
    n=len(wt)
    table=[[0 for x in range(max_wt+1)] for x in range(n+1) ]
    
    for i in range(n+1):
        for j in range(max_wt+1):
             
            if i==0 or j==0:
                table[i][j]=0
            elif wt[i-1]<=j:
                table[i][j]=max(profit[i-1]+table[i-1][j-wt[i-1]],table[i-1][j])
            else:
                table[i][j]=table[i-1][j]
    selected_items=[]
    temp=max_wt            
    
    for i in range(n,0,-1):
        if table[i][temp]!=table[i-1][temp]:
            selected_items.append((i-1,profit[i-1],wt[i-1]))
            temp-=wt[i-1]

        
    return table[n][max_wt],selected_items
                

profit=[10, 5, 15, 7, 6, 18, 3]
wt=[2, 3, 5, 7, 1, 4, 1]
max_wt=15
print(knapsack(max_wt,profit,wt))