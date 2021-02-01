import math

def slice_pi():
    with open('pi.txt', 'r', encoding='utf-8') as f:
        tmp = f.read()
        print(tmp[:10])
        for i in range(100):
            if i < 10:
                file_name = f'0{i}'
            else:
                file_name = str(i)
            with open(f'{file_name}.txt','w') as f1:
                j = i + 1
                if i == 0:
                    f1.write(tmp[:j*10000])
                    print(tmp[:j*10000])
                elif i == 99:
                    f1.write(tmp[i*10000 + 1:])
                else:
                    f1.write(tmp[i*10000 + 1:j*10000])

def get_prime_number(the_max):
    start = 3
    prime_series = [2]
    for i in range(start, the_max + 1):
        for j in prime_series:
            if i%j == 0:
                break
            if j**2 > i:
                prime_series.append(i)
                break
    return(prime_series)
    

if __name__ == "__main__":
    seed = 1234567890
