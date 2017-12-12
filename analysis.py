#! anaconda3/bin/python
# -*- conding: utf-8 -*-


import json
import pandas as pd


def analysis(file, user_id):
    user_id = int(user_id)
    try:
        df = pd.read_json(file)
    except ValueError:
        return 0, 0
 
    user_info = df[df['user_id'] == user_id]['minutes']
#    print(user_info.count(), user_info.sum())
    return user_info.count(), user_info.sum()


#if __name__ == '__main__':
#    import sys
#    analysis(sys.argv[1], sys.argv[2])

