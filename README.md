# pwncheck - check if you havebeenpwned
pwncheck is a command-line python script to check if your password has been compromised in any one of the breaches online. This python script uses [haveibeenpwned](https://haveibeenpwned.com/API/v3) API to check whether your password was pwned or not. This API uses [K-Anonymity model](https://en.wikipedia.org/wiki/K-anonymity) that allows a password to be searched for by partial hash in order to anonymously verify if a password was pwned, without disclosing the given password.

## Git Installation
```
# Clone the repository
$ git clone https://github.com/lokesh1912/pwncheck.git

# Change the working directory to pwncheck
$ cd pwncheck

# Install the requirements
$ pip install -r requirements.txt
```
## Usage
```
py pwncheck.py -p <your password here>
```

## Example

#### Input

```
py pwncheck.py -p hello123
```

#### Output

```
[*] Checking
     [+] Pwned!!!
You need to change this password.
hello123 - has previously appeared in a data breach.
```
