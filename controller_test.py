import git, os

#githubアカウントの設定・読み込み
filename = 'config_test.txt'
with open(filename,'r') as f:
  filedata=f.read()
filelist=filedata.split('\n')
#RepositoryのURL取得
if filelist[0]=='addles: ':
  inaddles = input('addlesを入力してください：')
  filelist[0]='addles: '+inaddles+'\n'
else:
  lista=filelist[0].split(' ')
  inaddles = lista[1]
  filelist[0]='addles: '+inaddles+'\n'
#githubのユーザーネームを入力
if filelist[1]=='username: ':
  inusername = input('githubのusernameを入力してください：')
  filelist[1]='username: '+inusername+'\n'
else:
  listu=filelist[1].split(' ')
  inusername = listu[1]
  filelist[1]='username: '+inusername+'\n'
#githubのパスワードを入力
if filelist[2]=='password: ':
  inpassword = input('githubのpasswordを入力してください：')
  filelist[2]='password: '+inpassword
else:
  listp=filelist[2].split(' ')
  inpassword = listp[1]
  filelist[2]='password: '+inpassword
conadd=inaddles[:8]+inusername+':'+inpassword+'@'+inaddles[8:]
print(filelist)
print(conadd)

#config_test.txtに書き込み
with open(filename,'w') as f:
  for i in filelist:
    f.write(i)

#githubのRepositoryをclone
git.Git().clone(conadd)

#ディレクトリのリストを表示
path='.'
os.chdir(inaddles.split('/')[4][:-4])
print(os.listdir(path))
os.chdir('../')
