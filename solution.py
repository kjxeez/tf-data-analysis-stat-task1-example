import pandas as pd
import numpy as np


chat_id = 584664949 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    mu = np.mean(x)
    return mu/32 # Ваш ответ
