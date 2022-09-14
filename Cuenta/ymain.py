from Cuenta import Cuenta

Marie = Cuenta ("Marie", "Curie", 50000)
Nicolas = Cuenta ("Nicolas", "Tesla", 50000) 


print(Marie.nombre)
Marie.mostrar_info_cuenta().depósito(5000).depósito(10000).depósito(6000).retiro(72000, (Marie.balance)).mostrar_info_cuenta()

print("\n")

print(Nicolas.nombre)
Nicolas.mostrar_info_cuenta().depósito(15000).depósito(6000).retiro(5000, (Nicolas.balance)).retiro(5000, (Nicolas.balance)).retiro(5000, (Nicolas.balance)).retiro(4000, (Nicolas.balance)).generar_interés().mostrar_info_cuenta()