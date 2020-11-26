def calculating_trans(price_num, commission=0.0):
    sum_trans = 0
    sum_com_trans = 0
    for i in range(len(price_num)):
        sum_trans += float(price_num[i])
        sum_com_trans += float(price_num[i]) * commission / 100
    return sum_trans, sum_com_trans


print("Привет! Это калькулятор доходности по акциям.\n"
      "Введи какую комиссию берёт брокер за сделку: ")
commission_trans = float(input())

print("Введи через пробел, цены покупки акции: ")
price_trans_purchase = str(input())
price_trans_purchase_list = price_trans_purchase.split()
sum_trans_ptp, sum_com_trans_ptp = calculating_trans(price_trans_purchase_list, commission_trans)

print("Введи через пробел, цены продажи акции: ")
price_trans_sale = str(input())
price_trans_sale_list = price_trans_sale.split()
sum_trans_pts, sum_com_trans_pts = calculating_trans(price_trans_sale_list, commission_trans)

print("Были ли дивиденды по акции, ответье Да - если были и Нет - если не были: ")
question_dividend = str(input())
if question_dividend == "Да":
    print("Введи через пробел, полученные дивиденды до вычета НДФЛ: ")
    trans_div = str(input())
    trans_div_list = trans_div.split()
    sum_trans_td, sum_com_trans_td = calculating_trans(trans_div_list)
else:
    sum_trans_td = 0
    sum_com_trans_td = 0

print("Потраченные деньги на покупку без комиссии: ", sum_trans_ptp)
print("Полученные деньги без комиссии и дивидендов: ", sum_trans_pts)
print("Комиссии за сделки: ", sum_com_trans_ptp + sum_com_trans_pts)
print("Дивиденды акции: ", sum_trans_td)
com = ((sum_trans_pts + sum_trans_td) - sum_trans_ptp) * 0.13 + sum_com_trans_ptp + sum_com_trans_pts
print("Комиссии и налоги: ", com)
profit = (sum_trans_pts + sum_trans_td) - sum_trans_ptp - com
profit_proc = profit / ((sum_trans_ptp + com) * 0.01)
print("Доход: ", profit, "(", profit_proc, "%)")
