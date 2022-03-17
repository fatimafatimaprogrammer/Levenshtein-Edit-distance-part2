#main code that calls levenstein distance method
#opening  the files in read mode to get text
def Levenstein_distance(a,b):
    #defining the rows and cols for 2d matrix which is equal to the length of a and b
    (m,n)= (len(a) , len(b))
 
    #initilizing the array named lev with size equal to (n+1)x (m+1)
    lev = [[0 for x in range(n+1)] for y in range(m+1)]
    
    #populating the row from 1 to m+1 
    for i in range(1, m + 1):
        lev[i][0]= i
       
    #populating the col from 1 to n+1
    for j in range(1, n + 1):
        lev[0][j]= j
      
    #implementing the checks in order to calculate levenstein distance
    for i in range(1,m + 1):
        for j in range(1,n + 1):
            #check
            if a[i-1] == b[j-1]:
                cost = 0
            else:
                cost = 1
                
            #levenstein defination for calculating cost 
            left = lev[i][j-1]
            left_up = lev[i-1][j-1]
            top = lev[i-1][j]
            lev[i][j] = min((left + 1) , (top + 1), (left_up + cost))
            l_dist = lev[i][j]
            #calculating insertions,deletions and subsitutions
            insertions = abs(m - n) - 1
            deletions = abs(m-n) + 1
            subsitutions = l_dist - insertions - deletions

            '''deletions = ()
            if deletions < 0:
                deletions = 0 '''
     
    #printing the 2d matrix to show cost at every point 
    for r in range(n):
        print(lev[r])
           
    #returning the levenstein distance which is the last cost in matrix        
    return l_dist,insertions,deletions,subsitutions

input1 = open('reference.txt','r')
input2 = open('hypothesis.txt','r')
 
#as split method does not works on file operators so first 
#we read data from that file and then split it or tokenize it 
c = input1.read()
d = input2.read()

a = c.split()
b = d.split()
 
res,ins,dels,subs = Levenstein_distance(a,b)
print('levenstein distance is = ' , res )
print('insertions: ',ins)
print('deletions: ',dels)
print('subsitutions: ',subs)

result = open('result.txt','w')
file_output = 'levenstein distance is = '+str(res)+'\nInsertions : '+str(ins)+'\nDeletions : '+str(dels)+'\nSubsitutions : '+str(subs)
result.write(file_output)
