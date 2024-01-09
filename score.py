import os 
def run_files():
    start = 1 
    end = 22

    li = []

    for i in range(start,end+1) :
        if i <9 :
            li.append("math00"+str(i))

        if i > 9 :
            li.append('math0'+str(i))

    for i in li :
        val = os.path.join(i,"solution.py")
    
        # print(val)

        os.system('python3 '+val)


if __name__=="__main__" :
    run_files()

        


