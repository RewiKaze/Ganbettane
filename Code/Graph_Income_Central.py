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
                if row[0] == 'Greater Bangkok ':
                    li_collect = []
                    for check in row:
                        li_collect.append(check.replace(',',''))

                if row[0] == 'Central Region ':
                    li_collect_2 = []
                    for each in row:
                        li_collect_2.append(each.replace(',',''))
            for row_ex in reader_ex:
                if row_ex[0] == 'Greater Bangkok':
                    li_collect_ex = []
                    for check in row_ex:
                        li_collect_ex.append(check.replace(',',''))
                if row_ex[0] == 'Central Region':
                    li_collect_ex2 = []
                    for each in row_ex:
                        li_collect_ex2.append(each.replace(',',''))
            income_lis = ['Central Region']
            expense_lis = ['Central Region']
            for num in range(1, 7):
                result_income = (int(li_collect[num]) + int(li_collect_2[num])) // 2
                income_lis.append(result_income)
                result_expense = (int(li_collect_ex[num])+ int(li_collect_ex2[num])) // 2
                expense_lis.append(result_expense)
            graph_css = Style(
                    colors=['blue', 'red']
                    )
            line_income = pygal.Line(fill=True, style=graph_css)
            line_income.title = 'รายได้-รายจ่ายของภาคกลางรวมทุกจังหวัดในแต่ละปี'
            line_income.x_labels = [2549, 2550, 2552, 2554, 2556, 2558]
            line_income.y_labels = map(int, range(0, 50001, 5000))
            line_income.add('รายได้', [int(i) for i in income_lis[1::]])
            line_income.add('รายจ่าย', [int(num) for num in expense_lis[1::]])
            line_income.render_to_file('Income_Central.svg')
create_graph()
