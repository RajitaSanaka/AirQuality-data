import matplotlib.pyplot as plt
days = ["Sun","Mon","Tues","Wed","Thu","Fri","Sat"]
air = [100,110,112,98,105,107,108]
plt.plot(days,air,marker = 'o')
plt.xlabel("Days")
plt.ylabel("Air Quality Level")
plt.title("Weekly Air Pollution Analysis")
plt.show()