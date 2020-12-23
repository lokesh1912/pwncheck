import argparse
import hashlib
import re
import requests

def pwncheck(x):

    SHA1 = hashlib.sha1(x.encode('utf-8'))
    hash_string = SHA1.hexdigest().upper()
    prefix = hash_string[0:5]

    header = {
        'User-Agent': 'password checker'
    }

    url = "https://api.pwnedpasswords.com/range/{}".format(prefix)

    req = requests.get(url, headers=header).content.decode('utf-8')
    hashes = req.split('\r\n')

    for j in hashes:
        hash_list = re.sub(r':(.*)', "", req).split('\n')

    for i in hash_list:
        real_hash = prefix + i
        
        if hash_string == real_hash:
            print("     [+] Pwned!!!\nYou need to change this password.")
            print("{} - has previously appeared in a data breach. ".format(x))
            break

    if hash_string != real_hash:
        print("     [+]Not pwned!!!")
        print("{} - This password is safe!".format(x))


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--password")
args = parser.parse_args()
argv = vars(args)
p = argv['password']

if args.password:
    print("\n[*] Checking " )
    pwncheck(p)
else:
    print("No password provided\n")
    parser.print_help()