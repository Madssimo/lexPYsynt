
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'SLR'

_lr_signature = 'leftWRITESTRleftWRITETABLAleftWRITELOGleftWRITEINTROleftIDleftDOBLEENTONCESleftENTONCESleftORleftANDrightNOTleftAPARCPARALFANUMERICO AND APAR ASIGNACION CONTRA CPAR CTEXTO DECI DIGITO DOBLEENTONCES ENTONCES ESTERM ID IDENTIFICADOR LETRA NOT NUMERO OR PCOMA TAUTO WRITEINTRO WRITELOG WRITESTR WRITETABLAprog : sentenciassentencias : sentencias sentencia\n                  | sentencia\n                  | emptysentencia : asig PCOMA\n                 | sentwritestr PCOMA\n                 | sentwritelog PCOMA\n                 | sentwriteintro PCOMA\n                 | sentwritetabla PCOMAexpresion : NOT expresion\n                 | expresion DOBLEENTONCES expresion\n                 | expresion ENTONCES expresion\n                 | expresion AND expresion\n                 | expresion OR expresion\n                 | NUMERO\n                 | APAR expresion CPAR\n                 | identificador\n                 | senttauto\n                 | sentcontra\n                 | sentdeciasig : identificador ASIGNACION expresionidentificador : IDsentwriteintro : WRITEINTRO APAR CPARsentwritelog : WRITELOG APAR expresion CPARsentwritestr : WRITESTR APAR CTEXTO CPARsentwritetabla : WRITETABLA APAR matriz CPARmatriz : NOT matriz\n              | matriz DOBLEENTONCES matriz\n              | matriz ENTONCES matriz\n              | matriz AND matriz\n              | matriz OR matriz\n              | APAR matriz CPAR\n              | identificadorsenttauto : TAUTO APAR matriz CPARsentcontra : CONTRA APAR matriz CPARsentdeci : DECI APAR matriz CPARempty :'
    
