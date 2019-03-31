![](./data/img/FoodInKm.png?raw=true "Title")


www.foodinkm.com


## Abstract

Una herramienta que sigue el rastro de los alimentos y facilita el consumo de proximidad 

FOOD IN KM es una aplicación web que permite visualizar los kilómetros que recorre cada alimento desde su origen hasta el hogar. Así, el ciudadano puede organizar la lista de la compra eligiendo las marcas que le ofrecen una mejor relación calidad/precio/distancia. Para ello, se vincula la dirección de los productores de cada alimento con el código postal proporcionado por el usuario.
El equipo ha trabajado a partir de los datos obtenidos de productores y distribuidores. Para el lanzamiento de esta primera versión solo se ha podido usar el catálogo de una de las  mayores cadenas (Mercadona) a partir de la técnica de web scraping. Los datos se han limpiado y procesado para su uso, añadiendo información adicional con la ayuda de Google Geocode API.
El concepto de proximidad se presenta en un vídeo protagonizado por un garbanzo, producto paradójico desde la perspectiva ecológica, al tratarse de un cultivo tradicional en España que se importa masivamente desde Norteamérica. Esta información se complementa con una infografía sobre el viaje del garbanzo.
En definitiva, FOOD IN KM ofrece al público una herramienta para reducir su huella ecológica de manera fácil y sencilla, aportando transparencia a un sector opaco.
Además, la aplicación es de código abierto, por lo que está abierta a mejoras y extensiones y a la participación ciudadana para completar la base de datos incluyendo productos de otras superficies así como de grupos de consumo.

## Bitácora

El diseño del proyecto empezó con la idea de crear una solución práctica para un problema social: cómo ayudar al ciudadano a averiguar qué productos son de cercanía para que pueda escoger las marcas que ofrecen un mejor compromiso calidad/precio. Podéis encontrar más información en la descripción del proyecto. Como aspecto destacable, es importante mencionar el proceso iterativo entre los coordinadores de plantear problemáticas en el campo de la trazabilidad de la alimentación y buscar soluciones técnicas teniendo en cuenta la duración del hackathon y considerando en todo momento cómo de viable sería con los datos públicos disponibles. Sin duda, una de las claves en el diseño para obtener este resultado ha sido el partir a partes iguales de una persona especialista en el tema del hackathon como Pablo Saralegui y una persona experta en datos como Celsa Díaz.

El primer día del hackathon la idea ya había tomado más forma, a nivel técnico, con la ayuda del científico de datos Levin Brinkmann. Esta idea inicial se presentó ante toda la audiencia para la búsqueda de más colaboradores. Adolfo Antón nos ayudó a formar grupos lo más heterogéneos posibles en términos de conocimientos especializados. Así, en esta segunda etapa fue muy interesante la interacción con especialistas en otros campos, particularmentemente en periodismo y diseño gráfico. Por otro lado, ya que uno de los coordinadores (Pablo Saralegui) no pudo asistir, fue importante contar con la ayuda de Inés Cambra como ingeniera agrónoma.

La comunicación ha sido eminentemente presencial, aunque también se creó grupo de Telegram y se usaron herramientas colaborativas y repositorios de documentos variados. Para conseguir dar una forma final al proyecto fue clave, por un lado, limitarse a lo que se podía contar a partir de los datos disponibles para no perder el foco y, por otro, la continua aportación de ideas por parte de todos los miembros del grupo para mejorar cada una de las partes.

El segundo día el equipo se reunió para orientar editorialmente el proyecto (definición de objetivos) y el diseño de la herramienta, que debería ofrecer de forma sencilla y amable, muy visual, información sobre el origen de los productos alimentarios disponibles en el supermercado de su elección (aunque en un primer momento solo estará disponible el catálogo de uno) y facilitar la elección de aquellos productos más próximos a la localización del usuario. 

El trabajo, como en días sucesivos, se hizo por grupos y con puestas en común. Los integrantes del equipo editorial se familiarizaron, por ejemplo, con la base de datos del supermercado y se comenzó con la documentación periodística sobre el comercio y el transporte de los alimentos. En la parte técnica se llevó a cabo la mayoría de trabajo de web scraping y se empezó a testear.

En conjunto, se constató una limitación de partida insalvable: no se puede hacer una trazabilidad completa del recorrido del producto ya que en el caso de los productos transformados no es obligatorio informar del origen de los distintos ingredientes; y, en el caso de productos no elaborados, tampoco es posible rastrear el transporte del mismo. 

De hecho, durante un día se trabajó con la idea de personalizar una historia en torno a un alimento importado desde Asia, pero no se pudo documentar, así que finalmente se eligió el garbanzo como el producto para contar la historia. 

Con un protagonista ya definido para la narrativa, Juan Corellano trabajó con ese punto de partida en un vídeo promocional que sirviera como primer reclamo de la página para atraer al usuario. Debido a la falta de recursos y profesionales del campo de la visualización en el equipo, se optó por crear una pieza audiovisual con imágenes estáticas cuyo principal atractivo residiera en el audio. El resultado final fue un vídeo en tono cómico que jugaba con la idea de una hipotética relación sentimental entre el alimento, bautizado como Garbanzón, y el consumidor.

