

seconds = int(input('Введите время в секундах: '))

hh = seconds // 3600
mm = (seconds - hh * 3600) // 60
ss = seconds - hh * 3600 - mm * 60

print(f'{hh}:{mm}:{ss}')