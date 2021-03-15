import numpy as np
import sys
class Module():
  def __init__(self):
    self.unit={} 
    self.unit["M"] = {"M":1,"other":{"tag":"质量","name":"M"}}
    self.unit["L"] = {"L":1,"other":{"tag":"长度","name":"L"}}
    self.unit["T"] = {"T":1,"other":{"tag":"时间","name":"T"}}
    self.unit["A"] = {"A":1,"other":{"tag":"安培","name":"A"}}
    self.unit["K"] = {"K":1,"other":{"tag":"开尔文","name":"K"}}
    self.unit["mol"] = {"mol":1,"other":{"tag":"摩尔","name":"mol"}}
    self.unit["cd"] = {"cd":1,"other":{"tag":"坎德拉","name":"cd"}}

    self.base = ["M","L","T","A","K","mol","cd"]

    self.unit["v"] = {"L":1,"T":-1,"other":{"tag":"速度","name":"v"}}
    self.unit["a"] = {"L":1,"T":-2,"other":{"tag":"加速度","name":"a"}}
    self.unit["N"] = {"M":1,"L":1,"T":-2,"other":{"tag":"牛顿","name":"N"}}
    self.unit["mv"]={"M":1,"L":1,"T":-1,"other":{"tag":"动量","name":"mv"}}
    self.unit["E"] = {"M":1,"L":2,"T":-2,"other":{"tag":"能量","name":"E"}}
    self.unit["J"] = {"M":1,"L":2,"T":-2,"other":{"tag":"焦耳","name":"J"}}
    self.unit["k"] = {"M":1,"T":-2,"other":{"tag":"弹性系数","name":"k"}}
    self.unit["role"] = {"M":1,"L":-1,"other":{"tag":"密度","name":"role"}}
    self.unit["Pa"] = {"M":1,"L":-1,"T":-2,"other":{"tag":"帕斯卡","name":"Pa"}}
    
    self.unit["av"] = {"T":-1,"other":{"tag":"角速度","name":"av"}}
    self.unit["ava"] = {"T":-2,"other":{"tag":"角加速度","name":"ava"}}
    self.unit["Hz"] ={"T":-1,"other":{"tag":"赫兹","name":"Hz"}}
    self.unit["W"] = {"M":1,"L":2,"T":-3,"other":{"tag":"瓦特","name":"W"}}
    self.unit["C"] = {"A":1,"T":1,"other":{"tag":"库伦","name":"C"}}
    self.unit["V"] = {"M":1,"L":2,"T":-3,"A":-1,"other":{"tag":"伏特","name":"V"}}
    self.unit["F"] = {"M":-1,"L":-2,"A":2,"T":4,"other":{"tag":"法拉","name":"F"}}
    self.unit["R"] = {"M":1,"L":2,"T":-3,"A":-2,"other":{"tag":"欧姆","name":"R"}}
    self.unit["H"] = {"M":1,"L":2,"T":-2,"A":-2,"other":{"tag":"亨利","name":"H"}}
    self.unit["Wb"] = {"M":1,"L":2,"T":-2,"A":-1,"other":{"tag":"韦伯","name":"Wb"}}
    self.unit["B"] = {"M":1,"T":-2,"A":-1,"other":{"tag":"特斯拉","name":"B"}}

    self.unit["G"]={"M":-1,"L":3,"T":-2,"other":{"value":[{"amount":6.67*10e-11}],"tag":"万有引力常数","name":"G"}}
    self.unit["g"] = {"L":1,"T":-2,"other":{"value":[{"amount":9.8}],"tag":"重力加速度","name":"g"}}
    self.unit["c"] = {"L":1,"T":-1,"other":{"value":[{"amount":3*10e8}],"tag":"光速","name":"c"}}
    self.unit["h"] = {"M":1,"L":2,"T":-1,"other":{"value":[{"amount",6.626*10e-34}],"tag":"普朗克常数","name":"h"}}
    self.unit["ev"] = {"M":1,"L":-2,"T":-2,"other":{"value":[{"amount":1.602*10e-19,"unit":"J"},
                                             {"amount":10000,"unit":"K"}],"tag":"电子伏特","name":"ev"}}
    self.unit["a0"] = {"L":1,"other":{"value":0.5*10e-10,"tag":"原子距离","name":"a0"}}
    self.unit["E0"] = {"M":1,"L":2,"T":-2,"other":{"value":[{"amount":2,"unit":"ev"}],"tag":"原子能量","name":"E0"}}
    self.unit["Mpc2"] = {"M":1,"L":-1,"T":-2,"other":{"value":[{"amount":10e9,"unit":"ev"}],"tag":"质子能量","name":"Mpc2"}}
    self.unit["Mp"] = {"M":1,"other":{"value":[],"tag":"质子质量","name":"Mp"}}
    self.unit['Mec2'] = {"M":1,"L":-1,"T":-2,"other":{"value":[{"amount":0.5*10e6,"unit":"ev"}],"tag":"电子能量","name":"Mec2"}}

    self.unit["Na"] = {"mol":-1,"other":{"value":[{"amount":6.022*10e-23}],"tag":"阿伏伽德罗常数","name":"Na"}}
    self.unit["kB"] = {"M":1,"L":2,"T":-2,"K":-1,"other":{"value":[{"amount":1.380649*10e-23}],"tag":"玻尔兹曼常数","name":"kB"}}
    
    self.const=["G","g","c","h","ev","a0","E0","Mpc2","Mp","Mec2","Na","kB"]
  
  
  def express(self,arg):
    exp="$"
    if not arg:
        return
    for key in arg:
        if key=="other": continue
        if arg[key]!=0 : exp+=key+"^{"+str(arg[key])+"}"
    exp+="$"
    return exp
  
  
            
  def print(self):
        print("sample:python3 lgfx T M L G ...")
        print("output & input is:")
        for item in self.unit.values():
          print(item["other"]["name"]+"-->"+item["other"]["tag"])
  
  def transArgs(self,arg):
    output=None
    for key,item in self.unit.items():
      if item["other"]["name"]==arg[0]:
         output = item
    if output==None:
      raise Exception("output argument is not correct!")
    input = []
    for key,item in self.unit.items():
      for key1 in arg[1:]:
        if item["other"]["name"]==key1:
           input.append(item)
    if len(input)==0:
      raise Exception("input argument is not correct!")
    return output,input
  def mat_input(self,arg):
        keys=set()
        for mod in arg:
          for key in mod:
            if key=="other":continue
            keys.add(key)
        mat=[]
        for mod in arg:
            arr=[0 for i in range(len(keys))]
            for key1 in mod:
                for i,key2 in enumerate(keys):
                  if key1==key2 :
                    arr[i]=mod[key1]
            mat.append(arr)
        return keys,np.array(mat).T
  def mat_output(self,keys,output):
        lose = set(output.keys())-set(keys)-set(['other'])  
        if len(lose)>0:  #说明输出的量纲数小于等于输入定义的量纲数
          raise Exception("输入参数缺少量纲",lose)
        arr = [0 for i in range(len(keys))]
        for key1 in output:
            for i,key2 in enumerate(keys):
                if key1==key2 :
                    arr[i]=output[key1]
        return np.array(arr)
  
  def resolve(self,output,input):
        keys,i=self.mat_input(input)
        print("输入参数:\n",keys)
        print("矩阵:\n",i)
        if (np.linalg.matrix_rank(i))!=len(keys):
            print("矩阵的rank为"+str(np.linalg.matrix_rank(i))+"，说明方程不可解。需要参数",len(keys),keys,"\n",i)
            return
        if i.shape[0]!=i.shape[1]:
            print("矩阵必须是方阵。",i.shape)
            return
        o = self.mat_output(keys,output)
        print("输出向量:\n",o)
        if i.shape[0]!=len(o):
            print("输入矩阵参数不足输出向量",len(o))
            return
        args=np.linalg.solve(i,o)
        #print(args)
        result={output["other"]["name"]:"="}
        for idx,item in enumerate(input):
            result[item["other"]["name"]]=args[idx]
        return result
        
mod=Module()
args=sys.argv
if len(args)==1:
  mod.print()
else:
  args = mod.transArgs(args[1:])
  result = mod.resolve(args[0],args[1])
  print("结果:\n",result)
  print("latex表达式:\n",mod.express(result))