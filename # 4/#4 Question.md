# Question

To increase annual revenue, the government has created an IPPE - Written Tax.
A collection of words is monthly disclosed and the real amount charged for its use in
messages. Each written message is then taxed according to the amount of
number of occurrences of each word in the collection, multiplied by the value of the respective
word. But an interim measure adopted shortly thereafter allows recovery to be
made up to, at most, the second use of each word. To the joy of citizens, the third
use is free of charge.

# Input

A entrada é dada por um arquivo binário e um arquivo texto.
O arquivo binário de nome “referencia.bin” é composto por uma sequência de registros formatos
cada um por uma string que ocupa 256 bytes (uma palavra) e um número em ponto flutuante de
precisão dupla (o valor do imposto sobre a respectiva palavra). O fim da sequência de registros
é sinalizado pelo término do arquivo.
O arquivo texto contém a mensagem escrita que será taxada pelo novo importo. O texto nesse
arquivo é composto por múltiplas linhas e as palavras podem aparecer tanto escritas com letras
minúsculas quanto com letras maiúsculas. O nome do arquivo é dado pelo usuário através da
entrada padrão.
As palavras poderão aparecer tanto nos registros do arquivo binário quanto no arquivo texto
com letras maiúsculas quanto com letras minúsculas. Seu programa deverá ser capaz de
identifica-las como iguais, independentes do caso. Ou seja, “Abacaxi”, “abacaxi” e “ABACAXI”
correspondem à mesma palavra. Além disso, o arquivo texto pode incluir pontuação (ponto,
vírgula, etc.), que deverá ser ignorada pelo seu programa. Nenhuma palavra nos arquivos será
acentuada.

# Output

Seu programa deverá emitir um arquivo texto de nome “imposto.txt” com a mensagem
“O imposto cobrado é de R$<VALOR>”, onde <VALOR> deve ser substituído pelo valor total do
imposto cobrado sobre o arquivo texto informado na entrada, com duas casas decimais.

╔════════════╦═══════════════════════════════════════════╦════════════════╦════════════════════╗
║ In         ║ letter.txt                                ║ ref.bin        ║ *Out               ║
║            ║                                           ║                ║ bill.txt           ║
╠════════════╬═══════════════════════════════════════════╬════════════════╬════════════════════╣
║ letter.txt ║ Ola amigo,                                ║ Voce 0.05      ║ "O imposto cobrado ║
║            ║ Quanto tempo! Tudo bem com voce?          ║ Dica 0.75      ║  é de R$4.51"      ║
║            ║ Esses dias lembrei daquela vez que eu,    ║ Obrigado 0.30  ║                    ║
║            ║ voce e Amanda estávamos                   ║ Tempo 1.40     ║                    ║
║            ║ conversando sobre as ADs do CEDERJ.       ║ Tudo 0.01      ║                    ║
║            ║ Voce nos falou para fazer todas as        ║ Abacaxi 0.89   ║                    ║
║            ║ questoes de Fundamentos de Programacao    ║ EU 0.34        ║                    ║
║            ║ e procurar os tutores em caso de          ║ As 0.01        ║                    ║
║            ║ duvida.                                   ║ De 0.02        ║                    ║
║            ║ A dica que voce deu foi muito boa.        ║ Novamente 1.34 ║                    ║
║            ║  Obrigado!                                ║ Caso 0.21      ║                    ║
║            ║ Um abraco, nos veremos novamente no Polo. ║                ║                    ║
╚════════════╩═══════════════════════════════════════════╩════════════════╩════════════════════╝ffffefefefefeffefefefefeffefefef