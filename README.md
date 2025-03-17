
# How to Run AI Voice Agent for Zendalona?




## Run Locally

Clone the project

```bash
  git clone git@github.com:Kitsunnneee/AI-Voice-Agent-for-Zendalona.git
```

Go to the project directory

```bash
  cd <project-directory>
```
Create a new python env and activate

```bash
  python -m venv va
  source va/bin/activate
```
Creating the .env file and adding API Keys
```bash
  vi .env
  #adding api keys
  GROQ_API_KEY=<your-groq-api-key>
  LIVEKIT_API_KEY=<your-livekit-api-key>
  LIVEKIT_API_SECRET=<your-livekit-secret-key>
  LIVEKIT_URL=<your-livekit-url-key>
  CARTESIA_API_KEY=<your-cartesia-api-key>
```
You can get your own api key,secret and url for livekit by going to [livekit cloud](https://cloud.livekit.io/projects/p_5frf69f6z88) and going to api keys section.
For groq and cartesia go to their website and signup and youll get api keys for free trial. I have used those.

Install dependencies

```bash
  pip install -r requirements.txt
```


Run the Livekit Agent (Development)

```bash
  python src.main download-files
  python src.main dev
```
For Testing out the Agent

* Go to [Livekit Playground](https://agents-playground.livekit.io/#cam=1&mic=1&video=1&audio=1&chat=1&theme_color=cyan).
* Install livekit cli following [this](https://github.com/livekit/livekit-cli).
* Run this command
    bash
    ```
    lk token create \                                
  --api-key <you-api-key> --api-secret <you-api-secret> \
  --join --room test_room --identity test_user \
  --valid-for 24h
    ```
    This will generate the livekit token.

* Now add the wss url and token and talk with you agent!




## Information on the Project
File Structure

```bash
├── LICENSE
├── README.md
├── config.py
├── data
│   └── Zendalone.txt
├── main.py
├── rag
│   ├── __init__.py
│   ├── document_processor.py
│   ├── embeddings.py
│   ├── index.py
│   └── retreiver.py
├── requirements.txt
├── storage
│   ├── default__vector_store.json
│   ├── docstore.json
│   ├── graph_store.json
│   ├── image__vector_store.json
│   └── index_store.json
├── utils
│   ├── __init__.py
│   └── helpers.py
└── voice
    ├── __init__.py
    ├── agent.py
    ├── llm.py
    ├── stt.py
    └── tts.py
```






### Documentation

This project is built for creating an AI Voice Assistance for all the products of Zendalona.

The main components for this project is:

* RAG built using llamaindex
* Real time Voice Agent built using [Livekit](https://livekit.io/).

### High-Level Diagram of the Project

![Diagram](https://github.com/Kitsunnneee/AI-Voice-Agent-for-Zendalona/blob/main/assests/Zendalona-RAG.png "High-Level Diagram")



## Further Improvements

* Building a Frontend so that I donot have to rely on their Agent playground.
  The instructions for build a frontend and everything is given [here](https://docs.livekit.io/reference/).
* Integrating Custom Local LLM, TTS and STT instead of relying on API Keys.
  They Have already provided support for local WHisper STT. We can create the local llm and tts integration using their [Base class](https://docs.livekit.io/agents-js/classes/plugins_agents_plugin_openai.TTS.html) implementation.

* Integrating Screen reader for ease of use for specially-abled people. 
* Looking into self hosting a [WebRTC server](https://docs.livekit.io/home/self-hosting/deployment/) so that we don't have to reply on Livekit's Cloud service.
* Creating a auto web scrapper so that we do not have to manually create a document all the time.
## Demo

![Demo]()

