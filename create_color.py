# -*- coding: utf-8 -*-
from random import randint,choice
chinese_color_l=['#f9f4dc', '#f7e8aa', '#f8df72', '#f8df70', '#fbda41', '#fed71a', '#f7de98', '#f8d86a', '#fcd337', '#fcd217', '#ffd111', '#f6dead', '#f7da94', '#f9d367', '#fbcd31', '#fccb16', '#fecc11', '#fbc82f', '#fcc515', '#fcc307', '#f8c387', '#f7c173', '#fbb929', '#fbb612', '#fcb70a', '#f9a633', '#fba414', '#fca106', '#fca104', '#fc8c23', '#f28e16', '#ff9900', '#fb8b05', '#e9ddb6', '#eed045', '#f2ce2b', '#f1ca17', '#ddc871', '#dfc243', '#e2c027', '#e4bf11', '#d2b42c', '#d2b116', '#b7ae8f', '#ad9e5f', '#8e804b', '#887322', '#867018', '#685e48', '#695e45', '#645822', '#5e5314', '#f9f1db', '#f8e8c1', '#f9d770', '#ffc90c', '#f2e6ce', '#f0d695', '#f4ce69', '#f6c430', '#f9c116', '#f9bd10', '#e5d3aa', '#e8b004', '#ebb10d', '#d9a40e', '#b5aa90', '#b6a476', '#b78d12', '#87723e', '#876818', '#8a6913', '#4a4035', '#4d4030', '#584717', '#5b4913', '#f9e9cd', '#f8e0b0', '#f9d27d', '#feba07', '#f3bf4c', '#f8bc31', '#e2c17c', '#e5b751', '#eaad1a', '#d6a01d', '#b4a992', '#b78b26', '#826b48', '#806332', '#815f25', '#835e1d', '#4f4032', '#503e2a', '#513c20', '#533c1b', '#553b18', '#fbf2e3', '#f9e8d0', '#f9cb8b', '#fbb957', '#ffa60f', '#f4a83a', '#e3bd8d', '#e7a23f', '#daa45a', '#de9e44', '#dc9123', '#c09351', '#97846c', '#986524', '#66462a', '#5d3d21', '#5c3719', '#fbecde', '#f8b37f', '#f97d1c', '#fa7e23', '#f7cdbc', '#f6cec1', '#f0945d', '#f0ada0', '#eeaa9c', '#eea08c', '#ea8958', '#f27635', '#f86b1d', '#ef6f48', '#ef632b', '#f1441d', '#f04b22', '#f2481b', '#f34718', '#f43e06', '#ed5126', '#f09c5a', '#f26b1f', '#d99156', '#db8540', '#de7622', '#c1b2a3', '#be7e4a', '#c1651a', '#918072', '#9a8878', '#945833', '#964d22', '#954416', '#624941', '#64483d', '#71361d', '#753117', '#732e12', '#fc6315', '#e8b49a', '#e46828', '#d85916', '#b7a091', '#b7511d', '#8b614d', '#8c4b31', '#873d24', '#883a1e', '#5b423a', '#603d30', '#673424', '#652b1c', '#692a1b', '#fb9968', '#fc7930', '#edc3ae', '#e16723', '#d4c4b7', '#cf7543', '#cd6227', '#aa6a4c', '#a6522c', '#773d31', '#483332', '#4b2e2b', '#482522', '#481e1c', '#fbeee2', '#f6dcce', '#f7cfba', '#f6ad8f', '#f68c60', '#f9723d', '#fa5d19', '#ee8055', '#cf4813', '#b89485', '#b14b28', '#863020', '#862617', '#592620', '#5a1f1b', '#5c1e19', '#f4c7ba', '#f17666', '#f15642', '#f5391c', '#f25a47', '#f33b1f', '#f2b9b2', '#f19790', '#f05a46', '#f23e23', '#f2cac9', '#efafad', '#f1908c', '#f03f24', '#f0a1a8', '#f1939c', '#f07c82', '#f04a3a', '#f13c22', '#e77c8e', '#ed5a65', '#ed4845', '#ed3b2f', '#ed3321', '#ee4866', '#ee4863', '#ef475d', '#ee3f4d', '#ed3333', '#ec2b24', '#eb261a', '#de2a18', '#d42517', '#ab372f', '#ac1f18', '#5d3131', '#5c2223', '#5a191b', '#5a1216', '#eea2a4', '#ed556a', '#f03752', '#c04851', '#c02c38', '#a7535a', '#7c1823', '#4c1f24', '#4d1018', '#ee2746', '#de1c31', '#d11a2d', '#c45a65', '#c21f30', '#a61b29', '#894e54', '#82202b', '#82111f', '#541e24', '#500a16', '#f8ebe6', '#ec7696', '#ef3473', '#ea7293', '#ec9bad', '#eb507e', '#ed2f6a', '#eeb8c3', '#ea517f', '#f1c4cd', '#ec8aa4', '#ce5777', '#ed9db2', '#ef82a0', '#eb3c70', '#ec2c64', '#e3b4b8', '#cc163a', '#c27c88', '#bf3553', '#73575c', '#621624', '#63071c', '#36282b', '#30161c', '#2b1216', '#2d0c13', '#ce5e8a', '#ec4e8a', '#ee2c79', '#951c48', '#621d34', '#62102e', '#382129', '#381924', '#33141e', '#310f1b', '#eea6b7', '#ef498b', '#de7897', '#de3f7c', '#d13c74', '#c5708b', '#a8456b', '#4b1e2f', '#461629', '#440e25', '#f0c9cf', '#eba0b3', '#ec2d7a', '#e16c96', '#ede3e7', '#e9d7df', '#d2568c', '#d2357d', '#d1c2d3', '#c8adc4', '#c08eaf', '#ba2f7b', '#8076a3', '#806d9e', '#815c94', '#813c85', '#7e1671', '#e9ccd3', '#d276a3', '#cc5595', '#e6d2d5', '#c35691', '#c06f98', '#bdaead', '#b598a1', '#9b1e64', '#856d72', '#4f383e', '#482936', '#f2e7e5', '#e0c8d1', '#bc84a8', '#ad6598', '#a35c8f', '#983680', '#8b2671', '#894276', '#7e2065', '#681752', '#5d3f51', '#4e2a40', '#411c35', '#36292f', '#1e131d', '#1c0d1a', '#f1f0ed', '#e2e1e4', '#ccccd6', '#a7a8bd', '#61649f', '#74759b', '#cfccc9', '#525288', '#2e317c', '#7a7374', '#302f4b', '#3e3841', '#322f3b', '#22202e', '#1f2040', '#131124', '#2775b6', '#2474b5', '#d0dfe6', '#93b5cf', '#619ac3', '#2376b7', '#5698c3', '#2177b8', '#b0d5df', '#8abcd1', '#66a9c9', '#2983bb', '#1772b4', '#63bbd0', '#5cb3cc', '#2486b9', '#1677b3', '#126bae', '#22a2c3', '#1a94bc', '#158bb8', '#1177b0', '#0f59a4', '#2b73af', '#cdd1d3', '#3170a7', '#5e616d', '#475164', '#fffefa', '#35333c', '#0f1423', '#baccd9', '#8fb2c9', '#1661ab', '#c4cbcf', '#15559a', '#4e7ca1', '#346c9c', '#2f2f35', '#2d2e36', '#131824', '#d8e3e7', '#c3d7df', '#2f90b9', '#1781b5', '#c7d2d4', '#11659a', '#c0c4c3', '#b2bbbe', '#5e7987', '#144a74', '#74787a', '#495c69', '#47484c', '#2b333e', '#1c2938', '#142334', '#101f30', '#eef7f2', '#c6e6e8', '#93d5dc', '#51c4d3', '#29b7cb', '#0eb0c9', '#10aec2', '#57c3c2', '#b9dec9', '#83cbac', '#12aa9c', '#66c18c', '#5dbe8a', '#55bb8a', '#45b787', '#2bae85', '#1ba784', '#12a182', '#c4d7d6', '#1e9eb3', '#0f95b0', '#1491a8', '#7cabb1', '#a4aca7', '#869d9d', '#648e93', '#3b818c', '#126e82', '#737c7b', '#617172', '#134857', '#474b4c', '#21373d', '#132c33', '#a4cab6', '#2c9678', '#9abeaf', '#69a794', '#92b3a5', '#248067', '#428675', '#9fa39a', '#8a988e', '#70887d', '#497568', '#5d655f', '#314a43', '#223e36', '#1a3b32', '#363433', '#1f2623', '#141e1b', '#c6dfc8', '#9eccab', '#68b88e', '#20a162', '#61ac85', '#40a070', '#229453', '#cad3c3', '#3c9566', '#20894d', '#83a78d', '#579572', '#207f4c', '#6e8b74', '#1a6840', '#5e665b', '#485b4d', '#393733', '#373834', '#2b312c', '#15231b', '#f0f5e5', '#dfecd5', '#add5a2', '#41b349', '#43b244', '#41ae3c', '#e2e7bf', '#d0deaa', '#b2cf87', '#8cc269', '#b7d07a', '#d2d97a', '#bacf65', '#96c24e', '#e2d849', '#bec936', '#5bae23', '#253d24', '#fffef8', '#f8f4ed', '#fffef9', '#f7f4ed', '#e4dfd7', '#dad4cb', '#bbb5ac', '#bbb5ac', '#867e76', '#847c74', '#80766e', '#81776e']

