per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму вклада: '))
tkb_deposit = int(per_cent['ТКБ'] * money * 0.01)
skb_deposit = int(per_cent['СКБ'] * money * 0.01)
vtb_deposit = int(per_cent['ВТБ'] * money * 0.01)
sb_deposit = int(per_cent['СБЕР'] * money * 0.01)
print('Размер накопленных процентов за год: ''\n',
      tkb_deposit,
      skb_deposit,
      vtb_deposit,
      sb_deposit
      )
deposit_max = max(tkb_deposit,
                  skb_deposit,
                  vtb_deposit,
                  sb_deposit
                  )
print('Максимальная сумма, которую Вы можете заработать:''\n', deposit_max)