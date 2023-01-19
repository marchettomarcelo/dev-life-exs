# Python >> 05. Laços de Repetição (while) >> Estatísticas do hospital

# Estatísticas do hospital

# Um hospital quer conhecer melhor o público de seu pronto atendimento para 
# decidir qual tipo de investimento é mais prioritário. 
# Para isso, faça um programa que pergunta repetidamente para o usuário a idade do paciente. 
# Quando o usuário digita um número negativo o programa mostra o texto a seguir e termina 
# (importante: os números são apresentados com exatamente duas casas decimais):

# 0-11 anos: A.AA %
# 12-17 anos: B.BB %
# 18-25 anos: C.CC %
# 26-35 anos: D.DD %
# 36-59 anos: E.EE %
# Acima de 60 anos: F.FF %


zero_a_onze = 0
doze_a_dezessete = 0
dezoito_a_vinte_e_cinco = 0
vinte_e_seis_a_trinta_e_cinco = 0
trinta_e_seis_a_cinquenta_e_nove = 0
sessenta_e_um_ou_mais = 0


perguntar_idade = True

while perguntar_idade:

    idade = int( input('Digite a idade do paciente: ') )
    
    if idade < 0:
        perguntar_idade = False
    

    elif idade <= 11:
        zero_a_onze += 1


    elif  idade <= 17:
        doze_a_dezessete += 1
    
    elif idade <= 25:
        dezoito_a_vinte_e_cinco += 1
    
    elif idade <= 35:
        vinte_e_seis_a_trinta_e_cinco += 1
    
    elif idade <= 59:
        trinta_e_seis_a_cinquenta_e_nove += 1
    
    elif idade >= 60:
        sessenta_e_um_ou_mais += 1

    
total_de_pacientes = zero_a_onze + doze_a_dezessete + dezoito_a_vinte_e_cinco + vinte_e_seis_a_trinta_e_cinco + trinta_e_seis_a_cinquenta_e_nove + sessenta_e_um_ou_mais

print(f''' 
    0-11 anos: {zero_a_onze / total_de_pacientes * 100:.2f} %
    12-17 anos: {doze_a_dezessete / total_de_pacientes * 100:.2f} %
    18-25 anos: {dezoito_a_vinte_e_cinco / total_de_pacientes * 100:.2f} %
    26-35 anos: {vinte_e_seis_a_trinta_e_cinco / total_de_pacientes * 100:.2f} %
    36-59 anos: {trinta_e_seis_a_cinquenta_e_nove / total_de_pacientes * 100:.2f} %
    Acima de 60 anos: {sessenta_e_um_ou_mais / total_de_pacientes * 100:.2f} %
''')

