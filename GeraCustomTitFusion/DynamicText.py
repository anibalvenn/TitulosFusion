#! /usr/bin/env python
# -*- coding: utf-8 -*-

from cgitb import text
from resolvedynamictext import TitleTemplate
import RemoteData

# This proof of concept application demonstrates an aproach in creating
# dynamic title templates for DaVinci Resolve via Fusion Title Templates.
# One button will create a timestamped slate. Another will create a crawl
# with the latest Bundesliga football news obtained via RSS feed.
# It is required to press each button once prior to launching Resolve since
# Resolve only loads the list of available templates once at startup.
# Each subsequent press will refresh the template contents.
# igor@hdhead.com

# Create necessary instances
dtitle = TitleTemplate()
dtitle.getOS()

# Functions actuated by button on-release events


def titleBali(gainers : dict):
    for i in gainers:
        count = 1
        nestedlista = gainers[i]
        lista = nestedlista[0]
        ticker = lista[0]
        nome = lista[1]
        variacao = lista[2]
  
        posX = '0.3904761904762'
        posY =  '0.52111'
    
        dtitle.genTemplate  = 'template_anibal.txt'
        dtitle.templateName = ''.join(('Title', str(i), '.txt'))
        dtitle.replace(variacao, nome, "Arial", "Tahoma", "Bold","Regular", '0.1234','0.1111', '0.2222', '0.3333', '0.4444', posX, posY)
        count =+ count +1

gainers = RemoteData.listaTresPrimeiros()
titleBali(gainers)