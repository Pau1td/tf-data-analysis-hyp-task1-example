import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

chat_id = 278913153 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    #return ... # Ваш ответ, True или False  

    pval_tz = 0.03

    count = np.array([x_cnt, y_cnt])
    nobs = np.array([x_success, y_success])
    stat, pval = proportions_ztest(count, nobs, alternative='smaller')
    #print('{0:0.3f}'.format(pval))

    if pval < pval_tz:
      return True
    else:
      return False
