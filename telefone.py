import re
def validacao_telefone(telefone):
    if re.match("^\(\d{2}\)\s9\d{4}-\d{4}$", telefone):
        return "Número de telefone válido."
    else:
        return "Número de telefone inválido."
        
telefone = input('')
print(validacao_telefone(telefone))
