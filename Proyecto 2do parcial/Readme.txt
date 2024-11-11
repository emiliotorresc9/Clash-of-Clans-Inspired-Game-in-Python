La aldea contara con los siguientes recursos:
*Frutos
*Carne
*Piedra
*Oro
*Madera

*cada recurso podrá obtenerse de distintas maneras como cazando, minando, cultivando, o simplemente atacando y robando recursos a otras aldeas. 

El jugador podrá construir los siguientes edificios:
*Casa: Necesaria para poder generar aldeanos (puedes generar a lo mucho 3 aldeanos por cada casa que tengas) 
Materiales necesarios para la construcción de una casa: 19 madera 12 piedra 1 oro 
Requisito de construcción: 20 (la suma del atributo construcción de la población de al menos 20)
 
*Coliseo: Necesario para poder generar soldados (puedes generar a lo mucho 2 soldados por cada coliseo que tengas)
Materiales necesarios para la construcción de una casa: 30 madera 25 piedra 6 oro 
Requisito de construcción: 40 (la suma del atributo construcción de la población de al menos 40)
 
*Establo: Necesario para poder generar jinetes (puedes generar a lo mucho un jinete por cada establo que tengas)
Materiales necesarios para la construcción de una casa: 50 madera 40 piedra 10 oro 
Requisito de construcción: 60 (la suma del atributo construcción de la población de al menos 60)

Tipo de población de la aldea:
*Constructor: Ideal para las construcciones
*Guerrero: Ideal para los ataques
*Soldado: Version mejorada del guerrero (necesitas un coliseo para poder generar un soldado)
*Jinete: Version mejorara del soldado (necesitas un establo para poder generar un jinete)
*Minero: Ideal para minar
*Aldeano: Muy versátil ya que es bueno para realizar la mayoría de las actividades de recolección de recursos de la aldea, su único punto débil es el ataque y la construcción
*Cazador: Version mejorada del aldeano en el aspecto de cazar
*Agricultor: Version mejorada del aldeano en el aspecto de cultivar
*Talador: Version mejorada del aldeano en el aspecto de talar.

La interfaz de la aldea contará con un buffer de acciones (activity record) el cual mostrará al usuario las acciones que vaya agregando previo a ejecutarlas.
La interfaz cuenta con 7 botones de acciones:
*Hunt: Preguntará cuantos miembros quieres mandar a cazar para obtener el recurso de carne
*Farm: Preguntará cuantos miembros quieres mandar a cultivar para obtener el recurso de frutos
*Mine: Preguntará cuantos miembros quieres mandar a minar para obtener los recursos de oro y piedra
*Chop: Preguntará cuantos miembros quieres mandar a talar para obtener el recurso de madera
*Flirt: Preguntará a que miembro quiere reproducir Restricciones:
	
Constructor: 
  - Solo se puede generar uno a la vez.
  - Se necesitan 10 frutos, 2 carne 1 de oro. 

Guerrero: 
 - Puedes generar máximo 2. 
 - Se necesitan 3 frutos, 7 carne, 2 oro. 

Soldado: 
 - Necesitas un coliseo
 - El número máximo que puedes generar depende del número de coliseos. 
 - Se necesitan 5 frutos, 10 carne, 3 oro. 

Jinete:  
 - Se necesita un establo 
 - El número máximo que puedes generar depende del número de establos.
 - Se necesitan 10 frutos 16 carne 4 oro . 

Minero: 
 - Solo se puede generar uno a la vez.
 - Se necesitan 7 frutos, 5 carne

Aldeano: 
 - Necesitas una asa para poderlos generar 
 - El número máximo de aldeanos depende del número de casas.
 - Se necesitan 3 frutos, 1 carne 

Cazador: 
 - Solo se puede generar uno a la vez 
 - Se necesitan 10 frutos, 1 oro 


Agricultor: 
 - Solo se puede generar uno a la vez 
 - Se necesitan 5 carne, 1 oro 

talador: 
 - Solo se puede generar uno a la vez 
 - Se necesitan 5 frutos, 5 carne 1 oro 


*Build: Preguntara que quiere construir; casa, coliseo o establo. Posteriormente el código verificara si hay materiales disponibles para construir.
	Si los hay, aparecerá en la aldea una imagen de la edificación que le usuario podrá colocar donde quiera, siempre y cuando sea un lugar valido. 
		Una vez seleccionado el lugar por medio de las flechas del teclado, podrá presionar enter para establecer la edificación y ya no se podrá editar.
        Considera que solo se puede constuir 1 tipo de edificio a la vez (para construir otro se tiene que dar click en play), además de que no se puede hacer ninguna otra acción si se va a constuir.
*Attack: Preguntará en primera instancia cuantos miembros de la aldea desea mandar a atacar, el programa simulará un rival, posteriormente te mostrar nivel de poder tuyo y del rival, 
		con esta información se podrá decidir ya sea seguir adelante con el ataque o rendirse. Por medio del algoritmo implementado podrá tomar las decisiones en base a prioridades. 

Por ejemplo, si tenemos 3 aldeano, 3 mineros y se selecciona la opción "mine" con 3 personas, el algoritmo decidirá enviar a los 3 mineros a realizar la tarea, no a los aldeanos. 
De igual manera en un ataque siempre se trataran de enviaran todas las tropas mas fuertes primero para lograr alcanzar el máximo poder posible. 
	En general el algoritmo es capaz de identificar las prioridades a la hora de realizar tareas en la aldea. 


* El jugador tendrá siempre una área de texto que le informara que esta sucediendo en la aldea, así como los botones para cada acción en la pantalla los cuales, al ser presionados añadirán as acciones al buffer para posteriormente ser ejecutadas una vez se presione el botón "ejecutar". 

* De igual manera el jugador o la aldea estarán siempre al acecho de los rivales, un algoritmo genera rivales aleatorios en un tiempo indeterminado los cuales constantemente querrán atacarte. En ese caso existen dos opciones: Defenderse o Rendirse. Desde luego cada una de las acciones tiene sus consecuencias. Al rendirse no perderás tropas sin embargo perderás recursos acorde al poder de tu rival, y viceversa, si decides defenderte, no perderás recursos pero si perderás una cantidad de tu población directamente proporcional al nivel del rival.    







