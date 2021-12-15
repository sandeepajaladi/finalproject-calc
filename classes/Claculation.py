import logging
import pandas as pd
import os

from pandas.core.frame import DataFrame

from classes.Addition import Addition
from classes.Subtraction import Subtraction
from classes.Multiplication import Multiplication
from classes.Division import Division
class Calculation:
    src_path = "/Users/sujayjaladi/Downloads/sandeepaflask/"
    
    
    
    def __init__(self,n1,n2,op) :
        self.n1 = n1
        self.n2 = n2
        self.op = op
        self.df = pd.DataFrame(columns=['Number1','Number2','Result','Operation'])
        
        
        
    
    def operation(self):
        if self.op == 'add':
            a1 = Addition(int(self.n1),int(self.n2))

            result = a1.addition()
            #print(self.n1)
            #print(self.df.columns) 
            self.df['Number1'] = [self.n1]
            self.df['Number2'] = [self.n2]
            self.df['Result'] = [result]
            self.df['Operation'] = [a1.__class__.__name__]
            #print(self.df['Number1'])
            df1 = pd.DataFrame(self.df,columns=['Number1','Number2','Result','Operation'])
            op = df1.to_csv(os.path.join(self.src_path,"History.csv"), index=False,mode="a",header=False)
        elif self.op == 'sub':
            a1 = Subtraction(int(self.n1),int(self.n2))
            result = a1.subtraction()
            #print(self.n1)
            #print(self.df.columns) 
            self.df['Number1'] = [self.n1]
            self.df['Number2'] = [self.n2]
            self.df['Result'] = result
            self.df['Operation'] = [a1.__class__.__name__]
            #print(self.df['Number1'])
            df1 = pd.DataFrame(self.df,columns=['Number1','Number2','Result','Operation'])
            op = df1.to_csv(os.path.join(self.src_path,"History.csv"), index=False,mode="a",header=False)
        elif self.op == 'mul':
            a1 = Multiplication(int(self.n1),int(self.n2))
            result = a1.multiplication()
            #print(self.n1)
            #print(self.df.columns) 
            self.df['Number1'] = [self.n1]
            self.df['Number2'] = [self.n2]
            self.df['Result'] = [result]
            self.df['Operation'] = [a1.__class__.__name__]
            #print(self.df['Number1'])
            df1 = pd.DataFrame(self.df,columns=['Number1','Number2','Result','Operation'])
            op = df1.to_csv(os.path.join(self.src_path,"History.csv"), index=False,mode="a",header=False)
            
        else:
            a1 = Division(int(self.n1),int(self.n2))
            result = a1.division()
            #print(self.n1)
            #print(self.df.columns) 
            self.df['Number1'] = [self.n1]
            self.df['Number2'] = [self.n2]
            self.df['Result'] = [result]
            self.df['Operation'] = [a1.__class__.__name__]
            #print(self.df['Number1'])
            df1 = pd.DataFrame(self.df,columns=['Number1','Number2','Result','Operation'])
            op = df1.to_csv(os.path.join(self.src_path,"History.csv"), index=False,mode="a",header=False)
            



            