#!/usr/bin/python
# -*- coding: utf-8 -*-

'''Resumo: este código cria strings com somente um caractere hexadecimal (chave), calcula o xor entre estas e a string dada no problema, retorna o valor em ASCII e verifica se o texto resultante é característico de um texto em inglês comum. Se for, imprime a chave correspondente e o texto.

    O meu método de verificação consiste em dividir o texto resultante em substrings e verificar se não há nada de muito errado com as palavras. Basicamente, eu checo a presença de caracteres especiais (no caso, qualquer coisa além de letras e números) e separo em strings que são (ou não) boas candidatas. Para fazer a checagem, eu antes retiro a pontuação ortográfica das palavras, visto que sinais de pontuação também contam como caracteres especiais, que com grande chance estarão presentes em um texto de inglês comum.
    
    Decidi fazer a checagem dessa forma após imprimir as strings resultantes do XOR em uma lista e verificar que quase todas tinham um grande número de caracteres especiais. Aparentemente, funcionou bem. Certamente há outros métodos mais completos e otimizados, mas por ora esse deu conta do recado, tanto para o problema 3 quanto o problema 4. Com mais tempo, eu poderia testar outros métodos que tenho em mente, como por exemplo a comparação das palavras encontradas nas strings com uma "bag of words" de 3000 palavras mais comuns do inglês, de forma a montar condições com pontuações de palavras encontradas e fornecer o resultado final.
    
    Escolhi como canditatos para a chave os caracteres hexadecimais que vão do número 20 ao 79.'''

given_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

def hex_xor_calc(hexstring1, hexstring2):
    # Função p/ calcular o XOR entre as duas strings codificadas em hexadecimal.
    
    decstring1 = int(hexstring1, 16) #decodifica a primeira em decimal
    decstring2 = int(hexstring2, 16) #decodifica a segunda em decimal
    xor = decstring1 ^ decstring2 #calcula o xor, em decimal
    xor_hex = format(xor, 'x') #converte o xor para hexadecimal
    if len(xor_hex) % 2 == 0: #verifica se a string resultante em hex tem um número de caracteres par (caso contrário não pode ser decodificada)
        return xor_hex.decode("hex")
    else:
        return "odd"
    

def str_creator(x): #função que cria uma string de um caractere hexadecimal sem letras, com o mesmo comprimento da string dada
    
    test = '%d' % (x)
    test_long = len(given_string)*test
        
    if len(test_long) > len(given_string):
            
        return test_long[:len(given_string)] 
    
def str_creator_lett(x): #cria uma string de um caractere hexadecimal com letras, com o mesmo comprimento da string dada
    
    test = '%s' % (x)
    test_long = len(given_string)*test
    
    if len(test_long) > len(given_string):
            
        return test_long[:len(given_string)] 
    
def main():
    
    for j in range(20, 41) + range(41, 61) + range(61, 80): #cria um laço para caracteres hexadecimais entre 20 e 80, sem letras
        
        string = "%s" % (str_creator(j)) #cria a string que será comparada
        final_value = hex_xor_calc(given_string, string) #cria a string que será analisada como texto simples de inglês ou não, que chamarei de candidata.
        if final_value == "odd":
            break
        else:
            split_str = final_value.split() #encontra os espaços dentro da candidata e os usa como separador para substrings;
            for k in  range (0, len(split_str)): #laço para analisar a pontuação (ortográfica) das substrings. Neste laço, substrings com pontuação usual do inglês terão sua pontuação removida.
                split_str_elem = split_str[k]
                count_punct = split_str_elem.count("'") + split_str_elem.count("?") + split_str_elem.count(".") +  split_str_elem.count("!") + split_str_elem.count(",") + split_str_elem.count(":") + split_str_elem.count(";") + split_str_elem.count("\"")
                if count_punct > 0:
                    split_str[k] = split_str[k].replace("'","").replace("?","").replace(".","").replace("!","").replace(",","").replace(":","").replace(";","").replace("\"","")
            
            '''restaram agora somente substrings sem pontuação. Quaisquer outros caracteres especiais não costumam estar presentes em um texto simples de inglês. Portanto, se nas palavras restantes estiver presente algum outro caractere especial, a string será descartada por não ser uma boa candidata'''
            
            for l in range(0, len(split_str)):
                if split_str[l].isalnum() == True:
                    if l == len(split_str)-1:
                        print(j, final_value) #se for uma boa candidata, a chave (em hexadecimal) e a string serão impressas no terminal.
                    continue
                break
            
    '''abaixo segue a repetição do mesmo procedimento anterior, entretanto com caracteres que contém letras e não mais numéricos.'''
    lst = ["2a","2b","2c","2d","2e","2f","3a","3b","3c","3d","3e","3f","4a","4b","4c","4d","4e","4f","5a","5b","5c","5d","5e","5f","6a","6b","6c","6d","6e","6f","7a","7b","7c","7d","7e","7f"]        
    for j in lst:
        
        string = "%s" % (str_creator_lett(j))
        final_value = hex_xor_calc(given_string, string)
        if final_value == "odd":
            break
        else:
            split_str = final_value.split()
            for k in  range (0, len(split_str)):
                split_str_elem = split_str[k]
                count_punct = split_str_elem.count("'") + split_str_elem.count("?") + split_str_elem.count(".") +  split_str_elem.count("!") + split_str_elem.count(",") + split_str_elem.count(":") + split_str_elem.count(";") + split_str_elem.count("\"")
                if count_punct > 0:
                    split_str[k] = split_str[k].replace("'","").replace("?","").replace(".","").replace("!","").replace(",","").replace(":","").replace(";","").replace("\"","")
                    
            for l in range(0, len(split_str)):
                if split_str[l].isalnum() == True:
                    if l == len(split_str)-1:
                        print(j, final_value)
                    continue
                break
    

if __name__ == '__main__':
    main()
