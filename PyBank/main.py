import os
import csv
months = []
total = []
profit = []
difference = []
greatest_increase = []
greatest_decrease = []

budget_data_csv = os.path.join(
    "/Users/saurin/desktop/Resources", "budget_data.csv")
file_to_output = os.path.join(
    "/Users/saurin/Desktop/bootcamp/python-challenge/PyBank", "financial_analysis.text")
with open(budget_data_csv, newline='')as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')

    for row in reader:
        months.append(row["Date"])
        total.append(int(row["Profit/Losses"]))

with open(file_to_output, "w")as txt_file:
    total_months = f"Total Months: {len(months)}"
    print(total_months)
    txt_file.write(total_months)
    total_profit = f"\nTotal: ${sum(total)}"
    print(total_profit)
    txt_file.write(total_profit)

    for i in range(1, len(total)):
        difference.append(total[i] - total[i-1])
    # print(difference)
    # print(sum(difference))
    average_change = round(sum(difference)/(len(months)-1), 2)
    change = f"\nAverage Change: ${average_change}"
    print(change)
    txt_file.write(change)
    greatest_increase = max(difference)
    greatest_decrease = min(difference)
    greatest_increase_month = str(
        months[difference.index(greatest_increase)+1])
    greatest_decrease_month = str(
        months[difference.index(greatest_decrease)+1])

    increase = f"\nGreatest Increase in Profits: {greatest_increase_month} (${greatest_increase})"
    print(increase)
    txt_file.write(increase)
    decrease = f"\nGreatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})"
    print(decrease)
    txt_file.write(decrease)
