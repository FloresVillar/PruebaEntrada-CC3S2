# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 00:32:10 2023

@author: ESAU FLORES
"""
import numpy
#import math
# entrada de la cantidad de ternas  N 
#en este caso 
# entrada de ternas (altura, x1, x2)
#M= numpy.random.randint(1,30,(20,3))
N=int(input("ingresa la cantidad de ternas")) 
#N=3
#xf-xi>=2
#cumpla con las condiciones
vv=numpy.zeros((N,3),float)
for i in range(N):
    x1=x2=h=0
    print("\tterna %d"%(i+1))
    h=int(input("\ningresa la altura\t"))
    x1=int(input("\ningresa la coordenada inicial(x1)\t"))
    x2=int(input("\ningresa la coordenada final (x2)\t"))
    flag1 = ((x2-x1)<=2)
    while(flag1):
            print("\ningresa coordenadas correctas\t")
            x1=int(input("\ningresa la coordenada inicial(x1)\t"))
            x2=int(input("\ningresa la coordenada final (x2)\t"))
            flag1 = ((x2-x1)<2)
    vv[i]=[h,x1,x2] 
print("las ternas ingresadas son: ")
print(vv)     
#depurando si hay superposicion
N=len(vv)
for k in range(N):
    l=k+1
    while(l<N):
        f1=(vv[l,1]<=vv[k,2] and vv[l,2]>vv[k,1] and vv[k,0]==vv[l,0])
        f2=(vv[l,2]<vv[k,2] and vv[l,2]>vv[k,1] and vv[l,0]==vv[k,0])
        if(f1 or f2):
            print("la plataforma %d se superpone con la plataforma %d"%(l+1,k+1))
            x1=x2=h=0
            print("\tterna %d"%(l+1))
            h=int(input("\ningresa la altura\t"))
            x1=int(input("\ningresa la coordenada inicial(x1)\t"))
            x2=int(input("\ningresa la coordenada final (x2)\t"))
            flag1 = ((x2-x1)<=2)
            while(flag1):
                    print("\ningresa coordenadas correctas\t")
                    x1=int(input("\ningresa la coordenada inicial(x1)\t"))
                    x2=int(input("\ningresa la coordenada final (x2)\t"))
                    flag1 = ((x2-x1)<=2)
            vv[l]=[h,x1,x2]
            l=l
        else: l=l+1
# menor ordenando de acuerdo a las coordenadas x1 en X
N=len(vv)
for i in range(N):
    for j in range(i,0,-1):
        if(vv[j-1,1] > vv[j,1]):
            aux=vv[j,1]
            vv[j,1]=vv[j-1,1]
            vv[j-1,1]=aux
            aux=vv[j,0]
            vv[j,0]=vv[j-1,0]
            vv[j-1,0]=aux
            aux=vv[j,2]
            vv[j,2]=vv[j-1,2]
            vv[j-1,2]=aux
N=len(vv)
suma=0
for i in range(1,N-1):
    if(vv[i,1]>=vv[i-1,1] and vv[i,1]<vv[i-1,2]):
        suma+=(max(vv[i,0],vv[i-1,0]))
        if(vv[i-1,2]<vv[i,2]):
            if(vv[i-1,2]<=vv[i+1,1]):
                suma+=vv[i-1,0]
            else:
                suma+=(max(vv[i-1,0],vv[i+1,0]))
    else:
        2*vv[i-1,0]
        if(vv[i,1]<vv[i+1,1]):
            suma+=vv[i,0]
        else:
            suma+=(max(vv[i,0],vv[i+1,0]))
print("la longitud es %d"%(suma))  

#print(vv)
# #obteniendo longitudes, primera forma , no resulta 
# suma=0
# for i in range(1,N-1):
#     if(vv[i,1]>vv[i-1,1] and vv[i,1]<vv[i-1,2]):
#         suma+=vv[i-1,0]
#         if(vv[i,0]>=vv[i-1,0]):
#             suma+=(vv[i,0]-vv[i-1,0])
#         else:
#             suma+=(vv[i-1,0]-vv[i,0])
#     else:
#         if(vv[i,1]>=vv[i-1,2]):
#             if(vv[i,1]<=vv[i+1,1]):
#                 suma+=vv[i,0]
#             else:
#                 if(vv[i,0]>=vv[i+1,0]):
#                     suma+=(vv[i,0]-vv[i+1,0])
#                 else:
#                     suma+=(vv[i+1,0]-vv[i,0])
#     if(vv[i,2]>vv[i-1,2] and vv[i,2]<vv[i+1,2]):
#         suma+=vv[i+1,0]
#         if(vv[i,2]>=vv[i+1,2]):
#             if(vv[i,0]>vv[i+1,0]):
#                 suma+=vv[i,0]-vv[i+1,0]
#             else:
#                 suma+=vv[i,0]
#         else:
#             suma+=vv[i,0]
#     else:
#         if(vv[i,2]<=vv[i+1,2]):
#             if(vv[i,2]<=vv[i-1,2]):
#                 suma+=(vv[i,0]-vv[i-1,0])
#             else:
#                 suma+=vv[i,0]
#         else: 
#             if(vv[i,2]>=vv[i+1,1] and vv[i,2]<=vv[i+1,2]):
#                 suma+=(vv[i,0]-vv[i+1,0])
# print("la longitud es %d"%(suma))
# #forma alternativa, tener esperanzas
# suma= 0
# N=len(vv)
# for i in range(1,N-1):
#     if(vv[i,1]<vv[i-1,2]):
#         if(vv[i,0]>vv[i-1,0]):
#             suma+=vv[i,0]
#         else:
#             suma+=vv[i-1,0]
#     else:
#         if(vv[i,1]<vv[i+1,1]):
#             suma+=vv[i,0]
#         else:
#             if(vv[i,0]<vv[i+1,0]):
#                 suma+=vv[i+1,0]
#             else:
#                 suma+=vv[i,0]
# print("la longitud es %d"%(suma))        
        
