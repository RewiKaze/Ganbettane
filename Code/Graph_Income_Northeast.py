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
                if row[0] == 'Northeastern Region':
                    li_collect = []
                    for check in row:
                        li_collect.append(check.replace(',',''))
                    print(li_collect) #for check income list
                    break
            for row_ex in reader_ex:
                if row_ex[0] == 'Northeastern Region':
                    li_collect_ex = []
                    for check in row_ex:
                        li_collect_ex.append(check.replace(',',''))
                    print(li_collect_ex) #for check expense list
                    break
            graph_css = Style(
                    colors=['blue', 'red']
                    )
            line_income = pygal.Line(fill=True, style=graph_css)
            line_income.title = 'รายได้-รายจ่ายของภาคตะวันออกเฉียงเหนือรวมทุกจังหวัดในแต่ละปี'
            line_income.x_labels = [2549, 2550, 2552, 2554, 2556, 2558]
            line_income.y_labels = map(int, range(0, 50001, 5000))
            line_income.add('รายได้', [int(i) for i in li_collect[1::]])
            line_income.add('รายจ่าย', [int(num) for num in li_collect_ex[1::]])
            line_income.render_to_file('Income_Northeastern.svg')
create_graph()
