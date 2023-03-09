import numpy as np

girdi = np.array([5,8])

agirlik = {'g11': np.array([3,-2]),
           'g12': np.array([4,0.5]),
           'g13': np.array([-1,1]),
           'g2' : np.array([-1,1,2])}

katman_2_girdi = np.array([(girdi * agirlik['g11']).sum(),
                           (girdi * agirlik['g12']).sum(),
                           (girdi * agirlik['g13']).sum()])

katman_2_cikti = np.tanh(katman_2_girdi)

katman_3_girdi = (katman_2_cikti * agirlik['g2']).sum()

cikti = np.tanh(katman_3_girdi)

print('Girdi: ', girdi, '\nKatman 2 Girdi: ', katman_2_girdi,
      '\nKatman 2 Cikti : ', katman_2_cikti,'\nKatman 3 Girdi: ',
      katman_3_girdi, '\nCikti: ',cikti)