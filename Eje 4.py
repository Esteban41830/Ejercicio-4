class Ventana:
    __Titulo = ''
    __Xsupizquierdo = 0
    __Ysupizquierdo = 0
    __Xinfderecho = 0
    __Yinfderecho = 0
    
    def __init__(self,Titulo,Xsupizquierdo = 0,Ysupizquierdo = 0,Xinfderecho = 0,Yinfderecho = 0):
        self.__Titulo = Titulo
        self.__Xsupizquierdo = Xsupizquierdo
        self.__Ysupizquierdo = Ysupizquierdo
        self.__Xinfderecho = Xinfderecho
        self.__Yinfderecho = Yinfderecho
        
    
    def mostrar(self):
        print('Titulo: {}\nCoordenadas superior izquierdo: ({};{})\nCoordenadas inferior derecho: ({};{})'
              .format(self.__Titulo,self.__Xsupizquierdo,self.__Ysupizquierdo,
                      self.__Xinfderecho,self.__Yinfderecho,))

    def getTitulo(self):
        return self.__Titulo
    
    def alto(self):
        return self.__Ysupizquierdo - self.__Xinfderecho
    
    def ancho(self):
        return self.__Xinfderecho + self.__Xinfderecho
    
    def moverDerecha(self,Valor_movimiento):
        controladorXS = self.__Xinfderecho + Valor_movimiento
        controladorYS = self.__Xinfderecho + Valor_movimiento
        controladorXI = self.__Ysupizquierdo + Valor_movimiento
        controladorYI = self.__Xsupizquierdo + Valor_movimiento
        if (controladorXS >= 0 and controladorYS >= 0)and(controladorXI <=500 and controladorYI <=500):
            self.__Xinfderecho = controladorXS
            self.__Yinfderecho = controladorYS
            self.__Ysupizquierdo = controladorXI
            self.__Xsupizquierdo = controladorYI
        
    def moverIzquierda(self,Valor_movimiento):
        controladorXS = self.__Xinfderecho - Valor_movimiento
        controladorYS = self.__Xinfderecho - Valor_movimiento
        controladorXI = self.__Ysupizquierdo - Valor_movimiento
        controladorYI = self.__Xsupizquierdo - Valor_movimiento
        if (controladorXS >= 0 and controladorYS >= 0)and(controladorXI <=500 and controladorYI <=500):
            self.__Xinfderecho = controladorXS
            self.__Yinfderecho = controladorYS
            self.__Ysupizquierdo = controladorXI
            self.__Xsupizquierdo = controladorYI
        
        
    def bajar(self,Valor_movimiento):
        controladorXS = self.__Xinfderecho - Valor_movimiento
        controladorYS = self.__Xinfderecho - Valor_movimiento
        controladorXI = self.__Ysupizquierdo - Valor_movimiento
        controladorYI = self.__Xsupizquierdo - Valor_movimiento
        if (controladorXS >= 0 and controladorYS >= 0)and(controladorXI <=500 and controladorYI <=500):
            self.__Xinfderecho = controladorXS
            self.__Yinfderecho = controladorYS
            self.__Ysupizquierdo = controladorXI
            self.__Xsupizquierdo = controladorYI
    
    def subir(self,Valor_movimiento):
        controladorXS = self.__Xinfderecho + Valor_movimiento
        controladorYS = self.__Xinfderecho + Valor_movimiento
        controladorXI = self.__Ysupizquierdo + Valor_movimiento
        controladorYI = self.__Xsupizquierdo + Valor_movimiento
        if (controladorXS >= 0 and controladorYS >= 0)and(controladorXI <=500 and controladorYI <=500):
            self.__Xinfderecho = controladorXS
            self.__Yinfderecho = controladorYS
            self.__Ysupizquierdo = controladorXI
            self.__Xsupizquierdo = controladorYI
    
        

if __name__ == '__main__':
    print('==== Ventana Inicio ====')
    ventanaInicio = Ventana('Inicio')
    ventanaInicio.mostrar()
    print('Ventana: {} Alto: {}cm Ancho: {}cm'.format(ventanaInicio.getTitulo(),ventanaInicio.alto(),ventanaInicio.ancho()))
    print('==== Ventana Cargar ====')
    ventanaCargar= Ventana('Cargar',10,20)
    ventanaCargar.mostrar()
    print('*** Mueve a la derecha ***')
    ventanaCargar.moverDerecha(10)
    ventanaCargar.mostrar()
    print('*** Mueve a la izquierda ***')
    ventanaCargar.moverIzquierda(10)
    ventanaCargar.mostrar()
    print('*** Bajar ***')
    ventanaCargar.bajar(10)
    ventanaCargar.mostrar()
    print('==== Ventana Borrar ====')
    ventanaBorrar = Ventana('Borrar', 10,20,100,200)
    ventanaBorrar.mostrar()
    print('*** Subir ***')
    ventanaBorrar.subir(5)
    ventanaBorrar.mostrar()
    print('*** Subir ***')
    ventanaBorrar.subir(6)
    ventanaBorrar.mostrar()
    print('*** Bajar ***')
    ventanaBorrar.bajar(6)
    ventanaBorrar.mostrar()

