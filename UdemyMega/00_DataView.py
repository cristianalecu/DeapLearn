import matplotlib.pyplot as plt
t = [1,2,3,4,5,6,7,8,9,10]
temp = [4,5,5,6,7,6,5,8,9,7]
dewpoint = [2,3,4,5,4,3,2,3,4,5]
plt.plot(t,temp,'red')
plt.plot(t,dewpoint,'blue')
plt.xlabel('Date')                   
plt.title("Temp")
plt.show()

plt.axes([0.05, 0.05, 0.425, 0.9])
plt.plot(t,temp,'red')
plt.xlabel('Date')                   
plt.title("Temp")

plt.axes([0.525, 0.05, 0.425, 0.9])
plt.plot(t,dewpoint,'blue')
plt.xlabel('Date')                   
plt.title("Dew point")
plt.show()

plt.subplot(2,1,1)
plt.plot(t,temp,'red')
plt.xlabel('Date')                   
plt.title("Temp")
plt.subplot(2,1,2)
plt.plot(t,dewpoint,'blue')
plt.xlabel('Date')                   
plt.title("Dew point")
plt.tight_layout()
plt.show()

yr=[1,2,3,4,5,6,7,8,9,10]
pib = [20000,23000,25000,27500,28300,29800,31899, 33697, 35000,36222]
plt.plot(yr,pib, label="PIBs")
plt.xlabel('Year') 
plt.ylabel('Milioane lei') 
plt.title("PIB")  
plt.annotate("best", xy=(4,27500))
plt.annotate("worst", xy=(5,28500), xytext=(6, 27000), arrowprops={'color':'red'})
plt.legend(loc="upper right")
plt.show()

plt.style.use("seaborn-pastel")
plt.plot(yr,pib)
plt.xlabel('Year') 
plt.ylabel('Milioane lei') 
plt.title("PIB")  
plt.xlim(6,8)
plt.ylim(26000,34000)
# same as plt.axis((6,8,26000,34000))
# axis("equal")  (can support also "off", "square", "tight" )

#cs_max = computer_science.max()
#yr_max = year[computer_science.argmax()]
#plt.annotate('Maximum', xy=(yr_max, cs_max), xytext=(yr_max-1, cs_max-10), arrowprops=dict(facecolor='black'))
plt.show()
# plt.savefig("axis_limits.png")

print(plt.style.available)
plt.style.use("seaborn-pastel")
