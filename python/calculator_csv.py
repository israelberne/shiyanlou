import sys
import json
import csv

def calculator(income):
    insurance_point = 0.08 + 0.02 + 0.06 + 0.005
    start_point = 5000
    tax_part = income * ( 1 - insurance_point ) - start_point

    if tax_part <= 0:
        tax = 0
    elif tax_part <= 3000:
        tax = tax_part * 0.03
    elif tax_part <= 12000:
        tax = tax_part * 0.1 - 210
    elif tax_part <= 25000:
        tax = tax_part * 0.2 - 1410
    elif tax_part <= 35000:
        tax = tax_part * 0.25 - 2660
    elif tax_part <= 55000:
        tax = tax_part * 0.3 - 4410
    elif tax_part <= 80000:
        tax = tax_part * 0.35 - 7160
    else:
        tax = tax_part * 0.45 - 15160

    salary = income * ( 1 - insurance_point ) - tax
    return '{:.2f}'.format(salary)

def output(data):
    json_str = json.dumps(result)
    with open(sys.argv[2],'w') as f:
        f.write(json_str)

def main():
    result = {}
    data_file = sys.argv[1]
    usr_csv = csv.reader(open(data_file))
    data = list(usr_csv)
    for item in data:
        id, income = item[0],float(item[1])
        income = calculator(income)
        result[id] = income

    output(result)

if __name__ == '__main__':
    main()

