import os #Importa o módulo ou biblioteca
print("#" * 60) #Imprimindo # 60 vezes
ip_ou_host = input("Digite o IP ou o Host a ser verificado: ") #Variável que recebe o IP ou o Host
print("-" * 60) #Imprimindo - 60 vezes
os.system('ping -n 6 {}'.format(ip_ou_host)) #Chamando system da biclioteca OS
#-n -num de pacotes que serão 6
print("-" * 60) #Imprimindo - 60 vezes
