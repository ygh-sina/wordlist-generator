#initialize files
one=(open('1.txt', 'r')).readlines()
two=(open('2.txt', 'r')).readlines()
#making the wordlist
wordlist=[]
for word1 in one:
    for word2 in two:
        new=word1+word2
        wordlist.append(new)


   
#arrange the wordlist
wordlist = [item.replace('\r', '').replace('\n', '') for item in wordlist]
print('the wordlist you made:\n',wordlist)
print("SAVED")
WordList='\n'.join(wordlist)
Wlist=open('wordlist.txt','w')
Wlist.write(WordList)

