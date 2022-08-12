#! /usr/bin/env python
# -*- coding: utf-8 -*-

# This module allows dynamic text replacement in DaVinci Resolve 15 by
# altering the content of Fusion Title and replacing the .settings file.
# igor@hdhead.com

import os
import sys

class TitleTemplate(object):
	def __init__(self):
	# 	self.placeholder  = '<Token>'
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
		self.positionY = "<PositionY>" #posição em X
		 
		
		# self.genTemplate  = 'GenericTemplate_01.txt'
		self.genTemplate  = 'template_anibal.txt'
		self.templateName = 'TitleTemplate.setting'

	def getOS(self):
		# Evaluate host's OS.
		if sys.platform.startswith('darwin'):
			self.templatePath = '/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Templates/Edit'

		elif sys.platform.startswith('win') or sys.platform.startswith('cygwin'):
			appData = os.getenv('APPDATA')
			self.templatePath = os.path.join(appData, 'Blackmagic Design',
				'DaVinci Resolve', 'Support', 'Fusion', 'Templates','Edit','Titles')

		elif sys.platform.startswith('linux'):
			sys.exit('Linux support not implemented')

	# We'll load the template if exists, replace text string, and save over the original.
	def replace(self, input, input2, fontNome, fontNome2, fontEstilo, fontEstilo2, fontTamanho, fontTamanho2, fontVermelho,
	fontVerde, fontAzul, posicaoX, posicaoY):
		# Open template
		try:
			with open(self.genTemplate, 'r') as templatefile:
				template = templatefile.read()
		except IOError:
			return False

		# Replace string
		template = template.replace(self.inputTextValue, input)
		template = template.replace(self.inputTextValue2, input2)
		template = template.replace(self.fontName, fontNome)
		template = template.replace(self.fontName2, fontNome2)
		template = template.replace(self.fontStyle, fontEstilo)
		template = template.replace(self.fontStyle2, fontEstilo2)
		template = template.replace(self.fontSize, fontTamanho)
		template = template.replace(self.fontSize2, fontTamanho2)
		template = template.replace(self.redScale, fontVermelho)
		template = template.replace(self.greenScale, fontVerde)
		template = template.replace(self.blueScale, fontAzul)
		template = template.replace(self.positionX, posicaoX)
		template = template.replace(self.positionY, posicaoY)

		# Save template
		try:
			t = os.path.join(self.templatePath, self.templateName)
			with open(t, 'w') as templatefile:
				templatefile.write(template)
		except IOError:
			return False

		return True

if __name__ == '__main__':
	# Create a title instance
	title  = TitleTemplate()

	# Evaluate host OS one time
	title.getOS()

	# Replace text
	myText = ''
	myText2 = ''
	myFont = ''
	myFont2 = ''
	myFontStyle = ''
	myFontStyle2 = ''
	myFontSize = 1
	myFontSize2 = 1
	myRed = 1
	myGreen = 1
	myBlue = 1
	mypsX = 1
	mypsY = 1
	title.replace(myText, myText2, myFont, myFont2, myFontStyle, myFontStyle2, myFontSize, myFontSize2, myRed, myGreen, myBlue, mypsX, mypsY)
