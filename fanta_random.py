import csv
import random
import time

print("\033c")
with open('static/lista_mantra.csv', 'r') as file:
    reader = csv.reader(file)
    reader_array = []
    for row in reader:
        reader_array.append(row)

input("⚠️  ⚠️  Premi INVIO per iniziare il sorteggio  ⚠️  ⚠️")
print("\033c")
time.sleep(2)
print('Buona asta 💰 💰 💰')
time.sleep(2)
print("\033c")
count = len(reader_array)
for x in range(count):
    reader_array_len = len(reader_array) 
    random_num = random.randint(0, reader_array_len-1)
    print('\nNome: ' + str(reader_array[random_num][1]))
    print('Ruolo: ' + str(reader_array[random_num][0]))
    print('Squadra: ' + str(reader_array[random_num][2]))
    print('\n\nMacano da estrarre ' + str(reader_array_len-1) + ' giocatori')
    with open('backup/backup.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(reader_array[random_num])
    reader_array.pop(random_num)
    input("\n⚽️ ⚽️  Estrai nuovo giocatore premendo INVIO ⚽️ ⚽️")
    print("\033c")
time.sleep(1)
print('✅ ✅  Asta conclusa, quest\'anno vincerai sicuramente  ✅ ✅\n\n\n\n')