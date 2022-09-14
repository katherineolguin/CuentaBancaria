class Cuenta:

    # nombre_banco = "Primer Dojo Nacional"
    # todas_las_cuentas = []

    def __init__ (self, nombre, apellido, balance): 
        self.nombre = nombre
        self.apellido = apellido
        self.balance = balance
        self.tasa_interés = 0.5
        

    def depósito(self, amount_increase):
        self.balance += amount_increase
        if self.balance + 1:
            print(f"Tienes un deposito de $+{amount_increase}")
            return self
            
        
    def retiro(self, amount_decrease, Usuario_balance):
        self.balance -= 5
        self.balance -= amount_decrease
        if self.balance < amount_decrease:
            self.balance = Usuario_balance
            print(f"Saldo insuficiente, intente otro monto menor a ${Usuario_balance}.- "  )
            return self
        else:
            print(f"Has echo un retiro de: $-{amount_decrease}, con un cobro de retiro de $5")
            return self


    def mostrar_info_cuenta(self): 
        print(f"Tu balance es de: ${self.balance} ")
        return self


    def generar_interés(self):
        self.balance += self.balance * self.tasa_interés 
        print(f"Tu balance más tu tasa de interes es de: ${self.balance}")
        return self
