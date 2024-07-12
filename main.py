None
baza_dannych = {
  'LOL' : 'odpowiedź na coś zabawnego',
  'CRINGE' : 'coś dziwnego lub wstydliwego',
  'ROFL' : 'odpowiedź na żart',
  'SHEESH' : 'lekka dezaprobata',
  'CREEPY' : 'straszny, złowieszczy',
  'AGGRO' : 'stać się agresywnym/zły'
}
print('Wstkie Slowa', baza_dannych)

slowo = input('Napiz slowo ktore zmeiniemy')

if slowo in baza_dannych:
  new_value = input('Podaje nowe slowo:')
  baza_dannych[slowo] = new_value
  print('ASKtualizowa baza dannych: ', baza_dannych)