def random_color_mode_1():
    bg_color_range=[30,60]
    text_color_range=[20,40]
    bg_min,bg_max=int(255*(bg_color_range[0]/100)),int(255*(bg_color_range[1]/100))
    text_min,text_max=int(255*(text_color_range[0]/100)),int(255*(text_color_range[1]/100))
    # 随机背景色
    bg_color_l=[]
    for i in range(3):
        bg_color_l.append(randint(bg_min,bg_max))
    # 随机字体颜色
    add_color_l=[]
    for i in range(3):
        add_color_l.append(randint(text_min,text_max))
        # 把颜色数值加载基本色上
    text_color_l=[]
    for v1,v2 in zip(bg_color_l,add_color_l):
        result=255 if v1+v2 > 255 else v1+v2
        text_color_l.append(result)
    # 两个颜色转十六进制
    convert=lambda x: hex(x).replace('0x','')
    bg_color_result,text_color_result='#','#'
    for v in bg_color_l:
        bg_color_result+=convert(v)
    for v in text_color_l:
        text_color_result+=convert(v)
    return bg_color_result,text_color_result
def random_color_mode_2():
    # 文字颜色都是白色
    text_color_result='#FFFFFF'
    # 背景颜色从中国色里面获取
    bg_color_result=choice(chinese_color_l)
    return bg_color_result,text_color_result