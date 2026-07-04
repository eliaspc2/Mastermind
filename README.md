# Mastermind

Projeto em Python para uma versão simples do jogo Mastermind.

## Objetivo

O objetivo é adivinhar a sequência secreta de números antes de esgotar as tentativas.

## Como executar

1. Abrir um terminal na pasta do projeto.
2. Executar:

```bash
python main.py
```

## Regras atuais

- A sequência tem por defeito 4 números.
- Os números são gerados aleatoriamente entre 0 e 9.
- Podes repetir números na tentativa.
- Tens 10 tentativas para acertar.

## Estrutura do projeto

Neste momento a app está concentrada num único ficheiro para facilitar o copy-paste e o desenvolvimento inicial.

- `main.py`: contém o menu, a lógica da geração da sequência e a validação das tentativas
- `README.md`: documentação básica do projeto
- `.gitignore`: ficheiros e pastas que não devem ir para o Git

## Como funciona o código

- `RandomOrder`: gera a sequência secreta e compara a tentativa com a solução
- `Menu`: gere o menu inicial, o arranque do jogo e a leitura das tentativas

## Próximos passos sugeridos

1. Separar a lógica do jogo em classes mais específicas
2. Guardar o histórico das tentativas
3. Melhorar as regras do Mastermind para ficarem mais próximas da versão clássica
