# Academic Co-authorship is a Risky Game Simulator
Details about the relevant theory and methods can be found in our [paper](add-here-later).

## Abstract 
Conducting a project with multiple participants is a complex task that involves multiple social, economic, and psychological interactions. Conducting academic research in general and the process of writing an academic manuscript, in particular, is notorious for being challenging to successfully navigate due to the current form of collaboration dynamics common in academia. In this study, we propose a game-theory-based model for a co-authorship writing project in which authors are allowed to raise an ultimatum, blocking the publishment of the manuscript if they do not get more credit for the work. Using the proposed model, we explore the influence of the contribution and utility of publishing the manuscript on the rate one or more authors would gain from raising an ultimatum. Similarly, we show that the project's duration and the current state have a major impact on this rate, as well as the number of authors. In addition, we examine common student-advisor and colleague-colleague co-authorships scenarios. Our model reveals disturbing results and demonstrates that the current, broadly accepted, academic practices for collaborations are designed in a way that stimulates authors to raise an ultimatum and stopped only by their integrity and not by a systematic design. 

## Prerequisites
- Python         3.7
- numpy          1.18.1
- matplotlib     3.2.2
- pandas         1.1.5

These can be found in the **requirements.txt** and easly installed using the "pip install requirements.txt" command in your terminal. 


## Citation

If you use parts of the code in this repository for your own research purposes, please cite:

@article{lazebnik2022,
	title={Academic Co-authorship is a Risky Game},
	author={Lazebnik, T. and Beck, S. and Shami, L.},
	journal={TBD},
	year={2022}
}

## Dependencies

This project uses Python 3.7.
To create a virtual environment and install the project dependencies, you can run the following commands:

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Usage 

1. Clone the repo
2. Install the '**requirements.txt**' file (pip install requirements.txt)
3. Put the relevant data in the "data" folder.
4. Run the '**main.py**' file (python main.py or python3 main.py)
5. Checkout the results in the "results" folder.
