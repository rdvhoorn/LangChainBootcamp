# LangChainBootcamp
A repository containing tutorial materials for exploring the library and making quick proof of concepts. Includes an overarching tutorial and starting templates for all main components of LangChain. The purpose of this repository is to get you started with building simple LLM proof of concepts to show to your boss who the actual boss is!


## Getting up and running
Quick reminder for creating a pipenv to get started as fast as possible: 
```bash
python -m venv <dir\name_of_venv>
.\<dir\name_of_venv>\Scripts\activate
pip install -r requirements.txt

// or directly copy paste
python -m venv .\venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

If VS code does not find your interpreter right away, you can now choose your interpreter using:
```
control+shift+p -> command pallete

choose -> Python: select interpreter
       -> Navigate to your environment / Scripts / python.exe
```

Make sure to separately select your interpreter for your notebook environment if this is necessary (i.e. for V.S. code in the top right of your notebook file).