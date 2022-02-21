#!/usr/bin/python3

import dns.resolver
import sys


if len(sys.argv) < 2:
    print("Error! target not mentioned!")
    print(" ")
    print("usage: subby.py <target.com>")
    print("")
    exit(0)


domain = sys.argv[1]


file = open("wordlist.txt","r")
content = file.read()


subdomains = content.splitlines()



def main():
	subdomain_store = []
	for subdoms in subdomains:
		try:
			ip_value = dns.resolver.resolve(f'{subdoms}.{domain}', 'A') 
			if ip_value:
				subdomain_store.append(f'{subdoms}.{domain}')
				if f'{subdoms}.{domain}' in subdomain_store:
						print(f'{subdoms}.{domain}')
				else: 
					pass

		except dns.resolver.NXDOMAIN:
			pass
		except dns.resolver.NoAnswer:
			pass
		except KeyboardInterrupt:
			quit()

if __name__ == "__main__":
	main()
