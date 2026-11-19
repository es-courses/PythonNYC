
# contacts = [
#     ['Ann', '689345525', 'ann@nyc.gr'],
#     ['Michael', '699345123', 'mic@nyc.gr'],
#     ['James', '6778543119', 'jam@nyc.gr']
# ]

contacts = {
    "Ann": {'name':'Ann', 'phone':'689345525', 'email':'ann@nyc.gr'},
    'Michael': {'name':'Michael', 'phone':'699345123', 'email':'mic@nyc.gr'},
    'James': {'name':'James', 'phone':'6778543119', 'email':'jam@nyc.gr'}
}

# I want to find the phone of James

contacts['Donald']['phone'] = '654123414'

name = input("Name: ")
if name in contacts:
    print(f"{name} phone is {contacts[name]['phone']}")
else:
    print(f"{name} not found")