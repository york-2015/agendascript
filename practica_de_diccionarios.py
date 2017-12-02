#guardar en un archivo de texto
ob=open('holis.txt', 'w')

#inserta lista
li_1=["hola1","hola2","hola3","hola4"]
li_2=["hola5","hola6","hola7","hola8"]
for e in li_1, li_2:
	ob.write('%s \n' % e)
ob.close()

#nueva lista y quitar saltos de linias
dic=[]
ob=open('holis.txt', 'r')
for i in ob:
	i=i.strip('\n ')
	dic.append(i)

#comparar los resultados
print "esta es la primera lista: \n %s " % li_1
print "esta es la segunda lista: \n %s " % dic
ob.close()

#busqueda de un elemento
print 'Comenzando busqueda.'
ob=open('holis.txt', 'r')
lis_busqueda=[]
for t in ob:
	t=t.strip('\n ')#quita \n y los espacios
	lis_busqueda.append(t)

#buscar elemento queridos
cont=0 
for a in lis_busqueda:
	if a == 'hola5':
		print '%s\n%s\n%s\n%s\n' % (lis_busqueda[cont], lis_busqueda[cont+1], lis_busqueda[cont+2], lis_busqueda[cont+3] ) 	
	cont+=1
ob.close()