'''
Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

Note: keep the original order of the names in the output.


'''


def friend(x):
    #Code
    fr=[]
    for name in x:          #choose every name in list
        if (len(name)==4):  # compare length of name, if it is equal to 4
            fr.append(name) # append the name to the already created list fr
    return fr               #return the list to server(driver function)



# it is only the function you have to complete in the online problem on codewars
# driver function is already on  their servers.
