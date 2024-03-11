def comer(comida, eh_saudavel):
    if eh_saudavel:
        final = 'quero manter a forma.'
    else:
        final = 'a gente s[o vive uma vez]'

    return f'Estou comendo {comida} porque {final}' 

def dormir(num_horas):
    if num_horas > 8:
        return 'Puts, dormi muito'
    else:
        return 'Durmi pouco'


