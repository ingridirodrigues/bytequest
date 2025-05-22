usuarios = {
    "admin": {
        "senha": "1234",
        "pontuacao": {
            "facil": 0,
            "medio": 0,
            "dificil": 0
        },
        "pontuacao_total": 0
    }
}

perguntas = {
    "facil": [
        {
            "texto": "\n1 - O operador lógico E (AND) exige que ambas as condições sejam verdadeiras para o resultado ser verdadeiro.\n",
            "pergunta": "Qual será o resultado da expressão: Verdadeiro E Falso?\n",
            "respostas": {
                "A": "Verdadeiro",
                "B": "Falso",
                "C": "Indefinido",
                "D": "Erro"
            },
            "resposta_certa": "B"
        },
        {
            "texto": "\n2 - No operador lógico OU (OR), basta que uma das condições seja verdadeira para que o resultado também seja verdadeiro.\n",
            "pergunta": "Qual será o resultado da expressão: Falso OU Verdadeiro?\n",
            "respostas": {
                "A": " Falso",
                "B": "Verdadeiro",
                "C": "Indefinido",
                "D": "Erro"
            },
            "resposta_certa": "B"
        },
        {
            "texto": "\n3 - Primeiro resolvemos o E (AND), depois o OU (OR)\n",
            "pergunta": "Qual o resultado da operação: (Verdadeiro E Falso) OU Verdadeiro?\n",
            "respostas": {
                "A": "Verdadeiro",
                "B": "Falso",
                "C": "Erro",
                "D": "Nulo"
            },
            "resposta_certa": "A"
        }
    ],
    "medio": [
        {
            "texto": "\n1 - O for é um laço de repetição usado quando sabemos quantas vezes queremos\n "
                     "repetir uma ação. Ele percorre uma sequência (como uma lista ou intervalo) e "
                     "executa um bloco de código para cada item dessa sequência. ",
            "pergunta": "\nUm robô precisa andar 5 passos. Cada passo é representado com uma contagem simples: \n"
                     "for i in range(5):" 
                        "print(""Passo"","" i)"
                     "Quantas vezes a mensagem será exibida? \n",
            "respostas": {
                "A": "4",
                "B": "5",
                "C": "6",
                "D": "0"
            },
            "resposta_certa": "B"
        },
        {
            "texto": "\n2 - O while é usado quando queremos repetir uma ação enquanto uma condição for" 
                     "verdadeira. O laço só para quando essa condição deixar de ser satisfeita.\n ",
            "pergunta": "Um contador de energia é ativado e deve desligar ao atingir 3 unidades:\n"
                    "energia = 0"
                    "while energia < 3: "
                        "energia += 1 "
                    "print(energia)" 
                    "Qual será o valor final de energia?",
            "respostas": {
                "A": "2",
                "B": "3",
                "C": "4",
                "D": "0"
            },
            "resposta_certa": "B"
        },
        {
            "texto": "\n3 - Contadores são variáveis usadas para armazenar valores que vão se acumulando" 
                     "em um loop. Podemos usá-los para contar quantos itens atendem a uma condição" 
                     "específica.\n",
            "pergunta": "O código abaixo conta quantos números de 1 a 5 são maiores que 2:\n"
                     "contador = 0 "
                     "for i in range(1, 6): "
                        "if i > 2: "
                            "contador += 1 ",
            "respostas": {
                "A": "3",
                "B": "2",
                "C": "5",
                "D": "4"
            },
            "resposta_certa": "A"
        }
    ],
    "dificil": [
        {
            "texto": "\n1 - Pseudocódigo é a descrição do algoritmo em linguagem natural estruturada, não dependendo de sintaxe de programação.\n",
            "pergunta": "Dado um fluxograma que inicia com ""x"" = 10" "e repete ""x"" = x - 1"" até que x seja igual a 0,"
                        "qual seria o pseudocódigo mais adequado para representá-lo?\n",
            "respostas": {
                "A": " para x de 10 até 0 faça x = x + 1",
                "B": "enquanto x > 0 faça x = x - 1",
                "C": "se x == 0, x = x - 1",
                "D": "repita x = x + 1 enquanto x != 0"
            },
            "resposta_certa": "B"
        },
        {
            "texto": "\n2 - Ao simplificar condições, o algoritmo se torna mais rápido e legível, evitando checagens desnecessárias.\n",
            "pergunta": "Em um algoritmo que verifica se uma pessoa pode se aposentar (idade maior ou igual a"
            "65 E anos de contribuição maior ou igual a 30), qual seria a melhor maneira de otimizar a verificação?\n",
            "respostas": {
                "A": "Verificar a contribuição antes da idade",
                "B": "Verificar a idade antes da contribuição",
                "C": "Testar ambas as condições juntas em uma única linha",
                "D": "Separar as condições em funções diferentes"
            },
            "resposta_certa": "C"
        },
        {
            "texto": "\n3 - O operador de resto (módulo) retorna 0 para números pares e 1 para ímpares\n",
            "pergunta": " Um fluxograma mostra um processo onde se verifica se um número é par ou ímpar. Se"
                        "for par, exibe ""Par""; caso contrário, exibe ""Ímpar"". Sabendo que a operação de resto (%) entre o"
                        "número e 2 define isso, qual saída será exibida se o número for 7?\n",
            "respostas": {
                "A": "Par",
                "B": "Ímpar",
                "C": "Nenhuma saída",
                "D": "Erro no processo\n"
            },
            "resposta_certa": "B"

        }
    ]
}

