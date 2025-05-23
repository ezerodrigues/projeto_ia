# 🖐️ Reconhecimento de Mãos com IA

![Licença](https://img.shields.io/badge/Licença-MIT-green)
![Python](https://img.shields.io/badge/Python-3.6+-blue)
![Status](https://img.shields.io/badge/Status-Funcional-success)

## 📋 Descrição do Projeto

Este projeto implementa um sistema de reconhecimento de mãos em tempo real utilizando Inteligência Artificial. Através da webcam, o programa identifica e rastreia as mãos do usuário, marcando os pontos-chave e contornos na imagem.

### 🎯 Funcionalidades

- Detecção de até 4 mãos simultaneamente
- Rastreamento em tempo real
- Identificação de pontos-chave das mãos
- Visualização dos resultados em uma janela interativa

## 🚀 Tecnologias Utilizadas

- **Python**: Linguagem de programação principal
- **OpenCV**: Biblioteca para processamento de imagens e visão computacional
- **MediaPipe**: Framework de ML para detecção de pontos-chave
- **CVZone**: Biblioteca auxiliar para rastreamento de mãos

## 📦 Pré-requisitos

Antes de começar, você precisará ter instalado:

- Python 3.6 ou superior
- Pip (gerenciador de pacotes Python)
- Webcam funcional

## ⚙️ Instalação

1. Clone este repositório:
```bash
git clone https://github.com/ezerodrigues/projeto_ia.git
cd projeto_ia
```

2. Instale as dependências necessárias:
```bash
pip install opencv-python mediapipe cvzone
```

## 🎮 Como Usar

1. Execute o script principal:
```bash
python projeto_ai.py
```

2. Uma janela será aberta mostrando a imagem da webcam com as marcações das mãos detectadas.

3. Para encerrar o programa, pressione qualquer tecla.

## 📊 Parâmetros Configuráveis

O sistema possui parâmetros que podem ser ajustados para diferentes cenários:

```python
rastreador = HandDetector(detectionCon=0.8, maxHands=4)
```

- `detectionCon`: Confiança mínima para detecção (0.0 a 1.0)
- `maxHands`: Número máximo de mãos a serem detectadas

## 🔍 Exemplos de Uso

Este projeto pode ser utilizado em diversas aplicações, como:

- Interfaces de usuário baseadas em gestos
- Jogos interativos controlados por movimentos
- Sistemas de tradução de linguagem de sinais
- Aplicações de realidade aumentada

## 🛠️ Possíveis Melhorias

- Adicionar reconhecimento de gestos específicos
- Implementar contagem de dedos
- Criar interface gráfica mais elaborada
- Salvar vídeos das detecções

## 👨‍💻 Autor

**Eliézer Rodrigues**

- GitHub: [ezerodrigues](https://github.com/ezerodrigues)

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!