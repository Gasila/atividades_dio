# Desafio Azure Speech Studio e Language Studio

Este repositório contém as anotações e insights adquiridos durante o laboratório prático de Azure Speech Studio e Language Studio. O objetivo principal deste laboratório é aprofundar o uso dessas ferramentas para análise de fala e linguagem natural, e desenvolver soluções baseadas em inteligência artificial para voz e linguagem.

## Objetivo

O objetivo do laboratório é:

- **Praticar e aprofundar o uso das ferramentas Azure Speech Studio e Language Studio.**
- **Desenvolver soluções baseadas em IA focadas na análise de fala e linguagem natural.**
- **Criar um repositório de anotações e insights adquiridos, servindo como material de apoio para estudos e futuras implementações.**

## Ferramentas Usadas

- **Azure Speech Studio:** Utilizado para transformar áudio em texto (Speech-to-Text) e gerar texto falado a partir de texto (Text-to-Speech), além de realizar análise de fala e identificar intenções e entidades.
- **Azure Language Studio:** Usado para análise de linguagem natural (NLU), como extração de sentimentos, análise de tópicos, classificação de texto, entre outros.

## Estrutura do Repositório

Este repositório está organizado da seguinte forma:

- **/notebooks:** Contém os notebooks Jupyter com experimentos práticos utilizando a API de Speech e Language Studio.
- **/scripts:** Scripts de código para automatizar o uso das APIs.
- **/insights:** Arquivo contendo anotações e insights adquiridos durante o laboratório.
- **README.md:** Este arquivo, que descreve o laboratório e organiza o material para estudo.

## Passos Seguidos no Laboratório

1. **Configuração do Ambiente**
   - Criação de uma conta no [Azure](https://azure.microsoft.com/).
   - Criação de serviços no Azure Speech e Language Studio.
   - Obtenção das chaves de API para integração com as ferramentas.

2. **Exploração do Azure Speech Studio**
   - Configuração de Speech-to-Text: Conversão de áudios gravados em texto.
   - Análise de fala: Identificação de características da fala, como velocidade, entonação e volume.
   - Text-to-Speech: Geração de áudio a partir de texto.

3. **Exploração do Azure Language Studio**
   - Análise de Sentimentos: Determinação do sentimento (positivo, negativo, neutro) de textos.
   - Extração de Entidades: Identificação de entidades-chave em textos.
   - Classificação de Texto: Treinamento de modelos para categorizar textos em diferentes classes.
   - Análise de Intenções: Identificação de intenções e classificações de ações a partir de comandos de voz.

4. **Desenvolvimento de Soluções**
   - Aplicação dos conceitos aprendidos para criar soluções como chatbots de voz e análise de feedbacks de usuários.
   - Integração das APIs de Speech e Language Studio com um front-end simples (usando, por exemplo, React ou HTML) para exibir resultados interativos.

5. **Documentação**
   - Criação de um repositório com anotações e insights.
   - Explicação detalhada do processo de implementação de cada funcionalidade.

## Insights Adquiridos

Durante a prática, alguns dos principais insights adquiridos foram:

- **Precisão no Speech-to-Text:** A precisão do reconhecimento de fala pode ser influenciada pela qualidade do áudio e pelo sotaque do locutor. A utilização de modelos personalizados pode melhorar significativamente a precisão em contextos específicos.
- **Análise de Sentimentos:** A ferramenta de análise de sentimentos se mostrou eficaz para entender o feedback de clientes, mas o contexto e a linguagem coloquial podem afetar a precisão da análise.
- **Text-to-Speech:** A funcionalidade Text-to-Speech do Azure oferece uma variedade de vozes e entonações, permitindo criar respostas mais naturais em chatbots de voz.

## Exemplos de Uso

### 1. **Speech-to-Text**
   - Carregar um arquivo de áudio e convertê-lo para texto.
   
   ```python
   import azure.cognitiveservices.speech as speechsdk
   
   speech_config = speechsdk.SpeechConfig(subscription="YOUR_KEY", region="YOUR_REGION")
   audio_config = speechsdk.audio.AudioConfig(filename="path_to_audio.wav")
   speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
   
   result = speech_recognizer.recognize_once()
   
   if result.reason == speechsdk.ResultReason.RecognizedSpeech:
       print("Texto reconhecido: {}".format(result.text))
```
### 2. **Análise de Sentimento**
   - Analisar o sentimento de um texto.

   ```
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint = "YOUR_ENDPOINT"
key = "YOUR_KEY"

client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

document = ["Estou muito feliz com o serviço!"]
sentiment_result = client.analyze_sentiment(documents=document)[0]

print("Sentimento: {}".format(sentiment_result.sentiment))
   ```

## Conclusão
O laboratório proporcionou uma experiência prática valiosa na utilização das ferramentas Azure Speech Studio e Language Studio. Aprendemos a integrar a inteligência artificial em processos de análise de fala e linguagem natural, desenvolvendo soluções mais inteligentes e eficientes para diversas aplicações.

## Referências:
http://learn.microsoft.com/en-us/azure/ai-services/language-service/
https://learn.microsoft.com/en-us/azure/ai-services/speech-service/

# Gabriel Siqueira Lannes - Junho de 2025.
