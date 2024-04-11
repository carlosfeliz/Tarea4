import os
import time
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

class TestWebApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Utilizando una cadena de texto cruda para la ruta del archivo
        cls.service = Service(r"C:\Program Files (x86)\msedgedriver.exe")

        # Inicializar el WebDriver de Microsoft Edge con el servicio especificado
        cls.driver = webdriver.Edge(service=cls.service)

        # Abrir una página web en el navegador y tomar una captura de pantalla
        cls.driver.get("https://proyecto.rdcoordinacion.website/")
        cls.take_screenshot("pagina_cargada")

        # Maximizar la ventana del navegador
        cls.driver.maximize_window()

        # Esperar un tiempo determinado para que la página cargue completamente
        cls.driver.implicitly_wait(10)

    def test_login(self):
        # Encontrar el campo de usuario por su nombre y enviar las teclas
        user_input = self.driver.find_element(By.XPATH, "//input[@name='user_name']")
        user_input.send_keys("00101328409")

        # Encontrar el campo de contraseña por su nombre y enviar las teclas
        password_input = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password_input.send_keys("00101328409")

        # Encontrar el botón de login por su valor y hacer clic en él
        login_button = self.driver.find_element(By.XPATH, "//input[@value='LOGIN']")
        login_button.click()

        # Esperar un tiempo para que se complete el inicio de sesión
        self.driver.implicitly_wait(10)

        # Tomar una captura de pantalla después de iniciar sesión
        self.take_screenshot("inicio_sesion")

        # Verificar que el inicio de sesión fue exitoso
        self.assertIn("home", self.driver.current_url)  # Cambiado a "home"


    def test_view_profile(self):
        try:
            # Encontrar el elemento del nombre de usuario y hacer clic en él para abrir el toggle
            username_element = self.driver.find_element(By.XPATH, "//span[contains(text(), 'SOL MARIA')]")
            username_element.click()
            
            # Esperar un breve momento para que se abra el toggle
            time.sleep(1)
            
            # Encontrar y hacer clic en el botón de perfil
            profile_button = self.driver.find_element(By.XPATH, "//a[contains(@href, 'profile')]")
            profile_button.click()
            
            # Esperar un tiempo para que se cargue la página del perfil
            self.driver.implicitly_wait(10)
            
            # Tomar una captura de pantalla después de abrir el perfil
            self.take_screenshot("perfil_abierto")
            
            # Verificar que la URL del perfil es la esperada
            self.assertIn("profile", self.driver.current_url)
        
        except Exception as e:
            print(f"Error en test_view_profile: {str(e)}")
            self.take_screenshot("error_view_profile")

    def test_open_users_page(self):
        try:
            # Encontrar y hacer clic en el botón de "Usuarios"
            users_button = self.driver.find_element(By.XPATH, "//p[contains(text(), 'Usuarios')]")
            users_button.click()

            # Esperar un tiempo para que se cargue la página de usuarios
            self.driver.implicitly_wait(10)

            # Tomar una captura de pantalla después de abrir la página de usuarios
            self.take_screenshot("pagina_usuarios")

        except Exception as e:
            print(f"Error en test_open_users_page: {str(e)}")
            self.take_screenshot("error_open_users_page")


    
    @classmethod
    def tearDownClass(cls):
        # Cerrar el navegador
        cls.driver.quit()

    @staticmethod
    def take_screenshot(name):
        # Directorio para almacenar capturas de pantalla
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)

        # Tomar captura de pantalla y guardarla
        screenshot_path = os.path.join(screenshot_dir, f"{name}.png")
        TestWebApp.driver.save_screenshot(screenshot_path)

if __name__ == "__main__":
    # Especificar la ruta de salida del reporte
    report_path = os.path.join("Reporte", "reporte_test.html")
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=report_path))
