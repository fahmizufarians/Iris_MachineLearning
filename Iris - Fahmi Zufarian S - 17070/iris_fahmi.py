import csv
import random
import math

with open('C:/Users/Fahmi Zufarian/Downloads/Iris/iris_dataset.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     spamreader = list(spamreader)
       
Theta_1=random.random()
print("Theta_1: %s" % (Theta_1))
Theta_2=random.random()
print("Theta_2: %s" % (Theta_2))
Theta_3=random.random()
print("Theta_3: %s" % (Theta_3))
Theta_4=random.random()
print("Theta_4: %s" % (Theta_4))
Theta_5=random.random()
print("Theta_5: %s" % (Theta_5))
Theta_6=random.random()
print("Theta_6: %s" % (Theta_6))
Theta_7=random.random()
print("Theta_7: %s" % (Theta_7))
Theta_8=random.random()
print("Theta_8: %s" % (Theta_8))
Bias=random.random()
print("Bias : %s" % Bias)
Bias_2=random.random()
print("Bias_2: %s" % Bias_2)

class target:
    def __init__(self, Theta_1, Theta_2,Theta_3,Theta_4,spamreader,Bias):
      self.Theta_1 = Theta_1
      self.Theta_2 = Theta_2
      self.Theta_3 = Theta_3
      self.Theta_4 = Theta_4
      self.spamreader = spamreader
target = []
i=0
for i in range(149):
 target.append(i)
 target[i]=float(spamreader[i][0])*Theta_1+float(spamreader[i][1])*Theta_2+float(spamreader[i][2])*Theta_3+float(spamreader[i][3])*Theta_4+Bias
 print("target1: %s" % (target[i]))
 i = i+1

class target2:
    def __init__(self, Theta_5, Theta_6,Theta_7,Theta_8,spamreader,Bias_2):
      self.Theta_5 = Theta_5
      self.Theta_6 = Theta_6
      self.Theta_7 = Theta_7
      self.Theta_8 = Theta_8
      self.spamreader = spamreader
target2 = []
i=0
for i in range(149):
 target2.append(i)
 target2[i]=float(spamreader[i][0])*Theta_5+float(spamreader[i][1])*Theta_6+float(spamreader[i][2])*Theta_7+float(spamreader[i][3])*Theta_8+Bias_2
 print("target2: %s" % (target2[i]))
 i = i+1

class sigmoid:
    def __init__(self, target):
      self.target = target
sigmoid = []
i=0
for i in range(149):
 sigmoid.append(i)
 sigmoid[i]=1/(1+math.exp(-target[i]))
 print("sigmoid: %s" % (sigmoid[i]))
 i = i+1

class sigmoid_2:
    def __init__(self, target):
      self.target2 = target2
sigmoid2 = []
i=0
for i in range(149):
 sigmoid2.append(i)
 sigmoid2[i]=1/(1+math.exp(-target2[i]))
 print("sigmoid2: %s" % (sigmoid2[i]))
 i = i+1

class prediction:
    def __init__(self, sigmoid):
      self.sigmoid = sigmoid
prediction = []
i=0
for i in range(149):
 prediction.append(i)
 if(sigmoid[i]<float(0.5)):
    prediction[i]=0
    print("prediction: %s" % (prediction[i]))
 else:
    prediction[i]=1
    print("prediction: %s" % (prediction[i]))    
 i = i+1

class prediction2:
    def __init__(self, sigmoid):
      self.sigmoid2 = sigmoid2
prediction2 = []
i=0
for i in range(149):
 prediction2.append(i)
 if(sigmoid2[i]<float(0.5)):
    prediction2[i]=0
    print("prediction2: %s" % (prediction2[i]))
 else:
    prediction2[i]=1
    print("prediction2: %s" % (prediction2[i]))    
 i = i+1

class error:
    def __init__(self, sigmoid, spamreader):
      self.sigmoid = sigmoid
      self.spamreader = spamreader
error = []
i=0
for i in range(149):
 error.append(i)
 error[i]=(sigmoid[i]-float(spamreader[i][5]))*(sigmoid[i]-float(spamreader[i][5]))
 print("error: %s" % (error[i]))
 i = i+1

class error2:
    def __init__(self, sigmoid, spamreader):
      self.sigmoid2 = sigmoid2
      self.spamreader = spamreader
error2 = []
i=0
for i in range(149):
 error2.append(i)
 error2[i]=(sigmoid2[i]-float(spamreader[i][6]))*(sigmoid2[i]-float(spamreader[i][6]))
 print("error2: %s" % (error2[i]))
 i = i+1

class d_theta_1:
	def __init__(self, sigmoid, spamreader):
		self.sigmoid = sigmoid
		self.spamreader= spamreader
d_theta1 = []
i=0
for i in range(149):
 d_theta1.append(i)
 d_theta1[i]=2*(sigmoid[i]-float(spamreader[i][5]))*(1-sigmoid[i])*sigmoid[i]*float(spamreader[i][0])
 print("d_theta_1: %s" % (d_theta1[i]))
 i=i+1

class d_theta_2:
	def __init__(self, sigmoid, spamreader):
		self.sigmoid = sigmoid
		self.spamreader= spamreader
d_theta2 = []
i=0
for i in range(149):
 d_theta2.append(i)
 d_theta2[i]=2*(sigmoid[i]-float(spamreader[i][5]))*(1-sigmoid[i])*sigmoid[i]*float(spamreader[i][1])
 print("d_theta_2: %s" % (d_theta2[i]))
 i=i+1

class d_theta_3:
	def __init__(self, sigmoid, spamreader):
		self.sigmoid = sigmoid
		self.spamreader= spamreader
d_theta3 = []
i=0
for i in range(149):
 d_theta3.append(i)
 d_theta3[i]=2*(sigmoid[i]-float(spamreader[i][5]))*(1-sigmoid[i])*sigmoid[i]*float(spamreader[i][2])
 print("d_theta_3: %s" % (d_theta3[i]))
 i=i+1

class d_theta_4:
	def __init__(self, sigmoid, spamreader):
		self.sigmoid = sigmoid
		self.spamreader= spamreader
d_theta4 = []
i=0
for i in range(149):
 d_theta4.append(i)
 d_theta4[i]=2*(sigmoid[i]-float(spamreader[i][5]))*(1-sigmoid[i])*sigmoid[i]*float(spamreader[i][3])
 print("d_theta_4: %s" % (d_theta4[i]))
 i=i+1

class d_theta_5:
	def __init__(self, sigmoid_2, spamreader):
		self.sigmoid2 = sigmoid2
		self.spamreader= spamreader
d_theta5 = []
i=0
for i in range(149):
 d_theta5.append(i)
 d_theta5[i]=2*(sigmoid2[i]-float(spamreader[i][6]))*(1-sigmoid2[i])*sigmoid2[i]*float(spamreader[i][0])
 print("d_theta_5: %s" % (d_theta5[i]))
 i=i+1

class d_theta_6:
	def __init__(self, sigmoid_2, spamreader):
		self.sigmoid2 = sigmoid2
		self.spamreader= spamreader
d_theta6 = []
i=0
for i in range(149):
 d_theta6.append(i)
 d_theta6[i]=2*(sigmoid2[i]-float(spamreader[i][6]))*(1-sigmoid2[i])*sigmoid2[i]*float(spamreader[i][1])
 print("d_theta_6: %s" % (d_theta6[i]))
 i=i+1

class d_theta_7:
	def __init__(self, sigmoid_2, spamreader):
		self.sigmoid2 = sigmoid2
		self.spamreader= spamreader
d_theta7 = []
i=0
for i in range(149):
 d_theta7.append(i)
 d_theta7[i]=2*(sigmoid2[i]-float(spamreader[i][6]))*(1-sigmoid2[i])*sigmoid2[i]*float(spamreader[i][2])
 print("d_theta_7: %s" % (d_theta7[i]))
 i=i+1

class d_theta_8:
	def __init__(self, sigmoid_2, spamreader):
		self.sigmoid2 = sigmoid2
		self.spamreader= spamreader
d_theta8 = []
i=0
for i in range(149):
 d_theta8.append(i)
 d_theta8[i]=2*(sigmoid2[i]-float(spamreader[i][6]))*(1-sigmoid2[i])*sigmoid2[i]*float(spamreader[i][3])
 print("d_theta_8: %s" % (d_theta8[i]))
 i=i+1

class d_bias:
	def __init__(self, sigmoid, spamreader):
		self.sigmoid = sigmoid
		self.spamreader= spamreader
d_bias = []
i=0
for i in range(149):
 d_bias.append(i)
 d_bias[i]=2*(sigmoid[i]-float(spamreader[i][5]))*(1-sigmoid[i])*sigmoid[i]*1
 print("d_bias: %s" % (d_bias[i]))
 i=i+1 

class d_bias_2:
	def __init__(self, sigmoid, spamreader):
		self.sigmoid2 = sigmoid2
		self.spamreader= spamreader
d_bias2 = []
i=0
for i in range(149):
 d_bias2.append(i)
 d_bias2[i]=2*(sigmoid2[i]-float(spamreader[i][6]))*(1-sigmoid2[i])*sigmoid2[i]*1
 print("d_bias_2: %s" % (d_bias2[i]))
 i=i+1 