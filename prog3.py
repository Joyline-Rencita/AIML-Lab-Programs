## prog3

dataarr = []
with open('/content/drive/MyDrive/contents/porg3.csv') as f:
  for line in f :
    dataarr.append(line.strip().split(','))

rows = len(dataarr)
cols = len(dataarr[0])
shypo = ['0']*(cols-1)
ghypo = [['?']*(cols-1)]
print("Initial specific hypothesis = ",shypo)
print("Initial general hypothesis = ",ghypo)

for x in range(1,rows):
  lst = dataarr[x]
  if lst[cols-1] == "yes":
    for i in range(0,cols-1):
      if(shypo[i]==lst[i]):
        continue
      shypo[i] = '?' if shypo[i]!='0' else lst[i]
      for g in ghypo:
        if g[i]!='?' and shypo[i]=='?':
          ghypo.remove(g)

  elif lst[cols-1] == "no":
    for i in range(0,cols-1):
      if lst[i] !=shypo[i] and shypo[i]!='?':
        temp_lst = ['?']*i + [shypo[i]] + (['?']*(cols-2-i))
        if temp_lst not in ghypo:
          ghypo.append(temp_lst)

  print("S Hypothesis after row",x, "=",shypo)
  print("G Hypothesis after row",x, "=",ghypo)

print("Final Hypothesis ",shypo)
print("Final Hypothesis ",ghypo)


output:

     sky airTemp humidity    wind water forecast enjoySport
0  sunny    warm   normal  strong  warm     same        yes
1  sunny    warm     high  strong  warm     same        yes
2  rainy    cold     high  strong  warm   change         no
3  sunny    warm     high  strong  cool   change        yes

Initial specific hypothesis =  ['0', '0', '0', '0', '0', '0']
Initial general hypothesis =  [['?', '?', '?', '?', '?', '?']]
S Hypothesis after row 1 = ['sunny', 'warm', 'normal', 'strong', 'warm', 'same']
G Hypothesis after row 1 = [['?', '?', '?', '?', '?', '?']]
S Hypothesis after row 2 = ['sunny', 'warm', '?', 'strong', 'warm', 'same']
G Hypothesis after row 2 = [['?', '?', '?', '?', '?', '?']]
S Hypothesis after row 3 = ['sunny', 'warm', '?', 'strong', 'warm', 'same']
G Hypothesis after row 3 = [['?', '?', '?', '?', '?', '?'], ['sunny', '?', '?', '?', '?', '?'], ['?', 'warm', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', 'same']]
S Hypothesis after row 4 = ['sunny', 'warm', '?', 'strong', '?', '?']
G Hypothesis after row 4 = [['?', '?', '?', '?', '?', '?'], ['sunny', '?', '?', '?', '?', '?'], ['?', 'warm', '?', '?', '?', '?']]
Final Hypothesis  ['sunny', 'warm', '?', 'strong', '?', '?']
Final Hypothesis  [['?', '?', '?', '?', '?', '?'], ['sunny', '?', '?', '?', '?', '?'], ['?', 'warm', '?', '?', '?', '?']]
