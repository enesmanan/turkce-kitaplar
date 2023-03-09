import numpy as np

girdi = np.array([5,8])

agirlik = {'g11': np.array([3,-2]),
           'g12': np.array([4,0.5]),
           'g13': np.array([-1,1]),
           'g2' : np.array([-1,1,2])}

katman_2 = np.array([(girdi * agirlik['g11']).sum(),
                     (girdi * agirlik['g12']).sum(),
                     (girdi * agirlik['g13']).sum()])

cikti = (katman_2 * agirlik['g2']).sum()

print('Girdi: ', girdi, '\nKatman 2: ', katman_2, '\nCikti: ',cikti)