Finalmente, aunque no estuviera previsto en su génesis, este vídeo sirvió para estructurar el resto de la narrativa que guiaba al usuario a la utilización de la herramienta. De esta manera, con la ayuda de las ilustraciones de Xaquín Veira, se realizó una historia complementaria que mostraba las diferentes etapas del viaje que un garbanzo de origen mexicano, como nuestro protagonista, realizaba desde su plantación hasta nuestro plato. 

De nuevo, se trataba de una historia fundamentalmente visual, únicamente acompañada por unas breves líneas explicativas de texto para cuya redacción se contó con la ayuda de Monica Ulmanu. Además del vídeo promocional creado inicialmente, se mantuvo el audio y se cambió el componente visual, que fue rediseñado y editado por Covadonga Fernández, quien, además, realizó todas las ilustraciones del personaje. 

En cuanto a la parte técnica, la función principal fue automatizar el web scraping a través de Selenium y BeautifulSoup y montar la estructura básica de la aplicación web (backend/frontend). También fue clave discutir la idea con Lázaro Gamio para dar forma a la interfaz gráfica de la herramienta principal. Para poder realizar la búsqueda automática de datos y el cálculo de los kilómetros de distancia para cada usuario de una forma eficiente fue determinante el uso de Elasticsearch como base de datos.

El miércoles se siguió perfilando el diseño de la interfaz, básicamente en cuatro pantallas. También se consiguió terminar la recolección de datos y se empezó con su procesamiento y anotación, especialmente la extracción de la geolocalización de los productores o proveedores gracias a Geocode API de Google. Al final del día se consiguió añadir los datos limpios y procesados en Elasticsearch y se pudo probar la herramienta a nivel local.

También se barajó limitar la elección a una lista de los 12 productos más consumidos con la idea de ofrecer unas comparativas más detalladas, pero la falta de datos precisos sobre la cesta tipo y las dificultades para determinar criterios con los que ampliar esta visualización de datos hizo que se descartara la idea y se optara por ofrecer todo el catálogo de productos con sus datos de origen junto a un mapa. 

Respecto al resultado final se descartó la conversión de los kilómetros de la cesta de la compra a emisión de gases contaminantes por la imposibilidad de acceder a los datos reales en las diferentes fases y medios de transporte.

Al mismo tiempo, se comprobó que una gran empresa de la distribución ha introducido blockchain para registrar la trazabilidad del producto desde el origen hasta su almacén y ha lanzado una aplicación en la que ofrece esta información, o parte de ella, más como una estrategia de mercadotecnia. 

El jueves los periodistas (David Sanz Frías, Mayra Margffoy y Mario Vallejo, además de Juan) dieron forma a los textos finales, en particular los de la infografía interactiva que se presenta al final, cuya finalización ha sido posible gracias a Covadonga Fernández.

También descartamos la visualización de los aditivos. En principio, la idea era mostrar, junto al precio y al kilometraje del producto, el número de aditivos potencialmente peligrosos que contiene dicho producto o, en todo caso, el número total de estos componentes, pero finalmente se optó por no saturar de información la página, más aún sobre asuntos sobre los que convendría una contextualización mayor a la que podíamos ofrecer con las limitaciones de tiempo y espacio de este proyecto.

En cuanto a la parte técnica, la mayoría del tiempo se centró en la corrección de fallos o bugs en el código, así como la detección y corrección de errores en los datos. En la parte de diseño gráfico, se consiguió dar forma al diseño final de la herramienta de búsqueda y presentación de los resultados de la compra llevada a cabo por el ciudadano. También se llevó a cabo el deployment de toda la herramienta web y se puso online en el dominio foodinkm.com.

Finalmente, el viernes se testeó la web, se realizaron algunas mejoras de diseño y se puso en común toda la experiencia para preparar la presentación final, la exposición (donde destaca el trabajo de Alessandra Spina) y la documentación del proyecto.

Para acabar, el equipo hace constar que el cambio de modelo de alimentación hacia un sistema más sostenible debe tener en cuenta otros criterios socioeconómicos. Son muchos los conflictos políticos, laborales y ambientales que envuelven a muchos productos que consumimos. Un esbozo de los que atañen al caso de Garbanzón (nombre que se ha dado al alimento que ha vehiculado la narrativa de este proyecto) se puede leer en el reportaje anexo.


## La historia de Garbanzón 

La historia del garbanzo representa el hilo conductor de la herramienta FOOD IN KM. Inicialmente hace un llamado al usuario sobre su desconocimiento de la cantidad de kilómetros de su compra y por qué esta situación debe preocuparle.
 
La invitación del garbanzo conduce al usuario a una interfaz que simula una cesta de compra donde este puede escoger una variedad de productos y seleccionar aquellos que hayan tenido un mayor o menor kilometraje con respecto a su punto de geolocalización. En el mapa se reflejan las distancias recorridas de aquellos productos. Asimismo, se destacan datos sobre el tipo del producto, su precio y su recorrido según la dirección/ciudad/país del proveedor.
 
