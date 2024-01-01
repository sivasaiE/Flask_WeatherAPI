
def email_slicer(email):
    (name,domain) = str(email).split('@')
    (domain, extension) = str(domain).split('.')
    return ('name: ',name, 'domain: ',domain, 'extension:',extension)
email = input()
print(email_slicer(email))


"THis is for sample testing"