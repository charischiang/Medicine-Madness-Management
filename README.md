# PROJECT WRITEUP

## Inspiration
1 billion or 15% of the world's population have a (diagnosed) disability. 1 in 4 adults in the United States have multiple chronic illnesses which are often disabling. For individuals over age 65, that number is tripled to 3 quarters of seniors. To add to the overwhelmingness of managing their conditions, the persons with disability or their caregivers often have to take charge of a complicated medication regimen. Each medication comes with its own dosage and intake requirements, as well as multiple warnings or instructions. Furthermore, for persons with disabilities and chronic illnesses, dosages and medications to take can be constantly changing over time or based on the person's current condition. When patients don't stick to their prescribed medicine regimen, they are quickly classified as non compliant and often dismissed. However, a closer look found that 80% of these individuals have 3 or more chronic illnesses and 70% have mental illnesses. 70% also know they need to self-manage their medication to treat or manage their conditions but are unable to do so without assistance.

## What it does
Thus, our **Medicine Madness Management** APP serves to streamline the user's medicine management process. Enabling the user to easily manage their own medicine regimen and increasing their independence as they require less support from their caregiver in this regard. Alternatively, the APP could also be utilised by a caregiver of a person with disability to reduce their already heavy caregiving burden. 

The user can simply use the APP to take or upload a photo of their prescription or doctor's instructions. The APP will then use an AI model to pick out key information such as the medication name, when or how often the medicine should be taken, dosage, and any relevant warnings or instructions such as "do not take on an empty stomach". The user or their care provider has the option to check through and ensure accuracy if they wish. Then, reminders will be scheduled based on the gathered information to alert the user to when they should take each medication along with the appropriate warnings or instructions.

## How to run
  - Run both notebooks to download and build required files
  - Open cmd and key in "python3 flask_web.py"
  - Open http://127.0.0.1:5000/ on webbrowser
  - Upload image of medicine tag and press "upload"

## Tools used
  - Character image recognition - pytesseract
  - Word embeddings robust to frequent character errors- Facebook fasttext 
  - Web API - flask

## Links
  - Video demo: https://youtu.be/ufANbVqQER0
