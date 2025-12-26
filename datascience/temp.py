


import matplotlib.pyplot as plt
# plt.plot([1,2,3],[4,5,6])
# plt.show()

def create_vertical_bar_chart():
    years = [x for x in range(1990,2014,2)]
    runs = [x for x in range(500,1700,100)]
    print(years)
    print(runs)
    plt.bar(years,runs)
    plt.xlabel("Year")
    plt.ylabel("Runs Scored")
    plt.title("Sachin Tendulkar's yearly runs")
    plt.show()

# create_vertical_bar_chart()


def create_pie_chart():
    labels = ["Sachine","Sehwag","Kohli","Yuvraj"]
    runs = [18000,800,12000,9500]
    plt.title("score by Indian batsman")
    plt.pie(runs,labels=labels)
    plt.show()

create_pie_chart()

