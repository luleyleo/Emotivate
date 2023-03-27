# The sustAGE off-the-shelf sentiment analysis toolkit

This repository provides an off-the-shelf sentiment analysis API, which can be used to infer whether any input sentence conveys a positive or a negative sentiment. The input sentence should contain at least 3 tokens; otherwise, the API raises an exception.

## General Installation Instructions

### Linux
If you have conda installed (either miniconda or anaconda), you can execute
```bash
conda env create -f .env-ymls/FIPsustAGE.yml
```
to setup the virtual environment required to execute the API. You can activate the `FIPsustAGE` environment with 
```bash
source ./activate FIPsustAGE
```

## Source code
`src` contains the back-end Python scripts of the API, including the tokenization of the input sentence, the extraction of word embeddings, and its analysis using a Hierarchical Contextual Attention neural network. 

## Demonstration
Next, we provide an example on how to execute the provided API inside a Python program.

```python
>>> import module_sentiment as sentiment
>>> sentiment.API('I am meeting with friends in the afternoon and we are going to the cinema')
('positive', '0.739')
```

The first element corresponds to the sentiment inferred by the model (`positive` or `negative`), and the second element indicates the probability score associated to the inference. 

## Citation
If you use the code from this repository, you are kindly asked to cite the following paper.

**[TBD]**

## License
The code and the model weights are released under the MIT License.

## Acknowledgements
The research and development of this toolkit has received funding from the European Union's Horizon 2020 research and innovation programme under grant agreement No. 826506 (sustAGE).
