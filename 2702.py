num_refeicoes = input().split()
prato_frango, prato_bife, prato_massa = map(int, num_refeicoes)

num_pedidos = input().split()
qtd_frango, qtd_bife, qtd_massa = map(int, num_pedidos)

sobra_frango = prato_frango - qtd_frango
sobra_bife = prato_bife - qtd_bife
sobra_massa = prato_massa - qtd_massa
passageiros_insatisfeitos = 0

if sobra_frango < 0:
    passageiros_insatisfeitos -= sobra_frango

if sobra_bife < 0:
    passageiros_insatisfeitos -= sobra_bife

if sobra_massa < 0:
    passageiros_insatisfeitos -= sobra_massa

print(passageiros_insatisfeitos)