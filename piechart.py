from matplotlib import pyplot as plt
labels=["python",'javascript','java', 'ruby','C++']
data = [95,89,65,80,95]
explode =[0.3,0.0,0.1,0.0,0.0]
plt.pie(data, labels=labels, explode=explode)
plt.show()
