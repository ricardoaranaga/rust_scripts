from sys import stdin                   #Import stdin library  

flag = 0                                #Flag 0 has only 7-bit characters and 1 has 8-bit characters
                                        #Function to decode binary string
def decode(binary, n):                  #Function takes the binary string and the length
    text = ""                           #Initialize the string variable text to epsilon
    i = 0                               #Create a counter
    while i < len(binary):              #While i is less than lenth of binary string
        byte = binary[i:i + n]          #First chunk of length n (selecting current chars from i to n
        byte = int(byte, 2)             #Decode chunk to ASCII   
        if (byte > 127):                #Has 8-bit characters
            flag = 1                    #Is 8-bit
        if byte == 8:                   #If the current byte is [bs]
            text += chr(byte)           #Add char to the output text string
            text = text[:-2]            #Eliminate the last char because of [bs]
        else:                           #Else
            text += chr(byte)           #Just add the char to the output string
        
        i += n                          #Next chunk of the binary, and loop

    return text                         #Return the built text string


binary = stdin.read().rstrip("\n")      #Read from stdin eliminating the new line

if len(binary) % 8 == 0:                #If 7-bit
    text = decode(binary, 8)            #Function call for 7-bit

if len(binary) % 7 == 0:                #If 8-bit
    text = decode(binary, 7)            #Function call for 8-bit

print("Decoded string:")

if flag == 0:                           #Print if only 7-bit valid characters
    print(text)                         #Output decoded string
if flag == 1:                           #Print if 8-bit characters
    print(text)                         #Output decoded string

