from locust import HttpUser, task, between

class TheInternetUser(HttpUser):
    wait_time = between(1, 3)  # pausa entre acciones

    @task
    def acceso_inicio(self):
        """1.Acceder a la página de inicio"""
        self.client.get("/", name="Inicio")

    @task
    def login(self):
        """2.Acceder a la sección Form Authentication y realice un intento de inicio de sesión """
        self.client.get("/login", name="Abrir Login")
        payload = {
            "username": "tomsmith",
            "password": "SuperSecretPassword!"
        }
        response = self.client.post("/authenticate", data=payload, name="Login")

        # Validación de autenticación exitosa
        if response.status_code == 200 and "secure" in response.text:
            print("Inicio de Sesión exitoso")
        else:
            print("Inicio de sesión Fallido")

    @task
    def descargar_archivo(self):
        """3.Acceder a la sección File Download y realice una descarga de archivo"""
        response = self.client.get("/download/some-file.txt", name="Descargar Archivo")

        if response.status_code == 200:
            print("Se desacargo Archivo Correctamente")
        else:
            print("No se puede descargar el archivo")
