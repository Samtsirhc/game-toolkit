from simple_tools import list_sum
import math
import numpy as np

class RandomEvaluator():
    '''
        Evaluate the randomness of a random series. 
        First, creat a random mode.You need to set the range of the random number: [a, b], int only. 
        After initialize, you can use the evaluate function to evaluate the randomness of your series.
    '''

    def __init__(self, a, b):
        self.min = a
        self.max = b
        self.get_mode_info()
        pass

    def get_mode_info(self):
        self.mode_expection = (self.min + self.max)/2
        self.mode_variance = ((self.min + self.max)**2)/12
        print(f'mode_expection = {self.mode_expection}\nmode_variance = {self.mode_variance}')
    
    def evaluate(self, series:list):
        self.sample = series
        self.sample_sum = list_sum(self.sample)
        self.sample_mean = np.mean(self.sample)
        self.sample_variance = np.var(self.sample)
        print(f'sum = {self.sample_sum}\nmean = {self.sample_mean}\nvariance = {self.sample_variance}')

    def check_randomness(self):
        pass
if __name__ == "__main__":
    a = RandomEvaluator(000, 999)
    with open('pi\\00.txt','r',encoding='utf-8') as f:
        t = f.read()
        tmp = []
        for i in range(1,3000):
            tmp.append(int(t[i * 3:i * 3 + 3]))
        a.evaluate(tmp)