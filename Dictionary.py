# info = {
#     "name" : "Rafi",
#     "subjects" : ["python", "C", "JAVA"],
#     "topics" : ("dict","set"),
#     "age" : 10
# }
# print(info)
# print(info["name"])          # we can print the value of perticaular key
# info["name"] = "MDR"         # We can reassign the value for our key of dictionary
# info['address'] = "pakbara"  # We can add the new key in our dictionary
# print(info)

#Nested dictionary

# student = {
#     "name" : "Rafi",
#     "Subject" : {
#         "phy" : 88,
#         "Chem" : 98
#     },
#     "Age" : 36
# }
# print(student)                   # Print the whole dictionary
# print(student["Subject"])        # Print the perticular keyvalue
# print(student["Subject"]["phy"]) # Print the perticular keyvalue for nested dictionary
# print(student.keys())            # To print all the keys in dictionary
# print(student.values())          # To print all the values in dictionary
# print(student.items())           # To print all the keys and values in dictionary
# print(student.get("Subject")) 
# student.update({"city" : "delhi"})  # add the new key in dictionary
# print(student)
# #or    
# newdict = {"city" : "delhi"}         # another way to add the new key in dictionary
# student.update(newdict)
# print(student)         
 
# dictionary = {
#             "table" : ("Table","Nilkamal"),
#             "cat"   : "small animal"

# }      
# print(dictionary)
