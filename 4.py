#!/usr/bin/python
# -*- coding: utf-8 -*-

'''Este código funciona basicamente como o utilizado no problema 3, mas trabalha com várias strings dadas ao invés de uma só.'''

given_string_len = 60

def hex_xor_calc(hexstring1, hexstring2):
    
    decstring1 = int(hexstring1, 16)  
    decstring2 = int(hexstring2, 16)  
    xor = decstring1 ^ decstring2  
    xor_hex = format(xor, 'x')  
    if len(xor_hex) % 2 == 0:
        return xor_hex.decode("hex")
    else:
        return "odd"
    

def str_creator(x):
    
    test = '%d' % (x)
    test_long = given_string_len*test
        
    if len(test_long) > given_string_len:
            
        return test_long[:given_string_len] 
    
def str_creator_lett(x):
    
    test = '%s' % (x)
    test_long = given_string_len*test
    
    if len(test_long) > given_string_len:
            
        return test_long[:given_string_len] 
    
def main():
    
    f=open("data.txt","r") #abre o arquivo com as strings em linha
    f1 = f.read().splitlines() #separa as strings em uma lista
    
    
    for r in range(0,327): #cria o loop para leitura das várias strings dadas.
    
        for j in range(20, 41) + range(41, 61) + range(61, 80):
            
            string = "%s" % (str_creator(j))
            final_value = hex_xor_calc(f1[r], string)
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
        lst = ["2a","2b","2c","2d","2e","2f","3a","3b","3c","3d","3e","3f","4a","4b","4c","4d","4e","4f","5a","5b","5c","5d","5e","5f","6a","6b","6c","6d","6e","6f","7a","7b","7c","7d","7e","7f"]        
        for j in lst:
            
            string = "%s" % (str_creator_lett(j))
            final_value = hex_xor_calc(f1[r], string)
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
