if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name , score])
        
sortt = sorted(l , key= lambda x:(x[1],x[0]))

sec_low_g = sorted(set(score for name, score in sortt))[1]

sec_low_stud = [name for name, score in sortt if score == sec_low_g]

for stud in sorted(sec_low_stud):
    print(stud)
    
