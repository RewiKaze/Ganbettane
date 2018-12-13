"""Input"""
import csv
import pygal
from pygal.style import Style
def create_graph():
    """create graph using pygal"""
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
            li_minus = []
            for each in li_collect:
                if each.isdigit() == True:
                    place = li_collect.index(each)
                    li_minus.append(int(each) - int(li_collect_ex[place]))
                else:
                    li_minus.append(each)
            print(li_minus) #for check income - expense list

            graph_css = Style(
                colors=['green']
                    )
            line_income = pygal.StackedLine(fill=True, style=graph_css)
            line_income.title = 'รายรับและรายจ่ายที่นำมาลบกันในแต่ละปีของภาคตะวันออกเฉียงเหนือ'
            line_income.x_labels = [2549, 2550, 2552, 2554, 2556, 2558]
            line_income.y_labels = [0, 2000, 4000, 6000, 8000, 10000]
            line_income.add('ยอดสุทธิ', [int(i) for i in li_minus[1::]])
            line_income.render_to_file('Minus_Northeast.svg')
create_graph()
