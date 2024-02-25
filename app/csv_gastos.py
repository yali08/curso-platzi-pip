import csv

def read_csv(path):
   # Tu código aquí 👇
   with open(path, 'r') as cvsfile:
      reader = csv.reader(cvsfile, delimiter=',')
      g_dic = {n: g for n,g in reader}
      total = 0
      for valor in g_dic.values():
         total += int(valor)
      return total
response = read_csv('./app/gastos.csv')
print(response)