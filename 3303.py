palavra = ''
palavra = str(input()).strip() if len(palavra) <= 20 else exit()
palavrao = ''
palavrinha = ''

if len(palavra) >= 10:
    palavra = palavrao
    print('palavrao')

else:
    palavra = palavrinha
    print('palavrinha')