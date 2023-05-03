class Ventana:
    __titulo = ''
    __xsup = 0
    __ysup = 0
    __xinf = 0
    __yinf = 0
    
    
    def __init__(self,titulo = 'ventana',xsup = 0,ysup = 0,xinf = 500,yinf = 500):
        self.__titulo = titulo
        self.__xsup = xsup
        self.__ysup = ysup
        self.__xinf = xinf
        self.__yinf = yinf
    
    def getTitulo(self):
        return self.__titulo
    
    def alto(self):
        return self.__xsup - self.__xinf
    
    def ancho(self):
        return self.__yinf - self.__xinf
        
    def mostrar(self):
        print('Ventana:{}\n Alto: {}\n Ancho{}'.format(self.__titulo,self.alto(),self.ancho()))
    
    def moverDerecha(self,desplazamiento):
        self.__xsup = self.__xsup + desplazamiento
        self.__xinf = self.__xinf + desplazamiento
    
    def moverIzqquierda(self,desplazamiento):
        self.__xsup = self.__xsup - desplazamiento
        self.__xinf = self.__xinf - desplazamiento
    
    def bajar(self,desplazamiento):
        self.__xsup = self.__xsup - desplazamiento
        self.__ysup = self.__ysup - desplazamiento
        self.__xinf = self.__xinf - desplazamiento
        self.__yinf = self.__yinf - desplazamiento
    
    def subir(self,desplazamiento):
        self.__xsup = self.__xsup + desplazamiento
        self.__ysup = self.__ysup + desplazamiento
        self.__xinf = self.__xinf + desplazamiento
        self.__yinf = self.__yinf + desplazamiento





if __name__ == '__main__':
    
    print('====Ventana====')
    ventanaInicio = Ventana('Inicio')
    ventanaInicio.Mostrar()
    print('Ventana:{}\n Alto: {}\n Ancho{}'.fotmat(ventanaInicio.getTitulo(),ventanaInicio.alto(),ventanaInicio.ancho()))
    print('====Ventana Cargar====')
    ventanaCargar = Ventana('Cargar',10,20)
    ventanaCargar.mostrar()
    print('****Mueve derecha****')
    ventanaCargar.moverDerecha(10)
    ventanaCargar.mostrar()
    print('****Mover Izquierda****')
    ventanaCargar.moverIzqquierda(10)
    ventanaCargar.mostrar()
    print('****Bajar****')
    ventanaCargar.bajar(10)
    ventanaCargar.mostrar()
    print('====Ventana Borrar====')
    ventanaBorrar = Ventana('Borrar',10,20,100,200)
    ventanaBorrar.mostrar()
    print('****Subir****')
    ventanaBorrar.subir(5)
    ventanaBorrar.mostrar()
    print('****Subir****')
    ventanaBorrar.subir()
    ventanaBorrar.mostrar()
    print('****Bajar****')
    ventanaBorrar.bajar()
    ventanaBorrar.mostrar()
    
        