def processData(num):

    print str(num) + ": ", 

    if num == 1:
        print 1
    else:
        lucky = 1;
        i = 2
        while i <= 2 * num:
            temp = str(i)
            if ("4" not in temp) and ("13" not in temp):
                lucky += 1;

            if lucky == num:
                print i
                return
            i+=1

input_level = [1,2,3,4,5,6,7,10,11,12,13,14,15,31,888]

for item in input_level:
    processData(item)
