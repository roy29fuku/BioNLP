CHEMDNER task sample data (Version 25th June 2013)
---------------------------------------------------

1) Annotation Guidelines: chemdner_data_preparation.pdf

This document describes the article selection process as 
well as the annotation guidelines used for the CHEMDNER task.



2) Sample data abstracts: chemdner_sample_abstracts.txt

This file contains a sample set of the plain text input file
of PubMed abstracts for which the annotations were generated.
It is a three tabular separated file containing the following
data:

1- Article identifier (PMID, PubMed identifier)
2- Title of the article
3- Abstract of the article

Note that the training, development and test set will be provided in
essentially the same format.



3) Sample data annotations: chemdner_sample_annotations.txt

This file contains manually generated annotations of chemical entities 
in the same format as will be distributed in case of the training and 
development sets.

It consists in tabular separated fields containing:
1- Article identifier (PMID)
2- Type of text from which the annotation was derived (T: Title, A:Abstract)
3- Start offset
4- End offset
5- Text string of the entity mention
6- Type of chemical entity mention (ABBREVIATION,FAMILY,FORMULA,IDENTIFIERS,MULTIPLE,SYSTEMATIC,TRIVIAL)



4) Sample data Gold Standard file for the Chemical document indexing (CDI) sub-task: chemdner_sample_cdi_gold_standard.txt

Given a set of documents, for this subtask, the participants are asked to return for each of them a ranked list 
of chemical entities described within each of these documents. You are not requested to provide the specific type of
chemical entity class.

It consists in tabular separated fields containing:
1- Article identifier (PMID)
2- Text string of the entity mention

An example is shown below:
596853	14-acetoxycarminomycinone
596853	14-bromcarminomycinone
596853	14-hexa-acetyl-14-oxycarminomycinone
596853	14-oxycarminomycinone


5) Sample data Gold Standard file for the Chemical entity mention recognition (CEM) sub-task: chemdner_sample_cem_gold_standard.txt

Given a set of documents, for this subtask, the participants have to return the start and end indices corresponding to all 
the chemical entities mentioned in this document. You are not requested to provide the specific type of chemical entity class.


It consists in tabular separated fields containing:
1- Article identifier (PMID)
2- Offset string consisting in a triplet joined by the ':' character. You have to provide 
the text type (T: Title, A:Abstract), the start offset and the end offset.


An example is shown below:
6780324	T:24:61
6780324	A:17:21
6780324	A:35:39
6780324	A:49:94


6) BioCreative evaluation library:

bc_evaluation-3.2.tar.gz
bc_evaluation-3.2.zip

These files contain the BioCreative evaluation library scripts. You can also
directly download them from the BioCreative Resources page at:

http://www.biocreative.org/resources/biocreative-ii5/evaluation-library/

This webpage explains in detail how to install the library and how it works. 

For both of the tasks you should use the --INT evaluation option like shown below:

bc-evaluate --INT prediction_file evaluation_file

Example evaluation files for both subtasks were described above (chemdner_sample_cdi_gold_standard.txt for the CDI subtask
and chemdner_sample_cem_gold_standard.txt for the CEM subtask).

7) Prediction format for the CDI subtask
Please make sure that your predictions are compliant with the formatting
information provided for the --INT option of the evaluation library.
(The webpage and the bc-evaluate -h and bc-evaluate -d option provide you 

with more details).
In short you have to provide a tab separated file with:
1- Article identifier
2- The chemical entity mention string
3- The rank of the chemical entity returned for this document

4- A confidence score
Example case:
6780324	LHRH	1	0.9
6780324	FSH	2	0.857142857143
6780324	3H2O	3	0.75
6780324	(Bu)2cAMP	4	0.75
6780324	vitro	5	0.666666666667
6780324	plasminogen	6	0.5

6780324	ethylamide	7	0.5
6780324	beta-3H]testosterone	8	0.5
6780324	NIH-FSH-S13	9	0.5
6780324	D-Ser-(But),6	10	0.5
6780324	4-h	11	0.5
6780324	3-isobutyl-l-methylxanthine	12	0.5
2231607	thymidylate	1	0.666666666667

2231607	acid	2	0.666666666667
2231607	TS	3	0.666666666667

8) Prediction format for the CEM subtask:
Please make sure that your predictions are compliant with the formatting
information provided for the --INT option of the evaluation library.

(The webpage and the bc-evaluate -h and bc-evaluate -d option provide you 
with more details). 

In short you have to provide a tab separated file with:
1- Article identifier (PMID)
2- Offset string consisting in a triplet joined by the ':' character. You have to provide 
the text type (T: Title, A:Abstract), the start offset and the end offset.
3- The rank of the chemical entity returned for this document

4- A confidence score


Example case:
6780324	A:104:107	1	0.5
6780324	A:1136:1147	2	0.5
6780324	A:1497:1500	3	0.5
6780324	A:162:167	4	0.5
6780324	A:17:21	5	0.5
6780324	A:319:330	6	0.5
6780324	A:448:452	7	0.5

6780324	A:461:481	8	0.5
6780324	A:50:63	9	0.5
6780324	A:733:742	10	0.5
6780324	A:757:784	11	0.5
6780324	A:84:94	12	0.5
6780324	T:158:163	13	0.5
2231607	A:1027:1036	1	0.5
2231607	A:114:134	2	0.5
2231607	A:17:26	3	0.5



9) Example predictions and evaluations for the CDI sample data:

CDI example predictions:
chemdner_cdi_prediction_1.txt
chemdner_cdi_prediction_2.txt

Evaluations of these predictions:
chemdner_cdi_prediction_1_EVAL.txt
chemdner_cdi_prediction_2_EVAL.txt

These evaluations were obtained by running the evaluation script. Example:
bc-evaluate --INT chemdner_cdi_prediction_2.txt chemdner_sample_cdi_gold_standard.txt

10) Example predictions and evaluations for the CEM sample data:

CEM example predictions:
chemdner_cem_prediction_1.txt
chemdner_cem_prediction_2.txt

Evaluations of these predictions:
chemdner_cem_prediction_1_EVAL.txt
chemdner_cem_prediction_2_EVAL.txt

These evaluations were obtained by running the evaluation script. Example:
bc-evaluate --INT chemdner_cem_prediction_1.txt chemdner_sample_cem_gold_standard.txt

