from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *



class Bot(DesktopBot):
    def action(self, execution=None):

        # 2º bot

        self.browse("https://www.hashtagtreinamentos.com/")

        if not self.find( "curso python", matching=0.97, waiting_time=10000):
            self.not_found("curso python")
        self.click()
        
        if not self.find( "pagina carregou", matching=0.97, waiting_time=10000):
            self.not_found("pagina carregou")
        
        self.scroll_down(3000)
        
        if not self.find( "nome", matching=0.97, waiting_time=10000):
            self.not_found("nome")
        self.click()
        
        self.paste("SeuNome")
        
        if not self.find( "email", matching=0.97, waiting_time=10000):
            self.not_found("email")
        self.click()
        
        self.paste("seuemail@gmail.com")
        
        if not self.find( "cadastrar", matching=0.97, waiting_time=10000):
            self.not_found("cadastrar")
        self.click()

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()

































