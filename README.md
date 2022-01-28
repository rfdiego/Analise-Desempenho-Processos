# Análise e Desempenho De Processos

O objetivo do projeto consiste basicamente em realizar o processamento de determinada tarefa (em nosso caso serão cálculos) em diferentes conceitos de programação, obtendo como resultado final o tempo de execução desta tarefa para análise de performance e desempenho.
Serão apresentados 3 cenários:

### Estrutura sequencial
1.	Projeto utilizando a estrutura sequencial de processos:
O projeto utiliza a estrutura sequencial, ou seja, a linha subsequente do bloco de código só será executada após a finalização da linha corrente.

### 2.	Projeto utilizando Threads:
O processo com threads consiste em separar as tarefas do projeto em diversas partes em subprocessos filho, onde é possível compartilhamento da mesma região de memória

### 3.	Projeto utilizando Multi-processing:
O procedimento consiste em separar as tarefas do projeto em diversas partes em PROCESSOS diferentes PARALELAMENTE, onde não é possível compartilhamento da mesma região de memória, mas podendo utilizar os outros núcleos de processamento, melhorando o desempenho do objetivo final.

## Observações:
* Para fins didáticos, será utilizado como parâmetro de cálculo a função que tem a finalidade de verificar se é um número primo dentro de determinado range especificado
* A ideia do projeto não é explicar o funcionamento desta função, e sim o tempo que ela é processada e como podemos otimizar isso através do paralelismo.

