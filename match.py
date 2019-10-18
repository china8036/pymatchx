# -*- coding: cp936 -*-
#opencvģ��ƥ��----��Ŀ��ƥ��
import cv2
#��ȡĿ��ͼƬ
target = cv2.imread("target.png")
#��ȡģ��ͼƬ
template = cv2.imread("template.png")
#���ģ��ͼƬ�ĸ߿�ߴ�
theight, twidth = template.shape[:2]
#ִ��ģ��ƥ�䣬���õ�ƥ�䷽ʽcv2.TM_SQDIFF_NORMED
result = cv2.matchTemplate(target,template,cv2.TM_SQDIFF_NORMED)
#��һ������
cv2.normalize( result, result, 0, 1, cv2.NORM_MINMAX, -1 )
#Ѱ�Ҿ���һά���鵱����������Mat���壩�е����ֵ����Сֵ��ƥ��������λ��
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
#ƥ��ֵת��Ϊ�ַ���
#����cv2.TM_SQDIFF��cv2.TM_SQDIFF_NORMED����min_valԽ������0ƥ���Խ�ã�ƥ��λ��ȡmin_loc
#������������max_valԽ������1ƥ���Խ�ã�ƥ��λ��ȡmax_loc
strmin_val = str(min_val)
#���ƾ��α߿򣬽�ƥ�������ע����
#min_loc�����ζ���
#(min_loc[0]+twidth,min_loc[1]+theight)�����εĿ��
#(0,0,225)�����εı߿���ɫ��2�����α߿���
cv2.rectangle(target,min_loc,(min_loc[0]+twidth,min_loc[1]+theight),(0,0,225),2)
#��ʾ���,����ƥ��ֵ��ʾ�ڱ�������
cv2.imshow("MatchResult----MatchingValue="+strmin_val,target)
cv2.waitKey()
cv2.destroyAllWindows()
