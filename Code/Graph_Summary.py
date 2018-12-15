"""Input"""
import csv
import pygal
from pygal.style import Style
def create_graph():
    with open('Income(csv).csv') as file:
        reader = csv.reader(file)
        with open('Expenses(csv).csv') as ex_file:
            reader_ex = csv.reader(ex_file)
            for row in reader:
                if row[0] == 'Southern Region':
                    li_collect_south = []
                    for check in row:
                        li_collect_south.append(check.replace(',',''))
                    print(li_collect_south) #for check income list
                if row[0] == 'Northeastern Region':
                    li_collect_northeast = []
                    for check in row:
                        li_collect_northeast.append(check.replace(',',''))
                    print(li_collect_northeast) #for check income list
                if row[0] == 'Northern Region':
                    li_collect_north = []
                    for check in row:
                        li_collect_north.append(check.replace(',',''))
                    print(li_collect_north) #for check income list
                if row[0] == 'Greater Bangkok ':
                    li_collect = []
                    for check in row:
                        li_collect.append(check.replace(',',''))
                if row[0] == 'Central Region ':
                    li_collect_2 = []
                    for each in row:
                        li_collect_2.append(each.replace(',',''))

            for row_ex in reader_ex:
                if row_ex[0] == 'Southern Region':
                    li_collect_ex_south = []
                    for check in row_ex:
                        li_collect_ex_south.append(check.replace(',',''))
                    print(li_collect_ex_south)
                if row_ex[0] == 'Northeastern Region':
                    li_collect_ex_northeast = []
                    for check in row_ex:
                        li_collect_ex_northeast.append(check.replace(',',''))
                    print(li_collect_ex_northeast)
                if row_ex[0] == 'Northern Region':
                    li_collect_ex_north = []
                    for check in row_ex:
                        li_collect_ex_north.append(check.replace(',',''))
                    print(li_collect_ex_north)
                if row_ex[0] == 'Greater Bangkok':
                    li_collect_ex = []
                    for check in row_ex:
                        li_collect_ex.append(check.replace(',',''))
                if row_ex[0] == 'Central Region':
                    li_collect_ex2 = []
                    for each in row_ex:
                        li_collect_ex2.append(each.replace(',',''))

            income_lis_central = ['Central Region']
            expense_lis_central = ['Central Region']
            for num in range(1, 7):
                result_income = (int(li_collect[num]) + int(li_collect_2[num])) // 2
                income_lis_central.append(result_income)
                result_expense = (int(li_collect_ex[num])+ int(li_collect_ex2[num])) // 2
                expense_lis_central.append(result_expense)


    line_chart = pygal.StackedBar()
    line_chart.title = 'Summary Income'
    line_chart.x_label = [2549, 2550, 2552, 2554, 2556, 2558]
    line_chart.add('ภาคกลาง', [int(i) for i in income_lis_central[1::]])
    line_chart.add('ภาคใต้', [int(i) for i in li_collect_south[1::]])
    line_chart.add('ภาคตะวันออกเฉียงเหนือ', [int(i) for i in li_collect_northeast[1::]])
    line_chart.add('ภาคเหนือ', [int(i) for i in li_collect_north[1::]])
    line_chart.render_to_file('bar_summary_income.svg')

    bar_chart = pygal.StackedBar()
    bar_chart.title = 'Summary Expenses'
    bar_chart.x_label = [2549, 2550, 2552, 2554, 2556, 2558]
    bar_chart.add('ภาคกลาง', [int(i) for i in expense_lis_central[1::]])
    bar_chart.add('ภาคใต้', [int(i) for i in li_collect_ex_south[1::]])
    bar_chart.add('ภาคตะวันออกเฉียงเหนือ', [int(i) for i in li_collect_ex_northeast[1::]])
    bar_chart.add('ภาคเหนือ', [int(i) for i in li_collect_ex_north[1::]])
    bar_chart.render_to_file('bar_summary_expense.svg')
create_graph()
