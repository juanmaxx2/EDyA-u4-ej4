import string
from nodo import Nodo

class Huffman:
    __raiz = None
    __archivo = None

    def Inicio(self):
        archivo = open("archivo.txt", "r")
        texto = ''
        lista = []
        for linea in archivo:
            texto += linea
        archivo.close()
        texto = texto.translate({ord(c): None for c in string.whitespace}).lower()
        for i in range(len(texto)):
            if texto[i] not in lista:
                unNodo = Nodo(texto.count(texto[i]), texto[i])
                lista.append(unNodo)
        lista.sort()
        while len(lista) >= 2:
            NuevoNodo = Nodo(lista[0].getItem()+lista[1].getItem(), lista[0].getCar()+lista[1].getCar())
            NuevoNodo.setIzq(lista[0])
            NuevoNodo.setDer(lista[1])
            lista.pop(0)
            lista.pop(0)
            lista.append(NuevoNodo)
            lista.sort()
        self.__raiz = lista[0]

    def Inorder(self, nodo):
        if nodo != None:
            self.Inorder(nodo.getIzq())
            print(nodo.getCar())
            self.Inorder(nodo.getDer())
    
    def getRaiz(self):
        return self.__raiz