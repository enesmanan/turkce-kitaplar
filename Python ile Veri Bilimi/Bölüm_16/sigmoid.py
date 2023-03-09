import numpy as np

# sigmoid aktivasyon fonksiyonu kullanan bir yapay sinir agi ornegi

girdi_1 = np.array([4,5])

agirlik_1 = {'dugum_1': np.array([2,-1]),
             'dugum_2': np.array([1,1])} 

girdi_21 = (girdi_1 * agirlik_1['dugum_1']).sum()
girdi_22 = (girdi_1 * agirlik_1['dugum_2']).sum()

cikti_21 = 1 / (1 + np.exp(-girdi_21))
cikti_22 = 1 / (1 + np.exp(-girdi_22))

cikti_2 = np.array([cikti_21, cikti_22])

agirlik_2 = np.array([2,1])

girdi_3 = (cikti_2 * agirlik_2).sum()

cikti_3 = 1 / (1 + np.exp(-girdi_3))

print('Girdi_21: ',girdi_21,'\nGirdi_22: ', girdi_22,'\nCikti:',cikti_3)