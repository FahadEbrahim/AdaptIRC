# eIRC
This repository contains notebooks that replicate the usage of adapters for the task of issue report classification. 

## Dataset
The data used is available at: [NLBSE'24 competition](https://github.com/nlbse2024/issue-report-classification). 

## Requirements
The Python packages required to run the code are listed in [`requirements.txt`](requirements.txt). 

The requirements can easily installed via `pip install -r requirements.txt`. 

For saving the model on Huggingface and for experiment tracking on wandb, you need to have your API keys. 

## Notebooks
The code is simplified and available in several Python Jupyter Notebooks, compatible to run on Google Colab.

| Notebook | Description |
| -------- | ----------- |
| [AdaptIRC_unsplit.ipynb](notebooks/AdaptIRC_Unsplit.ipynb) | This notebook trains adapter per repo and does not split the training data into training and validation. |
| [AdaptIRC_FT.ipynb](notebooks/AdaptIRC_FT.ipynb) | This notebook utilises full fine-tuning if the RoBERTa model.|
| [AdaptIRC_SA.ipynb](notebooks/AdaptIRC_SA.ipynb) | This notebook trains a single adapter for all repositories. |
| [eIRC_Demo.ipynb](notebooks/eIRC_Demo.ipynb) | This notebook shows a demo of the eIRC web application. |

The work during the NLBSE'24 competition is available on another branch at: 
[AdaptIRC](https://github.com/FahadEbrahim/AdaptIRC/tree/NLBSE2024)

## Adapters
The adapters created ara available on the following link: 
[Adapters](https://huggingface.co/models?other=adapterhub%3AIRC_Adapters)

## Results
The JSON format results are avaialble on the results directory at 
[Results](results)


## eIRC Web Application
The adapters created ara available on the following link: 
[eIRC](https://huggingface.co/spaces/buelfhood/eIRC)

## Acknowedgement
This repository used codes of different libraries and other notebooks:
1. [Adapters](https://github.com/adapter-hub/adapters)
2. [Transformers](https://github.com/huggingface/transformers)
3. [NLBSE'2024 competition](https://github.com/nlbse2024/issue-report-classification)
4. [Gradio](https://github.com/gradio-app/gradio)
5. [Huggingface](https://huggingface.co/)

## Citation
The work is based on the NLBSE'24 competition.

```bibtex
@inproceedings{nlbse2024,
  author={Kallis, Rafael and Colavito, Giuseppe and Al-Kaswan, Ali and Pascarella, Luca and Chaparro, Oscar and Rani, Pooja},
  title={The NLBSE'24 Tool Competition},
  booktitle={Proceedings of The 3rd International Workshop on Natural Language-based Software Engineering (NLBSE'24)},
  year={2024}
}
```
It is also an extention of the AdaptIRC model.
```bibtex
@inproceedings{Ebrahim2024FewShot,
  author = {Fahad Ebrahim and Mike Joy},
  title = {Few-Shot Issue Report Classification with Adapters},
  booktitle = {2024 ACM/IEEE International Workshop on NL-based Software Engineering (NLBSE '24)},
  year = {2024},
  month = {April},
  day = {20},
  address = {Lisbon, Portugal},
  publisher = {ACM},
  location = {New York, NY, USA},
  pages = {4},
  numpages = {4},
  doi = {10.1145/3643787.3648039},
  url = {https://doi.org/10.1145/3643787.3648039}
}
```
The Journal will be shared later. 