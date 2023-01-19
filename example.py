from dou_extractor import DOUExtractor

douext = DOUExtractor('seu login', 'sua senha') # do usuário criado em https://inlabs.in.gov.br/acessar.php

atos = douext.extract('2023-01-17', '2023-01-19')