Para ejecución realizar:

1. Abrir el entorno virtual
   1. `cd .\my-venv\`
   2. `cd .\Scripts\`
   3. `dir` para listar los archivos y carpetas
   4. `.\Activate.ps1`
   5. `cd..`
   6. `cd..`
2. Ejecutar `python -m pytest -s -k "Yvytu"`

Siempre que se ejecute "pip install package"
Posterior a eso se debe ejecutar "pip freeze > .\requirements.txt"

### Ejercicio 1:

Entrar en una URL
Hacer click en un link
En ese link, hacer click en otro link

### Ejercicio 2:

Entrar en una URL
SOLO SI ES NECESARIO: Hacer click en un botón de búsqueda para que se despliegue la barra de búsqueda
Rellenar la barra de búsqueda con algún valor válido
Hacer click en el botón de búsqueda

### Ejercicio 3:

Entrar en la URL de una tienda virtual
Seleccionar el primer producto disponible en la Home Page (Les debería llevar a la página del producto)
Seleccionar alguna característica del producto (cantidad-talle-color-tamaño-capacidad-etc)
Agregar en el carrito

### Ejercicio 4:

Entrar en la URL de una tienda virtual
Buscar un producto existente y clickear en él (Les debería llevar a la página del producto)
Validar los labels de los campos select o number, y labels de botones que tenga esa página. Máximo 2 de cada uno.
Validación de textos/labels con la función compareLabels:
requirement = () #Expected Result
labelObtained = () #Actual Result

def compareLabels():
if requirement in labelObtained:
print("Pass")
else:
print("Fail")

comprarButton = driver.find_element(By.XPATH, '/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[2]/div[2]/form/div[2]/div/div[2]/div/button')  
#Aquí identificamos el elemento

labelComprarButton = driver.find_element(By.XPATH, '/html/body/main/section/div[2]/div/section/div[2]/div[1]/div[2]/div[2]/div[2]/form/div[2]/div/div[2]/div/button').text
#Aquí extraemos el texto dentro del elemento

Eclipse
Behave
Allure-behave
pillow (para las imagenes a los reportes)
