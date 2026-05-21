## AFD — Simulador de Autômato Finito Determinístico

Projeto desenvolvido para a disciplina de **Linguagens Formais e Autômatos**.  
Simula um Autômato Finito Determinístico (AFD) diretamente no terminal — sem dependências externas, sem interface gráfica, só Python puro.

---

## O que é um AFD?

Um **Autômato Finito Determinístico** é um modelo computacional que lê uma string símbolo por símbolo e decide, ao final, se ela pertence ou não a uma linguagem.

Formalmente, é definido pela quíntupla:

```
M = (Q, Σ, δ, q₀, F)
```

| Componente | Significado |
|---|---|
| `Q` | Conjunto finito de estados |
| `Σ` | Alfabeto (símbolos aceitos) |
| `δ` | Função de transição: `δ(estado, símbolo) -> próximo estado` |
| `q₀` | Estado inicial |
| `F` | Conjunto de estados de aceitação |

---

## Como usar

### Pré-requisitos

- Python 3.x instalado
- Nenhuma biblioteca externa necessária

### Executando

```
python afd.py
```

### Fluxo do programa

O programa guia você passo a passo pelo terminal:

```
1. Informe o alfabeto           →  ex: a, b
2. Informe os estados           →  ex: q0, q1, q2, q3
3. Informe o estado inicial     →  ex: q0
4. Informe os estados finais    →  ex: q1, q3
5. Preencha a tabela de transições (uma por uma)
6. Teste quantas palavras quiser
```

---

## Exemplo de sessão completa

```
=============================================
     AFD - Simulador de Automato Finito
=============================================

Simbolos do alfabeto (ex: a, b): a, b
Conjunto de estados  (ex: q0, q1, q2): q0, q1, q2, q3
Estado inicial: q0
Estados de aceitacao (ex: q1, q3): q1, q3

  Preencha as transicoes:
  f(q0, a) -> q1
  f(q0, b) -> q2
  f(q1, a) -> q2
  f(q1, b) -> q3
  f(q2, a) -> q0
  f(q2, b) -> q3
  f(q3, a) -> q1
  f(q3, b) -> q2

---------------------------------------------
  Tabela de transicoes (Delta):
---------------------------------------------
  Delta(q0, a) : q1
  Delta(q0, b) : q2
  Delta(q1, a) : q2
  Delta(q1, b) : q3
  Delta(q2, a) : q0
  Delta(q2, b) : q3
  Delta(q3, a) : q1
  Delta(q3, b) : q2
---------------------------------------------
  Estado inicial   : q0
  Estados de aceit.: q1, q3
---------------------------------------------

  Automato pronto! Digite palavras para testar.
  (Pressione Enter vazio para sair)

  >> a
  Caminho: q0 -> q1
  Resultado: [ACEITA]

  >> aa
  Caminho: q0 -> q1 -> q2
  Resultado: [REJEITA]

  >> ab
  Caminho: q0 -> q1 -> q3
  Resultado: [ACEITA]

  >> bab
  Caminho: q0 -> q2 -> q0 -> q2
  Resultado: [REJEITA]
```

---

## Estrutura do código

```
afd.py
│
├── ler_lista()                   # lê entrada separada por vírgulas
├── montar_tabela_de_transicoes() # constrói o δ interativamente
├── checar_transicoes()           # valida se os destinos existem em Q
├── rodar_palavra()               # executa a simulação da palavra
└── main()                        # orquestra tudo e loop de testes
```

---

## Casos de teste

| Palavra | Caminho | Resultado |
|---|---|---|
| `a` | q0 → q1 | ✅ ACEITA |
| `b` | q0 → q2 | ❌ REJEITA |
| `ab` | q0 → q1 → q3 | ✅ ACEITA |
| `aa` | q0 → q1 → q2 | ❌ REJEITA |
| `bb` | q0 → q2 → q3 | ✅ ACEITA |
| `aba` | q0 → q1 → q3 → q1 | ✅ ACEITA |
| `bab` | q0 → q2 → q0 → q2 | ❌ REJEITA |
| `abab` | q0 → q1 → q3 → q1 → q3 | ✅ ACEITA |

---

## Estrutura do repositório

```
📁 afd-simulador/
├── afd.py       # código principal
└── README.md    # este arquivo
```

---

## Contexto acadêmico

Desenvolvido como trabalho prático da disciplina de **Linguagens Formais e Autômatos**, abordando os seguintes conceitos:

- Definição formal de um AFD
- Função de transição `δ`
- Estados de aceitação e rejeição
- Simulação de processamento de strings
- Tabela de transições

---

## Autor

Feito por **Vinícius Amâncio Martins Pereira**  
