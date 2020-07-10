# connect a variable above and read its value from the variables dictionary:

import datetime
#def read_event(event):
#  name = event['summary']
#  beginning = event['start']
#  end = event['end']
#  x = ("Apartament: {}, przyjazd: {}, wyjazd: {}".format(name, beginning, end))

#  󰀂v.22-sprzatania󰀂.append(x)

#for event in 󰀂v.0-Events󰀂:
#  read_event(event)
months = ['STYCZEŃ', 'LUTY', 'MARZEC', 'KWIECIEŃ', 'MAJ', 'CZERWIEC', 'LIPIEC', 'SIERPIEŃ', 'WRZESIEŃ', 'PAŹDZIERNIK', 'LISTOPAD', 'GRUDZIEŃ']
today = datetime.datetime.today()
actual_month_name = months[today.month-1]
month_before_name = months[today.month-2]
month_after_name = months[today.month]
try:
  for i in range(len(󰀂v.11-Column_0󰀂)):
  #print("Apartament: {}, Nazwisko: {}, Przyjazd: {}, Wyjazd: {}, Miesiąc".format(󰀂v.13-Column_2󰀂[i], 󰀂v.12-Column_1󰀂[i], 󰀂v.14-Column_3󰀂[i], 󰀂v.15-Column_4󰀂[i], 󰀂v.11-Column_0󰀂[i]))
    if int(󰀂v.15-Column_4󰀂[i]) == today.day+1:  # var check if cleaning is tomorrow
      if 󰀂v.11-Column_0󰀂[i] == actual_month_name:
        if 'GÓRSKI' in 󰀂v.13-Column_2󰀂[i] or 'CICHA' in 󰀂v.13-Column_2󰀂[i] or 'KASPROWICZA' in 󰀂v.13-Column_2󰀂[i] or 'SIENKIEWICZA' in 󰀂v.13-Column_2󰀂[i] or 'SŁONECZNY' in 󰀂v.13-Column_2󰀂[i] or 'PARASOL' in 󰀂v.13-Column_2󰀂[i] or 'KĄCIK' in 󰀂v.13-Column_2󰀂[i] or 'SMREKOWA' in 󰀂v.13-Column_2󰀂[i] or 'GIEWONT' in 󰀂v.13-Column_2󰀂[i] or 'CLASSIC' in 󰀂v.13-Column_2󰀂[i] or 'ZIELONY' in 󰀂v.13-Column_2󰀂[i]:
          x = ("||| {}, Wyjazd: {} - {} |||".format(󰀂v.13-Column_2󰀂[i], 󰀂v.15-Column_4󰀂[i], 󰀂v.11-Column_0󰀂[i]))
          󰀂v.22-sprzatania󰀂.append(x)
          print("Wyjazdy nasze: ", 󰀂v.13-Column_2󰀂[i], 󰀂v.15-Column_4󰀂[i])
  for i in range(len(󰀂v.11-Column_0󰀂)):
  #print("Apartament: {}, Nazwisko: {}, Przyjazd: {}, Wyjazd: {}, Miesiąc".format(󰀂v.13-Column_2󰀂[i], 󰀂v.12-Column_1󰀂[i], 󰀂v.14-Column_3󰀂[i], 󰀂v.15-Column_4󰀂[i], 󰀂v.11-Column_0󰀂[i]))
    if int(󰀂v.15-Column_4󰀂[i]) == today.day+1:  # var check if cleaning is tomorrow for ELA
      if 󰀂v.11-Column_0󰀂[i] == actual_month_name:
        if 'HM2' in 󰀂v.13-Column_2󰀂[i] or 'HS' in 󰀂v.13-Column_2󰀂[i] or 'HSII' in 󰀂v.13-Column_2󰀂[i] or 'HONEYMOON' in 󰀂v.13-Column_2󰀂[i] or 'FOLK' in 󰀂v.13-Column_2󰀂[i] or 'CS' in 󰀂v.13-Column_2󰀂[i] or 'MO' in 󰀂v.13-Column_2󰀂[i]:
          b = ("||| {}, Wyjazd: {} - {} |||".format(󰀂v.13-Column_2󰀂[i], 󰀂v.15-Column_4󰀂[i], 󰀂v.11-Column_0󰀂[i]))
          󰀂v.25-sprzatania_ela󰀂.append(b)
          print("Wyjazdy ELI: ", 󰀂v.13-Column_2󰀂[i], 󰀂v.15-Column_4󰀂[i])
except Exception as e:
  pass

