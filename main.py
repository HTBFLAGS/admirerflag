from cryptography.fernet import Fernet as frt

key="hBU9lesroX_veFoHz-xUcaz4_ymH-D8p28IP_4rtjq0="
cipher="gAAAAABaDDCRPXCPdGDcBKFqEFz9zvnaiLUbWHqxXqScTTYWfZJcz-WhH7rf_fYHo67zGzJAdkrwATuMptY-nJmU-eYG3HKLO9WDLmO27sex1-R85CZEFCU="

f=frt(key)
output = f.decrypt(cipher.encode('utf-8'))
output_decoded = output.decode('utf-8')
print('decrypted: {0}'.format(output_decoded))