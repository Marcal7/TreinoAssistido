## ⛹️‍♂️ Trabalho de Biomecânica:

Este projeto nasceu da curiosidade em analisar a biomecânica do basquete, mais especificamente o movimento do salto.  No entanto, devido a algumas limitações, decidimos adaptar o escopo e criar uma ferramenta mais prática para auxiliar no treinamento físico.

###  O que fizemos:
* **Captura de movimentos:** Utilizamos a webcam para gravar os exercícios e extrair os dados dos movimentos.
* **Contagem inteligente:** Desenvolvemos um algoritmo capaz de contar o número de repetições de cada exercício com alta precisão.
* **Registro detalhado:** Os dados coletados são organizados em planilhas Excel, permitindo acompanhar o progresso e identificar áreas para melhoria.

### ️ Tecnologias utilizadas:
* **Python:** Linguagem principal para o desenvolvimento do projeto.
* **OpenCV:** Biblioteca para processamento de imagens e vídeos.
* **MediaPipe:** Framework para desenvolvimento de pipelines de aprendizado de máquina, utilizado para a detecção de poses.
* **Pandas:** Biblioteca para manipulação de dados e criação das planilhas Excel.

###  Próximos passos:
* **Interface gráfica intuitiva:** Desenvolver uma interface gráfica para tornar a ferramenta mais amigável e acessível.
* **Expansão de exercícios:** Adicionar novos exercícios e criar planos de treino personalizados.

###  Registro do exercício:
```python

novo_reg.append({
    "Matricula": matricula,
    "Data": datetime.now().strftime("%Y-%m-%d"),
    "Hora": datetime.now().strftime("%H:%M"),
    "N polichinelos": n_poli,
    "Série de polichinelos": s_poli,
    "N flexão": n_flex,
    "Série de flexão": s_flex,
    "N agacha": n_agacha,
    "Série de agachamento": s_agacha,
    "Descanso": descanso
})
