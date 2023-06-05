import csv
import sys
import os
import datetime
from datetime import date

def check_date(yymmdd):
    try:
        new_date = datetime.datetime.strptime(yymmdd, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def csv_input(command_list):
    torihiki_list = []
    torihiki = []
    today = datetime.date.today()
    use_date_2 = today.strftime('%Y-%m-%d')
    item_list = {1:'交通費', 2:'飲食', 3:'食費', 4:'買い物', 5:'入金'}
    debit_list = {1:'費用', 2:'スイカ', 3:'スイカ'}
    credit_list = {1:'スイカ', 2:'カード', 3:'現金'}
    balance_2 = int(input('初期の残高:'))
    while(True):
        print('続けますか？')
        yes_no = input('y/n:')
        if yes_no != 'y':
            break
        print('今の日付:',use_date_2)
        use_date = input('use_date:')
        if use_date == '':
            use_date = use_date_2
        if check_date(use_date):
            use_date_2 = use_date
        else:
            print("入力エラー")
            continue
        print("1:'交通費', 2:'飲食', 3:'食費', 4:'買い物', 5:'入金'")
        try:
            item_n = int(input('item:'))
        except ValueError:
            print("入力エラー")
            continue
        if item_n >= 1 and item_n <= 5:
            item = item_list[item_n]
        else:
            print("入力エラー")
            continue
        print("1:'費用', 2:'スイカ（入金）', 3:'現金（入金）'")
        try:
            debit_n = int(input('debit:'))
        except ValueError:
            print("入力エラー")
            continue
        if debit_n >= 1 and debit_n <= 3:
            debit = debit_list[debit_n]
            credit = credit_list[debit_n]
        else:
            print("入力エラー")
            continue
        print('今の残高:',balance_2)
        try:
            balance = int(input('balance:'))
        except ValueError:
            print("入力エラー")
            continue
        amount = balance_2 - balance
        if amount < 0:
            if item_n == 5 and ((debit_n == 2) or (debit_n == 3)):
                amount *= -1
            else:
                print('入力エラー')
                continue
        balance_2 = balance
        torihiki.append(use_date)
        torihiki.append(item)
        torihiki.append(debit)
        torihiki.append(credit)
        torihiki.append(amount)
        torihiki_list.append(torihiki)
        torihiki = []
    print(torihiki_list)
  
    with open(command_list[0], 'w', newline='') as csvfile:
        w = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in torihiki_list:
            w.writerow(i)
    
if __name__ == '__main__':
    args = sys.argv
    if len(args) == 2:
        del args[0]
        csv_input(args)
    else:
        print('python3 input_suica.py file_name')
