def inPutS():
    a=input() ## input in a single line()
    s,i,f = a.split()
    print(s+" "+ str(int(i)+float(f))) ##type cast i to int, f to float. Add i with f. Typecast the result to string
