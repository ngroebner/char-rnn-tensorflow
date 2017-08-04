char-rnn-tensorflow-disease-generator
===
Generates new disease names using recurrent neural networks.

Forked from Sherjil Ozair's [char-rnn-tensorflow](https://github.com/sherjilozair/char-rnn-tensorflow) which was in turn inspired by Andrej Karpathy's [char-rnn](https://github.com/karpathy/char-rnn).

## Requirements
- [Tensorflow 1.0](http://www.tensorflow.org)

## Concept
Based on Janelle Shane's use of RNN's to generate new names for multiple types of products (e.g. such as [beer](http://gizmodo.com/weve-run-out-of-beer-names-and-ai-is-here-to-help-1797480178) and [metal bands](http://gizmodo.com/here-s-what-happened-when-computers-tried-naming-metal-1795538443) )
## Basic Usage
Train on a list of ~1000 disease names scraped from the [CDC's Diseases and Conditions](https://www.cdc.gov/diseasesconditions/) page:

python train.py

To sample from a checkpointed model, `python sample.py`.

Here are some of my favorites, trained with a variety of hyperparameters.

- Henorphy Sistes
- Menutinia — see Naspilmonakis Incatinal Proasossa Infection
- fempoora — see Spinges
- Groopent, Health
- perpacter Farterosis
- Imberlossis croubocrocustem frumllossomic viruves
- Angi peli Infection
- Grouplas Disease
- Batobacteria fever (ADm)
- Genis
- Shammition
- Pse pee — see Anisalia virus fervic Fraet. see also Restipatomoficu Infection]
- SkV, Pagillosoma dinease
- Lumphagic tupboclosis (Chorcanc Ercucilation — see Spolirmien-hygina diseasee)
- Vinus and Meat Disease
- Lockworm Virus 
- Deat Lutaticationaty (ILS)
- Group A Disease Toxoravirus Infection
- Ovisal Cancer
- Mydoma Infection
- Mubic Cholepiasis
- Thrhama Disease and Rastric Bats, Cexilness 
- Chronic Caplitimexiosis
- Hebomitis — see B Cromen
- Puping Pumjo Fever
- Fancers Vaccination
- Pulst Epesita Cancer 
- Herpes, Areaterial Death Disorders
- Black Vingilla B disis
- Fengillaris
- Mibringiosis
- Kernectaliticar Disease


And this is raw output from a run of 100 epochs with default parameters:

-  neallobacites
- Dickethir Heatted Hemorrhail fevirus [VRP)
- Varialla Health Pastemia — see Sepsisis — see Harstems and Workforce Development (DPF) [Varichllobkere Infection]
- Perichory Amey Infection]
- Glostrommal Pasinella Infection — see Choluraty Vaccination
- Trictostisis, Fecapleagosy Syndrome (CDR)
- Traumagia Disporla Infection]
- Chickren
- Vaginal and Insatt, humaly Syndrome)
- CEV Infection
- Afrian) Puldobacil-Ascoila — see Emergobenthurita (MAF)
- Asistaphyate Meliotoskis Mancepation
- Orviunlal Resistan