try:
  for i in range(len(󰀂v.11-Column_0󰀂)):
    #print(󰀂v.14-Column_3󰀂)
    if 󰀂v.14-Column_3󰀂[i] > 󰀂v.15-Column_4󰀂[i]:  # var check if arrival was in previous month, write which reserv
      pass
      #print("Przyjazd we miesiącu poprzednim do wyjazdu: Apartament: {}, Nazwisko: {}, Przyjazd: {}, Wyjazd: {}, Miesiąc {}".format(󰀂v.13-Column_2󰀂[i], 󰀂v.12-Column_1󰀂[i], 󰀂v.14-Column_3󰀂[i], 󰀂v.15-Column_4󰀂[i], 󰀂v.11-Column_0󰀂[i]))
    if float(󰀂v.14-Column_3󰀂[i]) == today.day+1:  # var check if arrival is tomorrow
      if 󰀂v.11-Column_0󰀂[i] == actual_month_name:
        if 'GÓRSKI' in 󰀂v.13-Column_2󰀂[i] or 'CICHA' in 󰀂v.13-Column_2󰀂[i] or 'KASPROWICZA' in 󰀂v.13-Column_2󰀂[i] or 'SIENKIEWICZA' in 󰀂v.13-Column_2󰀂[i] or 'SŁONECZNY' in 󰀂v.13-Column_2󰀂[i] or 'PARASOL' in 󰀂v.13-Column_2󰀂[i] or 'KĄCIK' in 󰀂v.13-Column_2󰀂[i] or 'SMREKOWA' in 󰀂v.13-Column_2󰀂[i] or 'GIEWONT' in 󰀂v.13-Column_2󰀂[i] or 'CLASSIC' in 󰀂v.13-Column_2󰀂[i] or 'ZIELONY' in 󰀂v.13-Column_2󰀂[i] or 'HONEYMOON' in 󰀂v.13-Column_2󰀂[i] or 'POMORSKA' in 󰀂v.13-Column_2󰀂[i] or 'GOŚCINNY' in 󰀂v.13-Column_2󰀂[i]:
          y = ("||| {}, Przyjazd: {} - {} |||".format(󰀂v.13-Column_2󰀂[i], 󰀂v.14-Column_3󰀂[i], 󰀂v.11-Column_0󰀂[i]))
          󰀂v.21-przyjazdy󰀂.append(y)
          print("Przyjazdy: ", 󰀂v.13-Column_2󰀂[i], 󰀂v.14-Column_3󰀂[i])
    if 󰀂v.11-Column_0󰀂[i] == month_after_name:
      if 󰀂v.14-Column_3󰀂[i] > 󰀂v.15-Column_4󰀂[i]:
        if float(󰀂v.14-Column_3󰀂[i]) == today.day+1:  #var check if tomorrow arrival is described as next month departure
          print("Przyjazd w miesiącu poprzednim do wyjazdu: Apartament: {}, Nazwisko: {}, Przyjazd: {}, Wyjazd: {}, Miesiąc {}".format(󰀂v.13-Column_2󰀂[i], 󰀂v.12-Column_1󰀂[i], 󰀂v.14-Column_3󰀂[i], 󰀂v.15-Column_4󰀂[i], 󰀂v.11-Column_0󰀂[i]))
          if 'GÓRSKI' in 󰀂v.13-Column_2󰀂[i] or 'CICHA' in 󰀂v.13-Column_2󰀂[i] or 'KASPROWICZA' in 󰀂v.13-Column_2󰀂[i] or 'SIENKIEWICZA' in 󰀂v.13-Column_2󰀂[i] or 'SŁONECZNY' in 󰀂v.13-Column_2󰀂[i] or 'PARASOL' in 󰀂v.13-Column_2󰀂[i] or 'KĄCIK' in 󰀂v.13-Column_2󰀂[i] or 'SMREKOWA' in 󰀂v.13-Column_2󰀂[i] or 'GIEWONT' in 󰀂v.13-Column_2󰀂[i] or 'CLASSIC' in 󰀂v.13-Column_2󰀂[i] or 'ZIELONY' in 󰀂v.13-Column_2󰀂[i] or 'HONEYMOON' in 󰀂v.13-Column_2󰀂[i] or 'POMORSKA' in 󰀂v.13-Column_2󰀂[i] or 'GOŚCINNY' in 󰀂v.13-Column_2󰀂[i]:
            y = ("||| {}, Przyjazd z wyjazdem w nastęonym miesiącu: {} - {}, {}, {} |||".format(󰀂v.13-Column_2󰀂[i], 󰀂v.14-Column_3󰀂[i], actual_month_name, 󰀂v.12-Column_1󰀂[i], 󰀂v.13-Column_2󰀂[i]))
            󰀂v.21-przyjazdy󰀂.append(y)
            print("Przyjazdy: ", 󰀂v.13-Column_2󰀂[i], 󰀂v.14-Column_3󰀂[i])
    if float(󰀂v.14-Column_3󰀂[i]) == today.day+1:  # var check if arrival is tomorrow for ELA
      if 󰀂v.11-Column_0󰀂[i] == actual_month_name:
        if 'HM2' in 󰀂v.13-Column_2󰀂[i] or 'HS' in 󰀂v.13-Column_2󰀂[i] or 'HSII' in 󰀂v.13-Column_2󰀂[i] or 'HONEYMOON' in 󰀂v.13-Column_2󰀂[i] or 'FOLK' in 󰀂v.13-Column_2󰀂[i] or 'CS' in 󰀂v.13-Column_2󰀂[i] or 'MO' in 󰀂v.13-Column_2󰀂[i]:
          a = ("||| {}, Przyjazd: {} - {} |||".format(󰀂v.13-Column_2󰀂[i], 󰀂v.14-Column_3󰀂[i], 󰀂v.11-Column_0󰀂[i]))
          󰀂v.24-przyjazdy_ela󰀂.append(a)
          print("Przyjazdy ELI: ", 󰀂v.13-Column_2󰀂[i], 󰀂v.14-Column_3󰀂[i])
except Exception as e:
  pass