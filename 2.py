#!/usr/bin/python
# -*- coding: utf-8 -*-

def hex_xor_calc(hexstring1, hexstring2):
    # Função p/ calcular o XOR entre as duas strings codificadas em hexadecimal.
    
    decstring1 = int(hexstring1, 16) #decodifica a primeira
    decstring2 = int(hexstring2, 16) #decodifica a segunda
    xor = decstring1 ^ decstring2 #calcula o xor
    xor_hex = format(xor, 'x') #converte o xor para hexadecimal
    return xor_hex
     


def main():
    # Executa a função
    value = hex_xor_calc("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965") 
    print value


if __name__ == '__main__':
    main()
