import matplotlib.pyplot as plt

Months=["Jan","Feb","March","April","May","Jun","July","Aug"]
sales=[1200, 2300, 4500, 3200, 3900, 6200, 7900, 5800]

marks_perc = []
for x in sales:
	res = (x/10000)*100
	marks_perc.append(res)

print(marks_perc)

# bar chart 
def percentage_bar_chart():
    plt.bar(sales,marks_perc)
    plt.title("Company Annual Sales Chart")
    plt.xlabel("Months")
    plt.ylabel("Sales")
    plt.show()
percentage_bar_chart()