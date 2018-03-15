def comss_sort(str,model,flag):
    valuestr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    times = 16/flag
    indexo = 0
    indexj = 1
    while(times > 0):
        for i in range(0+(16/flag-times)*flag,flag/2+(16/flag-times)*flag):
            valuestr[indexo]=str[i]
            valuestr[indexj]=str[i+flag/2]
            i=i+2
            indexo = indexo+2
            indexj = indexj+2
        times=times-1
        indexo = 0+(16/flag-times)*flag
        indexj = 1+(16/flag-times)*flag
    display(valuestr,model)

def display(str,model):
    times = 4
    print "\n",model
    while(times > 0):
        print str[16-times*4],str[17-times*4],str[18-times*4],str[19-times*4]
        times=times-1

a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
display(a,'')
comss_sort(a,"w",16)
comss_sort(a,"c",8)
comss_sort(a,"f",4)

