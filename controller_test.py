#ファイル読み込みテスト
filename = 'text_test.txt'
with open(filename,'r') as f:
  filedata=f.read()
filelist=filedata.split('\n')
print(filelist)
if filelist[0]=='text: ':
  intext = input('textを入力してください：')
  filelist[0]='text: '+intext+'\n'
if filelist[1]=='number: ':
  innumber = input('numberを入力してください：')
  filelist[1]='number: '+innumber
print(filelist)

with open(filename,'w') as f:
  for i in filelist:
    f.write(i)
