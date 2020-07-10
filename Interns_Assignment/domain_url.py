import re

for _ in range(int(input("enter the no.of url"))):
    url=input("Enter the url")

    domain_url=re.findall(r'\/\/?[\w]+\.([^/?].+)$',url)

    for domain in domain_url:      
        print(domain)



##output
'''
enter the no.of url1
Enter the url https://www.google.com 
google.com 
'''
