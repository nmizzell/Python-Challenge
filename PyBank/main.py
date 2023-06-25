import csv
import os
import locale

#for formatting decimals as currency
locale.setlocale(locale.LC_ALL, '')

def format_as_currency(amount):
    return locale.currency(amount, grouping=True).replace("(","-").replace(")","")

#set file path for input
dirname = os.path.dirname(__file__)
path = os.path.join(dirname,'Resources/budget_data.csv')

#read input file
with open(path) as csvfile:
    data = csv.reader(csvfile)

    #define variables
    total_months = 0 
    net_pnl = 0
    total_change_pnl = 0
    pnl_change = 0
    greatest_increase_pnl = 0
    greatest_decrease_pnl = 0
    greatest_increase_date = str()
    greatest_decrease_date = str()

    #read csv file, iterate through each row.
    previous_row = None

    for index, row in enumerate(data):
        #skip header row
        if index == 0 :
            pass
        else:

            #first column is the date
            date = row[0]

            #second column is the pnl (profit and loss)
            pnl = float(row[1])

            #add to net total pnl
            net_pnl += pnl
            
            #add one to months
            total_months += 1

            #calculate pnl change based on previous row
            if previous_row[1] == 'Profit/Losses':
                pass
            else:
                pnl_change = pnl - float(previous_row[1])
                total_change_pnl += pnl_change


            #check if the pnl is less than the greatest decrease
            if pnl_change < greatest_decrease_pnl:
                greatest_decrease_pnl = pnl_change
                greatest_decrease_date = date

            if pnl_change > greatest_increase_pnl:
                greatest_increase_pnl = pnl_change
                greatest_increase_date = date



            
        
        #set the previous row equal to the current row at the end of the code. Next iteration, this will be true
        previous_row = row

    avg_change_pnl = total_change_pnl / (total_months-1)

    results = (f'''
          Financial Analysis
          --------------------------
          Total Months: {total_months}
          Total: {format_as_currency(net_pnl)}
          Average Change: {format_as_currency(avg_change_pnl)}
          Greatest Increase in Profits: {greatest_increase_date} ({format_as_currency(greatest_increase_pnl)})
          Greatest Decrease in Profits: {greatest_decrease_date} ({format_as_currency(greatest_decrease_pnl)})
          
          ''')
    
    #print results to terminal
    print(results)
    
    #export results as txt
    with open("Analysis",'w') as f:
        f.write(results)





        


        
