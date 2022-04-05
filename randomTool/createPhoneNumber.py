"""
Create PN

"""

import random


class PN:
    def pn():
        list_tel = ['134', '135', '136', '137', '138', '139', '147', '150', '151', '152', '157', '158', '159', '178',
                    '182', '183', '184', '187', '188', '198', '130', '131', '132', '155', '156', '145', '176', '185',
                    '186', '166', '133', '149', '153', '173', '177', '180', '181', '189', '199']
        list_tel1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        tel_mid = '8996'
        phone = random.choice(list_tel) + tel_mid + random.choice(list_tel1) + random.choice(
            list_tel1) + random.choice(list_tel1) + random.choice(list_tel1)
        return phone
