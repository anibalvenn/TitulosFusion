Adapatação do código de Igor para criação de títulos Fusion para Davinci REsolve.
Criou-se um template genérico onde as variáveis estão colocadas com plaholders a fim de serem substituídas por seus valores finais.
A variáveis editáveis estão no arquivo resolvedynamictext.py, e são:

        self.inputTextValue  = "<InputText>" #Texto superior
        self.inputTextValue2  = "<InputText2>" #Texto inferior
        self.fontName  = "<FontInput>" #fonte texto superior
        self.fontName2  = "<FontName2>" #fonte texto inferior
        self.fontStyle  = "<FontStyle>" #estilo fonte superior
        self.fontStyle2  = "<FontStyle2>" #estilo fonte inferior
        self.fontSize  = "<FontSize>" #tamanho fonte superior
        self.fontSize2  = "<FontSize2>" #tamanho fonte inferior
        self.redScale  = "<ValueRed>" #valor cor vermelha (RGB)
        self.greenScale  = "<ValueGreen>" #valor cor verde (RGB)
        self.blueScale  = "<ValueBlue>" #valor cor azul (RGB)
        self.positionX = "<PositionX>" #posição em X
        self.positionY = "<PositionY>" #posição em Y

Video exmample: https://www.youtube.com/watch?v=w9l1IFbcxno
