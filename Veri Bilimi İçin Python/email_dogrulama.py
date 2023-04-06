import re

# girilen e-postayi duzenler
def normalize_email(email):
    # e-mail için buyuk kucuk harf farketmez
    email = email.lower().strip()
    
    # '@' simgesinin oncesindeki ozel karakterler kaldirilir
    # '.' karakteri kaldirilmaz
    username, domain = email.split('@')
    username = re.sub(r'[^\w.]', '', username)
    
    # e-posta adresini yeniden olustur
    normalized_email = username + '@' + domain
    return normalized_email


def validate_email(email):

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if bool(re.match(pattern, email)):
        return True
    else:
        if '@' not in email:
            print('Gecersiz e-posta adresi. Lutfen \'@\' simgesi iceren bir e-posta adresi giriniz.')
        else:
            return None

def main():

    while True:
        email = input('Lutfen e-posta adresinizi giriniz: ')
        if validate_email(email):
            print('Gecerli e-posta adresi')
            break
        if not validate_email(email):
            tahmin = normalize_email(email)
            print('Lutfen tekrar deneyiniz.', f'\nE-posta adresiniz {tahmin} olabilir mi?')


if __name__ == '__main__':
    main()