_lr_action_items = {'$end':([0,1,2,3,4,16,17,18,19,20,21,],[-37,0,-1,-3,-4,-2,-5,-6,-7,-8,-9,]),'WRITESTR':([0,2,3,4,16,17,18,19,20,21,],[11,11,-3,-4,-2,-5,-6,-7,-8,-9,]),'WRITELOG':([0,2,3,4,16,17,18,19,20,21,],[12,12,-3,-4,-2,-5,-6,-7,-8,-9,]),'WRITEINTRO':([0,2,3,4,16,17,18,19,20,21,],[13,13,-3,-4,-2,-5,-6,-7,-8,-9,]),'WRITETABLA':([0,2,3,4,16,17,18,19,20,21,],[14,14,-3,-4,-2,-5,-6,-7,-8,-9,]),'ID':([0,2,3,4,16,17,18,19,20,21,22,24,26,29,31,41,43,45,46,47,48,51,52,53,58,59,60,61,],[15,15,-3,-4,-2,-5,-6,-7,-8,-9,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'PCOMA':([5,6,7,8,9,15,27,28,30,32,33,34,40,49,54,55,57,63,64,65,66,67,76,77,78,],[17,18,19,20,21,-22,-17,-21,-15,-18,-19,-20,-23,-10,-25,-24,-26,-11,-12,-13,-14,-16,-34,-35,-36,]),'ASIGNACION':([10,15,],[22,-22,]),'APAR':([11,12,13,14,22,24,26,29,31,35,36,37,41,43,45,46,47,48,51,52,53,58,59,60,61,],[23,24,25,26,31,31,41,31,31,51,52,53,41,41,31,31,31,31,41,41,41,41,41,41,41,]),'DOBLEENTONCES':([15,27,28,30,32,33,34,39,42,44,49,50,56,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,],[-22,-17,45,-15,-18,-19,-20,45,58,-33,-10,45,58,-27,-11,-12,-13,-14,-16,58,58,58,-32,-28,-29,-30,-31,-34,-35,-36,]),'ENTONCES':([15,27,28,30,32,33,34,39,42,44,49,50,56,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,],[-22,-17,46,-15,-18,-19,-20,46,59,-33,-10,46,59,-27,46,-12,-13,-14,-16,59,59,59,-32,59,-29,-30,-31,-34,-35,-36,]),'AND':([15,27,28,30,32,33,34,39,42,44,49,50,56,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,],[-22,-17,47,-15,-18,-19,-20,47,60,-33,-10,47,60,-27,47,47,-13,47,-16,60,60,60,-32,60,60,-30,60,-34,-35,-36,]),'OR':([15,27,28,30,32,33,34,39,42,44,49,50,56,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,],[-22,-17,48,-15,-18,-19,-20,48,61,-33,-10,48,61,-27,48,48,-13,-14,-16,61,61,61,-32,61,61,-30,-31,-34,-35,-36,]),'CPAR':([15,25,27,30,32,33,34,38,39,42,44,49,50,56,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,],[-22,40,-17,-15,-18,-19,-20,54,55,57,-33,-10,67,71,-27,-11,-12,-13,-14,-16,76,77,78,-32,-28,-29,-30,-31,-34,-35,-36,]),'NOT':([22,24,26,29,31,41,43,45,46,47,48,51,52,53,58,59,60,61,],[29,29,43,29,29,43,43,29,29,29,29,43,43,43,43,43,43,43,]),'NUMERO':([22,24,29,31,45,46,47,48,],[30,30,30,30,30,30,30,30,]),'TAUTO':([22,24,29,31,45,46,47,48,],[35,35,35,35,35,35,35,35,]),'CONTRA':([22,24,29,31,45,46,47,48,],[36,36,36,36,36,36,36,36,]),'DECI':([22,24,29,31,45,46,47,48,],[37,37,37,37,37,37,37,37,]),'CTEXTO':([23,],[38,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,],[1,]),'sentencias':([0,],[2,]),'sentencia':([0,2,],[3,16,]),'empty':([0,],[4,]),'asig':([0,2,],[5,5,]),'sentwritestr':([0,2,],[6,6,]),'sentwritelog':([0,2,],[7,7,]),'sentwriteintro':([0,2,],[8,8,]),'sentwritetabla':([0,2,],[9,9,]),'identificador':([0,2,22,24,26,29,31,41,43,45,46,47,48,51,52,53,58,59,60,61,],[10,10,27,27,44,27,27,44,44,27,27,27,27,44,44,44,44,44,44,44,]),'expresion':([22,24,29,31,45,46,47,48,],[28,39,49,50,63,64,65,66,]),'senttauto':([22,24,29,31,45,46,47,48,],[32,32,32,32,32,32,32,32,]),'sentcontra':([22,24,29,31,45,46,47,48,],[33,33,33,33,33,33,33,33,]),'sentdeci':([22,24,29,31,45,46,47,48,],[34,34,34,34,34,34,34,34,]),'matriz':([26,41,43,51,52,53,58,59,60,61,],[42,56,62,68,69,70,72,73,74,75,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> sentencias','prog',1,'p_prog','pysyntax.py',25),
  ('sentencias -> sentencias sentencia','sentencias',2,'p_sentencias','pysyntax.py',29),
  ('sentencias -> sentencia','sentencias',1,'p_sentencias','pysyntax.py',30),
  ('sentencias -> empty','sentencias',1,'p_sentencias','pysyntax.py',31),
  ('sentencia -> asig PCOMA','sentencia',2,'p_sentencia','pysyntax.py',35),
  ('sentencia -> sentwritestr PCOMA','sentencia',2,'p_sentencia','pysyntax.py',36),
  ('sentencia -> sentwritelog PCOMA','sentencia',2,'p_sentencia','pysyntax.py',37),
  ('sentencia -> sentwriteintro PCOMA','sentencia',2,'p_sentencia','pysyntax.py',38),
  ('sentencia -> sentwritetabla PCOMA','sentencia',2,'p_sentencia','pysyntax.py',39),
  ('expresion -> NOT expresion','expresion',2,'p_expresion','pysyntax.py',43),
  ('expresion -> expresion DOBLEENTONCES expresion','expresion',3,'p_expresion','pysyntax.py',44),
  ('expresion -> expresion ENTONCES expresion','expresion',3,'p_expresion','pysyntax.py',45),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion','pysyntax.py',46),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion','pysyntax.py',47),
  ('expresion -> NUMERO','expresion',1,'p_expresion','pysyntax.py',48),
  ('expresion -> APAR expresion CPAR','expresion',3,'p_expresion','pysyntax.py',49),
  ('expresion -> identificador','expresion',1,'p_expresion','pysyntax.py',50),
  ('expresion -> senttauto','expresion',1,'p_expresion','pysyntax.py',51),
  ('expresion -> sentcontra','expresion',1,'p_expresion','pysyntax.py',52),
  ('expresion -> sentdeci','expresion',1,'p_expresion','pysyntax.py',53),
  ('asig -> identificador ASIGNACION expresion','asig',3,'p_asig','pysyntax.py',57),
  ('identificador -> ID','identificador',1,'p_identificador','pysyntax.py',62),
  ('sentwriteintro -> WRITEINTRO APAR CPAR','sentwriteintro',3,'p_sentwriteintro','pysyntax.py',67),
  ('sentwritelog -> WRITELOG APAR expresion CPAR','sentwritelog',4,'p_sentwritelog','pysyntax.py',72),
  ('sentwritestr -> WRITESTR APAR CTEXTO CPAR','sentwritestr',4,'p_sentwritestr','pysyntax.py',77),
  ('sentwritetabla -> WRITETABLA APAR matriz CPAR','sentwritetabla',4,'p_sentwritetabla','pysyntax.py',82),
  ('matriz -> NOT matriz','matriz',2,'p_matriz','pysyntax.py',87),
  ('matriz -> matriz DOBLEENTONCES matriz','matriz',3,'p_matriz','pysyntax.py',88),
  ('matriz -> matriz ENTONCES matriz','matriz',3,'p_matriz','pysyntax.py',89),
  ('matriz -> matriz AND matriz','matriz',3,'p_matriz','pysyntax.py',90),
  ('matriz -> matriz OR matriz','matriz',3,'p_matriz','pysyntax.py',91),
  ('matriz -> APAR matriz CPAR','matriz',3,'p_matriz','pysyntax.py',92),
  ('matriz -> identificador','matriz',1,'p_matriz','pysyntax.py',93),
  ('senttauto -> TAUTO APAR matriz CPAR','senttauto',4,'p_senttauto','pysyntax.py',98),
  ('sentcontra -> CONTRA APAR matriz CPAR','sentcontra',4,'p_sentcontra','pysyntax.py',103),
  ('sentdeci -> DECI APAR matriz CPAR','sentdeci',4,'p_sentdeci','pysyntax.py',108),
  ('empty -> <empty>','empty',0,'p_empty','pysyntax.py',113),
]