Al completar la cesta, el usuario podrá ver la cantidad de kilómetros que ha recorrido su compra y el promedio del recorrido. Igualmente podrá ver el total del coste según el número de productos seleccionados.


## Reportaje: El viaje insostenible de los garbanzos

Hasta tu sofá llega un antojo vespertino de cocido madrileño. Se apodera de ti. Te acercas hasta al supermercado más cercano para comprar un bote de garbanzos frescos y el resto de ingredientes necesarios para dar rienda suelta a tus dotes culinarias. El resultado final es un cocido más castizo que el chotis… al menos, eso crees. En el bote has leído en un vistazo distraído que la materia prima viene directamente desde León, pero… ¿estás seguro de que ese es su verdadero origen?
 
Pues bien, para tu desconsuelo, todo parece indicar que no. Un vistazo más detallado a la información de los garbanzos te revela su verdadero primer punto de partida. Probablemente no provengan de donde creías. De repente, descubres que realmente han recorrido miles de kilómetros hasta llegar a tu plato.
 
Ahora quieres saber más sobre el origen de tus garbanzos. Descubre la verdadera aventura que tu alimento vive desde que crece en una planta hasta que lo saboreas en tu boca.
 
Nuestro recorrido empieza al otro lado del Atlántico. Gran parte de los garbanzos importados que consumes en tu cocido provienen de México, particularmente del noroeste de este país. Los estados líderes en producción de este grano son Sinaloa, Sonora, Michoacán y Baja California Sur, donde se ha invertido en tecnología para producir una mejor variedad de garbanzo blanco. Aunque estas regiones han tenido problemas en el desarrollo de los cultivos por el exceso de lluvias y la especulación de los precios internacionales, en 2017 lograron exportar entre un 21 y un 28% de las 183.576 toneladas producidas.
 
Después de sobrevivir a las inundaciones, el garbanzo está listo para abandonar el noroeste mexicano y dirigirse al puerto de Veracruz. Una vez allí, es enviado a diferentes países por todo el mundo y uno de los destinos fetiche es nuestro país. De acuerdo con el Ministerio de Agricultura, Pesca y Alimentación, en ese mismo año, España realizó una importación de 41.758 toneladas de esta leguminosa para poder cubrir las necesidades de consumo nacional, de las cuales un 39,2% correspondió a la cuota de proveedores de México.
 
Es importante tener en cuenta la amplitud de posibilidades de los destinos y los trayectos. No solo importan los kilómetros, sino también el modo de transporte. Como se explica en el informe Alimentos Kilométricos de Amigos de la Tierra, en el cálculo de emisiones no solo cuentan los kilómetros recorridos, sino también el coeficiente energético del vehículo utilizado (camión, tren, avión o barco), así como el impacto de las emisiones del tipo de energía que utilizan (diésel, gasolina, queroseno, electricidad, etc.). En ese sentido, los barcos y trenes representan una alternativa más eficiente en el plano medioambiental con respecto a los aviones y camiones para transportes transoceánicos y terrestres, respectivamente.
 
Volviendo al recorrido del garbanzo mexicano, este sale del puerto de Veracruz en México y recorre 8.790 kilómetros aproximadamente hasta el puerto de Vigo. A su llegada a territorio español, los garbanzos mexicanos empiezan a convivir con la producción nacional, que está radicada principalmente, según datos de Statista de 2017, en Andalucía (29,1%) y, en menor grado, en Castilla y León (4,5%), Castilla-La Mancha (2,3%) y Extremadura (2,0%). Dentro de esta convivencia y competencia, debido al alto consumo, la cantidad de garbanzos importados se ha visto incrementada en los últimos años.
 
Desde el puerto, los garbanzos viajan por carretera a León, donde se ubica la planta envasadora. En este trayecto recorre unos 260 kilómetros. Una vez envasado, el producto recorre otros 337 kilómetros hasta un supermercado de Madrid a un precio similar a un garbanzo producido en una región cercana. En nuestro ejemplo, desde su lugar de origen, se han emitido 2.700 kg de CO2.
 
¿Cómo podemos reducir estos kilómetros? ¿Cómo se podrían reducir esas emisiones de CO2? Según Jorge Molero, de la Fundación Entretantos, “el coste de producción de los garbanzos de México y Estados Unidos es mucho más bajo que el de España. Esto hace que, competitivamente, sea más bajo. Con 10 céntimos más que se pagara por cada kilo de garbanzo, se podrían cubrir los costes aquí. Eso implicaría el aumento del precio del estatal”.
 
Sin embargo, no todas las soluciones dependen de las políticas gubernamentales. Al final, nuestra decisión como consumidores también es clave para reducir el número de kilómetros. Esto implicaría aumentar el consumo del producto de proximidad. “Lo que habría que hacer para recuperar las legumbres nacionales es que las administraciones públicas fomenten y convenzan a la gente para comprar producto local”, agrega Morelo.
 
Actualmente, una asociación de Madrid llamada “La garbancera madrileña” está desarrollando un proyecto agrícola para recuperar la producción de garbanzo autóctono. Esto es solo una muestra de cómo podría mejorar nuestra relación con la comida de una forma más sostenible.
 