def login():
    print("O que deseja fazer?")
    print("[1] Entrar")
    print("[2] Cadastar")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        usuario = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")

        if usuario in usuarios and usuarios[usuario]["senha"] == senha:
            print(f"Bem-vindo, {usuario}!")
            return usuario
        else:
            print("Usuário ou senha incorretos.")
            return login()

    elif opcao == "2":
        usuario = input("Digite seu nome de usuário: ")
        print("A senha deve ter pelo menos 6 caracteres, com número e símbolos.")
        senha = input("Digite sua senha: ")

        if usuario in usuarios:
            print("Usuário já existe.")
            return login()
        else:
            usuarios[usuario] = {
                "senha": senha,
                "pontuacao": {
                    "facil": 0,
                    "medio": 0,
                    "dificil": 0
                },
                "pontuacao_total": 0
            }
            print(f"Usuário {usuario} cadastrado com sucesso!")
            return login()

    else:
        print("Opção inválida.")
        return login()

def pegar_resposta():
    resposta_usuario = input("Digite a letra da sua resposta: \n").upper()

    return resposta_usuario

def jogar_nivel(dificuldade):
    print(f"\n---------------Você está no nível {dificuldade}---------------\n")
    print("- Você tem 3 perguntas para responder.\n")
    print("- Você precisa acertar 2 perguntas para passar para o próximo nível.")

    perguntas_nivel = perguntas[dificuldade]
    pontuacao = 0

    for pergunta in perguntas_nivel:
        print(pergunta["texto"])
        print(pergunta["pergunta"])

        for letra, resposta in pergunta["respostas"].items():
            print(f"{letra}: {resposta}")

        resposta_usuario = pegar_resposta()

        while resposta_usuario not in pergunta["respostas"]:
            print("Resposta inválida. Tente novamente.")
            resposta_usuario = pegar_resposta()

        if resposta_usuario == pergunta["resposta_certa"]:
            pontuacao += 1

    return pontuacao

def jogar(usuario):

    if usuarios[usuario]["pontuacao"]["facil"] < 2:
        dificuldade = "facil"
    elif usuarios[usuario]["pontuacao"]["medio"] < 2:
        dificuldade = "medio"
    elif usuarios[usuario]["pontuacao"]["dificil"] < 2:
        dificuldade = "dificil"
    else:
        print("Parabéns! Você completou todas as dificuldades.")
        print(f"Pontuação total: {usuarios[usuario]['pontuacao_total']}")
        return

    resultado = jogar_nivel(dificuldade)
    usuarios[usuario]["pontuacao"][dificuldade] = resultado

    if (resultado >= 2):
        usuarios[usuario]["pontuacao_total"] += resultado

    jogar(usuario)

def iniciar():
    print("\nBem-vindo ao ByteQuest!\n"
          "\nO Jogo ByteQuest foi desenvolvido para você que tem interesse em aprender lógica de programação, "
          "e tem alguma noção ou quase nenhuma. \n "
          "\n -------------- Regras do Jogo -------------- \n"
          " - Você terá no total 10 perguntas de nível facil, 10 de nível médio e 10 de nivel Dificil;\n"
          " - Cada pergunta tem um texto explicativo, com 4 alternativas;\n"
          " - Cada pergunta contabiliza 1 ponto;\n"
          " - Para avançar o próximo nível você téra que acumular no minimo 8 pontos.\n")
    usuario = login()
    jogar(usuario)

iniciar()
