
TempStr = input("��������з��ŵ��¶�ֵ��")
if TempStr[-1] in ['f','F']:
    C = (eval(TempStr[0:-1])-32)/1.8
    print("ת������¶���{:.2f}C".format(C))
elif TempStr[-1] in ['c','C']:
    F = 1.8*eval(TempStr[0:-1])+32
    print("ת������¶���{:.2f}F".format(F))
else:
    print("�����ʽ����")