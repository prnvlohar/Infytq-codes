def encode(message):
    output=''
    privious=message[0]
    i=1
    count=1
    while len(message)>i:
        if privious==message[i]:
            count+=1
        else:
            output+=str(count)+privious
            count=1
            privious=message[i]

        if i==len(message)-1:
            output += str(count) + privious
        i+=1
    if len(message)==1:
        output += str(count) + privious
    return output

#Provide different values for message and test your program
encoded_message=encode("ABCDE")
print(encoded_message)