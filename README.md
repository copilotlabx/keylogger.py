El script es un keylogger que registra las palabras escritas por el usuario (separadas por espacios) en un archivo de texto y, cuando se presiona la tecla "esc", envía el archivo a una dirección IP y puerto específicos. 
Después de enviar el archivo, lo elimina del sistema y detiene el script.
Cumple con las siguientes funciones:

  - Captura las pulsaciones del teclado:
        Utiliza la librería keyboard para enganchar las pulsaciones de teclas y llamar a la función pulsar cada vez que una tecla es presionada.
        La función pulsar guarda los caracteres imprimibles en la variable global word.
        Cuando se presiona la barra espaciadora, llama a la función guardar_palabra_espacio, que escribe la palabra actual en el archivo output.txt y luego la resetea llamando a reset_word.

  - Almacena palabras en un archivo:
        La función guardar_palabra_espacio abre (o crea si no existe) el archivo output.txt en modo de añadir y escribe la palabra capturada seguida de un salto de línea.
        Luego, imprime la palabra registrada en la consola y resetea la variable word con la función reset_word.

  - Envía el archivo mediante sockets:
        La función enviar_via_sockets se conecta a una dirección IP y puerto específicos (ip_destino y puerto_destino), lee el contenido del archivo output.txt y lo envía al destino especificado.
        Después de enviar el archivo, lo borra del sistema y termina el script.

  - Detiene el script y envía datos:
        La función detener_script desengancha todas las pulsaciones del teclado, llama a enviar_via_sockets para enviar el archivo output.txt, y luego pausa la ejecución del script durante 12 segundos.

  - Esperar la tecla "esc" para terminar:
        El script espera a que la tecla "esc" sea presionada (keyboard.wait("esc")). Cuando esto sucede, llama a detener_script.
        Si se produce una interrupción del teclado (por ejemplo, Ctrl+C), imprime "Script Detenido".

Ademas Para convertir este script de Python en un ejecutable .exe utilizando PowerShell, puedes usar la herramienta PyInstaller. Aquí están los pasos detallados:

- Instala PyInstaller:
    Primero, necesitas tener PyInstaller instalado. Abre PowerShell y ejecuta el siguiente comando:

    powershell

pip install pyinstaller

Crea el ejecutable .exe:
- Navega hasta el directorio donde se encuentra tu script de Python y ejecuta el siguiente comando:

powershell

pyinstaller --onefile tu_script.py
Reemplaza tu_script.py con el nombre de tu archivo de script.

- Opciones adicionales (opcional):

    Si quieres ocultar la consola cuando se ejecuta el archivo .exe, puedes agregar la opción --noconsole:

    powershell

pyinstaller --onefile --noconsole tu_script.py

Si tu script necesita incluir archivos adicionales, puedes usar la opción --add-data. Por ejemplo, si necesitas incluir output.txt, puedes usar:

powershell

        pyinstaller --onefile --add-data "output.txt;." tu_script.py

- Encuentra el ejecutable:
    Después de ejecutar PyInstaller, deberías ver un directorio llamado dist en el mismo directorio donde se encuentra tu script. Dentro de dist, encontrarás tu archivo ejecutable .exe.

