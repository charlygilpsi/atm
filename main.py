from model.atm import ATM
from model.bank_account import BankAccount
from model.transaction import Transaction

def caso_de_uso(transaccion: Transaction, cantidad: int) -> str:
    multiplo_de_10 = True
    no_superado_limite_de_cajero = True
    no_superado_limite_de_cuenta = True
    
    print(f"\n- Saldo inicial en la cuenta: {transaccion.bank_account.check_balance()} euros.")
    print(f"- Saldo inicial en el cajero: {transaccion.atm.stock} euros.")
    print(f"- Cantidad introducida para retirar dinero: {cantidad} euros")
    
    if not transaccion.validate_amount_is_multiple_of_ten(cantidad):
        print("\nERROR: La cantidad introducida no es múltiplo de 10.")
        multiplo_de_10 = False
    else:
        
        if not transaccion.validate_withdraw_cash_from_atm(cantidad):
            print("\nERROR: No hay suficiente dinero en el cajero.")
            no_superado_limite_de_cajero = False
        else:
            
            if not transaccion.validate_debit_from_account(cantidad):
                print("\nERROR: No hay suficiente dinero en la cuenta.")
                no_superado_limite_de_cuenta = False
    
    if multiplo_de_10 and no_superado_limite_de_cajero and no_superado_limite_de_cuenta:
        transaccion.atm.withdraw_cash(cantidad)
        transaccion.bank_account.debit(cantidad)
        
        print("\nTransacción realizada con éxito.")
        print(f"\nSaldo en el cajero después de la transacción: {transaccion.atm.stock} euros.")
        print(f"Saldo en la cuenta después de la transacción: {transaccion.bank_account.check_balance()} euros.")
        
                
cajero_automatico_1 = ATM(1000)
cuenta_1 = BankAccount(1, 1, 123, 900)
transaccion_1 = Transaction(cajero_automatico_1, cuenta_1)

cajero_automatico_2 = ATM(500)
cuenta_2 = BankAccount(1, 1, 123, 400)
transaccion_2 = Transaction(cajero_automatico_2, cuenta_2)

cajero_automatico_3 = ATM(400)
cuenta_3 = BankAccount(1, 1, 123, 500)
transaccion_3 = Transaction(cajero_automatico_3, cuenta_3)

cantidad = 500
cantidad_2 = 15


print("\n\n################################")
print("CASO DE USO DONDE NO HAY ERRORES")
print("################################")
caso_de_uso(transaccion_1, cantidad)

print("\n\n#############################################")
print("CASO DE USO DONDE HAY ERROR POR MÚLTPLO DE 10")
print("#############################################")
caso_de_uso(transaccion_1, cantidad_2)

print("\n\n################################################")
print("CASO DE USO DONDE HAY ERROR POR LÍMITE DE CAJERO")
print("################################################")
caso_de_uso(transaccion_3, cantidad)

print("\n\n################################################")
print("CASO DE USO DONDE HAY ERROR POR LÍMITE DE CUENTA")
print("################################################")
caso_de_uso(transaccion_2, cantidad)