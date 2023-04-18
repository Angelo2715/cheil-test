# Con unittest nos podemos traer todas nuestras pruebas
import unittest
# Ayuda a orquestar cada una de las pruebas que estaremos
# ejecutando junto con los reportes
from pyunitreport import HTMLTestRunner
# Para comunicarnos con el navegador usamos webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class HelloWorld(unittest.TestCase):
	# Realiza todo lo necesario antes de empezar la prueba
    @classmethod # Decorador para que las distintas paginas corran en una sola pestaña
    def setUpClass(cls):
        d = DesiredCapabilities.CHROME
        d['goog:loggingPrefs'] = {'browser': 'ALL'}
        cls.driver = webdriver.Chrome(executable_path=r"./chromedriver.exe",desired_capabilities=d)
        driver = cls.driver
		# esperamos 10 seg antes de realizar la siguiente accion
        driver.implicitly_wait(10)

	# Caso de prueba donde realizaremos una serie de acciones para que el navegador las automatice
    def test_hello_cheil(self):
        driver = self.driver
        driver.get('C:/Code/cheil_test/caso_satisfactorio.html')
        # driver.get('C:/Code/cheil_test/caso_fallido.html')  # habilitar para el caso FALLIDO
        # Busca los elementos del formulario y completa los campos
        first_name = driver.find_element(By.ID, "first-name")
        first_name.send_keys("John")
        last_name = driver.find_element(By.ID, "last-name")
        last_name.send_keys("Doe")
        email = driver.find_element(By.ID, "email")
        email.send_keys("johndoe@example.com")
        password = driver.find_element(By.ID, "password")
        password.send_keys("secretpassword")
        confirm_password = driver.find_element(By.ID, "confirm-password")
        confirm_password.send_keys("secretpassword")

        # Envía el formulario haciendo clic en el botón de envío
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()
        # Captura los logs de la consola
        print("CAPTURAS")
        salida=driver.get_log('browser')
        print(salida[0]['message'])
        if "Submitting form data..." in salida[0]['message']:
            print("-----------------------------Reporte exitoso-------------------------")
            self.assertTrue(True, "El mensaje 'Submitting form data...' está en los logs de la consola")
        else:
            print("-----------------------------Reporte Fallido---------------------")
            self.assertFalse(False, "El mensaje 'Submitting form data...' no está en los logs de la consola")

	# Cerramos el navegador una vez terminadas las pruebas
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'Reportes', report_name = 'report-cheil'))