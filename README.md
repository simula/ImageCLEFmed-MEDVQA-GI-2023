# ImageCLEFmed-MEDVQA-GI-2023
Identifying lesions in colonoscopy images is one of the most popular applications of artificial intelligence in medicine. Until now, the research has focused on single-image or video analysis. With this task, we aim at bringing a new aspect to the field by adding multiple modalities to the picture. The main focus of the task will be on visual question answering and visual question generation. The goal is that through the combination of text and image data the output of the analysis gets easier to use by medical experts. The task has three sub-tasks.

For the visual question answering (VQA), the participants need to combine images and text answers to answer the questions.
In the visual question generation (VQG) subtask, the participants are asked to generate text questions from a given image and answer. Example questions for both VQA and VQG: How many polyps are in the image? Are there any polyps in the image? What disease is visible in the image?
The third subtask is the visual location question answering (VLQA), where the participants get an image and a question and are required to answer it by providing a segmentation mask for the image. Example questions are: Where in the image is the polyp? Where in the image is the normal and the diseased part? What part of the image shows normal mucosa?

## Task Descriptions

### Visual question answering (VQA)
The VQA task asks participants to generate text answers given a text question and image pair. For example, we provide an image containing a colon polyp with the following question, "Where in the image is the polyp located?". Here, the answer should be a textual description of where in the image the polyp is located, like upper-left or in the center of the image.

### Visual question generation (VQG)
The VQG task asks participants to generate text questions based on a given text answer and image pair. This task is an inverse of task 1, where instead of generating the answer, we are asking for the question. An example could be given the answer "The image contains a polyp" and an image containing a polyp; the question should be "Does the image contain an abnormality?".

## Visual location question answering (VLQA)
The VLQA task asks participants to segment parts of an image given a text question and image pair. This task differs from task 1 and task 2 as it requires a visual output rather than a textual one. For example, given the question "Where is the abnormality?" and an image containing a polyp, the output should give a segmentation mask covering the polyp in the image.

## Data
The provided data is based on the Hyper Kvasir dataset [datasets.simula.no/hyper-kvasir](datasets.simula.no/hyper-kvasir) with the additional question-and-answer ground truth, which was developed with our medical partners. The data includes images spanning the entire gastrointestinal tract, from mouth to anus, and will include abnormalities, surgical instruments, and normal findings. This includes data from different procedures such as gastroscopy and colonoscopy.

For task 1 (VQA) and task 2 (VQG), we provide at 2,000 image samples. Not all questions will be relevant to the provided image, and we expect the submissions to be able to handle cases where there is no correct answer.

For task 3 (VLQA), we provide 500 images with question and segmentation mask pairs. This part of the data will be based on the segmentation part of HyperKvasir and Kvasir Instrument.

The dataet for both task can be downlaoded below.

* **Development Dataset \[ [Download](https://drive.google.com/file/d/1jTyLWwcHzbLpWjSNwmgiiavXDjuQe5y7/view?usp=sharing) \]**

* **Test Dataset \[ TBA \]**

## Evaluation methodology
For assessing performance the following metrics will be used: F1 score, Accuracy, Recall, MCC, mIOU and Dice coefficient.
More information to be added soon.

## Participant registration
Please refer to the general ImageCLEF registration instructions

## Preliminary Schedule
* 13 February 2023: Release of the training and validation sets
* 1st April 2023: Release of the test sets
* 22 April 2023: Registration closes
* 10 May 2023: Run submission deadline
* 17 May 2023: Release of the processed results by the task organizers
* 5 June 2023: Submission of participant papers [CEUR-WS]
* 23 June 2023: Notification of acceptance
* 7 July 2023: Camera ready copy of participant papers and extended lab overviews [CEUR-WS]
* 18-21 September CLEF Conference

## Organizers

* Steven A. Hicks <steven(at)simula.no>, SimulaMet, Norway
* Michael A. Riegler <michael(at)simula.no>, SimulaMet, Norway
* Vajira Thambawita  <vajira(at)simula.no>, SimulaMet, Norway
* Andrea Storås <andrea(at)simula.no>, SimulaMet, Norway
* Pål Halvorsen <paalh(at)simula.no>, SimulaMet, Norway
* Thomas de Lange <thomas.de.lange(at)gu.se>, Sahlgrenska University Hospital, Sweden
* Nikolaos Papachrysos  <nikolaos.papachrysos(at)vgregion.se>, Sahlgrenska University Hospital, Sweden
* Johanna Schöler  <johanna.scholer(at)vgregion.se>, Sahlgrenska University Hospital, Sweden
* Debesh Jha <debesh.jha(at)northwestern.edu>, Norway & Northwestern University, USA
